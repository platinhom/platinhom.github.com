---
layout: post_small
title: Python基础篇
date: 2015-08-31 12:51:01
categories: Coding
tags: Python
archive: true
---

基础篇介绍简单的语法, 变量类型, 判断循环, 函数和对象的简介.

# 基础语法

- 关键词列表:

and   |  as  |  assert  |  break  |  class  | continue  | def |  del  | elif   |  else |  except |
exec  |   finally  |   for  |   from   |  global  |  if  |  import  |  in  |   is   | lambda  |  not  |  
or  |  pass  |  print | raise |  return |  try | while |  with |  yield |

## 内建类型,变量

### 几种内建类型:

- 数值型
	- int: 普通整型, [-2147483648,2147483647],支持8进制`055`,16进制`0xff`表达
	- long: 长整型,可以无限..如1000000000000L
	- float: 浮点型, 都是双精浮点,支持科学计数法. 如1.0, 1. , 1.0e-10
	- complex: 复数型, 实际是两个双精度浮点. 1+2j, 
	- bool: 逻辑型, True , False (分别相当于1,0)
- 序列型(Sequence),集合,字典
	- list: 列表型(可变序列型)
	- tuple: 元组型(不可变序列型)
	- set: 可变集合型,另有不可变集合型frozenset.
	- dict: 字典型
	- str: 字符串型(不可变序列型),
	- unicode: 字符串型(不可变序列型),
	- bytearray: 字节数组(可变序列型),
- 常见重要基础类型
	- file: 文件型,通过句柄进行操作.
	- 函数: 自定义如function类, 内建 builtin\_function\_or\_method, 对象方法 method_descriptor或function
	- 对象: object等
	- 模块module: 包括模块和包 
	- iterator: 迭代器类型
	- Exception和Error: 异常和错误
- 特殊类型
	- NoneType: `None`, 缺值.bool可以转为False,str转为str,int不能转.
	- NotImplementedType: NotImplemented, 未执行, 出现在数字处理方法.bool后成True. 少见
	- ellipsis: Ellipsis, 用于表明存在"..."语法.bool后成True. 少见

### 变量: 

- 弱类型的,赋值时根据内容自动定义类型.
- 变量名可以字母数字和\_组成,开头字母或\_
- python没有常量, 没有机制保证其不被改变.一般常量用大写作名字, 自己不去操作他就行了.


## 列表,元组,字符串,bytearray,字典,set,

### 序列sequence
- 索引 index: `seq[i]` 可以获取元素,索引号从0开始, 最高索引是`len(seq)-1`.
- 分片 slicing: `[i:j]`: 所有索引k: i<=k<j的元素的列表, `[:j]`:0到j-1元素,`[i:]`:i到最后一个元素, `[i:j,k]`k可以控制采样步长,若k为负数,先将列表倒序再采样.
- 长度: `len(seq)` 可以获得元素总数.
- 成员检查: `data in seq` 返回对错.
- 负数索引: -1代表最后一个元素的索引,注意a[:-1] 则不包括最后一个(最后一个即终止).
- **不可变序列**:tuple, string, unicode. 和可变序列相比, 缺少了元素赋值能力和del能力,一旦定义,就不能修改元素. 但如果元素是可变序列,其内容依然可以被修改, 例如: a=[1,2];b=(a,);改变a的元素,b也会改变.但b[0]=c则不行.
- 不可变序列可进行哈希化hashable,而可变序列则不可以.

具体类型:

- 列表**list**: 
	- [element1,element2...]
	- 元素可以是任何对象, 大小可随时修改. 可变序列.
	- 分隔符`,`,一个元素时[a]来定义.无元素[].
	- 方法: append(v),insert(i,v), pop([i])等.
	- list()
- 元组**tuple**: 
	- (element1,element2...)
	- 元素可以是任何对象, 定以后不能修改, 不可变序列.
	- 分隔符`,`,一个元素时(a,)来定义(防止括号歧义).无元素().
	- tuple()
- 字符串型**str**: 
	- "string"或'string' (等价), `'''.......'''`字符串块,包含整段字符串,包括其中的换行等.常用于大段文字说明.可以前面加r.
	- 支持转义`\`, 当特殊符号如`', ", \`可以通过转义来表达.
	- `r"string"`: 字符串不进行转义(转义符失效).
	- 字符串型是不可变序列.因此不能随意对字符串的变量替换其内容,如用索引/分片赋值.
	- python没有字符型char,直接用单字符串代替.字符大小最少是8-bit一字节.  
	- str(), chr(), ord()
- unicode型**unicode**: 
	- u"string"或unicode(string)
	- unicode型是不可变序列.
	- 字符大小是16-bit或32-bit,取决于编译时参数.在sys.maxunicode可查询.
	- unicode(), unichr(), ord(), u.encode()
- 字节数组型**bytearray**:
	- bytearray(seq) 或 bytearray(string)
	- 可变序列
	- 储存字节的对应数值. 

