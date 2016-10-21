---
layout: post
title: AMBER:小分子处理
date: 2015-11-11 18:58:20
categories: CompCB
tags: CompBiol MD
---

## 基础知识

小分子和蛋白标准残基不同, 形形式式, 所以几乎都没有相关参数. 为了进行动力学模拟, 小分子要进行相关处理获取参数, 才能获取动力学中的力场参数, 包括键长,键常数,夹角和二面角, 电荷, 原子半径等. Amber Tutorials有相关的小分子处理教程[^amberLig], 可以进行参考.

小分子参数化的关键程序是Ambertools里的`antechamber` [^antechamber], [^anteHom], 会自动计算小分子的属性并获得参数. 而`parmchk`程序则可以将具有GAFF力场信息的分子进一步转化为Amber的小分子参数化文件`frcmod`, 具备参数化文件后, 就可以在`tleap`中读取用于参数化小分子, 最后生成amber输入的信息文件`top`文件和坐标文件`crd`文件.

小分子参数化使用的其实是GAFF力场参数(general AMBER force field)[^GAFF]. GAFF是设计来涵盖大部分药物分子的力场参数并且能与Amber力场进行兼容, 使得在动力学中可以使用两种力场进行复合物的模拟. 对于新的配体分子, 其实就是分析结构后利用`parmchk`"套用"GAFF力场参数到该分子中, 而没有的参数则重新参数化, 保存到frcmod文件当中去, 从而使得tleap能顺利读取没有的参数. 

## 预备

这里测试使用Amber14的Ambertool进行. 假设你已经装有Ambertool或Amber了, `source Ambertool/amber.sh` (根据自己电脑情况)来加载amber一些设置, 加载后就可以直接使用amber的程序了(例如ante后tab一下看能不能保全命令). 这里假设都是已经设置好了.

小分子输入文件取于amber tutorial. 可以去下载相应sustiva.pdb/mol2文件, 或者`wget http://ambermd.org/tutorials/basic/tutorial4b/files/sustiva.pdb` (原始pdb),`wget http://ambermd.org/tutorials/basic/tutorial4b/files/sustiva.mol2` (已经经过处理的mol2)获取小分子. 为了通适性, 一般我把小分子配体保存为ligand.mol2, 所以这里也通将分子文件名变为`ligand.mol2`: `mv sustiva.mol2 ligand.mol2`. 或者`ligand.pdb`: `mv sustiva.pdb ligand.pdb`. 

