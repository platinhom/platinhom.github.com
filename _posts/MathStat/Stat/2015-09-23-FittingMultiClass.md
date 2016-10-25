---
layout: post
title: 多组同时Fitting
date: 2015-09-23 05:26:59
categories: MathStat
tags: Stat Python
---

这里加了个预处理,将第三列为空(0)的数据扔掉.类似地可以进行数据预处理.

用法就是数据从Excel复制到data.txt,然后双击这个脚本...出来的par.txt就是参数了.

Enjoy It~

~~~python
#! /usr/bin/env python
# -*- coding: utf8 -*-
# File: TotalPara.py
# Author: Platinhom, 2015.9.23
# Usage: Use data.txt as data file and run this script.

import os,sys
import numpy as np

# Whether to do for test case
needtest=False;

fr=open("data.txt")
fw=open("data2.txt",'w')

for line in fr:
	area=line.split()[2] #area
	if (area!="0"):
		fw.write(line)

fw.close()
fr.close()

dataclass={}
classlist=[]
fr=open("data2.txt")
for line in fr:
	tmp=line.split()
	if (tmp[0] not in dataclass):
		dataclass[tmp[0]]=[]
		classlist.append(tmp[0])
	dataclass[tmp[0]].append(tmp[1:])
fr.close()

testin=[]

if (needtest):
	fr=open("test.txt")
	for line in fr:
		tmp=line.split()
		testin.append(tmp[1:])
	fr.close()

Tpara=[]
TPred_Eng=[]
Tdelta_Eng=[]
TRMS=[]

TparaT=[]
TPred_EngT=[]
Tdelta_EngT=[]
TRMST=[]

for cls in classlist:
	data=np.array(dataclass[cls],dtype=np.float64)
	dlen=data.shape[1]
	# Nonpolar Energy
	E=data[:,0]
	# Train data
	A=data[:,1:dlen] 
	I=np.eye(dlen-1)
	# Parameter
	para=(np.linalg.inv(A.T.dot(A)+500*I)).dot(A.T.dot(E)) #9*1
	
	# Predicted Energy
	Pred_Eng=A.dot(para);
	delta_Eng=E-Pred_Eng;
	RMS=np.sqrt(np.sum((E-Pred_Eng)*(E-Pred_Eng))/len(Pred_Eng))

	# To write out
	Tpara.append([int(cls)]+list(para))
	TPred_Eng+=list(Pred_Eng)
	Tdelta_Eng+=list(delta_Eng)
	TRMS.append(RMS)

	# For test
	if (needtest):
		test=np.array(testin,dtype=np.float64)
		ET=test[:,0];
		AT=test[:,1:dlen];
		Pred_EngT=AT.dot(para);
		delta_EngT=ET-Pred_EngT;
		RMST=np.sqrt(np.sum((ET-Pred_EngT)*(ET-Pred_EngT))/len(Pred_EngT))
		TPred_EngT+=list(Pred_EngT)
		Tdelta_EngT+=list(delta_EngT)
		TRMST.append(RMST)


np.savetxt('par.txt',np.array(Tpara))
np.savetxt('pred.txt',np.array(TPred_Eng))
np.savetxt('delta.txt',np.array(Tdelta_Eng))
np.savetxt('rms.txt',np.array(TRMS))

if (needtest):
	np.savetxt('predTest.txt',np.array(TPred_EngT))
	np.savetxt('deltaTest.txt',np.array(Tdelta_EngT))
	np.savetxt('rmsTest.txt',np.array(TRMST))
~~~

------
