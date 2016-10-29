---
layout: post
title: Python字符串格式化
date: 2015-09-13 07:40:06
categories: Coding
tags: Python
archive: true
---

在许多编程语言中都包含有格式化字符串的功能，比如C和Fortran语言中的格式化输入输出。Python中内置有对字符串进行格式化的操作%。

## 模板

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

## 格式符

格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:

- `%s`    字符串 (采用str()的显示)
- `%r`    字符串 (采用repr()的显示)
- `%c`    单个字符
- `%b`    二进制整数
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

## 更复杂的控制

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

## format函数和字符串format方法

这是另一种处理方法格式化方法: 通过函数/方法. 例如下面的例子:

要将一个列表(float型)的内容格式化并空格分隔写到文件中,一行怎么写?

`f.write( ' '.join(map((lambda v: format(v, '<8.5f')),list))`{: .language-python} 或 `f.write(' '.join([ "%-8.5f" % i for i in lll]))`{: .language-python}

两者结果是一致的. 用lambda函数的好处是, 可以定义一个新函数来方便统一处理一系列的格式, 当需要修改时只修改一处即可. 而`%`方法则要把每处的格式化式改写一遍. 

另外, 试试:

`print "%-"+str(var)+".5f" % i`{: .language-python}, 你会发现报错: *not all arguments converted during string formatting*, 原因是该格式化字符串需要一个完成的串, 格式化串分析在字符串合并前进行,因此错了. 但`format(i, "<"+str(var)+".5f")`{: .language-python} 是可行的

### format函数

format(value[, format_spec]), 后面是格式表达式, 默认是"", 即不格式化直接字符串化. 很基础简单的函数.

和`%`格式化式类似, 支持上面提及的`[flags][width].[precision]typecode` 格式化表达式. 但注意:

1. format函数不需要`%`或后面提到的`:`
2. format函数左中右对齐分别使用`<^>`
3. 其余0填充, "0<6.3f"这些表达是一样的.
4. 只能对单一个元素进行操作, 不支持别名`(name)`,不支持字典, 列表等.

### 字符串的format方法

str.format(*args, **kwargs), 支持多种方式的格式化, 在Python2.6后引入. 和之前两种方法不同, 主要使用`{}`和`:`进行格式化,前者指定位置, 后者相当于`%`.

#### 映射式格式化

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

#### 格式限定符

首先将格式化限定式写在`{}`内, `:`作为格式化标识开始. 同样支持 `[flags][width].[precision]typecode` 格式化表达式, 其中左中右对齐和format函数一样, 使用`<^>`.

~~~python
':_<8.4f'.format(6.4)
#6.4000__
~~~


## 总结

Python中内置的`%` 操作符可用于格式化字符串操作，控制字符串的呈现格式。Python中还有其他的格式化字符串的方式，但%操作符的使用是最方便的。

format函数提供函数化的格式化办法, 而字符串的format方法则提供更丰富的操作方式.

> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#format-string-symbol)中, 不再更新.

------