### 字典dict

- `{key: value, ....}`或`dict[key]=value`
- 无序, key键和value对应值组成每项
- key需要可以被哈希化,因此不能是可变型对象如字典,set(frozenset可以),可变序列等.
- value可以是任何东东..包括字典,列表等.
- 方法: get(k[,v]), pop(k)

### 集合set

- 无序, 元素唯一的对象.
- 对于数值, 不论类型, 会进行数值比较.如1.0和1归为一项
- 不支持索引, 只能用于in检索,长度len操作,迭代等.
- 去除重复元素后, 有利于快速成员检查in, 种类数的确定.
- 支持: `t|s` 并集; `t&s` 交集; `t-s` 差集; `t^s` 交集的补集(只出现t或s中，不能都有)
- 两种类型: set()构成的可变集合(set型)和frozenset()构成的不可变集合(frozenset型).frozenset型可用于哈希化从而进一步作为一个元素或者作为字典的键.

### 表达式和语句

- 注释: python只有单句注释, 使用`#` 作为注释符.
- 表达式就是运算式子,包括数学运算, 比较运算, 逻辑运算, 变量表达等.
- 语句就是执行一句命令, 告知计算机操作, 一般造成相应变化, 例如赋值语句, 执行函数命令等. 往往表达式是语句的一个成分(宾语主语), 仍需要一个动作(动词).
- 表达式, 语句, 函数, 对象, 变量均是**大小写敏感**的.
- 表达式结果取决于复杂类型的成分的类型,例如 *10/3* 返回结果依然是int: 3, 而 *10.0/3* 则是float: 3.333
- 空语句: `pass`,可以在需要语句块的地方填充以防止语法错误,实际不进行任何操作. 
- 语句块就是一系列语句的集合,例如if/for等后面跟随相应语句块进行操作. python的语句块利用**缩进**(indent)来描述语句块, 同一缩进层次的作为一个语句块. 缩进没有限定,可以tab, 可以N个空格.一般使用四空格或一个tab. 注意tab和空格不能混用.

#### 运算和判断表达式

- `and` 与运算, 会短路(执行第一个否就不执行第二个).
- `or` 或运算,会短路(执行第一个是就不执行第二个).
- `not` 非运算, 跟在前面.
- `==` 相等判断. 值判断, 不包括类型.
- `!=`或`<>` 不等判断

## 判断和循环

### if...elif...else...判断语句

~~~python
if [condition]:
	statement
elif [condition]:
	statement
else:
	statement
~~~

### for 循环

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

形式太简单..一般用于不定次数循环. 这里的while还支持else子句.

~~~python
while condition:
	statement;
[else:]
	[statement;]
~~~

### break,continue

break打断整个循环跳出, continue跳过该次循环后面的部分.

## 输入输出和文件

- `print` 语句(2.\*, 3.\*使用print函数): print obj/expression. `,`会化作空格,但可以字符串和数值一起输出, `+`可以连接字符串,但是数值要先str()转化. 表达式会进行计算后再输出.
- `raw_input([promt])`: 获取输入,返回输入的字符串.promt是提示语句,不换行.
- `input([prompt])`: 获取输入并运算后转化为相应值的字符串返回.相当于: eval(raw_input(prompt)).
- 获取一个字符串, input需要输入"abc",而raw_input只要abc. input后输入1+2, 返回数值3.
- raw_input常也用于卡住脚本不让其终止.
- 文件对象使用handle=open(filename,action)来打开并进行相应操作.和一般的文件对象类似.

## 函数

~~~python
def funcname([argv1,argv2..]): 
	contents;  
	return [vars]
~~~

- 定义函数,也可以不加形参argv,return定义返回内容(无值返回None)
- 返回值可以是多个值return x,y (本质以元组返回). 接收时 x,y=F()即可.
- 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”.
- 函数形参的默认参数最好是不变对象,更多请参考[传递参数](/2015/08/07/PyArgsInput/).
- **\*args**表示任何多个无名参数，它是一个tuple；**\*\*kwargs**表示关键字参数，它是一个 dict(实参时用**变量名=值**)。并且同时使用\*args和\*\*kwargs时，必须\*args参数列要在\*\*kwargs前。若此时给的是list或tuple,可直接在实参前面加`*`.如func(\*list1); 也可以给实参字典前加`**`,如func(**kw)。

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

## 迭代器

迭代器和生成器, 参考[迭代器](/2015/09/07/PyIterator/)

## 异常和debug

try...except..else..., try..finally.., raise, assert 的用法. 参考[异常处理](/2015/08/25/PythonException/)以及[捕获所有异常](/2015/08/26/CatchAllError/)

## 模块

