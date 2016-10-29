---
layout: post
title: 利用Amber将Mol2转为PQR
date: 2015-07-11 19:06:39
categories: CompCB
tags: CompBiol Amber Bash
---

## Small molecule to PQR with charge/radius information

需要的是AmberTool软件, [免费下载](http://ambermd.org/). 主要使用[Antechamber](http://ambermd.org/antechamber/ac.html)进行电荷计算和布置原子类型. 只要amber能正常运行,这套流程就能走通. 主要调用下属程序:

- 利用AmberTool的`antechamber`计算电荷和原子类型
- `parmchk`转化为参数文件`frcmod`
- `tlead`使用GAFF力场并加载参数文件后,生成拓扑文件`top`和`crd`坐标文件
- 利用`parmed.py`更改原子半径
- 利用`ambpdb`将amber动力学参数文件输出为pqr文件

起始在antechamber后应该可以自己写脚本加载力场中原子半径等信息,但是上述方法更为自动化简单一些.  

如果需要高级电荷计算如ESP, RESP,则要调用高斯进行,这里当然就不弄了 ╮(╯▽╰)╭ 起始我就是给服务器加个功能罢了.

起始并不需要整套的ambertool, 主要上述文件相关的存在就好了, 文件不齐全跑的时候会报错, 逐个从服务器掉过来就好了~

###### FILE: mol22pqr.sh
~~~bash
#! /bin/bash
# Usage: Change the input molecule to pqr file with vdw radius.
# Input: molecule file in pdb/mol2 format
# Author: Platinhom 2015.7.11
# Use as: ./mol22pqr.sh input.mol2 bcc mbondi
#
# Before use, change the AMBERHOME to your amber directory. And also change the amber.sh to make sure it can run.

if [ -z $1 ];then
echo "Please assign the input file!"
exit
fi

if [ -z $2 ];then
echo "Please assign the charge method! Can be:"
echo "  bcc for AM1-BCC charge"
echo "  mul for Mulliken charge"
echo "  gas for Gasteiger charge"
echo "  cm2, esp, resp charge need more programs.. so don't support here."
exit 
fi

if [ -z $3 ];then
echo "Please assign the vdw radius type of atom! Can be:"
echo "bondi, mbondi(default), mbondi2, mbondi3, amber6.(In amber14)"
exit
fi

#if need changevdw, change value to "True". And change the vdwtype value
changevdw="True"
#vdw Type as: bondi, mbondi(default), mbondi2, mbondi3, amber6.(In amber14)
vdwtype=$3

if [ $changevdw = "True" ];then
echo "It will use $vdwtype method for vdw radiis."
fi

#Setup the amber environment. You should modify by your own environment
if [ -z $AMBERHOME ];then
source /AMBERHOME/amber.sh

fi

basename=${1%.*}
exdname=${1##*.}
if [ $exdname = "mol2" ];then
antechamber -fi mol2 -fo mol2 -pf y -i $1 -c $2 -o ${basename}_gaff.mol2
elif [ $exdname = "pdb" ];then
antechamber -fi pdb -fo mol2 -pf y -i $1 -c $2 -o ${basename}_gaff.mol2
else
echo "Only support for pdb or mol2 files!"
exit
fi

parmchk -i ${basename}_gaff.mol2 -f mol2 -o ${basename}.frcmod
echo "source leaprc.gaff">>${basename}_gaff.leapin
echo "loadamberparams ${basename}.frcmod" >>${basename}_gaff.leapin
echo "hom=loadmol2 ${basename}_gaff.mol2">>${basename}_gaff.leapin
echo "saveamberparm hom ${basename}.top ${basename}.crd">>${basename}_gaff.leapin
echo "quit">>${basename}_gaff.leapin
tleap -f ${basename}_gaff.leapin >/dev/null

#Change the vdw radius by amber sets
####
if [ $changevdw = "True" ];then
echo "changeRadii $vdwtype">>${basename}_gaff.parmedin
echo "outparm ${basename}.top">>${basename}_gaff.parmedin
parmed.py -p ${basename}.top -i ${basename}_gaff.parmedin -O > /dev/null
fi
####

ambpdb -p ${basename}.top -pqr < ${basename}.crd >${basename}.pqr
rm ${basename}_gaff.* sqm.* leap.log
~~~

------
