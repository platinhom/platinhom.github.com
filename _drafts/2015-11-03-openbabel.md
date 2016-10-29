---
layout: post
title: openbabel
date: 2015-11-03 09:50:47
categories: CompCB
tags: CompChem
---

- `obabel -L` 列出插件, `obabel -L pluginName` 列出插件可用内容

babel主命令的使用.

babel -imol2 hi.mol2 -opdb hello.pdb

babel abc.sdf -O out.mol2 -m # 分割文件并转为mol2, 文件名为out1.mol2,out2.mol2

## Reference

1. [添加插件](http://open-babel.readthedocs.org/en/latest/WritePlugins/index.html)

------
