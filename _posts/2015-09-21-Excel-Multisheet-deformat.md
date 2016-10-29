---
layout: post_py
title: Excel多表格操作
date: 2015-09-21 12:04:58
categories: IT
tags: Excel
---

最近经常多表格进行操作, 每个表格是不同的数据保存. 例如为了节约空间便于交流, 需要去公式化. 一个一个表格全选, 选择性黏贴实在太麻烦了...两个方法:

## 利用多sheet操作

- 利用**shift**/**ctrl**键点击sheet可以进行多选操作. 
- 点当前的工作表中任意一格,然后**ctrl+A** 两次进行全选.
- 右键,选择性粘贴, 数值.(新版本可以右键直接看到选择粘贴数值的快捷方式). OK!全部被选的sheet均进行了如此操作.
- 补充复制到新工作薄: 新建一个工作薄并打开. 选择多sheet后, 右键Move or Copy(移动或复制), 再Cteate a copy(创建拷贝), 上面工作薄选择刚才新建的工作薄. OK, 复制过去了,然后按上面操作即可去格式化.

## 利用VBA

见如下代码.其实是利用`.Formula=.Value`部分. 针对工作薄知识多个循环罢了. 不过有以上方法..谁还这么干了..

~~~vb

Sub 只去除本工作表公式()

With ActiveSheet
.UsedRange.Formula = .UsedRange.Value
End With
End Sub

Sub 去除工作薄公式()

Dim s As Worksheet
   For Each s In ThisWorkbook.Sheets
      s.UsedRange.Formula = s.UsedRange.Value
   Next

End Sub

~~~


------
