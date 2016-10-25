---
layout: post_py
title: VB基础-VBA篇
date: 2015-10-02 12:12:01
categories: Coding
tags: VB Excel
---

对象:  
Application, Workbook, Worksheet, Range  
层次:  
Application -> Workbooks集合-> Workbook -> Worksheets集合 -> Worksheet -> Range  

Alt+F11 调出VBA控制台VBE编辑器.

Set rng = Worksheets("Sheet1").Range("A1:B2")

## Workbook对象
Workbooks.Add 创建工作薄并返回
wb.Worksheets("Sheet1") 调用名为Sheet1的工作表

Visible 可见属性

## Worksheet对象

Name 工作表名
Range("A1:C3") 返回范围对象

## Range对象

Value="Hello" 值和显示内容
Font.Bold=True, Font.Size=19
Interior.Color=vbYellow (背景色)

Cells(row,column)

ActiveCell  
ActiveCell.Offset(1, 0).Activate 偏差函数,激活

Selection





## Reference

1. [完美Excel博客](http://www.excelperfect.com/index.php/category/excelprogram/)
2. [微软Excel VBA参考-对象模型](https://msdn.microsoft.com/zh-cn/library/ff821495.aspx)

------
