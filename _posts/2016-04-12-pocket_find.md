---
layout: post
title: 复合物-受体-配体口袋映射
date: 2016-04-11 21:04:08
categories: CompCB
tags: CompBiol
---

工作需要, 指定复合物,受体,配体的pqr文件, 获得每个原子归属(受体?配体?结合口袋?)

难点是判断复合物中原子归属受体?配体? 其实就是快速坐标比较就好了. 先将受体和配体比较,定义出受体的口袋原子/残基. 再将复合物和受体比较. 如果复合物不是等于受体+配体, 还要再加一个判断原子是否配体. 这里偷懒了.

使用就是`python stript.py complex.pqr protein.pqr ligand.pqr [5 [a]]` 第四五参数分别是半径和是否使用邻近残基来定义. 默认半径是5, 默认使用邻近残基.

输出文件是对应每个原子的状态, 蛋白中0代表普通蛋白原子,1代表口袋原子; 复合物中0代表普通蛋白原子,1代表口袋原子,2代表配体原子. 可以加个3代表其他原子

> Update:  
- 支持其余原子,同时输出 `lig.pok`
- 输出到pqrp文件

~~~python
#! /usr/bin/env python

'''Usage:
python stript.py complex.pqr protein.pqr ligand.pqr [5 [a]]
# complex,receptor,ligand pdb/pqr file
# 5: radius for pocket from ligand
# a: Whether to find near residue  
'''

import sys,os

ligfile="lig.pqr"
profile="pro.pqr"
comfile="com.pqr"
if (len(sys.argv)>=4):
	ligfile=sys.argv[1]
	profile=sys.argv[2]
	comfile=sys.argv[3]

if not os.path.exists(ligfile) or not os.path.exists(profile) or not os.path.exists(comfile): 
	print "Plz assign com.pqr pro.pqr lig.pqr"
	sys.exit(1)	

radius=5.0
if (len(sys.argv)>4):
	radius=float(sys.argv[4])

useresidue=True
if (len(sys.argv)>5):
	useresidue=False

def getcoord(line):
	return (float(line[30:38]),float(line[38:46]),float(line[46:54]))

def sameatom(coor1,coor2):
	if (abs(coor1[0]-coor2[0])+abs(coor1[1]-coor2[1])+abs(coor1[2]-coor2[2])<0.05):
		return True
	return False

def nearatom(coor1,coor2,r):
	x=abs(coor1[0]-coor2[0])
	if x>r:return False
	y=abs(coor1[1]-coor2[1])
	if y>r:return False
	z=abs(coor1[2]-coor2[2])
	if z>r:return False
	if (x*x+y*y+z*z>r*r):
		return False
	return True

fc=open(ligfile)
fp=open(profile)
fl=open(comfile)
fclines=fc.readlines()
fc.close()
fplines=fp.readlines()
fp.close()
fllines=fl.readlines()
fl.close()

lp=open("lig.pok",'w')
cp=open("com.pok",'w')
pp=open("pro.pok",'w')

# atom coordinates
lc=[]
pc=[]
cc=[]
for line in fllines:
	if (len(line)>50 and (line[:6]=="ATOM  " or line[:6]=="HETATM")):
		lc.append(getcoord(line))
for line in fplines:
	if (len(line)>50 and (line[:6]=="ATOM  " or line[:6]=="HETATM")):
		pc.append(getcoord(line))
for line in fclines:
	if (len(line)>50 and (line[:6]=="ATOM  " or line[:6]=="HETATM")):
		cc.append(getcoord(line))	

# whether receptor atom in pocket
ppocket=[]
for p in pc:
	ispocket=False
	for l in lc:
		if (nearatom(p,l,radius)):
			ppocket.append(True)
			ispocket=True
			break
	if not ispocket:
		ppocket.append(False)

# Whether to define pocket atoms based on near residue
if (useresidue):
	count=-1
	resn=-1
	lcount=-1
	for line in fplines:
		lcount+=1
		if (len(line)>50 and (line[:6]=="ATOM  " or line[:6]=="HETATM")):
			count+=1
			rn=int(line[22:26].strip())
			if (rn == resn):
				continue
			resn=rn
			pres=False
			reach=0
			# Further check and modify based on residue
			for i in range(100):
				lline=fplines[lcount+i]
				if (len(lline)>50 and (lline[:6]=="ATOM  " or lline[:6]=="HETATM")):
					rn2=int(lline[22:26].strip())
					if rn2 == resn:
						if (not pres and ppocket[count+i]):
							pres=True
					else:

						reach=i
						break
				else:
					reach=i
					break
			if (pres):
				print line[17:20],line[22:26]
				for i in range(reach):
					ppocket[count+i]=1

## Whether complex atom in pocket/receptor/ligand/other(solvent)
## Define atoms in protein(0)/pocket(1)/ligand(2)/other(3)
cpocket=[]
#0:protein,1:pocket,2:ligand,3:other
for c in cc:
	findp=False
	for i in range(len(pc)):
		if (sameatom(c,pc[i])):
			if (ppocket[i]):
				cpocket.append(1)
			else:
				cpocket.append(0)
			findp=True
			break
	if (not findp):
		findl=False
		for j in lc:
			if (sameatom(c,j)):
				cpocket.append(2)
				findl=True
				break
		if (not findl):
			cpocket.append(3)

## Write out results
for l in lc:
	lp.write("2\n")
for c in cpocket:
	cp.write(str(c)+"\n")
for p in ppocket:
	pp.write(str(int(p))+"\n")

lp.close()
cp.close()
pp.close()

## Write out pqrp file
lw=open('lig.pqrp','w')
pw=open('pro.pqrp','w')
cw=open('com.pqrp','w')
for line in fllines:
	if (len(line)>50 and (line[:6]=="ATOM  " or line[:6]=="HETATM")):
		lw.write("%-85s" % line.rstrip('\n')+" "+"%8s"%2+"\n")
	else:
		lw.write(line)
linecount=0		
for line in fplines:
	if (len(line)>50 and (line[:6]=="ATOM  " or line[:6]=="HETATM")):
		pw.write("%-85s" % line.rstrip('\n')+" "+"%8s"%int(ppocket[linecount])+"\n")
		linecount+=1
	else:
		pw.write(line)
linecount=0
for line in fclines:
	if (len(line)>50 and (line[:6]=="ATOM  " or line[:6]=="HETATM")):
		cw.write("%-85s" % line.rstrip('\n')+" "+"%8s"%cpocket[linecount]+"\n")	
		linecount+=1
	else:
		cw.write(line)
lw.close()
cw.close()
pw.close()
~~~

------
