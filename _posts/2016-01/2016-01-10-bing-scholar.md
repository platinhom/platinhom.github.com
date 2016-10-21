---
layout: post
title: 必应学术搜索爬虫
date: 2016-01-10 08:54:26
categories: IT
tags: Website Python
---

`&filters=time%3age2014` (time:ge2014)大于等于2014

`&first=11` 从第11个结果开始.

暂时没找到别的好用的关键词..

### 搜索结果HTML架构: 

- body > div#b\_content > ol#b\_results >  li.b_algo 就是每个结果
- 搜索结果每条: 
	- h2 -> a : 结果title以及对应链接
	- div.b_caption : 后面的信息
		- div.b\_snippet -> div.b\_attribution -> cite : 就是链接地址
		- div.b\_snippet -> p : 就是摘要, 作者信息等.
		- div.sa\_uc -> ul.b\_vList -> li.b\_annooverride -> div.b\_acedemicanswer : 内含下面一块文献信息
			- div.b_hPanel (span 作者): 作者信息
			- div.b_hPanel (span 期刊): 期刊信息和年份
			- div.b_hPanel (span 关键字): 关键词信息
			- div.b\_factrow : 内含被引数和引用/下载的按钮
				- div.b_hPanel -> span 被引数 -> span 被引数量 -> span.b\_citeItem (含有data-paperid) 引用
				- div.b_hPanel -> span 被引数 -> span 被引数量 -> span.b\_downloadItem (含有data-paperid) 下载
- body > div#b\_content > ol#b\_results > li (data-bm) > div.b\_pag > ul > li > a 各种下一页.

### 引用和download

点击引用后显示的内容:

`http://mylib.chinacloudsites.cn/Paper/Bibliography/%PaperId%`

点击相应文献工具后对应的:

- BibTeX: `http://mylib.chinacloudsites.cn/Paper/Citation/%PaperId%?type=bibtex`
- EndNote: 	`http://mylib.chinacloudsites.cn/Paper/Citation/%PaperId%?type=endnote`
- RefMan: `http://mylib.chinacloudsites.cn/Paper/Citation/%PaperId%?type=refman`
- RefWorks: `http://mylib.chinacloudsites.cn/Paper/Citation/%PaperId%?type=refworks`

点击下载后实际加载内容:

`http://mylib.chinacloudsites.cn/Paper/Download/%paperId%`

以上经测可以爬.

### 实践

以下是一段可以通过关键词爬bing academic抓pdf的python代码, 需要requests, beautifulsoup4 模块. 

妈蛋, `http://www.bing.com/academic/` 直接爬会404, 但浏览器正常,折腾了很久headers都无效. 后来发现了, 如果区域设置是米国, 该网页会404, 米国版的必应学术还不太一样.... 其中有个很关键的`{"mkt":"zh-CN"}`可以让爬虫指定中国形式,并且把搜素作为get参数params传递就可以解决404了.偶尔发现的,算lucky吧 ╮(╯▽╰)╭...

以类的形式实现功能(其实还可以创建record的一个类保存记录信息, 懒得弄了). 创建一个BingAcedemic类, 然后`grepBingAcadPDF("keyword",maxpage=3)`方法,maxpage是爬最多几页(每页10篇, 根据Bing的结果一般不多于10页,所以限制最大数量是10页.).如果要爬记录(bibtex或endnote), 自己修改bidref方法就好了.

只是个例子, 经测可用. 不再在此更新(懒癌...).

~~~python
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,re,requests,difflib
from bs4 import BeautifulSoup

#disable warning
requests.packages.urllib3.disable_warnings()


########## DOI and pdf tools library ####################
def quoteDOI(doi):
	'''Quote the doi name'''
	return requests.utils.quote(doi)

def unquoteDOI(doi):
	'''Unquote the doi name'''
	return requests.utils.unquote(doi)

def quotefileDOI(doi):
	'''Quote the doi name for a file name'''
	return quoteDOI(doi).replace('/','@')

def unquotefileDOI(doi):
	'''Unquote the doi name for a file name'''
	return unquoteDOI(doi.replace('@','/'))

def removeunicode(s):
	'''Remove non-ascii char'''
	out=''
	for i in range(len(s)):
		if (ord(s[i])<128):
			out+=s[i]
	return str(out)

def normalizeString(s):
	'''Replace [!a-zA-Z0-9_] to blank'''
	return re.sub("\W+",' ',s)

def getwebpdf(link,fname):
	'''Get a PDF from a link. if fail, return False'''
	try:
		rpdf=requests.get(link)
		if (rpdf.status_code is 200 and rpdf.headers['Content-Type'].lower().strip()=='application/pdf'):
			fpdf=open(fname,'wb')
			fpdf.write(rpdf.content)
			fpdf.close()
			return True
	except requests.exceptions.ConnectionError:
		print "Error to get pdf linK: "+link+" for file: "+fname
	return False

######## CrossRef records library #########

