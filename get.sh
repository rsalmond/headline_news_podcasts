#!/bin/bash

# prep work dir 
rm working -rf
mkdir -p working/out

# get dem podcasts
echo "dloading podcasts ..."
python grabber.py

# normalize bit and sample rates
cd working
for f in *.mp3; do avconv -i $f -b 64k -ar 44100 -c:a pcm_s16le ./out/$f.wav; done

# re encode to mp3
cd out
for f in *.wav; do lame $f $f.mp3; done

# concat
cd ../..
mp3wrap ./working/final.mp3 ./working/out/*.mp3

# fucking mp3wrap shits on my filenames
mv ./working/final_MP3WRAP.mp3 ./final.mp3
