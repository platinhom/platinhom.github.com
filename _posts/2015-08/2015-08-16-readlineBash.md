---
layout: post
title: Bash中按行读取和处理
date: 2015-08-16 12:49:43
categories: Coding
tags: Bash
---

Bash的处理文档能力肯定是不如python友好了.但是要是能用Bash来处理, 那也是十分赞的. Bash还能配合awk, sed等一起操作, 用熟了应该不比python差.但是python的扩展库多,语言友好, bash就限定在那几个程序了...好吧, 那还是要学好的.

## for + cat 循环读取

使用cat 再for的缺点是, 要是有空格/tab, 就不会按行处理! 因为分隔符默认是空格,tab,换行! 这个问题再6-26号生日的博客中提及过了. 有两种写法去处理. 这里举例说明:

~~~bash
#! /bin/bash --login

# Backup the IFS
OLDIFS=$IFS
# Method 1:
IFS="
"
# Method 2:
IFS=$'\n'

echo > ambertype.log
for dir in `cat $1`
do
mol2pqr.sh ${dir}.mol2 pqrt no amber mbondi

for line in $(cat ${dir}.pqrt)
do
if [[ ${line:0:4} == "ATOM" || ${line:0:6} == "HETATM" ]];then
echo ${line:78:10} >> ambertype.log
fi
done

done

# Set back the IFS
IFS=$OLDIFS
~~~

这个脚本是操作文件内序号来读取文件,并提取行内信息的. 如果不设置IFS,读取结果是空白! 因为按空格和换行分隔了每个项...

## while read 循环读取

比较常用的方法, 但有缺陷: 由于IFS定界符的原因, 多个定界符会合为一个进行处理. 要是使用重定义定界符的方法可以避免. 可以使用重定向输入或管道的方法进行,重定向的效率和速度更快!

~~~bash
# testfile:
#1   2  3
#4 5  6

# -r取消反义, 按实际显示行来输入
# 将每行内容给line, 要是line1 line2 line3则根据定界符分隔每行赋给每个变量
while read -r line
do
    echo $line
done < $testfile
# 返回
#1 2 3
#4 5 6

IFS=$'\n'
# 或者用管道
cat $testfile | while read -r line
do
    echo $line
done
#返回
#1   2  3
#4 5  6
~~~

也可以使用文件句柄的方法指明输入:

~~~bash
#! /bin/bash
afile=$1
bfile=$2
# 将afile文件与bfile中的每行内容拼接起来. 
# 注意因为两个都要为真, 因此一个文件读完后循环将停止, 即使另一文件没读完.
while read -u3 i && read -u4 j;do
echo $i $j
done 3<$afile 4<$bfile
~~~

还有人这么做重定向..使用输入3接受标准输入,再使用文件内容重定向给标准输入(相当于保存了内容到输入3),然后再将输入3传给标准输入作为read的输入...(就不能直接0<$FILENAME写后面么..经测试,还真不行..)

~~~bash
#! /bin/bash
exec 3<&0
exec 0<$FILENAME
while read line
do
echo $line
done
exec 0<&3
~~~

## 使用自定义函数

这里使用特殊的大写字母作为变量传递.

~~~bash
function while_read_LINE_bottm(){
OLDIFS=$IFS
IFS=$'\n'
While read LINE
do
echo $LINE
done  < $FILENAME
IFS=$OLDIFS
}
~~~

------
