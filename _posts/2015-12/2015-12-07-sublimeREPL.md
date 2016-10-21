---
layout: post
title: SublimeREPL使用
date: 2015-12-07 00:46:30
categories: IT
tags: IDE
---

发现Anaconda并不好用...并不能真正运行并且显示出交互效果. 所以转着试试SublimeREPL, 一个支持多语言的IDLE.


![](/other/pic/blog-tmp/sublimeREPL-1.png)

> Packages/User/Default (OSX).sublime-keymap

~~~css
[
    { "keys": ["super+ctrl+m"], "command": "markdown_preview", "args": { "target": "browser"} },
    {"keys":["f5"],
        "caption": "SublimeREPL: Python - RUN current file",
        "command": "run_existing_window_command", "args":{
            "id": "repl_python_run",
            "file": "config/Python/Main.sublime-menu"
        }
    },
    {"keys":["f4"],
        "caption": "SublimeREPL: Python - IPython",
        "command": "run_existing_window_command", "args":{
            "id": "repl_python_ipython",
            "file": "config/Python/Main.sublime-menu"
        }
    }
]
~~~




------
