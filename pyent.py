#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import getopt

import lib.entropy

def print_header():
     print "PyENT - entropy measurement tool"
     print "Michal 'carstein' Melewski"
     print "This is a rip-off from Gynvael Coldwind Ent"

def PyEnt(filename):
    
    ent = entropy.EntCalc()

    try:
        fh = open(filename, "rb")
        ent.calculate_entropy(fh.read())
        fh.close()
    except IOError:
        print("File %s not found"%filename)
        sys.exit(1)
        
    ent.make_image()

def main():
    print_header()

    short_options = "f:"
    long_options = ['file=']
    
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
