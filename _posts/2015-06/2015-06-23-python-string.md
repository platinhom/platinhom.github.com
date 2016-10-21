---
layout: post
title: Python字符串相关
date: 2015-06-23 06:20:48
categories: Coding
tags: Python
archive: true
---

Python是十分方便的小型脚本语言, 优点是易用. 内建的字符串对象的自带方法很丰富. 这里总结一下字符串相关的函数,库和方法.

~~~python
# 一般字符串
big="abcd "
# 分行输入
big="this is a long string\  
that spans two lines."  
# 分行输入并换行
big="this is a long string\n\  
that spans two lines."
# 字符串段三引号法
big="""abcd
efg
"""
# 禁转义
big=r"this is a long string\n\  
that spans two lines."  

# 字符串拼接
a="123"+"456"
# 格式化字符串
"%3.3f"%("1.234")

~~~

## 内建函数

- `type(var)` 求出变量类型,例如`str`
- `len(str)` 求出字符串长度
- `int(str)` 字符串变整型
- `float(str)` 字符串变浮点
- `long(str)` 字符串变长整型
- `str(var)` 将变量转为字符串. 
- `list(str)` 将字符串逐个逐个字符变为list型..类似地`tuple(str)`也行..
- `repr(object)`                                  返回值为适合机读的字符串形式(1000L->1000L)
- `chr(N)` 将整型变为字符.
- `unichr(num)`                   将字母顺序值转为某unicode单字符（0~65535）
- `unicode(var,codec)`                         将变量按codec转为unicode型(前面加了个u)=str.decode(codec)
- `input(prompt)`                              获取用户输入，须合法的python表达式：”字符”
- `raw_input(prompt)`                    获取用户输入，返回字符串


## 字符串方法（并不能改变字符串的值，只起到返回作用）
- `str.decode(codec)`                        根据codec将字符串解码成unicode,等于unicode函数
- `str.encode(codec)`                        根据codec将unicode字符串编码为codec的内容
- `str.find(a,x,y)`                               str中查找字符串a,xy为查找始末(不含y)不输入xy默认头到尾.返回索引号,没有返回-1
- `str.rfind(a,x,y)`                             str中查找最后一个字符串a,xy为始末,返回最后一个的索引号，没有返回-1
- `str.index(a,x,y)`                                     和find功能基本一致，区别在查找不到返回错误
- `str.rindex(a,x,y)`                          和rfind功能基本一致，区别在查找不到返回错误
- `str.count(a,x,y)`                           str中查找a,xy始末,返回a出现次数
- `str.startwith(a,x,y)`                    str中检查xy范围内是否以字符串a起始，返回TrueFalse
- `str.endwith(a,x,y)`                       str中检查xy范围内是否以字符串a终结，返回TrueFalse
- `str.join(Seq)`                                  序列Seq各字符元素用str连接起来.要在始末加连接符要加空元素’’.返回连接的字符串
- `str.lower()`                                    str小写化，返回小写字符串
- `str.islower()`                                 检查str是否小写，返回真假
- `str.capitalize()`                             str句首首字母大写，返回字符串
- `str.swapcase()`                                      str字母交换大小写，返回字符串
- `str.title()`                                       str词首大写，包括’s，the等。返回字符串
- `str.istitle()`                                    检查str是否词首大写，返回真假
- `str.upper()`                                    str大写化，返回大写字符串
- `str.isupper()`                                 检查str是否大写，返回真假
- `str.replace(a,b,[x])`                     替换,将a变成b。x为参数限定最大替换数，不输为全替换。返回字符
- `str.expandtabs([x])`                    将Tab产生的长度替换为x个空格，不指明x为默认tab长度。返回字符串
- `str.split([spe[,x]])`                        将分隔符spe(不输入默认空格换行制表符等)从字符串中去除,x为最大去除数。返回列表
- `str.splitlines([keepends])`                   将多行分裂开成列表，可选保留换行符不。
- `str.strip(‘a’)`                                 将str两端的符合条件’a’的都删除,返回字符串.不输默认空格tab换行,或者某些单字符
- `str.lstrip(‘a’)`                                同strip，不过只删左边end部分
- `str.rstrip(‘a’)`                                同strip，不过只删右边开头部分
- `str.translate(table[,’char’])`     按字母表（用maketrans函数产生）单字符地替换str，删掉’char’，返回字符串
- `str.zfill(x)`                                       填充字符串使其变成长度x的字符串，不足从左填入0
- `str.center(x[,’a’])`                        变成长度x字符串,str归中处理(若基数右侧多1).指明a的话即用a填充,否则空格
- `str.ljust(x[,’a’])`                             变成长度x字符串,str左对齐处理.指明a的话即用a填充,否则空格
- `str.rjust(x[,’a’])`                                     变成长度x字符串,str右对齐处理.指明a的话即用a填充,否则空格
- `str.isalnum()`                                检查str是否数字或字母，返回是否。
- `str.isalpha()`                                  检查str是否字母，返回是否。
- `str.isdigit()`                                    检查str是否数字，返回是否。
- `str.isspace()`                                 检查str是否空格，返回是否。
- `str.partition(‘sep’)`                     从左搜索str的分隔符sep，并返回(head,sep,tail)即分隔开后的元组
- `str.rpartition(‘sep’)`                    从右搜索str的分隔符sep，并返回(head,sep,tail)即分隔开后的元组

## string标准库
现在已经很少用. 内置一些奇怪的常量, 还有一些str类不具有的方法.

### 常量:

- `whitespace` : a string containing all characters considered whitespace
- `lowercase` : a string containing all characters considered lowercase letters
- `uppercase` : a string containing all characters considered uppercase letters
- `letters` : a string containing all characters considered letters
- `digits` : a string containing all characters considered decimal digits
- `hexdigits` : a string containing all characters considered hexadecimal digits
- `octdigits` : a string containing all characters considered octal digits
- `punctuation` : a string containing all characters considered punctuation
- `printable` : a string containing all characters considered printable

### DATA:

- `ascii_letters` = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
- `ascii_lowercase` = 'abcdefghijklmnopqrstuvwxyz'
- `ascii_uppercase` = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
- `digits` = '0123456789'
- `hexdigits` = '0123456789abcdefABCDEF'
- `letters` = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
- `lowercase` = 'abcdefghijklmnopqrstuvwxyz'
- `octdigits` = '01234567'
- `printable` = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
- `punctuation` = `` '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' ``
- `uppercase` = `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`
- `whitespace` = `'\t\n\x0b\x0c\r '`

### 方法

- `string.Template(’a’)`       模板字符串，结合$x和A.substitute(x=’a’)使用
- `string.atoi(str[,base])` 字符串到整型,base默认10进制,可以输入8/16/2等
- `string.atol(str[,base])` 字符串到长整型,base默认10进制,可以输入8/16/2等
- `string.atof(str)`	字符串到浮点
- `string.capwords(str[,sep])`  利用sep作分隔的词首字母大写，较好，返回字符串.默认为空格分隔.
- `string.maketrans(‘ab’,’cd’)`      将256位字符表中a和b相应换成c和d，返回字符串.用于translate方法。
- `string.capitalize(string)`    首字母大写
- `string.lower(string)`    全部小写化
- `string.upper(string)`    全部大写化
- `string.replace(string,old,new[,maxsplit])`     字符串中替换,max为最多替换个数
- `string.join(list[,sep])`  使用分界符(sep,默认空格)将字符串列表连接起来.
- `string.split(string,sep=None,maxsplit=-1)` 以sep为分界符将string分开成一个列表

> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#mid-string-relative)中, 不再更新.


---
