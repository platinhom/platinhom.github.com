---
layout: post
title: 网站统计
date: 2015-06-11 01:29:16
categories: IT
tags: Website
---

## Website Data Analysis 

做完网站, 当然关系自己网站的访问情况了, 要是热闹的话还可以搞点广告外快呢 2333.

### Google Analytics
1. 首先,得有Google账户.其次,到[Google Analytics](http://www.google.com/analytics/ce/mws/) 上注册(Access Google Analytics).
2. 新建用户,跟踪内容网站,设置好主页和网站名(随便起)后即可.
3. 随后,会处在跟踪代码中.会看到跟踪ID,和下面一段代码.将代码添加到页面代码中.最好是添加到页头模板页面中(github的_layout里的相应文件).添加后更新你的网站.
4. 随后就可以在报告中看到情况了!

### Baidu Tongji
1. 首先去 [百度统计](http://tongji.baidu.com/web/welcome/login) 注册账号(不同于一般百度账号). 点击注册, 注册百度统计站长版.
2. 注册时填写好你的网站, 选一个行业, OK. 就会创建一个账号并默认指定一个自己的网页.
3. 进去后, 可以在网站中心(上方)看到自有网站, 点击代码获取(或者在左边也有代码获取),选择异步加载的代码.可以获得相应代码.复制
4. 将代码添加到页面的head部分,即`</head>`之前.最好是添加到页头模板页面中(github的_layout里的相应文件).添加后更新你的网站.
5. 点击代码安装检查. 点击检查即可. 点击网站中心看到自由网站列表显示代码安装正确.
6. 成功后稍等一段时间即可在上方"报告"中看到自己网站的访问统计.统计的东西老TM多呢..

### 不蒜子(静态网页统计)
1. 到[不蒜子](http://ibruce.info/2015/04/04/busuanzi/)网页去. 就是很简单的统计点击数和访问数.
2. 在head部分加入代码安装脚本`<script async src="https://dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>` (和后面的代码一起放在别的地方也可以)
3. 使用以下代码进行总访问量,访客数,页面访问数的统计.搞掂!可以自己设置显示的文字,更多功能请参考其网页. 只计数不显示的话不加下面的代码就可以了.

~~~~
<span id="busuanzi_container_site_pv">本站总访问量<span id="busuanzi_value_site_pv"></span>次</span>
<span id="busuanzi_container_site_uv">本站访客数<span id="busuanzi_value_site_uv"></span>人次</span>
<span id="busuanzi_container_page_pv">本文总阅读量<span id="busuanzi_value_page_pv"></span>次</span>
~~~~

---
