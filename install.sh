#! /bin/bash

# set target folder where links should be created
installfolder="/home/$USER/bin"

# Make sure target folder exists
if [ ! -d "$installfolder" ]; then
    echo "'$installfolder' does not exist"
    exit 1
fi
# Make sure target folder is on path
onpath=`echo $PATH | grep -o "$installfolder"`
if [ -d "$installfolder" -a "$onpath" == "" ]; then
    echo "Make sure '$1' is on your execution path"
    exit 1
fi

# Find current path (location of this repo)
path=$(dirname $(readlink -f $0))

function link() {
    if [ -L "$1" ]; then
        echo "symlink $1 exists, overwriting.."
        rm $1
        ln -s $path/$1 $1
    elif [ -f "$1" ]; then
        echo "file with name '$1' already exists, skipping.."
    else
        echo "creating symlink for $1"
        ln -s $path/$1 $1
    fi
}

cd "$installfolder"
link "pdfscrape"
link "gitrepos2push"
link "jpg2pdf"
link "arrange-screens"
link "mkmermaid"
#link "lint_files"
link "check_markdown_links"
link "generate_pw"


