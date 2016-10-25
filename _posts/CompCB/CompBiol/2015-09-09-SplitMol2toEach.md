---
layout: post
title: Py脚本:分割Mol2文件到每一个小分子
date: 2015-09-08 21:15:29
categories: CompCB
tags: CompBiol Python
---

分割Mol2分子所有小分子到独立文件中,文件名根据分子名(第二行).

以后可以新加功能:

1. 提取指定文件中分子名的mol2分子
2. 批量给分子根据给定文件中名字命名

## SplitMol2.py

~~~python
#! /usr/bin/env python
# -*- coding: utf8 -*-
# Author: Platinhom; Last Updated: 2015-09-09

# Extract each molecule in a big mol2 file.
# Use the molecular name as file name.

import os,sys

if (__name__ == '__main__'):
	fname=sys.argv[1]
	fnamelist=os.path.splitext(fname)
	fwname=fnamelist[0]+"_extract"+fnamelist[1]
	fr=open(fname)
	
	writemol=""
	findmol=False;
	molname="tmp";
	nextmol=False;
	for line in fr:
		if (line.strip() == "@<TRIPOS>MOLECULE"):
			if (nextmol):
				fw=open(molname+".mol2",'w');
				fw.write(writemol);
				fw.close();
			else: nextmol=True;
			writemol=line;
			findmol=True;
			continue;
		if (findmol):
			molname=line.strip();
			findmol=False;
		writemol=writemol+line;
	#write the last molecule
	if(len(writemol)>1):
		fw=open(molname+".mol2",'w');
		fw.write(writemol);
		fw.close();
~~~

------
