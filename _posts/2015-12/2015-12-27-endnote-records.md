---
layout: post
title: Endnote:Journal的XML条目
date: 2015-12-27 12:28:13
categories: IT
tags: Software
---

XML是比较方便统一的数据源, 可以方便地导入导出数据.

### Endnote XML主体结构

~~~html
<?xml version="1.0" encoding="UTF-8" ?><xml><records>
<record>..</record>
</records></xml>
~~~

先声明xml, 符号, 然后是表面xml数据的标签, 然后再是总数据records标签, 最后是每个记录的record标签, 每个record标签内有各个属性标签, 这里的只讨论Journal的标签.

### Journal标签

按显示顺序:

- database : 表面是什么数据库的,数据源
- source-app : 表面是Endnote并且那个版本产生的
- rec-number : 表明该数据是第几条
- foreign-keys : ??? 貌似和上面类似
- ref-type : 表面该条是那种类型的记录, 一般为Journal. 标签inner内容是该类型的对应编号.
- contributors : 贡献者, 一般就是作者, 或者还有翻译作者(不同类型)等.这里包括:
	- authors : 该文献的所有作者. 里面再有每个`<author> </author>`记录.
	- translated-authors: 翻译者. 里面再有每个`<author> </author>`记录, Journal一般没有该项.
- auth-address : 作者地址. 只有一条.内容换行显示的话使用`&#xD;`
- titles : 该条目文献的题目或相关的, 包括子条目:
	- title : 就是文献题目了 (真正的Title项)
	- secondary-title : 可能是二级题目? Journal 里面这个一般是杂志名 (Journal项)
	- alt-title : 另一个可选的 *title*. Journal 里面这个一般是杂志简称 (Alternate Journal项).
	- short-title : 对应short title
	- translated-title : 对应 translated title
- periodical : 杂志全称和简称信息对应关系, 内含两项.
	- full-title : 杂志全称
	- abbr-1 : 杂志简称
- alt-periodical : 和periodical类似,但是是在自定义Journal全称-简称. 如果没有自定义Journal信息, 这项可能和上面一致; 如果有, 上一项periodical可能就没有.
	- full-title : 杂志全称
	- abbr-1 或 abbr-2 或 abbr-3: 杂志简称, 对应简称表里1,2,3.
- pages : 对应 pages
- volume : 对应Volume
- number : 对应issue
- edition : 对应 epub date
- section : 对应start page
- reprint-edition : 对应reprint edition
- keywords : 内含 相应每行一个 `<keyword>...</keyword>`
- dates : 日期相关, 内含:
	- year : 对应year
	- pub-dates : 里面再含一个`<data>...</date>`, 对应Date 
- orig-pub : original publication
- isbn : 对应ISSN部分
- accession-num : 对应accession number
- call-num : 对应call number
- abstract : 摘要部分.
- label : 对应label
- caption : 对应 caption
- image : 对应图片, 他会复制图片到库的目录下(就是PDF同层的地方). 使用相对地址
- notes : 对应notes
- work-type : 对应type of arrticle
- reviewed-item : 对应reviewed item
- urls : 各种链接和pdf连接
	- related-urls : 对应相对应的网页连接 `<url>..</url>`: 
	- pdf-urls : 对应PDF的连接 `<url>..</url>`, 一般内容是 `internal-pdf://`后面是PDF文件夹内链接
- custom1 : 对应 Legal note
- custom2 : 对应 PMCID
- custom6 : 对应 NIHMSID
- custom7 : 对应 article number
- electronic-resource-num : 对应DOI
- remote-database-name : 对应 name of database
- remote-database-provider : 对应database provider
- research-notes : 对应Research Notes部分
- language : 对应Language语种
- access-date : 对应Access Date部分

> 注意:   

- Rate评分是没有显示的. 
- &lt; &gt; 和 &#xD; 对应 <>和换行
- style部分样式是可以不要的 (一样可以导入, 还省很多空间).

其实根据介绍, 我们知道一篇文献最基础的要求是:

- 题目: titles -> title
- 作者: contributors -> authors -> author
- 杂志: titles -> secondary-title
- 年: dates -> year
- 卷: volume
- 期: number
- 页码: pages

更丰富应该拥有的是: 

- doi: electronic-resource-num
- 外链: urls-> related-urls -> url
- pdf: urls-> pdf-urls -> url (或者更进一步需要database来构建绝对地址)
- notes: 额外信息, 例如引用次数
- 摘要: abstract

### 一个record的示例:

去掉style部分 (为了方便, 本来是一行的, 我断行了):

