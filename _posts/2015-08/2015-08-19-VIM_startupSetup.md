---
layout: post
title: VIM启动设置
date: 2015-08-19 11:26:55
categories: IT
tags: IDE
---

在`~/.vimrc`中编辑即可设置vim启动时的设置,也可以设置`/usr/share/vim/vim73/`内的文件. 也可以在vim里使用`:set ....`来设置. 

~~~vim
set backspace=indent,eol,start        " 使vi可以用退格键删除,默认不能删旧的.indent是指可以删除字段缩进,eol是可以通过退格键合并两行,start则是可以删除插入前的输入(bs)
set nocompatible        " 缺省vi兼容模式,不能用退格.设置为不兼容模式(cp)
set number        " 行号显示---
set ruler        " 底部的行号等显示
syntax on        " 语法高亮,clear可以临时清楚颜色,off则关闭
set showmatch    " 当输入一个左括号时自动匹配右括号
set whichwrap=>        " 默认时,右键不能转到下一行.ww可以开启自动折向下行.<>分别代表左右,=后是指定可以换行的.(ww)
set autoindent     " 开启自动缩进   (ai)
set smartindent    " 智能选择对齐方式,类似C语言.换行时自动学会缩进.
set tabstop=4    " 一个tab等于多少空格(ts)
set shiftwidth=4    " 自动缩进时缩进为4格(sw)
set expandtab    " 编辑时可以将tab替换为空格(et)
set cindent    " c缩进
set incsearch    " 很聪明的查找,输入一个字符马上自动匹配,而不是输入完再查找
set highlight    " 寻找时匹配高亮显示(hls)
set softtabstop
set nobackup    " 不备份(讨厌的~文件)
set cursorline    " 高亮当前行(青色)
filetype on    " 检测文件类型
set guioptions-=T " 关闭GUI版工具栏
set t_vb    " 当vim进行编辑时，如果命令错误，会发出一个响声，该设置去掉响声
set autowrite    " 自动保存
set autochdir    " 自动切换当前目录为当前文件所在的目录
set nowrapscan    " 关闭扫描到文件两端时重新搜索
set background=dark/light    " 设置背景颜色与syntax对应
colorscheme darkblue    " 配色方案,在/usr/share/vim/vim70/colors,还有如evening blue.vim, delek.vim, evening.vim, murphy.vim torte.vim, darkblue.vim, desert.vim, koehler.vim, pablo.vim, ron.vim, zellner.vim, default.vim, elflord.vim morning.vim, peachpuff.vim, shine.vim
~~~

~~~vim
" Only do this part when compiled with support for autocommands.
if has("autocmd")
    " Use filetype detection and file-based automatic indenting.
    filetype plugin indent on
    " Use actual tab chars in Makefiles.
    autocmd FileType make set tabstop=8 shiftwidth=8 softtabstop=0 noexpandtab
endif

" For everything else, use a tab width of 4 space chars.
set tabstop=4       " The width of a TAB is set to 4.
                    " Still it is a \t. It is just that
                    " Vim will interpret it to be having
                    " a width of 4.
set shiftwidth=4    " Indents will have a width of 4.
set softtabstop=4   " Sets the number of columns for a TAB.
set expandtab       " Expand TABs to spaces.
~~~



------