#! /bin/bash


path=$(dirname $(readlink -f $0))
echo $path

cd /home/$USER/bin

ln -s pdfscrape $path/pdfscrape
ln -s jpg2pdf $path/jpg2pdf
ln -s arrange-screens $path/arrange-screens
ln -s mkmermaid $path/mkmermaid



