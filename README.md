# Collection of Utility Scripts

## Install
There is an install script available, that symlinks all important \
scripts to `~/bin`. Run with
```
./install.sh
```
Make sure `~/bin` is on your execution path.

## Overview of scripts

### pdfscrape
Used mainly to scrape pdf files. Supports
- only downloads changed or inexistent files
- HTTPBasicAuth
- other media formats

### jpg2pdf
Takes a jpg and puts enbeds it into a pdf. Some other things like \
date or title can be added to the pdf via flags.

### arrange-screens
This is a script to change screen settings on the laptop, abstracting \
complicated xrandr commands to arrange multiple screens.
