---
layout: post
title: 根据ID抓取EMD数据信息
date: 2015-08-09 07:07:00
categories: CompCB
tags: CompBiol EMD Python
---

这是以前用来统计EMD数据库中有fitting的EMD有多少, 格点和分辨率多少等.  

使用就是脚本+EMD编号即可.

要新加新的抓取信息部分自行添加了~使用到python的正则表达式模块re,网页模块urllib2.

## 简化版:

返回: EMDID FitPDB GridSize Resolution

~~~python
#! /usr/bin/env python
# File: EMDwebAnalyser.py
#
# To get EMD information from EMD databank
# Usage: python EMDwebAnalyser.py 1149
# Return: EMDID FitPDB GridSize Resolution (1149 2BYU  3.33 16.50)
# Author: Zhixiong Zhao
# Last Upate: 2015.9.17

import urllib2,re,sys
if (len(sys.argv)<2):
        print "Please give a EMD number as first parameter!"
        exit()
emdnum=sys.argv[1];

#Get the corresponding PDB number from EMD number
# Emdatabank has updated its website....
#emdlink="http://www.ebi.ac.uk/pdbe/entry/EMD-"+emdnum;
#emdmaplink=emdlink+"/map"

# Use rutgers website..
emdlink="http://emsearch.rutgers.edu/atlas/"+emdnum+"_summary.html";
emdmaplink=emdlink.replace("summary","mapparams");
urlreq=urllib2.Request(emdlink);
emdweb=urllib2.urlopen(urlreq).read();
fstr=re.search('<td class="first"><a\s+?href=.*target="_atlas_external">(?P<emdnumber>.{4}?)</a>',emdweb);
if (fstr):
        pdbnum=fstr.group("emdnumber").upper();
else:
        pdbnum='    '

#Get the resolution
fstr=re.search('<a class="help" id="resolution" href="#">\s+?Resolution:\s+?</a></td><td width="" valign="top" class="first">(?P<Reso>.+?) &Aring;',emdweb);
if (fstr):
        reso=float(fstr.group("Reso"));
else:
        reso=-1.0;

#Get the Voxel spacing value (grid size)
urlreq=urllib2.Request(emdmaplink);
emdweb=urllib2.urlopen(urlreq).read();
fstr=re.search('<a class="help" id="voxelSpacing" href="#">Voxel spacing:</a></td><td class="first" width=""\s+?valign="top">(?P<spacing>.+?)&Aring;</td>',emdweb);
if (fstr):
        spacing=float(fstr.group("spacing"));
else:
        spacing=-1.0
print emdnum,pdbnum,"%5.2f"%spacing,"%5.2f"%reso;
~~~

## 深化版

返回: EMDID FitPDB GridSize Resolution Symmetry Rigid/Flex Software Protocol Title Sample

~~~python
#! /usr/bin/env python
# File: EMDwebAnalyser.py
#
# To get EMD information from EMD databank
# Usage: python EMDwebAnalyser.py 1149
#
# Return: EMDID FitPDB GridSize Resolution Symmetry Rigid/Flex Software Protocol Title Sample
# As: 1149::2BYU::16.5::3.33::T::rigid body::URO::Protocol: rigid body. One dimer of 1gme A and B,
# 	residues 43-137 and 146-151, was fitted in URO and tetrahedral symmetry was used to generate 
#	the other five dimers.::Dodecameric structure of the small heat shock protein Acr1 from 
#	Mycobacterium tuberculosis.::Recombinant protein Acr1 From M.Tuberculosis made in E.coli.
#
# Author: Zhixiong Zhao
# Last Upate: 2015.9.17

import urllib2,re,sys
if (len(sys.argv)<2):
        print "Please give a EMD number as first parameter!"
        exit()
emdnum=sys.argv[1];

#Get the corresponding PDB number from EMD number
# Emdatabank has updated its website....
#emdlink="http://www.ebi.ac.uk/pdbe/entry/EMD-"+emdnum;
#emdmaplink=emdlink+"/map"
#emdexplink=emdlink+"/experiment"

# Use rutgers website..
emdlink="http://emsearch.rutgers.edu/atlas/"+emdnum+"_summary.html";
emdmaplink=emdlink.replace("summary","mapparams");
emdexplink=emdlink.replace("summary","sample");

