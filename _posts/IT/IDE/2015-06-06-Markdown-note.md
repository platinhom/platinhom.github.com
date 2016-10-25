---
layout: post
title: Markdown 笔记
categories: IT
tags: IDE
archive: true
---

﻿扩展名使用md/markdown，在为知当中使用md后缀命名笔记即可识别为markdown.

[英文维基](http://en.wikipedia.org/wiki/Markdown); [中文维基](http://zh.wikipedia.org/wiki/Markdown); [中文教程](http://wowubuntu.com/markdown/)
编辑器可参考: [知乎: 用Markdown 写作用什么文本编辑器？](http://www.zhihu.com/question/19637157)
Window 下软件: [MarkDownPad](http://markdownpad.com/), 
Mac 下软件: [Mou](http://25.io/mou/), ByWord
Online 软件: [Cmd Markdown](https://www.zybuluo.com/mdeditor), [StackEdit](https://stackedit.io/), [Raysnote](https://raysnote.com/). 
Chrome: [Markdown here](https://chrome.google.com/webstore/detail/markdown-here/elifhakcjgalahccnjkneoccemfahfoa), 

--- 


### 以下是一般的规则:
1. **特殊符号**：`#_` \` 等， 要在行头等特殊位置表达，可用转义符` \`， 一般符号后最好跟空格。
2. **强制换行**: 在行最后用两个空格并按下回车
3. **粗体和斜体**： 斜体用`*文字*` 或`_文字_`      粗体用`**文字**`   或` __文字__`   特别强调（粗斜体）用`***文字***` 或   `___文字___`
4. **分隔线**：用多于三个的`*`或者`-` 。
5. **标题**（html的head）：使用`#`作行开头，可以 1-6 个`#`，代表从大到小的六种标题规格，最多6个。若一段文字下一行为`====`或`--------`，该段文字自动处理为一级标题和2级标题。
6. **引用**： `>` 符号开头跟的内容
7. **无序列表**：使用 `-` 作行开头，子列表可以用制表符（tab）或四个空格来示意。 支持用`*` ,`-` 或者`+` 作标符。开头带空格可以作为下级列表.
8. **有序列表**：使用`1.    2.     3.  `等开头。`.`号后有空格.
9. **表格**：用 `|` 分隔，第二行可用 `|--------|:---------:| --------:|` 来分别指明是左对齐（默认），居中和右对齐，此时第一行会作为表头加粗居中。
10. **超链接**： `[显示文字](链接地址)`
11. **图片**： `![显示文字](链接地址)`
12. **代码**：在标准markdown里面支持四个空格或者tab开头自动进入代码块模式，但是这里要用  `` `文字` `` 作代码块. 在行代码内时, \` 需要用 \`\` 作外标.
在为知中根据不同代码不同标记，如下

~~~~~
```cpp  
代码内容
```
~~~~~  
注意: 在kramdown中使用\~ 而不是\` 作代码块. 另外, 长代码块(例如5个\` 优先于3个,可以利用该办法来表达.

### 使用HTML 方法
**字体颜色**：需要使用html方法 例如`<font color="red"> 文字 </font>`  
**居中对齐**: `<center>内容</center>`

### Kramdown
在Github中,旧版默认使用[maruku](http://maruku.rubyforge.org/markdown_syntax.html) 进行jekyll处理, 但由于停止更新, 现需要使用[kramdown](http://kramdown.gettalong.org/syntax.html) 来进行. 注意两者的差异.
- 语法块的下一行可以使用 `{: .language-ruby}` 来注明语言.当然也支持老式方法.

### 比较偏的用法:
- 内标签
`[显示内容][tag名]`
`[tag名]: 链接地址`


### cmd markdown : 网上MD的服务器
[简明语法](https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown) ;
[高级语法](https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown#cmd-markdown-高阶语法手册)

-  标签: 标签名1 标签名2    (用于归类, 也可用tags)
-  `[TOC]`        (内容目录结构)
-  `~~内容~~`       (删除线)
-  引用
`[^cite1]`    (插入位置,根据位置编号)
`[^cite1]`  : 内容    (对应内容,参考文献)
	
- 数学公式, 请参考[Mathjax](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

~~~
$数学公式$  行内插入数学公式
$$ 数学公式 $$ 整行为一数学
~~~

- [流程图](http://adrai.github.io/flowchart.js/)

~~~
```flow  
内容  
```  
~~~

- 序列图 序列图语法参考. 

~~~
```seq  
内容  
```  
~~~


> 本博文已合并到[Github相关总结](/1233/01/01/Github-related/#standard-markdown)中, 不再更新.
