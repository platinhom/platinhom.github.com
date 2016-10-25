---
layout: post
title: DOI-PMID-PMCID转换
date: 2015-12-31 09:11:19
categories: IT
tags: Internet
---

## PMID

PMID是在[PubMed](http://www.ncbi.nlm.nih.gov/pubmed)中使用的文章ID号, 在pubmed中搜索出来的结果都有一个PMID号.是一个数字串, 例如 [24936230](http://www.ncbi.nlm.nih.gov/pubmed/24936230). 

PubMed为啥不用DOI呢? 因为有的PubMed结果是没有DOI号的, 例如 [3940185](http://www.ncbi.nlm.nih.gov/pubmed/3940185).

Pubmed网址后面加上PMID就是对应的记录了, 如[http://www.ncbi.nlm.nih.gov/pubmed/24936230](http://www.ncbi.nlm.nih.gov/pubmed/24936230), 但如果要用DOI对应网址, 就要加个搜索项`?term=doi`: [http://www.ncbi.nlm.nih.gov/pubmed/?term=10.1021/ml100016x](http://www.ncbi.nlm.nih.gov/pubmed/?term=10.1021/ml100016x).

一部分DOI在PubMed中都是收录有的, 但一些和生命医学无关的估计就没有被收录了, 例如数学的.. 一般的PMID都有DOI, 除了极少数例外没有. 

## PMCID

PMCID是[PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/)中使用的ID, 由PMC前缀和一个数字串组成, 例如 `PMC2883744`.

PMC是提供免费 NIH/NLM 生物医学和生命科学全文文献的数据库, 至今提供300多万篇全文(写的那天). 欧洲也有[Europe PMC](http://europepmc.org)提供全文下载. 

- 每个Record的网址为[http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2883744](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2883744) 或 [http://europepmc.org/articles/PMC2883744]([http://europepmc.org/articles/PMCID). 欧洲的分中心还提供别的选项,例如摘要啥的,例如[http://europepmc.org/abstract/MED/PMC2883744]([http://europepmc.org/articles/PMCID).
- 一般全文下载地址是[http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2883744/pdf](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2883744/pdf) 或 [http://europepmc.org/articles/PMC2883744?pdf=render]([http://europepmc.org/articles/PMCID?pdf=render). 实际NCBI提供的PMC pdf下载地址后面还是有个pdf文件名的,不过可以重定向~

PMCID都有PMID对应, 基本是PMID的子集. 和DOI的关系和上面一样啦, 基本有PMCID的都有DOI.

## MID: NIHMSID 和 EMSID

这两个ID是类似的, MS就是 **Manuscripts**的缩写, 就是提供的是作者手稿版而非正式出版的版本. NIHMSID主要是NIH提供的, EMSID就是欧洲那边提供的. MID可以说是统称吧.

- ID格式前者是`NIHMS数字串`, 后者往往是`UKMS数字串`, 两者数字串往往不一致! 如果一篇PMCID提供了MS的记录, 往往就是草稿版... 
- 他们对应的网址和PMC的差异在于多了个`mid/`, 例如 [http://www.ncbi.nlm.nih.gov/pmc/articles/mid/NIHMS198092](http://www.ncbi.nlm.nih.gov/pmc/articles/mid/NIHMS198092), 同理欧洲的也是.
- PDF对应地址始终使用PMCID对应的地址, 所以需要转换回去PMCID.

NIHMSID和EMSID都有对应的PMCID, 所以也会有对应的PMID咯.

## ID格式转换

### 在线转换: [PMID-PMCID-DOI-ManucriptID Converter](http://www.ncbi.nlm.nih.gov/pmc/pmctopmid/)

- 支持ID格式: 这个格式转换器可以转换PMID, PMCID, DOI, MID (NIHMSID或EMSID)
- 结果格式: 结果可以是HTML (缺省格式), XML, JSON, CSV格式~~很强大. JSON的话会在`['records'][num]['pmid']`这样.

可以进行**相同格式**的多个ID的转换, 最多一次200个. 每个结果要是json就是在`['records'][num]` 对应的num处.

### API: [ID-converter-API](http://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/)

这个API提供接口提供方便的转换, 主网址是[http://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/](http://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/)

- 像URL的GET接受查询, 所以格式就是`主网址?参数名=参数值&下一参数名=参数值`, 例如转换一个ID获取JSON格式: `http://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=10.1021/ml100016x&format=json`
- 搜索支持doi/pmid/pmcid/mid, 返回结果主要有PMID/PMCID/DOI. MID藏在`['versions']`里头(因为可能有多个MID)!
- 如果文章embargo, 就是还没能用要等一段时间后才可以, 结果里面会有`live="false" release-date=某个时间`. 如果文章有了草稿, 迟点还会有正式出版全文, 就会在version里面某个version出现上述属性.

#### 参数名

- ids: 可以使用doi/PMID/PMCID/MSID/PMC版本ID等. 如果想查询多个, 使用`,`分隔每个ID.
- format: 返回格式, xml(默认),html,json,csv 
- idtype: id类型, auto/pmid/pmcid/doi/mid. 一般不指定(默认auto)
- versions: 是否显示versions, yes或者no. 默认yes
更多介绍参看[官方](http://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/)吧.

## FTP服务

[官方介绍](http://www.ncbi.nlm.nih.gov/pmc/tools/ftp/), PMC的FTP地址: [ftp://ftp.ncbi.nlm.nih.gov/pub/pmc](ftp://ftp.ncbi.nlm.nih.gov/pub/pmc)

## [OA web service](http://www.ncbi.nlm.nih.gov/pmc/tools/oa-service/) 

用来查询PMC的FTP存放的API. 注意只针对Open Access的, 例如ACS的一些在PMC有的文献并不能从这里找到.

API网址: [http://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi](http://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi). 返回结果xml.

- 查询词 id=PMCID
- 返回record里头文件格式: format=pdf 过滤出pdf; 
- 上传日期过滤 from/until 日期格式from=2013-01-01+08:00:00 或者2013-01-01. 
- resumptionToken 最多出来1000个结果, 随后的需要使用resumptionToken 来翻页. 



------
