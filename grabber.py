import feedparser
import requests
import os

working_dir = './working'

def dload(url):
    tmp = url.split('/')
    filename = tmp[len(tmp) - 1]

    response = requests.get(url, stream=True)
    with open(os.path.join(working_dir, filename), 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()


def get_latest(feed):
    feed = feedparser.parse(feed)
    if len(feed['items']) > 0:

        #from pprint import pprint
        #pprint(feed['items'][0])

        if 'links' in feed['items'][0]:
            for link in feed['items'][0]['links']:
                if 'type' in link  and 'href' in link:
                    if 'audio' in link['type']:
                        dload(link['href'])
                        return

    print 'Err: no media found'

if __name__ == '__main__':

    statics = ['http://wsdownload.bbc.co.uk/worldservice/css/32mp3/latest/bbcnewssummary.mp3']
    feeds = ['http://www.nhk.or.jp/rj/podcast/rss/english.xml',
        'http://www.cbc.ca/podcasting/includes/wr.xml',
        'http://www.npr.org/rss/podcast.php?id=500005']

    for feed in feeds:
        get_latest(feed)

    for static in statics:
        dload(static)
