---
layout: post
title: Amber输入结构的预处理
date: 2015-06-14 04:18:41
categories: CompCB
tags: Amber Python CompBiol
---

一般地,包括以下几个步骤

- 蛋白/核酸结构处理
- 水分子保留/去除
- 小分子配体处理
- Amber力场参数化

### 蛋白结构处理
蛋白结构经常会出现结构的不完整,如(1)结构片段缺失(尤其loop);(2)残基结构不完整甚至出错;(3)二硫键问题.  
商业软件有很多流程专门对蛋白结构进行预处理,如Schrodinger的[Protein Preparation Wizard](http://www.schrodinger.com/Protein-Preparation-Wizard/),MOE的[Automated Structure Preparation](https://www.chemcomp.com/MOE-Protein_and_Antibody_Modeling.htm#AutomatedStructurePreparation)等,在此暂不论述.   
一种处理方法使用Modeller等对缺失结构进行建模,也可以在Chimera中使用Model Loop方法重构和Rotamer来补充缺失侧链.这部分论述要比较多的时间,有空再写或另开章节了.总之要注意的就是上述几点了.

- Schrodinger的Protein Preparation说明[pdf](http://helixweb.nih.gov/schrodinger-2013.3-docs/general/protein_prep.pdf)

### 蛋白加氢和电荷
MD时结构是需要带氢的,并且需要带上电荷.一般电荷采用残基上的原子力场中相应电荷进行处理.这里推荐使用[PDB2PQR](http://nbcr-222.ucsd.edu/pdb2pqr_2.0.0/)处理.也可以使用Chimera进行相应处理.  

- 其中forcefield和output naming scheme均选择Amber.
- pKa一般选择ph=7下用PROPKA处理即可,用来对残基pKa进行预测并质子化处理.
- `Available options`提供更多功能和选项,一般选择:
	- `Ensure that new atoms are not rebuilt too close to existing atoms`避免加氢立体冲突;
	- `Optimize the hydrogen bonding network`优化H键网络;
	- `Add/keep chain IDs in the PQR file`保留链名(可不选);
	- `Create an APBS input file`利用APBS计算静电势.

###水分子
部分结构是含有结晶水的,保守结晶水对结构可能十分重要,可以通过Chimera一类软件选择保留. 去除水分子也可以很简单通过PDB2PQR处理或者在Chimera/Pymol中删掉.处理方法太多了...  
在Amber文件中, 结晶水应该是WAT的分子,其原子是`O `,`H1`和`H2`.在下载文件用moe处理或直接下载下来时, O变了OW,H变为HW.类型变为`HETATM`.此时要作以下预处理: 
  
- 因此要修改为`ATOM^^`这里`^`表示两个空格.  
- `OW`变为`O^`, `HW`分别变为`H1`和`H2`.  

~~~ python
#! /usr/bin/env python
# Author:Hom,2015-06-14
# To correct the water expression in PDB file

inputfile="input.pdb"
outputfile="output.pdb"

fi=open(inputfile,'r')
fo=open(outputfile,'w')
for line in fi:
	if len(line.split())>=4:
		if line.split()[3]=='WAT':
			# 记得ATOM后面两个空格
			line=line.replace('HETATM','ATOM  ')
			if line.split()[2]=='OW':
				count=1
				line=line.replace('OW','O ') #是O+空格
			if line.split()[2]=='HW':
				if count==1:
					line=line.replace('HW','H1')
					count=count+1
				if count==2:
 					line=line.replace('HW','H2')
					count==0
	fo.write(line)
fi.close();fo.close()
~~~

### TER处理
使用Amber时,链的尾部要加TER标明结束!如果MD出了问题或者处理出错,可以检查TER的处理.  
链最好带不同名字区分..另外注意AMBER的tleap处理会将链头和链尾处理为NLEU,CLEU这样区分,所以链的TER很重要,最好先把蛋白整条链补全,参见MOE的缺失残基补全方法.(包括残基原子缺失).  
自动写入TER的好方法是使用MOE处理,尤其注意水要全部先选上(select-solvent),然后SE-Edit-split chain分割成好多条链.保存时,pdb有选项可选AMBER格式.另外要勾选每条链后写TER的选项,切记!另一种暴力办法就是自己写入了..

更多处理如小分子参数化等,To be Continue..
---
