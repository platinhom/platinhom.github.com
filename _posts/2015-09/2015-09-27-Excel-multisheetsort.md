---
layout: post_py
title: Excel多表格进行同时排序
date: 2015-09-27 05:34:32
categories: IT
tags: Excel VB
---

多sheet选择的方法不能进行排序操作. 所有多个sheet进行排序要么一个一个按, 要么用宏.

在VIEW->Macros里面录制得单表格进行排序的宏,进行宏的编辑,然后加入循环即可. 这里将表面储存在CopyData的19列第四行起. 因此可以按快捷键后直接所有表格进行指定排序.

~~~vb

Sub Macro1()
'
' Macro1 Macro
' sort s3
'
' Keyboard Shortcut: Ctrl+k
'
Dim ws As String

For i = 1 To 16
	ws = ActiveWorkbook.Worksheets("CopyData").Cells(3 + i, 19).Value()
	'MsgBox (ws)
    Range("A1:DY671").Select
    Range("T9").Activate
    ActiveWorkbook.Worksheets(ws).Sort.SortFields.Clear
    ActiveWorkbook.Worksheets(ws).Sort.SortFields.Add Key:=Range("K2:K671") _
        , SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
    ActiveWorkbook.Worksheets(ws).Sort.SortFields.Add Key:=Range("E2:E671") _
        , SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
    ActiveWorkbook.Worksheets(ws).Sort.SortFields.Add Key:=Range("D2:D671") _
        , SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
    ActiveWorkbook.Worksheets(ws).Sort.SortFields.Add Key:=Range("B2:B671") _
        , SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
    With ActiveWorkbook.Worksheets(ws).Sort
        .SetRange Range("A1:DY671")
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With

Next i

End Sub

~~~


------
