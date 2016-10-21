#! /usr/bin/env python
# -*- coding: utf8 -*-

# file: pynewblog.py
# Author: Hom, Date: 2015.6.22
# A easy script to create new blog for Github with Jekyll
# Usage as: python pynewblog.py title [category tags]

import time,os,sys

# Here, you should assign the _post directory for creating blogs 
wd="C:\\Users\\Hom\\Desktop\\MyGit\\platinhom\\platinhom.github.com\\_posts"
#pwd="."

def newblog(title="Template",category="Other",*args):
	title=str(title);
	category=str(category);
	tags="Other"
	if (len(args)>0):
			tags=" ".join(str(args).strip("(',)").split(", '"));
			tags=tags.replace("'","");
	
	# Change to work directory
	nowwd=os.getcwd()
	os.chdir(wd)

	# Jekyll use GM time in blog time, I use GM+8 time in title.
	gmnow=time.gmtime();
	gm8now=time.localtime(time.mktime(gmnow)+8*3600.0);

	gmstr=time.strftime("%Y-%m-%d %H:%M:%S",gmnow)
	gm8str=time.strftime("%Y-%m-%d",gm8now)

		# create the new blog
	f=open(gm8str+"-"+title+".md",'w');
	f.write("---\nlayout: post\ntitle: "+title+"\ndate: "+gmstr+"\ncategories: "+category+"\ntags: "+tags+"\n---\n\n---")
	f.close()

	os.chdir(nowwd)
	
if (__name__ == '__main__'):
	# Setup template information
	title="Template"
	category="Other"
	tags="Other"

	# Get the parameters
	argc=len(sys.argv)
	if (argc>1):
		title=sys.argv[1];
		if (argc>2):
			category=sys.argv[2];
			if (argc>3):
				tags=" ".join(sys.argv[3:])
	newblog(title,category,tags);
#end main