---
layout: post
title: Endnote:抓杂志信息并加工
date: 2015-12-15 01:21:28
categories: IT
tags: Software
---

比较邪恶危险的做法. 小盆友勿乱学..被封号了不要怪我..

- 点左上的Online Search mode (temporary library)进入搜索模式
- 去google一下该杂志的全名, 使用web of science或者相应搜索引擎进行搜索(录入较慢)
- 搜索结果正常后, 和网上杂志的大概年月对上后. 说明资料建立OK
- 新建一个Library, 名字随便. 选中刚才在线搜索的**全部**结果(ctrl+A). 右键Copy Reference to 新建的库.
- 可以关闭旧的临时搜索库了, 关闭再打开新建的库(关闭才会正式保存).

处理:

- `Export`为 `xml` (Save as type: xml; Output style: Show All Field), 为什么是xml? 因为有标签而且方便处理并导入. 例如这样形式: 

~~~html
<?xml version="1.0" encoding="UTF-8" ?><xml><records><record><database name="ENJCC_1.enl" path="C:\Users\Hom\Desktop\Library.enl">Library.enl</database><source-app name="EndNote" version="17.0">EndNote</source-app><rec-number>574</rec-number><foreign-keys><key app="EN" db-id="pd09zt9thx2evzeapdyp9drbpdt2rs552xdv">574</key></foreign-keys><ref-type name="Journal Article">17</ref-type><contributors><authors><author><style face="normal" font="default" size="100%">Pascualahuir, J. L.</style></author><author><style face="normal" font="default" size="100%">Silla, E.</style></author><author><style face="normal" font="default" size="100%">Tomasi, J.</style></author><author><style face="normal" font="default" size="100%">Bonaccorsi, R.</style></author></authors></contributors><auth-address><style face="normal" font="default" size="100%">Pascualahuir, Jl&#xD;Univ Valencia,Fac Ciencias Quim,Doctor Moliner 50 Burjasot,Valencia,Spain&#xD;Univ Valencia,Fac Ciencias Quim,Doctor Moliner 50 Burjasot,Valencia,Spain&#xD;Univ Pisa,Departimento Chim,I-56100 Pisa,Italy&#xD;Cnr,Ist Chim Quantist Energet Molec,I-56100 Pisa,Italy</style></auth-address><titles><title><style face="normal" font="default" size="100%">Electrostatic Interaction of a Solute with a Continuum - Improved Description of the Cavity and of the Surface Cavity Bound Charge-Distribution</style></title><secondary-title><style face="normal" font="default" size="100%">Journal of Computational Chemistry</style></secondary-title><alt-title><style face="normal" font="default" size="100%">J Comput Chem</style></alt-title></titles><periodical><full-title><style face="normal" font="default" size="100%">Journal of Computational Chemistry</style></full-title><abbr-1><style face="normal" font="default" size="100%">J Comput Chem</style></abbr-1></periodical><alt-periodical><full-title><style face="normal" font="default" size="100%">Journal of Computational Chemistry</style></full-title><abbr-1><style face="normal" font="default" size="100%">J Comput Chem</style></abbr-1></alt-periodical><pages><style face="normal" font="default" size="100%">778-787</style></pages><volume><style face="normal" font="default" size="100%">8</style></volume><number><style face="normal" font="default" size="100%">6</style></number><dates><year><style face="normal" font="default" size="100%">1987</style></year><pub-dates><date><style face="normal" font="default" size="100%">Sep</style></date></pub-dates></dates><isbn><style face="normal" font="default" size="100%">0192-8651</style></isbn><accession-num><style face="normal" font="default" size="100%">WOS:A1987J750300004</style></accession-num><notes><style face="normal" font="default" size="100%">Times Cited:353&#xD;Cited References Count:30</style></notes><urls><related-urls><url><style face="normal" font="default" size="100%">&lt;Go to ISI&gt;://WOS:A1987J750300004</style></url><url><style face="normal" font="default" size="100%">http://onlinelibrary.wiley.com/store/10.1002/jcc.540080605/asset/540080605_ftp.pdf?v=1&amp;t=ii6plfbn&amp;s=ab06df4d28106c18581d2770c5942c7ac16e25eb</style></url></related-urls><pdf-urls><url>internal-pdf://2103995856/Pascualahuir-1987-Electrostatic Intera.pdf</url></pdf-urls></urls><electronic-resource-num><style face="normal" font="default" size="100%">DOI 10.1002/jcc.540080605</style></electronic-resource-num><language><style face="normal" font="default" size="100%">English</style></language></record></records></xml>
~~~ 

其中, \<record\>开始的就是一个record的摘要内容了,直到\</record\>终结该条记录. 底部的\</records\>终结所有记录. \<pdf-urls\>\<url>internal-pdf://2103995856/Pascualahuir-1987-Electrostatic Intera.pdf\</url>\</pdf-urls\></urls\> 是对应的本地文件相对位置哦!!~
- 我要替换掉Note中多余的第一行部分, 只留下 Times Cited: 开头的部分, 方便我按引用排序, 优先下那些高引paper. 打开一个可以正则表达式进行替换的编辑器, 例如Sublime. 进行替换搜索: 

`(?<=<notes><style face="normal" font="default" size="100%">).{5,20}?(?=Times)` 

替换为空白.

- 处理完后, 新建一个库, Import刚才的xml文件(Import图标, Import Option: Endnote generated XML, Duplicates: Import All)即可. 再怎么利用这些信息造数据库, 那就是你的事咯 ╮(╯▽╰)╭ 不懂? 不懂最好啦~~

------