urlreq=urllib2.Request(emdlink);
emdweb=urllib2.urlopen(urlreq).read();
fstr=re.search('<td class="first"><a\s+?href=.*target="_atlas_external">(?P<emdnumber>.{4}?)</a>',emdweb);
if (fstr):
        pdbnum=fstr.group("emdnumber").upper();
else:
        pdbnum='    '

#Get the resolution
fstr=re.search('<a class="help" id="resolution" href="#">\s+?Resolution:\s+?</a></td><td width="" valign="top" class="first">(?P<Reso>.+?) &Aring;',emdweb);
if (fstr):
        reso=float(fstr.group("Reso"));
else:
        reso=-1.0;

#Get the Voxel spacing value (grid size)
urlreq=urllib2.Request(emdmaplink);
emdweb=urllib2.urlopen(urlreq).read();
fstr=re.search('<a class="help" id="voxelSpacing" href="#">Voxel spacing:</a></td><td class="first" width=""\s+?valign="top">(?P<spacing>.+?)&Aring;</td>',emdweb);
if (fstr):
        spacing=float(fstr.group("spacing"));
else:
        spacing=-1.0

#Get the software
urlreq=urllib2.Request(emdexplink);
emdweb=urllib2.urlopen(urlreq).read();
fstr=re.search('(<td width="" valign="top".*){4}.*id="software" href="#">Software.*(<td width="" valign="top".*){4}</a></td>\s+</tr>\s+<tr>\s+(<td width="" valign="top".*){4} class="first">(?P<softw>.+?)</td>(<td width="" valign="top".*){4}</td>\s+</tr>',emdweb);
if (fstr):
        softw=fstr.group("softw");
else:
        softw=""

#Get the protocol (rigid/flex)
fstr=re.search('(<td width="" valign="top".*){4}.*id="software" href="#">Software.*(<td width="" valign="top".*){4}</a></td>\s+</tr>\s+<tr>\s+(<td width="" valign="top".*){2} class="first">(?P<tmp2>.+?)</td>(<td width="" valign="top".*){6}</td>\s+</tr>',emdweb);
if (fstr):
        tmp2=fstr.group("tmp2");
else:
        tmp2=""

#Get the protocol details
fstr=re.search('(<td width="" valign="top".*){4}.*id="software" href="#">Software.*(<td width="" valign="top".*){4}</a></td>\s+</tr>\s+<tr>\s+(<td width="" valign="top".*){8} class="first">(?P<tmp8>.+?)</td>\s+</tr>',emdweb);
if (fstr):
        tmp8=fstr.group("tmp8");
else:
        tmp8=""

#Get the symmetry information
fstr=re.search('<td width="200" valign="top" align="right" class="first"><a class="help" id="imposedSymmetry" href="#">Imposed symmetry:</a></td><td width="" valign="top" class="first">(?P<symminfo>.+?)</td>',emdweb);
if (fstr):
        symminfo=fstr.group("symminfo")
else:
        symminfo=""

#Get the title information
fstr=re.search('<td valign="top" align="right" width="200"><a class="help" id="title" href="#">Title:</a></td><td align="left">(?P<title>.+?)</td>',emdweb);
if (fstr):
        title=fstr.group("title")
else:
        title=""

#Get the sample information
fstr=re.search('<td valign="top" align="right" width="200"><a class="help" id="sampleName" href="#">Sample:</a></td><td align="left">(?P<sample>(.|\s)+?)</td>',emdweb);
if (fstr):
        sample=fstr.group("sample")
else:
        sample=""

print emdnum+"::"+pdbnum+"::"+str(reso)+"::"+str(spacing)+"::"+symminfo+"::"+tmp2+"::"+softw+"::"+tmp8+"::"+title+"::"+sample;
~~~

## 批处理

以下脚本可以协助获取一系列EMD数据信息. 抓取后用Excel打开输出文件即可统计分析~

`./GetEMDInfo.sh 1000 9999`

~~~bash
#! /bin/bash
# File: GetEMDInfo.sh
for ii in `seq $1 $2`
do
python EMDwebAnalyser.py $ii >> emdinfo_$1.txt
#sleep 1
done
~~~

------
