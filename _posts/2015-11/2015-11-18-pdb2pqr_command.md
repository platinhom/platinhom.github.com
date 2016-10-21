---
layout: post_small
title: pdb2pqr命令行使用
date: 2015-11-17 18:21:55
categories: CompCB
tags: CompBiol Software
---

PDB2PQR是[Nathan Baker Group](http://www.poissonboltzmann.org/)开发维护的蛋白电荷处理系统, 能够将pdb输入的蛋白结构输出为pqr格式带原子电荷和原子半径的文件. pdb2pqr可以使用多种力场来参数化蛋白, 并且可以添加氢原子并优化氢键网络, 修复残基缺失侧链, 判断二硫键, 计算指定pH下残基pKa来计算质子化状态. 输出pqr文件还可以根据力场规范格式化残基和原子类型, 用于动力学输入. 

如果仅仅对少量的蛋白进行处理, 推荐使用的[PDB2PQR服务器](http://nbcr-222.ucsd.edu/pdb2pqr_2.0.0/)进行, 十分简易. 类似功能的还有[H++ server](http://biophysics.cs.vt.edu/index.php), 但没有相应命令行工具只能逐一处理.

PDB2PQR也可以在命令行使用, 可以在其[主页注册下载](http://www.poissonboltzmann.org/docs/downloads/)命令行工具, 也可以直接从[github](https://github.com/Electrostatics/apbs-pdb2pqr)上克隆. 这里采用github方式安装.

~~~bash
git clone git@github.com:Electrostatics/apbs-pdb2pqr.git
cd apbs-pdb2pqr/pdb2pqr
python scons/scons.py install
~~~

默认安装位置在~/pdb2pqr, 可以修改`build_config.py`配置文件来设置安装的一些选项, 例如去注释后修改`PREFIX="~/pdb2pqr"`可以更改默认安装路径, 另外还包括不按照pdb2pka等.可自行参考文件说明.

可以选择性安装PDB2PKA程序, 一个基于APBS计算蛋白PKA的的程序; 默认情况下使用[PROPKA](https://github.com/jensengroup/propka-3.0)来计算残基pKa. 现在版本的PDB2PQR仍然使用PROPKA3.0, 该版本不支持小分子处理.

-------------

命令行选项原始页面[参考](http://www.poissonboltzmann.org/docs/pdb2pqr-usage/). 这里摘录并翻译之.

程序用法概要: 

`python pdb2pqr.py [options] --ff={forcefield} {path} {output-path}`

其中path和output-path分别是输入和输出文件名称. 如果{path}是PDB的ID号, 会从PDB数据库下载.

## OPTIONS
- -\-version	
	- show program's version number and exit
	- 显示程序版本并退出
- -h, -\-help	
	- show this help message and exit
	- 显示帮助信息并退出

## MANDATORY OPTIONS
One of the options must be used. 最少使用以下其中一个的选项.

- **-\-ff=FIELD_NAME**
	- The forcefield to use - currently amber, charmm, parse, tyl06, peoepb and swanson are supported.
	- 使用的力场, 可选为amber, charmm, parse, tyl06, peoepb 和 swanson
- -\-userff=USER\_FIELD\_FILE	
	- The user created forcefield file to use. Requires -\-usernames overrides -\-ff
	- 用户指定的力场文件. 另外需要-\-usernames来覆盖掉原来的力场.
- -\-clean	
	- Do no optimization, atom addition, or parameter assignment, just return the original PDB file in aligned format. Overrides -\-ff and -\-userff
	- 不进行优化, 添加原子或者指定参数. 只返回原始PDB文件的PQR对齐格式, 会使-\-ff and -\-userff选项无效.

## GENERAL OPTIONS
- -\-nodebump	
	- Do not perform the debumping operation
	- 不要进行debump操作. 就是确保构建新的原子不会太靠近于已有原子.
- -\-noopt	
	- Do not perform hydrogen optimization
	- 不进行氢键网络优化.
- **-\-chain**
	- Keep the chain ID in the output PQR file
	- 保留原始的链ID号到PQR文件中.
- -\-assign-only	
	- Only assign charges and radii - do not add atoms, debump, or optimize.
	- 只进行电荷和半径的计算添加. 不进行加氢, debump和优化.
- -**\-ffout=FIELD_NAME**	
	- Instead of using the standard canonical naming scheme for residue and atom names, use the names from the given forcefield - currently amber, charmm, parse, tyl06, peoepb and swanson are supported.
	- 使用指定力场命名方法来命令原子和残基, 而不是使用标准的命名策略. 支持: amber, charmm, parse, tyl06, peoepb 和 swanson.
- -\-usernames=USER\_NAME\_FILE	
	- The user created names file to use. Required if using -\-userff
	- 用户创建的力场名字文件, 当使用-\-userff选项时需要该选项指定文件.
- -\-apbs-input	
	- Create a template APBS input file based on the generated PQR file. Also create a Python pickle for using these parameters in other programs.
	- 创建作为APBS输入的临时文件. 同样创建一份Python的pickle用于其余程序读取这些参数.
- -\-ligand=PATH	
	- Calculate the parameters for the ligand in mol2 format at the given path. Pdb2pka must be compiled.
	- 在使用propka计算pKa时无法处理小分子. 可以使用mol2分子指定小分子的输入(原小分子结构会被弃掉),根据小分子mol2格式读入参数.需要编译出pdb2pka. mol2需要sybyl原子类型, 并且需要原子名称不能重复.
- -\-whitespace	
	- Insert whitespaces between atom name and residue name, between x and y, and between y and z.
	- 在原子名称-残基名, x坐标-y坐标, y坐标-z坐标 间插入空格
- -\-typemap	
	- Create Typemap output.
	- 构建Typemap 输出
- -\-neutraln	
	- Make the N-terminus of this protein neutral (default is charged). Requires PARSE force field.
	- 使得N-氮端的蛋白残基中性化(默认会被带电化). 需要使用PARSE力场.
- -\-neutralc	
	- Make the C-terminus of this protein neutral (default is charged). Requires PARSE force field.
	- 使得C-碳端的蛋白残基中性化(默认会被带电化). 需要使用PARSE力场.
- -v, --verbose	
	- Print information to stdout.
	- 将信息输出到屏幕.
- -\-drop-water	
	- Drop waters before processing protein. Currently recognized and deleted are the following water types:HOH, WAT
	- 在处理蛋白前先去水分子(默认不去水分子). 现在支持识别被删掉的水分子需要残基名为: HOH, WAT.
- -\-include_header	
	- Include pdb header in pqr file. WARNING: The resulting PQR file will not with APBS versions prior to 1.5
	- 包括pdb原来的head信息到输出的pqr文件中. 注意: 使用该选项生成的PQR文件不能被APBS 1.5版本以下所识别.

## PH OPTIONS
- **-\-ph-calc-method=PH\_METHOD**	
	- Method used to calculate ph values. If a pH calculation method is selected, for each titratable residue pH values will be calculated and the residue potentially modified after comparison with the pH value supplied by -\-with_ph 
		1. PROPKA - Use PROPKA to calculate pH values. Actual PROPKA results will be output to .propka. 
		2. PDB2PKA - Use PDB2PKA to calculate pH values. Requires the use of the PARSE force field. Warning: Larger residues can take a very long time to run using this method. EXPERIMENTAL!
	- 计算pH的方法, 用于指认残基的质子化状态. 每个可滴定残基的pKa会被计算, 并和环境pH值(-\-with_ph来给定)进行比较从而确定质子化状态. 以下是可用的PH\_METHOD (注意命令行是小写!!):
		1. PROPKA - 使用PROPKA方法去计算pH值, 实际PROPKA结果会输出到propka后缀的文件中.
		2. PDB2PKA - 使用PDB2PKA方法去计算pH值. 需要使用PARSE力场. 注意: 如果要计算的残基较多, 可能计算耗时会很长.

- **-\-with-ph=PH**	
	- pH values to use when applying the results of the selected pH calculation method. Defaults to 7.0
	- 用于计算质子化状态时的环境pH值, 缺省是7.0.

## PDB2PKA OPTIONS
- -\-pdb2pka-out=PDB2PKA\_OUT	
	- Output directory for PDB2PKA results. Defaults to pdb2pka_output.
- -\-pdb2pka-resume	
	- Resume run from state saved in output directory.
- -\-pdie=PDB2PKA_PDIE	
	- Protein dielectric constant. Defaults to 8
- -\-sdie=PDB2PKA_SDIE	
	- Solvent dielectric constant. Defaults to 80
- -\-pairene=PDB2PKA_PAIRENE	
	- Cutoff energy in kT for calculating non charged-charged interaction energies. Default: 1.0

## PROPKA OPTIONS

- -\-propka-reference=PROPKA_REFERENCE	
	- Setting which reference to use for stability calculations. See PROPKA 3.0 documentation.
	- 设置propka稳定性计算的参考. 详见PROPKA 3.0的文档.
- -\-propka-verbose	
	- Print extra proPKA information to stdout. WARNING: This produces an incredible amount of output.
	- 输出propka的额外计算信息到屏幕. 注意, 可能会产生大量的输出结果.

## EXTENSION OPTIONS

- -\-chi	
	- Print the per-residue backbone chi angle to {output-path}.chi
- -\-summary	
	- Print protein summary information to {output-path}.summary.
- -\-contact	
	- Print a list of contacts to {output-path}.con
- -\-newresinter	
	- Print interaction energy between each residue pair in the protein to {output-path}.newresinter.
- -\-salt	
	- Print a list of salt bridges to {output-path}.salt

## HBOND EXTENSION OPTIONS

- -\-hbond	
	- Print a list of hydrogen bonds to {output-path}.hbond
	- 输出氢键信息到hbond后缀文件.
- -\-whatif	
	- Change hbond output to WHAT-IF format.
	- 更改氢键输出为WHAT-IF格式
- -\-angle\_cutoff=ANGLE_CUTOFF	
	- Angle cutoff to use when creating hbond data (default 30.0)
	- 氢键判断的角度截断值(缺省30.0度)
- -\-distance\_cutoff=DISTANCE_CUTOFF	
	- Distance cutoff to use when creating hbond data (default 3.4)
	- 氢键判断的距离截断值(缺省3.4 A)
- -\-old\_distance\_method	
	- Use distance from donor hydrogen to acceptor to calculate distance used with -\-distance\_cutoff.
	- 使用旧的氢键距离方法, 就是使用供体氢原子到受体原子的距离. 截断取决于-\-distance\_cutoff.

## RESINTER EXTENSION OPTIONS
- -\-resinter	
	- Print interaction energy between each residue pair in the protein to {output-path}.resinter.
	- 输出蛋白中每个残基对的相互作用能量到.resinter后缀文件.
- -\-residue_combinations	
	- Remap residues to different titration states and rerun resinter appending output. Consider only the minimum number of whole protein titration combinations needed to test each possible pairing of residue titration states. Normally used with -\-noopt. If a protein titration state combination results in a pair of residue being re-tested in the same individual titration states a warning will be generated if the re-tested result is different. This warning should not be possible if used with -\-noopt.
- -\-all\_residue\_combinations	
	- Remap residues to ALL possible titration state combinations and rerun resinter appending output. Results with -\-noopt should be the same as -\-residue_combinations. Runs considerably slower than -\-residue\_combinations and generates the same type of warnings. Use without -\-noopt to discover how hydrogen optimization affects residue interaction energies via the warnings in the output.

## RAMA EXTENSTION OPTIONS
- -\-rama	
	- Print the per-residue phi and psi angles to {output-path}.rama for Ramachandran plots
	- 输出每个残基的phi和psi角度到rama后缀文件,用于Ramachandran图.
- -\-phi_only	
	- Only include phi angles in output. Rename output file {output-path}.phi
	- 只输出phi角度到结果, 重命名结果为phi后缀.
- -\-psi_only	
	- Only include psi angles in output. Rename output file {output-path}.psi
	- 只输出psi角度到结果, 重命名结果为psi后缀.

-----------

## 实例

### 蛋白处理,Amber输入:

`pdb2pqr --ff=amber --ffout=amber --verbose --chain --ph-calc-method=propka --with-ph=7.0 protein.pdb protein.pqr`

要是要去除水分子:

`pdb2pqr --ff=amber --ffout=amber --verbose --chain --ph-calc-method=propka --with-ph=7.0 --drop-water protein.pdb protein.pqr`

### 使用配体进行处理,Amber输入

`pdb2pqr --ff=amber --ffout=amber --verbose --chain --ph-calc-method=propka --with-ph=7.0 --ligand ligand.mol2 protein.pdb protein.pqr`

------
