---
layout: post
title: AMBER:一般动力学流程简介
date: 2015-11-13 11:21:28
categories: CompCB
tags: CompBiol MD
---

Abmber主页 <http://ambermd.org/>, 官方教程 <http://ambermd.org/tutorials/>

[Amber Reference Manuals 参考手册](http://ambermd.org/doc12/), [Amber14手册](http://ambermd.org/doc12/Amber14.pdf), [各版本补丁](http://ambermd.org/bugfixes.html),[archive mailing list](http://archive.ambermd.org/), [AmberTools](http://ambermd.org/#AmberTools)

先了解主要程序组成：

- **sander**: 最主要MD程序，NMR限制条件模拟，replica-exchange 副本交换分子动力学模拟方法 ?，热力学积分TI thermodynamic integration， potential of mean force (PMF) 平均力势等。。
- **LEaP**：生成amber输入top/crd文件的程序, 包括两个版本. **xleap**，具X-windows功能，主要的生成拓扑，坐标，参数等的程序; **tleap**, 更常用命令行版本.
- **pmemd**: 扩展版sander,用于periodic PME simulations,也适用于隐性溶剂 Generalized Born(GB)模拟. 速度更优化, 适合GPU模拟, 但模拟有一定限制.
- **nmode**: 根据1,2阶导数进行Normal mode analysis简正振动分析，用于找最小值,过渡态，局部最优等。
- **gibbs**：程序包含自由能微扰(FEP)和热动力学积分(TI)，还允许平均力势(PMF)的计算。 
- **antechamber**: 用于生成小分子,特殊残基力场GAFF类型, 加电荷等处理.
- **parmchk**: 用于生成小分子缺失力场参数.
- **ambpdb**: 将top+crd文件转为pdb文件.
- **reduce**: 加氢去氢
- **pdb4amber**: 
- **nab**: 核酸构建的程序. amber10之前是[nucgen](http://nucleix.mbu.iisc.ernet.in/nucgen/index.htm).
- **sqm**: 半经验DFTB量化计算程序, 一般不用.
- **parmed.py**: top文件加工, [ref](http://jswails.wikidot.com/parmed), 对应在bin/ParmEd文件夹呢的脚本
- **roar**：进行QM/MM计算，“真正的”Ewald模拟，以及备用的分子动力学积分程序。 
- **ptraj** / cpptraj: 轨迹分析，时间相关的东东如RMSD,H-键，扩散行为等
- **mm_pbsa** / mmpbsa.py：顾名思义，切成各种能量项算自由能，MM-PB/GB-SA

文件类型:

- *prmtop* 或 *top*: parameters topology 拓扑和力场参数,定义了连接啊,参数啊,在MD时是静态不变的.
- *inpcrd* 或 *crd*: input coordinate 具体坐标和速度,周期盒等信息, 也是具体的轨迹数据. 结合top文件导出分子结构。
- *mdin*: md input file, MD动力学模拟参数设置等

## 预处理 

[PDB2PQR server](http://nbcr-222.ucsd.edu/pdb2pqr_2.0.0/)
该服务器能预处理蛋白,比较好。生成的文件改名为pdb即可用，但电荷总和非整数..

标准流程
蛋白预处理:去掉remark,HETATM,每条链后增加TER,根据质子化状态命名HIS,HIE,HID,HIP;根据CYS状态命名CYS,CYX

前处理：包括去除可选构象，去除水附加等等杂物，二硫键CYS->CYX，

awk '$4=="LIG"' 1ODX.pdb > 1ODX_protein.pdb
awk '$4!="LIG"' 1ODX.pdb | awk '$1=="ATOM"' > 1ODX_protein.pdb


### 小分子参数化

主要使用antechamber实现.参考[Amber小分子处理](/2015/11/12/AMBER-Ligand/)以及[antechamber使用](/2015/09/16/antechamber/)

一般计算bcc电荷,用下述命令: 

`antechamber -i  ***.mol2 -fi mol2 -o ***_bcc.mol2 -fo mol2 -c bcc`

小分子加电荷,-i/o 输入输出, -fi/fo 输入输出文件类型, -c 使用电荷 这里用自带的bcc

计算完电荷后,可以产生参数文件(其实可以不用了,可以直接加载mol2文件)

`antechamber -i ***_bcc.mol2 -fi mol2 -o ligand.prep -fo prepi`

然后关键一步, 利用 **parmchk** 产生缺失的力场参数

`parmchk -i ligand.prep -f prepi -o ligand.frcmod`

当分子太大时,parmchk可能会报错: *parmchk the atom number exceeds the MAXATOM*

此时,ligand.frcmod里面没有参数,后面再读入分子时就会无参数.此时处理方法是,先删掉部分常见基团(如异丙基啥的),保存一个新分子(原子数最好在100以内),重新用上述方法处理,获得的frcmod文件代替上述出错空白的frcmod文件.如果分子实在太大...分隔一块块处理吧,再把参数加在一起..

------------

要用高斯来计算ESP/RESP电荷等 (更多参考: [自动计算ESP和RESP电荷(AMBER and G09)](/2015/09/17/AutoCalcRESP/)),用以下指令转为gjf格式: 

`antechamber -i  ***.mol2 -fi mol2 -o ligand.gjf -fo gcrt`

去掉#HF中的`opt`结构优化,然后高斯计算:

`g03 ligand.gjf` (注意,g09要将iop改为iop(6/50=1),否则出错)

计算完后将log文件用于拟合电荷.

`antechamber -i ligand.log -fi gout -o resp.mol2 -fo mol2 -c resp `

------------

#### nucgen 产生核酸结构. (新版已被移除)

因为已被移除, 可以忽略之. 取而代之是nab程序. 只是老版笔记的残留..

`nucgen -O -i nuc.in -o nuc.out -d $AMBERHOME/dat/leap/parm/nucgen.dat -p nuc.pdb`

输入nuc.in, 输出记录文件nuc.out和pdb文件nuc.pdb(居然没有TER信息,仅有A5 T3之类)


## tleap产生动力学输入

#### ambpdb程序
该程序用于将动力学top文件和crd/rst文件转化为pdb/pqr

`ambpdb -p complex.prmtop < complex.rst/inpcrd > polyAT_vac_init_min.pdb`
产生pdb文件 用ambpdb将rst文件或inpcrd文件导入到top文件就可以输出pdb了

~~~bash
tleap -s -f leaprc.ff03
# following is tleap commands
mol = loadpdb protein.pdb
solvatebox mol TIP3PBOX 12.0
charge mol
addions mol Na+ 0
saveamberparm mol protein.prmtop protein.inpcrd
quit

# shell command
ambpdb -p protein.prmtop < protein.inpcrd > protein_solvated.pdb 
~~~

## 设置动力学参数文件



## sander/pmend 动力学模拟

> sander [-O] -i mdin -o mdout -p prmtop -c inpcrd -r restrt [-ref refc] [-x mdcrd] [-v mdvel] [-e mden] [-inf mdinfo]

- **-O** overwrite output file,否则报错; 
- **-i** 输入动力学参数文件mdin,动力学执行过程
- **-o** 对应输出信息文件(不是坐标)
- **-p** 输入的top文件
- **-c** 输入的crd文件
- **-r** 最终的坐标(rst文件, 带速度信息),也可用于重启;
- **-ref** 限制的reference坐标,用回crd就行; 
- **-x** MD过程坐标轨迹记录文件(crd文件)
- -v MD过程速度记录文件;
- -e MD过程能量记录文件;
- -inf 记录每祯能量信息.

mdin：

~~~
Test run 1
 &cntrl
     IMIN = 1, NCYC = 250, MAXCYC = 500, ntb = 0, igb= 0, cut = 12
 /
~~~

`$AMBERHOME/exe/sander -O -i polyAT_vac_init_min.in -o polyAT_vac_init_min.out -c polyAT_vac.inpcrd -p polyAT_vac.prmtop -r polyAT_vac_init_min.rst`

*.rst是最终结果,且是restart point

`sander -O -i polyAT_vac_md1_12Acut.in -o polyAT_vac_md1_12Acut.out -c polyAT_vac_init_min.rst -p polyAT_vac.prmtop -r polyAT_vac_md1_12Acut.rst -x polyAT_vac_md1_12Acut.mdcrd`
开始跑动力学！

~~~bash
mkdir polyAT_vac_md1_12Acut
cd polyAT_vac_md1_12Acut
perl process_mdout.perl ../polyAT_vac_md1_12Acut.out （该脚本在exe文件夹有）
~~~

注意缩进,","分隔各项,可分行可同行; /表示某namelist结束,&起是namelist.
能量优化部分参数
IMIN=0,0为默认的只做动力学;1表示开启能量最小化,不动力学;5为对轨迹构象进行优化,maxcyc=1时可以提取能量信息
NCYC=10, step to turn to  conjugate gradient
MAXCYC=1, 最大优化步数,maxcyc>ncyc表示将进行ncyc步最抖下降再进行共轭梯度


势能函数部分参数:

NTB=1,0::no periodicity is applied and PME is off,1 constant volume,2 constant pressure
IGB=0,GB 隐性模型,0不使用
CUT=8,非键截断

Berendsen法虽然能保证动力学能量在指定温度上，但是不能保证动力学能量是分子的,会导致热溶剂冷溶剂的现象，为此必须要做升温；Langevin体系,如果结果上比较合理,就可以在指定温度直接开始动力学模拟。

sander指令和输入


imin ^0;1 否/是进行能量优化
maxcyc 最大优化步数,默认1
ncyc ntmin=1时，分割最陡和共轭的步数
ntmin 0,^1,2 全套共轭；先最陡再共轭；只进行最陡 

nmropt  ^0,1 否/是进行NMR分析限制(为了后面分时间段)
ntr ^0,1 否/是位置限制
ntwprt=0 默认0,可设N.表示只记录从1-N的原子的信息.
restraint_wt 位置限制权重值kcal/molA^2 (NTR=1)
restraintmask  限制的内容, :1-147,168 对残基限制
ntx ^1,5,7 不读速度;读入速度体积box
irest 


nstlim ^1 步数,总时间nstlim*dt
dt 0.001/0.002 间隔时间ps,用SHAKE时设0.002,否则.001

### sander并行计算

`mpirun -np 32 sander.MPI -O -i prod.in -p protein.prmtop -c protein_equil.rst -o protein_prod.out -r protein_prod.rst -x protein_prod.mdcrd`

### pmend并行计算

## 结果处理分析

ptraj指令输入

~~~bash
# Shell command
ptraj topfile ptraj_input
# ptraj commands in ptraj_input
trajin file [start stop offset] 读入crd文件,后面是处理的轨迹内容,offset间隔
trajout file 
trajout abc.pdb pdb nobox
center :1-341 归中
image center familiar
strip :Na+
strip :WAT    :在WAT前空格后,表示对象归属
rms first out filename time interval mask ||first从第一个读起,out和filename指明输出,time是每个frame的间隔时间,
mask如:1-146@C*,N*,O*,S*,Cl,F,Br,I 蛋白重原子 ; :1-146 蛋白所有残基; CA,C,N 主链
average abc.pdb pdb    
~~~

其他

`process_mdout.perl`  abc.out 处理结果,EPTOT为能量

grace
grace data1,data2.....
输入字符时, \cE，用\C中止,比如要表示 (angstrom^2) 输入 (\cE\C\S2\N) 











 


------