~~~html
<?xml version="1.0" encoding="UTF-8" ?><xml><records>
<record>
<database name="newlib.enl" path="/Users/Hom/Desktop/newlib.enl">newlib.enl</database>
<source-app name="EndNote" version="17.2">EndNote</source-app>
<rec-number>2</rec-number>
<foreign-keys><key app="EN" db-id="20xtvasr7stxf0esstqv5fw9a9s59wt9f0aw">2</key></foreign-keys>
<ref-type name="Journal Article">17</ref-type>
<contributors>
<authors><author>Mullinax, J. W.</author><author>Sokolov, A. Y.</author><author>Schaefer, H. F.</author></authors>
<translated-authors><author>translated author</author></translated-authors>
</contributors>
<auth-address>Schaefer, HF&#xD;Univ Georgia, Ctr Computat Quantum Chem, Athens, GA 30602 USA&#xD;Univ Georgia, Ctr Computat Quantum Chem, Athens, GA 30602 USA&#xD;Univ Georgia, Ctr Computat Quantum Chem, Athens, GA 30602 USA&#xD;Princeton Univ, Dept Chem, Princeton, NJ 08544 USA</auth-address>
<titles>
<title>Can Density Cumulant Functional Theory Describe Static Correlation Effects?</title>
<secondary-title>Journal of Chemical Theory and Computation</secondary-title>
<alt-title>J Chem Theory Comput</alt-title>
<short-title>shorttitle</short-title>
<translated-title>translated title</translated-title>
</titles>
<periodical>
<full-title>Journal of Chemical Theory and Computation</full-title>
<abbr-1>J Chem Theory Comput</abbr-1>
</periodical>
<alt-periodical>
<full-title>Journal of Chemical Theory and Computation</full-title>
<abbr-1>J Chem Theory Comput</abbr-1>
</alt-periodical>
<pages>2487-2495</pages>
<volume>11</volume>
<number>6</number>
<edition>epubdate</edition>
<section>startpage</section>
<reprint-edition>reprintedition</reprint-edition>
<keywords><keyword>configuration-interaction calculations</keyword></keywords>
<dates>
<year>2015</year>
<pub-dates><date>Jun</date></pub-dates>
</dates>
<orig-pub>originalpublication</orig-pub>
<isbn>1549-9618</isbn>
<accession-num>accessionnumber</accession-num>
<call-num>callnumber</call-num>
<abstract>We evaluate the.</abstract>
<label>label</label>
<image>3316878595SV物品.jpg</image>
<caption>caption</caption>
<notes>Times Cited:0&#xD;Cited References Count:112</notes>
<work-type>typeofarrticle</work-type>
<reviewed-item>revieweditem</reviewed-item>
<urls>
<related-urls><url>&lt;Go to ISI&gt;://WOS:000356201700010</url><url>http://pubs.acs.org/doi/pdfplus/10.1021/acs.jctc.5b00346</url></related-urls>
<pdf-urls><url>internal-pdf://2020440412/Mullinax-2015-Can Density Cumulant.pdf</url></pdf-urls>
</urls>
<custom1>legalnote</custom1>
<custom2>pmcid</custom2>
<custom6>mihmsid</custom6>
<custom7>articlenumber</custom7>
<electronic-resource-num>10.1021/acs.jctc.5b00346</electronic-resource-num>
<remote-database-name>name of database</remote-database-name>
<remote-database-provider>database provider</remote-database-provider>
<research-notes>researchnotes</research-notes>
<language>English</language>
<access-date>accessdate</access-date>
</record>
</records></xml>
~~~

完整的导出时:
 
