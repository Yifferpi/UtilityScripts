#! /bin/bash


path=$(dirname $(readlink -f $0))
echo $path

cd /home/$USER/bin

ln -s $path/pdfscrape pdfscrape
ln -s $path/jpg2pdf jpg2pdf
ln -s $path/arrange-screens arrange-screens
ln -s $path/mkmermaid mkmermaid



