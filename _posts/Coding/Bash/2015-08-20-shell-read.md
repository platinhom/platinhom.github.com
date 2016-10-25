---
layout: post
title: shell的read命令
date: 2015-08-19 23:39:57
categories: Coding
tags: Bash
---

read命令接收标准输入（键盘）的输入，或其他文件描述符的输入(使用句柄)。  

得到输入后，read命令将数据放入一个或多个标准变量(甚至数组)或传给REPLY变量。  
多变量时,根据分界符空格/tab来划分,若变量数少于输入中提供的数量,则不考虑分界符将后面的通通扔给最后的变量(参见行分界符的第5例子).

基本shell都支持. 选项不少, 不同系统会有差异. 比较重要的是-t 等待时间, -p 提示语句, -s 不回显, -d 行定界符.

可以接受管道和重定向输入(例6).  

## read 选项介绍,英文源自HPCC的man.

`read [-ers] [-a aname] [-d delim] [-i text] [-n nchars] [-N nchars] [-p prompt] [-t timeout] [-u fd] [name ...]`

One  line  is  read  from  the  standard  input, or from the file descriptor fd supplied as an argument to the -u option, and the first word is assigned to the first name, the second word to the second name,  and  so  on,  with leftover  words  and  their intervening separators assigned to the last name.  If there are fewer words read from the input stream than names, the remaining names are assigned empty values.  The characters in IFS  are  used  to split  the  line  into words.  The backslash character (\) may be used to remove any special meaning for the next character read and for line continuation.  Options, if supplied, have the following meanings:

- -a  **数组变量** aname
    The words are assigned to sequential indices of the array variable *aname*, starting at 0. *aname* is unset before any new values are assigned. Other name arguments are ignored.  
    将内容读入到数组变量中. 如`read -a array; echo ${#array[@]}`
- -d  **行定界符** delim
    The first character of delim is used to terminate the input line, rather than newline.  
    指定**行定界符**,一般是换行符.注意, 多变量赋值分界符依然是空格tab,但`-dq`可以使用q作为结束而不是按下确定.
- -e    Interactive. 
    If the standard input is coming from a terminal, readline (see READLINE above) is used to obtain the line. Readline uses the current (or default, if line editing was not previously active) editing settings.  
    只用于互相交互的脚本，它将readline用于收集输入行。
- -i   text  
     If readline is being used to read the line, text is placed into the editing buffer before editing begins.  
     Mingw就不支持.
- -n  **读取指定字符个数** nchars  
    read returns after reading nchars characters rather than waiting for a complete line of input, but honor a delimiter if fewer than nchars characters are read before the delimiter.  
    用于限定最多可以有多少字符(包括空格等!)可以作为有效读入。例如echo –n 5 value1 value2，如果我们试图输入12  34，则只有前面有效的12 3，作为输入，实际上在你输入第5个字符3后，就自动结束输入。
- -N   nchars  
    read returns after reading exactly nchars characters rather than waiting for a complete line of input, unless EOF is  encountered or read times out. Delimiter characters encountered in the input are not treated specially and do not cause read to return until nchars characters are read.
    真实地读取指定字符个数. Mingw就不支持.
- -p  **提示语句** prompt  
    Display prompt on standard error, without a trailing newline, before attempting to read any input. The prompt is displayed only if input is coming from a terminal.  
    指定提示语句，如 `read –p "… my promt?" value`. 提示语句会在同一行中.
- -r  **取消反义符作用**  Backslash does not act as an escape character.    
	The backslash is considered to be part of the line. In particular, a backslash-newline pair may not be used as a line continuation.  
	取消反义号作用, 影响本来取消换行的效果. 在参数输入中，我们可以使用`\`表示没有输入完，换行继续输入，如果我们需要行最后的`\`作为有效的字符，可以通过-r来进行。此外在输入字符中，我们希望`\n`这类特殊字符生效，也应采用-r选项。
- -s  **不回显** Silent mode.      
	If input is coming from a terminal, characters are not echoed.
	不显示输入内容. 参见第二个例子.
- -t  **等待时间** timeout    
    Cause read to time out and return failure if a complete line of input is not read within timeout seconds. timeout may be  a decimal number with a fractional portion following the decimal point. This option is only effective if read is reading input from a terminal, pipe, or other special file; it has no effect when reading from regular files. If timeout is 0, read returns success if input is available on the specified file descriptor, failure otherwise. The exit status is greater than 128 if the timeout is exceeded.   
    用于表示等待输入的时间，单位为秒，等待时间超过，将继续执行后面的脚本，注意不作为null输入，参数将保留原有的值. 此时read命令返回非零退出. 十分重要的**防止脚本停止**的选项!
- -u fd  **文件句柄** Read input from file descriptor fd.  
	从指定文件句柄中读取. 参见第一个例子.
- If no names are supplied, the line read is assigned to the variable REPLY. The return code is zero, unless end-of-file is encountered, read times out (in which case the return code is greater than 128), or an invalid file descriptor is supplied as the argument to -u.  
在read命令行中也可以不指定变量.如果不指定变量，那么read命令会将接收到的数据放置在环境变量REPLY中。

## Read的相关实例

- 1\. 拼接文件

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

- 2\. 输入不在终端显示

~~~bash
read -p "Input passwd: " -s Passwd
echo Password is $Passwd. 
~~~

- 3\. 延迟五秒，没有输入将自动退出返回错误退出值.

~~~bash
#!/bin/bash 
if read -t 5 -p "please enter your name:" name 
then 
    echo "hello $name ,welcome to my script" 
else 
    echo "sorry,too slow"
    exit 1 
fi 
~~~

- 4\. 读取限定字符

~~~bash
#!/bin/bash 
read -n1 -p "Do you want to continue [Y/N]?" answer
case $answer in 
Y | y) 
      echo "fine ,continue";; 
N | n) 
      echo "ok,good bye";; 
*) 
     echo "error choice";; 
esac 

read -p "Input a word:" -n 5 Word1 Word2
echo $Word1 $Word2
~~~

- 5\. 指定行分界符

~~~bash
#输入，直到输入q，将自动退出
read -dq -p "Input some words end with q:" word ok
echo word: $word ok: $ok
#输入 10 9 8 7 abcq
#结果: word: 10 ok: 9 8 7 abc
~~~

- 6\. 重定向或管道

~~~bash
# -r取消反义, 按实际显示行来输入
while read -r line
do
    echo $line
done < $testfile
# 以管道作为输入
cat $testfile | while read -r line
do
    echo $line
done
~~~

------
