---
layout: post
title: Python:BeautifulSoup强大的HTML页面解析
date: 2016-01-08 19:13:27
categories: Coding
tags: Python
---

## 安装和加载:

`pip install beautifulsoup4`

安装后模块名是bs4, 版本较新.

`pip install BeautifulSoup`

安装后模块名是BeautifulSoup, 版本较老.

一般首先先加载bs4, 再考虑BeautifulSoup. 为了兼容, 可以:

~~~python
# Import BeautifulSoup -- try 4 first, fall back to older
try:
    from bs4 import BeautifulSoup
except ImportError:
    try:
        from BeautifulSoup import BeautifulSoup
    except ImportError:
        print('It need BeautifulSoup, sorry...')
        sys.exit(1)
~~~

## 使用

更多细节可以参考[官方文档](http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

#### 创建一个HTML的soup顶层对象:

- BeautifulSoup(string) : 使用html内容创建
- BeautifulSoup(fileobj) : 使用html文件对象创建

可以指定解析器来解析html, 默认是python的html.parser, 还可以使用lxml, html5lib, 差异[参考](http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id49).

模块内含对象包括:  Tag , NavigableString , BeautifulSoup , Comment.

### Tag对象 : 就是像html内tag一样, 主要被操作的对象.

#### 属性

- name : 该tag元素的名字, 对应顶层的soup对象是'[document]'
- attrs : 最重要属性, 返回该tag所有属性的字典, 包括class, id, name, style, href等. 属性可以用`obj['attr']`来调用,修改,增加(就是字典嘛). 多值属性返回的可以是list(如class多个).
- string : tag内内容, 相当于innerHtml
- parent : 上级的tag对象.
- 

#### 方法:

- `find`(name=None, attrs={}, recursive=True, text=None, **kwargs): 例如(name="div", attrs={"class":"abc"}) 可以找到第一个符合的子元素. 可以直接使用`属性名=值`来简化attrs的指定. 如果只给一个参数, 就是tag对象name的匹配.
- `findAll`(name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs): 同样的有find_all方法.
- `prettify`(encoding=None, formatter='minimal') : 就是将内容变成好看的带缩进的输出格式, 一般配合print使用.
- `get_text`(separator=u'', strip=False, types=(<class 'bs4.element.NavigableString'>, <class 'bs4.element.CData'>))) : 获取所有子字符串, 并串联起来. 可以指定串联时使用的separator. 

------
