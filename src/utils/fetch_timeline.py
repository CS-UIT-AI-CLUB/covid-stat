from bs4 import BeautifulSoup
import datetime
import unicodedata

def fetch_timeline(response):
    '''
    Fetch latest COVID-19 news.
    Input: HTML content fetched from the web.
    Return (
        unix_timestamp,
        list of paragraphs (unicode NFKC normalized)
    )
    '''
    soup = BeautifulSoup(response, features="html.parser")
    
    # Fetch latest news
    timeline = soup.find("div", {"class": "timeline-detail"})
    date = timeline.find("div", {"class": "timeline-head"}).text.strip()
    content = timeline.find("div", {"class": "timeline-content"})
    
    # Convert from string to datetime
    date = datetime.datetime.strptime(date, '%H:%M %d/%m/%Y')
    # Convert from UTF+7 to UTC+0
    date = date - datetime.timedelta(hours=7)
    timestamp = date.timestamp()
    
    # Normalize content
    content = unicodedata.normalize('NFKC', content.text).strip()
    # Split lines
    lines = content.splitlines()
    
    return timestamp, lines