Headline News Podcasts
======================

These little scripts will download world headline news podcasts from NHK, the BBC, CBC, and NPR.
The files are then converted to a common bitrate and samplerate (64kbps / 44.1khz) and concatenated
into a single file for easy consumption.


# Requirements:

mp3wrap     http://mp3wrap.sourceforge.net/
libav-tools https://libav.org/
lame        http://lame.sourceforge.net/

# Setup

```
git clone https://github.com/rsalmond/headline_news_podcasts.git
cd headline_news_podcasts
sudo pip install -r requirements.txt
sudo apt-get install mp3wrap libav-tools lame
```

# Usage:

```
$ bash get.sh     
dloading podcasts ...

... < a lot of transcoding output > ...

$ ls final.mp3 -alh
-rw-r--r-- 1 user users 12M Jan  3 18:33 final.mp3
```

# Todo:

  * use a real tempdir for workfiles
  * --help
  * config file for podcast sources
