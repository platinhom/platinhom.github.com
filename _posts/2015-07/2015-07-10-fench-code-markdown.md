---
layout: post
title: Markdown中的代码块
date: 2015-07-09 18:27:52
categories: IT
tags: IDE Git
---

Code block in markdown
-----

Markdown应该不陌生了,代码块不就是简单的`~~~ ~~~`或```` ```  ``` ````嘛...其实我也很希望就那么简单...

- 1\. 行内代码块`` `..` ``  
这个应该比较简单就是很简单的在行内用两个斜点.例如:  
这里是行内代码`print "hello world"`.  
也可以使用HTML代码`<code></code>`来实现,例如:  
这也是行内代码块<code>print "```...```"</code>.  
这是行内代码块中的代码块<code>print "`...`"</code>. (kramdown不支持嘛,github有显示).  

~~~markdown
这里是行内代码`print "hello world"`.
这也是行内代码块<code>print "```...```"</code>
这是行内代码块中的代码块<code>print "`...`"</code>. 
~~~

- 2\. 标准代码块  
标准代码块表示使用空格/tab来开头的块状代码块,而不是```` ``` ~~~ ````.  
^
    Here comes some code

    This text belongs to the same code block.


~~~
~~~
	Here are some code with tab at start.  

    Here are some code with 4 blank.

~~~
~~~

以下是上面那三团代码块的原markdown代码(GH显示继续三团╮(╯▽╰)╭):

~~~~markdown
~~~
~~~
	Here are some code with tab at start.  

    Here are some code with 4 blank.
    
~~~
~~~
~~~~

- 3\. fenced代码块  
就是使用<code>```...```, ~~~ ... ~~~</code>包围的代码块, 其中\`\`\`的方式前面可能没有显示(例如github).fenced块好处是可以标记是那种语言,从而对其语法着色.  
kramdown支持超过三个的`~`优先于三个的,因此可以在语句块内防止误解.一下是kramdown效果(5,4,3个`~`).而github虽然支持`~`,但是会分成三个语句块..kramdown不支持\`\`\`来做fenced代码块.

~~~~~bash
~~~~
~~~bash
echo I'm coding..
~~~
~~~~
~~~~~

另外, kramdown还支持在下面用`{: .language-markdown}`这样去标识代码种类用于着色.下面这段话github和很多markdown解析器会解析不了.Github默认会解析为一个title和一段引用..引用中还带一段代码 ╮(╯▽╰)╭.

~~~~
~~~
## I'm title

> I'm blockquote
~~~
{: .language-markdown}
~~~~
{: .language-markdown}

## Reference

1. [这篇博文的Github显示](https://github.com/platinhom/platinhom.github.com/blob/master/_posts/2015-07-10-fench-code-markdown.md)
2. [这篇博文的Kramdown博文显示](http://platinhom.github.io/2015/07/10/fench-code-markdown/)
3. [官方kramdown语法](http://kramdown.gettalong.org/syntax.html#code-blocks)

------
