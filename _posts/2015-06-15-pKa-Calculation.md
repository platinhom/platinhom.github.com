---
layout: post_mathjax
title: pKa Calculation
date: 2015-06-15 08:43:13
categories: CompCB
tags: CompBiol Python Bash
---

### PB-Based methods
First finite-difference PB (FDPB) solver for irregular shape was constructed by Bashford and Karplus(Bashford-1990).
Neilsen et al optimize the hydrogen-bond network in protein for PB-based pKa calculations.(Nielsen-2001)

由平衡常数公式可以推得:
$$\alg \Delta G^o (A,HA) &= RT\ln 10 (pH-pK_a) \ealg$$  
根据残基在溶液中一般pKa和在蛋白中pKa可以知道`pKa Shift=pKa'(protein)-pKa(solution)`,再根据该残基在两种状态的$\Delta G$可以知道:  

$$\alg pK'_a = pKa + \frac{1}{RT \ln 10}[\Delta G_p (A,HA) - \Delta G_s (A,HA)]\ealg$$ ,其中s代表溶液状态,p代表蛋白状态. 
 
计算从气相到溶液相的溶剂化能,根据热力学平衡有:  

$$\alg \Delta G_s(HA,A) = -\Delta G_{g/s}(HA)+\Delta G_{g}(HA,A)+\Delta G_{g/s}(A)+\Delta G_{g/s}(H)\ealg$$  

计算从气相到蛋白相的溶剂化能,根据热力学平衡有:  

$$\alg \Delta G_p(HA,A) = -\Delta G_{g/p}(HA)+\Delta G_{g}(HA,A)+\Delta G_{g/p}(A)+\Delta G_{g/p}(H)\ealg$$  

由于游离质子在溶液中,不受蛋白影响,故有$$\Delta G_{g/p}(H) = \Delta G_{g/s}(H)$$, 两式相减,有:  

$$\alg \Delta \Delta G_{solv} = \Delta G_p(HA,A)-\Delta G_s(HA,A ) = RT\ln 10(pK^p_a-pK^s_a)\\ = \Delta G_{g/p}(A)-\Delta G_{g/s}(A)-[\Delta G_{g/p}(HA)-\Delta G_{g/s}(HA)] \ealg$$  

可以通过PB方程求解得出每个物质的溶剂化能,从而根据上式解得$$pK^p_a - pK^s_a$$.

- Born Formula  
The Born Formula can calculate the a charged atom with a lower dielectric constant $$\varepsilon_{int}$$ immersed in a continuum media with a higher dielectric constant $$\varepsilon_{ext}$$. It can be used to calculate the solvation energy and check the accuracy of PB solver.

$$\alg \Delta G^{sol} = - \frac{Q^2}{2 \cdot 4 \cdot \pi \cdot \varepsilon_0 } \cdot \frac{1}{r} (\frac{1}{\varepsilon_{int}}-\frac{1}{\varepsilon_{ext}}) \ealg$$    

In the formula, $$e=1.602176565\times 10^{-19}C$$, $$\varepsilon_0=8.8541878176\times 10^{-12}F/m$$ (permittivity of free space), $$k=1.38\times 10^{-23}J/K, T=297.33K, NA=6.022\times 10^{23}, cal=4.184 J $$, $$\varepsilon_{int} \varepsilon_{ext}$$: interior dielectric constant and exterior dielectric constant.  

For example, Q=10e, $$\varepsilon_{int}=4.0$$, $$\varepsilon_{ext}=80.0$$, r=1 A, energy is -6673.71kT; $$\varepsilon_{int}=20.0$$, $$\varepsilon_{ext}=80.0$$, energy is -1024.255kT

$$\frac{e^2}{ 4 \cdot \pi \cdot \varepsilon_0 } \cdot \frac{1}{ \AA } \cdot \frac{NA}{kcal} = 332.06364261083113511637811411787 $$

