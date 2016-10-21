---
layout: post
title: 在写blog/Html时嵌入Pdf显示
date: 2015-06-07 15:40:04
categories: Coding
tags: Website HTML
---
对于科研的人,PDF对得比word要多,而且可以各种文档转化为PDF用于交流.这里作介绍如何在Blog(MD格式)或HTML中插入PDF.注意HTML代码是会直接在MarkDown转化的,不过要注意最好要代码前后留空行,保证作为一个代码段. 这里以一个简单的[PDF例子](http://platinhom.github.io/HomPDF/mou.pdf)为例

-  直接使用`embed`方法.例如直接写这段话就OK了,相应更改pdf文档位置及大小即可. 注意,使用的其实是内置的Aodbe PDF插件. 在Mou等编辑器上不能显示pdf.

~~~
<center><embed src="/pdf/mou.pdf" width="850" height="600"></center>
~~~
效果如下:
<center><embed src="/HomPDF/mou.pdf" width="850" height="600"></center>

- 使用frame的方法,效果类似. 英文好的可以参考[这里](http://www.ehow.co.uk/video_4983082_display-pdf-file-html-web.html)的介绍.

~~~
<iframe src="/pdf/mou.pdf" style="width:300px; height:100px;" frameborder="0"></iframe>
~~~

效果如下:

<iframe src="/HomPDF/mou.pdf" style="width:300px; height:100px;" frameborder="0"></iframe>

- 使用Google View来看. 据说支持多种格式如PPT,DOC.就是在国内不知道效果如何..
 
~~~
<iframe src="http://docs.google.com/gview?url=http://platinhom.github.io/pdf/mou.pdf&embedded=true" style="width:500px; height:100px;" frameborder="0"></iframe>
~~~

效果如下:

<iframe src="http://docs.google.com/gview?url=http://platinhom.github.io/HomPDF/mou.pdf&embedded=true" style="width:500px; height:100px;" frameborder="0"></iframe>

- 使用豆丁的[Docin API](http://api.docin.com/). 这是开放式“文档在线预览”接口程序,可以显示doc,pdf等文件.必须指定网络文档. 现在需要付费了,还会有人用么?

- 使用`<object>`标签插入对象. 这么复杂,记不住.

~~~~
<object border="0" classid="clsid:CA8A9780-280D-11CF-A24D-444553540000" width="650" height="600" VIEWASTEXT="">
<PARAM NAME="_cx" VALUE="17197">
<PARAM NAME="_cy" VALUE="15875">
<param name="_Version" value="65539">
<param name="_ExtentX" value="20108">
<param name="_ExtentY" value="10866">
<param name="_StockProps" value="0">
<param name="SRC" value="yourfile.pdf"> </OBJECT>
~~~~

推荐使用第一种.找到更多方法将继续更新.

---
