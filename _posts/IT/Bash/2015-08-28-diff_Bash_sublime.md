---
layout: post
title: 查找文件差异的diff和工具
date: 2015-08-28 06:27:30
categories: IT
tags: Bash IDE
---

## diff命令

Compare files line by line.

-  -i  -\-ignore-case  Ignore case differences in file contents.
-  -\-ignore-file-name-case  Ignore case when comparing file names.
-  -\-no-ignore-file-name-case  Consider case when comparing file names.
-  -E  -\-ignore-tab-expansion  Ignore changes due to tab expansion.
-  -b  -\-ignore-space-change  Ignore changes in the amount of white space.
-  -w  -\-ignore-all-space  Ignore all white space.
-  -B  -\-ignore-blank-lines  Ignore changes whose lines are all blank.
-  -I RE  -\-ignore-matching-lines=RE  Ignore changes whose lines all match RE.
-  -\-strip-trailing-cr  Strip trailing carriage return on input.
-  -\-binary  Read and write data in binary mode.
-  -a  -\-text  Treat all files as text.
-  -c  -C NUM  --context[=NUM]  Output NUM (default 3) lines of copied context.
-  -u  -U NUM  --unified[=NUM]  Output NUM (default 3) lines of unified context.
-    -\-label LABEL  Use LABEL instead of file name.
-    -p  -\-show-c-function  Show which C function each change is in.
-    -F RE  -\-show-function-line=RE  Show the most recent line matching RE.
-  -q  -\-brief  Output only whether files differ.
-  -e  -\-ed  Output an ed script.
-  -\-normal  Output a normal diff.
-  -n  -\-rcs  Output an RCS format diff.
-  -y  -\-side-by-side  Output in two columns.
-    -W NUM  -\-width=NUM  Output at most NUM (default 130) print columns.
-    -\-left-column  Output only the left column of common lines.
-    -\-suppress-common-lines  Do not output common lines.
-  -D NAME  -\-ifdef=NAME  Output merged file to show `#ifdef NAME' diffs.
-  -\-GTYPE-group-format=GFMT  Similar, but format GTYPE input groups with GFMT.
-  -\-line-format=LFMT  Similar, but format all input lines with LFMT.
-  -\-LTYPE-line-format=LFMT  Similar, but format LTYPE input lines with LFMT.
    LTYPE is `old', `new', or `unchanged'.  GTYPE is LTYPE or `changed'.  
    GFMT may contain:  
      %<  lines from FILE1  
      %>  lines from FILE2  
      %=  lines common to FILE1 and FILE2  
      %[-][WIDTH][.[PREC]]{doxX}LETTER  printf-style spec for LETTER  
        LETTERs are as follows for new group, lower case for old group:  
          F  first line number  
          L  last line number  
          N  number of lines = L-F+1  
          E  F-1  
          M  L+1  
    LFMT may contain:  
      %L  contents of line  
      %l  contents of line, excluding any trailing newline  
      %[-][WIDTH][.[PREC]]{doxX}n  printf-style spec for input line number  
    Either GFMT or LFMT may contain:  
      %%  %  
      %c'C'  the single character C  
      %c'\OOO'  the character with octal code OOO  
-  -l  -\-paginate  Pass the output through `pr' to paginate it.
-  -t  -\-expand-tabs  Expand tabs to spaces in output.
-  -T  -\-initial-tab  Make tabs line up by prepending a tab.
-  -\-tabsize=NUM  Tab stops are every NUM (default 8) print columns.
-  -\-suppress-blank-empty  Suppress space or tab before empty output lines.
-  -r  -\-recursive  Recursively compare any subdirectories found.
-  -N  -\-new-file  Treat absent files as empty.
-  -\-unidirectional-new-file  Treat absent first files as empty.
-  -s  -\-report-identical-files  Report when two files are the same.
-  -x PAT  -\-exclude=PAT  Exclude files that match PAT.
-  -X FILE  -\-exclude-from=FILE  Exclude files that match any pattern in FILE.
-  -S FILE  -\-starting-file=FILE  Start with FILE when comparing directories.
-  -\-from-file=FILE1  Compare FILE1 to all operands.  FILE1 can be a directory.
-  -\-to-file=FILE2  Compare all operands to FILE2.  FILE2 can be a directory.
-  -\-horizon-lines=NUM  Keep NUM lines of the common prefix and suffix.
-  -d  -\-minimal  Try hard to find a smaller set of changes.
-  -\-speed-large-files  Assume large files and many scattered small changes.
-  -v  -\-version  Output version info.
-  -\-help  Output this help.

FILES are 'FILE1 FILE2' or 'DIR1 DIR2' or 'DIR FILE...' or `FILE... DIR'.
If --from-file or --to-file is given, there are no restrictions on FILES.
If a FILE is `-', read standard input.
Exit status is 0 if inputs are the same, 1 if different, 2 if trouble.

### 选项

### 结果

## Sublime插件

### [FileDiffs](https://github.com/colinta/SublimeFileDiffs)

- 特点: 免费, sublime版diff,支持外部diff工具. 缺点: 就真的是diff结果的显示..
- 用法: 
	1. 安装后, 调用处filediffs菜单:
		- 方法1: Ctrl+Shift+P调出指令框再输入filediffs找到filediffs: menus,点击即可
		- 方法2: 修改Key Bindings-User里面,增加新的key如下面列出所示,随后可以用快捷键ctrl+shift+d来进行.
	2. 随后会出现5个选项命令: 
		1. `file_diff_clipboard`: 是当前(文件/选择)和粘贴板比较
		2. `file_diff_saved`: 当前(文件/选择)状态和先前保存状态的差异
		3. `file_diff_file`: 当前(文件/选择)状态和Project类某文件的差异
		4. `file_diff_tab`: 当前(文件/选择)状态和当前某tab打开的文件的差异(我最常用)
		5. `file_diff_previous`: 当前(文件/选择)状态和先前处于活动状态的文件的差异(特殊的两tab比较)
		6. `file_diff_selections`: 先要选择两个区域,然后才会出现该选项.比较两个选择区域
	3. 使用相应命令后将生产untitled临时文件,储存diff结果.开始时告诉你---和+++代表什么文件,后面相应-,+着色对于相应文件.就这样了
	4. 外部程序: 通过Filediffs的default setting可以设置一些参数,例如可以取消注释掉某些行来启动外部另外一些diff程序,最好使用绝对路径(或者加入到/usr/local/bin/ 符号链接)

~~~css
	//filediffs
	{ "keys": ["ctrl+shift+d"], "command": "file_diff_menu" },
	{ "keys": ["ctrl+shift+e"], "command": "file_diff_menu", "args": {"cmd": ["opendiff", "$file1", "$file2"] } }
~~~

### [diffy](https://packagecontrol.io/packages/Diffy)

- 特点: 分屏差异化显示,缺点:不能同步两边进行文件拉动.
- 用法: 
	1. Alt+shift+2/1切换双视窗和单视窗(或者View->Layout->Column:2)
	2. 两个视窗各放置需要比较的文件(如果是复制内容新建一个临时文件就好了).
	3. ctrl+k, ctrl+d(Mac: super+k,super+d)进行比较,其实就是将差异之处列出来.
	4. ctrl+k, ctrl+c取消比较

------