## 常见表达式（xyz代表数字，abc代表字符,ABC代表序列）就是一种表达，返回值作为输入
- x               整型,整形输入，表达返回int或long
- x.           浮点型,只要后面带点，都处理为返回浮点型float
- a+bj 复数            复数类型(ab均是float,0+1j)，*.real, *.img, *.conjugate 分别代表实部虚步和共轭复数（方法）。 
- ‘abc’,“abc”，'''abc''',r'\n' 字符串 string str类型
- u‘foo'                  unicode字符序列
- 0xAF                            16进制输入，返回int
- 0AA                    8进制输入，返回int
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
- scope={}\exec’action’ in scope: 命名空间,就是创立一个含有内建函数的空间,使exec的行为在这个空间中执行,而不影响真实外部。关键是exec in {}表达。同样适用于: eval.内含’__builtins__’项: 
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

​

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

- `#! /usr/bin/env python` 首行, 或者`#! /usr/bin/python2`, 再`chmod +x *.py`就可以使脚本在unix基础系统上能直接执行.(如果是window编写的可能出现最后换行符问题不识别,此时先`dos2unix *.py`就好了)
- 第二行 `# -*- coding: utf8 -*-` 指明字符集，用utf8就可以支持中文了！
- 不懂按help(xx), 已加载对象模块内建内容可以直接用名字,否则要用字符串形式"xx".
- 避免window下运行完程序关闭窗口，可写入：raw_input(‘press <enter>’) 一句
- 好习惯在开头几行加入 #Filename: abc.py作注释该文件名.
- int('6.000000000000000000e+00')报错,float('6.000000000000000000e+00')则可以
- 注意机读形式和人读形式区别：例如长数10000，但机读为10000L；字符人读abc，机读为’abc’，print时是用人读形式，而repr则是可把人读形式转化为机读形式，并把结果保存为人读形式。因为变量必须非数字起头，所以机器默认abc为变量，’abc’为字符串输入，故repr(‘hello’)实际就是’hello’,没有意义。
- 关于换行输入，例如abc想把bc放在输入的第二行便于观察，按enter换行会变确定而出错，因此需要把enter键的值转义为换行.因此行末的\为转义换行，而真需要`\`时需要输入`\\`. 不能最后\’ 因为会转义。
- r’abc\n’就是abc\n，但r’let\’s go’必须转义，否则语法错误，这样进行r处理后输出let\’s go。同理若r’c:\’会因转义了’报错，而r’c:\\’ 则会输出c:\\。
- 字符串是特殊的序列，但是列表不可以和字符串合并相加。另外，用in检测成员资格时，[‘abc’,’def’,’ghi’]必须对应abc才能true，bcd则false。但是对于字符串’abcdefg’，只要包含相同'bcd'都true。而且seqA in seqB也需要A作为子元素才行。
- (序列)变量不能以数字开头，只能含字母数字或下划线。区分大小写。
- 单元素分片是值，但是多于一个元素就是序列了。
- 字符串格式化：str %转换标志(-+空格0)最小字段宽.精度值或* 最后跟转换类型。-为左对齐，+为数值要加+-号，空白为正数前空格，0为转换值不足最小字段宽补0。精度值为最大字符数，*的话需要后面赋值。转换类型常用d/i正数f浮点s字符串r机读字符串C单字符x/X大或小写16进制。可以用元组来格式化, 列表不行!字典格式化%(key) % {key:val}
- 空字典可以随意用赋值添加项，而列表不行。x=[],x[42]=’go’出错
- 关于输出print时，用，表示空格连接，下一行可再用print进行连接，可避免换行；用\换行，下一行的内容紧接上一行，即相当于+换行；+则表示直接字符串连接；用；表示另一个逻辑行。需另外有语句。
- 在keyword的关键词声明中如def,if,elif等，需要用:引出其实质内容块，并进行缩进。在def语句中，如果在IDLE shell中进行定义，结束时enter后在退出该块后，再按一下enter结束；在return后，则会自动退出块缩进。
- 在对序列进行for in时，尽量不要对该序列进行删增，排序等操作，易错！最好先用一个替代序列seq2=seq1[:]来赋值进行操作。
​- 关于py和pyw区别在于,后者使用pythonw.exe来运行,没有了控制台(如dos).
- `if __name__ == '__main__': main()`  该句常用,因为限制其为脚本而非模块.
- pyc文件是编译好的模块文件,可以加速运行.可以用py_compile.complie(file)来编译
- 关于import: 需要在系统路径中含有该路径,可以设置PYTHONPATH 的环境变量来永久添加. 暂时性增加,一般在发布程序时,因为不能改系统变量,所以,这时最好把模块放在同目录或附近目录下,此时,添加搜索路径方法:
- import sys;sys.path.append('..')或sys.path.insert(0,'..')(后者可以优先化). 也可修改..为.或任意目录.
- 定义包:在某目录dira下建`__init__.py` 可以为空,然后将相应的a.py,b.py放进去 然后import dira.a就可以了
- 读取环境变量 filename = os.environ.get('PYTHONSTARTUP')
- 判断文件存在: `if filename and os.path.isfile(filename):execfile(filename)`


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

> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#basic_gramma)中, 不再更新.

------
