import requests
import re
import json

highcharts = None

def fetch_province(response):
    '''
    Fetch the latest provincial COVID-19 statistics from Bo Y Te VN.
    Input: HTML content fetched from the web.
    Results are in the following format:
    {
        <hc_key>: {
            'name': name of province, e.g. "Hồ Chí Minh" or "Hải Dương".
            'hc-key': same as <hc_key>. An unique key for the province.
            'value': no. of active cases.
            'socadangdieutri': no. of curing cases.
            'socakhoi': no. of cured cases.
            'socatuvong': deaths.
        },
        <hc_key>: {
            ...
        },
        ...
    }
    '''
    # Fetch json data
    js = fetch_json(response)
    
    global highcharts
    # Fetch provinces info
    if not highcharts:
        highcharts = fetch_highcharts()
    
    # Join data
    js = join_data(js, highcharts)
    
    return js


def fetch_json(response):
    '''
    Fetch latest statistics from html content.
    '''
    # Look for json data hidden in the HTML response
    idx = re.search('var data = \[[^[\]]*\]', response)
    data = response[idx.start() + len('var data = '): idx.end()]
    js = json.loads(data)
    
    # Transpose data for faster lookup
    js = {x['hc-key']:x for x in js}
    return js
    
    
def fetch_highcharts():
    '''
    Fetch metadata for Vietnam's provinces such as hc-key or name.
    '''
    # Fetch Vietnam highcharts data
    data = requests.get('https://ncov.moh.gov.vn/o/corona.trangchu.top/js/vn-all.js', 
                        verify=False).content.decode()
    
    # Locate highcharts data from js source code
    idx = re.search('{', data)
    data = data[idx.start():]
    highcharts = json.loads(data)
    return highcharts


def join_data(js, highcharts):
    '''
    Join fetched JSON data and province name.
    '''
    # Join two fetched items
    for x in highcharts['features']:
        hc_key = x['properties']['hc-key']
        name = x['properties']['name']
        if hc_key in js:
            js[hc_key]['name'] = name
        else:
            print('{} (hc_key = {}) not in json data, skipping...'.format(name, hc_key))
            
    # Check for provinces with missing name and remove them
    missing = [] 
    for hc_key, x in js.items():
        if 'name' not in x:
            print('name not found (hc_key = {})'.format(hc_key))
            missing.append(hc_key)
    for x in missing: js.pop(x)
    
    return js