一般情况下, 我们通过第三方软件进行一个预处理获得小分子mol2文件. 也可以直接用pdb文件中提取相应配体分子(没有H). 如果没有氢原子的小分子pdb输入文件, 可以用Ambertool的`reduce`程序([选项](#reduce))来加氢.

`reduce ligand.pdb > ligand_h.pdb`. 检查ligand_h.pdb文件是否有H了. 有的话为了方便, 重命名一下:

`mv ligand.pdb ligand_noh.pdb`  
`mv ligand_h.pdb ligand.pdb`  

好了, 可以继续了.

## antechamber处理

GAFF力场参数的识别主要是靠原子类型实现的, 所以需要对小分子进行分析后设定好gaff原子类型. antechamber就是进行该工作的, 除此以外还能进行电荷的计算或指定. 

- antechamber使用`-at`选项来指定原子类型, 默认是gaff, 所以不用理会(不要乱设就好). 
- `-c`选项则可以指定电荷计算的方法, `-cf`可以指定电荷的文件而不是进行计算. 一般使用bcc电荷就好了(am1-bcc), 也可以使用基于量化计算结果的ESP/RESP电荷(如何计算参考另一篇blog [^CalcRESP] ). 
- `-i`, `-fi`和`-o`, `-fo` 分别是输入文件, 输入文件类型, 输出文件, 输出文件类型. 文件名指定不用说了, 输入文件类型取决于输入文件, 支持类型参见[^anteHom], 输出文件类型取决于parmchk的输入类型, 分别支持`prepi, prepc, ac, mol2`. 一般使用prepi和mol2. 
- `-pf y` 可以忽略计算中产生的中间文件, 墙裂建议!
- `-rn MOL` 可以设置残基名为MOL.默认没有残基名时使用MOL, 否则用原来的.

pdb输入的话:

`antechamber -i ligand.pdb -fi pdb -o ligand_bcc.mol2 -fo mol2 -c bcc -pf y`

mol2输入的话:

`antechamber -i ligand.mol2 -fi mol2 -o ligand_bcc.mol2 -fo mol2 -c bcc -pf y`

要是需要prepi 文件 (prepi和prepc分别是内坐标和卡迪尔坐标系的prep文件, 是以前程序[prep](http://ambermd.org/doc/prep.html)使用的 (现已由leap整合),可由antechamber或prepgen产生, 现常用于非标准残基读入和处理), prepi/prepc文件可以在leap中使用`loadamberprep residue.prep`来读入.

转化上面已经计算了电荷的分子到prep文件:

`antechamber -i ligand_bcc.mol2 -fi mol2 -o ligand.prepi -fo prepi -pf y`

要是使用pdb文件, 要像官网一样将残基名改为SUS, 则可以加多一个`-rn SUS`选项.

这里不像官方教程使用`-s 2`产生中间具体运行信息, 也不产生中间文件. 要有兴趣自行参考官网教程[^amberLig].

如果产生的prepi文件信息,内含缺失部分的信息IMPROPER(这里缺二面角):

> ligand.prepi

~~~
    0    0    2

This is a remark line
molecule.res
SUS   INT  0
CORRECT     OMIT DU   BEG
  0.0000
   1  DUMM  DU    M    0  -1  -2     0.000      .0        .0      .00000
   2  DUMM  DU    M    1   0  -1     1.449      .0        .0      .00000
   3  DUMM  DU    M    2   1   0     1.523   111.21       .0      .00000
   4  Cl    cl    M    3   2   1     1.540   111.208  -180.000 -0.074400
   5  C4    ca    M    4   3   2     1.722   132.004    59.566 -0.017600
   6  C5    ca    B    5   4   3     1.389   119.621  -148.359 -0.053000
   7  C6    ca    E    6   5   4     1.410   118.971   178.924 -0.175300
   8  H5    ha    E    6   5   4     0.970   120.518    -1.051  0.170000
   9  C3    ca    M    5   4   3     1.383   119.376    32.060 -0.068000
  10  H3    ha    E    9   5   4     0.970   119.632    -0.047  0.156000
  11  C2    ca    M    9   5   4     1.410   120.706   179.950 -0.172000
  12  H2    ha    E   11   9   5     0.970   120.541   179.542  0.149000
  13  C1    ca    M   11   9   5     1.417   118.878    -0.465  0.107600
  14  N     n     M   13  11   9     1.430   122.067   179.343 -0.474100
  15  HN    hn    E   14  13  11     0.860   119.015   -26.486  0.356500
  16  C14   c     M   14  13  11     1.378   121.961   153.494  0.843600
  17  O1    o     E   16  14  13     1.184   124.287  -152.739 -0.582500
  18  O2    os    M   16  14  13     1.373   115.898    26.859 -0.378900
  19  C7    c3    M   18  16  14     1.472   123.740     4.314  0.314200
  20  C13   c3    3   19  18  16     1.570   106.682    92.187  0.626900
  21  F1    f     E   20  19  18     1.330   111.794   165.985 -0.224300
  22  F2    f     E   20  19  18     1.335   111.702    46.293 -0.224300
  23  F3    f     E   20  19  18     1.330   112.111   -73.564 -0.224300
  24  C8    c1    M   19  18  16     1.483   107.799  -152.733 -0.204100
  25  C9    c1    M   24  19  18     1.175   179.516   103.650  0.013900
  26  C10   cx    M   25  24  19     1.710   179.457     2.155 -0.082600
  27  H101  hc    E   26  25  24     0.970   105.678    66.683  0.103700
  28  C11   cx    M   26  25  24     1.237   105.832  -145.943 -0.107900
  29  H112  hc    E   28  26  25     0.970   121.218  -150.200  0.081950
  30  H111  hc    E   28  26  25     0.970   121.261   -10.071  0.081950
  31  C12   cx    M   28  26  25     1.283    58.738    99.867 -0.107900
  32  H122  hc    E   31  28  26     0.970   121.212  -109.949  0.081950
  33  H121  hc    E   31  28  26     0.970   121.204   109.905  0.081950


LOOP
   C1   C6
   C7   C6
  C12  C10

IMPROPER
   C5   C3   C4   Cl
   C4   C6   C5   H5
   C7   C1   C6   C5
   C2   C4   C3   H3
   C1   C3   C2   H2
   C2   C6   C1    N
  C14   C1    N   HN
    N   O1  C14   O2

DONE
STOP
~~~

## parmchk处理

parmchk是检查小分子结构在GAFF(默认, 也可以自己指定力场,参见[选项](#parmchk) )下有哪些缺失参数. 找出参数并计算添加相应合适的缺失力场参数. 运行以下命令获得frcmod文件:

`parmchk -i ligand_bcc.mol2 -f mol2 -o ligand.frcmod`

要是有prepi则可以: 

`parmchk -i ligand.prepi -f prepi -o ligand.frcmod`

要是antechamber的输出是ac/prepc可以自行修改相应参数, -i是输入文件,-o输出文件, -f 是输入文件类型.

> ligand.frcmod

~~~
emark goes here
MASS

BOND

ANGLE
c1-c1-cx   56.280     178.460   same as c1-c1-c3
c1-cx-hc   48.250     109.750   same as c1-c3-hc

DIHE

IMPROPER
ca-ca-ca-ha         1.1          180.0         2.0          General improper torsional angle (2 general atom types)
ca-ca-ca-n          1.1          180.0         2.0          Using default value
c -ca-n -hn         1.1          180.0         2.0          General improper torsional angle (2 general atom types)
n -o -c -os        10.5          180.0         2.0          General improper torsional angle (2 general atom types)

NONBON

~~~

Update:

Amber14引入了`parmchk2`, 用法和parmchk 一样. 而parmchk2要比parmchk要好, 因为它将对所有子结构进行搜索打分, 对所有参数比较打分得到其中最适合的参数，而parmchk只是检查其中某几个子结构的参数文件来获取缺失参数.

### 处理综合脚本

上述处理的脚本, 根据文件名后缀判断类型, 第二参数指定电荷类型, 使用类型"no"可使用自带的电荷:

~~~bash
#! /bin/bash
# Author: Hom. 2015.11.12
# Usage: $0 inputfile chargetype
# For: Convert normal molecule file to frcmod and charged input file
 
if [ -z $1 ]; then
echo "No ligand file is assigned!"
exit 1
fi
 
 
if [ -z ${AMBERHOME} ]; then
#echo "The AMBERHOME var or ligand mol2 file is not set! Check it!"
#echo "Use it as './antchm.sh ligand.mol2'"
#exit
 
# If no define AMBERHOME, source the ambertools 
source ~/AmberTools/amber.sh
fi
 
 
chargemode=$2
if [ -z $2 ];then
    chargemode="bcc"
fi
 
basename=${1%.*}
exdname=${1##*.} 
 
if [ $exdname = "pqr" ];then
    cp $1 ${basename}.mpdb
    exdname="mpdb"
fi
 
ligbcc=${basename}_${chargemode}
if [ $chargemode = "no" ];then
    antechamber -i ${1} -fi $exdname -o ${ligbcc}.mol2 -fo mol2 -pf y
else
    antechamber -i ${1} -fi $exdname -o ${ligbcc}.mol2 -fo mol2 -c $chargemode -pf y
fi
 
sleep 1
 
antechamber -i ${ligbcc}.mol2 -fi mol2 -o ${ligbcc}.prepi -fo prepi -pf y
parmchk2 -i ${ligbcc}.prepi -f prepi -o ${ligbcc}.frcmod
 
if [ $exdname = "pqr" ];then
    rm ${basename}.mpdb
fi

rm sqm.*
# cp ${ligbcc}.mol2 ligand.mol2
~~~


## tleap处理

假设有一个处理过的配体分子 ligand.mol2,一个蛋白protein.pdb, 用以下脚本处理即可. 同时生成蛋白,配体,复合物, MD初始状态的结构和top. 这是一个tleap处理的例子. 或者参考官方教程的操作也行.

~~~bash
#!/bin/bash
# This script need 3 arguments:
#   1. ligand input file
#   2. protein input file
#   3. box radius

echo "#############################################################################"
echo "The script help to build a leap.in file and run the tleap for the complex."
echo "First parameter is the ligand file name ABC"
echo "Second is the protein file name"
echo "Third is the radius of TIP3P box."
# echo -n "Enter anything to continue....."
# read
echo "#############################################################################"

if [ -z ${AMBERHOME} ]; then
# echo "ERROR:The AMBERHOME var is not set! Check it!"
# echo "ERROR:Be sure the tleap could be run!"
# exit

# If no define AMBERHOME, source the ambertools 
source ~/AmberTools/amber.sh
fi

ligfile=$1
if [ -z $1 ];then
ligfile="ligand.mol2"
echo "Set ligand file name to default: ligand.mol2"
fi

profile=$2
if [ -z $2 ];then
profile="protein.pdb"
echo "Set protein file name to default: protein.pdb"
fi

boxradius=$3
if [ -z $3 ]; then
boxradius="10"
echo "Set box radius to default: 10"
fi

basename1=${ligfile%.*}
exdname1=`echo "${ligfile##*.}" | tr A-Z a-z`

if [ ! -f ${basename1}.frcmod ];then
echo "No ligand parameters file (ligandfile_prefix.frcmod)!"
exit 1
fi

# other options:
#   loadamberprep ligand.prep
#    list

echo "source leaprc.ff14SB
source leaprc.gaff
loadamberparams frcmod.ionsjc_tip3p
loadamberparams ${basename1}.frcmod
set default PBRadii mbondi2">leap.in

if [ $exdname1 = "mol2" ];then
echo "lig=loadmol2 $ligfile" >>leap.in
# no recommend with pdb file for ligand, no charge
elif [ $exdname1 = "pdb" ];then
echo "lig=loadpdb $ligfile" >>leap.in
fi

echo "check lig
saveamberparm lig lig.top lig.crd
pro=loadpdb $profile
saveamberparm pro pro.top pro.crd
com=combine {pro lig}
saveamberparm com com.top com.crd
check com
addions com Na+ 0
addions com Cl- 0
solvatebox com TIP3PBOX $boxradius
check com
saveamberparm com complex.top complex.crd
quit" >>leap.in

tleap -s -f leap.in
ambpdb -p lig.top < lig.crd > lig.pdb
ambpdb -p pro.top  < pro.crd > pro.pdb
ambpdb -p com.top < com.crd > com.pdb
ambpdb -p complex.top < complex.crd > complex_out.pdb

echo "###############################################################################"
echo "Note: Finish!"
echo "Note: Check the residues num for the restrain in minimization and heat step in MD!"
~~~

## 注意事项

## 附录1: parmchk {#parmchk}

~~~
Usage: parmchk -i input file name
               -o frcmod file name
               -f input file format (prepi, prepc, ac, mol2)
               -p ff parm file
               -pf parm file format
                   1  amber FF data file, the default
                   2  additional force field parameter file (frcmod file)
               -c atom type correspondening file, default is ATCOR.DAT
               -a print out all force field parameters including those in the parmfile
                  can be 'Y' (yes) or 'N' (no) default is 'N'
               -w print out parameters that matching improper dihedral parameters
                  that contain 'X' in the force field parameter file, can be 'Y' (yes)
                  or 'N' (no), default is 'Y'
~~~

## 附录2: reduce程序 {#reduce}

Ambertool中用于加氢(默认),去氢等处理氢的程序.

~~~
reduce: version 3.24 07/24/2013, Copyright 1997-2013, J. Michael Word  
reduce.3.24.130724  
arguments: [-flags] filename or -  

Suggested usage:  
reduce -FLIP myfile.pdb > myfileFH.pdb (do NQH-flips)  
reduce -NOFLIP myfile.pdb > myfileH.pdb (do NOT do NQH-flips)  

Flags:  
-FLIP             add H and rotate and flip NQH groups  
-NOFLIP           add H and rotate groups with no NQH flips  
-Trim             remove (rather than add) hydrogens  

-NOBUILD#.#       build with a given penalty often 200 or 999  
-BUILD            add H, including His sc NH, then rotate and flip groups  
                  (except for pre-existing methionine methyl hydrogens)


-STRING           pass reduce a string object from a script, must be quoted  
usage: from within a script, reduce -STRING "_name_of_string_variable_"  

-Quiet            do not write extra info to the console  
-REFerence        display citation reference  
-Version          display the version of reduce  
-Changes          display the change log  
-Help             the more extensive description of command line arguments 

If you publish work which uses reduce, please cite:
Word, et. al. (1999) J. Mol. Biol. 285, 1735-1747.
For more information see http://kinemage.biochem.duke.edu 
~~~

[^amberLig]: [ANTECHAMBER TUTORIAL](http://ambermd.org/tutorials/basic/tutorial4b/)
[^antechamber]: [Antechamber](http://ambermd.org/antechamber/)
[^anteHom]: [antechamber使用](/2015/09/16/antechamber/)
[^CalcRESP]: [自动计算ESP和RESP电荷(AMBER and G09)](/2015/09/17/AutoCalcRESP/)
[^GAFF]: Wang, J., Wolf, R.M., Caldwell, J.W., Kollman, P.A., Case, D.A. "Development and Testing of a General Amber Force Field", J. Comp. Chem., 2004, 25, 1157 - 1173. [link](http://onlinelibrary.wiley.com/doi/10.1002/jcc.20035/abstract), [paper](http://ambermd.org/antechamber/gaff.pdf)

------
