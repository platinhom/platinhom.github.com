---
layout: post
title: Project Page in Github Page
date: 2015-07-09 1:34:29
categories: IT
tags: Git Website
archive: true
---

It's very to create the web page for your new repository under your mainpage. Here, I record the procedure.

## Create a New Reposity

- You can easily create a new reposity in Github. At the left bottom corner of the main page of github, you can find your repositories. A "New reposity" button is there!
- Enter the name, describe your project, and choose whether create .gitingore file and license file. Then, create the new project.
- Copy the SSH address of your project, and `git clone git@github.com:username/projectname.git` clone the project with its address to local. It's not nessessary.

## Create a gh-pages branch
![](https://pages.github.com/images/create-branch@2x.png)

- The most easy way is to create the branch `gh-pages` online as the figure shown above. Enter the new name and github will remind you to create a new branch for it.
- You can also do that in command line by git: `git checkout --orphan gh-pages`, it will create a new branch without parent. If you want to create a blank branch only contains the project page, you can `git rm -rf .` to delete all the current files. I don't think it's nessesary indeed. It only need you to have a branch called `gh-pages`, that's enough. `git push -u origin gh-pages` to create your branch on remote.
- You can also change the default branch to gh-pages on repository setting. It will help you to change to gh-pages when you clone the repository.

## Create the page on gh-pages branch

- To create a simple index.html file online/on git is easy. But don't fancy.
- Use Jekyll! Yes, you can copy the jekyll needed files from your mainpage to the project page, such as _config.yml file, _layouts, _includes directory and even .gitignore CNAME 404.md files when you need. Because Jekyll need them to help you to convert markdown file to a page. If you don't copy these from your mainpage repository, the markdown file doesn't work at all!
- CSS/JS files don't need to be copied. Because the page can use them as its mainpage.
- Now you can visit `http://username.github.io/projectname` to visit the project page!

## Reference
1. [Creating Project Pages manually](https://help.github.com/articles/creating-project-pages-manually/)
2. [GitCafe-Project Page](https://help.gitcafe.com/manuals/help/pages-services#为项目创建-pages-服务)

> 本博文已合并到[Github相关总结](/1233/01/01/Github-related/#l2-project-gh-pages)中, 不再更新.

---
