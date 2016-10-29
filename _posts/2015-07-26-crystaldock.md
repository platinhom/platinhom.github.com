---
layout: post
title: Crystaldock
date: 2015-07-25 20:27:28
categories: CompCB
tags: CompBiol CADD Python src Presentation
---

Crystaldock是一个基于片段的药物设计方法.以前组会讲过.该方法中,首先打碎小分子配体成多个片段,然后识别出每个片段的微环境(周围几个残基),根据微环境情况对新的复合物进行分析,并引入相应片段,组合成新的分子.

当时组会(2012.3)报告PPT(PPT的Gview显示有点问题..还是pdf好..):

<iframe src="http://docs.google.com/gview?url=http://platinhom.github.io/HomPDF/Report/CrystalDock.pptx&embedded=true" style="width:1000px; height:800px;" frameborder="0"></iframe>

PDF版:

<iframe src="http://platinhom.github.io/HomPDF/Report/CrystalDock.pdf" style="width:1000px; height:730px;" frameborder="0"></iframe>


主程序源码如下:

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

<pre><code class="language-python" id="src"></code></pre>

<script>
$.get("http://platinhom.github.io/other/scripts/crystal_dock.py",function(data,status){
	//alert("Data: " + data + "\nStatus: " + status);
	$("#src").html(data);
	Prism.highlightAll();
	//Prism.highlightElement($('#src')[0]);
});
</script>


## Reference
1. [Crystal Dock](http://nbcr.ucsd.edu/data/sw/hosted/crystaldock/)
2. [SF-download](http://sourceforge.net/projects/crystaldock/files/)
3. [CrystalDock: A Novel Approach to Fragment-Based Drug Design](http://pubs.acs.org/doi/abs/10.1021/ci200357y), [l](http://pubs.acs.org.sci-hub.org/doi/abs/10.1021/ci200357y)

------
