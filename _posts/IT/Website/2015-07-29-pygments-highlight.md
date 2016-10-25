---
layout: post_py
title: Pygments语法高亮
date: 2015-07-28 16:52:13
categories: IT
tags: Website Git
---

这段时间都没有找什么新东西折腾, 今天才开始正式写回些东东. 因为写关于Excel的代码,但是Prism并不支持...而在Github中居然是支持VB的!!因此pygments可能会支持VB高亮.一查,果然支持vb.net..好吧..

## 本地安装pygments

1. 使用PIP安装: 直接敲`pip install Pygments`,稍等即可.
2. 使用python安装: 去[pypi-pygments](https://pypi.python.org/pypi/Pygments)下载zip源文件.解压后去源码文件夹执行`sudo python setup.py install` 安装即可(先保证有python哦亲)

## Jekyll/Github使用Pygments
和Prism要使用JS来解析语句不同,jekyll/Github自带的pygments解析器就可以进行解析, 所以不需要另外的JS,只需要设好css样式即可. 

- 启用Pygments: **_config.yml** 中设置 `pygments: true`. 有别的说法说需要`highlighter: pygments` 貌似默认就是,不用设置.
- 使用Pygments标记代码块: `\{\% highlight python \%\} 代码块 \{\% endhighlight \%\}` (将`\`去掉). python指明是代码块语言, 代码块支持语言名可以参考[语法分析器lexers](http://pygments.org/docs/lexers)的**short name**部分(或者使用首页的着色功能时选择语言名就可以知道应该对应用那个词).另外简单地看支持的语言可以看[Languages](http://pygments.org/languages/)部分,但语言名字不一定符合shortname要求.
- 要是想使用行号,可以在语言种类后加入linenos `highlight python linenos` 来加入行号.
- 在jekyll中,因为liquid模板具有优先权,优先于markdown,所以可以使用{highligh} 的方法来插入语法块,此时就不会像过往使用` ~~~ `时需要另开结构块!(即是,不用隔行就可以连接直接使用!)
- 生成CSS: 使用命令: `pygmentize -S default -f html > your/path/pygments.css` 来生成相应的CSS.-f指明formatter, -S指明style. style有多种,可以python进入交互命令后输入:`from pygments.styles import STYLE_MAP;STYLE_MAP.keys()` 来查看返回的style样式. 包括: *['monokai', 'manni', 'rrt', 'perldoc', 'borland', 'colorful', 'default', 'murphy', 'vs', 'trac', 'tango', 'fruity', 'autumn', 'bw', 'emacs', 'vim', 'pastie', 'friendly', 'native']*多种, 也可以去[demo](http://pygments.org/demo/2329807/?style=monokai)中右侧选style测试效果. 后续相应地,在你的layout或者博客文档加入相应的css就可以了,如`<link rel="stylesheet" href="/css/pygments.css">`
- 更多使用和细节参考[docs](http://pygments.org/docs/)部分,包括语法解析器lexer,过滤器Filter,格式化器formatter, 样式style等等. 因为pygment不仅仅是支持html的!

PS: [Ref3](http://zdan.me/post/2015/04/20/use-github-pages-as-blog.html)中需要安装pygments.rb并配置一步我并没测试. 此时并不能使用常规的```` ``` 或 ~~~ ````来进行语法块着色. 可能通过此步启动fenced code blocks就会有点效果.

更有兴趣的话还可以去研究另一种着色方案[Google Code Prettify](https://code.google.com/p/google-code-prettify/).

### 例子:

单纯使用:
{% highlight visualbasic %}
Sub test()
For Each cell In Range("A2:A6")
cell.Offset(0, 1) = cell.Hyperlinks(1).Address
Next
End Sub
{% endhighlight %}

带行号:
{% highlight visualbasic linenos %}
Sub test()
For Each cell In Range("A2:A6")
cell.Offset(0, 1) = cell.Hyperlinks(1).Address
Next
End Sub
{% endhighlight %}


PS:
使用上述方法构造出来的代码是`<div class="highlight"><pre><code class="language-vb.net" data-lang="vb.net">` 样式的,关键字部分是用**\<span class="p"\>**这样标记的. 和普通的fenced代码块相比,多了div部分.因此可以使用该方法区分css. pre 控制整个代码块的显示效果,而code[class=]部分控制了代码行的效果.所以添加以下两端可以将底色强行设为黑色,因此加入到相应pygments-css中即可(因为代码颜色由span控制,因此可以忽略其余影响,但字体和大小依然受原css控制).  
另外,linenos加入的行号可能没有样式,此时可以自己加入`.lineno`的样式.我将相应的以下代码加入pygments.css中后,就可以将prism的样式同时使用了!

~~~css
<style>
div[class="highlight"] > pre > code[class*="language-"] {
	background:black;
}
div[class="highlight"] > pre {
	background:black;
}
.lineno {color: #f8f8f2 } /*Number of line*/
</style>
~~~

附[拾色器](http://www.runoob.com/tags/html-colorpicker.html)(可以利用mac的自带拾色器在demo中确认颜色(10进制),然后[转换一下](http://tool.httpcn.com/Tool/JinZhiZhuanHuan.html?t1_10=238&t1_16=&t2_16=&t2_10=&t3_10=&t3_2=&t4_2=&t4_10=&t5_10=&t5_64=&t6_64=&t6_10=&s7nx=2&t7_x=&s7ny=2&t7_y=&page_url=http%3A%2F%2Ftool.httpcn.com%2FTool%2FJinZhiZhuanHuan.html&word=)).

## Reference
1. [Pygments官网](http://pygments.org/)
2. [pypi-pygments](https://pypi.python.org/pypi/Pygments)
3. [ZDAN博客:搭建GP](http://zdan.me/post/2015/04/20/use-github-pages-as-blog.html)
4. [Jekyll-模板](http://jekyllcn.com/docs/templates/)
5. [Jekyll-配置](http://jekyllcn.com/docs/configuration/)

> Update: [Github升级Jekyll3.0](/2016/02/04/update-github-rouge.html), 默认不再是Pygments, 需要另行安装Pygments; 另外Github不再支持Pygments只支持Rouge.. 

------
