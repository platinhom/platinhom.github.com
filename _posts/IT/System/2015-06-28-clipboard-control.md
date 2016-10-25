---
layout: post
title: 剪贴板的命令行/代码操作
date: 2015-06-28 05:38:27
categories: IT
tags: System
---

## Window
`clip` system32里自带程序

- `dir | clip` 将命令结果重定向到剪贴板
- `clip <readme.txt` 将文件内容复制到剪贴板
- `echo |clip ` 清空剪贴板

## Mac
`pbcopy`和`pbpaste`

- `cat file | pbcopy` 复制内容到剪贴板
- `pbcopy < readme.txt` 将文件内容输入到剪贴板
- `echo 'Hello World!' | tee >(pbcopy) tmp.txt` 同时将输出到文件, 剪贴板, 屏幕
- `pbpaste` 黏贴

## Linux
需要安装`xsel`或者`xclip` 可能需要另装.

## Python

### import win32clipboard 剪贴板操作

- `win32clipboard.OpenClipboard()` 打开剪贴板
- `win32clipboard.EmptyClipboard()` 清空剪贴板内存
- `win32clipboard.SetClipboardData(win32con.CF_TEXT, "Hello World!")` 复制文本内容到剪贴板，系统后台会返回内存地址
- `wincb.GetClipboardData(win32con.CF_TEXT) ` 
- `win32clipboard.CloseClipboard()` 关闭剪贴板

### [Pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/)
需下载放到Lib内

- `pyperclip.getcb()`  获取clipboard值
- `pyperclip.setcb(text)`  设置clipboard值

---
