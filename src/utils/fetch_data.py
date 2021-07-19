import requests
from .fetch_province import fetch_province
from .fetch_global import fetch_global
from .fetch_timeline import fetch_timeline

def fetch_data():
    # Request html content from Bo Y Te
    response = fetch_html()
    
    res = {}
    res['provinces'] = fetch_province(response)
    res.update(fetch_global(response))
    
    timestamp, content = fetch_timeline(response)
    timeline = {
        'timestamp': timestamp,
        'content': content
    }
    
    return res, timeline


def fetch_html():
    '''
    Fetch latest HTML content from Bo Y Te.
    '''
    # Send a request to Bo Y Te
    response = requests.get('https://ncov.moh.gov.vn/', verify=False).content.decode()
    
    return response
    