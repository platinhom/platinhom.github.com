---
layout: post
title: Jekyll下划线文件夹问题
date: 2015-12-02 04:31:49
categories: IT
tags: Website
---


今天下了Python的手册, 在Github/Jekyll生成时均页面无法正常显示, 但直接双击相应文件浏览器直接打开都没有问题. 据查, 主要原因是Jekyll对所有underscore leading文件夹(如\_)均不进行复制到_site文件夹操作, 因此无法在网页中存在\_static等文件夹, 从而无法加载一些js/css文件.

在Python中多利用[Sphinx](http://sphinx-doc.org/)来产生文档, 类似于Jekyll, Sphinx也使用自己的语言, 但主要基于Python. 在Sphinx里素材放在_static. _images, _templates 等文件夹内, 如果下载相应的离线文档包, 在jekyll中将不能挂载! 这个问题再Python说明书, Numpy, SciPy中均存在. 

这是个兼容的问题了, 在这个讨论[^jekyllgithubissue] 中提及到了一种解决办法: 在Jekyll根目录挂载这个离线文档中建立`.nojekyll`文件, 从而跳过Jkeyll的解析. 这样能够使Sphinx的网页原封不动地显示.

但这个办法始终是不够用的哇~ 其实利用find+sed 原位修改一下就好了~~

下面的脚本直接在相应文件夹执行就OK了~例如python2.7/里面有\_static等文件夹, 进去python2.7里面直接./sphinx2jekyll.sh 即可. 要等蛮久..要是报错什么鬼读写问题, 可能因为执行太快文件没有处理完成, 手动检查是否含有\_的遗漏并修复.

- `grep "_static/" */*` 进行相应级别的查找(`*/*`替换为报错的级别)
- `sed -i "s/_static\//static_\//g" 文件名` 对该文件名进行修复.

<script src="https://gist.github.com/platinhom/7dee08dd8df71dd29418.js?file=sphinx2jekyll.sh"></script>

[^jekyllgithubissue]: [Jekyll ignores directories/files with underscores](https://github.com/jekyll/jekyll/issues/55)




------
