#! /bin/bash
# file: newblog.sh
# Author: PlatinHom
# Last: 2015-06-21

# Full Usage: "./newblog.sh title category tag1 tag2"
# Simple Usage without category and tag: ".newblog/.sh title"

# You can register your sublime here. It's not nessary.
sublimecmd="/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl"

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
 
touch _posts/"${today}-${title}.md"
echo "---" >>_posts/"${today}-${title}.md"
echo "layout: post" >>_posts/"${today}-${title}.md"
echo "title: $title" >>_posts/"${today}-${title}.md"
echo "date: $nowGMT" >>_posts/"${today}-${title}.md"
echo "categories: $category" >>_posts/"${today}-${title}.md"
echo "tags: $tag" >>_posts/"${today}-${title}.md"
echo "---" >>_posts/"${today}-${title}.md"
echo "" >>_posts/"${today}-${title}.md"
echo "" >>_posts/"${today}-${title}.md"
echo "---" >>_posts/"${today}-${title}.md"

# Open the new blog by sublime.
# You can modify the program as you like.
if $(which sl);then
	sl _posts/"${today}-${title}.md" &
elif [ -x "$sublimecmd" ];then
	"$sublimecmd" _posts/"${today}-${title}.md" &
fi
