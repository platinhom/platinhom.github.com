---
layout: post_small
title: kramdown和markdown较大的差异比较
date: 2015-11-06 05:18:07
categories: IT
tags: IDE
---

kramdown是markdown的超集,在Jekyll中支持, 可以用于Github搭建博客. 和Jekyll一样, 使用Ruby作为核心语言. 由于Maruku不再更新, Github推荐使用kramdown作为markdown解析. kramdown作为markdown解析器号称速度快, 比[PHP markdown](https://michelf.ca/projects/php-markdown/)和[Maruku](http://maruku.rubyforge.org/)都要快几倍.

kramdown有很多一般markdown所没有的语法特点, 包括和[GFM](https://help.github.com/articles/github-flavored-markdown/)也有差异.另外也可以很方便地作为文件转换使用. 这里只讨论其markdown重要特色, 不考察其作为解析器的用法.

## 基本常识

Block-level元素就是显示HTML上的各个主成分,如段落, [Un]Order List等. Span-level元素就是成分的修饰,如强调, 粗体, 连接等. 对于一些block元素, 需要前面有空行(这和传统markdown不同), 例如header(`## header`), list, fenced code block, math code.  

## 新增功能

### header ID {#headerID}

就是实现html的锚anchor的功能. 例如[回到header ID](#headerID). `## Header {#ID}`. 对于setext style(标题名,下行`===`或`---`)或atx style(就是常用的`#`标题模式)

~~~markdown
##### Header1 {#ID1}

#### Header2 #### {#ID2}

Header3 {#ID3}
-----

[GoH1](#ID1), [GoH2](#ID2), [GoH3](#ID3)
~~~

效果:

##### Header1 {#ID1}

#### Header2 #### {#ID2}

Header3 {#ID3}
-----

[GoH1](#ID1), [GoH2](#ID2), [GoH3](#ID3)

### Footnote脚注

就是链接到footnote  html元素的超链接,形式像参考文献一样. `[^text]`是其形式, text可以是数字或字符串, 但统一显示是1,2,3...(有序列表形式尾注). 尾注内容部分可以是任意元素内容,出现在文章任意地方. 像参考文献一样, 一个显示上标形式标记`[^text]`定义, 一个使用具体内容解释,使用`[^text]: content`定义(注意空格或者换行缩进). 如果没有对应就不会显示. 

~~~markdown
This is some text.[^1]. Other text.[^footnote]. Not exist: [^noexist]

[^1]: Some *crazy* footnote definition.

[^footnote]:
    > Blockquotes can be in a footnote.

        as well as code blocks

    or, naturally, simple paragraphs

[^another]: Another test.
~~~

This is some text.[^1]. Other text.[^footnote]. Not exist: [^noexist]

[^1]: Some *crazy* footnote definition.

[^footnote]:
    > Blockquotes can be in a footnote.

        as well as code blocks

    or, naturally, simple paragraphs

[^another]: Another test.

### 链接

支持链接title(停留会显示), 在链接后空格再加`"titlename"`.  支持自动链接,链接地址用`<link address>`即可.

另外, 可以支持将链接在别的地方定义:`[linkname]: link`, 而原来则变为`[showname][linkname]`, 如果显示名字和定义链接名字一致,可以直接`[linkname]`

~~~markdown
[link](http://kramdown.gettalong.org "hp")

Information can be found on the <http://example.com> homepage.
You can also mail me: <me.example@example.com>

A [link][kramdown hp]
to the homepage.

A link to the [kramdown hp].

[kramdown hp]: http://kramdown.gettalong.org "hp"
~~~

[link](http://kramdown.gettalong.org "hp")

Information can be found on the <http://example.com> homepage.
You can also mail me: <me.example@example.com>

A [link][kramdown hp]
to the homepage.

A link to the [kramdown hp].

[kramdown hp]: http://kramdown.gettalong.org "hp"

### Abbreviations 缩略语

就是html的abbr. 鼠标移到相关词上面会出现词义解析. 在文档任意位置`*[word]: explanation` 即可.

~~~markdown
Move to HTML please.

*[HTML]: Hyper Text Markup Language
~~~

Move to HTML please.

*[HTML]: Hyper Text Markup Language

### Definition Lists 定义列表

就是html的dl, dt, dd. 意义不太大..

~~~markdown
kramdown
: A Markdown-superset converter
~~~

kramdown
: A Markdown-superset converter

### Inline Attribute Lists (IAL) 行内属性标记

IAL就是允许对block元素甚至span元素增加HTML的属性,例如class, name, id, 颜色等.用法简单,在block/span元素**后**跟`{:property=value}`即可, 对于id可以直接`{: #id}`,对于class直接`{: .classname}`. 甚至像css一样先定义一个简称`{:shortcut: p1=v1 p2=v2}`. 多个相同属性时或者合并(如class),或者覆盖(一般属性,后者覆盖前者.) 

对于block元素,这种IAL属性修饰可以在其前,也可以在其后, 可以有多个, 甚至有空格, 直到空行为止.对于span级元素,则必须紧跟其后(同行)并且不能有空格,支持多个IAL紧跟.

~~~markdown
paragraph1
{: .c1 #idp1 .c2 title="title"}

{:refdef: .c1 #idp2 .c2 title="title"}
paragraph2
{: refdef}

This *is*{:.underline} some `code`{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.

This is a Ruby code fragment `x = Class.new`{:.language-ruby}

HTML code as:

<p class="c1 c2" id="idp1" title="title">paragraph1</p>

<p class="c1 c2" id="idp2" title="title">paragraph2</p>

<p>This <em class="underline">is</em> some <code id="id" class="class">code</code>.
A <a href="test.html" rel="something">link</a> and some <strong class="tools">tools</strong>.</p>
~~~

paragraph1
{: .c1 #idp1 .c2 title="title"}

{:refdef: .c1 #idp2 .c2 title="title"}
paragraph2
{: refdef}

This *is*{:.underline} some `code`{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.

This is a Ruby code fragment `x = Class.new`{:.language-ruby}

### Table 表格

表格在很多Markdown扩展中均有, 包括GFM. 使用`|`分隔每列, 第一和最后一个`|`可以省略. 支持对齐(header分隔时`|--:|`冒号位置), 支持多tbody(再次出现`|----|`, 中间分隔列可以用`+`,为了好看..)支持尾注(`====`).

~~~markdown
|-----------------+------------+-----------------+----------------|
| Default aligned |Left aligned| Center aligned  | Right aligned  |
|-----------------|:-----------|:---------------:|---------------:|
| First body part |Second cell | Third cell      | fourth cell    |
| Second line     |foo         | **strong**      | baz            |
| Third line      |quux        | baz             | bar            |
|-----------------+------------+-----------------+----------------|
| Second body     |            |                 |                |
| 2 line          |            |                 |                |
|=================+============+=================+================|
| Footer row      |            |                 |                |
|-----------------+------------+-----------------+----------------|
~~~

|-----------------+------------+-----------------+----------------|
| Default aligned |Left aligned| Center aligned  | Right aligned  |
|-----------------|:-----------|:---------------:|---------------:|
| First body part |Second cell | Third cell      | fourth cell    |
| Second line     |foo         | **strong**      | baz            |
| Third line      |quux        | baz             | bar            |
|-----------------+------------+-----------------+----------------|
| Second body     |            |                 |                |
| 2 line          |            |                 |                |
|=================+============+=================+================|
| Footer row      |            |                 |                |
|-----------------+------------+-----------------+----------------|

### Math code block

kramdown支持直接将latex公式展示. 使用`$$ ... $$`即可. 可支持block(`$$`行开头直到某行`$$`结尾)或span级别(行内). 在使用时`|`最好使用`\vert`代替, 避免歧义为表格. 如果一个代码上下都空行会被作block处理但又想要inline效果, 可转义第一个符号`\$$...$$`

~~~markdown
$$
\begin{align*}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{align*}
$$

This is inline $$\sum_{i=1}^n x_ie_i$$

The following is a math block:

$$\sum_{i=1}^n x_ie_i$$

But next comes a paragraph with an inline math statement:

\$$\sum_{i=1}^n x_ie_i$$
~~~

$$
\begin{align*}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{align*}
$$

This is inline $$\sum_{i=1}^n x_ie_i$$

The following is a math block:

$$\sum_{i=1}^n x_ie_i$$

But next comes a paragraph with an inline math statement:

\$$\sum_{i=1}^n x_ie_i$$

### End-of-block标记
用以标记一个block元素的终结, 用在特殊情况空行有歧义时使用.很少用到. 就是在一空行第一个字符用`^`. 

~~~markdown
连续list项

* list item one
* list item two

被分割list项

* list item one

* list item two

EOB的list项

* list item one
^
* list item two
~~~

看HTML代码就明白什么回事了:

~~~html
<p>连续list项</p>

<ul>
  <li>list item one</li>
  <li>list item two</li>
</ul>

<p>被分割list项</p>

<ul>
  <li>
    <p>list item one</p>
  </li>
  <li>
    <p>list item two</p>
  </li>
</ul>

<p>EOB的list项</p>

<ul>
  <li>list item one</li>
</ul>
<ul>
  <li>list item two</li>
</ul>
~~~

效果: 

连续list项

* list item one
* list item two

被分割list项

* list item one

* list item two

EOB的list项

* list item one
^
* list item two

### Extension

kramdown另外的一些扩展功能, 例如网页注释, 不进行markdown处理, kramdown设置. 格式就是将对于block元素用`{::comment}..{:/comment}`包起来, 对于options(kramdown设置,全局设置,不对应任何元素)是`{::options key="val" /}`. comment就是该部分是网页注释不会被显示, nomarkdown就是该部分不进行markdown翻译处理. options是kramdown 选项设置. 例如`{::options auto_ids="false" /}`就是关闭kramdown自动产生headID的.

~~~markdown
{::comment}
This text is completely ignored by kramdown - a comment in the text.
{:/comment}

Do you see {::comment}this text{:/comment}?
{::comment}some other comment{:/}

{::nomarkdown}
## not a markdown part
{:/nomarkdown}

{::options key="val" /}
~~~

{::comment}
This text is completely ignored by kramdown - a comment in the text.
{:/comment}

Do you see {::comment}this text{:/comment}?
{::comment}some other comment{:/}

{::nomarkdown}
## not a markdown part
{:/nomarkdown}

## 差异

### 代码围栏

一般markdown使用```` ```code``` ````作代码围栏, 但kramdown使用``` ~~~ code ~~~```. 这个要注意转换.

~~~~markdown
```python
#normal markdown fenced code block
```

~~~python
#kramdown code fenced code block
~~~

~~~
#kramdown code fenced code block
#Using IAL to mark the code language
~~~
{: .language-python}
~~~~

效果:

```python
#normal markdown fenced code block
```

~~~python
#kramdown code fenced code block
~~~

~~~
#kramdown code fenced code block
#Using IAL to mark the code language
~~~
{: .language-python}


## Reference

1. [kramdown-Github](https://github.com/gettalong/kramdown)
2. [Kramdown主页](http://kramdown.gettalong.org/)
3. [Kramdown-语法](http://kramdown.gettalong.org/syntax.html), [部分翻译版](https://github.com/flyaway1217/flyaway1217.github.com/blob/master/_drafts/Kramdown-Syntax.md#标题)

------
