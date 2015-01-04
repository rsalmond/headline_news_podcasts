#!/bin/bash

cmd_exists() {
    hash "$1" > /dev/null 2>&1
}

for cmd in python avconv mp3wrap lame
do
    if ! cmd_exists $cmd; then
        echo "ERR: Can't find $cmd, $0 requires that $cmd is available"
        exit 1
    fi
done

exit 0

# prep work dir 
workdir=`mktemp -d`
mkdir $workdir/out

# get dem podcasts
echo "Downloading podcasts ..."
python grabber.py --dest=$workdir

# normalize bit and sample rates
cd $workdir
for f in *.mp3; do avconv -i $f -b 64k -ar 44100 -c:a pcm_s16le ./out/$f.wav; done

# re encode to mp3
cd out
for f in *.wav; do lame $f $f.mp3; done

# concat
cd $workdir
mp3wrap final.mp3 $workdir/out/*.mp3

# fucking mp3wrap shits on my filenames
mv ./working/final_MP3WRAP.mp3 ./final.mp3
