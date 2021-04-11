#! /bin/bash

# Make sure target exists and is on execution path
installfolder="/home/$USER/bin"
onpath=`echo $PATH | grep -o "$installfolder"`
if [-d "$installfolder" -a "$onpath" == "" ]; then
    echo "Make sure '~/bin' is on your execution path"
    exit 1
fi

#find gitrepo path which the skript links to 
path=$(dirname $(readlink -f $0))

cd "$installfolder"
ln -s $path/pdfscrape pdfscrape
ln -s $path/jpg2pdf jpg2pdf
ln -s $path/arrange-screens arrange-screens
ln -s $path/mkmermaid mkmermaid
ln -s $path/genpw genpw



