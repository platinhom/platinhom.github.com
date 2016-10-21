---
layout: post
title: Amber的top文件中电荷替代
date: 2015-08-03 06:55:27
categories: CompCB
tags: CompBiol MD Python Script
---

有时我们想对动力学的参数文件进行相应电荷的替换,这是曾经帮助Li Han师姐做的电荷替换的脚本, 其需求是将每行一个电荷的文件替换掉top文件中的电荷.


~~~python
#! /usr/bin/env python
# File: ChargeReplaceTop.py
# 
# Replace the charge in the amber top file.
# Charge file should one charge per line!
# Usage: python ChargeReplaceTop.py input.top charge.txt output.top
# Author: Zhixiong Zhao 
# Last update: 2013.6.12

import os,sys

topf=open(sys.argv[1])
chargef=open(sys.argv[2])
outf=open(sys.argv[3],'w')
charges=[]

# Read the charges. One charge per line
for line in chargef:
	tmp=line.strip()
	if len(tmp)>0:
        charges.append(tmp)
print "Num of charges: "+str(len(charges))

# Analyse Amber top file
readtop=False
readflag=False
atomnum=0
fstr=""
atomcount=0
for line in topf:
        if (not readtop): outf.write(line)
        if (line.strip()=="%FLAG POINTERS"):
                readflag=True
                continue
        if (line.strip()=="%FLAG CHARGE"):
                readtop=True
                continue
        if (line.strip()=="%FLAG MASS"):
                outf.write(line)
                readtop=False
				continue
        if ("%FORMAT" in line):
                if (readtop):outf.write(line)
                continue
        if (readflag):
                atomnum=int(line.strip().split()[0])
                readflag=False
                if (atomnum!=len(charges)):
                       print "Error: The atom num not equal to the number of charges!"
                       break
                print "Num of Atoms: "+str(atomnum)
        # Find the charge part.
        if (readtop):
                for i in range(5):
                        fstr=fstr+"%16.8E" % float(charges[atomcount])
                        atomcount+=1
                        if (atomcount==atomnum):break
                fstr=fstr+"\n"
                outf.write(fstr)
                fstr=""
topf.close()
chargef.close()
outf.close()
~~~

python脚本处理电荷替换,格式已采用amber的5E16.8格式.有原子数/电荷数检验.

用法:将脚本拷贝到linux或者在window内用dos命令行: 

`python hanli.py input.top input.charge output.top`

input.top input.charge output.top 分别是输入的top文件,电荷文件(每行一个电荷!)和输出文件.



------
