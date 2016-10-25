---
layout: post
title: Github:release发布版本
date: 2015-12-12 21:25:21
categories: IT
tags: Git
---

Creating Releases 创建发布包就是发布一个稳定合适供用户下载的版本. 一般项目都需要进行版本的发布.

-----

发布包是让用户接触项目不错的方式：

只有对项目具有写权限的管理用户才有发布或者查看draft草稿的权限.

1.页面顶端，点击你的用户名

![](https://help.github.com/assets/images/help/profile/top_right_avatar.png)

2.在你的 **profile**  页面，点击 **Repositories** 窗口，接着点击 **你的库** 的名称

![](https://help.github.com/assets/images/help/profile/profile_repositories_tab.png)

3.顶端，点击 **releases** (Commits/Branches/Releases/Contributor)

![](https://help.github.com/assets/images/help/releases/releases-header-menu.png)

4.再点击 **Draft a new release**

![](https://help.github.com/assets/images/help/releases/draft_release_button.png)

5.输入发布包的版本号。版本号基于 [Git 标签](http://git-scm.com/book/en/Git-Basics-Tagging),我们建议标签命名，符合[语义版本](http://semver.org/)。一般就是v1.0, v1.2.3这样, 或者对于测试版本, 可以像 v0.2-alpha 或者 v5.9-beta.3这样.

![](https://help.github.com/assets/images/help/releases/releases_tag_version.png)

6.选择发布版本基于哪个目标(分支和commit). 在`@ Target:` 处可以选择哪个branch分支, 甚至哪个commit. 选择合适的分支和commit的内容作为发布. 很重要。通常，你会想发布在你的主分支，除非你发布测试软件。

![](https://help.github.com/assets/images/help/releases/releases_tag_branch.png)

7.在你的发布包中输入标题和描述(大概介绍)

![](https://help.github.com/assets/images/help/releases/releases_description.png)

8.如果发布中包含二进制文件，托文件进二进制框中(适用于不方便发布源码的2进制文件)

![](https://help.github.com/assets/images/help/releases/releases_adding_binary.gif)


9.如果，发布包不稳定，选择`This is a pre-release` 来提醒用户这个是不能用于生产环境的

![](https://help.github.com/assets/images/help/releases/prerelease_checkbox.png)


10.如果准备好了发布了，点击 **Publish release**。另外, 点击 **Save draft** 用于保存在草稿箱中。只有你和你的合作者可以看到到草稿箱。

![](https://help.github.com/assets/images/help/releases/release_buttons.png)

11.现在, 用户就可以在release上选择release进行下载了! (zip/tar.gz进行库压缩的文件)

##Automatically creating releases 自动创建发布

 自动创建发布（支持命令行或者脚本），详见[Releases API documentation.](https://developer.github.com/v3/repos/releases/#create-a-release)

##Further reading 扩展阅读

* [链接到发布包](https://github.com/waylau/github-help/blob/master/Linking%20to%20releases%20%E9%93%BE%E6%8E%A5%E5%88%B0%E5%8F%91%E5%B8%83%E5%8C%85.md)



参考：[https://help.github.com/articles/creating-releases/](https://help.github.com/articles/creating-releases/)

------
