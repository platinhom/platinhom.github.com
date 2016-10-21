---
layout: post_py
title: Excel批量提取链接地址
date: 2015-07-27 21:44:55
categories: IT
tags: VB Excel
---

使用Alt+F11打开宏编辑器,新建一个module,输入以下内容,操作即可.

- 方法一: 使用指定range逐一迭代  
Offset(y,x) 返回的是该cell相应行和列的偏移后的对象.

~~~vb
Sub test()
For Each cell In Range("A2:A6")
cell.Offset(0, 1) = cell.Hyperlinks(1).Address
Next
End Sub
~~~

- 方法二: 使用所有Hyperlinks的集合来迭代.  
这里包括了直接编辑成markdown的格式.

~~~vb
Sub ExtractHL()
    Dim HL As Hyperlink
    For Each HL In ActiveSheet.Hyperlinks
        HL.Range.Offset(0, 2).Value = HL.Address
        HL.Range.Offset(0, 3).Value = "[" + HL.Range.Offset(0, 0).Value + "](" + HL.Address + ") : " + HL.Range.Offset(0, 1).Value
    Next
End Sub
~~~

- 方法三: 使用自定义函数  
例如以下在标准模块中定义出一个自定义函数GetURL, 在相应的excel格内输入 *=GetURL(A1)* 即可

~~~vb
Function GetURL(rng As Range) As String
    On Error Resume Next
    GetURL = rng.Hyperlinks(1).Address
End Function
~~~

------
