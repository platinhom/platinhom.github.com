---
layout: post
title: Py脚本:各元素面积计算
date: 2015-09-10 21:03:47
categories: CompCB
tags: Python
---

结合ESES计算总面积, 并进一步归结到原子面积.最后sum出每种元素的面积.

## ESESAtomArea.py

~~~python
#! /usr/bin/env python
# -*- coding: utf8 -*-
# Author: Platinhom; Last Updated: 2015-09-10

# Calculate surface area by MS_Intersection and match the result to the pqr file.
# Only for pqr format.
# python ESESAtomArea.py file.pqr

import os,sys

# Modify the ESES program parameter here. 
# You can modify to command line input parameter as you like
probe=1.4
grid=0.8
buffer=2.0

if (__name__ == '__main__'):
	fname=sys.argv[1]
	fnamelist=os.path.splitext(fname)
	fxyzr=open(fnamelist[0]+".xyzr",'w')
	fr=open(fname)
	inlines=fr.readlines();
	fr.close();

	# All elements/types of input atoms, used in element area summary.
	atomtypes=[];
	# Write out the corresponding xyzr file.
	for line in inlines:
		# Each atom
		if (line[:4]=="ATOM" or line[:6]=="HETATM"):
			# Atom element here
			tmp=line.split();
			element=tmp[-1].upper();
			atomtypes.append(element);
			# Extract x, y, z, r from pqr to xyzr file
			radius="%10.5f" % float(line[62:70].strip());
			xcoor="%10.5f" % float(line[30:38].strip());
			ycoor="%10.5f" % float(line[38:46].strip());
			zcoor="%10.5f" % float(line[46:54].strip());
			xyzrstr=xcoor+ycoor+zcoor+radius+"\n";
			fxyzr.write(xyzrstr);
	fxyzr.close()
	
	# Use external ESES program to generate surface and calculate atom area
	## So you have to put the ESES program in the same directory
	# Output a "partition_area.txt" file saving atom area
	#os.system('./MS_Intersection_Area '+fnamelist[0]+".xyzr "+str(probe)+" "+str(grid)+" "+str(buffer));
	p=os.popen('./MS_Intersection_Area '+fnamelist[0]+".xyzr "+str(probe)+" "+str(grid)+" "+str(buffer),'r')
	totalArea="0"
	totalVolume="0"
	while 1:
		line=p.readline();
		if "area:" in line: totalArea=line.split(':')[1].split()[0]
		if "volume:" in line: totalVolume=line.split(':')[1].split()[0]
		if not line:break

	# Analyze output atom area file
	fa=open("partition_area.txt")
	atomareas=[];# tmp save atom area by atom number
	typedefault=["H","C","N","O","F","S","P","CL"];
	typeareas={"H":0.0,"C":0.0,"N":0.0,"O":0.0,"F":0.0,"S":0.0,"P":0.0,"CL":0.0};
	atomnum=0;
	for line in fa:
		tmp=line.split();
		atomarea="%12.6f" % float(tmp[1]);
		atomareas.append(atomarea);
		atype=atomtypes[atomnum];
		typeareas[atype]=typeareas.setdefault(atype,0.0)+float(tmp[1]);
		atomnum=atomnum+1;
	fa.close()
	
	# Write out pqra file saving atom area
	fwname=fnamelist[0]+"_area.pqra"
	fw=open(fwname,'w')
	
	# Write the total area for each element.
	## Notice that here just write out the default elements.
	## If you want all elements, use "typeused" for iteration.
	typeused=["H","C","N","O","F","S","P","CL"];
	for i in typeareas.iterkeys():
		if i not in typeused:typeused.append(i);
	
	# For print out the atom area summary
	outputelearea=fnamelist[0]+" Areas: "+totalArea+" Volumes: "+totalVolume+" ";
	fw.write("REMARK  AREAS  "+totalArea+"\n");
	fw.write("REMARK  VOLUMES  "+totalVolume+"\n");	

	for element in typedefault:
	# If you want all elements, need to comment the above line and uncomment the following line.
	#for element in typeused:
		fw.write("REMARK  AREA  "+"%2s"%element+"  "+"%20.6f"%typeareas.get(element,0.0)+"\n");
		outputelearea=outputelearea+element+": "+str(typeareas[element])+" ";
	print outputelearea
	
	fr=open(fname)
	atomnum=0;
	for line in fr:
		if (line[:4]=="ATOM" or line[:6]=="HETATM"):
			tmp=line.split();
			element=tmp[-1].upper();
			newline=line.strip('\n')+atomareas[atomnum]+"\n";
			fw.write(newline);
			atomnum=atomnum+1;
		else:
			fw.write(line);
	fr.close();
	fw.close()
#end main			
~~~

------