~~~html
<?xml version="1.0" encoding="UTF-8" ?><xml><records><record><database name="newlib.enl" path="/Users/Hom/Desktop/newlib.enl">newlib.enl</database><source-app name="EndNote" version="17.2">EndNote</source-app><rec-number>2</rec-number><foreign-keys><key app="EN" db-id="20xtvasr7stxf0esstqv5fw9a9s59wt9f0aw">2</key></foreign-keys><ref-type name="Journal Article">17</ref-type><contributors><authors><author><style face="normal" font="default" size="100%">Mullinax, J. W.</style></author><author><style face="normal" font="default" size="100%">Sokolov, A. Y.</style></author><author><style face="normal" font="default" size="100%">Schaefer, H. F.</style></author></authors><translated-authors><author><style face="normal" font="default" size="100%">translated author</style></author></translated-authors></contributors><auth-address><style face="normal" font="default" size="100%">Schaefer, HF&#xD;Univ Georgia, Ctr Computat Quantum Chem, Athens, GA 30602 USA&#xD;Univ Georgia, Ctr Computat Quantum Chem, Athens, GA 30602 USA&#xD;Univ Georgia, Ctr Computat Quantum Chem, Athens, GA 30602 USA&#xD;Princeton Univ, Dept Chem, Princeton, NJ 08544 USA</style></auth-address><titles><title><style face="normal" font="default" size="100%">Can Density Cumulant Functional Theory Describe Static Correlation Effects?</style></title><secondary-title><style face="normal" font="default" size="100%">Journal of Chemical Theory and Computation</style></secondary-title><alt-title><style face="normal" font="default" size="100%">J Chem Theory Comput</style></alt-title><short-title><style face="normal" font="default" size="100%">shorttitle</style></short-title><translated-title><style face="normal" font="default" size="100%">translated title</style></translated-title></titles><periodical><full-title><style face="normal" font="default" size="100%">Journal of Chemical Theory and Computation</style></full-title><abbr-1><style face="normal" font="default" size="100%">J Chem Theory Comput</style></abbr-1></periodical><alt-periodical><full-title><style face="normal" font="default" size="100%">Journal of Chemical Theory and Computation</style></full-title><abbr-1><style face="normal" font="default" size="100%">J Chem Theory Comput</style></abbr-1></alt-periodical><pages><style face="normal" font="default" size="100%">2487-2495</style></pages><volume><style face="normal" font="default" size="100%">11</style></volume><number><style face="normal" font="default" size="100%">6</style></number><edition><style face="normal" font="default" size="100%">epubdate</style></edition><section><style face="normal" font="default" size="100%">startpage</style></section><reprint-edition><style face="normal" font="default" size="100%">reprintedition</style></reprint-edition><keywords><keyword><style face="normal" font="default" size="100%">configuration-interaction calculations</style></keyword><keyword><style face="normal" font="default" size="100%">coupled-cluster theory</style></keyword><keyword><style face="normal" font="default" size="100%">contracted schrodinger-equation</style></keyword><keyword><style face="normal" font="default" size="100%">molecular electronic-structure</style></keyword><keyword><style face="normal" font="default" size="100%">ab-initio calculations</style></keyword><keyword><style face="normal" font="default" size="100%">wave-functions</style></keyword><keyword><style face="normal" font="default" size="100%">p-benzyne</style></keyword><keyword><style face="normal" font="default" size="100%">perturbation-theory</style></keyword><keyword><style face="normal" font="default" size="100%">quantum-chemistry</style></keyword><keyword><style face="normal" font="default" size="100%">beryllium dimer</style></keyword></keywords><dates><year><style face="normal" font="default" size="100%">2015</style></year><pub-dates><date><style face="normal" font="default" size="100%">Jun</style></date></pub-dates></dates><orig-pub><style face="normal" font="default" size="100%">originalpublication</style></orig-pub><isbn><style face="normal" font="default" size="100%">1549-9618</style></isbn><accession-num><style face="normal" font="default" size="100%">accessionnumber</style></accession-num><call-num><style face="normal" font="default" size="100%">callnumber</style></call-num><abstract><style face="normal" font="default" size="100%">We evaluate the performance of density cumulant functional theory (DCT) for capturing static correlation effects. In particular, we examine systems with significant multideterminant character of the electronic wave function, such as the beryllium dimer, diatomic carbon, m-benzyne, 2,6-pyridyne, twisted ethylene, as well as the barrier for double-bond migration in cyclobutadiene. We compute molecular properties of these systems using the ODC-12 and DC-12 variants of DCT and compare these results to multireference configuration interaction and multireference coupled-cluster theories, as well as single-reference coupled-cluster theory with single, double (CCSD), and perturbative triple excitations [CCSD(T)]. For all systems the DCT methods show intermediate performance between that of CCSD and CCSD(T), with significant improvement over the former method. In particular, for the beryllium dimer, m-benzyne, and 2,6-pyridyne, the ODC-12 method along with CCSD(T) correctly predict the global minimum structures, while CCSD predictions fail qualitatively, underestimating the multireference effects. Our results suggest that the DC-12 and ODC-12 methods are capable of describing emerging static correlation effects but should be used cautiously when highly accurate results are required. Conveniently, the appearance of multireference effects in DCT can be diagnosed by analyzing the DCT natural orbital occupations, which are readily available at the end of the energy computation.</style></abstract><label><style face="normal" font="default" size="100%">label</style></label><image><style face="normal" font="default" size="100%">3316878595SV物品.jpg</style></image><caption><style face="normal" font="default" size="100%">caption</style></caption><notes><style face="normal" font="default" size="100%">Times Cited:0&#xD;Cited References Count:112</style></notes><work-type><style face="normal" font="default" size="100%">typeofarrticle</style></work-type><reviewed-item><style face="normal" font="default" size="100%">revieweditem</style></reviewed-item><urls><related-urls><url><style face="normal" font="default" size="100%">&lt;Go to ISI&gt;://WOS:000356201700010</style></url><url><style face="normal" font="default" size="100%">http://pubs.acs.org/doi/pdfplus/10.1021/acs.jctc.5b00346</style></url></related-urls><pdf-urls><url>internal-pdf://2020440412/Mullinax-2015-Can Density Cumulant.pdf</url></pdf-urls></urls><custom1><style face="normal" font="default" size="100%">legalnote</style></custom1><custom2><style face="normal" font="default" size="100%">pmcid</style></custom2><custom6><style face="normal" font="default" size="100%">mihmsid</style></custom6><custom7><style face="normal" font="default" size="100%">articlenumber</style></custom7><electronic-resource-num><style face="normal" font="default" size="100%">10.1021/acs.jctc.5b00346</style></electronic-resource-num><remote-database-name><style face="normal" font="default" size="100%">name of database</style></remote-database-name><remote-database-provider><style face="normal" font="default" size="100%">database provider</style></remote-database-provider><research-notes><style face="normal" font="default" size="100%">researchnotes</style></research-notes><language><style face="normal" font="default" size="100%">English</style></language><access-date><style face="normal" font="default" size="100%">accessdate</style></access-date></record></records></xml>
~~~



------
