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