class crossrefrecord(object):
	'''Simple CrossRef Record just for check doi+title'''
	def __init__(self):
		self.title=""
		self.year=""
		self.doi=""
		self.volume=""
		self.issue=''
		self.pages=""

	def __repr__(self):
		return self.title+"; "+self.doi+"; "+self.year+"; "+self.volume+"; "+self.issue+"; "+self.pages
	def __str__(self):
		return self.__repr__()

	def reset(self):
		self.title=""
		self.year=""
		self.doi=""
		self.volume=""
		self.issue=''
		self.pages=""

	def crossrefdoi(self,doi):
		'''Get information from doi'''
		r=requests.get("http://api.crossref.org/works/"+doi)
		if (r.status_code is 200):
			data=r.json()['message']
			self.title=data.get('title',[''])[0]
			self.year=str(data['issued']['date-parts'][0][0])
			self.volume=data.get('volume','')
			self.issue=data.get('issue','')
			self.pages=data.get('page','')
			self.doi=data.get('DOI','')
			return True
		else:
			print "Error doi: "+doi
			return False

	def crossreftitle(self,title,year="",volume="",issue="",pages="", limit=3, offset=0, cutoff=0.9):
		'''Get information from journal title, better with year, volume, issue, pages information'''
		# Over limitation
		if (offset>limit):
			return False

		# search url
		url="http://api.crossref.org/works?query="+normalizeString(title)+"&rows=1&offset="+str(offset)
		if (year):
			#some time year maybe +- 1
			url+="&filter=from-pub-date:"+str(int(year)-1)+"-06,until-pub-date:"+str(int(year)+1)+"-06"	
		#print url
		
		# search crossref
		r=requests.get(url)
		if (r.status_code is 200):
			try:
				data=r.json()['message']['items'][0]
				#should better then cutoff
				if (float(data['score'])>cutoff):
					self.title=data.get('title',[''])[0]
					self.year=str(data['issued']['date-parts'][0][0])
					self.volume=data.get('volume','')
					self.issue=data.get('issue','')
					self.pages=data.get('page','')
					self.doi=data.get('DOI','')
					#check whether fitting to giving parameters
					if (year and year.strip()!=self.year.strip()): 
						if not (abs(int(year)-int(self.year)) is 1 and volume.strip()==self.volume.strip()):
							self.crossreftitle(title=title,year=year,volume=volume,issue=issue,pages=pages,limit=limit,offset=offset+1,cutoff=cutoff)
					if (volume and volume.strip()!=self.volume.strip()): 
						self.crossreftitle(title=title,year=year,volume=volume,issue=issue,pages=pages,limit=limit,offset=offset+1,cutoff=cutoff)
					if (pages and pages.strip().split('-')[0] !=self.pages.strip().split('-')[0]): 
						self.crossreftitle(title=title,year=year,volume=volume,issue=issue,pages=pages,limit=limit,offset=offset+1,cutoff=cutoff)
					#if (issue and issue.strip()!=self.issue.strip()): 
					#	self.crossreftitle(title=title,year=year,volume=volume,issue=issue,pages=pages,limit=limit,offset=offset+1,cutoff=cutoff)
					return True
				else:
					self.crossreftitle(title=title,year=year,volume=volume,issue=issue,pages=pages,limit=limit,offset=offset+1,cutoff=cutoff)
					return False
				if (offset>limit): print "Over limit for finding title:"+title.encode('utf-8')
			except:
				print "Something error for finding "+title.encode('utf-8')
				return False
		else:
			print "Journal title can't be found: "+title.encode('utf-8')
			return False			

############# Endnote relate libraray ##############

def enwparse(enw):
	'''Parse the endnote enw file, return dict'''
	result={'journal':"",'year':'','volume':"",'issue':'','pages':'','title':'','author':[]}
	lines=enw
	if (not isinstance(enw,file)):
		lines=enw.splitlines()
	for line in lines:
		if (len(line)>1):
			item=line[1]
			if item=="T":
				result['title']=line[3:].strip()
			elif item=="D":
				result['year']=line[3:].strip()
			elif item=="P":
				result['pages']=line[3:].strip()
			elif item=="J":
				result['journal']=line[3:].strip()
			elif item=="V":
				result['volume']=line[3:].strip()
			elif item=="N":
				result['issue']=line[3:].strip()
			elif item=="A":
				result['author'].append(line[3:].strip())
	return result

############### Bing Academey Search Related ########################

