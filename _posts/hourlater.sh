#! /bin/bash
# file: hourlater.sh
# Author: PlatinHom
# Last: 2015-06-21

# It's use for generating new blog some hours later.
# Full Usage: "./hourlater.sh hour title category tag1 tag2"
# Simple Usage without category and tag: ".hourlater/.sh 0 title"

# You can register your sublime here. It's not nessary.
sublimecmd="/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl"

hourchange=$1
title=$2
category=$3
tag="${@:4}"

if [ -z $2 ];then
title="TempTitle-`date +%H%M%S`"
fi

if [ -z $3 ];then
category="Other"
fi

if [ -z $4 ];then
tag="Other"
fi
#GMT+8 after some hour
hour1=`expr 8 + $1`

# My blog use GMT+8:00 time zone-China
# For MacOS
if [ `uname -s` == "Darwin" ];then
	today=`date -u -v "+${hour1}H" +"%Y-%m-%d"`
	# In github's jekyll,you should enter GMT time (time zone UTC(+0:00))
	nowGMT=`date -u -v "+${1}H" +"%Y-%m-%d %H:%M:%S"`
# Other OS
else
	today=`date -u -d "+${hour1} hour" +"%Y-%m-%d"`
	nowGMT=`date -u -d "+${1} hour" +"%Y-%m-%d %H:%M:%S"`
fi


 
touch ./"${today}-${title}.md"
echo "---" >>./"${today}-${title}.md"
echo "layout: post" >>./"${today}-${title}.md"
echo "title: $title" >>./"${today}-${title}.md"
echo "date: $nowGMT" >>./"${today}-${title}.md"
echo "categories: $category" >>./"${today}-${title}.md"
echo "tags: $tag" >>./"${today}-${title}.md"
echo "---" >>./"${today}-${title}.md"
echo "" >>./"${today}-${title}.md"
echo "" >>./"${today}-${title}.md"
echo "------" >>./"${today}-${title}.md"

# Open the new blog by sublime.
# You can modify the program as you like.
if $(which sl);then
	sl ./"${today}-${title}.md" &
elif [ -x "$sublimecmd" ];then
	"$sublimecmd" ./"${today}-${title}.md" &
fi
