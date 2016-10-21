#! /usr/bin/env python
# -*- coding: utf8 -*-

# Author: Hom, Date: 2015.6.17
# To extract the information from pqr file to siz and crg files for delphi.
# Usage: python pqr2sizcrg.py input.pqr

import os,sys

if (__name__ == '__main__'):
	if (len(sys.argv)!=2):
		print "Please assign the pqr file."
		input()
		exit()
	fname=sys.argv[1]
	fnamelist=os.path.splitext(fname)
	fcrg=fnamelist[0]+".crg"
	fsiz=fnamelist[0]+".siz"
	fr=open(fname)
	fs=open(fsiz,'w')
	fc=open(fcrg,'w')
	fs.write("!Extract info. from pqr to siz file. By Hom.\n")
	fc.write("!Extract info. from pqr to crg file. By Hom.\n")
	fs.write("atom__resnumbc_radius_\n")
	fc.write("atom__resnumbc_charge_\n")
	for line in fr:
		items=line.split()
		if (items[0]=="ATOM" or items[0]=="HETATM"):
			outline="%-5.5s %-3.3s %-4.4s "%(items[2],items[3],items[4])
			outs=outline+"%-6.6s \n"%items[9]
			outc=outline+"%-6.6s \n"%items[8]
			fs.write(outs)
			fc.write(outc)

#end main