class BingAcedemic(object):
	'''A class for Bing Academic Search'''

	# Global var for bing search, only valid when bing search is using China region!			
	bingacademicurl="http://www.bing.com/academic/"
	hdr={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',\
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',\
'Connection':'keep-alive','Content-Encoding': 'gzip','Content-Type': 'text/html; charset=utf-8','Host':'www.bing.com'}
	# re for extract BID in download/citation
	bidre=re.compile(r'(?<=data-paperid=\")\w+?(?=\">)')

	def bingacademicResultID(self,inq,maxpage=1):
		'''Get maxpage pages record ID in searching results for inq keyword in bing academic'''
		inq=re.sub(r"\s+","+",inq)
		bids=[]
		if (maxpage<1):maxpage=1
		if (maxpage>10):maxpage=10
		for pagei in range(maxpage):
			startpage=pagei*10+1
			param={"mkt":"zh-CN",'q':inq,'first':str(startpage)}
			r=requests.get(self.bingacademicurl,params=param,headers=self.hdr)
			if (r.status_code is 200):
				soup=BeautifulSoup(r.text, "html.parser")
				findpdflinkresult=soup.find_all(attrs={"class":"b_citeItem"})
				bids=bids+[self.bidre.search(str(s)).group() for s in findpdflinkresult]
		return bids

	def bingacademicPDFid(self,inq,maxpage=1):
		'''Get maxpage pages pdf links in searching results for inq keyword in bing academic'''
		inq=re.sub(r"\s+","+",inq)
		bids=[]
		if (maxpage<1):maxpage=1
		if (maxpage>10):maxpage=10
		for pagei in range(maxpage):
			startpage=pagei*10+1
			param={"mkt":"zh-CN",'q':inq,'first':str(startpage)}
			r=requests.get(self.bingacademicurl,params=param,headers=self.hdr)
			if (r.status_code is 200):
				soup=BeautifulSoup(r.text, "html.parser")
				findpdflinkresult=soup.find_all(attrs={"class":"b_downloadItem"})
				bids=bids+[self.bidre.search(str(s)).group() for s in findpdflinkresult]
		return bids

#### Example to avoid exceed retry.
#requestsSession = requests.Session()
#requestsAdapterA = requests.adapters.HTTPAdapter(max_retries=3)
#requestsSession.mount('http://', requestsAdapterA)
#requestsSession.mount('https://', requests.adapters.HTTPAdapter(max_retries=3))

	def bidpdflink(self,bid):
		'''Get PDF link from bing ID'''
		requestsSession = requests.Session()
		requestsSession.mount('http://', requests.adapters.HTTPAdapter(max_retries=5))
		try:
			r=requestsSession.get("http://mylib.chinacloudsites.cn/Paper/Download/"+str(bid),timeout=20)
			pdflinks=[]
			if (r.status_code is 200):
				results=r.json()['result']
				for result in results:
					pdflinks.append(result.get('link',''))
			return pdflinks
		except requests.exceptions.ConnectionError:
			print "ConnectionError: Fail to find pdf link for bid: "+bid
			return []

	def bidref(self,bid):
		'''Get reference information from bing ID'''
		requestsSession = requests.Session()
		requestsSession.mount('http://', requests.adapters.HTTPAdapter(max_retries=5))
		try:
			r=requestsSession.get("http://mylib.chinacloudsites.cn/Paper/Citation/"+str(bid)+"?type=endnote",timeout=20)
			if (r.status_code is 200):
				return enwparse(r.text)
			return enwparse('')
		except requests.exceptions.ConnectionError:
			print "ConnectionError: Fail to find ref info for bid: "+bid
			return enwparse('')

	def getbidpdf(self,bid,filename=None,printyn=True):
		'''Try to get pdf file based on bing id to a filename'''
		if (not filename): filename=bid+".pdf"
		pdflink=self.bidpdflink(bid)
		if (printyn): print pdflink
		for pl in pdflink:
			if (getwebpdf(pl,fname=filename)):
				break
		if (os.path.exists(filename)):
			return True
		return False

	def grepBingAcadPDF(self,keyword,maxpage=1,printyn=True):
		'''Grep at most maxpage pages pdf for searching keyword.
		Save to doi style based on refering to crossref.'''
		bids = self.bingacademicPDFid(keyword,maxpage)
		cr=crossrefrecord()
		for bid in bids:
			#if (bid=='68F37860'):
				ref=self.bidref(bid)
				if (printyn):
					print
					print "Finding for "+bid+"...."
					print ref
				if (os.path.exists(bid+".pdf")):
					continue
				if ref['title']:
					if (cr.crossreftitle(title=ref['title'],year=ref['year'],volume=ref['volume'],pages=ref['pages'],issue=ref['issue']) and cr.doi):
						if (printyn): print cr.__repr__().encode('utf-8')
						outname=quotefileDOI(cr.doi)+".pdf"
						if (not os.path.exists(outname)):
							self.getbidpdf(bid,filename=outname,printyn=printyn)
					else:
						self.getbidpdf(bid,filename=bid+".pdf",printyn=printyn)
				else:
					self.getbidpdf(bid,filename=bid+".pdf",printyn=printyn)
				cr.reset()
	def findcrossreftitledoi(self,doi,printyn=True):
		'''Find doi by crossref first'''
		cr=crossrefrecord()
		if( cr.crossrefdoi(doi) and cr.doi):
			keyword=cr.title+" "+cr.doi
			self.grepBingAcadPDF(keyword=keyword,maxpage=1,printyn=printyn)
		else:
			print "Error DOI!: "+doi
		cr.reset()

if __name__ == "__main__":
	bingacad=BingAcedemic()
	bingacad.grepBingAcadPDF("shoichet",maxpage=3)
~~~



------
