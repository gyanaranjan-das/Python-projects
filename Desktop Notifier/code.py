import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def loadRSS():
    """
    utility function to lead RSS feed"""

    resp = requests.get(RSS_FEED_URL)

    return resp.content

def parseXML(rss):
    """utility function to parse XML format rss feed"""

    root = ET.fromstring(rss)

    newsitems = []

    for item in root.findall('./channel/item'):
        news = {}

        for child in item:
            if child.tag == '{http://video.search.yahoo.com/mrss}':
                news['media']=child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
                newsitems.append(news)
    return newsitems

def topStories():
    """main function to generate and return news items"""

    rss = loadRSS()

    newsItems = parseXML()
    return newsItems