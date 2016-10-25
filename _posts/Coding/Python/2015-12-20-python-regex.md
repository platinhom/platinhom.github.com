---
layout: post
title: python正则表达式
date: 2015-12-20 02:02:53
categories: Coding
tags: Python
---

## 正则基础复习..

> [正则表达式(内链)](/2015/06/10/regexp-re/)

<iframe src="/2015/06/10/regexp-re/" width="100%" height="600px"></iframe>

## Python re模块

re模块是Python正则表达式模块, 能够对字符串进行模式匹配, 抓取内容, 十分常用. 主要有两个类: **RegexObject** 类(又俗称pattern对象)和 **Match** 类, 前者是对象化的正则表达式, 后者是匹配和匹配结果对象化.

使用示例:

- `pattern=re.compile(exp[,flags])` : 将正则表达式编译成Pattern对象, 返回Pattern对象
- `match=pattern.match(string)` : 利用正则表达式在string中进行匹配,返回Match对象. 无法匹配时返回None可以用 `if match:`去判断. match方法默认是从0开始进行匹配模式, 所以并一定匹配上.
- `match=pattern.search(string)` : search方法与match方法类似, 但"不限于"开头位置, 可以匹配到字符串中间的内容, 所以可以不限制后面的startpos和endpos. 返回也是match对象.
- `if (not match): print match.group()`: 将匹配部分结果打印出来.match匹配不上会返回None所以最好加个判断防出错. group()就是把匹配组打印出来. 如果pattern只有一个组就是这个组咯.

以上匹配/搜索还可以简单化为: `re.match/search(exp, string[,flags])` 返回match对象. 这种使用re函数方法适用于简单进行匹配, 不需要重复使用匹配pattern对像 (因为没有返回pattern对象). 

### 语法差异

- `(?P<name>)`:  分组自定义组名时多了个P, 这里name不用'name', 直接打就可以了
- `(?P=name)`:  引用自定义组名分组匹配到的字符串. (自动分组依然用`\num` )
- `(?(id/name)yespattern|nopattern)`: 如果组号为id或者name的组匹配到字符, 则后面需要匹配yespattern,否则就匹配nopattern. nopattern可以省略. 如`(\d)abc(?(1)\d|abc)`可以匹配1abc2或者abcabc
- `(?..)`或者`(?iLmsux)`: 每个字符代表一个匹配模式,只能用在正则表达式开头,可选多个. (参见re模块的compile的Pattern对象匹配模式部分).这种是非捕获性匹配. (除非`(?P=..)`)
- `\\\\和r"\\"`: 都是想表达查找`\\`,但是后者可用原生字符串r去解决. 建议多用r的表达去写正则表达字符串.

### re模块函数

这里的exp是指一个代表正则表达式的字符串, 而不是RegexObject对象. match/search/split/findall/finditer/sub/subn方法都在后面RegexObject对象中进行讨论和例子, 这里不展开.

