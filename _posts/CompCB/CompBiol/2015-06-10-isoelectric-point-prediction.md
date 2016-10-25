---
layout: post
title: 蛋白等电点预测
date: 2015-06-10 05:05:10
categories: CompCB
tags: CompBiol
---
# Prediction of pI(isoelectric point) of protein

等电点 [Isoelectric point](http://en.wikipedia.org/wiki/Isoelectric_point)是分子在溶液中不带电荷时的pH值,一般简称pI,pH(I),IEP. 等电点对电泳, 蛋白电泳/跑胶都十分重要.

一个只含有一个羧基和一个氨基的氨基酸等电点近似为:![氨基酸等电点](http://upload.wikimedia.org/math/f/f/7/ff7d10ea86b5d02228752ee25d77b112.png)

对于蛋白等电点预测,一般都使用[Henderson-Hasselbach equation](http://en.wikipedia.org/wiki/Henderson%E2%80%93Hasselbalch_equation)来计算某pH下蛋白电荷.   

- 对于负电荷氨基酸:![](http://isoelectric.ovh.org/files/pI1.png);   
- 对于正电荷氨基酸:![](http://isoelectric.ovh.org/files/pI2.png).
- 酸性AA:pka小到大:D(Asp, alpha酸),E(Glu,beta酸),C(Cys, -SH),Y(Tyr,酚);碱性AA:pka小到大:H(His,咪唑),K(Lys,4C-胺),R(Arg,3C-胍).
- 蛋白氮端(N-terminal, 含有-NH2)和碳端(C-terminal.含有-COOH)也要被考虑
- 在计算中, 要主要是否修饰,包括磷酸化,甲基化,NC端封端(-Ac或-OEt化一类)等情况进行修正.
- Cys的巯基可能会参与二硫键或被氧化而导致结果不同.
- 该些残基邻近有带电荷残基时亦会影响pI.

### pI预测工具
- [Protcalc](http://protcalc.sourceforge.net/)
- [ExPASy tool-Compute pI/Mw](http://web.expasy.org/compute_pi/)
- [Prot pi](https://www.protpi.ch/Calculator/ProteinTool)
- [L.P. Kozlowski server](http://isoelectric.ovh.org/)
- [DNAma软件](http://www.lynnon.com/)

---
