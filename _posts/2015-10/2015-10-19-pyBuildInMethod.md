---
layout: post_small
title: Python:内建函数与对象方法
date: 2015-10-18 21:56:04
categories: Coding
tags: Python
archive: true
---

包括内建函数, 内建对象(字符串,列表,字典,set,文件对象)的方法

内建的东东放在`__buildin__`模块当中.

## 内建函数，作为一种预设运算，用于返回值，特殊表达式
- float(object): 转换为浮点数
- int(object,base=10): 转换为整数，带小数时向下取整运算. 字符串时指定base可指定传入字符的进制,默认10.
- long(object): 转换为长整形数
- str(object): 转换为字符串(1000L->1000)
- repr(object): 返回值为适合机读的字符串形式(1000L->1000L)
- ord(‘char’): 将某单字符转成字母顺序值（单字符包括\n等）
- chr(num): 将字母顺序值转为某单字符（0~255）
- unichr(num): 将字母顺序值转为某unicode单字符（0~65535）
- unicode(var,codec): 将变量按codec转为unicode型(前面加了个u)=str.decode(codec)
- abs(number): 返回绝对值
- cmath.sqrt(number): 可带虚数均方根
- math.ceil(number): 返回数的上入整数，返回值为浮点数
- math.floor(number): 返回数的下舍整数，返回值为浮点数
- math.sqrt(number): 计算平方根，需为实数，返回浮点数
- pow(x, y[, z]): 返回x的y次幂，（所得结果对z取模），类型数相关
- round(number[, ndigits]): 根据给定精度进行四舍五入,返回float
- complex(real, img): 创建出复数，返回复数。
- input(prompt): 获取用户输入，须合法的python表达式：”字符”
- raw_input(prompt): 获取用户输入，返回字符串
- help([object]): 交互式帮助
- id(obj): 返回对象的id
- cmp(x, y): 比较xy的值大小，相同0前大1后大-1。
- len(seq): 返回序列的长度（元素个数）,或者字典的项数int。
- list(seq): 序列（字符串）转换为列表。
- tuple(seq): 把序列转为元组（包括列表、元组、字符串均可）
- bool(‘any’): 将任意转成布尔型，除了False的特殊值，其余均真。一般不需显式说明
- max(args): 返回序列或参数集合中最大值,多于一个序列时，比较第一个，迭代。
- min(args): 返回序列或参数集合中最小值,多于一个序列时，比较第一个，迭代。
- sum(sqe[,start]): 求序列之和。start参数为起始值，用于复合使用。
- reversed(seq): 序列反向迭代
- sorted(seq): 返回A已排序的列表，不改变A的顺序。
- string.Template(’a’): 模板字符串，结合$x和A.substitute(x=’a’)使用
- string.capwords(‘str’): 词首字母大写，较好，返回字符串
- string.maketrans(‘ab’,’cd’): 将256位字符表中a和b相应换成c和d，返回字符串.用于translate方法。
- range([x,]y[,z]): 产生整形列表,x起y终z步长,默认x=0,z=1.常用在for语句中.切记y终点在列表外
- xrange([x,]y[,z]): 类似于range但是更简洁,用于迭代用
- zip(seqA,SeqB….): 多个序列(包括元组字符串)的项组成一个元组并返回列表,最短序列决定列表长(舍去).
- filter(func,list): 对list元素都执行func,如返回True则保留,否则被过滤掉.
- map(func,list): 对list元素都执行func,并返回对应的list
- reduce(func,seq[,init]): init默认第一项,把该项和后一项传递给func,返回的结果再和下一项扔给func,直到结束
- enumerate(iter): 对可迭代对象所有项迭代索引,项目对。如用于编号迭代。返回迭代对象
- eval(exp[,global[,local]]): 会计算表达式exp的值,并返回结果.eval(raw_input(…))等于input(..).可用两个命名空间。
- set(seq): 返回([...])的集合,无重复元素的.seq可为字符串,元组,列表.
- type(var): 返回变量类型,type('a')==str 返回True
- vars(): 返回当前局部变量
- callable(obj): 检查对象是否可调用,可调用返回True
- help(module[.func]): 查看模组帮助,
- lambda x: 含x表达: 就是对x进行表达式中的运作,返回函数对象lambda.用法a=lambda x:x*2+3 执行a(5). 
- dir([obj]): 列出obj的所含标识符(函数,类,变量,模块),不加参数针对当前模块
- isinstance(var, type): 可以比较两个参数项类型是否相同.如isinstance("abcd",str).type部分还可以用元组的形式指定多种类型.isinstance和type比较差异参看[ref](http://segmentfault.com/q/1010000000127305),主要是isinstance可以对继承的类也进行相等判断,type不行.

## 复数

- C.real: 实数部分
- C.imag: 虚数部分

## 列表方法

- A.append（对象）: 列表末追加新对象（一次一个，对象可为列表）
- A.count(obj): 统计列表某元素出现次数
- A.extend(B): 在列表A后追加另一序列B的值,B可以是任意iterable对象
- A.index(obj[,start,stop]): 索引,返回第一个匹配obj的元素在列表中索引号n（第n+1个）.start和stop可以限制搜索区间.找不到会报ValueError.
- A.insert(index,obj): 插入，在索引号处插入对象。
- A.pop(index): 移除索引号的元素,返回该元素的值。()时移除最后一个,出栈.唯一修改列表还能返回值。
- A.sort(): 排序，默认按升序。可添加参数cmp、key、reverse。cmp可以自定义的函数,返回负数时, 按此时顺序排序，详见脚本例子
- A.remove(obj): 移除列表内某个指定元素，不返回任何值。找不到会报ValueError.
- A.reverse(): 反向列表A，不返回值。

## 元组方法

- T.count(obj): 统计元组某元素出现次数
- T.index(obj[,start,stop]): 索引,返回第一个匹配obj的元素在元组中索引号n（第n+1个）.start和stop可以限制搜索区间.找不到会报ValueError.

## 字典方法
- dict.clear(): 清空字典所有的项，无返回值None。
- dict.copy(): 浅复制副本，用于赋值,深复制用copy.deepcopy
- dict.fromkeys(seq[,val]): 从seq内读入键，建立并返回一个新的字典，值通为val或者None（默认）
- dict.get(key[,noneval]): 读取并返回字典某key的值,若不存在该键返回None或指定值,好处在于不存在不报错。
- dict.setdefault(key[,val]): 和get类似，读取并返回键值。差别在于，若不存在，则新建该键及键值。
- dict.update(dictB): 用dictB的项更新dict，相当于复制。若有相同键则覆盖。
- dict.has_key('key'): 检查是否字典中含有该键值，和in用法一样，返回真假。
- dict.items(): 将字典所有项以列表方式返回,每个项以元组方式,但返回时没有特殊顺序
- dict.iteritems(): 和items功能一样，但是返回迭代器对象,可用list()将函数读出
- dict.keys(): 返回字典中的键的列表
- dict.iterkeys(): 返回字典中的键的列表的迭代器对象
- dict.values(): 返回字典中值的列表
- dict.itervalues(): 返回字典中值的列表的迭代器对象
- dict.pop(key): 读出某键的值,并从字典中删除该项，栈操作。
- dict.popitem(): 随机读出字典中一个项以元组返回,并从字典中删除。

## 集合方法
- set.add(element)    集合添加一个元素
- set.update(seq)    集合添加多项
- set.remove(element)    移除集合一个元素
- t\|s 并集 t&s 交集 t-s 差集 t^s交集的补集(只出现t或s中，不能都有)

## 字符串方法（大部分并不能改变字符串的值，只起到返回作用）

- str.decode(codec): 根据codec将字符串解码成unicode,等于unicode函数
- str.encode(codec): 根据codec将unicode字符串编码为codec的内容
- str.find(a,x,y): str中查找字符串a,xy为查找始末(不含y)不输入xy默认头到尾.返回索引号,没有返回-1
- str.rfind(a,x,y): str中查找最后一个字符串a,xy为始末,返回最后一个的索引号，没有返回-1
- str.index(a,x,y): 和find功能基本一致，区别在查找不到返回错误
- str.rindex(a,x,y): 和rfind功能基本一致，区别在查找不到返回错误
- str.count(a,x,y): str中查找a,xy始末,返回a出现次数
- str.startwith(a,x,y): str中检查xy范围内是否以字符串a起始，返回TrueFalse
- str.endwith(a,x,y): str中检查xy范围内是否以字符串a终结，返回TrueFalse
- str.join(Seq): 序列Seq各字符元素用str连接起来.要在始末加连接符要加空元素’’.返回连接的字符串
- str.lower(): str小写化，返回小写字符串
- str.islower(): 检查str是否小写，返回真假
- str.capitalize(): str句首首字母大写，返回字符串
- str.swapcase(): str字母交换大小写，返回字符串
- str.title(): str词首大写，包括's，the等。返回字符串
- str.istitle(): 检查str是否词首大写，返回真假
- str.upper(): str大写化，返回大写字符串
- str.isupper(): 检查str是否大写，返回真假
- str.replace(a,b,[x]): 替换,将a变成b。x为参数限定最大替换数，不输为全替换。返回字符
- str.expandtabs([x]): 将Tab产生的长度替换为x个空格，不指明x为默认tab长度。返回字符串
- str.split([spe[,x]]): 将分隔符spe(不输入默认空格换行制表符等)从字符串中去除,x为最大去除数。返回列表
- str.splitlines([keepends]): 将多行分裂开成列表，可选保留换行符不。
- str.strip('a'): 将str两端的符合条件'a'的都删除,返回字符串.不输默认空格tab换行,或者某些单字符
- str.lstrip('a'): 同strip，不过只删左边end部分
- str.rstrip('a'): 同strip，不过只删右边开头部分
- str.translate(table[,'char']): 按字母表（用maketrans函数产生）单字符地替换str，删掉'char'，返回字符串
- str.zfill(x): 填充字符串使其变成长度x的字符串，不足从左填入0
- str.center(x[,'a']): 变成长度x字符串,str归中处理(若基数右侧多1).指明a的话即用a填充,否则空格
- str.ljust(x[,'a']): 变成长度x字符串,str左对齐处理.指明a的话即用a填充,否则空格
- str.rjust(x[,'a']): 变成长度x字符串,str右对齐处理.指明a的话即用a填充,否则空格
- str.isalnum(): 检查str是否数字或字母，返回是否。
- str.isalpha(): 检查str是否字母，返回是否。
- str.isdigit(): 检查str是否数字，返回是否。
- str.isspace(): 检查str是否空格，返回是否。
- str.partition('sep'): 从左搜索str的分隔符sep，并返回(head,sep,tail)即分隔开后的元组
- str.rpartition('sep'): 从右搜索str的分隔符sep，并返回(head,sep,tail)即分隔开后的元组
 


## 文件方法和属性  help(file)
- open('filepath','mode'[,bufsize])    同file,但可以打开文件对象。'r''w''a''b''+'分别为读,写,追加,二进制方法,和读/写,后两种可以和前面合用。
- file('filepath','mode'[,bufsize])    建立文件对象,bufsize为缓存区大小,一般不设.mode默认'r'读。'U'模式支持各种换行符.
- f.read([size])                读取文件,记得有定位的,读完就改变定位.size指明为读取字节数,不指明全部读取.返回字符串
- f.readline([size])            读取一行,读完改变定位,size指明为读取字节数(非行数),不指名读取一行(常用)。返回字符串.读行是从当前位至\n为止。
- f.readlines([size])            不设置size读取所有行,以每行为序列的一个元素返回全文的序列。
- f.write(str)                把字符串(必须是字符串)写入到文件中.注意,和定位符有关.不会帮你换行,手动加入制表符.若对已存在文件操作则覆盖
- f.writelines(seq)            把序列的各个str串连起来全部写入到文件中。
- f.close()                    关闭文件，否则驻留内存。常用try..finally的后者来保证关闭。
- \#readfile('filepath')    读取文件内容并返回内容，参数为路径。
- \#addfile('filepath','str')    追加str到p文件的末尾，返回None。
- f.name        返回file的filepath+name
- f.closed        返回file是否关闭真假
- f.mode        返回file读取模式
- f.encoding        ？
- f.newlines        ？
- f.softspace        ？
- f.tell()        返回文件操作标记符所在处，换行符\n占两位其余一位，从0开始。但\n用read来读代表1byte。
- f.next()        和readline()类似，从当前处读到行末并返回，跳至下一行开头。注意，实际文件操作符其实已到文件末,tell()显示文件末尾,没法用read()类再读取。
- f.seek(offset[,whence])    文件操作符移动到offset步数的位置,正值正移负值负移,移动的起点whence为0时为文件头1为当前操作符位置2为文件末。不输入默认为从文件头开始。注意a模式下每次都会自动返回到文件末。
- f.truncate([size])        裁剪，不可用于只读。输入大小，就是文件保留的大小。不标大小表示裁到文件操作符，若大于文件大小则补空格(win)
- f.isatty()        返回文件是否是一个终端设备文件（unix）
- f.fileno()        返回长整形的‘文件标签’
- f.flush()        把缓冲区内容写入硬盘
- for line in file1： 用迭代器逐行读取，注意此时不能再用readline()之类读取，不怎么占内存的方式

> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#buildin-list)中, 不再更新.

------