- `re.compile(exp[,flags])` :  
将正则表达式编译成Pattern对象, 第二个参数是匹配模式(可用`|`分隔多个模式). 返回Pattern对象. Pattern对象可以通过相应方法实现很多正则表达式功能. 一般正则表达式需要重用时常使用pattern对象, 否则一般情况使用相应re方法即可.  
其中匹配模式:  `re.compile('exp',re.I |re.M)` 等效于`re.compile("(?im)exp")`. 匹配模式flags包括:
	- `re.I` (re.IGNORECASE): 忽略大小写差异.
	- `re.M` (re.MULTILINE): 多行模式, 改变`^`,`$`的匹配行为
	- `re.S` (re.DOTALL): 点任意匹配模式(包括换行), 改变`.` 的行为
	- `re.L` (re.LOCALE): 使预定字符类` \w \W \b \B \s \S `取决于当前区域设定
	- `re.U` (re.UNICODE): 使预定字符类` \w \W \b \B \s \S \d \D `取决于unicode定义的字符属性
	- `re.X` (re.VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
- `re.match(exp, string[,flags])` : 
使用exp进行从头匹配字符串string.
- `re.search(exp, string[,flags])` :  
使用exp进行搜素匹配字符串string.
- `re.split(exp, string[, maxsplit, flags])` :  
使用exp匹配的作为分隔符来分隔字符串. 如果exp含有分组, 会保留匹配的字符串到结果的列表.
- `re.findall(exp, string[, flags])` :  
使用exp去查证string, 返回所有匹配的子串或者分组情况. 
- `re.finditer(exp, string[, flags])` :  
返回一个可以查收Match对象的迭代器, 描述string中所有匹配exp的部分.
- `re.sub(exp, repl, string[, count])` :  
使用repl来代替string中exp匹配的部分. count是最大替换数. repl可以是字符串可以是函数.
- `re.nsub(exp, repl, string[, count])` :  
返回元组(替换后字符串,替换次数)
- `re.escape(string)` :  
会把字符串非数字字母的符号变成转义式, 再把转义式的`\`再转义. 例如`a b`会返回`a\\ b`. 尤其适于对匹配表达式的处理.
- `re.purge()` :  
清楚正则表达式缓存

### RegexObject对象
#### 属性:
1. `pattern`: 编译时的表达式字符串
2. `flags`: 匹配模式, 数字形式
3. `groups`: 表达式中分组数量
4. `groupindex`: 表达式中有别名的组的别名为键, 对应组的编号为值得字典. 无别名的组不包含在内.

#### 使用re函数的方法:
1. `match(string[, pos[, endpos]])`:  
这个方法将从string的pos下标处起尝试匹配pattern；如果pattern结束时仍可匹配，则返回一个Match对象；如果匹配过程中pattern无法匹配，或者匹配未结束就已到达endpos，则返回None。pos和endpos的默认值分别为0和len(string). match是位置锁定(给定位置从头开始匹配)的匹配.
2. `search(string[, pos[, endpos]])`:  
这个方法用于查找字符串中可以匹配成功的**第一个**子串。从string的pos下标处起尝试匹配pattern，如果pattern结束时仍可匹配，则返回一个Match对象；若无法匹配，则将pos加1后重新尝试匹配；直到pos=endpos时仍无法匹配则返回None。 search是位置不定搜索串的匹配. 
3. `split(string[, maxsplit])`:  
按照能够匹配的子串将string分割后返回列表(即匹配式作为分隔符)。maxsplit用于指定最大分割次数，不指定(默认0)将全部分割。  
如果pattern里面有分组, 返回的列表中将会包含这些匹配的部分.
4. `findall(string[, pos[, endpos]])`:   
搜索string，以列表形式返回全部能匹配的子串。 如果RegexObject对象对象含有分组, 返回的内容则是分组相关的列表. 所以可能有三种结果: 
	- 如果没有分组, 返回就是所有对pattern匹配的子串的列表.
	- 如果分组数只有一个, 则返回一个列表包括所有能匹配这个分组的部分.
	- 如果有多个分组, 则返回一个列表, 里面的元素是元组, 元组每个元素对应每个分组的匹配部分. 
5. `finditer(string[, pos[, endpos]])`:  
搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。 
6. `sub(repl, string[, count])`:  
使用repl替换string中每一个匹配的子串后返回替换后的字符串。 count可以限定最大替换次数(0为全部替换,默认). repl可以两种情况:
	- 当repl是一个字符串时，可以使用`\id`或`\g<id>`、`\g<name>`引用pattern里面的分组情况，但不能使用编号0。
	- 当repl是一个函数名时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。count用于指定最多替换次数，不指定时全部替换。
7. `subn(repl, string[, count])`:  
返回元组 (sub(repl, string[, count]), 替换次数), 即(替换后字符串, 替换次数)。

~~~python
## match and search
s="www.baidu.com"
p1=re.compile("www")
p2=re.compile("com") 
p1.match(s).group()
>> 'www'
p1.search(s).group()
>> 'www'
p2.match(s)
>> None
p2.search(s).group()
>> 'com'

## split
p=re.compile('\W+')
p.split('Words, words, words.')
>> ['Words', 'words', 'words', '']
p=re.compile('(\W+)')
p.split('Words, words, words.')
>> ['Words', ', ', 'words', ', ', 'words', '.', '']

## findall
p0=re.compile('go(?:to|ing)')
p0.findall("goto find going where found high")
>> ['goto', 'going']
p1=re.compile('go(to|ing)')
p1.findall("goto find going where found high")
>> ['to', 'ing']
p2=re.compile('go(to|ing).*?(f.*?\W)')
p2.findall("goto find going where found high")
>> [('to', 'find '), ('ing', 'found ')]

## sub
re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
       r'static PyObject*\npy_\1(void)\n{',
       'def myfunc():')
>> 'static PyObject*\npy_myfunc(void)\n{'

def dashrepl(matchobj):
	if matchobj.group(0) == '-': return ' '
	else: return '-'
re.sub('-{1,2}', dashrepl, 'pro----gram-files')
>> 'pro--gram files'
re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
>> 'Baked Beans & Spam'
~~~

### Match对象

#### 属性:

1. `string` :  匹配时使用的文本。
2. `re`: 匹配时使用的Pattern对象。
3. `pos`: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
4. `endpos`: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
5. `lastindex`: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
6. `lastgroup`: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。

#### 方法:

1. `group([group1, …])`:  
获得一个或多个分组截获的字符串；指定多个参数时将以**元组**形式返回。group1可以使用编号也可以使用别名；编号**0**代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
2. `groups([default])`:  
以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
3. `groupdict([default])`:  
返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
4. `start([group])`:  
返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
5. `end([group])`:  
返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
6. `span([group])`:  
返回(start(group), end(group))。
7. `expand(template)`:  
将匹配到的分组使用template进行替换然后返回替换后字符串, 详细参考`re.sub`方法。template中可以使用`\id`或`\g<id>`、`\g<name>`引用分组，但不能使用编号0。`\id`与`\g<id>`是等价的；但`\10`将被认为是第10个分组，如果你想表达`\1`之后是字符'0'，只能使用`\g<1>0`。


<iframe src="/ManualHom/Coding/Python/python-2.7.11rc1-docs-html/library/re.html" width="100%" height="600px"></iframe>


## Reference

1. [CNBlog: Python正则表达式指南](http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html  ); 
2. [W3CSchool: Python正则表达式](http://www.w3cschool.cc/python/python-reg-expressions.html);  
3. [Python专题教程：正则表达式re模块详解](http://www.crifan.com/files/doc/docbook/python_topic_re/release/html/python_topic_re.html)  
4. [【教程】详解Python正则表达式](http://www.crifan.com/detailed_explanation_about_python_regular_express/);

------
