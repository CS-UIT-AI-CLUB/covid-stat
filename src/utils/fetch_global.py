from bs4 import BeautifulSoup, NavigableString

def fetch_global(response):
    '''
    Fetch latest COVID-19 statistics of Vietnam and Global.
    Input: HTML content fetched from the web.
    Return JSON in the following format:
    {
        'vietnam': {
            'value': no. of active cases.
            'socadangdieutri': no. of curing cases.
            'socakhoi': no. of cured cases.
            'socatuvong': deaths.
        },
        'global': {
            'value': no. of active cases.
            'socadangdieutri': no. of curing cases.
            'socakhoi': no. of cured cases.
            'socatuvong': deaths.
        },
    }
    '''
    soup = BeautifulSoup(response, features="html.parser")
    res = {}
    
    # Find Vietnam statistic
    root = soup.find_all("span", {"class": "box-vn"})[0].parent
    res['vietnam'] = fetch_stat(root)
    
    # Find Global statistic
    root = soup.find_all("span", {"class": "box-tg"})[0].parent
    res['global'] = fetch_stat(root)
    
    return res
    

def fetch_stat(root):
    '''
    Fetch statistic from a given Soup node.
    '''
    stat = []
    while True:
        root = root.next_sibling
        if not root:
            break
        if isinstance(root, NavigableString):
            continue
        text = root.text.strip()
        if text:
            text = text.split()[-1].replace('.', '')
            stat.append(int(text))
            
    assert len(stat) == 4
    stat = {
        'value': stat[0],
        'socadangdieutri': stat[1],
        'socakhoi': stat[2],
        'socatuvong': stat[3],
    }
    
    return stat