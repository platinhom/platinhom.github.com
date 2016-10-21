---
layout: post
title: 多种分子文件格式提取原子坐标
date: 2015-06-11 23:16:38
categories: CompCB
tags: Python CompBiol
---
## Extract the coordinates from molecular files.

Extracting the atomic coordinates (X,Y,Z) from molecular files is often performed before we use some program. This script could be used to do so! 

### Python script
Now only support mol2, pdb, pqr   
It's simple to run as:  
`python script.py input.pdb`  
It will give `input_extract.pdb` containing the coordinates.   

~~~~ python
#! /usr/bin/env python
# -*- coding: utf8 -*-
# Author: Platinhom; Last Updated: 2015-06-12

# Extract the coordinates from molecular files.
# Now only support mol2, pdb, pqr

import os,sys

if (__name__ == '__main__'):
    fname=sys.argv[1]
    fnamelist=os.path.splitext(fname)
    fwname=fnamelist[0]+"_extract"+fnamelist[1]
    fr=open(fname)
    fw=open(fwname,'w')
	
	# MOL2 format
    if fnamelist[1].lower()==".mol2":
        print "Processing mol2 file"
        readcord=False
        for line in fr:
            if (line.strip()=="@<TRIPOS>ATOM"):
                readcord=True
                continue
            elif ("@<TRIPOS>" in line.strip()):
                readcord=False
                continue
            if (readcord):
                tmp=line.split()
                fw.write(" ".join(tmp[2:5])+"\n") 
	
	# MOL format
    elif fnamelist[1].lower()==".mol":
        print "Processing mol file,not support now.."

	# PDB format
    elif fnamelist[1].lower()==".pdb":
        print "Processing pdb file"
        readcord=False
        for line in fr:
            if (line[:6]=="REMARK"): continue
            elif (line[:4]=="ATOM" or line[:6]=="HETATM"):
				fw.write(line[30:54]+"\n") #x,y,z
				
	# PQR format
    elif fnamelist[1].lower()==".pqr":
        print "Processing pqr file"
        readcord=False
        for line in fr:
            if (line[:6]=="REMARK"): continue
            elif (line[:4]=="ATOM" or line[:6]=="HETATM"):
                tmp=line.split()
                fw.write(" ".join(tmp[-5:])+"\n")

	# SDF format
    elif fnamelist[1].lower()==".sdf":
        print "Processing sdf file, not support now.."

    fr.close()
    fw.close()
#end main
~~~~


---
