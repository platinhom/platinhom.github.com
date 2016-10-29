---
layout: post
title: Markdown 笔记
categories: IT
tags: IDE Git Key
---

> Update: 2016.10.27 for 一坨翔

> Markdown 有很多版本, 概述起来分三类:   
>
> - 基础Markdown : 段落/引用 有序/无序列表 多级标题 水平线 超链接/图片 斜体/粗体 (行)代码
> - 基本扩展Markdown : 学习标准, 以 GFM 为标杆, 主要多了: 高亮围栏代码块, 表格, 删除线 (有些有任务列表).
> - 复杂扩展Markdown : 定制性强, 根据具体使用来调整. 如Kramdown和MultiMarkdown

﻿[Markdown](https://zh.wikipedia.org/wiki/Markdown) 是一种轻量级标记语言, 允许人们用易读易写的纯文本格式编写文档, 然后转换成有效的XHTML或HTML文档, 便于读取, 简之就是`易读易写`. Markdown通过简易的标记来编写纯文本文档, 然后转为格式化的便于阅读的文档, 因此被广泛用于各种一般网络文档的书写. Markdown的标准语法十分简单, 以致于衍生了各种版本的Markdown, 例如Github里面使用的GFM. 

Markdown文件扩展名使用`md`或`markdown`，很多现代的文档编辑器都支持对Markdown语法的着色. 一些笔记软件也是支持Markdown的, 像有道云笔记最近就支持了`Markdown`哦! 有不少专门用于Markdown阅读的软件(甚至online版的), 这些软件好不好用关键看这几点:

- 有木有同步预览 
- 同步预览有木有同步拖动功能
- 支持的Markdown 衍生类型有多少
- 能不能定制CSS

一些支持Markdown的产品如: 

- 在 **有道云笔记** 中可以选择创建新文件, 类型`Markdown`, 就会新建一个以`.md`结尾的笔记(后缀不能改哦), 并出现分屏的窗口(一个Markdown输入一个预览)
- 在 **为知笔记**当中使用`.md`后缀命名笔记即可识别为markdown, 当编辑完毕保存后会显示预览.
- Github : 支持直接转换显示, 包括md文件和评论. 使用GFM.
- SourceForge, Reddit, Stack Exchange 等. 

Markdown有很多衍生方言, 没有一个统一化的标准. 最早的Markdown 源于2004年 创始人 John Gruber的[Markdown 1.0.1](http://daringfireball.net/projects/markdown/), 2014年Jeff Atwood 发起的 想标准化Markdown(但被创始人否决) 的 [CommonMark](http://commonmark.org/), 而比较流行的版本还包括Github使用的 [GitHub Flavored Markdown (GFM)](https://help.github.com/enterprise/11.10.340/user/articles/github-flavored-markdown/)和Sublime里面支持提及的[MultiMarkdown](http://fletcherpenney.net/multimarkdown/)

--- 

## 原始 Markdown

取于 2004年 最早版本的 [Markdown 1.0.1](http://daringfireball.net/projects/markdown/syntax), 也是基本遵循的法则. 中文可参考[图灵社区翻译版本](http://www.ituring.com.cn/article/775). 

| 用法 | MarkDown 表达 | HTML对应 | 解释 | 
|----|-----|-----|----| 
| 斜体 | \*文字\* 或 <br> \_文字\_ | \<em\> | 斜体和粗体表达时, 符号一定要与内容接触, 中间不能留空 |
| 粗体 | \*\*文字\*\* 或 <br> \_\_文字\_\_ | \<strong\> | 要是斜体和粗体并用, 可以用上两种表达: \_ab\*\*123\*\*cd\_|
| 换行 | 行末两空格 | \<br /\> | 最常用于段落和引用换行 |
| 水平线 | \-\-\- 或 <br> \*\*\* | \<hr /\>| 多于三个,中间甚至可空格|
|---|----|---|----|
| 段落 | 无特殊标记的内容 | \<p\>| 一般 MD 里没啥特殊块标注的都是段落. 连续几行会合并为一个段落(可包含行末两空格的换行), 段落和段落之间用空行隔开
| 标题 | \#\# | \<h1>,\<h2>..\<h6> | 多少个\#就是多少级标题,最小是6级. 另外前两级还有特殊表示法.
| 无序列表 | \- 内容1 <br> \- 内容2 | \<ul\> | 支持用\* ,\- 或者\+ 作标符。子列表可以用制表符（tab）或四个空格来开头示意。 开头带空格可以作为下级列表. | 
| 有序列表 | 1. 内容1 <br> 2. 内容2 | \<ol\> | \. 号后有空格 (不多于4个)或tab. 支持子列表. 极度注意, 有序列表写的序号和显示的序号无关 (只与排列当前位置相关), 但习惯也按顺序书写.  
| 引用 | \> 内容 | \<blockquote\> | 引用可嵌套 (\> \> 内容); 引用块可包含其他MD元素; 可以只用一个\>, 也可以行行都\> | 
| 超链接 | \[显示文字](链接地址) | \<a\> | 链接地址空一格后可接链接解释, 支持标签外部定义链接 | 
| 图片 | \!\[显示文字](链接地址) | \<img\> | 同超链接部分 | 
| 行内代码 | \`代码\` | \<code> | 多个\`可以用于包括单个\`
| 代码块 | 行前四空格或tab | \<pre>\<code> | \<\>\& 会被html转义

附注: 

- *斜体*和**粗体**: 这个表达式符号和内容紧接, 不要` ** hello ** `, 应该紧接为`**hello**`
- **标题**（html的head）：使用`#`作行开头，可以 1-6 个`#`，代表从大到小的六种标题规格，最多6个。若一段文字下一行为`====`和`--------`，该段文字自动处理为一级标题和2级标题
- **特殊符号**：``#_` `` 等， 要在行头等特殊位置表达，可用转义符`\`。
- 自动超链接: `<http://www.baidu.com>` 会直接转为超链接. 还支持**邮箱**哦! 
- 标签化**链接**: `[显示文字][标签名] ... [标签名]: 超链接地址` , 同样也支持鼠标移过去时进行解释 (链接地址后空格加入说明). 
- 隐性标签化链接: `[显示文字][] ... [显示文字]: 超链接地址` , 同样也支持鼠标移过去时进行解释 (链接地址后空格加入说明). 
- 行内代码: ``` `` hehe`haha `` ``` 多个\`时优先作为代码的外部
- HTML扩展 : 很多HTML元素没有的, 可以直接写HTML代码. 注意HTML 代码的前后都要留空来隔开MARKDOWN部分. 另外, 标签开头和结尾之前都不要留空格或tab. 例如: 
	- 换行: 有些时候不方便行末双空格换行, 可以用`<br/>`
	- 字体颜色: `<font color="red"> 文字 </font>`  
	- 居中对齐: `<center>内容</center>` 

基本上, 原始的Markdown 和 后续的 `Fenced 代码块 (语法高亮)`, `表格`, `删除线`, 构成了现代主流的Markdown用法 (可以直接去看GFM介绍).

## [CommonMark](http://commonmark.org/)

Jeff Atwood 发起的想标准化Markdown的项目, 一般其他方言都支持. 现在项目主持在[John MacFarlane的Github内](https://github.com/jgm), 其中还包括著名的Pandoc项目哦! Commonmark 提供一个[简易教程](http://commonmark.org/help/), 建议初学者玩玩. 也提供[在线测试](http://spec.commonmark.org/dingus/), 直接查看MD结果. 

和原始MD的区别可以查看[Github这里](https://github.com/jgm/CommonMark#differences-from-original-markdown), 基本没有引入新支持HTML元素, 但也有些重要常用新增加特点: 

- Fenced 代码块: ```` ~~~ 内容 ~~~ ````, ```` ``` 内容 ``` ```` 都支持, 扩展了根据缩进定义的代码块. ````` ```` 优先于 ``` `````
- 有序列表支持`1) 内容`的表达, 切换`1)`和`1.` 会被认为是两个不同列表. 另外, 有序列表开始的编号变得重要. 

## GFM (Github Flavored Markdown)

如果是新手, 又是接触Github, 那么推荐阅读官方[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

GFM为了日常使用, 新加了些常用功能 (可以参考[官方区别文档](https://help.github.com/enterprise/11.10.340/user/articles/github-flavored-markdown/)) : 

- **表格** : 用 `|` 分隔各列，首列前和末列后的 `|`可省略. 
	- 第二行可用 `|--------|---------| --------|`分隔前后, 这时第一行会成为表头. 如果该行出现在表其他位置, 则会用于表内分割 (即有不同的\<tbody>), 显示上会在一个大表内, 会有边界差异(甚至改变后面对齐). 
	- 第二行可以指明对齐: `|--------|:---------:| --------:|` 来分别指明是左对齐（默认），居中和右对齐，此时第一行会作为表头加粗居中。
- **删除线** : `~~内容~~` 相当于 `<del>`. 蛮有用的新功能.
- **任务列表** : `- [ x ] 内容` 和 `- [ ]`, 前者是任务已完成,后者没完成. 本质是个checkbox.
- **语法高亮** : 在fenced 语法块 ```` ```python ```` 中加入语言名进行解析. 使用[linguist](https://github.com/github/linguist)进行检测和高亮, 支持语言名称参考[the languages YAML file](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml). (注意: 很多markdown方言都支持语法高亮了, 但是解析器和支持语言各不相同, 这里只是GFM 这里的版本)
- **表情emoji** : 格式是`:代码:` :+1: . github评论等支持弹出提示, 一般就要参考[EMoji cheat sheet](http://www.webpagefx.com/tools/emoji-cheat-sheet/). [Emoji cheat sheet 源代码参考](https://github.com/WebpageFX/emoji-cheat-sheet.com). 

> 标注语言的fenced 代码块:   

~~~~~markdown
```cpp  
代码内容
```
~~~~~

其余差异:

- 一般MD在词内强调使用`_`或者`*`, GFM在词内 (注意, 是词内) 仅使用`*`, 可以使得`2014_10_01` 这样不会被错译.
- 网址自动链接: 一般MD使用`<网址>`可以自动链接, GFM直接网址就可以了, 如`http://www.baidu.com`. 

另外, GFM里还针对代码仓库和用户评论有一些专用语法, 例如`@user, @team/user`, `#` 用于pull和问题的追踪,SHA的自动连接等. 不知道也罢 ╮(╯▽╰)╭

## Multimarkdown

[MultiMarkdown](http://multimarkdown.com/) 是偏向于科学写作的Markdown (尤其往Latex靠近) , 引用很多功能, 能够导出多种格式 (包括latex). 特征语法可以参考: [MultiMarkdown Cheat Sheet](https://rawgit.com/fletcher/human-markdown-reference/master/index.html). 简而言之, 包括以下特征:

- 脚注 `[^脚注名]`  .. `[^脚注名]: 脚注解释`
- 文献(或别的)引用索引和引用内容 (citations and bibliography)
- latex的数学支持
- CriticMarkup功能, 即支持 高亮, 删除, 下划, 替换几种常用标记模式
- definition lists
- cross reference
- document metadata

## Kramdown

在Github中,旧版默认使用[maruku](http://maruku.rubyforge.org/markdown_syntax.html) 进行jekyll处理, 但由于停止更新, 现需要使用[kramdown](http://kramdown.gettalong.org/syntax.html) 来进行. 注意两者的差异, 细节可参考本处另一篇博文: [kramdown和markdown较大的差异比较](/2015/11/06/Kramdown-note/), 比较重要的差异如下 : 

- `$$....$$` latex数学代码块
- IAL(Inline Attribute Lists) 行内属性标记 `{:attribute="value"}`, 标记在对象后. 其中两个固定用法: `{:.class}` 和 `{: #id}`用于指明类和身份ID. 
	- 语法块的下一行可以使用 `{: .language-ruby}` 来注明语言.当然也支持老式方法. 另外这样可以对行内代码进行高亮哦!
- HEADER ID : `## Header {#ID1} .. [GoH1](#ID1)`
- Footnote: `[^footnote] ... [^footnote]: 内容`
- `^` End of block标记 (EOB). 
- `{::nomarkdown} .. {:/nomarkdown}` 可以将其中的部分不进行Markdown处理, 如果因为Markdown转换会引起麻烦(尤其是HTML代码), 使用这可以避免一些bug. 
- `{::comment} .. {:/comment}` 可以进行注释啦, 注释是不会转到HTML上的.


## 其余非主流

### 有道云笔记

有道云笔记 2016.5开始支持markdown: 

- 支持通用型markdown
- 支持一般的表格, 代码块. 
- 支持删除线, 代办事宜列表
- `==内容==` 可以文字背景黄色高亮
-  ````` ```math   ````` 代码块可以用latex公式
- 支持流程图, 序列图, 甘特图. 

### cmd markdown : 网上MD的服务器
[简明语法](https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown) ;
[高级语法](https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown#cmd-markdown-高阶语法手册)

-  标签: 标签名1 标签名2    (用于归类, 也可用tags)
-  内容目录结构 : `[TOC]`
-  删除线 : `~~内容~~` 
-  Footnote引用 : `[^footnote]`
-  数学公式, 请参考[Mathjax](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

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


## Reference 

- [kramdown和markdown较大的差异比较](/2015/11/06/Kramdown-note/)
- [英文维基](http://en.wikipedia.org/wiki/Markdown); [中文维基](http://zh.wikipedia.org/wiki/Markdown)
- 2004年John Gruber的[Markdown 1.0.1](http://daringfireball.net/projects/markdown/), [图灵社区翻译](http://www.ituring.com.cn/article/775)
- [RFC7763](https://tools.ietf.org/html/rfc7763) : 注册 text/markdown 作为MIME类型. [RFC7764](https://tools.ietf.org/html/rfc7764) : 注册多种Markdown语言 (包括区别)
- [Ubuntu Markdown中文教程](http://wowubuntu.com/markdown/)
- 编辑器可参考: [知乎: 用Markdown 写作用什么文本编辑器？](http://www.zhihu.com/question/19637157)
	- Window 下软件: [MarkDownPad](http://markdownpad.com/), 
	- Mac 下软件: [Mou](http://25.io/mou/), ByWord
	- Online 软件: [Cmd Markdown](https://www.zybuluo.com/mdeditor), [StackEdit](https://stackedit.io/), [Raysnote](https://raysnote.com/). 
	- Chrome: [Markdown here](https://chrome.google.com/webstore/detail/markdown-here/elifhakcjgalahccnjkneoccemfahfoa)  

附些音乐: 

- 游戏王: 此乐一出谁与争锋? <http://music.163.com/#/m/song?id=4998139>

{::nomarkdown}

<div>
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="http://music.163.com/outchain/player?type=2&id=784594&auto=1&height=66"> </iframe>
</div>

{:/nomarkdown}
