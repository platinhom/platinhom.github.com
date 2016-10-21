---
layout: post
title: Shell中date命令用法
date: 2015-06-07 10:32:12
categories: Coding
tags: Shell Bash Git
---

由于想自动化创建markdown模板用于写blog, 需要调用date命令来完成, 在此复习一下吧.

## date 选项 参数
获取当前或指定时候的时间; 或者设置时间(需要root权限). 请注意Mac中date的选项有极大差异,但依旧支持当今时间格式化直接输出.

## 选项

~~~~
不加: 显示当前的时间.
-d <字符串>：显示字符串所指的日期与时间。字符串前后必须加上双引号； 
-s <字符串>：根据字符串来设置日期与时间。字符串前后必须加上双引号； 
-u：显示GMT； 
--help：在线帮助； 
--version：显示版本信息。
~~~~
在MacOS中,时间差需要用`-v 8H`这样不同于一般Linux,时间指定为`y, m, w, d, H, M, S`.参见-d下面的讨论.

## 参数 <+时间日期格式>：指定显示时使用的日期时间格式。
就是格式化字符串处理.当需要用到空格时要使用双引号,如`"+%Y-%m-%d %H:%M:%S"`.

### 日期格式字符串列表
~~~~
%H 小时，24小时制（00~23） 
%I 小时，12小时制（01~12） 
%k 小时，24小时制（0~23） 
%l 小时，12小时制（1~12） 
%M 分钟（00~59） 
%p 显示出AM或PM 
%r 显示时间，12小时制（hh:mm:ss %p） 
%s 从1970年1月1日00:00:00到目前经历的秒数 
%S 显示秒（00~59） 
%T 显示时间，24小时制（hh:mm:ss） 
%X 显示时间的格式（%H:%M:%S） 
%Z 显示时区，日期域（CST） 
%a 星期的简称（Sun~Sat） 
%A 星期的全称（Sunday~Saturday） 
%h,%b 月的简称（Jan~Dec） 
%B 月的全称（January~December） 
%c 日期和时间（Tue Nov 20 14:12:58 2012）(不加参数时的效果) 
%d 一个月的第几天（01~31） 
%x,%D 日期（mm/dd/yy） 
%j 一年的第几天（001~366） 
%m 月份（01~12） 
%w 一个星期的第几天（0代表星期天） 
%W 一年的第几个星期（00~53，星期一为第一天） 
%y 年的最后两个数字（1999则是99）
~~~~

- 一般,`%Y %m %d %H %M %S` 是最基本的. 使用星期月份时也会用到`%a %b`
- `%s`十分重要,得出了从1970.1.1起的秒数,可用于时间相减,计算耗时.

#### 显示时间
- 使用当前时间,可以忽略选项,指明格式化参数.如`date +"%Y-%m-%d"`
- 使用其余时间,需要`-d`参数,后面需要再跟字符串表达时间偏移值.
- 时间偏移值支持`+-`法则,支持`second minute hour day week month year`甚至支持`1 day ago`.
- 注意: Mac系统date的`-d`和一般的不一样,设置时区等相关.用法更复杂,请`man date`查看.

### 例子

~~~~ bash
# 格式化输出： 
date +"%Y-%m-%d" ###2009-12-07 
# 输出昨天日期： 
date -d "1 day ago" +"%Y-%m-%d" ###2012-11-19 
# 2秒后输出： 
date -d "2 second" +"%Y-%m-%d %H:%M.%S" ###2012-11-20 14:21.31 
# 传说中的 1234567890 秒： 
date -d "1970-01-01 1234567890 seconds" +"%Y-%m-%d %H:%m:%S" ###2009-02-13 23:02:30 
# 普通转格式： 
date -d "2009-12-12" +"%Y/%m/%d %H:%M.%S" ###2009/12/12 00:00.00 
# apache格式转换： 
date -d "Dec 5, 2009 12:00:37 AM" +"%Y-%m-%d %H:%M.%S" ###2009-12-05 00:00.37 
# 格式转换后时间游走： 
date -d "Dec 5, 2009 12:00:37 AM 2 year ago" +"%Y-%m-%d %H:%M.%S" ###2007-12-05 00:00.37
~~~~

#### 设定时间
使用`-s`选项. 时间必须是AA:BB:CC格式. 日期可以两种八数字格式. 可以只更改时间或只更改日期,也可以一起更改,例如:
`date -s "01:01:01 2012-05-23"`
`date -s "01:01:01 20120523"`

## 自动创建带有时间的Github Pages的markdown模板的脚本
~~~~ bash
#! /bin/bash
# Author: PlatinHom
# Last: 2015-06-07

# Full Usage: ./a.sh  title category tag
# Simple Usage without category and tag: ./a.sh  title

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

#My blog use GMT+8:00 time zone-China
# For MacOS
if [ `uname -s` == "Darwin" ];then
	    today=`date -u -v "+8H" +"%Y-%m-%d"`
# Other OS
else
		today=`date -u -d "+8 hour" +"%Y-%m-%d"`
fi
#In github's jekyll,you should enter GMT time (time zone UTC(+0:00))
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
~~~~

---
