#! /usr/bin/env python
# -*- coding: utf8 -*-

# Author: Hom, Date: 2015.6.17
# To calculate the coulombic energy from pqr file.
# Usage: python pqr2col.py input.pqr [indi]
# Default interior dielectric is set to 1.

import os,sys
from math import *

if (__name__ == '__main__'):
	if (not(len(sys.argv) == 2 or len(sys.argv) == 3)):
		print "Please assign the pqr file."
		input()
		exit()
	indi=1.0
	if (len(sys.argv) == 3):
		indi=float(sys.argv[2])
	fname=sys.argv[1]
	fnamelist=os.path.splitext(fname)
	fr=open(fname)
	atomlist=[];#[[x,y,z,charge],..]
	for line in fr:
		items=line.split()
		if (items[0]=="ATOM" or items[0]=="HETATM"):
			atomlist.append([items[5],items[6],items[7],items[8]])
	totalatoms=len(atomlist);
	sum=0.0;
	for i in range(totalatoms):
		for j in range(i+1,totalatoms):
			x1=float(atomlist[i][0])
			y1=float(atomlist[i][1])
			z1=float(atomlist[i][2])
			x2=float(atomlist[j][0])
			y2=float(atomlist[j][1])
			z2=float(atomlist[j][2])
			r=sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
			sum=sum+(float(atomlist[i][3])*float(atomlist[j][3])*332.06364261/(r*indi))
	print "Total coulombic energy is "+str(sum)+" kcal/mol"
#end main
