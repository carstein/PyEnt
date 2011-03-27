#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import getopt

import lib.entropy

def print_header():
     print "---------------------------------------------------------------------------------"
     print "PyENT - entropy measurement and graphing tool - version 0.2"
     print "Michal Melewski - <carstein.sec@gmail.com>"
     print "This is a rip-off from Gynvael Coldwind Ent - http://gynvael.coldwind.pl/?id=158"
     print "---------------------------------------------------------------------------------"
     

def PyEnt(filename):
    
    ent = lib.entropy.EntCalc()

    try:
        fh = open(filename, "rb")
        ent.calculate_entropy(fh.read())
        ent.make_image(filename)
        fh.close()
    except IOError:
        print "Usage: %s -f <filename>"%sys.argv[0]
        sys.exit(1)
        

def main():
    print_header()

    short_options = "f:"
    long_options = ['file=']
    filename=""
    
    try:
        opt,args=getopt.getopt(sys.argv[1:],short_options,long_options)
    except:
        print_header()

    for o, ext in opt:
        if o in ("-f","--file"):
            filename=ext
    
    PyEnt(filename)

if __name__ == "__main__":
    sys.exit(main())
