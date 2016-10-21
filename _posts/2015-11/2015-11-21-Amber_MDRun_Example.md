---
layout: post_small
title: Amber MD一些教程
date: 2015-11-21 08:56:24
categories: CompCB
tags: CompBiol MD
---

[原文](http://enzyme.fbb.msu.ru/Tutorials/Tutorial_1/Sec_1.htm)

## System preparation

Let`s consider a protein comprising 500 amino acids that consists of two chains and let's assume that you have obtained its pdb structure from Protein Data Bank. First of all you should remove remarks, connectivity data and HETATM lines except crystallographic water (it's reasonable to include it in model) by some text editor. Then you should add TER card between protein chains. Optionally you could set protonation state of some histidines by editing residue name HIS to HIE, HID or HIP.

Now you're ready to launch tleap program that is a part of AmberTools package. It serves to produce files for calculation.

`tleap -s -f leaprc.ff99SB`

You can see that it tells tleap to load ff99SB force field that is appropriate for our purpose. Now you can load your protein structure into tleap creating object named mol:

>\> mol = loadpdb protein.pdb  
This will add hydrogens to your structure. Now create 12 angstrom layer of TIP3P water around the protein:

>\> solvatebox mol TIP3PBOX 12.0  
You can check system charge:

>\> charge mol  
And then you should add counterions (Na+ or Cl-) to neutralize the system:

>\> addions mol Na+ 0  
Final step is to create prmtop and inpcrd files:

>\> saveamberparm mol protein.prmtop protein.inpcrd  
>\> quit  

File protein.prmtop contains molecular topology, force field parameters, atom and residue names. File protein.inpcrd contains initial coordinates. You could convert prmtop and inpcrd files into pdb format by ambpdb to visualise obtained system:

`ambpdb -p protein.prmtop < protein.inpcrd > protein_solvated.pdb`

## Energy minimization

We will run two stage energy minimization of our system. In the first stage we will minimize water positions keeping protein fixed. And in the second stage the whole system will be minimized. You should use control data files min1.in and min2.in when running sander (program which carries out energy minimization and molecular dynamics).

### Here is the min1.in:

~~~
energy minimization stage 1
 &cntrl
  imin=1, maxcyc=5000, ncyc=2500,
  cut=10.0, ntb=1,
  ntc=1, ntf=1,
  ntpr=10,
  ntr=1,
  restraintmask=':1-500',
  restraint_wt=2.0
 /
~~~

Information in the input file: 

- imin=1  perform minimization 
- maxcyc=5000  maximum number of minimization cycles 
- ncyc=2500  method of minimization will be switched from steepest descent to conjugate gradient after ncyc cycles 
- cut=10.0  specify the nonbonded cutoff, in Angstroms 
- ntb=1  periodic boundary, constant volume 
- ntc=1  SHAKE is not performed (for better energy convergence) 
- ntf=1  force evaluation, complete interaction is calculated 
- ntpr=10  every ntpr steps energy information will be printed in human-readable form to mdout file 
- ntr=1  flag for restraining specified atoms using harmonic potential 
- restraintmask=':1-500'  string that specifies the restrained residues 
- restraint_wt=2.0  the weight (in kcal/mol-A^2) for the positional restraints

So, run sander to perform minimization stage 1:

`sander -O -i min1.in -p protein.prmtop -c protein.inpcrd -o protein_min1.out -r protein_min1.rst -ref protein.inpcrd`

File usage: 

- mdin  control data for the min/md run 
- prmtop  molecular topology, force field, atom and residue names 
- inpcrd  initial coordinates 
- mdout  user readable state info and diagnostics 
- rstrt  final coordinates and velocities 
- refc  reference coords for position restraints

### Here is the min2.in:

~~~
energy minimization stage 2
 &cntrl
  imin=1, maxcyc=10000, ncyc=5000,
  cut=10.0, ntb=1,
  ntc=1, ntf=1,
  ntpr=10,
 /
~~~

Use min2.in and protein_min1.rst to run minimization stage 2:

`sander -O -i min2.in -p protein.prmtop -c protein_min1.rst -o protein_min2.out -r protein_min2.rst`

## Heating

Now we will allow the system to heat up from 0 K to 300 K running 50 ps molecular dynamics with position restraints at constant volume. 

Here is the heat.in:

~~~
heating
 &cntrl
  imin=0,irest=0,ntx=1,
  nstlim=25000,dt=0.002,
  ntc=2,ntf=2,
  cut=10.0, ntb=1,
  ntpr=500, ntwx=500,
  ntt=3, gamma_ln=2.0,
  tempi=0.0, temp0=300.0,
  ntr=1, restraintmask=':1-500',
  restraint_wt=1.0,
  nmropt=1
 /
 &wt TYPE='TEMP0', istep1=0, istep2=25000,
  value1=0.1, value2=300.0, /
 &wt TYPE='END' /
~~~

Information in the input file: 

- imin=0  do molecular dynamics 
- irest=0  flag to restart the run, no effect 
- ntx=1  no initial velocity information 
- nstlim=25000  number of MD-steps to be performed 
- dt=0.002  time step (psec) 
- ntc=2  flag for SHAKE, bonds involving hydrogen are constrained 
- ntf=2  force evaluation, bond interactions involving H-atoms omitted 
- ntwx=500  every ntwx steps the coordinates will be written to mdcrd file 
- ntt=3  use Langevin thermostat 
- gamma_ln=2.0  collision frequency in temperature regulation 
- tempi=0.0  initial temperature 
- temp0=300.0  reference temperature 
- nmropt=1  varying conditions 
- TYPE='TEMP0'  varies the target temperature 
- istep1=0, istep2=25000  change is applied over steps istep1 through istep2 
- value1=0.1, value2=300.0  values of the change corresponding to istep1 and istep2, respectively

So, run sander to perform heating and use files heat.in and protein_min2.rst:

`sander -O -i heat.in -p protein.prmtop -c protein_min2.rst -o protein_heat.out -r protein_heat.rst -x protein_heat.mdcrd -ref protein_min2.rst`

File mdcrd contains coordinate sets saved over trajectory.

## Equilibration

To equilibrate the system before production dynamics we will run 500 ps molecular dynamics without positional restraints at constant pressure. 

Here is the equil.in:

~~~
equilibration
 &cntrl
  imin=0, irest=1, ntx=5,
  nstlim=250000, dt=0.002,
  ntc=2, ntf=2,
  cut=10.0, ntb=2, ntp=1, taup=2.0,
  ntpr=500, ntwx=500, ntwr=5000,
  ntt=3, gamma_ln=2.0,
  temp0=300.0,
 /
~~~

Information in the input file: 
- irest=1, ntx=5  restart calculation, requires velocities in coordinate input file 
- ntb=2  periodic boundary, constant pressure 
- ntp=1  flag for constant pressure dynamics, md with isotropic position scaling 
- taup=2.0  pressure relaxation time (in ps) 
- ntwr=5000  every ntwr steps during dynamics, the restrt file will be written, ensuring that recovery from a crash will not be so painful

Use equil.in and protein_heat.rst to run equilibration:

`sander -O -i equil.in -p protein.prmtop -c protein_heat.rst -o protein_equil.out -r protein_equil.rst -x protein_equil.mdcrd`

## Production dynamics

Now you're ready to run 10 ns production dynamics at constant pressure. Otained trajectory could be used to analyse system properties you want. 

Here is the prod.in:

~~~
production dynamics
 &cntrl
  imin=0, irest=1, ntx=5,
  nstlim=5000000, dt=0.002,
  ntc=2, ntf=2,
  cut=10.0, ntb=2, ntp=1, taup=2.0,
  ntpr=1000, ntwx=1000, ntwr=50000,
  ntt=3, gamma_ln=2.0,
  temp0=300.0,
 /
~~~

You could notice that prod.in differs from equil.in only in nstlim, ntpr, ntwx, and ntwr values. 
When you have to perform five million MD-steps it`s reasonble to run parallel version of sander on some computer cluster by command like this:

`mpirun -np 32 sander.MPI -O -i prod.in -p protein.prmtop -c protein_equil.rst -o protein_prod.out -r protein_prod.rst -x protein_prod.mdcrd`

You could process and analyse obtained trajectory by ptraj program from AmberTools package and visualize it by VMD.


amber 动力学过程：

1、选择力场 tleap -s -f $AMBERHOME/dat/leap/cmd/leaprc.ff99

2、导入晶体结构 model=loadpdb "sbp_lin.pdb"

保存crd和top文件 saveamberparm model polyAT_vac.top polyAT_vac.crd

此时注意电荷是否平衡：

如果缺正电荷 addions model Na+ 0 负离子就用Cl-

 选择水箱 solvateoct model TIP3PBOX 8.0

3、保存crd和top文件 saveamberparm model model_wat.top model_wat.crd

4、退出tleap quit

5、保存新的pdb ambpdb -p model_wat.top <> model2.pdb

6、溶剂环境能量最优化。这一步保持溶质（蛋白）不变，去除溶剂中能量不正常的范德华相互作用。

该步骤的配置文件min1.in如下：

---------------------------------------------------------------------

oxytocin: initial minimisation solvent + ions ##说明信息######

&cntrl ##模拟参数起始

imin = 1, ##任务是优化，0 是分子动力学

cut = 10 ##非键相互作用的截断值为10 挨

ntb = 1, ##周期边界条件 0 不采用；1 定容 ；2 定压

maxcyc = 4000, ##优化步数

ntr = 1, ##优化时需要一些约束原子 -ref

ncyc = 2000, ##前2000最陡下降，后面步骤共轭梯度

/

Hold the protein fixed ##约束说明

500.0 ##作用在肽键上的力 kcal/mol

RES 1 9 ##限制的残基序号 同restrain=’:1-9’

END

END

------------------------------------------------------------------------------

任务命令：如果

 sander -O -i min1.in -p model_wat.top -c model_wat.crd -o min1.out -r min1.rst –ref model_wat.crd &

7、对蛋白进行优化，min2.in文件将min1.in中的限制原子修改，限制水的位置。

也可以考虑利用restrainmask=’:1-9@CA,N,C’约束蛋白主链上的原子。

sander -O -i min2.in -p model_wat.top -c min1.rst -o min2.out -r min2.rst&

8、整体的优化,去掉限制条件

sander -O -i min3.in -p model_wat.top -c min2.rst -o min3.out -r min3.rst &


9、有限制的分子动力学

 第一步分子动力学保持蛋白分子位置不变，但是不是完全固定每个原子，同时缓解蛋白分子周围的水分子，是溶剂环境能量优化。在这个步骤中，我们将主要目的是对特定的原子使用作用力使其能量优化。

 Eq1.in 如下：

fix protein ,relax H2O

&cntrl

nstlim=25000, dt=0.002, ntx=1, irest=0, ntpr=500, ntwr=500,ntwx=500,

tempi=0.0,temp0=300,ntt=3, gamma_ln=1.0,

ntb=1, ntp=0,

nrespa=1,

cut = 10,

ntc=2,ntf=2,

NTR=1,

/

fix protein and HEM

10

RES 1 284

END

END

-----------------------------

nstlim = #：＃表示计算的步数。dt = 0.002：表示步长，单位为ps，0.002表示2fs。ntx=1 irest=0 默认 ntb = 1：表示分子动力学过程保持体积固定。

imin = 0：表示模拟过程为分子动力学，不是能量最优化。

temp0 = 300：表示最后系统到达并保持的温度，单位为K。

tempi = 100：系统开始时的温度。 ntc=2,ntf=2 忽略氢键

gamma_ln = 1：表示当ntt＝3时的碰撞频率，单位为ps-1（请参考AMBER手册）

ntt = 3：温度转变控制，3表示使用兰格氏动力学。

 sander -O -i eq1.in -p model_wat.top -c min3.rst -o eq1.out -r eq1.rst -ref min3.rst -x eq1.mdcrd


11整系统分子动力学模拟: eq2

-------------------------------------------------

 f2:500ps MD

&cntrl

 imin = 0, irest=1, ntx=5,

 ntb=2, pres0 = 1.0, ntp=1,

 taup = 2.0, ntc=2, ntf=2,

 cut = 10, ntr = 0,

 ntt = 3, gamma_ln = 1.0,

 tempi = 300.0 , temp0 = 300.0

 nstlim=500000, dt=0.002,

 ntpr=500, ntwr=500, ntwx=500

/

----------------------------------------------------------

ntb=2：表示分子动力学过程的压力常数。Pres0＝1：引用1个单位的压强。

ntp＝1：表示系统动力学过程各向同性。taup = 2.0：压力缓解时间，单位为ps。

使用以下命令进行MD：

sander -O -i eq2.in -p model_wat.top -c eq1.rst -o eq2.out -r eq2.rst -x eq2.mdcrd -ref eq1.rst &

结果处理：

在动力学过程中，将会产生 .rst 和.mdrcd 文件（需要的），由于crd文件很多，可以将其压缩成.gz 文件：gzip filename，将产生一个filename.gz 文件

做出已跑动力学的rmd图，判断是否平衡：

ptraj xxx.top <>

xxx.in 内容：

trajin eq2.mdcrd.gz

trajin eq3.mdcrd.gz

trajin eq4.mdcrd.gz

trajin eq5.mdcrd.gz

rms first mass out xin.rms.dat1 :1-284@CA,C,N time 0.1

#产生一个xin.rms.dat1的文件，整体1-284骨架上的C与N原子

rms first mass out xin.rms.dat2 :88-91,172,201-204,230@CA,C,N time 0.1

 #产生一个xin.rms.dat2的文件，保守残基骨架上的C与N原子

----------------------------------------------------------------------------

利用xmgrace 作图：

xmgrace xin.rms.dat1 xin.rms.dat2


如果需要取随即的点的构型：

ptraj xxx.top <>

xxx.in内容：

trajin eq7.mdcrd.gz 117 117 #eq7中的117ps 的构型

strip :WAT #冒号前有空格，后没有，注意wat与top的水的大小写一致

strip :Na+

trajout eq7.pdb pdb nobox 产生一个eq7.pdb.117的文件

-------------------------------------------

traj AR.top <<>

> trajin AR.md7.crd 300 500

> center :1-250

> image center familiar

> rms first mass out rms.dat :1-250

> average average.rst restrt

> average average.pdb pdb

> EOF


--------------


在cluster上交分子动力学模拟作业的步骤：
1.准备复合物的参数文件(.top, .crd)
(1)计算小分子配体的电荷（amber不提供小分子的电荷参数）
可以用amber自带的bcc电荷，antechamber –i  ***.mol2 –fi mol2 –o ***_bcc.mol2 –fo mol2 –c bcc
也可采用外部程序计算的电荷，如gaussian，先计算静电势，然后拟合RESP电荷。具体步骤：
利用antechamber产生计算静电势的文件，antechamber –i  ***.mol2 –fi mol2 –o ligand.gjf –fo gcrt
修改ligand.gjf，去掉#HF行中的opt。然后用gaussian计算：g03 ligand.gjf。计算完毕产生ligand.log文件，拟合resp电荷：antechamber –i ligand.log –fi gout –o resp.mol2 –fo mol2 –c resp 将resp.mol2中的电荷部分拷贝到原始的mol2文件，即***.mol2
(2)小分子参数文件
如果是计算bcc电荷，antechamber –i ***_bcc.mol2 –fi mol2 –o ligand.prep –fo prepi
                    parmchk –i ligand.prep –f prepi –o ligand.frcmod
如果计算resp电荷，antechamber –i ***.mol2 –fi mol2 –o ligand.prep –fo prepi
                    parmchk –i ligand.prep –f prepi –o ligand.frcmod
注：此处的***.mol2中电荷部分已经修改过
(3)将小分子`***.mol2`与蛋白分子`***.pdb`（没有氢原子）合并成一个复合物，存成pdb文件，可命名为temp.pdb
(4)产生复合物的参数文件
命令：tleap –s –f tleap.in
tleap.in内容：
source leaprc.gaff
loadamberprep ligand.prep
loadamberparams ligand.frcmod
check LIG （注：为***.mol2文件中的分子子结构的命名，一个配体对应唯一的子结构命名）
saveamberparm LIG lig.top lig.crd (小分子参数文件)
source leaprc.ff03
com=loadpdb temp.pdb (导入复合物文件)
check com
saveamberparm com com.top com.crd
solvatebox com TIP3PBOX 10.0 （加水盒子）
addions com Na+ N (或者Cl-，看复合物带什么电性，N取决于复合物所带的电荷，使它保持中和)
saveamberparm com complex.top complex.crd (加了模型水的复合物参数)
 
2cluster上计算分子动力学模拟
先把complex.top complex.crd两个文件传到cluster
上传mini.in heat.in 和md.in输入文件，分别计算结构优化，加热和平衡过程，文件中的具体参数设置见amber manual
交作业命令：qsub md.pbs
删作业命令：qdel N  (N是作业的编号)
看作业计算情况：qstat –f  N
根据该命令提供的信息找到作业所在的节点，如c0-12
则ssh c0-12
cd /data/$username/N……
可进入文件夹访问


------
