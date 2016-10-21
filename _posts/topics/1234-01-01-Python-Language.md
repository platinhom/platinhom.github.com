---
layout: post_toc
title: Python语法汇总
date: 1234-01-01 00:19:34
categories: Coding
tags: Python
---

汇总贴, 不停更新合并................

{::comment}
archive: true
> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#format-string-symbol)中, 不再更新.
> 原博文: [Python基础](/2015/08/31/python_basic/){: target='_blank'}
{:/comment}

- 基础篇介绍简单的语法, 变量类型, 判断循环, 函数和对象的简介, 加载模块, Python一些语法外基础知识.
- 中级篇介绍稍微复杂点的基础语法, 可能会根据内容展开.如更复杂的函数, 
- 进阶篇就是一些知识点进一步的展开了.
- 各式语句和内建函数篇作为查询, 或者嵌套其中.

这里尽量不讲内建模块!

### 关键词和内建函数列表

看着关键词列表, 能熟知多少?

and   |  as  |  assert  |  break  |  class  | continue  | def |  del  | elif   |  else |  except |
exec  |   finally  |   for  |   from   |  global  |  if  |  import  |  in  |   is   | lambda  |  not  |  
or  |  pass  |  print | raise |  return |  try | while |  with |  yield |

下面的内建函数掌握多少啦?

abs()        | cmp()       | file()      | hex()        | long()        | ord()       | reversed()     | super()
all()        | compile()   | filter()    | id()         | map()         | pow()       | round()        | tuple()
any()        | complex()   | float()     | input()      | max()         | print()     | set()          | type()
basestring() | delattr()   | format()    | int()        | memoryview()  | property()  | setattr()      | unichr()
bin()        | dict()      | frozenset() | isinstance() | min()         | range()     | slice()        | unicode()
bool()       | dir()       | getattr()   | issubclass() | next()        | raw_input() | sorted()       | vars()
bytearray()  | divmod()    | globals()   | iter()       | object()      | reduce()    | staticmethod() | xrange()
callable()   | enumerate() | hasattr()   | len()        | oct()         | reload()    | str()          | zip()
chr()        | eval()      | hash()      | list()       | open()        | repr()      | sum()          | \_\_import\_\_()
classmethod()| execfile()  | help()      | locals()     |   |   |   |   |

# 基础语法 {#basic_gramma}

> 原博文: [Python基础](/2015/08/31/python_basic/){: target='_blank'}

基础内容不多, 包括掌握:

- 内建类型和变量
- 表达式和语句(判断和循环)
- 简单的函数和对象定义使用
- 文件读写和输入输出
- python基础的杂项知识

## 内建类型,变量

### 几种内建类型:

##### 数值型

- int: 普通整型, [-2147483648,2147483647], 支持8进制`055`, 16进制`0xff`表达
- long: 长整型,可以无限..如1000000000000`L`
- float: 浮点型, 都是双精浮点,支持科学计数法. 如1.0, `1.` , 1.0e-10
- complex: 复数型, 实际是两个双精度浮点. `1+2j`, 
- bool: 逻辑型, `True` , `False` (分别相当于1,0)

PS: 

- int('6.000000000000000000e+00')类型转换会报错,float('6.000000000000000000e+00')则可以

##### 序列型(Sequence),集合,字典

- list: 列表型(可变序列型)
- tuple: 元组型(不可变序列型)
- set: 可变集合型,另有不可变集合型 frozenset.
- dict: 字典型
- str: 字符串型(不可变序列型)
- unicode: 字符串型(不可变序列型)
- bytearray: 字节数组(可变序列型)

##### 常见重要基础类型

- file: 文件型,通过句柄进行操作.
- 函数: 自定义如function类, 内建 builtin\_function\_or\_method, 对象方法 method_descriptor或function
- 对象: object等
- 模块module: 包括模块和包 
- iterator: 迭代器类型
- Exception和Error: 异常和错误

##### 特殊类型

- NoneType: `None`, 缺值.bool可以转为False,str转为str,int不能转.
- NotImplementedType: NotImplemented, 未执行, 出现在数字处理方法.bool后成True. 少见
- ellipsis: Ellipsis, 用于表明存在"..."语法.bool后成True. 少见

### 变量: 

- 弱类型的,赋值时根据内容自动定义类型.
- 变量名可以字母数字和\_组成,开头字母或\_
- python没有常量, 没有机制保证其不被改变.一般常量用大写作名字, 自己不去操作他就行了.


## 列表,元组,字符串,bytearray,字典,set

### 序列sequence
- 索引 index: `seq[i]` 可以获取元素,索引号从0开始, 最高索引是`len(seq)-1`.
- 分片 slicing: `[i:j]`: 所有索引k: i<=k<j的元素的列表, `[:j]`:0到j-1元素,`[i:]`:i到最后一个元素, `[i:j:k]`k可以控制采样步长,若k为负数,先将列表倒序再采样.
- 长度: `len(seq)` 可以获得元素总数.
- 成员检查: `data in seq` 返回对错.
- 负数索引: -1代表最后一个元素的索引,注意a[:-1] 则不包括最后一个(最后一个即终止).
- **不可变序列**:tuple, string, unicode. 和可变序列相比, 缺少了元素赋值能力和del能力,一旦定义,就不能修改元素. 但如果元素是可变序列,其内容依然可以被修改, 例如: a=[1,2];b=(a,);改变a的元素,b也会改变.但b[0]=c则不行.
- 不可变序列可进行哈希化hashable,而可变序列则不可以.

PS: 

- (序列)变量不能以数字开头，只能含字母数字或下划线。区分大小写。
- 单元素分片是值, 如a[i]; 但是多于一个元素就是序列了。

具体类型:

#### 列表 list 

- [element1,element2...]
- 元素可以是任何对象, 大小可随时修改. 可变序列.
- 分隔符`,`,一个元素时[a]来定义.无元素[].
- [1]*3 -> [1,1,1]; [1]+[2]=[1,2]
- 不可以对不存在元素的索引处赋值, 例如10个元素的a, a[15]=0肯定错.
- 方法: append(v),insert(i,v), pop([i])等.
- list()


#### 元组tuple 

- (element1,element2...)
- 元素可以是任何对象, 定以后不能修改, 不可变序列.
- 分隔符`,`,一个元素时(a,)来定义(防止括号歧义).无元素().
- tuple()

#### 字符串型str 

- "string"或'string' (等价), `'''.......'''`字符串块,包含整段字符串,包括其中的换行等.常用于大段文字说明.可以前面加r.
- 支持转义`\`, 当特殊符号如`', ", \`可以通过转义来表达.
- `r"string"`: 字符串不进行转义(转义符失效).
- 字符串型是不可变序列.因此不能随意对字符串的变量替换其内容,如用索引/分片赋值.
- python没有字符型char,直接用单字符串代替.字符大小最少是8-bit一字节.  
- str(), chr(), ord()
- 注意机读形式和人读形式区别：例如长数10000，但机读为10000L；字符人读abc，机读为’abc’，print时是用人读形式，而`repr`函数则是可把人读形式转化为机读形式，并把结果保存为人读形式。因为变量必须非数字起头，所以机器默认abc为变量，’abc’为字符串输入，故repr(‘hello’)实际就是’hello’,没有意义。
- r’abc\n’就是abc\n，但r’let\’s go’必须转义，否则语法错误，这样进行r处理后输出let\’s go。同理若r’c:\’会因转义了’报错，而r’c:\\’ 则会输出c:\\。
- 字符串是特殊的序列，但是列表不可以和字符串合并相加。另外，用in检测成员资格时，[‘abc’,’def’,’ghi’]必须对应abc才能true，bcd则false。但是对于字符串’abcdefg’，只要包含相同'bcd'都true。而且seqA in seqB也需要A作为子元素才行。
- 字符串格式化：str %转换标志(-+空格0)最小字段宽.精度值或* 最后跟转换类型。-为左对齐，+为数值要加+-号，空白为正数前空格，0为转换值不足最小字段宽补0。精度值为最大字符数，*的话需要后面赋值。转换类型常用d/i正数f浮点s字符串r机读字符串C单字符x/X大或小写16进制。可以用元组来格式化, 列表不行!字典格式化%(key) % {key:val}


#### unicode型unicode 

- u"string"或unicode(string)
- unicode型是不可变序列.
- 字符大小是16-bit或32-bit,取决于编译时参数.在sys.maxunicode可查询.
- unicode(), unichr(), ord(), u.encode()

#### 字节数组型bytearray

- bytearray(seq) 或 bytearray(string)
- 可变序列
- 储存字节的对应数值. 

### 字典dict

- `{key: value, ....}`或`dict[key]=value`
- 无序, key键和value对应值组成每项
- key需要可以被哈希化,因此不能是可变型对象如字典,set(frozenset可以),可变序列等.
- value可以是任何东东..包括字典,列表等.
- 空字典可以随意用赋值添加项，而列表不行。x=[],x[42]=’go’出错;而dict={},dict['a']=99则可以.
- 方法: get(k[,v]), pop(k)

### 集合set和frozenset

- 无序, 元素唯一的对象.
- 对于数值, 不论类型, 会进行数值比较.如1.0和1归为一项
- 不支持索引, 只能用于in检索,长度len操作,迭代等.
- 去除重复元素后, 有利于快速成员检查in, 种类数的确定.
- 支持: `t|s` 并集; `t&s` 交集; `t-s` 差集; `t^s` 交集的补集(只出现t或s中，不能都有)
- 两种类型: set()构成的可变集合(set型)和frozenset()构成的不可变集合(frozenset型).frozenset型可用于哈希化从而进一步作为一个元素或者作为字典的键.

## 表达式和语句

- 注释: python只有单句注释, 使用`#` 作为注释符.
- 表达式就是运算式子,包括数学运算, 比较运算, 逻辑运算, 变量表达等.
- 语句就是执行一句命令, 告知计算机操作, 一般造成相应变化, 例如赋值语句, 执行函数命令等. 往往表达式是语句的一个成分(宾语主语), 仍需要一个动作(动词).
- 不同语句可以使用`;`分隔从而方便写在同一行内(不提倡). `;`有语句结束的判断作用.
- 在IDE交互模式, 输入`a` 会输出变量a的值, 但 `a;` 就相当于空语句, 不会输出a的值.
- 表达式, 语句, 函数, 对象, 变量均是**大小写敏感**的.
- 表达式结果取决于复杂类型的成分的类型,例如 *10/3* 返回结果依然是int: 3, 而 *10.0/3* 则是float: 3.333
- 空语句: `pass`,可以在需要语句块的地方填充以防止语法错误,实际不进行任何操作. 
- **语句块**就是一系列语句的集合,例如if/for/while/class/def等后面跟随相应语句块进行操作. python的语句块利用**缩进**(indent)来描述语句块, 同一缩进层次的作为一个语句块. 缩进没有限定,可以tab, 可以N个空格.一般使用四空格或一个tab. 注意tab和空格不能混用, 否则会语法错误报错. 可以在 *notepad++* 中将 行开头的 *tab转空格* 或者反过来也行.

### 运算和判断表达式

- `and` 或`&` : 与运算, 会短路(执行第一个否就不执行第二个).
- `or` 或`|` : 或运算,会短路(执行第一个是就不执行第二个).
- `not` 非运算, 在表达式的前面.
- `==` 相等判断. 值判断, 不包括类型.
- `!=`或`<>` 不等判断
- `<`,`>`,`>=`,`<=` 不用我解释了吧..

## 判断和循环

### if...elif...else...判断语句

语句块使用缩进作为定义.没啥特别的. 

~~~python
if [condition]:
	statement
elif [condition]:
	statement
else:
	statement
~~~

### for 循环

in 后面一般是可迭代对象, 例如列表, 数组, 字典(迭代key), 文件对象. 要用数字控制,一般使用range.

在对序列进行for in时，尽量不要对该序列进行删增，排序等操作，易错(可能干扰了迭代器)！最好先用一个替代序列seq2=seq1[:]来赋值进行操作。

~~~python
for i in iterableObj:
	statement;
#judge whether iterable:
isinstance(obj, Iterable);

# such as:
# iterable obj
for i in list/tuple/set/string/:
# number list
for i in range(start, end+1, step):
# key in dict
for key in dict:
# value in dict
for val in dict.value:
# double var 
for key,val in dict.items():
for index,vali in enumerate(list):
	statement;
~~~

### while循环

形式太简单..一般用于 **不定次数循环**. 这里的while还支持else子句 (不满足时执行一次, 也就是最少执行一次).

~~~python
while condition:
	statement;
[else:]
	[statement;]
~~~

### break,continue, exit

- `break`: 打断整个循环并跳出.
- `continue`: 跳过该次循环的后面部分, 开始下次循环.
- `exit()` : 结束脚本运行, 出错时再用.

## 输入输出和文件

### print语句/函数

