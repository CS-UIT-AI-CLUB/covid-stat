import requests
from .fetch_province import fetch_province
from .fetch_global import fetch_global


def fetch_data():
    # Request html content from Bo Y Te
    response = fetch_html()
    
    res = {}
    res['provinces'] = fetch_province(response)
    res.update(fetch_global(response))
    
    return res


def fetch_html():
    '''
    Fetch latest HTML content from Bo Y Te.
    '''
    # Send a request to Bo Y Te
    response = requests.get('https://ncov.moh.gov.vn/', verify=False).content.decode()
    
    return response
    