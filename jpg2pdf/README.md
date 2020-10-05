
This is a tiny tool, that takes a jpg as an argument and embedds it into a pdf

usage: jpg2pdf [-h] [--nodate] [-o output] [-t title] input [input ...]

positional arguments:
  input       File to be processed

optional arguments:
  -h, --help  show this help message and exit
  --nodate    Omit inserting current date
  -o output   Set the name of the output file, doesn't work with multiple
              files, if not specified, imagename will be used
  -t title    Set a title inside the document

