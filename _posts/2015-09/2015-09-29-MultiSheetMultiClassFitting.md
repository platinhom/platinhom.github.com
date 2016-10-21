---
layout: post
title: 多表格数据统一进行多类回归拟合参数
date: 2015-09-28 23:02:37
categories: MathStat
tags: Stat Python Excel
---

同时对多种电荷进行类似的拟合, 一个一个复制数据, 很烦. 但每个表格格式基本是一致的. 于是重写了一下多组回归的脚本.

- 在Excel工作薄中有多个工作表, 表明如下的datasheet中所示.
- 新建一个工作表, 其中一列按顺序放如下: training set数据的**行数+1**和**列数+1**,在工作表中绝对位置, 各个工作表名.该列稍下放一个该列名. 例如S列数据为

~~~
394
15
$P$56
BZ2A
MZ2A
GZ2A

S
~~~

假设我需要training复制的数据是393行和14列,位置在每个表的P56.

- 然后利用以下公式: `=IF(MOD(ROW(),$S$1)=1,INDIRECT("$"&$S$8&"$"&(CEILING(ROW()/$S$1,1)+3)),OFFSET(INDIRECT(INDIRECT("$A$"&(CEILING(ROW()/$S$1,1)-1)*$S$1+1)&"!"&$S$3),MOD(ROW()-2,$S$1),MOD(COLUMN()-1,$S$2)))`, 从A1开始拉到N1(14列),然后一直向下拉到合适即可.
	- IF判断是否标题行(用求余),是就写标题,否就写数据.
	- 第一个个indirect是要引用出表格名,`"$"&$S$8&"$"`的表达是方便我插入新列时移位自动修改列名,8是那个S(列名)存的行数.`+3`是因为跳过前三行去读取表名. 
	- OFFSET函数用来定位在相应表格中的数据,这里需要变化表名,数据所在相对位置.
	- `INDIRECT(INDIRECT("$A$"&(CEILING(ROW()/$S$1,1)-1)*$S$1+1)&"!"&$S$3)`中第一个INDIRECT用来定位表名和相应数据起始位置(实际为INDIRECT(表名!$S$3)).第二个INDIRECT用来定位出数据所在的表格名. 
	- `MOD(ROW()-2,$S$1),MOD(COLUMN()-1,$S$2)`用来求余获取相对位置,注意第一个位置偏移是0,0 所以均要-1,行数时要再减标题.
- 利用公式拉出N个表的数据集后,选上这几列, 复制, 粘贴到一个txt文件, 例如叫hello.txt
- 复制下面脚本并保存, 运行`python MultiSheetPara.py hello.txt` 或者直接把数据文件拖到脚本上面即可. 将生产相应表面的文件夹,里面有data.txt文件及结果等.
- 运行后所在文件夹有个totalpar.txt文件. 将内容加载到excel里面,就是所有表格相应的训练参数了~

~~~python
#! /usr/bin/env python
# -*- coding: utf8 -*-
#
# File: MultiSheetPara.py
# Author: Platinhom, 2015.9.29
# Usage: Use a data file as first argument. Data file should have sheet name and data under it.

import os,sys
import numpy as np

datasheet=["BZ2A","MZ2A","GZ2A","SZ2A","EOZ2A","ROZ2A","BOZ2A","MOZ2A","GOZ2A","SOZ2A","EPOZ2A","RPOZ2A","BPOZ2A","MPOZ2A","GPOZ2A","SPOZ2A"]


if (__name__ == '__main__'):
	if (len(sys.argv)!=2):
		print "Please assign the data file as *.txt."
		input()
		exit()
	fname=sys.argv[1]
	fnamelist=os.path.splitext(fname)
	fr=open(fname)
	nowdoing="";
	fw=open(fname);
	for line in fr:
		tmp=line.strip().split()
		if (len(tmp)==0):continue
		if(tmp[0] in datasheet):
			nowdoing=tmp[0];
			if (fw):
				fw.close()
			if (not os.path.exists(nowdoing)):
				os.mkdir(nowdoing);
			fw=open(nowdoing+"/data.txt",'w');
			continue;
		fw.write(line)
	fw.close();
	fr.close();

	# Whether to do for test case
	needtest=False;
	totalpar=open("totalpar.txt",'w');

	for dirname in datasheet:
		fr=open(dirname+"/data.txt")
		fw=open(dirname+"/data2.txt",'w')
		totalpar.write(dirname+"\n");

		for line in fr:
			area=line.split()[2] #area
			if (area!="0"):
				fw.write(line)

		fw.close()
		fr.close()

		dataclass={}
		classlist=[]
		fr=open(dirname+"/data2.txt")
		for line in fr:
			tmp=line.split()
			if (tmp[0] not in dataclass):
				dataclass[tmp[0]]=[]
				classlist.append(tmp[0])
			dataclass[tmp[0]].append(tmp[1:])
		fr.close()

		testin=[]

		if (needtest):
			fr=open(dirname+"/test.txt")
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


		np.savetxt(dirname+'/par.txt',np.array(Tpara))
		np.savetxt(dirname+'/pred.txt',np.array(TPred_Eng))
		np.savetxt(dirname+'/delta.txt',np.array(Tdelta_Eng))
		np.savetxt(dirname+'/rms.txt',np.array(TRMS))

		if (needtest):
			np.savetxt(dirname+'/predTest.txt',np.array(TPred_EngT))
			np.savetxt(dirname+'/deltaTest.txt',np.array(Tdelta_EngT))
			np.savetxt(dirname+'/rmsTest.txt',np.array(TRMST))

		fr=open(dirname+"/par.txt")
		for lline in fr:
			totalpar.write(lline);
		fr.close();
		
	totalpar.close();
~~~

------