- print 语句(2.\*, 3.\*使用print函数): `print obj/expression`. 
- 可以使用`,`连接成份, `,`会化作空格, 此时数值可以和字符串一起输出, 如: print "age",30
- `+`可以连接字符串,但是数值**必须**要先`str(val)`转化为字符串. 若是表达式,则会进行计算后再输出.
- 关于print输出时，用`,`结束该行, 下一行再用print时会两行会连接(留一个空格)，从而可避免换行；也可以行末用转义符`\`换行使得下一行的内容紧接上一行；
- 用`；`表示另一个逻辑行,表示语句结束。需另外有语句。

### raw_input和input函数

- `raw_input([promt])`: 获取输入,返回输入的字符串. promt是提示语句,不换行.
- `input([prompt])`: 获取输入并运算后转化为相应值的字符串返回.相当于: `eval(raw_input(prompt))`.
- 获取一个字符串, input需要输入"abc",而raw_input只要abc. input后输入1+2, 返回数值3.
- raw_input() 也常用于卡住脚本不让其终止, 方便调试或者观看脚本结果.

### 文件读写简介

- 文件是通过文件句柄(file handle)来辨认和处理的, 可以认为文件句柄就是一个文件对象/实例吧. 文件不是通过文件名来操作的, 是通过文件句柄操作的! 如 f.read(); f.write(); f.close()
- 文件对象使用`handle=open(filename,action)`形式来打开文件并进行相应操作.和一般语言的文件对象处理类似.
- action有: 'r'只读不能写(默认方式, 可以不指定action采用默认只读); 'w' 只写不能读; 'a' 追加; 'w+','r+','a+' 读写均可; 'rb'和'wb' 以二进制形式读/写.
- 读取文件: 
	- f.read() : 读取全部到一个字符串; 
	- f.readline() : 读取一行, 文件指针指向下一行.
	- f.readlines() : 读取文件并根据换行符切割成一个列表, 每个元素是对应一行 (注意: 每行依然带有换行符).
	- `for line in f`: 使用迭代器方式逐行读取文件内容到line变量, 此时不能再用read和readline等.
- 写文件:
	- f.write(string) : 将string内容写到文件, 注意可能要自己写换行符`\n`.
	- f.writelines(str_list) : 将字符串列表内容逐个写到文件内. 注意! 不会帮你加换行符, 依然要手动加换行符, 只是不用一个一个写罢了... 
- 文件关闭: f.close() 文件读完或者到末尾要养成文件关闭的习惯, 否则该文件会一直处于打开状态! 如果想对文件进行读取并原位修改可以先读取, 关闭文件, 在以写模式打开进行输出.

## 函数

~~~python
def funcname([argv1,argv2..]): 
	contents;  
	return [vars]
~~~

- 定义函数,也可以不加形参argv,return定义返回内容(无值返回None)
- 返回值可以是多个值return x,y (本质以元组返回). 接收时 x,y=F()即可.
- 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”.
- 函数形参的默认参数最好是不变对象,更多请参考[传递参数](./#mid-pass-func-argv).
- **\*args**表示任何多个无名参数，它是一个tuple；**\*\*kwargs**表示关键字参数，它是一个 dict(实参时用**变量名=值**)。并且同时使用\*args和\*\*kwargs时，必须\*args参数列要在\*\*kwargs前。若此时给的是list或tuple,可直接在实参前面加`*`.如func(\*list1); 也可以给实参字典前加`**`,如func(**kw)。

## 类的一般知识 

Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。用类作为抽象"模板", 而创建机体的一个对象, 称之为实例(Instance).用来储存对象属性数据的称为属性, 而调用来进行针对对象的处理的关联函数,称之为方法.

### 定义一个类

~~~python
# 定义一个普通类, 不进行继承
class ClassName(): 
    statement

# 定义一个继承于父类的类
# 可以多个父类
class ClassName(Parent1[,Parent2..]):
    statement

# 定义一个新式类,继承自object
class ClassName(object): 
    statement

# 使用type函数定义类
# parents是元组,继承的父类,第三个是字典,定义属性和方法
ClassName=type("ClassName",(parents),{"property/method":value})
~~~

### 定义类属性和方法

~~~python
class ClassName():
    # 定义类内的属性 
    prop1=value1

    # 初始化函数,在类初始化时可以传入参数.第一个必须是self 实例本身.
    __init__(self[,var1,var2...]):
        # 通过方法绑定属性,动态绑定
        self.prop1=var1
        self.prop2=var2
        statement
    # 一般的方法,对比一般函数,第一个总是self 实例本身
    method1(self[,var1...]):
        print self.prop1
~~~

### 创建实例

创建实例就是`类名(参数)`,参数取决于`__init__`方法.

~~~python
# __init__(self)
obj=ClassName()
# __init__(self,var1,var2)
obj2=ClassName2(varA,varB)
~~~

## 模块module和包package

编程语言通过将语意作用相关的程序放在一起, 形成整套程序的一份零件. 而我们在编写程序时亦都会经常借助于外部的现成工具. 这些"零件"和"工具"协助起来构成我们的程序. 

在C++里, 头文件和源文件构成一个"工具零件", 而带main函数的部分则成为主要程序运行主体. Python里哪个是主体取决于执行哪个脚本, 所以文件都储存在py文件中, 或者进一步编译成pyc/pyd文件. 每一个这种文件都可以作为一个工具, 称之为`模块module`. 而将相关功能的模块放在一个文件夹里, 则构成了`包Package`. 加载模块和包就可以获得相应的函数和类对象, 从而获得新功能.

### 模块

任何一个py/pyc/pyd文件都可以作为一个模块. 只需要使用`import 模块名`加载即可. 加载后调用模块里的成员使用`模块名.成员名`, 像对象属性/方法一样. 模块名在当前文件中有命名空间作用, 区分可能同名的变量/函数/类. Python有很多内建模块装有相当强大的功能, 一般直接加载即可(不需目录名等). 自定义模块可以放到搜索路径, 当前目录下或者相应包中. 详细[参看](./#more-module-package)下面的部分.

#### 加载模块最常用方法

~~~python
# 加载模块1和模块2, 逗号分隔
import module1,module2
# 加载模块module并重命名为mod, 便于方便写少些字 233 
import module as mod 
# 只从模块中加载其中的某成员,包括变量,函数,类等. 还可以把该成员改名为sth2
# 该加载方式调用成员时不再需要模块名.
from module import sth [as sth2]
# 加载模块中所有成员, 不需再用模块名. 
# 为防止命名空间冲突, 不建议使用(除非很清楚没有冲突) 
from module import *
~~~

### 包

不同于c++可以加载头文件时使用目录结构, python不能使用目录'/'或'\\'. 但便于管理仍然把相关模块放到一个文件夹内, 这个文件夹称之为包Package.  

为了识别这个文件夹是包而不是一般文件夹, 需要在文件夹下存在一个`__init__.py`文件(可以是空).这样就可以通过包名来加载里面的模块. 例如`import packagename.modulename`. 也可以直接加载包名(效用取决于`__init__.py`,更多细节参考[进阶篇说明](./#more-module-package).  

## 标准IDLE和设置

- `_`在交互模式下代表上一个结果。如3+4~~7, 2+_~~9
- 查看历史记录Alt+p（之前）和Alt+n（之后），linux下是Ctrl+P/N （注意要小写状态。。)
- 关于补全expand word(Alt+/)指的是自动填充曾经输入的,可多按几次换别的;show completion默认是Ctrl+space,但一般被输入法占据，可用Ctrl+Alt+Space,显示可补全的所有东西提示，用上下方向键控制选择。Tab补全,如果只有一个可选则自动补全,否则会和show completion一样。
- IDLE Python集成开发环境
- edit|run或`Ctrl+F5`为运行程序
​- Go to line （`Alt+G`）直接跳到某一行
- Indent region：使所选内容右移一级，即增加缩进量。`Ctrl+]`
- Dedent region：使所选内容组左移一级，即减少缩进量。`Ctrl+[` 和括号指向相关..
- Comment out region：将所选内容变成注释。`Alt+3`
- Uncomment region：去除所选内容每行前面的注释符。`Alt+4`
- Tabify region:使所选空格变Tab.`Alt+5`
- UnTabify region:使所选Tab变指定空格.`Alt+6`
- 关于python安装路径注册表: HKEY\_LOCAL\_MACHINE\SOFTWARE\Wow6432Node\Python\PythonCore\2.7\InstallPath. 在安装一些python应用时检测版本时, 可以修改这里的值来变更安装对应的版本及路径.


## 小知识

- `#! /usr/bin/env python` 首行, 或者`#! /usr/bin/python2`, 再`chmod +x *.py`就可以使脚本在unix基础系统上能直接执行.(如果是window编写的可能出现最后 **换行符问题** 不识别,此时先`dos2unix *.py`就好了)
- 第二行 `# -*- coding: utf8 -*-` 指明字符集，用utf8就可以支持中文了！
- 定义包:在某目录dira下建`__init__.py` 可以为空,然后将相应的a.py,b.py放进去 然后import dira.a就可以了
- 不懂按`help(xx)`, 已加载对象模块和内建内容可以 *直接用名字*,否则要用 *字符串* 形式"xx".
- 避免window下运行完程序关闭窗口，可写入：raw_input(‘press <enter>’) 一句
- 好习惯在开头几行加入 `#Filename: abc.py`作注释该文件名.
- 关于`.py`和`.pyw`区别在于,后者使用pythonw.exe来运行,没有了控制台(如dos).
- `.pyc`文件是编译好的模块文件,可以加速运行.可以用py_compile.complie(file)来编译
- `if __name__ == '__main__': main()`  该句常用,因为限制后面内容为执行脚本而非模块内容. 使用该句后的语句块只有在py文件被直接运行(如python a.py)时才执行, import a.py 就不会则行.
- 关于换行输入，例如abc想把bc放在输入的第二行便于观察，按enter换行会变确定而出错，因此需要把enter键的值转义为换行.因此行末的\为转义换行，而真需要`\`时需要输入`\\`. 不能最后\’ 因为会转义。一般不是断裂变量名/字符串时, 可以忽略末尾换行符(会自动识别语句没结束, 换行再读取直到语句结束), 但良好习惯还是可以加上`\`, 反正无害.
- 在keyword的关键词声明中如def,if,elif等，需要用`:`引出其实质内容块，并进行缩进。在def语句中，如果在IDLE shell中进行定义，结束时enter后在退出该块后，再按一下enter结束；在return后，则会自动退出块缩进。
- 关于import: 需要在系统路径中含有该路径,可以设置PYTHONPATH 的环境变量来永久添加. 暂时性增加,一般在发布程序时,因为不能改系统变量,所以,这时最好把模块放在同目录或附近目录下,此时,添加搜索路径方法:
- import sys;sys.path.append('..')或sys.path.insert(0,'..')(后者可以优先化). 也可修改..为.或任意目录.
- 读取环境变量 filename = os.environ.get('PYTHONSTARTUP')
- 判断文件存在: `if filename and os.path.isfile(filename):execfile(filename)`



# 中级语法 {#medium-gramma}

> 原博文: [Python中级篇](/2015/10/21/pyMedium/){: target='_blank'}

- 列表: 列表生成器, 排序函数sort, 高阶函数 map/reduce/filter.
- 字符串: 格式化字符串, 编码问题.
- 函数: lambda, 偏函数, 闭包和返回函数, 装饰器
- 对象: 
- 迭代器: 
- 异常: 

进阶篇将会补充比较少用的语法和更详尽讨论个别内容.


## 列表

### 列表生成式(映射list)

`[expression for i in Iterable]`, 也可以嵌套: `[expression for i in Iterable1 for j in Iterable2]`, 甚至可以加入判断条件 `[expression for i in Iterable if condition]`. 循环也可以像一般for循环支持多循环变量. 迭代产生列表时若某项出错,则会报错生成失败.

列表生成器使用一句的语法用生成器生成列表的各个项, 仅适用于列表,而且记得加`[..]`

就是将迭代的i进行相应表达式操作, 生成相应一个新的列表, 若加入判断条件,列表长度可能改变. 例如

~~~python
[ x*x for x in range(1,11)]
#->[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[ x*x for x in range(1,11) if x%2 = 0 ]
#->[4, 16, 36, 64, 100]
[m + n for m in 'ABC' for n in 'XYZ'] 
#->['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.iteritems()]
#->['y=B', 'x=A', 'z=C']
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
#->['hello', 'world', 'ibm', 'apple']
g=( x*x for x in range(1,11) );g
#-><generator object <genexpr> at 0x104feab40>
A=[]
for i in g:A.append(i);
~~~

将中括号变成小括号, 返回的将是`生成器`而不是列表.

### sorted排序函数

`sorted(list[,func])`: 对列表排序, 默认从小到大. 可以自定义提供函数`func(x,y)`来自定义排序, 默认当x < y 返回-1 (即不变顺序), x > y返回1 (即变顺序), x==y 返回0 (即不变顺序).

~~~python
# 缺省从小到大,所以默认函数
def funcsort(x,y):
    if x<y:return -1
    elif x>y:return 1
    else return 0

# 按字符第一个字母(不考虑大小写)排序

def strsort(x,y):
    x1=x[0].upper()
    y1=y[0].upper()
    if x1<y1:return -1
    elif x1>y1:return 1
    else return 0
~~~

## 字符串

### Python字符串相关 {#mid-string-relative}

> 原博文: [Python字符串相关](/2015/06/23/python-string/){: target='_blank'}

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

### 内建相关函数

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


### 字符串方法（并不能改变字符串的值，只起到返回作用）
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

### string标准库
现在已经很少用. 内置一些奇怪的常量, 还有一些str类不具有的方法.

#### 常量:

- `whitespace` : a string containing all characters considered whitespace
- `lowercase` : a string containing all characters considered lowercase letters
- `uppercase` : a string containing all characters considered uppercase letters
- `letters` : a string containing all characters considered letters
- `digits` : a string containing all characters considered decimal digits
- `hexdigits` : a string containing all characters considered hexadecimal digits
- `octdigits` : a string containing all characters considered octal digits
- `punctuation` : a string containing all characters considered punctuation
- `printable` : a string containing all characters considered printable

#### DATA:

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

#### 方法

- `string.Template(’a’)`       模板字符串，结合$x和A.substitute(x=’a’)使用
- `string.atoi(str[,base])` 字符串到整型,base默认10进制,可以输入8/16/2等
- `string.atol(str[,base])` 字符串到长整型,base默认10进制,可以输入8/16/2等
- `string.atof(str)`    字符串到浮点
- `string.capwords(str[,sep])`  利用sep作分隔的词首字母大写，较好，返回字符串.默认为空格分隔.
- `string.maketrans(‘ab’,’cd’)`      将256位字符表中a和b相应换成c和d，返回字符串.用于translate方法。
- `string.capitalize(string)`    首字母大写
- `string.lower(string)`    全部小写化
- `string.upper(string)`    全部大写化
- `string.replace(string,old,new[,maxsplit])`     字符串中替换,max为最多替换个数
- `string.join(list[,sep])`  使用分界符(sep,默认空格)将字符串列表连接起来.
- `string.split(string,sep=None,maxsplit=-1)` 以sep为分界符将string分开成一个列表

(不断更新哈...)

TODO: 字符串格式化; string的方法; print时的输出差异. 

---------

### Python字符串编码问题 {#more-encoding}

> 原博文: [Python字符串编码问题](/2015/10/17/PyEncode/){: target='_blank'}

字符串实质是字符的一个集合,而字符则以数字形式储存. 最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255, 两个字节可以表示的最大整数是65535，3个字节最大整数是16711425, 4个字节可以表示的最大整数是4294967295. 三个字节就足够多了...

#### ASCII

最早只有127个字母被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，Z编码90; 小写字母a编码97, z的编码是122。这种编码一个字符只需一个字节, 对于英文字符而言足够了.这也是最基础的字符集.

#### GB2312等local语言编码
为了解决如汉字等其他语言的编码问题, 出现了如GB2312码等, 用于把中文编进去. 这些编码最少需要两个字节,一般向下兼容ASCII码.

然而.各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。

#### Unicode
Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了, 便于统一使用.Unicode标准在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。Python中unicode的编码字节数取决于编译时环境.

#### UTF-8
如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果要传输的文本包含大量英文字符，用UTF-8编码就能节省空间.

-------------

- 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
- 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：

----------

#### Python的字符串编码

#### ascii

Python2默认使用ascii编码. Python3默认使用unicode进行编码. 即使使用ascii编码, 在编码转换时中间总是经过unicode.

~~~python
ord('a') #->97
chr(97) #->a
~~~

#### unicode

unicode.encode和decode是两个unicode字符串的重要方法,可以将其强行转换为别的编码,encode是unicode->other, decode是other-> unicode. 

~~~python
print u"你好!" 
# -> 你好!
u"你好" 
# -> u'\u4f60\u597d'
print unichr(0x4f60)
# -> 你

# unicode to other

u"你好!".encode('utf-8')
# -> '\xe4\xbd\xa0\xe5\xa5\xbd!'
u"你好!".encode('gb2312')
# -> '\xc4\xe3\xba\xc3!'

# other to unicode
print '\xe4\xbd\xa0\xe5\xa5\xbd!'.decode('utf-8')
# -> 你好!
~~~

###### Reference

1. [Unicode-wiki](https://zh.wikipedia.org/wiki/Unicode)
2. [UTF-8-wiki](https://zh.wikipedia.org/wiki/UTF-8)

------------

### 格式化符格式化字符串 {#format-string-symbol}

> 原博文: [Python字符串格式化](/2015/09/13/PyStringFormat/){: target='_blank'}

在许多编程语言中都包含有格式化字符串的功能，比如C和Fortran语言中的格式化输入输出。Python中内置有对字符串进行格式化的操作%。

#### 模板

格式化字符串时，Python使用一个字符串作为模板。模板中有格式符，这些格式符为真实值预留位置，并说明真实数值应该呈现的格式。Python用一个tuple(其实可以不写tuple括号也可以)将多个值传递给模板，每个值对应一个格式符。如下面的例子：

~~~python
print("I'm %s. I'm %d year old" % ('Hom', 30))`
~~~

"I'm %s. I'm %d year old" 为我们的模板。%s为第一个格式符，表示一个字符串。%d为第二个格式符，表示一个整数。('Hom', 30)的两个元素'Hom'和30为替换%s和%d的真实值。 在模板和tuple之间，有一个`%`号分隔，它代表了格式化操作。

整个表达式实际上构成一个字符串表达式。我们可以像一个正常的字符串那样，将它赋值给某个变量,如:

~~~python
a = "I'm %s. I'm %d year old" % ('Hom', 30)
print a
~~~

也可以用**词典**来传递真实值,如：

~~~ python
print("I'm %(name)s. I'm %(age)d year old" % {'name':'Hom', 'age':30})
~~~

可以看到，我们对两个格式符进行了命名。命名使用()括起来。每个命名对应词典的一个key。

#### 格式符

格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:

- `%s`    字符串 (采用str()的显示)
- `%r`    字符串 (采用repr()的显示)
- `%c`    单个字符
- `%b`    二进制整数(只能用于字符串format方法和format函数,`%`不能用.)
- `%d`    十进制整数
- `%i`    十进制整数
- `%o`    八进制整数
- `%x`    十六进制整数
- `%e`    指数 (基底写为e)
- `%E`    指数 (基底写为E)
- `%f`    浮点数
- `%F`    浮点数，与上相同
- `%g`    指数(e)或浮点数 (根据显示长度)
- `%G`    指数(E)或浮点数 (根据显示长度)

要是想输出`%`则要使用`%%`进行转义操作.

#### 更复杂的控制

`%[(name)][flags][width].[precision]typecode`

- `(name)`: 命名,用于字典控制赋值
- `flags`: 可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
- `width`: 显示宽度,总长度,会补齐空格.
- `precision`: 表示小数点后精度.

比如：

~~~ python
print "%+10x" % 10   # "        +a"
print "%04d" % 10    # "0010"
print "%6.3f" % 2.3  # " 2.300"
~~~

上面的width, precision为两个整数。我们可以利用`*`，来动态代入这两个量。比如：

~~~python
# python 3.0
print("%.*f" % (4, 1.2))  # "1.2000"
~~~

Python实际上用4来替换*。所以实际的模板为"%.4f"。

#### format函数和字符串format方法

这是另一种处理方法格式化方法: 通过函数/方法. 例如下面的例子:

要将一个列表(float型)的内容格式化并空格分隔写到文件中,一行怎么写?

`f.write( ' '.join(map((lambda v: format(v, '<8.5f')),list))`{: .language-python} 或 `f.write(' '.join([ "%-8.5f" % i for i in lll]))`{: .language-python}

两者结果是一致的. 用lambda函数的好处是, 可以定义一个新函数来方便统一处理一系列的格式, 当需要修改时只修改一处即可. 而`%`方法则要把每处的格式化式改写一遍. 

另外, 试试:

`print "%-"+str(var)+".5f" % i`{: .language-python}, 你会发现报错: *not all arguments converted during string formatting*, 原因是该格式化字符串先执行再相加, 即`".5f" % i`优先, 要是`print ("%-"+str(var)+".5f") % i`{: .language-python} 则没有问题. 格式化串分析在字符串合并前进行,因此错了. 但`format(i, "<"+str(var)+".5f")`{: .language-python} 是可行的

##### format函数

format(value[, format_spec]), 后面是格式表达式, 默认是"", 即不格式化直接字符串化. 很基础简单的函数.

和`%`格式化式类似, 支持上面提及的`[flags][width].[precision]typecode` 格式化表达式. 但注意:

1. format函数不需要`%`或后面提到的`:`
2. format函数左中右对齐分别使用`<^>`
3. 其余0填充, "0<6.3f"这些表达是一样的.
4. 只能对单一个元素进行操作, 不支持别名`(name)`,不支持字典, 列表等.

##### 字符串的format方法

str.format(*args, **kwargs), 支持多种方式的格式化, 在Python2.6后引入. 和之前两种方法不同, 主要使用`{}`和`:`进行格式化,前者指定位置, 后者相当于`%`.

###### 映射式格式化

通过大括号标记为一个"元素", 然后format里的`*args`或`**kwargs`逐一对应进行填充. 支持多种方式:

- 通过索引号或位置对应: 可以使用参数位置定应的索引号进行对应, `{index}`; 也可以根据位置使用匿名方式(Py2.7+才支持), `{},{}`. 后者大括号对数超过参数个数, 或者索引号大于参数个数, 都会报错: *IndexError: tuple index out of range*

~~~python
'{1},{0},{1}'.format('a',5)
# a,5,a
'{},{}'.format('a',5)
# a,5
~~~

- 通过序列调用下标

~~~python
s=['Hom',30]
'{s[0]}:{s[1]}'.format(s)
~~~

- 通过命名方式(类似于字典key=value关系)

~~~python
'{name}:{age}'.format(age=30,name="Hom")
~~~

###### 格式限定符

首先将格式化限定式写在`{}`内, `:`作为格式化标识开始. 同样支持 `[flags][width].[precision]typecode` 格式化表达式, 其中左中右对齐和format函数一样, 使用`<^>`.

~~~python
':_<8.4f'.format(6.4)
#6.4000__
~~~

#### 总结

Python中内置的`%` 操作符可用于格式化字符串操作，控制字符串的呈现格式。Python中还有其他的格式化字符串的方式，但%操作符的使用是最方便的。

format函数提供函数化的格式化办法, 而字符串的format方法则提供更丰富的操作方式.

## 函数

### Python传递参数 {#mid-pass-func-argv}

> 原博文: [Python传递参数](/2015/08/07/PyArgsInput/){: target='_blank'}

和C/C++那种传值传址的传递参数不同, Python中函数参数的传递是通过“赋值”来传递的。函数参数的使用可以概括地分为两个方面，一是函数参数如何定义，二是函数在调用时的参数如何解析的。

#### 函数形参定义

函数参数的定义有四种形式：

1. F(arg1,arg2,...)  一般形式
2. F(arg2=,arg3=...)  默认值定义
3. F(*arg1) 不定参数个数
4. F(**arg1) 不定的关键字赋值传给字典

实际中, 这四种方式可以组合在一起形成复杂多样的形参定义形式。在定义或调用这种函数时，要遵循以下**参数顺序规则**：

1. `arg=`必须在`arg`后
2. `*arg`必须在`arg=`后
3. `**arg`必须在`*arg`后

否则,python认不出究竟哪个参数打哪个参数,就会报错.

#### 函数调用形参赋值

在函数调用过程中，形参赋值的过程是这样的：

1. 按顺序把`arg`这种形式的实参给对应的形参
2. 把`arg=`这种形式的实参赋值给形参
3. 把多出来的`arg`这种形式的实参**组成一个tuple**给带一个星号的形参
4. 把多出来的`key=value`这种形式的实参转为一个dictionary给带两个星号的形参。

支持关健字赋值法,即调用函数赋值时,指定相应形参名和值. 此时仍遵循`arg=`必须在`arg`后的原则, 而同级的`arg=`则不必遵守形式参数的前后顺序.

#### 说明和实例

- **“传统”方式只给形参名：F(arg1,arg2,...)**   
一个函数可以定义一定个数参数，参数（形式参数）放在跟在函数名后面的小括号中，各个参数之间以逗号隔开。用这种方式定义的函数在调用的时候也必须在函数名后的小括号中提供相等个数的值（实际参数），不能多也不能少，而且顺序还必须相同。也就是说形参和实参的个数必须一致，而且想给形参1的值必须是实参中的第一位，形参与实参之间是一一对应的关系，即“形参1=实参1 形参2=实参2...”。很明显这是一种非常不灵活的形式。  

如：`def addOn(x,y): return x + y`，可以用addOn(1,2)的形式调用(x=1,y=2),也可以addOn(1,y=2)和addOn(y=1,x=2)。多参addOn(1,2,3), 少参addOn(1), 违反参数顺序规则addOn(y=2,1)都会出错. 

- **形参名和默认值: F(arg2=,arg3=...)**  
在调用这种函数时，如果没有给对应的形式参数传递实参，那么这个形参就将使用默认值。  

如：`def addOn(x=3,y=5): return x + y`，可以addOn(6,8)-->x=6，y=8; addOn(7)-->x=7，y=5; addOn(y=6)-->x=3,y=6; addOn(y=4,x=6)-->x=6,y=4.  
当: `def addOn(x,y=5): return x + y`时,addOn(y=4,6)就会报错,不遵守参数顺序规则,6究竟是给谁的?!

上面两种方式定义的形式参数的个数都是固定的，比如定义函数的时候如果定义了5个形参，那么在调用的时候最多也只能给它传递5个实参。但是在实际编程中并不能总是确定一个函数会有多少个参数。此时要用下述两种方法来捕获未知的输入.

- **不定个数参数: F(*arg1)**  
以一个`*`加上形参名的方式定义形参，这个函数实际参数是不一定的，可以是零个，也可以是N个。不管是多少个，在函数内部都被存放在以形参名为标识符的元组tuple中。比如:

~~~python
def addOn(*arg):
    sum = 0
    if len(arg) == 0: return 0
    else:
        for x in arg: ##迭代元组内的值
            sum += x
    return sum
~~~

对这个函数的调用addOn() addOn(2) addOn(3,4,5,6)等等都是可以的。

有时候，要给`*arg`赋值，但有时又为了方便使用列表，这时加入以下例子中的判断或在**实参前加`*`**:

~~~python
def func(filedir,*strings):
    #The following is the same when use func(dir,*list_subdir)
    if type(strings[0])==list or type(strings[0])==tuple:
        strings=strings[0]

    print filedir+'/'+'/'.join(strings)
~~~
PS: 实际上，Python内部已经加入这种这样处理了,不过需要在前面加`*`,如传递的是list1,则`func(dir,*list1)`就可以了。func("/home/",\*["a","b","c"])和func("/home/",\*"a","b","c")等价。如果不加`*`,func("/home/",["a","b","c"])中strings实际是 *(["a","b","c"],)*.

- **不定个数并指定参数名: F(\*\*arg1)**  
形参名前面加`**`表示，参数在函数内部将被存放在以形参名的字典。这时候调用函数必须采用key1=value1、key2=value2...的形式。该方法的优点是还可以给出相应的参数名,从而通过字典中键值的处理进行一些操作和过滤. 比如：

~~~python
def addOn(**arg):
    sum = 0
    if len(arg) == 0: return 0
    else:
        for x,y in arg.items(): #或用迭代器arg.iteritems(), 迭代字典
            if (x[0] in "abcdefg"):
                sum += y
    return sum
~~~
那么对这个函数的调用可以用addOn()或诸如addOn(a=4,b=5,k=6)等的方式调用(此时返回9)。

听起来好复杂，实际是是很简单的。很直观，来看例子：

~~~python
def testArgs(x,y=5,*a,**b):
    print x,y,a,b

#test arguments
testArgs(1) # 1 5 () {}
testArgs(1,2) # 1 2 () {}
testArgs(1,2,3) # 1 2 (3,) {}
testArgs(1,2,3,4) # 1 2 (3,4)
testArgs(x=1) #1 5 () {}
testArgs(x=1,y=1) # 1 1 () {}
testArgs(x=1,y=1,a=1) # 1 1 () {'a':1}
testArgs(x=1,y=1,a=1,b=1) #1 1 () {'a':1,'b':1}
testArgs(1,y=1) # 1 1 () {}
testArgs(1,2,y=1) # 出错，2和y=1都是赋给y
testArgs(1,2,3,4,a=1) # 1 2 (3,4) {'a':1}
testArgs(1,2,3,4,k=1,t=2,o=3) # 1 2 (3,4) {'k':1,'t':2,'o':3}
~~~

##### 形参最好是不变对象

函数在定义的时候,默认参数的值就被计算出来了,也就是说形参赋的值对应的内存对象已定. 当使用可变对象时, 形参也会被改变.因此可能导致函数功能出错!!例如:

~~~python
def add_end(L=[]):
    L.append('END')
    return L
print add_end()
#->['END']
print add_end()
#->['END','END']
print add_end()
#->['END','END','END']
~~~

形参是可变序列, 定义后L指向一个数组, 当执行函数使用形参后,该形参默认参数对应的列表被修改,因此出错!

-----------

### 递归函数

其实就是函数内调用函数自身, 注意收敛终止就OK了.

~~~python
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
~~~

另外要注意栈溢出,如fact(1000)报错:RuntimeError: maximum recursion depth exceeded. 每当递归进行一次时,就会通过栈stack来保存数据记录,当函数返回时再通过栈逐层返回. python栈大小是有限的. 此时最好转用循环来改变思路. 传说有一种叫*尾递归* 的方法避免栈溢出, 但是python并不支持.

### 高阶函数

让函数参数接收别的函数, 函数再应变函数. 例如

~~~python
def add(x, y, func):
    return func(x) + func(y)
add(3,-4,abs)
# -> 7
~~~

#### map/reduce/filter函数
都是典型高阶函数.

- `map(func,list)` 将func应用于list每个元素并返回列表. 相当于[func(x) for x in list]
- `reduce(func,list)` 函数必须是接受两个参数的(否则报错),随后从前到后将元素和func(x,y)结果作进一步计算,即f(f(f(x1,x2),x3)x4)..
- `filter(func,list)` 将函数应用于list元素,若返回True则保留,否则去掉.最后返回过滤后的列表,相当于`[x for x in list if func(x)]`

### lambda函数 (匿名函数)

快速定义单行单表达式操作并返回的最小函数, lambda函数是从lisp借来的.虽然说lambda函数,但其实他是个语句关键词而不是一个函数.

`func=lambda 参数: 表达式` 等价于`def func(参数):return 表达式`, 也可以直接`(lambda 参数:表达式)(实参)`直接调用.

lambda函数代码较简, 但只适用于单个表达式, 并且不能包含命令(直接return),但可接受多参数. 如果函数内容较复杂,建议用def func().lambda函数一个重要应用是在高阶函数中作为函数参数传入.

~~~python

# 以下例子定义一个函数,若collapse为真,执行压缩字符串空白; 否则返回字符串.
# 其本事是函数,因为核心执行的是lambda部分.
processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
~~~

### 偏函数

是一种高阶函数,其实就是可以重新设定指定函数某些参数的默认值,返回一个新的函数. 

使用`functools.partial(func,*args,**kw)` 来进行重新定义默认值, 其中kw就是`arg=val`形式,而args就是一般的参数,会从原函数参数左边插入该些参数. 例如

~~~python
int2 = functools.partial(int, base=2)
int2('1000000') #>>> 64

# 等价于 :
int('1000000', base=2) #>>> 64

# 也可在偏函数中像原函数一样指定值:
int2('1000000', base=10) #>>> 1000000

# 指定*args部分:
max10 = functools.partial(max,10);
# 传入参数后等价于max(10,5,6,7)
max10(5,6,7)  #>>>10
~~~

### 闭包和返回函数

返回函数就是将一个函数作为结果返回. 当返回的函数在一个函数内时(就是函数内的函数), 称之为闭包(closure), 此时相关参数和变量都保存在返回的函数中.

返回的函数是一个新的对象, 存有相应的信息.由于只是返回函数, 并没有执行返回函数内的返回结果, 只有在再次调用时才起效.

~~~python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
f() #>>> 25
~~~

在返回函数返回多个闭包时,注意返回函数不要引用任何循环变量或者后续会变化的变量.

~~~python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
f1();f2();f3(); #>>> 9; 9; 9

### 没有预期结果原因是, 返回的是列表是三个闭包, 这三个闭包的值引用的是i, 而i的值在返回阶段才执行

# 正确写法:
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
f1();f2();f3(); #>>> 1; 4; 9
~~~

-------------------

### 装饰器和符号@ Decorator {#more-decorater}

> 原博文: [Python装饰器和符号@](/2015/10/25/pyDecorator/){: target='_blank'}

在代码运行期间动态增加功能的方式，称之为“装饰器”。装饰器本质是高阶函数, 就是将函数作为参数进行相应运作,最后返回一个闭包代替原有函数. 装饰器本质就是将原函数修饰为一个闭包(一个返回函数).

装饰器在python中在函数/对象方法定义前使用`@`符号调用. 装饰器可以在函数运行前进行一些预处理, 例如检查类型等.

~~~python
@dec1
@dec2(arg1,arg2)
def test(arg):
    pass
~~~

以上代码等于`dec1(dec2(arg1,arg2)(test(arg)))`

#### 简单的装饰器及其运行机制

例如:

~~~python
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2015-10-26'
    return "done"
now()
# 实际调用wrapper()
#>>> call now()
#>>> 2015-10-26
~~~

#### 装饰器运行机制

机制就是,调用now()实际调用log(now)() (前面`@`写法后,实际运行now=log(now)),也就是运行了wrapper(),并把now函数原有参数传递给了wrapper函数. wrapper在运行时,加入了新的处理`print 'call %s():' % func.__name__`一句, 并运行相应传递参数的`func(*args,**kw)`并把原有结果返回.

~~~python
now=log(now) #->now=wrapper
result=now() #->wrapper()
>>>call now() #-> wrapper修饰部分
>>>2015-10-26 #-> 原函数部分执行部分
print result
>>>done #-> 原函数的返回部分
~~~

所以装饰器机制简单地说就是要:

1. 将原来函数通过装饰器变成一个传递函数本身的高阶函数(`@log`部分,`now=log(now)`)
2. 新的高阶函数要返回一个修饰函数,从而使调用原函数时实际调用该部分. (`def wrapper()..return wrapper`部分)
3. 新修饰函数进行相应修饰处理(print语句)后,执行原函数并返回原函数值.

#### 传递参数的装饰器

~~~python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print '2015-10-26'
    return "done"
now()
#>>> excute now()
#>>> 2015-10-26
~~~

装饰器本身可以传入参数.不要小看这个传入参数, 传入的参数因为占据了本身装饰器的参数, 所以需要**新的一层装饰器**来处理原函数. 上述机制:

~~~python
now=log('execute')(now) #-> now=wrapper
#或者可以说f=log('execute')  -> f=decorator
#          f(now) -> decorator(now) -> wrapper
#          now=wrapper
result=now() #wrapper()
~~~

实际`now=log('execute')(now)`两个参数表就是执行了一次闭包decorator(now).执行该闭包后返回的才是真正的装饰器wrapper.

两层闭包的机制可以保证传递参数给内在的装饰器wrapper.第一层将参数传进行生成第一层闭包对应返回函数,第二层则将该参数继续留给真正的装饰器闭包.

#### 继承原有函数信息

在以上装饰器中, 其实质都是`now=wrapper`, 此时我们要是输出`now.__name__`得到的将是装饰器wrapper的名字.可以用`wrapper.__name__=func.__name__` 加在装饰器内部进行原函数信息的继承, 也可以使用`functools.wraps`来实现.

~~~python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
~~~

对于带参数的装饰器, 依然将`@functools.wraps(func)`写在实质装饰器wrapper前面.

其机制:

~~~python
wrapper=functools.wraps(func)(wrapper) 
#将原函数func信息给返回函数f=functools.wraps(func), f 闭包含有相应func信息.
#用f 返回函数来修饰wrapper, 此时实际可以将wrapper的一些信息替换为原函数
~~~

对于很复杂的体系, 需要经常定义一些高阶函数对新函数进行一系列处理, 此时定义装饰器就可以省很多功夫. 但缺点是初学比较难以理解, 要对OOP十分熟悉.

#### 对象方法变对象属性的装饰器@property和@*.setter

该装饰器是python内置的,是类中一个高级用法,作用是将一个**方法名变成一个对象属性**. 类需要继承于**object**相应的类.    
构建相应`@property def prop(self):return self._prop`就可以直接`obj.prop`来将方法变成获取对象属性的调用形式.而相应`@prop.setter def prop(self,value): self._prop=value` 就可以实现`obj.prop=value`将方法转为对象属性的赋值.而且好处还可以在此加入属性的值的检查. *obj._prop*只是相应储存的储存地方,名字也是无限制的.  
不定义setter而只定义property的话,该**属性就是只读的**不能修改的!!

例如:

~~~python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def fail(self):
        return True if (self.score <60) else False
        # (self.score <60) and return True or return False

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，实际转化为s.get_score()
### 60
s.score = 9999
### Traceback (most recent call last):
###   ...
### ValueError: score must between 0 ~ 100!
s.fail
### False
s.fail=True
### Traceback (most recent call last)
### ...
### AttributeError: can't set attribute
~~~


## 类和对象

继承和多态: 支持子类从父类继承, 通过重新定义方法实现多态.

Python中的类不是封闭的，你可以动态的为类添加方法。

~~~python
class Foo:
    pass
def bar(self):
    print "ok"
Foo.bar = bar
Foo().bar()
~~~

如果你想添加的是一个静态方法，可以这样：

~~~python
class Foo:
    pass
@staticmethod
def bar():
    print "ok"
Foo.bar = bar
Foo.bar()
~~~

### 动态类和对象方法:

python动态语言,可以对类/对象直接添加新的属性和方法. 对类进行添加,所有实例都起效, 对某个实例添加, 只能对该实例起效,其余实例不受影响. 注意添加方法需要使用self,因为会传递实例本身.

~~~python
class Student(object):pass
s1=Student();
s2=Student();
s1.hi=10; s1.hi; # 对实例添加新属性
# -> 10
s2.hi;
# -> 'Student' object has no attribute 'hi'
Student.hi=11; # 对类添加新属性
s1.hi; #实例不受新添加类属性影响
#-> 10
s2.hi; # 新属性对另一实例起效
#-> 11

def prints(self):print "Hello!";
def printss():print "Hi!";
s1.printss=printss; 
s1.printss    #-> <function __main__.printss>
s1.printss(); # 其实此时并不是绑定的方法,而只是调用一个函数.
# -> Hi!
s2.printss();
#-> 'Student' object has no attribute 'printss'
Student.printss=printss
s2.printss()
#-> printss() takes no arguments (1 given)
Student.prints=prints;
s2.prints  # 绑定的方法,会传递self
#-> <bound method Student.prints of <__main__.Student object at 0x050D6770>>
s2.prints()
#-> Hello!
~~~

使用MehodType函数可以也将函数绑定为类的方法. 第二个参数为None,第三个参数若为类, 则所有实例都起效; 也可以只绑定某个实例对象(第二个参数为实例,第三个参数为类或不填), 此时其余对象不具有该方法.

~~~python
from types import MethodType
def set_score(self, score):
    self.score = score
s1=Student();s2=Stundet();
s1.MethodType(set_score, s1, Student)
s1.set_score(60),s1.score; #-> 60
s2.set_score(60); #-> AttributeError: 'Student' object has no attribute 'set_age'
Student.set_score = MethodType(set_score, None, Student)
s2.set_score(80);s2.score; #-> 80
~~~
 
### 限制类属性 \_\_slots\_\_:

` __slots__ = ('name', 'age')` 可以限制类属性只能有列出的来的几种. 添加或指定新属性将报错AttributeError.

`__slots__`只对当前类起效, 对子类无效. 若子类也定义了slots, 则子类运行的属性则是父类和子类的slots的合集.

### 对象方法变对象属性的装饰器@property和@*.setter

该装饰器是python内置的,是类中一个高级用法,作用是将一个**方法名变成一个对象属性**. 类需要继承于**object**相应的类.  
构建相应`@property def prop(self):return self._prop`就可以直接`obj.prop`来将方法变成获取对象属性的调用形式.而相应`@prop.setter def prop(self,value): self._prop=value` 就可以实现`obj.prop=value`将方法转为对象属性的赋值.而且好处还可以在此加入属性的值的检查. *obj._prop*只是相应储存的储存地方,名字也是无限制的.  
不定义setter而只定义property的话,该**属性就是只读的**不能修改的!!

例如:

~~~python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def fail(self):
        return True if (self.score <60) else False
        # (self.score <60) and return True or return False

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，实际转化为s.get_score()
### 60
s.score = 9999
### Traceback (most recent call last):
###   ...
### ValueError: score must between 0 ~ 100!
s.fail
### False
s.fail=True
### Traceback (most recent call last)
### ...
### AttributeError: can't set attribute
~~~




> 原博文: [Python:类和对象object](/2015/10/20/pyObject/){: target='_blank'}



### 访问限制 {#mid-class}

python没有真正的办法限制用户访问对象的属性/方法, 只能靠自觉了.以`__`开头的变量(`__var__`特殊变量除外) 不能直接用名字访问; 以`_`开头的变量暗示不要去访问,但不限制直接访问. 以`__`开头的变量其实可以用`_className__var`来访问.

~~~python
class Student(object):
    __init__(self,name,score):
        # can't access directly
        self.__name=name
        # recommend not to access
        self._score=score
    get_name(self):
        return self.__name
    set_name(self,name):
        self.__name=name
s=Student("John",59);
s.__name="Mike"
# -> AttributeError: 'Student' object has no attribute '__name'
s._Student__name="Mike"
# OK!~
~~~

### 继承和多态

python的继承和多态比C++要简单太多..继承就是从父类继承一切, 多态就是重置一些父类也有的属性/方法,使其实现子类的特殊性. 

继承的好处在于可以减少重用代码, 实现更抽象,也是多态的基础.

多态的好处在于有共同的某个方法,可以在传入后根据类的不同/特性来调用相应方法.

~~~python
# 定义父类, 继承于新式类object
class Animal(object):
    def run(self): print "Animal is running"
# 定义子类, 继承于父类
class Dog(Animal):
    # 重载方法, 实现多态
    def run(self): print "Dog is running"
a=Animal()
d=Dog()
# isinstance 判断可以判断出其是否源于某个父类.
isinstance(d,Animal)
# True
isinstance(a,Dog)
# False

# 多态的好处在于有共同的某个方法,可以在传入后根据类的不同/特性来调用相应方法.
def runTwice(animal):
    animal.run()
~~~

Python还可以进行**多重继承**(指定多个父类), 通过多重继承来获得附属的新属性和功能, 这种设计又叫Mixin设计, 在C++/Java中均没有的功能.

多重继承时, 若多个父类中有相同的方法, 则排在前的父类将覆盖后面的,则越靠前越"主类". 即使主类的方法源自父类的父类, 也依然优先.

~~~python
# 定义主线父类, 继承于新式类object
class Animal(object):
    def eat(self): print "Animal can eat"
# 定义Mixin所用的"功能"类
class Flyable(object):
    def fly(self): print "Animal can fly"
class Runnable(object):
    def run(self): print "Animal can run"
# 进行多重继承
class Dog(Animal, Runnable): pass
class Cat(Animal, Runnable): pass
class Bird(Animal, Flyable): pass
~~~

## 新式类(object类)和传统类

Python2.1前,旧式类是唯一可用的类型, 在2.2中引入了新式类, 为了统一class和type的概念.

旧式类中的实例x, `x.__class__`对应的是其类,但`type(x)`永远都是 `<type 'instance'>`. 在新式类中, 一般情况下`x.__class__`和`type(x)`都是统一的(因为私自可以改`__class__`).

旧式类的类型是`<type 'classobj'>`, 而新式类的类型则是`<type 'type'>`, 表面旧式类是源自于classobj,其实例源自于instance. 而新式类的则源于type, 并且其实例源自于对应的类. 引入新式类是为了使用**元类**来构造类对象, 统一类的模型. 一般新式类顶级的类是`object`,一般新式类均源于他. Python 3.x 全是新式类, 不需再继承object了.

新式类的使用有很多好处: 可以继承大部分内建类型, 引入了计算属性功能的descriptor(装饰器或者叫描述符, 如`@property`等), 使用各种特殊方法(如`__str__`,低级别的构造函数`__new__`,`__slots__`限定属性等), 元类的使用, 多重继承的一些问题.

~~~python
class C():pass
class CC(object):pass
c=C();
cc=CC();
type(C)
# <type 'classobj'>
type(CC)
# <type 'type'>
type(c)
# <type 'instance'>
type(cc)
# <class '__main__.CC'>

print C
# __main__.C
print CC
# <class '__main__.CC'>
print c
# <__main__.C instance at 0x1096f4320>
print cc
# <__main__.CC object at 0x1096ed950>

# Python 2.7.10测试. 3.x测试结果可能不同.
dir(c)
# ['__doc__', '__module__']
dir(cc)
# ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

BB=CC
bb=BB();
print bb
# <__main__.CC object at 0x1096eda10>
~~~

以上是经典的查看经典类和新型类(继承自object)信息的代码. 经典类的类叫 **classobj**, 而新式类的类叫 **type**. 经典类对象的类是熟知的**instance**, 而新式类的对象的类则是创建该类的类对象`__main__.CC`. 打印出来的效果也是,新式类才是真的类,其对象也才是真的object对象.

新式类本事其实也是一个对象, 可以用变量接收, 可以作为函数参数传递甚至返回, 可以拷贝, 可以添加新属性, 可以创造对象(类的特性). 例如上述例子用BB接收类,用BB同样可以创造CC类的对象.

### 元类

元类就是类的类,用于创建各种类,一般类的元类是type类. 可以利用type方法来创建新式类(和class关键词效果相当).

细节请参考另一篇[Python:元类metaclass](/2015/10/23/pyMetaClass/).


### 类的特殊属性/方法

请参考另一篇[Python对象的特殊属性和方法](/2015/10/09/pySpecialObjMethod/).

#### 属性

- `__slots__`: 一个元组, 规定了可以设置的属性. 防止动态加载过多的属性.

#### 方法

- `__new__`: 构造函数, 创造类实例时的函数, 一般不修改.

#### 类/对象的相关函数

- `type(obj)`: 获取对象的相应类型.
- `type(className, (parents), {attr:value})`: 创建并返回一个类, 三个参数对于类名(字符串),父类(放在元组内)以及属性(属性/方法名以及对应值)
- `isinstance(obj, type)`: 判断对象是否和指定的type类型相等(type甚至可以是父类).
- `hasattr(obj, attr)`: 判断对象是否具有指定属性/方法
- `getattr(obj, attr[, default])`: 获取属性/方法的值, 如设置default,要是没有该属性则返回缺失值(否则AttributeError). 类似于obj.attr
- `setattr(obj,attr,value)`: 设定该属性/方法的值. 类似于obj.attr=value
- `dir(obj)`: 获取相应对象的**所有**属性和方法名(字符串)的列表.




###### Reference

1. [Python对象的特殊属性和方法](/2015/10/09/pySpecialObjMethod/)
2. [Python Datamodel](https://docs.python.org/2/reference/datamodel.html#special-method-names), 中文版[数据模型](http://python.usyiyi.cn/python_278/reference/datamodel.html)

-------------

## 迭代器 {#iterator}

> 原博文 [Python迭代器和生成器](/2015/09/07/PyIterator/)

### 可迭代对象Iterable

凡是可以用作for循环的都是可迭代对象,包括一般的list,tuple,set,dict,迭代器和生成器(或生成器函数)等.

可迭代对象具有`__iter__`方法返回迭代器. 可迭代对象可以通过`iter(obj)`生成迭代器(本质调用`__iter__`方法). 

可迭代对象本质是数据流,一个接一个的数据,但不一定像迭代器和生成器一样记住迭代到那个点, 下一个是什么, 利用iter()函数可以将list等转变为迭代器(其实是生成器), 逐个元素投出.

可以通过`isinstance(obj, Iterable)` (需要事先`from collections import Iterable`)来判断对象是否可迭代对象.

### 迭代器(Iterator)对象：

凡是可以通过next()方法返回下一个值的可迭代对象就是迭代器. 生成器是一种迭代器.enumurate也是迭代器(本质生成器)

可以通过`isinstance(obj, Iterator)` (需要事先`from collections import Iterable`) 来判断对象是否迭代器.

迭代到没有值了返回`StopIteration`错误.

迭代器拥有`__iter__`方法和`next`方法,有时隐藏掉(如生产器).但本质具备该两种方法.`__iter__`方法返回迭代且对象本身, 而next方法则调用下一个元素. 在自定义迭代器时需要定义该两种方法.for循环本质是通过调用可迭代对象的`__iter__`方法获取迭代器对象,再用next方法遍历元素.

#### 可迭代对象和迭代器的分开自定义

分开定义的好处在于, 当对可迭代对象使用iter()转变时,返回一个新的迭代器对象, 这时不受先前产生的相应迭代器对象影响.

~~~python
class Zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return ZrangeIterator(self.n)

class ZrangeIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()    

            
zrange = Zrange(3)
print zrange is iter(zrange)   
#>>> True  
print [i for i in zrange]
#>>>[1,2,3]
print [i for i in zrange]
#>>>[1,2,3]

# 若不区分可迭代对象和迭代器, 即这里列表生成式中使用ZrangeIterator的话, 
# 第二次调用时迭代器已被迭代完,第二次会为空集.
zzrange=ZrangeIterator(3);
print [i for i in zzrange]
#>>>[1,2,3]
print [i for i in zzrange]
#>>>[]
~~~

### generator生成器对象

生成器通过`生成器函数`产生, 生成器函数可以通过常规的def语句来定义, 不用return而是使用`yield`一次返回一个结果, 返回后停在相应位置, 再次调用时继续执行生成下一个结果, 当生成器结束没有下次执行时, 返回`StopIteration`.

`(x for x in range(10))`该表达式产生的是生成器对象,而非列表.

生成器有`close()`方法,可以关闭生成器. 另有`send(obj)`方法,定义`yield`表达式执行后返回的值. 如`val=yield i`,正常情况下用next返回的值为None,所以`send(None)`和next()等价.也可以另外赋值,从而追踪某些情况.另外注意send第一次使用要在执行过yield以后(即最少一次执行迭代)才能使用,否则没有yield的返回值可以定义就会报错.

~~~python
# 生成器函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #生成器关键一步yield,每次执行到此返回,下次从此开始.
        yield b
        a, b = b, a + b
        n = n + 1
# 通过生成器函数产生生成器对象
g=fib(6);
# 单独调用生成器对象
print g.next();
# 利用循环迭代生成器
for i in g:
    print i
~~~

### list等的迭代器.

将list/dict等转化为迭代器使用`iter(obj)`函数.

`i.next()`方法或`next(i)` 函数遍历迭代器

`enumerate(i)`

#### 通过iter()函数将list/dict等数据组组转为迭代器.

~~~python
# 创建一个列表迭代器(listiterator)
i1 = iter([1, 2, 3])  # iter是Python BIF，用于生成迭代器，文档见底部
type(i1)
<type 'listiterator'>
i1
<listiterator object at 0x1cedf50>

# 创建一个字典项迭代器(dictionary-itemiterator)
d = dict(a = 1, b = 2)
i2 = d.iteritems()  # 生成iterator对象，对于字典来说还有iterkeys, itervalues等方法可用
i2
<dictionary-itemiterator object at 0x1dfe208>
[e for e in d.iteritems()]  # dict.iteritems方法生成的是迭代器元素为键值对形式
[('a', 1), ('b', 2)]

# 另外还有tuple/set等都可使用iter函数返回iterator对象
~~~

#### 步进式访问迭代器中元素

obj.next()

~~~python
i = iter(range[3])
i.next()
0
i.next()
1
next(i)  # next() - python2.6新增BIF，作用同iterator.next()
2
next(i)  # 无元素可迭代时，抛出StopIteration异常，可以通过捕获此异常判断是否迭代完毕
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
~~~

#### 循环访问遍历迭代器：

~~~python
# 手动循环
try:
    while True:
        next(i)  # python2.6之前版本使用iterator.next()方法
except StopIteration:
    print 'Done'

# for循环
>>> i = iter(range(3))
# 以下句法叫做列表解析，这与生成器表达式类似，之后文章介绍生成器时再记
>>> [e for e in i]  # for在这里不断调用next函数，直到捕获StopIteration异常后退出
[0, 1, 2]
~~~

#### 将迭代器传递给其他函数使用：

~~~python
>>> list(iter(range(3)))
[0, 1, 2]
~~~

#### 帮助迭代器实现索引功能：

使用enumerate函数返回一个迭代器对象, 该对象能够生产一个元组包括`(索引,值)`.

`enumerate(iterable, start=0)`

第一参数是可迭代对象包括list/dict/迭代器等, 第二个参数是索引开始的号.

~~~python
>>> i = iter('abc')  # python中字符串也是可迭代对象
>>> [(k, v) for k, v in enumerate(i)]  # enumerate返回一个元素为tuple的iterator，文档见底部
[(0, 'a'), (1, 'b'), (2, 'c')]
~~~

###### Reference
1. iter函数 - [文档](https://docs.python.org/2/library/functions.html#iter)
2. enumerate函数 - [文档](https://docs.python.org/2/library/functions.html#enumerate)
3. [Python迭代器和生成器](http://www.cnblogs.com/wilber2013/p/4652531.html)

------------------

## Python异常处理和debug {#Exception-debug}

这里主要是try...except..else..., try..finally.., raise, assert 的用法.

> 原博文: [Python异常处理](/2015/08/25/PythonException/){: target='_blank'}

异常处理无外乎几件事: 断言(assert)和抛错(raise), 检查(try), 捕获(except), 处理(except,else,finally).  

- 异常即是一个**事件**，该事件会在程序执行过程中发生，影响了程序的正常执行。一般情况下，在Python无法正常处理程序时就会发生一个异常。当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。异常作为事件，不需要在程序里传送结果标志或显式地测试它们。
- 异常是Python**对象**，表示一个错误。异常可以作为类被定义, 也可以人为引发异常.
- 异常可以作为**控制流**, 通过异常情况或人为引发异常, 可以执行代码流控制, 实现比较高级的"goto"效果. 例如在for循环内引发错误,可以跳到外面几层的某个try..except内.

~~~python
# 相关语句
try:
    <statement>        #运行别的代码
except：
    <statement>        #捕获任何在try中引发的异常
except <name>：
    <statement>        #如果在try部份引发了'name'异常
except <name>，<data>:
    <statement>        #如果引发了'name'异常，获得附加的数据
except (<name1>,<name2>...):
    <statement>        #捕获任何列出的错误
else:
    <statement>        #如果没有异常发生
finally:
    <statement>    #退出try时总会执行
raise   #人为引发错误
assert <judgement>  #断言,判断一定要返回True否则会引发AssertionError
~~~

try语句用于检测语句块中的错误,从而让except语句捕获其中的异常信息并处理. finally是无论有错无错都会执行.raise语句可以用于人为制造错误. assert语句是断言条件必为真,否则返回断言异常.

### try语句

try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。try语句有两种模式,try..except..else和try..finally.

#### try..except..else

~~~python
# 最常见的模式 try..except..else模式
try:
    <statement>        #运行别的代码
except <name>：
    <statement>        #如果在try部份引发了'name'异常
else:
    <statement>        #如果没有异常发生
~~~

- 如果当try后的语句执行时发生异常，python就跳回到try并执行**最近匹配**该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
- 如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被**递交到上层的try**，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
- 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。

except语句有几种形式,包括捕获所有异常的`except: `,某个异常的`except ErrorName:`或几种异常`except (Error1,Error2,Error3):`, `except ErrorName,e:`和`except Error as e: `可以将异常传给变量e,收集作为数据进行处理.

#### try..finally

~~~python
# try..finally模式
try:
    <statement>        #运行别的代码
finally:
    <statement>        #不管有无异常都会执行
~~~

try..finally模式是:  

1. 没有异常就先运行try所有语句,再运行finally所有语句. 
2. 要是有异常,try执行到异常就跳到finally,然后直接跳出将异常递交给上层的try.控制流并不通过所有try语句.
3. finally能跟在except/else后,优先先执行except/else再执行finally.

由此可知, try...finally 模式更适合于嵌套在try..except内作为保证某些代码一定执行.因为try..except...else要是执行了except就不会执行else,无法保证某个代码必须执行.所以常见的整合模式为:

~~~python
# 两种模式的嵌套和结合
try:
    <statement1>        #运行测试代码1
    try:
        <statement2>        #运行测试代码2
    finally:
        <statement3>        #不管测试代码2有无异常都会执行
except <name>：
    <statement>        #测试代码1或2发生错误而被捕获,就会执行异常
else:
    <statement>        #测试代码1和2都没有发生错误就会执行
finally:
    <statement4>        #无论两个try有无异常,都会运行一次.
~~~

PS: 要是finally在except/else前面肯定会报错.因为try后直接给finally,然后会交给上层try.但没有上层try...

实例:

~~~python
#!/usr/bin/python

try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print "Going to close the file"
      fh.close()
except IOError:
   print "Error: can't find file or read data"
~~~

### raise语句

raise语句可以很好地用于抛出某个异常从而被try捕获. 更常用于结合if等进行条件检查.例如某变量假定[0,10],<0时抛出一个错,>10抛出另一个错误.

raise一般是`raise exception,args`,args一般采用一个值,来初始化异常类的args属性,也可以直接使用元组来初始化args.

~~~python
raise <name>    #手工地引发异常
raise <name>,<data>    #传递一个附加的数据(一个值或者一个元组),要是不指定参数,则为None.
raise Exception(data)    #和上面等效.
raise [Exception [, args [, traceback]]]  # 第三个参数是用于跟踪异常对象,基本不用.

try:
    if (i>10):
        raise TypeError(i)
    elif (i<0):
        raise ValueError,i
#下面的e实际是返回错误的对象实例.
except TypeError,e:
    print str(e)+" for i is larger than 10!"
except ValueError,e:
    print str(e)+" for i is less than 0!"
else:
    print "i is between 0 and 10~"
~~~


### assert语句

Python的assert是用来检查一个条件，如果它为真，就不做任何事。如果它为假，则会抛出AssertError并且包含错误信息。

`assert expression[,argument]`

表达式部分返回真/假, argument部分一般是引发时传递的标示,一般用于输出,或者进一步用于控制.  

断言一般用于检查条件(像使用if语句再抛错或退出), 而不是用于抛错, 抛错请使用raise. 更多使用技巧参考ref1. 

~~~python
try:
    assert 1 == 0,'one does not equal zero'
except AssertionError,args:
    print '%s:%s' % (args.__class__.__name__,args)
# AssertionError:one does not equal zero 
~~~

### 异常

当一个未捕获的异常发生时，python将结束程序并打印一个堆栈跟踪信息，以及异常名和附加信息。如

~~~python
 Traceback (innermost last):
      File "test.py", line 3, in ?
      a = 1 /0
      ZeroDivisionError: integer division or modulo
~~~

这里异常是ZeroDivisionError, 后面是附加信息.

一般异常类是Except(args), args是一个元组可以接收给予的参数. 字符串化一个异常类就是将这些赋予的参数印出来, 当只有一个参数时,就直接将内容输出,例如上述一些例子在`raise error,string`,`assert exp, string; except AssertionError, e:print e` 都是直接将参数打印出来罢了.如果是多个参数, 就是把元组字符串化. 

异常是一个类. 可以用系统定义的类或者自定义的类.有教程说raise..except可以用字符串作为异常是错误的.会这么说:

~~~python
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    raise "Error1"
TypeError: exceptions must be old-style classes or derived from BaseException, not str
~~~

异常最好直接或间接继承自异常的类, 例如以下:

~~~python
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.argsm = arg
try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.argsm
#经测试,要是args的话,返回的是一个元组
~~~

上面的测试时,要是把argsm变为args,输出是个元组.why? 因为默认的BaseException里的\_\_init\_\_也是使用args属性来储存所有参数,其本质是个元组,当字符串给了这个元组时就分解为字符元组了.

一般地, 自定义异常类就是写好`__init__`就好了, 也可以自定义一些新属性用于输出.但意义不大, 一般错误就是message和args两个主要属性,还有个`__dict__`属性. 方法里有如`__str__`这种字符串化输出的方法.

#### 常见异常

异常名称     |  描述
BaseException    |  所有异常的基类
SystemExit   |  解释器请求退出
KeyboardInterrupt    |  用户中断执行(通常是输入^C)
Exception    |  常规错误的基类
StopIteration    |  迭代器没有更多的值
GeneratorExit    |  生成器(generator)发生异常来通知退出
StandardError    |  所有的内建标准异常的基类
ArithmeticError  |  所有数值计算错误的基类
FloatingPointError   |  浮点计算错误
OverflowError    |  数值运算超出最大限制
ZeroDivisionError    |  除(或取模)零 (所有数据类型)
AssertionError   |  断言语句失败
AttributeError   |  对象没有这个属性
EOFError     |  没有内建输入,到达EOF 标记
EnvironmentError     |  操作系统错误的基类
IOError  |  输入/输出操作失败
OSError  |  操作系统错误
WindowsError     |  系统调用失败
ImportError  |  导入模块/对象失败
LookupError  |  无效数据查询的基类
IndexError   |  序列中没有此索引(index)
KeyError     |  映射中没有这个键
MemoryError  |  内存溢出错误(对于Python 解释器不是致命的)
NameError    |  未声明/初始化对象 (没有属性)
UnboundLocalError    |  访问未初始化的本地变量
ReferenceError   |  弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError     |  一般的运行时错误
NotImplementedError  |  尚未实现的方法
SyntaxError  |  Python 语法错误
IndentationError     |  缩进错误
TabError     |  Tab 和空格混用
SystemError  |  一般的解释器系统错误
TypeError    |  对类型无效的操作
ValueError   |  传入无效的参数
UnicodeError     |  Unicode 相关的错误
UnicodeDecodeError   |  Unicode 解码时的错误
UnicodeEncodeError   |  Unicode 编码时错误
UnicodeTranslateError    |  Unicode 转换时错误
Warning  |  警告的基类
DeprecationWarning   |  关于被弃用的特征的警告
FutureWarning    |  关于构造将来语义会有改变的警告
OverflowWarning  |  旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning    |  关于特性将会被废弃的警告
RuntimeWarning   |  可疑的运行时行为(runtime behavior)的警告
SyntaxWarning    |  可疑的语法的警告
UserWarning  |  用户代码生成的警告

#### Python内建异常体系结构

~~~
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- StopIteration
+-- StandardError
|    +-- BufferError
|    +-- ArithmeticError
|    |    +-- FloatingPointError
|    |    +-- OverflowError
|    |    +-- ZeroDivisionError
|    +-- AssertionError
|    +-- AttributeError
|    +-- EnvironmentError
|    |    +-- IOError
|    |    +-- OSError
|    |         +-- WindowsError (Windows)
|    |         +-- VMSError (VMS)
|    +-- EOFError
|    +-- ImportError
|    +-- LookupError
|    |    +-- IndexError
|    |    +-- KeyError
|    +-- MemoryError
|    +-- NameError
|    |    +-- UnboundLocalError
|    +-- ReferenceError
|    +-- RuntimeError
|    |    +-- NotImplementedError
|    +-- SyntaxError
|    |    +-- IndentationError
|    |         +-- TabError
|    +-- SystemError
|    +-- TypeError
|    +-- ValueError
|         +-- UnicodeError
|              +-- UnicodeDecodeError
|              +-- UnicodeEncodeError
|              +-- UnicodeTranslateError
+-- Warning
+-- DeprecationWarning
+-- PendingDeprecationWarning
+-- RuntimeWarning
+-- SyntaxWarning
+-- UserWarning
+-- FutureWarning
+-- ImportWarning
+-- UnicodeWarning
+-- BytesWarning
~~~

###### Reference

1. [Python中何时使用断言](http://blog.jobbole.com/76285/)

----------

### Python捕获所有异常 {#catch-all-exception}

> 原博文: [Python捕获所有异常](/2015/08/26/CatchAllError/){: target='_blank'}

有关异常的东东可以参考前篇[Python异常处理](http://platinhom.github.io/2015/08/25/PythonException/).

前篇已经提及可以使用`except: statement`来捕获所有异常, 但是你不知道那个是什么异常..但我们很多时候也想知道究竟是啥异常在哪里发生.其实是有方法通抓错误并分析的. 当然, 使用异常处理还是最好使用好针对某种异常的处理啦.推荐记住`except:traceback.print_exc()`

#### 使用traceback模块

回溯模块可以回溯运行记录. `traceback.print_exc()`可以印出最后的异常情况.

~~~python
import traceback
try:
    print b[1]
except:
    traceback.print_exc()
print "hello world"
raw_input()
#输出:
#Traceback (most recent call last):
#  File "C:\Users\Hom\Desktop\test.py", line 17, in <module>
#    print b[1];
#NameError: name 'b' is not defined
#hello world
~~~

还可以使用文件来保存异常信息用于日后分析,例如:

~~~python
import traceback
try:
    print b[1]
except:
    ferr=open("errorlog.txt",'a')
    traceback.print_exc(file=ferr)#实名指定参数
    f.flush()#刷新
    f.close()
raw_input()
~~~


#### 使用sys模块

使用`sys.exc_info()` 方法会返回一个三元元组, 第一个是错误类型, 第二个是错误信息,第三个是回溯对象信息. 信息差不多,但是不如traceback.print_exc()来得干脆.

~~~python
import traceback
try:
    print b[1]
except:
    print sys.exc_info()
print "hello world"
raw_input()
#输出:
#(<type 'exceptions.NameError'>, NameError("name 'b' is not defined",), <traceback object at 0x02582288>)
#hello world
~~~

#### 使用基类:

~~~python
try:
    statement
except Exception,ex:
    print Exception,":",ex
~~~

这里使用了基类Exception来通捕获错误. 其实第一个只是告诉自己是什么类型异常(肯定是*<type 'exceptions.Exception'>*了),意义不大,而后面实例化抓回来的ex就可以储存信息了,究竟是啥错误~ 这种应用基类的方法可以捕获各种错误并且实例化,但是缺点是不知道异常类型, 靠猜.

## 模块

### \_\_future\_\_模块

`__future__`模块用来引入一些新版本的特性, 例如在2.x版本中引入3.x版本的特性.

- `from __future__ import unicode_literals` 引入3.x版本中字符串特性, 使用该语句后,`"str"`就已经是unicode的,而2.x版本中的字符串则要使用`b"str"`来表示.
- `from __future__ import division` 引入3.x中除法特性,3.x中除法默认是精确除法,2.x则是向下取整.例如`10/3`2.x的是3,3.x是3.33333.使用该特性后就会采用3.x的特性, 而原有的除法要使用`10//3`来表示.

# 进阶篇




## help的使用 {#more-help}

> 原博文: [Python帮助及设置](/2015/10/10/pyHelp/){: target='_blank'}

我们知道,`help('obj')`可以查询命名空间存在的模块,类,函数,对象. 在ipython可以用 `obj?` 来查询其信息. 这里主要介绍, 怎么写help时显示的内容.

help是函数,help(内容), 这个内容可以是一个变量, 对象, 或者'函数名', '模块名', '主题'等. 进入后可能很长,按`空格`下页,按`q`退出.

一般内容部分如下(注意是字符串形式,还是直接形式:对象名/变量名):

- 'help': 可以获得一个总体介绍,例如一些词,例如help('modules name')来列出含有该词的模块.不建议使用..
- 'keywords': 可以查询所有keywords列表,例如help('if')可以查询关键词
- 'modules': 可以查询所有可用模块(包括安装的,但不包含当前目录).例如help('os')
- 'topics': 可以查询所有主题, 主题都是大写.例如help('CALL')
- '关键词': 字符串形式(否则会处理为关键词), 可以查询关键词介绍. 包括使用格式, 介绍.如help('lambda')
- '模块名': 没加载的可用模块需要字符串形式,使其可以从关键词库搜索; 加载的模块(如用户模块)可以用直接形式.就是查询模块帮助, 后面介绍.
- '主题名': 查询一些主题,例如调用, 字符串,浮点等.就是说明书了..
- 类名: 如help(str).一句话用法, 介绍, 方法, 数据(属性)描述符, 其余属性, 继承的内容.
- 函数名: 可以查询函数帮助,可用字符串形式. 第一句一般是简介来源,内建,文件等.第二句是格式. 第三句是介绍.
- 变量名: 可以查询变量对象的帮助,类似于类查询,但现实的是对象查询.
- 子内容: 例如模块类的对象, 对象类的方法, 均使用详细调用时的形式,例如help(os.path)

### 模块设置help信息

- NAME: `__name__`: 模块名, 主程序时是`__main__`. 写在模块开头的`'...'`字符串是模块名进一步说明.
- FILE: `__file__`: 默认就是文件绝对路径(包是`__init__`文件).
- DESCRIPTION: `__doc__`: 模块说明部分, 可以写在模块开始的`'''...'''`第一个字符串段(会跳过前面的注释,空行,以及第一个普通的`'...'`名字说明字符串), 也可以用变量赋值形式定义. 
- PACKAGE CONTENTS: 包内的模块名,包会用(package)说明.无介绍.
- SUBMODULES: 子模块?
- CLASSES: 模块内定义的类介绍及其方法,数据和属性. 包括import * 获得的.先展开列出所有class及子类,再是介绍.
- FUNCTIONS: 模块类定义的一般函数. 包括import * 获得的.
- DATA: 定义的模块全局变量.
- AUTHOR,VERSION,DATE等: `__author__`, `__version__`, `__date__`: 作为附加信息使用赋值方式定义,也会列在模块后.显示相应大写字符串. 这些叫metadata, 类似还有copyright, email, status, license, credits(数组,有贡献的人)等.

部分特殊变量是会有显示的, 但也有就是特殊`__`罢了.而`_var`或`_var_`变量会作为private变量/函数而不在help中显示信息, 以帮助简化及保护信息.

### 类设置help信息:

在类的开头定义后写上的第一个字符串段就是类的主要说明,会跳过前面的空行,注释行. `''' ... '''`和`'...'`均可.

"Methods defined here/inherited from ...": 本类内定义的/从母类继承的方法
"Data descriptors inherited from": 本类内定义的/从母类继承的内容描述,例如`__dict__`等特殊内容
"Data and other attributes inherited from": 本类内定义的/从母类继承的属性,是类内定义的变量等.注意不包括函数(包括`__init__`)内

### 函数设置help信息:
在函数定义下面注意缩进的第一个字符串内容(`'''...'''或'..'`)或者注释内容就是其注解.注意是函数def下面!注意缩进!

### 比较dir:

dir能列出模块或对象的方法属性等, 以列表返回. 而help则是列出这些信息以外还有介绍,但不好进一步处理.

-------------


## 元类和类 {#more-metaclass}

> 原博文: [Python:元类metaclass](/2015/10/23/pyMetaClass/){: target='_blank'}

元类就是类的类. 实际上,我们用`class` 关键词创建的类也是一个对象也就是我们常说的类其实也是通过一个底层的类来构建的,这个类就是元类(metaclass).

先看一段代码:

~~~python
class C():pass
class CC(object):pass
c=C();
cc=CC();
type(C)
# <type 'classobj'>
type(CC)
# <type 'type'>
type(c)
# <type 'instance'>
type(cc)
# <class '__main__.CC'>

print C
# __main__.C
print CC
# <class '__main__.CC'>
print c
# <__main__.C instance at 0x1096f4320>
print cc
# <__main__.CC object at 0x1096ed950>

BB=CC
bb=BB();
print bb
# <__main__.CC object at 0x1096eda10>
~~~

以上是经典的查看经典类和新型类(继承自object)信息的代码. 经典类的类叫 **classobj**, 而新式类的类叫 **type**. 经典类对象的类是熟知的**instance**, 而新式类的对象的类则是创建该类的类对象`__main__.CC`. 打印出来的效果也是,新式类才是真的类,其对象也才是真的object对象.

新式类本事其实也是一个对象, 可以用变量接收, 可以作为函数参数传递甚至返回, 可以拷贝, 可以添加新属性, 可以创造对象(类的特性). 例如上述例子用BB接收类,用BB同样可以创造CC类的对象.

新式类的类叫`type`, 这个type就是元类. 可以用元类来创建我们所熟知的新式类. 

### type函数利用元类创建新式类

我们可以使用type函数来获取类型,同样也可以用该函数创造一个类,取决于参数. `type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)`, 例如:

~~~python
CCC=type('CCC',(),{});
ccc=CCC()
print CCC
# <type 'type'>
print ccc
# <__main__.CCC object at 0x1096ed990>
~~~

这里使用type创建一个新式类, (虽然不继承任何类,但实际继承了object, 用一个变量CCC接收, 这个变量实际就是类名, 类似于上面的CC和BB.而实际类对象类型取决于type第一个参数字符串. 如果不加后面的元组和字典, type一个字符串返回的是<type 'str'>. 

例如CCCC继承自CCC并且有个方法fun,属性attr:

~~~python
def fun():pass
CCCC=type('CCCC',(CCC,),{'attr':True,'fun':fun})

class CCCC(CCC):
    self.attr=True
    self.fun=fun
~~~

实际上我们使用class关键词创建新式类时是调用了type函数来实现的.

### \_\_metaclass\_\_类属性

`__metaclass__`属性用于指明该类创建时使用的元类. 如果没有该属性,则使用type来创建. 注意, 这个过程是逐层搜的, 首先搜索该类的定义, 再搜索继承的父类, 要是还找不到就在模块里面找, 模块级别都找不到该属性, 就用type来创建. 例如上述CCCC的class式定义中,首先搜索CCCC类的定义,其次是CCC父类,再是模组(main这里), 最后才是用type. 

决定了`__metaclass__`以后, 则用其来创建一个类对象. 那么, 这个元类怎么创建类对象呢...怎么定义自己的元类呢..

### 自定义元类

首先要明确, 你要修改元类干什么. 修改元类是在创建类对象前进行拦截从而改变其特性的,用于修改类, 并且可以返回类对象. 例如,要把所有属性/方法名变成大写.

#### 使用新函数并将type函数作返回

使用一个新函数, 接受和type一样对应的三个参数. 当进行相应预处理后, 再将**type()函数**将修改内容生成类对象.

该方法简单易记, 缺点是不是oop的, 并且不能使用特殊方法来处理掉该预处理时的问题!

~~~python
# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
'''返回一个类对象，将属性名都转为大写形式'''
# 选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
# 将属性名转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
# 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)
 
__metaclass__ = upper_attr  
#  这会作用到这个模块中的所有类

class Foo(object):
# 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'
print hasattr(Foo, 'bar')
# 输出: False
print hasattr(Foo, 'BAR')
# 输出:True
f = Foo()
print f.BAR
# 输出:'bip'
~~~

#### 使用类的方法构建元类

使用类的方法就是要使用**type作父类**, 再覆盖`__new__`方法并返回相应的type类的`__new__`方法结果.

~~~python
class UpperAttrMetaclass(type):
# 请记住，'type'实际上是一个类，就像'str'和'int'一样, 所以，可以从type继承
    def __new__(self_class, future_class_name, future_class_parents, future_class_attr):
# __new__ 是在__init__之前被调用的特殊方法, 用来创建对象并返回之的方法
# 而__init__只是用来将传入的参数初始化给对象
# __new__()方法接收到的参数依次是：当前准备创建的类的对象; 类的名字; 类继承的父类集合; 类的方法集合。
# 一般很少用到__new__，除非你希望能够控制对象的创建
# 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
# 如果你希望的话，你也可以在__init__中做些事情
# 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
# 复用type.__new__方法, 覆盖原type的创建的方式. 比较OOP
        return type.__new__(self_class, future_class_name, future_class_parents, uppercase_attr)
# 也可以直接用type函数返回..但就和上面的函数方法类似.
        #return type(future_class_name, future_class_parents, uppercase_attr)
# 也可以不作用于type.__new__, 而是使用super函数的结果
        #return super(UpperAttrMetaclass, self_class).__new__(self_class, name, bases, uppercase_attr)
# self_class这里就是一般类的实例的self, 这里是类实例(就是一个类)

class Foo(object):
    __metaclass__=UpperAttrMetaclass #指示使用UpperAttrMetaclass来创建类.
~~~

## 典型应用: 编写ORM框架

ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

~~~python
class Field(object):
    # 负责保存数据库表的字段名和字段类型
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
# 各种类型的field
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')        

# 定义出自定义元类, 用于创建不同表(不同类)
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 基类
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        # ORM设置
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        # 不要把实例属性和类属性使用相同的名字。
        # ModelMetaclass会删除掉User类的所有类属性，目的就是避免造成混淆。
        for k in mappings.iterkeys():
            attrs.pop(k)
        # 将属于列的属性先提到mapping,保存到__mappings__中,其余用于创建类.
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)

# 基类
class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        # __mappings__属性由元类创建,对应于列.
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name) #列名
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 调用接口,使用ORM框架,这里想定义一个User类来操作对应的数据库表User
# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由基类借助元类的处理自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
~~~

##### Reference

1. [深刻理解Python中的元类(metaclass)](http://blog.jobbole.com/21351/)
2. [Python Types and Objects](http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html)

-------------

## Python模块和包加载机制 {#more-module-package}

> 原博文: [Python模块和包](/2015/08/29/pythonModule/){: target='_blank'}

python没有什么头文件cpp文件之分, 每个py文件都可以作为独立的模块module. 我们应该熟知使用 *import os* 一类语句加载标准模块.这里总结下模块,包等更多东东. 和一般的教材不同, 大家熟悉模块, 这里先介绍包, 概念比较简单, 但对后面模块进一步认识有很大意义.

### 包 package

和C++不同,模块加载是不支持路径形式的, 但我们经常要将很多个模块放在一个文件夹内便于管理.此时python就有了包package的概念. 包其实就是放了很多文件的文件夹特殊模块, 其最大作用是便于加载文件夹内的模块: `import package.module`

包的实质也是个模块.当在加载包内的模块时, 包也会被加载到模块列表中, 此时作为模块加载的内容在文件夹内`__init__.py`内. 

`__init__.py` : 当加载包模块时, 初始化包模块. 用途在于说明该文件夹是个package, 不需特殊加载的话可以留空,但作为包的话必须存在该文件.

先谈模块搜索路径, 再谈看似很简单的模块加载. 重点是模块与包的加载机制, 有助于了解import的实质.

### 模块的搜素路径: 

1. 当前目录
2. 环境变量`PYTHONPATH`中指定列表依次搜索
3. python安装目录,子目录(如lib/site-packages,plat-win,lib-tk等),相关目录等

可以使用`sys.path`来查看当前的搜索路径. 如常使用建议使用`PYTHONPATH`环境变量来定义.

在机制中,python会搜索Python Home, 由PYTHONHOME给定或者python.exe所在去找, 找到后将导入lib/site.py, 将site-packages目录及其下的包加入.

### 加载模块

加载模块最常用方法有:

~~~python
import module1,module2
import module as mod
from module import sth
from module import *
~~~

模块就是一个py(pyc,pyd)文件, import时不需要文件后缀. 第一种方法加载整个模块(内容且带命名空间); 第二种方法便于缩写(缩写作为命名空间,但实质还是加载相应模块对象,详细看下面一个例子); 第三者选定性加载内容且不需再带命名空间; 第四种方法加载所有东西且没有命名空间 (四种情况的加载机制都请参考下面import 的机制).

每个模块对象都有`__name__`属性(就是文件名不带后缀或者`__main__`),所以常用`if (__name__ == "__main__")`判断是否作为main主程序.

#### 一个比较健壮的加载代码: 

~~~python
import sys;
if not "/home/a/" in sys.path:
    sys.path.append("/home/a/")
if not 'b' in sys.modules:
    b = __import__('b')
else:
    eval('import b')
    b = eval('reload(b)')
~~~

#### 注意点

- 模块不能带路径,例如在a文件夹内的模块b, 不可以 *import a/b*,这时要用包(见下面).  
- 模块加载的路径储存在`sys.path`中.可以将某个文件夹路径加载到该列表中, 从而实现对文件夹内py文件的加载.
- 已加载的模块储存在`sys.modules`一个字典当中,可以对其进行检查模块是否已加载. 字典项是模块名,字典值是其路径(文件名)或内建模块.
- **一个模块不会重复被载入**.模块若已被加载, 再次加载将无效(除非退出主程序或者退出解析器PVM), 这样可以避免重复加载的发生(其实就是检测字典是否有重值). 此时如模块被修改需重新加载, 要用`reload(modname)`重新加载(注意,会优先加载编译过的pyc文件!). 
- 模块加载时,先检查是否加载了,否的话加载并把名称导入到Local命名空间,而已加载的话则将模块名字加入到正在使用的模块的Local命名空间(可用`locals()`查得,全局是`globals()`). **每个模块的Local命名空间是独立的**. import A 时即使内部进行了import B, B模块也只存在A的命名空间,而不在当前命名空间, 这会导致需要B被加载了,但B的内容不能被调用,要使用还是需要明确import B.见下面实例解释.
- 详细的模块和包的加载机制, 请看完下面的例子.

#### import中再import的Local命名空间问题:

~~~python

# 当前目录:
# now.py 
import pkg.mod1
now = 0
print "In now"

# pkg目录下:(包含空白__init__.py)

# __init__.py
p=-1

# mod1.py
import pkg.mod2
m1=1
print "In mod1"

# mod2.py
m2=2
print "In mod2"

# 以下是交互模式下输入, 输出用->表示

import sys
import now
# -> In mod2 ; In mod1 ; In now
# 可见加载顺序是递归的.

print now.now; 
# -> 0; 
# 需要用命名空间now

print pkg.p; print pkg.mod1.m1; print pkg.mod2.m2
# -> Traceback (most recent call last):
# ->  File "<stdin>", line 1, in <module>
# -> NameError: name 'pkg' is not defined
# pkg的名字存在于now模块中,但不存在当前模块! 更别说子模块了.

sys.modules["now"];
# -> <module 'now' from 'now.py'>
sys.modules["pkg"];
# -> <module 'pkg' from 'pkg/__init__.py'>
sys.modules["pkg.mod1"];
# -> <module 'pkg.mod1' from 'pkg\mod1.py'>
sys.modules["pkg.mod2"];
# -> <module 'pkg.mod2' from 'pkg\mod2.py'>
# 可见四个模块都被加载了,

locals()
# -> {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'now': <module 'now' from 'now.pyc'>, '__name__': '__main__', '__doc__': None}
# 因为只是加载now,所以里面的子内容都没有加载.

import pkg;locals()
# ->{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'now': <module 'now' from 'now.pyc'>, 'pkg': <module 'pkg' from 'pkg\__init__.py'>, '__name__': '__main__', '__doc__': None}
# 新加入了pkg, 但没有子模块.

print pkg.p;print pkg.mod1.m1;print pkg.mod2.m2
# -> -1 ; 1 ; 2
# 第一个很容易理解,因为pkg被加载到locals了. 但mod1和mod2没有啊..? 再做个测试就明白了.

# 退出python, 重头再来
import pkg.mod1
# -> In mod2 ; In mod1

print pkg.p;print pkg.mod1.m1;print pkg.mod2.m2
# -> -1 ; 1 ; 2

locals()
# -> {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'pkg': <module 'pkg' from 'pkg\__init__.pyc'>, '__name__': '__main__', '__doc__': None}

# 由此可见,命名空间中即使我import pkg.mod1, 但命名空间中只有pkg! 也就是说,一旦命名空间加入包名,就可以调用包内已加载的模组内容! 

# 退出python, 重头再来
import sys,pkg.mod2
# -> In mod2

print pkg.p;print pkg.mod2.m2
# -> -1 ; 2
print pkg.mod1.m1;
# -> Traceback (most recent call last):
# ->  File "<stdin>", line 1, in <module>
# -> AttributeError: 'module' object has no attribute 'mod1'
# 虽然pkg被加载到Local,但pkg对象没有mod1属性(模组属性)

sys.modules["pkg.mod2"];
# -> <module 'pkg.mod2' from 'pkg\mod2.pyc'> 变pyc了~
sys.modules["pkg.mod1"]
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# -> KeyError: 'pkg.mod1'
# 原因还是因为该模组mod1没有载入,不存在于pkg模组的__dict__当中.
~~~

#### 以下是import module as mod的测试,用numpy测试

~~~python
import sys
import numpy as np
sys.modules["numpy"]
# -> <module 'numpy' from 'c:\Python27\lib\site-packages\numpy\__init__.pyc'>
sys.modules["np"]
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# -> KeyError: 'np'
# 由此可见, 模组是按原名载入

type(np)
# -> <type 'module'>
type(numpy)
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# -> NameError: name 'numpy' is not defined
# 可见, 命名空间只有np而没有numpy
locals()
# -> {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'np': <module 'numpy' from 'c:\Python27\lib\site-packages\numpy\__init__.pyc'>, '__name__': '__main__', '__doc__': None}
# 结论也是np命名空间存在代替numpy模块

import numpy
locals()
# -> {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'np': <module 'numpy' from 'c:\Python27\lib\site-packages\numpy\__init__.pyc'>, '__name__': '__main__', 'numpy': <module 'numpy' from 'c:\Python27\lib\site-packages\numpy\__init__.pyc'>, '__doc__': None}
# 再次加载numpy后,numpy并没有实际再次加载创建对象, 但命名空间加入了numpy
~~~

### import的机制

先看个测试例子, 明白这个例子和import的机制,就能明白上面的例子了.

#### 测试交叉引用:

~~~python
# A.py
from B import D
class C:pass

# B.py
from A import C
class D: pass

# Test 1
# 运行:
import A
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# ->   File "A.py", line 1, in <module>
# ->     from B import D
# ->   File "B.py", line 1, in <module>
# ->     from A import C
# -> ImportError: cannot import name C

# Test 2
# 外部执行:
python A.py
# -> Traceback (most recent call last):
# ->   File "A.py", line 1, in <module>
# ->     from B import D
# ->   File "c:\Users\Hom\Desktop\B.py", line 1, in <module>
# ->     from A import C
# ->   File "c:\Users\Hom\Desktop\A.py", line 1, in <module>
# ->     from B import D
# -> ImportError: cannot import name D

# Test 3
# 若A.py 中改为import B:
import A
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# ->   File "A.py", line 1, in <module>
# ->     import B
# ->   File "B.py", line 1, in <module>
# ->     from A import C
# -> ImportError: cannot import name C

# Test 4
# 外部执行:
python A.py
# -> 
~~~

上面的例子要了解**import的机制**, 以from B import D为例:

1. 在sys.modules中查找符号"B".
2. 如果符号B存在，则获得符号B对应的module对象<module B>。从<module B>的`__dict__`中获得符号"D"对应的对象，如果"D"不存在，则抛出异常.
3. 如果符号B不存在，则创建一个新的module对象<module B>，注意，这时，module对象的`__dict__`为空。执行B.py中的表达式，填充<module B>的`__dict__` 。从<module B>的`__dict__`中获得"D"对应的对象，如果"D"不存在，则抛出异常。

而当import B时:

1. 在sys.modules中查找符号"B"
2. 如果符号B存在，则不再重复加载, 并把B (或者as name)加到命名空间(要是不存在于命名空间).要是as name方式加载,创建新名字映射到B模块对象(所以例子中numpy和np都是指向同一个numpy模块对象)
3. 如果符号B不存在，则创建一个新的module对象<module B>, 并执行B.py表达式, 将产生的子对象/变量等填充<module B>的`__dict__` . 并且和上面情况一样, 创建相应的命名空间并映射到模块对象. 完成后退出.

- 所以执行 *python A.py* 时: 
    1. A.py的from B import D, 创建B模块,并执行B.py来填`__dict__`(此时为空)
    2. B.py的from A import C. 此时从命令行执行,A.py是主程序, 并没有A模块.所以创建A模块,并执行A.py来填`__dict__`(此时为空)
    3. A.py的from B import D, 此时B模块已存在,所以根据上述机制2中所述,不创建B模块了而是从B中`__dict__`中调用D.此时字典为空,不存在D.所以抛错.如Test 2中错误无D的存在.
- 要是执行 *import A* 时:
    1. 创建模组A,执行A.py填空的`__dict__`
    2. B.py的from A import C. 此时已经存在模组A, 所以直接从`__dict__`中加载, 因为为空, 所以报错没有C.如Test 1所示.
- 要是A.py修改为 *import B* , 执行 *import A*, 效果和上面一样,A缺C, Test 3的情况
- 当执行 *python A.py* : 
    1. A.py的import B, 创建B模块,并执行B.py来填`__dict__`(此时为空)
    2. B.py的from A import C, 创建A模块,并执行A.py来填`__dict__`(此时为空)
    3. A.py的import B, B模块已存在, 完成.因为没有再加载D, 所以不报错.此时A和B模块实际仍是空的.

以上示例很好地说明了import的机制.一定要清楚!!!

当测试1 import再import的命名空间时,可以知道**包的import机制**: 

- 不管 *import pkg* 还是 *import pkg.mod1*, 第一步,先import pkg, 执行`__init__.py`内容, 创建命名空间及对应的包模块的对象, 在modules中加载模块.
- 如果*import pkg* 且`__init__.py` 不加载子模块,实际pkg这个包模块对象的`__dict__`是空的, 没有子对象.
- 要是执行*import pkg.mod1*,检测存在pkg模块后则继续执行import子模块pkg.mod1,此时, 不创建命名空间, 但创建对象, **对象绑定到pkg的`__dict__`中**. 在modules中也会加载模块pkg.mod1 来确认已加载避免重复加载

所以, 实际上包模块的加载方式是创建一个整体的pkg模块对象, 再加载子模块到pkg模块对象的`__dict__`中.只要子模块被加载并且母包存在于命名空间,则可被调用.

### 一个实际例子: Pymol 1.7.2.1

当我尝试help('modules')时,报错:

~~~
In [1]: help('modules')

Please wait a moment while I gather a list of all available modules...

/usr/local/lib/python2.7/site-packages/IPython/kernel/__init__.py:13: ShimWarning: The `IPython.kernel` package has been deprecated. You should import from ipykernel or jupyter_client instead.
  "You should import from ipykernel or jupyter_client instead.", ShimWarning)
Error: unable to initalize the pymol.cmd module
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/site-packages/pymol/cmd.py", line 117, in <module>
    from chempy import io
ImportError: cannot import name io
An exception has occurred, use %tb to see the full traceback.

SystemExit: 0
~~~

进一步追踪%tb.

~~~
site-packages/chempy/fragments/__init__.py:
      2 import chempy
----> 3 from chempy import io

chempy/io.py:
---> 21 from chempy.mol import MOL

chempy/mol.py:
---> 19     from pymol import CmdException

pymol/__init__.pyc:
--> 454     from pymol import cmd

pymol/cmd.pyc:
--> 328         sys.exit(0)
~~~

单独import pymol/chempy 均没有问题,但单独运行from chempy import io就报错. 因此局部模块很可能是交叉引用的问题, 

首先在fragments里先import chempy,再chempy.io,此时加载该模块,但里面dict为空,而后面pymol.cmd 又再次加载chempy.io 所以不存在就报错了. 解决办法在cmd.py前面from chempy import io, 前加入import pymol,chempy


----------------------


### 对象的特殊属性和方法 {#more-special-methodprop}

Python一切皆对象(object)，每个对象都可能有多个属性(attribute)。Python的属性有一套统一的管理方案。
 
对象的属性可能来自于其类定义，叫做类属性(class attribute)。
类属性可能来自类定义自身，也可能根据类定义继承来的。
一个对象的属性还可能是该对象实例定义的，叫做对象属性(object attribute)。
对象的属性储存在对象的`__dict__`属性中。
`__dict__`为一个词典，键为属性名，对应的值为属性本身。

#### 属性

- `__doc__`: 帮助说明, 将字符串写在对象定义声明之下.
- `__module__`: 模组名,就是文件的名字(无后缀)部分
- `__class__`: 返回对象的类信息
- `__dict__`: 储存对象属性/方法的字典.
- `__slots__`: 设置一个元组,限定允许绑定的属性名称(不能动态添加以外的属性). 只能对当前类起效, 对子类不起效(除非在子类中也定义`__slots__`，这样，子类允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。)

#### 方法

- `__init__(self, args)`: 对象初始化时执行的函数
- `__getattr__(self,attr)`:在调用获取对象属性执行,只查询在不在`__dict__`中的属性(相当于先在`__dict__`中查找,找不到再用本函数). 如果调用是对象方法, 处理时返回值是函数才OK.
- `__setattr__(self,attr,value)`:在对对象属性赋值时执行
- `__delattr__(self,attr)`:在删除属性时执行 `del obj.attr`.
- `__getattribute__(self,name)`: 在调用获取对象**任意**属性时执行,和getattr比,任意属性都会调用,相当于在`__dict__`查找前执行.
- `__str__(self)`: 在str()时执行相应功能
- `__repr__(self)`: 是输出和打印出来显示的内容.有时可以和`__repr__=__str__`解决
- `__len__(self)`: len()函数时返回长度的行为
- `__iter__(self)`: 作为可迭代对象时返回迭代器本身(或转为迭代器).
- `__call__(self)`: 将实例变得可调用 `obj()`.还可以定义参数.具备该方法,可以用`callable(var)`来判断一个变量是对象还是一个函数(可调用对象).
- `__lt/le/eq/ne/gt/ge__(self,other)`: 二元比较符时调用,对应于`<,<=,==,!=/<>,>,>=`,相当于self<other. 优先于`__cmp__`
- `__getitem__(self,var)`: 可以使用`obj[n]`方式获取值,例如Fib函数可以取其中一项.如果使用list的切片功能,就要判断var是否`slice`对象`isinstance(var,slice)`.slice有start, stop, step属性,负数处理要另外处理..
- `__setitem__(self,var,value)`: 可以用来对值进行赋值时的操作.
- `__delitem__(self,var)`: 删除某个元素的操作.
- `__iadd__(self, val)`: a+=b
- `__and__(self, val)` : a&b 

模组有:

`__name__`: 模组名


判断对象是否有指定属性:

1. `hasattr(obj,attr)`: 返回真假(通过getattr异常与否来实现)
2. `dir(obj)`: 列出对象现有属性
3. 通过`try: obj.attr; except AttributeError: pass`

###### Reference

1. [特殊方法](https://docs.python.org/2/reference/datamodel.html#special-method-names)

--------------

# 语句+表达式+基础类型方法+内建函数

## 常见表达式（xyz代表数字，abc代表字符,ABC代表序列）就是一种表达，返回值作为输入
- x               整型,整形输入，表达返回int或long
- x.           浮点型,只要后面带点，都处理为返回浮点型float
- a+bj 复数            复数类型(ab均是float,0+1j)，*.real, *.img, *.conjugate 分别代表实部虚步和共轭复数（方法）。 
- ‘abc’,“abc”，'''abc''',r'\n' 字符串 string str类型
- u‘foo'                  unicode字符序列
- 0xAF                            16进制输入，返回int
- 0AA                    8进制输入，返回int
- 0b111             2进制输入, 返回int
- xL                        长整型输入，返回长整形（大于(2^31)-1或小于(-2^31)会自动处理为长整）
- xj                         虚数表达
- None                  空值，注意首字大写
- “abc”                 或’abc’，8位ASCII字符，注意里面有’”时要用不同符号或转义。实为序列。
- ‘ab’+’de’           拼接字符串，对于直接的方法，还可以没有加号（不推荐）
- ‘ab’*3                重复字符串。=’ababab’。3处可被替换
- \`ab\`                     =rept(“ab”)
- ‘’’abc’’’              长字符串，可以enter换行不需\来结尾，’和”可以不需转义（但注意转义依然起效）
- r’abc’                 原始字符串，输入的照样作为字符串处理。但输入时依然受制于’/’，但实际的值不受转义影响。
- u’abc’                 16位unicode字符串，3.0后用unicode。
- [a,b,c]                列表
- (a,b,c)                元组，单元素时(a,)也可以a,。
- {a:b}                   字典，整对称项，前者为键后者为值。d[‘a’]代表该对应键,可进行赋值,in,删除等
- A[x]                     索引。序列A第x+1个元素（因为0为第一个）x若为负数，则从倒数起。
- OK[A,B,C]                   序列作为元素构成新的序列。尤其注意检验元素in语法时。
- a[b][c]                字典a中键b是字典，c是b的一个键。字典中的字典。
- A[x:y]                 分片。序列A第x+1到第y个（y+1作为尾部）元素，不指xy为第一和末尾。y大于序列长则为末端。
- A[x:y:z]              z为步长。z>0,x>y;z<0,x<y。[::2]表示从头到尾步长2遍历。[8:3:-1]表示第9到第5个。
- A+B                    序列相加。A或B可以以[x,y,z]表示。字符串不可与序列相加，加实质将B元素接于A后。
- A*3                     序列乘法，重复序列，注意是后接而非元素重复。
- x//y                    整除运算(只取整数部分)
- x%y                    取余运算
- x\*\*y                   乘方运算（优先于取反，需显式说明。如(-3)**2）=pow（x,y）
- x==y                   相等性测试
- x!=y                    不等于，返回真假
- x>y                      类似<,>=,<=，比较大小操作，返回真假
- 0<x<10              多重判断，返回真假
- a is b                  a和b同一性运算符。对于字符数值元组等不可变值,和==一致;但不可变型值如列表,和地址有关。
- a is not b           a和b不是同一个对象
- a in A                  成员资格，返回True或False,布尔运算符。
- a not in A          非成员检查，返回真假
- ‘\n’,’\t’               换行，制表符
- ‘a%s’ % b          格式化字符串，将b代替%s还可以往前加参数。
- '%10.2f' % float 格式化字符串,用变量来格式化成float,10长度,2位小数
- ‘%(key)s’ %d    格式化字符串，将字典d的key键的值代替%s。
- False                  假:False,None,0,””,(),[],{}都是假，即0、空序列、字典、空值和标准假值都算假，其余一切都真。
- not exp              非的表达。表达是判断条件时就反结果；是普通表达时就当做布尔型输入not ‘a’ False
- exp1 and exp2          且的表达,会短路要是exp1是假则跳出假。若exp1假输出exp1真则输出exp2
- exp1 or exp2             或的表达,会短路要是exp1是真则跳出真。若exp1假输出exp2真则输出exp1
- a if b else c       三元运算符，b真则输出a，假则输出c
- [exp for A if]     列表推导式,利用for的特性根据列表A生成元素为exp结果的新列表.用if部分可以筛选A的元素. 例如[x\*x for x in range(10) if x%3==0]x在0-9中当x整除3时输出seq[a]=x\*x的列表[0,9,36,81]
- set (seq)      构建一个集合，内无重复元素。​

## 常见语句，就是操作，包括赋值判断循环执行等
- a=1: a[1]=2: 赋值,变量或列表元素
- a,b,c=1,2,3: 序列解包，就是把元组解包赋值
- x=y=’abc’: 链式赋值，相当于y=’abc’，x=y
- x`+=`1;a\*=2: 就是x=x+1，a=a\*2.增量赋值 python不支持 *a++* 语法
- C=A[:]: 将A所有元素赋给C，即重新构造和A一样的C. 是复制对象.
- A[x:y]=[w:z]: 分片赋值。A[x:x]表示插入,A[x:y]=[]表删除。可以实现任意替换插入删除。
- print ‘A’+’B’,’C’: 显示A和B直接连接，然后空格再C。
- del a,b,c: 删除对象，但不会自动放内存..
- import 模块名: 调用模块
- import module as abc: 调用模块并用abc的名字调用
- from 模块 import 函数: 调用模块中的函数，免除模块.函数的输入。一般使用import更好。
- from \_\_future\_\_ import division: 调用新特性的除法，不会产生1/2=0的取整.
- from module import *: 调用所有模组中的函数，可能会覆盖。
- from mod import func as abc: 调用某个函数并用abc的名字调用。
 ​
- A=[‘a1’,’a2’,’a3’,’a4’]: 
- if a in A: print ‘go!’: If选择判断
- else:行为: If的另一个跳出
- elif 判断语句:行为: 多重选择的判断，用于多选。
- if…: …if… : …: 嵌套代码块，用于多条件判断
- assert 条件: 一旦不满足该条件，程序就崩溃推出。条件后可以,’abc’来解释断言
- while judge: do: while循环,为使动起来需要内加自变值语句。
- while True/[if] break: 除了某个条件break出去，一直循环。
- for i in seq:do: 对满足seq资格的进行循环,迭代器自变,seq可以是序列字典(key).结合range函数。
- for:if:break /else: 循环到一定条件则跳出，否则结束循环后执行else子句
- for i in iterable:do: 用迭代器来做循环，如iglob,enumerate等生产的对象
- for index,i in enumerate(obj[,start]):do: 枚举对象产生的是(0,seq[0])的值,索引在前,可指明起始值
- del obj: 删除对象，可以是变量，序列，序列元素，字典的项
- pass: 无操作占位符，用于填补语法空代码。一般结合注释使用。
- break: 提早完成跳出，尤其用于while True等,只挑出当前一轮循环。
- continue: 使当前迭代结束，跳到下一轮循环。用于跳过后面有繁琐循环体。即是break掉这轮循环
- str % values: 字符串格式化，values可以是字符数字或者元组。
- exec “action”: action就是普通的语句，将执行语句中的行为。命名空间行为。
- scope={}\exec’action’ in scope: 命名空间,就是创立一个含有内建函数的空间,使exec的行为在这个空间中执行,而不影响真实外部。关键是exec in {}表达。同样适用于: eval.内含’\_\_builtins\_\_’项: 
- assert 条件,promt: 断言语句，不符合条件的则弹出AssertionError:promt的错误。

~~~python
class name:
    def __init__ (self,a): #初始化类,a为要填入的形参。
    	pass; 
    def func(self,a):
    	self.arg=var #定义类的方法,后面一句可帮类建立arg属性(属性！)
# 特殊变量
__doc__ 在开头的一段话,可以紧接print来打印和显示
__name__ 当前文件名字
__main__ 主函数
~~~

注意！
字典是没有顺序的！
若x=y=’abc’，改变y对x不影响（同理数值,元组）;但x=y=[1,2,3],通过改变列表的方法改变x，y的值也受影响，因为指向同一个列表，同理对于字典也是。若xy本来指向同一列表，x又被重新赋值，x和y就不等同了。若使其不指向同一地址而是赋值，使用x=y[:]表达。同一性检测x is y对于这个问题很重要。


------------

## 内建函数和对象方法 {#buildin-list}

> 原博文: [Python:内建函数与对象方法](/2015/10/19/pyBuildInMethod/){: target='_blank'}

包括内建函数, 内建对象(字符串,列表,字典,set,文件对象)的方法

内建的东东放在`__buildin__`模块当中.

### 内建函数 (在\_\_buildin\_\_模块)
- float(object): 转换为浮点数
- int(object,base=10): 转换为整数，带小数时向下取整运算. 字符串时指定base可指定传入字符的进制,默认10.
- long(object): 转换为长整形数
- str(object): 转换为字符串(1000L->1000)
- repr(object): 返回值为适合机读的字符串形式(1000L->1000L)
- ord(‘char’): 将某单字符转成字母顺序值（单字符包括\n等）
- chr(num): 将字母顺序值转为某单字符（0~255）
- unichr(num): 将字母顺序值转为某unicode单字符（0~65535）
- bin(num): 将整数转为'0b1011'形式2进制字符串
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

### 复数方法

- C.real: 实数部分
- C.imag: 虚数部分

### 列表方法

- A.append（对象）: 列表末追加新对象（一次一个，对象可为列表）
- A.count(obj): 统计列表某元素出现次数
- A.extend(B): 在列表A后追加另一序列B的值,B可以是任意iterable对象
- A.index(obj[,start,stop]): 索引,返回第一个匹配obj的元素在列表中索引号n（第n+1个）.start和stop可以限制搜索区间.找不到会报ValueError.
- A.insert(index,obj): 插入，在索引号处插入对象。
- A.pop(index): 移除索引号的元素,返回该元素的值。()时移除最后一个,出栈.唯一修改列表还能返回值。
- A.sort(): 排序，默认按升序。可添加参数cmp、key、reverse。cmp可以自定义的函数,返回负数时, 按此时顺序排序，详见脚本例子
- A.remove(obj): 移除列表内某个指定元素，不返回任何值。找不到会报ValueError.
- A.reverse(): 反向列表A，不返回值。

### 元组方法

- T.count(obj): 统计元组某元素出现次数
- T.index(obj[,start,stop]): 索引,返回第一个匹配obj的元素在元组中索引号n（第n+1个）.start和stop可以限制搜索区间.找不到会报ValueError.

### 字典方法
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

### 集合方法
- set.add(element)    集合添加一个元素
- set.update(seq)    集合添加多项
- set.remove(element)    移除集合一个元素
- t\|s 并集 t&s 交集 t-s 差集 t^s交集的补集(只出现t或s中，不能都有)

### 字符串方法

因为字符串是不可序列, 所以大部分方法并不能改变字符串的值，而只起到返回作用.

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

### 文件方法和属性  help(file)
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


## Reference

1. [Python简明教程](http://woodpecker.org.cn/abyteofpython_cn/chinese/)
2. [Pyhon2官方手册](https://docs.python.org/2/)
2. [Python标准库](https://docs.python.org/2/library/index.html), [汉化版](http://python.usyiyi.cn/python_278/reference/)
4. [Python中文手册](http://www.pythondoc.com/pythontutorial27/index.html)
5. [深入 Python :Dive Into Python 中文版](http://woodpecker.org.cn/diveintopython/toc/index.html)
6. [官方内建函数](https://docs.python.org/2/library/functions.html)
7. [廖雪峰的Python教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

### 内链博客:

- [Python基础](/2015/08/31/python_basic/), [Python中级篇](/2015/10/21/pyMedium/), [内建函数与对象方法](/2015/10/19/pyBuildInMethod/), [帮助及设置](/2015/10/10/pyHelp/), [Python标准库小结](/2015/09/12/PythonSTL/),[模块和包](/2015/08/29/pythonModule/), [传递参数](/2015/08/07/PyArgsInput/)
- [Python:类和对象object](/2015/10/20/pyObject/), [对象的特殊属性和方法](/2015/10/09/pySpecialObjMethod/), [Python:元类metaclass](/2015/10/23/pyMetaClass/), [Python装饰器和符号@](/2015/10/25/pyDecorator/), 
- [python字符串相关](/2015/06/23/python-string/), [字符串格式化](/2015/09/13/PyStringFormat/),[字符串编码](/2015/10/17/PyEncode/)
- [迭代器和生成器](/2015/09/07/PyIterator/), [Python垃圾回收](/2015/10/22/pyGarbageCollection/), [Python多线程和多进程](/2015/10/26/pyMultiThread/)
- [异常处理](/2015/08/25/PythonException/),[捕获所有异常](/2015/08/26/CatchAllError/)
- [调用命令行](/2015/09/10/pythonComdline/), [读取命令行参数](/2015/06/13/ReadArgv/), [分析命令行模块optparse](/2015/10/04/PyOptParse/), [getopt模块](/2015/10/03/getopt/)
- [系统信息:platform模块](/2015/10/06/platformPy/)
- [正则表达式](/2015/06/10/regexp-re/)
- [numpy使用](/2015/09/15/numpy-use/)

------
