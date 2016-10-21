---
layout: post
title: DOAJ:open access库
date: 2016-01-16 08:36:24
categories: IT
tags: Internet
---

**DOAJ** 全称 *Directory of Open Access Journals*, [主页](https://doaj.org/). 顾明思议是open access的杂志的数据库. 需要杂志交付一些money登录在上面, 其实用途并不大嘛.. 可以在上面搜索, 搜索的结果都是open access的! 免费下载~

但DOAJ对于open access并不全, 例如PNAS, Oxford, wiley和springer的OA杂志都没有收录.. 但收录了很多乱七八糟的, 例如中文的... 至今(2016.1.23)收录 **11,075** 本杂志共 **2,166,082** 文章.

DOAJ收录的出名出版社包括:

- [BMC](http://www.biomedcentral.com/) BioMed Central, 收录了10几万
- [Hindawi](http://www.hindawi.com/), 收录了10几万
- [MDPI](http://www.mdpi.com/)
- [Copernicus](http://publications.copernicus.org/)
- [Frontiers](http://www.frontiersin.org/)
- [PLOS](http://www.plos.org/)部分(实际只有800多..)
- Medknow Publications, 5w+
- Elsevier, 2w多

这里只谈使用和接口.

华丽丽的分界线

---------

### 网页

打开[主页](https://doaj.org/), 在上面有两个搜索可选项, 一个搜journal一个搜文献. 前者搜出相关journal, 后者自然是文献了.

点击[Search](https://doaj.org/search?)可以进入更复杂的搜索页面, 不进行搜索时列出了所以journal, article, publisher信息(可以点击数字10设置显示数量). 右边是列出的结果. 可以根据Title, ISSN, DOI (可以前缀), publisher等进行搜索. 

### API

API是使用关键, 获得数据是json格式. [接口](https://doaj.org/api/v1/docs)名是"https://doaj.org/api/v1/" , 开放的接口有: 

- GET  /api/v1/search/articles/{search_query}  搜索文章
- GET  /api/v1/search/journals/{search_query}  搜索杂志
- GET  /api/v1/articles/{article_id}  根据具体ID搜文章, 少用
- GET  /api/v1/journals/{journals}  根据具体ID搜杂志, 少用

说白了就是用前两个..支持的搜索关键词项:

- **title** - 文章/杂志标题内含关键词
- **doi** - 文章doi(要精确匹配,不用只前缀), 搜杂志没有该方法.
- **issn** - 文章/杂志ISSN
- **publisher** - 发行商名, 例如Elsevier这样, 非精确匹配
- **abstract** - 搜索文章摘要 (只有article有)
- **license** - 精确licence, 如CC-BY (只有journal有)

`关键词名:值` 就是其接口的用法(无`?`号)

不能使用通配符, 正则, fuzzy和 Proximity 搜索....

例如: [https://doaj.org/api/v1/search/articles/publisher:Elsevier](https://doaj.org/api/v1/search/articles/publisher:Elsevier)

抓出来的是Json的数据, 默认每页10个, 最多每次100个..pageSize/page/sort 是辅助词用来控制每页多少结果, 第几页, 排序方式. 使用GET的传递方式, 例如: 

`https://doaj.org/api/v1/search/articles/publisher:Elsevier?pageSize=100&page=5`

在接口API介绍里面可以尝试自己填入关键词然后获得相应http/curl的表达式. 会有相应的回复以及头信息, 正常响应码 200.(不正常400)

更多问题参考 [FAQ](https://doaj.org/faq)

这个接口相比CrossRef还是弱了点..

------
