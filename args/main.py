#!/usr/bin/env python3

import sys
import argparse
from file import readcsv

def cmdline_args():

    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    p.add_argument("-i", "--ifile", help="vstupni soubor")
    p.add_argument("-o", "--ofile", help="vystupni soubor")

    return p.parse_args()

def process_args():
    lines = readcsv(args.ifile)
    for line in lines:
        print(line)
    print(lines)
       

if __name__ == '__main__':

    if sys.version_info < (3, 5, 0):
        sys.stderr.write('You need python 3.5 cd later.\n')
        sys.exit(1)

    #try:
    args = cmdline_args()
    #print(args)
    process_args()
    #except:
    #    print('Try main.py parametr -t')

    print()