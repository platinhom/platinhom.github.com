#! /bin/bash
# File: newblog.sh
# Author: PlatinHom
# Create: 2015-06-21, Last: 2015.10.1

# Full Usage: "./newblog.sh title category tag1 tag2"
# Simple Usage without category and tag: ".newblog/.sh title"

# You can register your sublime here. It's not nessary.
nowsys=`uname -s`
# For MacOS
if [ $nowsys == "Darwin" ];then
	alias subl="/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl"
# For MINGW in Window
elif [ ${nowsys:0:5} == "MINGW" ];then
	alias subl="/c/Program\ Files/Sublime\ Text\ 3/subl.exe"
fi
# Open sub-shell alias
shopt -s expand_aliases

# Set the directory to your blog directory
blogdir="."

# START
title=$1
category=$2
tag="${@:3}"

if [ -z $1 ];then
title="TempTitle-`date +%H%M%S`"
fi

if [ -z $2 ];then
category="Other"
fi

if [ -z $3 ];then
tag="Other"
fi

# My blog use GMT+8:00 time zone-China
# For MacOS
if [ `uname -s` == "Darwin" ];then
	today=`date -u -v "+8H" +"%Y-%m-%d"`
# Other OS
else
	today=`date -u -d "+8 hour" +"%Y-%m-%d"`
fi

# In github's jekyll,you should enter GMT time (time zone UTC(+0:00))
nowGMT=`date -u +"%Y-%m-%d %H:%M:%S"`
 
touch ${blogdir}/_posts/"${today}-${title}.md"
echo "---" >> ${blogdir}/_posts/"${today}-${title}.md"
echo "layout: post" >> ${blogdir}/_posts/"${today}-${title}.md"
echo "title: $title" >> ${blogdir}/_posts/"${today}-${title}.md"
echo "date: $nowGMT" >> ${blogdir}/_posts/"${today}-${title}.md"
echo "categories: $category" >> ${blogdir}/_posts/"${today}-${title}.md"
echo "tags: $tag" >> ${blogdir}/_posts/"${today}-${title}.md"
echo "---" >> ${blogdir}/_posts/"${today}-${title}.md"
echo "" >> ${blogdir}/_posts/"${today}-${title}.md"
echo "" >> ${blogdir}/_posts/"${today}-${title}.md"
echo "------" >> ${blogdir}/_posts/"${today}-${title}.md"

# Open the new blog by sublime.
# You can modify the program as you like.
if $(which sl);then
	sl ${blogdir}/_posts/"${today}-${title}.md" &
else
	subl ${blogdir}/_posts/"${today}-${title}.md" &
fi
