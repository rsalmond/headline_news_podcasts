#!/bin/bash

cmd_exists() {
    hash "$1" > /dev/null 2>&1
}

for cmd in python avconv lame
do
    if ! cmd_exists $cmd; then
        echo "ERR: Can't find $cmd, $0 requires that $cmd is available"
        exit 1
    fi
done

cwd=`pwd`

workdir=`mktemp -d`
mkdir $workdir/out

echo "Downloading podcasts ..."
python grabber.py --dest=$workdir

# normalize bit and sample rates
cd $workdir
for f in *.mp3; do avconv -i $f -b 64k -ar 44100 -c:a pcm_s16le ./out/$f.wav; done

# re encode to mp3
cd out
for f in *.wav; do lame $f $f.mp3; done

# concatenate normalized audio files and move the result to the cwd
cd $workdir/out
for f in *.mp3; do catfiles=$catfiles$f\|; done
avconv -i concat:$catfiles -c:a copy final.mp3

mv final.mp3 $cwd/Daily-Planet-$(date +"%b-%d-%Y").mp3

# tidy up
rm $workdir -rf
