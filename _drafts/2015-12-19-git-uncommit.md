---
layout: post
title: Git:取消上次commit
date: 2015-12-19 09:40:32
categories: IT
tags: Git
---

~~~bash
$ git commit -m "Something terribly misguided"              (1)
$ git reset --soft HEAD~                                    (2)
<< edit files as necessary >>                               (3)
$ git add ...                                               (4)
$ git commit -c ORIG_HEAD                                   (5)
~~~

还可以使用alias

`git config --global alias.undo-commit 'reset --soft HEAD^'` Then just type `git undo-commit`

------
