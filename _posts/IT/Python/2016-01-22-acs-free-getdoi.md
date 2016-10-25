---
layout: post
title: acs免费文献的doi及下载地址抓取
date: 2016-01-21 21:52:18
categories: IT
tags: Python Internet
---

这套脚本完成两个任务 :

1. 从ACS某个Journal中抓取所有free download的pdf的DOI号
2. 根据DOI去ACS下载PDF

----------

### 脚本一

第一个脚本是爬虫抓取DOI号的, 需要安装requests和BeautifulSoup. 需要修改:

- 该journal的简称(例如bichaw是biochemistry的简称,新版本改在定义在一个`jtodo`的list内,所有的简称在`jshort`)  
- 输出文件, 这里是`outfileprefix`变量定义文件前缀 

当然, 这两个可以在sys.argv里获取, 自行修改吧.


~~~python
#! /usr/bin/env python

import os,sys,gc,glob
import re,difflib,time,random,copy
import requests,urllib2,urlparse
from optparse import OptionParser
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

############ Global setting #############
escaper=HTMLParser()
#disable requests warning
requests.packages.urllib3.disable_warnings()

outfileprefix="downacsc307"

jshort=['achre4', 'jafcau', 'ancham', 'aamick', 'bichaw', 'bcches', 'bomaf6', 'abseba', 'accacs', 'acscii', 'acbcct', 'jceda8', 'jceaax', 'jcisd8', 'acncdm', 'crtoec', 'chreay', 'jctcce', 'cmatex', 'acsccc', 'cgdefu', 'enfuem', 'esthag', 'estlcu', 'iechad', 'iecred', 'aidcbc', 'inocaj', 'jacsat', 'langd5', 'amlccd', 'mamobx', 'jmcmar', 'amclct', 'mpohbp', 'ancac3', 'nalefd', 'jnprdf', 'joceah', 'orlef7', 'oprdfk', 'orgnd7', 'acsodf', 'apchd5', 'jpcafh', 'jpcbfk', 'jpccck', 'jpclcd', 'jpchax', 'jprobs', 'ascefj', 'ascecg', 'asbcd6', 'cenear']
#jdone=['bichaw','jpcafh','jpccck', 'orlef7', 'joceah', 'jmcmar', 'inocaj','jacsat', 'acbcct','bomaf6']

jtodo=['jnprdf','mpohbp','jpclcd','jprobs']

scriptre=re.compile(r"<script(.|\n)*?</script>")
for i in range(len(jtodo)):
	loi="http://pubs.acs.org/loi/"+jtodo[i]

	rloi=requests.get(loi)
	simpletext=scriptre.sub('',rloi.text)
	sloi=BeautifulSoup(simpletext, "html.parser")
	rows=sloi.findChildren("div",attrs={'class':'row'})

	issueurl=[ row.a['href'] for row in rows ]

	f=open(outfileprefix+str(i)+".txt",'a')
	for ilink in issueurl:
		print "Doing: "+ilink
		tmp=ilink.split('/')
		#if (int(tmp[-2])>43):
		#	continue
		#if (int(tmp[-2]) == 43 and int(tmp[-1]) >=11):
		#	continue
		try:
			r=requests.get(ilink)
			rs=BeautifulSoup(scriptre.sub("",r.text), "html.parser")
			eds=rs.findChildren(attrs={'class':"icon-item editors-choice"})
			aus=rs.findChildren(attrs={'class':"icon-item author-choice"})
			outs= [ out.parent.findChild(attrs={'class':"icon-item pdf-high-res"}).a['href'] for out in eds+aus] 
			corr=rs.findChildren(attrs={'id':'AdditionsandCorrections'})
			outs=outs+[out.parent.parent.findChild(attrs={'class':"icon-item pdf-high-res"}).a['href'] for out in corr]
			for out in outs:
				f.write(out+'\n')  
			#'/doi/pdf/10.1021/acs.jmedchem.5b00326'
			sys.stdout.flush()
			f.flush()
		except:
			pass

	f.close()
