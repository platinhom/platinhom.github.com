---
layout: post
title: SourceForge用于免费博客搭建(3)-脚本与动态网页
date: 2016-01-19 09:24:11
categories: IT
tags: Software Internet
---

前言再续又书接上两回: [SF的SSH-SCP-SFTP](/2016/01/17/sourceforge-for-freeblog.html)和[SF使用MySQL服务](/2016/01/18/sf-mysql.html), 最后是介绍SF的Web Services服务构建网页了~

动态网页功能是SF提供构建免费博客和项目主页的一大特色(虽然不是啥, 但是免费的提供服务的还能有啥哈?!), 支持多种语言, 支持用户主页和Project主页, 支持链接数据库, 一般支持使用开源第三方软件用于blog生产. 细节请参考以下官方三个文档(尤其第一个): 

1. [Project Web and Developer Web Server Configuration Details](https://sourceforge.net/p/forge/documentation/Project%20Web%20and%20Developer%20Web/)
2. [Developer Web Services](https://sourceforge.net/p/forge/documentation/Developer%20Web%20Services/)
3. [Project Web Services](https://sourceforge.net/p/forge/documentation/Project%20Web%20Services/)

----------

### 动态网页的语言支持以下脚本语言:

- PHP 5.3.2 under mod_php.
- Perl 5.8.8
- Python 2.4.3
- Ruby 1.8.7
- Tcl 8.4.13

### 文件读写

SF的文件系统有其独特特点, 和一般的系统的不同一致(一般就是User/Group/Other), 这里是 "project member", "project-initiated apache access" 以及 "everyone". 差异主要是: 
- 一般系统权限基本是基于用户为单位的, 而SF是基于Project为单位的, 所以一个Project文件夹所有项目成员都是等权限的(A创建, B也能删除). 所以用户部分替换为`project member`.
- 因为实际访问是通过Apache的, 所有用户的组都是Apache. 所以组是Apache的组, 也就是说所有用户都是Apache用户. 但是, 这个是`project-initiated`的, 就是说只有该项目的应用/文件才能通过apache来控制和修改文件, 不能跨项目(即虽然都是Apache组, 但B项目不能操控A项目的文件)
- SF的文件/文件夹权限不能设置为777, 最多就是775. 

更多参考参看: [Project Web Filesystem Permissions](https://sourceforge.net/p/forge/documentation/Project%20Web%20Filesystem%20Permissions/)

### Email系统

SF提供了EMail系统给project web用于发邮件给用户. 使用很简单, 详细可以参考 [Project Web Email Configuration](https://sourceforge.net/p/forge/documentation/Project%20Web%20Email/) .






------