- Coulombic energy
[Electric potential energy](https://en.wikipedia.org/wiki/Electric_potential_energy)

$$\alg U_E = \frac{1}{4 \pi \varepsilon_0 \cdot \varepsilon_{di}} \cdot \frac{1}{2} \cdot \sum_{i,j,i \neq j} (\frac{Q_i Q_j}{r_{ij}}) \ealg$$ 

A python script to calculate the Coulombic energy from pqr file: 

###### FILE: pqr2col.py

~~~ python
#! /usr/bin/env python
# -*- coding: utf8 -*-

# Author: Hom, Date: 2015.6.17
# To calculate the coulombic energy from pqr file.
# Usage: python pqr2col.py input.pqr [indi]
# Default interior dielectric is set to 1.

import os,sys
from math import *

if (__name__ == '__main__'):
	if (not(len(sys.argv) == 2 or len(sys.argv) == 3)):
		print "Please assign the pqr file."
		input()
		exit()
	indi=1.0
	if (len(sys.argv) == 3):
		indi=float(sys.argv[2])
	fname=sys.argv[1]
	fnamelist=os.path.splitext(fname)
	fr=open(fname)
	atomlist=[];#[[x,y,z,charge],..]
	for line in fr:
		items=line.split()
		if (items[0]=="ATOM" or items[0]=="HETATM"):
			atomlist.append([items[5],items[6],items[7],items[8]])
	totalatoms=len(atomlist);
	sum=0.0;
	for i in range(totalatoms):
		for j in range(i+1,totalatoms):
			x1=float(atomlist[i][0])
			y1=float(atomlist[i][1])
			z1=float(atomlist[i][2])
			x2=float(atomlist[j][0])
			y2=float(atomlist[j][1])
			z2=float(atomlist[j][2])
			r=sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
			sum=sum+(float(atomlist[i][3])*float(atomlist[j][3])*332.06364261/(r*indi))
	print "Total coulombic energy is "+str(sum)+" kcal/mol"
#end main
~~~

### Tools or server.

#### [APBS](http://www.poissonboltzmann.org/)

#### [DelPhi](http://wiki.c2b2.columbia.edu/honiglab_public/index.php/Software:DelPhi)
Ref: (Li-2012)

#### Amber-PB

**About APBS-Delphi-AmberPB please refer to another blog [Usage of Delphi-APBS-AmberPB](http://platinhom.github.io/2015/06/19/delphi-apbs-amberpbsa/)**

#### [PBEQ server](http://www.charmm-gui.org/?doc=input/pbeqsolver); 

### Empirical/Scoring function Based

- [PROPKA](https://github.com/jensengroup/propka-3.1)  
Empirical pKa predictors based on physical description of the desolvation and dielectric response for the protein. Most update 3.0 reference: (Olsson-2011, Søndergaard-2011)

- [Rosetta pKa](http://rosie.rosettacommons.org/pka)  
Consider side-chain ﬂexibility and use new scoring function incorporating a Coulomb electrostatic potential and optimizing the solvation reference energies for pKa calculations. (Kilambi-2012).


## Reference
<style>ol li{font-size:16px;padding:0;margin:2px 0 2px 36px} ol li strong{font-size:16px;padding:0;}</style>

1. Donald Bashford and Martin Karplus. pKa’s of  Ionizable Groups in Proteins:  Atomic Detail from a Continuum Electrostatic Model. Biochemistry **1990**, 29, 10219-10225. [ref](/pdf/reference/pKa-pI/pKa-PB.pdf)
2. An-Suei Yang, M. R. Gunner, Rosemary Sampogna, Kim Sharp, and Barry Honig. On the Calculation of pKas in Proteins. PROTEINS: Structure, Function, and Genetics **1993**, 15, 252-265. [ref](/pdf/reference/pKa-pI/On_the_calculation_of_pKas_in_protein.pdf)
3. Jens E. Nielsen and Gerrit Vriend. Optimizing the Hydrogen-Bond Network in Poisson–Boltzmann Equation-Based pKa Calculations. PROTEINS: Structure, Function, and Genetics **2001**, 43, 403–412. [ref](/pdf/reference/pKa-pI/Nielsen_et_al-2001-Proteins.pdf)
4. Sunhwan Jo, Miklos Vargyas, Judit Vasko-Szedlar, Benoît Roux and Wonpil Im. PBEQ-Solver for online visualization of electrostatic potential of biomolecules. Nucleic Acids Research, **2008**, 36, W270–W275. [ref](/pdf/reference/pKa-pI/NAR-PBEQ.pdf)
5. Mats H. M. Olsson, Chresten R. Søndergaard, Michal Rostkowski, and Jan H. Jensen. PROPKA3: Consistent Treatment of Internal and Surface
Residues in Empirical pKa Predictions. J. Chem. Theory Comput. **2011**, 7, 525–537. [ref](/pdf/reference/pKa-pI/olsson2011.pdf)
6. Chresten R. Søndergaard, Mats H. M. Olsson, Michaz Rostkowski, and Jan H. Jensen. Improved Treatment of Ligands and Coupling Effects in Empirical Calculation and Rationalization of pKa Values. J. Chem. Theory Comput. **2011**, 7, 2284–2295. [ref](/pdf/reference/pKa-pI/ct200133y.pdf)
7. Krishna Praneeth Kilambi and Jeffrey J. Gray. Rapid Calculation of Protein pKa Values Using Rosetta. Biophysical Journal. **2012**, 103, 587–595.[ref](/pdf/reference/pKa-pI/rosetta-pKa.pdf)
8. Lin Li, Chuan Li, Subhra Sarkar, Jie Zhang, Shawn Witham, Zhe Zhang, Lin Wang, Nicholas Smith, Marharyta Petukh and Emil Alexov. DelPhi: a comprehensive suite for DelPhi software and associated resources. BMC Biophysics **2012**, 5:9. [ref](/pdf/reference/pKa-pI/delphi-2012.pdf)

---
