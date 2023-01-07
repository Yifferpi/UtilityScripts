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

### generate_pw
Simple script that generates passwords from `/dev/random`.
Supports different charsets.

### jpg2pdf
Takes a jpg and puts enbeds it into a pdf. Some other things like
date or title can be added to the pdf via flags. 
Dependencies: pandoc and its depencencies

### arrange-screens
This is a script to change screen settings on the laptop, abstracting
complicated xrandr commands to arrange multiple screens.

### emlcontactextractor
Given a folder of `.eml` files, parse metadata and dump contact details
into `.csv` file for archiving/safekeeping.

### mkmermaid
Small python script to generate a
[Mermaid Chart](https://mermaid-js.github.io/mermaid/#/README).

### change-performance
Manipulate a linux systems cpu frequency governor.
