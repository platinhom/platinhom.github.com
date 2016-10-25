---
layout: post
title: W3School离线版去掉恼人的广告
date: 2015-12-01 11:17:33
categories: Coding
tags: Python Website
---

W3School离线版(html版)[下载](/ManualHom/Coding/W3School/W3Schools_Offline_2015-ProgramEsecure.7z), 去除广告后[效果](/ManualHom/Coding/W3School/W3Schools_Offline_2015/www.w3schools.com/).

~~~bash
#! /bin/bash
for f in *.html */*.html
do
python deleteAD.py "${f}"
done
~~~

主要执行脚本deleteAD.py

~~~python
#! /usr/bin/env python

import os,sys

f=open(sys.argv[1])
lines=f.readlines()
f.close()

fw=open(sys.argv[1],'w')

lineno=0
total=len(lines)
mark1=False; mark2=False; mark3=False;
revise=False
stepmark=0;
for i in range(lineno,total):
	if (not mark1 and "function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']"\
	    in lines[i] and "<script>" in lines[i-1]):
		fw.writelines(lines[lineno:i-1])
		stepmark=i-1
		mark1=True
		continue
	if (mark1==True and not mark2 and "var zbeforeResize = window.innerWidth;" in lines[i]):
		mark2=True
		continue
	if (mark1==True and mark2==True and "</script>" in lines[i]):
		mark1=False;mark2=False;lineno=i+1;
		revise=True
		break

# never find "var zbeforeResize = window.innerWidth;"
if (mark1==True and mark2==False):
	fw.writelines(lines[stepmark:])
	fw.close()
	exit()
# never find function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']
if (revise==False and mark1==False and mark2==False):
	fw.writelines(lines)
	fw.close()
	exit()

revise=False

findupblock=False;
for i in range(lineno,total):

	# revise the line. delete top AD div
	if (not findupblock and "<div id='mainLeaderboard'" in lines[i] and "<div id='div-gpt-ad" in lines[i]):
		j=lines[i].find("<div id='mainLeaderboard'"); k=lines[i].find("</script>")
		postpart=lines[i][k:]
		l=postpart.find("<div")
		newline=lines[i][:j]+postpart[l:]
		lines[i]=newline
		findupblock=True
		continue

	if (not mark1 and "<!-- SmallPS -->" in lines[i] \
		and "div-gpt-ad" in lines[i+1] and "<div style=" in lines[i-1]):
		fw.writelines(lines[lineno:i-1])
		stepmark=i-1
		mark1=True
		continue
	if (mark1==True and not mark2 and "<li id=\"facebook\">" in lines[i]):
		mark2=True
		continue
	if (mark1==True and mark2==True and "</script>" in lines[i]):
		mark3=True;
		continue
	if (mark1==True and mark2==True and mark3==True and "<div" in lines[i] and "</div>" in lines[i-1]):
		mark1=False;mark2=False;mark3=False;
		revise=True
		lineno=i
		break

## Don't find </div>\n<div ...>
## Don't find </script>, never happen
## Find SmallPS, but not facebook.. 
## Don't find mark1..
if (mark1==True):
	lineno=stepmark

fw.writelines(lines[lineno:]);
fw.close()
~~~

------
