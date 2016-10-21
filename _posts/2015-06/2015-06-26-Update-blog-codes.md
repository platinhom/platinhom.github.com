---
layout: post
title: 更新博客代码块脚本
date: 2015-06-25 16:29:09
categories: IT
tags: Bash Git Python
---


今天国内时间生日啦~猪自己生快~~~ :)   国外第一次过生日呢! 昨晚加班就是把想法实现成脚本了, 测试通过~~不怕空格~~不过可能怕文件名有`:`.

该脚本用于自动更新博文内的代码块, 而代码块的内容源于脚本文件夹内的指定文件. 需要在博文的代码块上加载 `###### FILE: filename` 这么一段话才能识别被更新的代码块. 例如:

~~~~ markdown

contents...

###### FILE: update.sh

~~~ bash
codes...
codes......
~~~

You can even add the link as 

###### FILE: [update.sh](filelink)

~~~~

可知可以将该文件名注释作为链接也是可以的~~这里用的是Markdown的示例.

主要执行一个Bash脚本, 主运行函数在Python脚本内(python脚本要放置在scripts目录内,其实可以改进到bash里面指明吧). 使用直接运行Bash脚本即可, 可以在任意位置运行, 但需要先更改`scripts`目录以及`_posts`目录的地址.   
细节看脚本注释吧.


###### FILE: [UPDateFromScript.sh](/scripts/UPDateFromScript.sh)

~~~ bash
#! /bin/bash
# file: UPDateFromScript.sh
# Author: Platinhom, 2015.6.25

# A script to update the code block in the blog files.
# The code block should be between ~~~ ..... ~~~ 
# and has a line before the block: ###### FILE: sourcecode_file  

# Example:
# ###### FILE: UPDateFromScript.sh
# 
# ~~~ bash
# codes
# ~~~
# Also support the filename as link in markdown:
# ###### FILE: [UPDateFromScript.sh](link)

# You may change the two directories, saving the source code files and blog files.
sd="/Users/Hom/MyGit/Homepage/platinhom.github.com/scripts"
pd="/Users/Hom/MyGit/Homepage/platinhom.github.com/_posts"

# Check the existence of UPDateFromScript.py
if [ ! -f "${sd}/UPDateFromScript.py" ];then
	echo "UPDateFromScript.py is not in the scripts directory!";
	exit 1;
fi

# Check the existence of two directories
if [ ! \( \( -d "${sd}" \) -a \( -d "${pd}" \) \) ];then
	echo "Please assign the scripts and _post directory!";
	exit 1;
fi

# Start the script in the script directory.
cd $sd

### linkfile save the relation between source code file and blog files.
: > linkfile #clear the file
### Update the working time
date >> UPDateFromScript.log

### File the relationship between source code files and blog files.
### Only process the file with extension start at [bspcfrjv] here.
### bat/sh/csh/f90/py/pl/rb/vbs/js
for fii in *.[spcfrj]*
do
	###  !!!!!! sourcecode_file
	echo "!!!!!! $fii">>linkfile
	### Blog with md/html extension.
	grep "^###### FILE:" ${pd}/*.[mh]*[dl] | grep "$fii" | awk -F \: '{print $1}' >>linkfile
done

# IFS is seperate symbol.
# Avoid the blank to seperate file name, 
# Here we change it temply.
OLDIFS=$IFS
IFS=$'\n'

sourcefile=""
blogfile=""
for line in `cat linkfile`
do
	if [ ${line:0:6} = "!!!!!!" ];then
		sourcefile=${line:7};
	else
		blogfile=$line;
		# Run the program by UPDateFromScript.py !
		newfile=`python UPDateFromScript.py "$sourcefile" "$blogfile" | grep "!!! New file"`;

		if [ -z "${newfile}" ];then
			echo "$sourcefile and $blogfile with the same codes"!
		else
			# Notice the string return...
			sysOS=`uname -s`
			if [ $sysOS == "Darwin" -o $sysOS == "Linux" ];then
				newfile=${newfile:17};
			else
			# file string is different when python return in Window.
				newfile="${blogfile}-tmp.md"
			fi
			
			# Log the result difference
			echo $newfile $blogfile | tee -a UPDateFromScript.log;
			diff $newfile $blogfile | tee -a UPDateFromScript.log;
			# Replace the old file
			echo "Compare done! Stop 5s. If you need, Ctrl+C to cancel replacement!"
			sleep 5
			mv $newfile $blogfile
		fi
	fi
done

# Correct the IFS
IFS=$OLDIFS

# Come back to the last directory.
cd - > /dev/null
~~~

###### FILE: [UPDateFromScript.py](/scripts/UPDateFromScript.py)

~~~~ python
#! /usr/bin/env python
# -*- coding: utf8 -*-

# file: UPDateFromScript.py
# Author: Hom, Date: 2015.6.25
# A script with UPDateFromScript.sh to update the code blocks in blogs.
# Usage as: python UPDateFromScript.py sourcecode_file blog_file

import os,sys

# The main function to refresh the code block in blog.
# Input 1:source code file; 2:blog file containing code block.
# Return whether the codes are the same. 
def RefreshFile(fi,fu):
	fin=open(fi,'r');
	fui=open(fu,'r');
	scriptlines=fin.read();
	fin.close();

	bloglines=""
	blogscript=""
	findplace=False;
	findcode=False;
	codepre=""
	for line in fui:
		# Find the head: "###### FILE: scriptname"
		if (line[:6]=="######"):
			tmp=line.split()
			# revise to fi in tmp[2]. To support link as [filename](link)
			if (tmp[1].upper()[:4]=="FILE" and (fi in tmp[2])):
				#print fi,fu
				findplace=True;
				bloglines=bloglines+line;
				continue;
		# Find the code block beginning with ~~~ 
		if (findplace and (not findcode)):
			if (line[:3]=="~~~"):
				codepre=line.split()[0];
				findcode=True;
				bloglines=bloglines+line;
				continue;
		#Find the end of code block
		if (findplace and findcode):
			if (line[:3]=="~~~"):
					if (line.strip()==codepre):
						findcode=False;
						findplace=False;
						#Have read all the codes in blog
						#Compare the codes
						#Maybe a \n will add to blog codes.
						if (blogscript==scriptlines or blogscript==scriptlines+'\n'):
							fui.close();
							return True;
						else:
						# Different codes! Update the blog code by script code!
							bloglines=bloglines+scriptlines;
							if (scriptlines[-1] !='\n'):
								bloglines=bloglines+'\n'+line;
							else:
								bloglines=bloglines+line;
							continue;
			blogscript=blogscript+line;
			continue;
		bloglines=bloglines+line;	
	fui.close();
	fuo=open(fu+'-tmp.md','w');
	fuo.write(bloglines);
	fuo.close();
	return False;

if (__name__ == '__main__'):
	if (len(sys.argv)!=3):
		print "Make sure two input files run as: ./UPDateFromScript.py sourcecode_file blog_file!"
		exit(1)
	# read the input, avoid last \n
	fi=sys.argv[1].strip();
	fu=sys.argv[2].strip();
	if (RefreshFile(fi,fu)):
		print "!!! The codes are the same!"
	else:
		# Warning : This return string is important for UPDateFromScript.sh!
		print "!!! New file as: "+fu+'-tmp.md';
#end main
~~~~

---
