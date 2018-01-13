#!/usr/bin/env python3
### gedcom
###
### Copyright 2017 Mac Radigan
### All Rights Reserved

"""gedcom.py

Usage Statement:

   usage: gedcom [-h] [-v] [-G] [-f] [-o PATH] -f FILE

   arguments:
     -f,--filename FILE        input filename

   optional arguments:
     -h,--help                 show this help message and exit
     -o,--output PATH          output directory
     -G,--debug                debug settings
     -v,--verbose              verbose output to stderr

Example Usage(s):

    ./bin/gedcom <args>

"""

import argparse
#import gedcom
from gedcom import GedcomParser
import re
from sys import stdout

def main(filename, output, verbose, debug):
  '...'
 #parser = gedcom.GedcomParser()
  parser = GedcomParser()
  parser.open(filename)
  pass

if __name__ == '__main__':
 parser = argparse.ArgumentParser(description='...')
 parser.add_argument('-G', '--debug',        action='store_true', dest='debug',        default=False,                      help='debug')
 parser.add_argument('-f', '--file',                              dest='file',         required=True,                      help='input file')
 parser.add_argument('-o', '--output',                            dest='output',       default='./GEDCOM_OUT',             help='output directory')
 parser.add_argument('-v', '--verbose',      action='store_true', dest='verbose',      default=False,                      help='verbose output to stdout')
 args = parser.parse_args()
 main(args.file, args.output, args.verbose, args.debug)

### *EOF*
