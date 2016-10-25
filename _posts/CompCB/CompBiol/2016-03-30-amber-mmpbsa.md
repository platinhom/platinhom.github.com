---
layout: post
title: Amber:MM-PBSA小记
date: 2016-03-29 20:55:32
categories: CompCB
tags: CompBiol Amber
---

AMBER PBSA部分的执行现有两套方法: 一个使用老的Perl脚本 `mm_pbsa.pl`, 一个使用新的Python方法`MMPBSA.py`. Perl版本老式教程部分参考[这里](http://ambermd.org/tutorials/advanced/tutorial3/section3.htm), Python部分参考[这里](http://ambermd.org/tutorials/advanced/tutorial3/py_script/). 在新版本Python的教程里还提供了[Normal Mode Analysis](http://ambermd.org/tutorials/advanced/tutorial3/py_script/section5.htm), [Alanine突变](http://ambermd.org/tutorials/advanced/tutorial3/py_script/section3.htm), 将[自由能分解到残基上](http://ambermd.org/tutorials/advanced/tutorial3/py_script/section6.htm),[并行计算](http://ambermd.org/tutorials/advanced/tutorial3/py_script/section4.htm)等的教程.

## Perl脚本

这是老版本使用`mm_pbsa.pl`的用法, 使用就是:

`mm_pbsa.pl mmpbsa.in > stdout.log`

参数文件是`mmpbsa.in`内, 屏幕输出(实际只是执行过程, 意义不大)重定向到指定文件.

这里以教程中的PB/GB参数文件为例 (这里我合并了其中两步为一步, 即两个输入文件合并了):

~~~bash
#
# Input parameters for mm_pbsa.pl
#
# Holger Gohlke
# 15.02.2012
#
################################################################################
@GENERAL
#
# General parameters
#   0: means NO; >0: means YES
#
#   mm_pbsa allows to calculate (absolute) free energies for one molecular
#     species or a free energy difference according to:
#
#     Receptor + Ligand = Complex,
#     DeltaG = G(Complex) - G(Receptor) - G(Ligand).
#
#   VERBOSE - If set to 1, input and output files are not removed. This is
#             useful for debugging purposes.
#   PARALLEL - If set to values > 1, energy calculations for snapshots are
#              done in parallel, using PARALLEL number of threads. 
#
#   PREFIX - To the prefix, "{_com, _rec, _lig}.crd.Number" is added during
#            generation of snapshots as well as during mm_pbsa calculations.
#   PATH - Specifies the location where to store or get snapshots.
#   START - Specifies the first snapshot to be used in energy calculations
#           (optional, defaults to 1).
#   STOP - Specifies the last snapshot to be used in energy calculations 
#          (optional, defaults to 10e10).
#   OFFSET - Specifies the offset between snapshots in energy calculations 
#            (optional, defaults to 1).
#
#   COMPLEX - Set to 1 if free energy difference is calculated.
#   RECEPTOR - Set to 1 if either (absolute) free energy or free energy
#              difference are calculated.
#   LIGAND - Set to 1 if free energy difference is calculated.
#
#   COMPT - parmtop file for the complex (not necessary for option GC).
#   RECPT - parmtop file for the receptor (not necessary for option GC).
#   LIGPT - parmtop file for the ligand (not necessary for option GC).
#
#   GC - Snapshots are generated from trajectories (see below).
#   AS - Residues are mutated to Ala during generation of snapshots from
#        trajectories.
#   DC - Decompose the free energies into individual contributions.
#        (When using DC, MM and GB must be set to 1, even if a PB decomposition
#         is also requested.)
#
#   MM - Calculation of gas phase energies using sander.
#   GB - Calculation of desolvation free energies using the GB models in sander
#        (see below).
#   PB - Calculation of desolvation free energies using the PB method and
#        computation of nonpolar solvation free energies according to
#        the INP option in pbsa (see below).
#   MS - Calculation of nonpolar contributions to desolvation using molsurf
#        (see below).
#        If MS == 0 and GB == 1, nonpolar contributions are calculated either
#        with the LCPO (GBSA == 1) or the ICOSA (GBSA == 2) method in sander 
#        (see below).
#        If MS == 0 and PB == 1, nonpolar contributions are calculated according
#        the INP option in pbsa (see below).
#   NM - Calculation of entropies with nmode.
#
VERBOSE               0
PARALLEL              0
#
PREFIX                snapshot
PATH                  ./
START                 1
STOP                  200
OFFSET                1
#
COMPLEX               1
RECEPTOR              1
LIGAND                1
#
COMPT                 ./ras-raf.prmtop
RECPT                 ./ras.prmtop
LIGPT                 ./raf.prmtop
#
GC                    1
AS                    0
DC                    0
#
MM                    1
GB                    1
PB                    1
MS                    1
#
NM                    0
#
################################################################################
@MAKECRD
#
# The following parameters are passed to make_crd_hg, which extracts snapshots
#   from trajectory files. (This section is only relevant if GC = 1 OR 
#   AS = 1 above.)
#
#   BOX - "YES" means that periodic boundary conditions were used during MD
#         simulation and that box information has been printed in the
#         trajecotry files; "NO" means opposite.
#   NTOTAL - Total number of atoms per snapshot printed in the trajectory file
#            (including water, ions, ...).
#   NSTART - Start structure extraction from NSTART snapshot.
#   NSTOP - Stop structure extraction at NSTOP snapshot.
#   NFREQ - Every NFREQ structure will be extracted from the trajectory.
#
#   NUMBER_LIG_GROUPS - Number of subsequent LSTART/LSTOP combinations to
#                       extract atoms belonging to the ligand.
#   LSTART - Number of first ligand atom in the trajectory entry.
#   LSTOP - Number of last ligand atom in the trajectory entry.
#   NUMBER_REC_GROUPS - Number of subsequent RSTART/RSTOP combinations to
#                       extract atoms belonging to the receptor.
#   RSTART - Number of first receptor atom in the trajectory entry.
#   RSTOP - Number of last receptor atom in the trajectory entry.
#   Note: If only one molecular species is extracted, use only the receptor
#         parameters (NUMBER_REC_GROUPS, RSTART, RSTOP).
#
BOX                   YES
NTOTAL                42193
NSTART                1
NSTOP                 200
NFREQ                 1
#
NUMBER_LIG_GROUPS     1
LSTART                2622
LSTOP                 3862
NUMBER_REC_GROUPS     1
RSTART                1
RSTOP                 2621
#
################################################################################
@TRAJECTORY
#
# Trajectory names
#
#   The following trajectories are used to extract snapshots with "make_crd_hg":
#   Each trajectory name must be preceeded by the TRAJECTORY card.
#   Subsequent trajectories are considered together; trajectories may be
#     in ascii as well as in .gz format.
#   To be able to identify the title line, it must be identical in all files.
#
TRAJECTORY            ./prod1.mdcrd
TRAJECTORY            ./prod2.mdcrd
TRAJECTORY            ./prod3.mdcrd
TRAJECTORY            ./prod4.mdcrd
#
################################################################################
@PB
#
# PB parameters (this section is only relevant if PB = 1 above)
#
#   The following parameters are passed to the PB solver.
#   Additional input parameters may also be added here. See the sander PB
#   documentation for more options.
#
#   PROC -  Determines which program is used for solving the PB equation:
#           Delphi (PROC == 1), PBSA (PROC == 2), or APBS (PROC == 3).
#           By default, PROC == 2, the pbsa program of the AMBER suite is used.
#   REFE -  Determines which reference state is taken for PB calc:
#           By default, REFE == 0, reaction field energy is calculated with
#           EXDI/INDI. Here, INDI must agree with DIELC from MM part.
#   INDI -  Dielectric constant for the solute.
#   EXDI -  Dielectric constant for the surrounding solvent.
#   ISTRNG - Ionic strength (in mM) for the Poisson-Boltzmann solvent.
#   SCALE - Lattice spacing in no. of grids per Angstrom.
#   LINIT - No. of iterations with linear PB equation.
#   RADIOPT - Option to set up radii for PB calc:
#             0: uses the radii from the prmtop file. Default.
#             1: uses the radii optimized by Tan and Luo with respect to the
#                reaction field energies computed in the TIP3P explicit solvents
#                (Tan & Luo, J. Phys. Chem. B, 2006, 110, 18680-18687). 
#                Note that optimized radii are based on AMBER atom types
#                (upper case) and charges. Radii from the prmtop files are used
#                if the atom types are defined by antechamber (lower case).
#   ARCRES - Resolution (in the unit of Angstrom) of solvent accessible arcs
#   IVCAP - If set to 1, a solvent sphere (specified by CUTCAP,XCAP,YCAP,
#           and ZCAP) is excised from a box of water. If set to 5, a solvent
#           shell is excised, specified by CUTCAP (the thickness of the shell 
#           in A). The electrostatic part of the solvation free energy is 
#           estimated from a linear response approximation using the explicit 
#           solvent plus a reaction field contribution from outside the sphere 
#           (i.e., a hybrid solvation approach is pursued). 
#           In addition, the nonpolar contribution is estimated from a sum of 
#           (attractive) dispersion interactions calc. between the solute and 
#           the solvent molecules plus a (repulsive) cavity contribution 
#           (Gohlke & Case, J. comput. Chem. 2004, 25, 238-250). 
#           For the latter, the surface calculation must be done with MS = 1 and
#           the PROBE should be set to 1.4 to get the solvent excluded surface.
#           In this case bondi radii are used as cavity radii set.
#   CUTCAP - Radius of the water sphere or thickness of the water shell.
#            Note that the sphere must enclose the whole solute.
#   XCAP  - Location of the center of the water sphere.
#   YCAP
#   ZCAP
#
# NP Parameters for nonpolar solvation energies if MS = 0
#
#   INP   - Option for modeling nonpolar solvation free energy.
#           See sander PB documentation for more information on the
#           implementations by Tan and Luo.
#           1: uses the solvent-accessible-surface area to correlate total
#              nonpolar solvation free energy:
#              Gnp = SURFTEN * SASA + SURFOFF. Default.
#           2: uses the solvent-accessible-surface area to correlate the
#              repulsive (cavity) term only, and uses a surface-integration
#              approach to compute the attractive (dispersion) term:
#              Gnp = Gdisp + Gcavity
#                  = Gdisp + SURFTEN * SASA + SURFOFF.
#           When this option is used, RADIOPT has to be set to 1,
#           i.e. the radii set optimized by Tan and Luo.
#   SURFTEN/SURFOFF - Values used to compute the nonpolar
#           solvation free energy Gnp acccording to INP.
#           If INP = 1 and RADIOPT = 0 (default, see above),
#           use SURFTEN/SURFOFF parameters that fit with the radii from the
#           prmtop file, e.g., 
#           use SURFTEN: 0.00542 and SURFOFF: 0.92 for PARSE radii.
#           If INP = 2 and RADIOPT = 1, please set these to the following: 
#           SURFTEN: 0.0378; OFFSET: -0.5692
#
# NP Parameters for nonpolar solvation energies if MS = 1
#
#   SURFTEN/SURFOFF - Values used to compute the nonpolar contribution Gnp to
#           the desolvation according to:
#      (I)  Gnp = SURFTEN * SASA + SURFOFF (if IVCAP == 0)
#           Use parameters that fit with the radii from the reaction field
#           calculation. E.g., use SURFTEN: 0.00542, SURFOFF: 0.92 for
#           PARSE radii 
#      (II) Gnp = Gdisp + Gcavity = Gdisp + SURFTEN * SESA + SURFOFF (IVCAP > 0)
#           Nonpolar solvation free energy calculated as discribed for IVCAP > 0
#           above. In this case use SURFTEN: 0.069; SURFOFF: 0.00 for
#           calculating the Gcavity contribution.
#
PROC                  2
REFE                  0
INDI                  1.0
EXDI                  80.0
SCALE                 2
LINIT                 1000
ISTRNG                0.0
RADIOPT               0
ARCRES                0.0625
INP                   1
#
SURFTEN               0.005
SURFOFF               0.00
#
IVCAP                 0
CUTCAP                -1.0
XCAP                  0.0
YCAP                  0.0
ZCAP                  0.0
#
################################################################################
@MM
#
# MM parameters (this section is only relevant if MM = 1 above)
#
#   The following parameters are passed to sander.
#   For further details see the sander documentation.
#
#   DIELC - Dielectricity constant for electrostatic interactions.
#           Note: This is not related to GB calculations.
#
DIELC                 1.0
#
################################################################################
@GB
#
# GB parameters (this section is only relevant if GB = 1 above)
#
#   The first group of the following parameters are passed to sander.
#   For further details see the sander documentation.
#
#   IGB - Switches between Tsui's GB (1) and Onufriev's GB (2, 5).
#   GBSA - Switches between LCPO (1) and ICOSA (2) method for SASA calc.
#          Decomposition only works with ICOSA.
#   SALTCON - Concentration (in M) of 1-1 mobile counterions in solution.
#   EXTDIEL - Dielectricity constant for the solvent.
#   INTDIEL - Dielectricity constant for the solute.
#
#   SURFTEN / SURFOFF - Values used to compute the nonpolar contribution Gnp to
#    the desolvation according to Gnp = SURFTEN * SASA + SURFOFF.
#    Choose SURFTEN and SURFOFF values according to the selected
#    GB model, e.g.:
#    IGB=1 : SURFTEN=0.0072, SURFOFF=0.0, mbondi radii
#            (Tsui & Case, Biopolymers 2000, 56, 275-291)
#    IGB=2 : SURFTEN=0.005, SURFOFF=0.0, mbondi2 radii
#            (Onufriev et al, Proteins 2004, 55, 383-394)
#    IGB=5 : SURFTEN=0.005, SURFOFF=0.0, mbondi2 radii
#            (Onufriev et al, Proteins 2004, 55, 383-394)
#
IGB                   2
GBSA                  1
SALTCON               0.00
EXTDIEL               80.0
INTDIEL               1.0
#
SURFTEN               0.005
SURFOFF               0.00
#
################################################################################
@MS
#
# Molsurf parameters (this section is only relevant if MS = 1 above)
#
#   PROBE - Radius of the probe sphere used to calculate the SAS.
#           In general, since Bondi radii are already augmented by 1.4A,
#           PROBE should be 0.0
#           In IVCAP = 1 or 5, the solvent excluded surface is required for
#           calculating the cavity contribution. Bondi radii are not
#           augmented in this case and PROBE should be 1.4.
#
PROBE                 0.0
#
################################################################################
@PROGRAMS
#
# Additional program executables can be defined here
#
#
################################################################################
~~~

这个参数文件很长..里面有参数详细解析. `@TRAJECTORY`这样的是选项卡, 即代表一系列相关参数在这部分, 例如@PB, @GB. 注释使用`#`.

一般地, 我们关注以下部分:

- `@GENERAL`卡:
	- `PREFIX` : 输入每帧文件和输出文件的前缀, 输出结果有 (算复合物结合自由能不算NMODE): 
		- $PREFIX_statics.out : 总输出文件, 读取分析这个就OK了, 里面包括三个单体和Delta的能量和各项的数值.
		- $PREFIX_com.all.out : 类似还有 rec, lig版本, 总共三个文件, 就是三个单体的各项计算的结果. 多个坐标轨迹输入会有更多的相应输出.
	- `MM`/`PB`/`GB`/`MS`/`NM`: 这是控制计算什么内容, 分别是分子力学能量, PB, GB, 表面(非极性贡献)和Normal Mode (熵). 一般地, MM, MS都设1, NM设0(要算才设1), PB/GB根据需要设定. 有时进行特殊计算, 某些项是必须打开的.
	- `COMPLEX`/`RECEPTOR`/`LIGAND` : 是否进行相应自由能计算. 受体可以单独计算, 一般算复合物三个都设1.
	- `COMPT`/`RECPT`/`LIGPT`: 复合物 (无溶剂), 受体和配体的prmtop文件指定.
	- `PATH` : 放置每帧Snapshot的文件夹位置. 如果GC=0, 保证PATH文件夹内有合符规格的每帧文件. GC=1, 这个路径就是输出每帧坐标的输出文件夹.
	- `GC` : 这个是用来将轨迹文件crd分解为每帧的crd的, 分解轨迹到PATH文件夹内. 文件名为 `$PATH/$PREFIX_com.crd.Number`, 相应com/rec/lig对应复合物, 受体和配体.Number是帧编号, 从1开始. 如果没有独立分解出每帧, GC就使用1让他自己生成, 此时需要用到输入文件的 `@MAKECRD` 和 `@TRAJECTORY` 卡部分.
	- `START`/`STOP`/`OFFSET` : 计算时使用的SNAPSHOT从START到STOP为止, 间隔为OFFSET. 如果GC=1, 可以GC时产生相应的帧, 这时这里的START/STOP/OFFSET用默认就好了(1/10e10/1). 如果产生了全部的SNAPSHOT, 想再自定义采帧方式, 可以改这三个.
	- `AS` : 进行Alanine扫描的设置, 这里不介绍. 不进行就设0.
	- `DC` : 进行能量分解的设置, 这里不介绍. 不进行就设0.
	- `VERBOSE` : 默认0是删除中间输入输出文件, 设置1则保留. 用于debug. 
	- `PARALLEL` : 并行计算时设置>1整数. 默认不适用时为0. (设置8就是同时分析8帧哦)  
- `@MAKECRD`卡
	- `BOX` : MD是否使用周期边界, 一般是,=1.
	- `NTOTAL` : MD轨迹文件每帧原子数 (包括溶剂,离子哦!)
	- `NSTART`/`NSTOP`/`NFREQ` : 提取帧从NSTART 到NSTOP(包含), 提取间隔是NFREQ为一帧.例如MD总2000帧, 每10帧输出一次.可以设1/2000/10.
	- `NUMBER_LIG_GROUPS`/`LSTART`/`LSTOP` : 配体有几组,每组原子取自下面的LSTART到LSTOP. (如果原子序号不连续, 就要多个组, 多个组就要写多个LSTART/LSTOP)
	- `NUMBER_REC_GROUPS`/`RSTART`/`RSTOP` : 受体有几组,每组原子取自下面的RSTART到RSTOP. (如果原子序号不连续, 就要多个组, 多个组就要写多个RSTART/RSTOP)
- `@TRAJECTORY`卡
	- `TRAJECTORY` : 指定相应的轨迹文件, 按顺序读入输出帧. 可以有多个TRAJECTORY.
- `@PB`卡
	- `PROC` : 使用哪种PB方法, 缺省2是使用内置的 *pbsa* 程序进行计算.
	- `REFE` : 使用reference state方法, 缺省0是使用EXDI/INDI计算reaction ﬁield energy. 
	- `INDI`/`EXDI` : 重要参数, 溶质和溶剂的介电常数. 这里溶质介电常数要和MM计算分子力学时的静电能时要一致! 默认1.0和80.0.
	- `ISTRNG` : 离子强度 (mM)
	- `PRBRAD` : 溶剂探针半径, 默认1.4. Luo等的方法可以设1.6.
	- `RADIOPT` : PB计算的原子半径采用何种方法, 这里perl说默认0是使用输入文件的原子半径, 1是使用Luo等的优化方法(原子类型大写时使用AMBER内置的处理, 小写时(如antechamber)采用top文件的原子半径). 这个设置错误可能会报错.
	- `LINIT` : 线性PB计算迭代最大次数.
	- `ARCRES` : 溶剂可及的弧度的点的分辨率. 越小越精确咯. 默认0.25, 见很多都用0.0625. 是*pbsa*的参数.
	- `INP` : 非极性溶剂化能的计算方法, 默认1是`Gnp=SURFTEN*SASA+SURFOFF`, 2是`Gnp=Gdisp+Gcavity=Gdisp+SURFTEN*SASA+SURFOFF`. Gdisp是吸引项, Gcavity是排斥项(SAS相关). 如果INP设为2, RADIOPT要设为1 (使用Luo等的方法)
	- `SURFTEN`和`SURFOFF` : 表面张力系数和一个offset值. 和INP, IVCAP 等设置时最好相关. 不懂时默认好了..
- `@GB`卡
	- 暂忽略
- `@MM`卡:
	- `DIELC` : 分子力学计算时静电作用的介电常数.

对于PB/GB计算自由能的[参数推荐](http://ambermd.org/tutorials/advanced/tutorial3/files/recommended_settings.pdf). 

对于输出结果在$PREFIX_statics.out中, 每项的含义:

~~~
*** Abbreviations for mm_pbsa output ***
ELE - 非键静电能项, 基于力场. non-bonded electrostatic energy + 1,4-electrostatic energy
VDW - 范德华作用能项, 基于力场. non-bonded van der Waals energy + 1,4-van der Waals energy
INT - 内能项, 基于力场. bond, angle, dihedral energies
GAS - 气相下静电+范德华+内能, 也就是力场能量. ELE + VDW + INT
PBSUR - PB非极性溶剂化能项. hydrophobic contrib. to solv. free energy for PB calculations
PBCAL - PB静电溶剂化能项. reaction field energy calculated by PB
PBSOL - PB溶剂化能. PBSUR + PBCAL
PBELE - PB结合自由能静电贡献项. PBCAL + ELE
PBTOT - PB计算结合自用能. PBSOL + GAS
GBSUR - hydrophobic contrib. to solv. free energy for GB calculations
GB - reaction field energy calculated by GB
GBSOL - GBSUR + GB
GBELE - GB + ELE
GBTOT - GBSOL + GAS
TSTRA - 平动熵贡献能. translational entropy (as calculated by nmode) times temperature
TSROT - 转动熵贡献能. rotational entropy (as calculated by nmode) times temperature
TSVIB - 振动熵贡献能. vibrational entropy (as calculated by nmode) times temperature
*** Prefixes in front of abbreviations for energy decomposition ***
"T" - energy part due to _T_otal residue
"S" - energy part due to _S_idechain atoms
"B" - energy part due to _B_ackbone atoms
~~~

所以, 如果只是进行PB/GB计算结合自由能, 读取PBTOT/GBTOT即可 (结合自由能=complex-receptor-ligand, Delta的输出里面其实就是最终结果). 

一般地, MM部分由ELE, VDW和INT组成, 计算delta时内能项基本被抵消. 溶剂化部分, PB/GB一般通过solver计算. 非极性作用项则是通过面积来拟合.

## Python脚本

该脚本系列有两个: `ante-MMPBSA.py` 和 `MMPBSA.py`, 前者用于创建复合物/受体/配体的拓扑文件(top), 后者用于一般的MMPBSA相关计算.

### ante-MMPBSA.py 

查询帮助可以知道一些选项: 

~~~
Usage: ante-MMPBSA.py [options]
 
Options:
  -h, --help            show this help message and exit
  -p PRMTOP, --prmtop=PRMTOP
  						指定复合物的top文件, 可以是溶剂化也可以是未溶剂化的 
                        Input "dry" complex topology or solvated complex
                        topology
  -c COMPLEX, --complex-prmtop=COMPLEX
  						指定输出去除溶剂的复合物top文件
                        Complex topology file created by stripping PRMTOP of
                        solvent
  -r RECEPTOR, --receptor-prmtop=RECEPTOR
  						指定输出去除配体的受体top文件 (基于COMPLEX的拓扑)
                        Receptor topology file created by stripping COMPLEX of
                        ligand
  -l LIGAND, --ligand-prmtop=LIGAND
  						指定输出去除受体的配体top文件 (基于COMPLEX的拓扑)
                        Ligand topology file created by stripping COMPLEX of
                        receptor
  -s STRIP_MASK, --strip-mask=STRIP_MASK
  						指定去除溶剂的表达式
                        Amber mask of atoms needed to be stripped from PRMTOP
                        to make the COMPLEX topology file
  -m RECEPTOR_MASK, --receptor-mask=RECEPTOR_MASK
  						指定受体的表达式 (和-n冲突)
                        Amber mask of atoms needed to be stripped from COMPLEX
                        to create RECEPTOR. Cannot specify with -n/--ligand-
                        mask
  -n LIGAND_MASK, --ligand-mask=LIGAND_MASK
  						指定配体的表达式 (和-m冲突)
                        Amber mask of atoms needed to be stripped from COMPLEX
                        to create LIGAND. Cannot specify with -m/--receptor-
                        mask
  --radii=RADIUS_SET    指定PB计算的半径set
  						PB/GB Radius set to set in the generated topology
                        files. This is equivalent to "set PBRadii <radius>" in
                        LEaP. Options are bondi, mbondi2, mbondi3, amber6, and
                        mbondi and the default is to use the existing radii.
~~~

用法其实主要就是3个:

1. 溶剂化复合物去除溶剂  
`ante-MMPBSA.py -p complex.top --radii mbondi2 -s ":WAT" -c com.top`  
如果要去除添加的盐离子:  
`ante-MMPBSA.py -p complex.top --radii mbondi2 -s ":WAT,Na+,Cl-" -c com.top`
1. 分解复合物top为受体和配体  
这里要使用没有溶剂的复合物top, 否则的话受体部分会含有溶剂!  
`ante-MMPBSA.py -p com.top --radii mbondi2 -n ":LIG" -l lig.top -r pro.top`
1. 除溶剂并分解为受体配体  
`ante-MMPBSA.py -p complex.top --radii mbondi2 -s ":WAT,Na+,Cl-" -c com.top -n ":LIG" -l lig.top -r pro.top`

对于表达式, 可以参考[Amber原子选取语法(Atom Mask Selection Syntax)](/2016/04/01/amberMask/).

### `MMPBSA.py`

该脚本参数(Amber14):

~~~
usage: MMPBSA.py [-h] [-v] [--input-file-help] [-O] [-prefix <file prefix>]
                 [-i FILE] [-xvvfile XVVFILE] [-o FILE] [-do FILE] [-eo FILE]
                 [-deo FILE] [-sp <Topology File>] [-cp <Topology File>]
                 [-rp <Topology File>] [-lp <Topology File>]
                 [-mc <Topology File>] [-mr <Topology File>]
                 [-ml <Topology File>] [-srp <Topology File>]
                 [-slp <Topology File>] [-y [MDCRD [MDCRD ...]]]
                 [-yr [MDCRD [MDCRD ...]]] [-yl [MDCRD [MDCRD ...]]]
                 [-make-mdins] [-use-mdins] [-rewrite-output] [--clean]
 
optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --input-file-help     Print all available options in the input file.
                        (default: False)
 
Miscellaneous Options:
  -O, --overwrite       Allow output files to be overwritten (default: False)
  -prefix <file prefix>
                        Prefix for intermediate files. (default: _MMPBSA_)
 
Input and Output Files:
  These options specify the input files and optional output files.
 
  -i FILE               MM/PBSA input file. (default: None)
  -xvvfile XVVFILE      XVV file for 3D-RISM. (default:
                        /opt/software/Amber/14v19--
                        Intel-13.0.1.117/dat/mmpbsa/spc.xvv)
  -o FILE               Output file with MM/PBSA statistics. (default:
                        FINAL_RESULTS_MMPBSA.dat)
  -do FILE              Output file for decomposition statistics summary.
                        (default: FINAL_DECOMP_MMPBSA.dat)
  -eo FILE              CSV-format output of all energy terms for every frame
                        in every calculation. File name forced to end in
                        [.csv]. This file is only written when specified on
                        the command-line. (default: None)
  -deo FILE             CSV-format output of all energy terms for each printed
                        residue in decomposition calculations. File name
                        forced to end in [.csv]. This file is only written
                        when specified on the command-line. (default: None)
  -sp <Topology File>   Topology file of a fully solvated system. If provided,
                        the atoms specified by <strip_mask> will be stripped
                        from the trajectory file. The complex topology file
                        (-cp) must be consistent with this stripped trajectory
                        (default: None)
  -cp <Topology File>   Topology file of the bound complex (or the single
                        system for 'stability' calculations) (default:
                        complex_prmtop)
  -rp <Topology File>   Topology file of the unbound receptor. If omitted (and
                        -lp is omitted, too), a stability calculation with
                        just the complex will be performed. (default: None)
  -lp <Topology File>   Topology file of the unbound ligand. If omitted (and
                        -rp is omitted, too), a stability calculation with
                        just the complex will be performed. (default: None)
  -mc <Topology File>   Complex topology file of the mutant complex in which
                        one residue has been mutated to either a glycine or
                        alanine to perform computational alanine (or glycine)
                        scanning. (default: None)
  -mr <Topology File>   Receptor topology file of the mutant receptor (see -mc
                        above). If omitted, the mutation is assumed to be in
                        the ligand. (default: None)
  -ml <Topology File>   Ligand topology file of the mutant receptor (see -mc
                        above). If omitted, the mutation is assumed to be in
                        the receptor. (default: None)
  -srp <Topology File>  Receptor ligand topology file. For use with multiple-
                        trajectory simulations when the receptor trajectory is
                        solvated. This will trigger the atoms specified by
                        'strip_mask' to be removed from the receptor
                        trajectory (default: None)
  -slp <Topology File>  Solvated ligand topology file. See -srp description
                        above. (default: None)
 
Input Trajectory Files:
  These files contain the snapshots analyzed by MM/PBSA-type calculations.
 
  -y [MDCRD [MDCRD ...]]
                        Input trajectories of the (maybe solvated) complex.
                        (specify as many as you'd like). (default: ['mdcrd'])
  -yr [MDCRD [MDCRD ...]]
                        Receptor trajectory file for multiple trajectory
                        approach (default: None)
  -yl [MDCRD [MDCRD ...]]
                        Ligand trajectory file for multiple trajectory
                        approach. (default: None)
 
Miscellaneous Actions:
  -make-mdins           Create the input files for each calculation and quit.
                        This allows you to modify them and re-run using -use-
                        mdins (default: False)
  -use-mdins            Use existing input files for each calculation. If they
                        do not exist with the appropriate names, MMPBSA.py
                        will quit in error. (default: False)
  -rewrite-output       Do not re-run any calculations, just parse the output
                        files from the previous calculation and rewrite the
                        output files. (default: False)
  --clean               Clean temporary files and quit. (default: False)
 
This program will calculate binding free energies using end-state free energy
methods on an ensemble of snapshots using a variety of implicit solvent models
~~~

该脚本简单的应用是:

`MMPBSA.py -O -i mmpbsa.in -o mmpbsa.out -cp com.top -rp rec.top -lp lig.top -y traj.crd`

如果轨迹(坐标)复合物中还有溶剂和离子,则需要使用`-sp`指明其拓扑, 再用cp+rp+lp指明子结构. 

`MMPBSA.py -O -i mmpbsa.in -o mmpbsa.out -sp complex.top -cp com.top -rp rec.top -lp lig.top -y traj.crd`


MPI并行版跑法:

`mpirun -np 8 MMPBSA.py.MPI -O -i mmpbsa.in -o mmpbsa.out -cp com.top -rp rec.top -lp lig.top -y traj.crd`

如果只要进行MMPBSA计算, 只需要上面几个参数就可以了. `-i`指明mmpbsa的配置文件, -o 是结果文件名, `-O`覆盖已有文件, `-sp/cp/rp/lp`分别是复合物(溶剂化),复合物(无水),受体和配体的拓扑文件, `-y`是轨迹或者相关坐标文件(rst,crd等),可以有多个文件,用`,`隔开.

### mmpbsa.in

是进行MMPBSA.py的参数配置文件. 如果不知道默认参数有哪些, 可以先书写一下的参数文件`mmpbsa.in`

~~~
Input file for running PB and GB
&general
   endframe=1, keep_files=2
/
&gb
/
&pb
/
~~~

然后跑以下命令. 其中`-make-mdins`是产生相应参数文件, 他会参考输入的`mmpbsa.in`来写出输出文件, 即`mmpbsa.in`里面的参数会覆盖掉默认的参数. 另外, 虽然程序只读取`mmpbsa.in`产生输出后即退出, 即不会读取拓扑和坐标文件, 但是这里也要指明相应文件(很傻吧..) 

`MMPBSA.py -O -make-mdins -i mmpbsa.in -o hi -sp complex.top -cp com.top -rp pro.top -lp lig.top -y complex.crd`

最后可以产生`_MMPBSA_gb.mdin`和`_MMPBSA_pb.mdin`文件, 里面有相应参数和配置值. 可以参考这些值放到mmpbsa.in来再跑, 也可以直接修改这两个文件, 然后用`-use-mdins`选项来直接来加载这两个文件(但还是要指明mmpbsa.in...).

如果熟悉这个配置文件怎么写, 就自己写吧. 这个文件一般有三个部分 (参考上面那个): `&general`,`&gb`,`&pb`, 对应整体配置, GB和PB设置. 如果要进行Normal Mode Analysis,能量分解和Alanine扫描,需要`&nmode`,`&decomp`和`&alanine_scanning`选项卡. 选项卡下面以`/`一行结束,参数写在每个选项卡当中, 可以逗号分隔, 可以另起一行.

以下是Amber提供的各种示例配置文件 (包括一般PB/GB,Alanine扫描,NMode,能量分解,QM/MMPBSA,3D-RISM):

~~~
Sample input file for GB and PB calculation
&general
startframe=5, endframe=100, interval=5,
verbose=2, keep_files=0,
/
&gb
igb=5, saltcon=0.150,
/
&pb
istrng=0.15, fillratio=4.0
/
--------------------------------------------------------
Sample input file for Alanine scanning
&general
verbose=2,
/
&gb
igb=2, saltcon=0.10
/
&alanine_scanning
/
--------------------------------------------------------
Sample input file with nmode analysis
&general
startframe=5, endframe=100, interval=5,
verbose=2, keep_files=2,
/
&gb
igb=5, saltcon=0.150,
/
&nmode
nmstartframe=2, nmendframe=20, nminterval=2,
maxcyc=50000, drms=0.0001,
/
--------------------------------------------------------
Sample input file with decomposition analysis
&general
startframe=5, endframe=100, interval=5,
/
&gb
igb=5, saltcon=0.150,
/
&decomp
idecomp=2, dec_verbose=3,
print_res=”20, 40-80, 200”
/
--------------------------------------------------------
Sample input file for QM/MMGBSA
&general
startframe=5, endframe=100, interval=5,
ifqnt=1, qmcharge=0, qm_residues=”100-105, 200”
qm_theory=”PM3”
/
&gb
igb=5, saltcon=0.100,
/
--------------------------------------------------------
Sample input file for MM/3D-RISM
&general
startframe=5, endframe=100, interval=5,
/
&rism
polardecomp=1, thermo=’gf’
/
~~~

这里只关注最简单的PB/GBSA

~~~
Sample input file for GB and PB calculation
&general
startframe=5, endframe=100, interval=5,
verbose=2, keep_files=0,
/
&gb
igb=5, saltcon=0.150,
/
&pb
istrng=0.15, fillratio=4.0
/
~~~

#### general卡

- startframe,endframe,interval: 读取轨迹帧的设置,起始(1开始),终止(默认9999999)和间隔(默认1)
- keep_files: 临时文件处理, 0: 不保留临时文件; 1: 缺省,保留产生的轨迹和mdout文件; 2. 保留所有临时文件(临时文件以`_MMPBSA_`开头,可以修改默认值)
- verbose: 输出文件详细度, 0: 简单输出; 1: 缺省, 输出所有复合物受体和配体项; 2: 输出输出每帧的相应项?


#### pb卡

- inp: 非极性计算方法. 默认2, 使用Gdisp项, 此时要用Luo等方法半径(radiopt=1). 1的话不考虑Gdisp项. 0的话不考虑非极性溶剂化项.
- radiopt: 默认1, 采用预计算的值; 或者0, 采用拓扑文件内的定义. 
- indi/exdi : 溶质和溶剂的介电常数,默认1.0/80.0
- istrng : 离子强度, mM (PBSA)或M(APBS), 缺省0.
- prbrad : 探针半径, 默认1.4, 或使用1.6.
- cavity\_offset/cavity\_surften : 用于计算非极性项的校正值和表面张力项. 默认-0.5692和0.0378.
- fillratio : 有限差分最长维度矩形和溶质的比例(默认4.0)

(一般inp/radiopt/cavity\_surften/cavity\_offset使用2/1//或1/0/0.005/0)

#### gb卡

- igb : GB方法, 1,2,5,7,8 (默认5)
- probe : 溶剂探针, 默认1.4 (只有molsurf设1有效)
- molsurf : 设置1时使用molsurf算法计算表面用于非极性项. 设置0 (默认), 使用LCPO(Linear Combination of Pairwise Overlaps)算法.
- saltcon : 盐浓度(默认 0.0 M)
- surfoff/surften : 用于计算非极性项的校正值和表面张力项. 默认0.0和0.0072(kcal/mol^2).

###### Error

- `PB Bomb in pb_aaradi(): No radius assigned for atom` : 主要是没有半径数据, 取决于radiopt.如果radiopt=0是从文件读取. =1是使用Amber参数集, 这时取决于内建定义咯. 这时最好用inp=1. 也可以参考[这个](http://archive.ambermd.org/201208/0074.html)修改参数文件..

## 批处理MMPBSA脚本

根据PDB号文件夹安置, 内含子文件夹`{pid}_mdin`,内含complex.top, complex.crd, com/pro/lig.top/crd.

~~~bash
#! /bin/bash

## Check $AMBER
if [ -z $AMBERHOME ];then
echo "No Amber tools were installed or loaded into system..."
## source config for Amber
module swap GNU Intel/13.0.1.117;
module load OpenMPI/1.4.4;
module load Amber/14v19;
source /opt/software/Amber/14v19--Intel-13.0.1.117/amber.sh
 
## Uncomment the following to exit when without Amber
#exit 1
fi

for pid in `ls -d ????`
do

if [ -d $pid ];then

#cp mibpbPBSA_step3_single.sh $pid
cd $pid


if [ ! -f done_step3.txt ];then
if [ ! -f working_step3.txt ];then

touch working_step3.txt

[ -d ${pid}_mdin/ ] && cd ${pid}_mdin/

if [ -f complex.top -a -f complex.crd ];then
if [ -f com.top -a -f com.crd ];then
if [ -f pro.top -a -f pro.crd ];then
if [ -f lig.top -a -f lig.crd ];then

echo -n "Doning $pid ... "

echo "Sample input file for GB and PB calculation
&general
startframe=1, endframe=1, interval=1,
verbose=1, keep_files=0,
#	entropy=1,
/
&gb
igb=5, saltcon=0.00,
probe=1.4,
/
&pb
istrng=0.0, fillratio=4.0,
inp=1,radiopt=0,
indi=1.0,exdi=80.0
prbrad=1.4
/">mmpbsa.in

#MMPBSA.py -O -o mmpbsa.out -i mmpbsa.in -sp complex.top -cp com.top -rp pro.top -lp lig.top -y complex.crd > mmpbsa_out.log
MMPBSA.py -O -o mmpbsa.out -i mmpbsa.in -cp com.top -rp pro.top -lp lig.top -y com.crd > mmpbsa_out.log

[ -d ../${pid}_mdin/ ] && cd ..

mv working_step3.txt done_step3.txt
echo "Done $pid !"

fi
fi
fi
fi
fi
fi

cd ..

fi

done
~~~

## 提取结果脚本

针对MMPBSA.py进行处理:

~~~python
#! /usr/bin/env python
import sys,os
f= open(sys.argv[2]) if len(sys.argv)>2 else open("mmpbsa.out")
if len(sys.argv)<2:
    sys.argv.append("Out")
    print "Out XB ITEM VDW EEL EXB ENP EDIS GGAS GSOL G"
lines=f.readlines()
f.close()
for i in range(len(lines)):
    if (lines[i].strip()=="GENERALIZED BORN:" or lines[i].strip()=="POISSON BOLTZMANN:"):
            for j in [0,1,2,3]:
                if (lines[i].strip()=="GENERALIZED BORN:"): print sys.argv[1].replace(" ","")+" GB",
                else:print sys.argv[1].replace(" ","")+" PB",
                if (j is 0): print "com",
                if (j is 1): print "pro",
                if (j is 2): print "lig",
                if (j is 3): print "delta",
                if (lines[i].strip()=="POISSON BOLTZMANN:" and j is 3):
                    print lines[i+14*j+5][14:].split()[0],lines[i+14*j+6][14:].split()[0],lines[i+14*j+7][14:].split()[0],lines[i+14*j+8][14:].split()[0],lines[i+14*j+9][14:].split()[0],
                    print lines[i+14*j+11][14:].split()[0],lines[i+14*j+12][14:].split()[0],lines[i+14*j+14][14:].split()[0]
                else:
                    print lines[i+14*j+5][14:].split()[0],lines[i+14*j+6][14:].split()[0],lines[i+14*j+7][14:].split()[0],lines[i+14*j+8][14:].split()[0],"0.0000",
                    print lines[i+14*j+10][14:].split()[0],lines[i+14*j+11][14:].split()[0],lines[i+14*j+13][14:].split()[0]
~~~

使用就是`python mmpbsa_out.py 1ajj mmpbsa.out`这样咯, 出来结果是以下顺序(共8行):

`PDB XB ITEM VDW EEL EXB ENP EDIS GGAS GSOL G`

> Update 脚本:

- Error1 : 对于部分有水分子的复合物, 出来一个WARNING:  
`WARNING: INCONSISTENCIES EXIST WITHIN INTERNAL POTENTIAL TERMS. THE VALIDITY OF THESE RESULTS ARE HIGHLY QUESTIONABLE`  
主要是出现了内能项不能抵消(这里主要1,4-vdw和1,4-静电项消不了..) 暂时不管只提取VDW和EEL项..
- ERROR2 : 直接跑不下来..`Found an invalid periodicity in the prmtop file:` (未解决)

~~~python
#! /usr/bin/env python
import sys,os
try:
	f= open(sys.argv[2]) if len(sys.argv)>2 else open("mmpbsa.out")
except IOError as e:
	print sys.argv[1], e
	print sys.argv[1], e
	print sys.argv[1], e
	print sys.argv[1], e
	print sys.argv[1], e
	print sys.argv[1], e
	print sys.argv[1], e
	print sys.argv[1], e
	sys.exit(1)
if len(sys.argv)<2:
	sys.argv.append("Out")
	print "Out XB ITEM VDW EEL EXB ENP EDIS GGAS GSOL G"
lines=f.readlines()
f.close()

items=["Complex:","Receptor:","Ligand:","Differences (Complex - Receptor - Ligand):"]

for i in range(len(lines)):
	if (lines[i].strip()=="GENERALIZED BORN:" or lines[i].strip()=="POISSON BOLTZMANN:"):
		j=0
		for k in range(i+1,len(lines)):
			if (lines[k].strip()=="GENERALIZED BORN:" or lines[k].strip()=="POISSON BOLTZMANN:"):
				break
			line=lines[k].strip()
			if (line in items):
				if (lines[i].strip()=="GENERALIZED BORN:"): print sys.argv[1].replace(" ","")+" GB",
				else:print sys.argv[1].replace(" ","")+" PB",
				if (line== "Complex:"): 
					j=0
					print "com",
				if (line== "Receptor:"): 
					j=1
					print "pro",
				if (line== "Ligand:"):
					j=2 
					print "lig",
				if (line== "Differences (Complex - Receptor - Ligand):"):
					j=3 
					print "delta",
				if lines[i].strip()=="POISSON BOLTZMANN:" and j is 3:
					if (lines[k+3].split()[0]!="BOND"):
						print lines[k+3][14:].split()[0],lines[k+4][14:].split()[0],lines[k+5][14:].split()[0],lines[k+6][14:].split()[0],lines[k+7][14:].split()[0],
						print lines[k+9][14:].split()[0],lines[k+10][14:].split()[0],lines[k+12][14:].split()[0]
					else:
						print lines[k+6][14:].split()[0],lines[k+7][14:].split()[0],lines[k+10][14:].split()[0],lines[k+11][14:].split()[0],lines[k+12][14:].split()[0],
						print lines[k+14][14:].split()[0],lines[k+15][14:].split()[0],lines[k+17][14:].split()[0]						
				else:
					if (lines[k+3].split()[0]!="BOND"):
						print lines[k+3][14:].split()[0],lines[k+4][14:].split()[0],lines[k+5][14:].split()[0],lines[k+6][14:].split()[0],"0.0000",
						print lines[k+8][14:].split()[0],lines[k+9][14:].split()[0],lines[k+11][14:].split()[0]
					else:
						print lines[k+6][14:].split()[0],lines[k+7][14:].split()[0],lines[k+10][14:].split()[0],lines[k+11][14:].split()[0],"0.0000",
						print lines[k+13][14:].split()[0],lines[k+14][14:].split()[0],lines[k+16][14:].split()[0]	
~~~

批处理提取结果:

~~~bash
#! /bin/bash
 
for dir in `ls -d ????`;do
 
[ -d ${dir}/pbsa_1 ] || mkdir ${dir}/pbsa_1
 
cp  mmpbsa_result.py ${dir}/pbsa_1
cd ${dir}/${dir}_mdin
 
[ -f mmpbsa.out ] && mv mmpbsa.out ../pbsa_1/
[ -f mmpbsa.in ] && mv mmpbsa.in ../pbsa_1/
[ -f mmpbsa_out.log ] && mv mmpbsa_out.log ../pbsa_1/
 
cd ../pbsa_1
python  mmpbsa_result.py $dir mmpbsa.out
 
cd ../..
done
~~~

------