~~~


### 脚本二

第二个脚本是抓取相应pdf的, 十分简单. 可以通用于ACS的抓取(别的杂志社要更改相应下载链接的解释). 没有检查抓取后的响应码. 也可以改为不需要requests的.

需要urllib2, time, glob, sys, os 其实足矣.

~~~python
#! /usr/bin/env python
 
import os,sys,gc,glob
import re,difflib,time,random,copy
import requests,urllib2,urlparse
from optparse import OptionParser
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
 
############ Global setting #############
escaper=HTMLParser()
#disable requests warning
requests.packages.urllib3.disable_warnings()
 
def quotefileDOI(doi):
        '''Quote the doi name for a file name'''
        return urllib2.quote(doi,'+/()').replace('/','@')
 
def unquotefileDOI(doi):
        '''Unquote the doi name for a file name'''
        return urllib2.unquote(doi.replace('@','/'))
 
f=open(sys.argv[1])
 
count=0
 
for line in f:
        doi=urllib2.unquote( line[line.find('10.'):].strip() )
        link="http://pubs.acs.org"+line.strip()
        # save file name
        fname=quotefileDOI(doi)+".pdf"
        r=requests.get(link)
        fw=open(fname,'wb')
        fw.write(r.content)
        fw.close()
        count+=1
        # When too much files(>300), move to a folder to upload to a server
        if (count>=300):
                for i in glob.iglob("*.pdf"):
                        os.renames(i,'Done/'+i)
                count=0
        time.sleep(random.randint(3,8))
f.close()
~~~

所有杂志和缩写

~~~javascript
{
achre4: 'accounts_chemical_research',
jafcau: 'agricultural_food_chemistry',
ancham: 'analytical_chemistry',
aamick: 'applied_materials_interfaces',
bichaw: 'biochemistry',
bcches: 'bioconjugate_chemistry',
bomaf6: 'biomacromolecules',
abseba: 'biomaterials',
accacs: 'catalysis',
acscii: 'central_science',
acbcct: 'chemical_biology',
jceda8: 'chemical_education',
jceaax: 'chemical_engineering_data',
jcisd8: 'chemical_information_modeling',
acncdm: 'chemical_neuroscience',
crtoec: 'chemical_research_toxicology',
chreay: 'chemical_reviews',
jctcce: 'chemical_theory_computation',
cmatex: 'chemistry_materials',
acsccc: 'combinatorial_science',
cgdefu: 'crystal_growth_design',
enfuem: 'energy_fuels',
esthag: 'environmental_science_technology',
estlcu: 'environmental_science_technology',
iechad: 'industrial_engineering_chemistry',
iecred: 'industrial_engineering_chemistry_research',
aidcbc: 'infectious_diseases',
inocaj: 'inorganic_chemistry',
jacsat: 'JACS',
langd5: 'langmuir',
amlccd: 'macro_letters',
mamobx: 'macromolecules',
jmcmar: 'medicinal_chemistry',
amclct: 'medicinal_chemistry_letters',
mpohbp: 'molecular_pharmaceutics',
ancac3: 'nano',
nalefd: 'nano_letters',
jnprdf: 'natural_products',
joceah: 'organic_chemistry',
orlef7: 'organic_letters',
oprdfk: 'organic_process_research_development',
orgnd7: 'organometallics',
acsodf: 'omega',
apchd5: 'photonics',
jpcafh: 'physical_chemistry_a',
jpcbfk: 'physical_chemistry_b',
jpccck: 'physical_chemistry_c',
jpclcd: 'physical_chemistry_letter',
jpchax: 'physical_chemistry'
jprobs: 'proteome_research',
ascefj: 'sensors',
ascecg: 'sustainable_chemistry',
asbcd6: 'synthetic_biology',
cenear: 'ce_n_archives'
}
~~~



------
