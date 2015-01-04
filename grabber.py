"""
A very simple podcast grabber

Usage:
    grabber.py [options]

Options:
    --help
    --dest=<location>   Where to put downloaded files, default is CWD


"""

import feedparser
import requests
from docopt import docopt
import os

def dload(download_dir, url, status=True):
    """ I use this code snippet so often i should submit a pr to requests """
    tmp = url.split('/')
    filename = tmp[len(tmp) - 1]
    if status:
        print 'Downloading {0} to {1}/{2} ...'.format(url, download_dir, filename)
    response = requests.get(url, stream=True)
    with open(os.path.join(download_dir, filename), 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()

def get_latest(download_dir, feed):
    feed = feedparser.parse(feed)
    if len(feed['items']) > 0:
        if 'links' in feed['items'][0]:
            for link in feed['items'][0]['links']:
                if 'type' in link  and 'href' in link:
                    if 'audio' in link['type']:
                        dload(download_dir, link['href'])
                        return

    print 'ERR: no media found'

if __name__ == '__main__':

    arguments = docopt(__doc__, version="Simple Podcast Grabber 0.1")
    dest_dir = arguments['--dest'] or '.'

    statics = ['http://wsdownload.bbc.co.uk/worldservice/css/32mp3/latest/bbcnewssummary.mp3']

    feeds = ['http://www.nhk.or.jp/rj/podcast/rss/english.xml',
        'http://www.cbc.ca/podcasting/includes/wr.xml',
        'http://www.npr.org/rss/podcast.php?id=500005']

    for feed in feeds:
        get_latest(dest_dir, feed)

    for static in statics:
        dload(dest_dir, static)
