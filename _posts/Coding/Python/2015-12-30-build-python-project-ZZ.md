---
layout: post
title: 以正确的方式开源Python项目(ZZ)
date: 2015-12-30 07:49:08
categories: Coding
tags: Python ZZ
---

转载自 [开源中国翻译:以正确的方式开源Python项目](http://www.oschina.net/translate/open-sourcing-a-python-project-the-right-way), 原英文版Jeff Knupp博文[链接](原文链接：http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)

这是篇不错的介绍怎么构建一个开源Python项目的文章~转载之~~

--------------

> 大多数Python开发者至少都写过一个像工具、脚本、库或框架等对其他人也有用的工具。我写这篇文章的目的是让现有Python代码的开源过程尽可能清晰和无痛。我不是简单的指——“创建一个GitHub库，提交，在Reddit上发布，每天调用它”。在本文的结尾，你可以把现有的代码转换成一个能够鼓励他人使用和贡献的开源项目。  
然而每一个项目都是不同的，但其中将现有代码开源的流程对所有的Python项目都是类似的。在另一个受欢迎的文章系列里我写了“[以正确方式开始一个Django项目](http://www.jeffknupp.com/blog/2012/10/24/starting-a-django-14-project-the-right-way/)”，我将概述在开源Python项目我发现的有必要的步骤。   
**更新** (8月17号): 感谢@pydann提醒我[Cookiecutter](https://github.com/audreyr/cookiecutter-pypackage)的存在，@audreyr的一个不起的项目。我在文章结尾添加了其中的一段。看一下Audrey的项目吧！  
**更新 2** (8月18号)：感谢@ChristianHeimes（和其他人）关于ontox这一段。Christian也让我想起了PEP 440和其他一些都已实现很棒的改进建议。

-------------

## 工具和概念

特别是，我发现一些工具和概念十分有用或者说是必要的。下面我就会谈及这方面主题，包括需要运行的精确的命令和需要设置的配置值。其终极目标就是让整个流程简单明了。

1. 项目布局（目录结构）
1. setuptools 和 setup.py文件
1. [git](http://www.git-scm.com/)版本控制
1. [GitHub](https://github.com/) 项目管理  
GitHub的"Issues" 如下作用:  
	1. bug跟踪
	1. 请求新特性
	1. 计划好的新特性
	1. 发布或者版本管理
1. [git-flow](http://nvie.com/posts/a-successful-git-branching-model/) git工作流
1. [py.test](http://pytest.org/latest/) 单元测试
1. [tox](http://tox.readthedocs.org/en/latest/) 标准化测试
1. [Sphinx](http://www.sphinx-doc.org/en/stable/) 自动生成HTML文档
1. [TravisCI](https://travis-ci.org/) 持续测试集成
1. [ReadTheDocs](https://readthedocs.org/) 持续文档集成
1. [Cookiecutter](https://github.com/audreyr/cookiecutter-pypackage)  为开始下一个项目自动生成这些步骤

## 项目布局

当准备一个项目时，正确合理的布局（目录结构）是十分重要的。一个合理的布局意味着想参与开发者不必花时间来寻找某些代码的位置; 凭直觉就可以找到文件的位置。因为我们在处理一个项目，就意味着可能需要到处移动一些东西。  

让我们从顶层开始。大多数项目都有很多顶层文件（如setup.py, README.md, requirements等等）。每个项目至少应该有下面三个目录：

1. doc目录，包括项目文档
1. 项目目录，以项目命名，存储实际的Python包
1. test目录，包含下面两部分
	1. 在这个目录下包括了测试代码和资源
	2. 作为一个独立顶级包

为了更好理解文件该如何组织，这里是一个我的简单项目：[sandman](https://github.com/jeffknupp/sandman) 布局快照。

~~~bash
$ pwd
~/code/sandman
$ tree
.
|- LICENSE
|- README.md
|- TODO.md
|- docs
|   |-- conf.py
|   |-- generated
|   |-- index.rst
|   |-- installation.rst
|   |-- modules.rst
|   |-- quickstart.rst
|   |-- sandman.rst
|- requirements.txt
|- sandman
|   |-- __init__.py
|   |-- exception.py
|   |-- model.py
|   |-- sandman.py
|   |-- test
|       |-- models.py
|       |-- test_sandman.py
|- setup.py
~~~

如你所看到那样，这里有一些顶层文件，一个docs目录（建立一个空目录，因为sphinx会将生成的文档放到这里），一个sandman目录，以及一个在sandman目录下的test目录。

## setuptools 和 setup.py文件

setup.py文件，你可能已经在其它包中看到过，被distuils包用来安装Python包的。对于任何一个项目，它都是一个很重要的文件，因为它包含了版本，包依赖信息，PyPi需要的项目描述，你的名字和联系信息，以及其它一些信息。它允许以编程的方式搜索安装包，提供元数据和指令说明让工具如何做。

setuptools包（实际上就是对distutils的增强）简单化了建立发布python包。使用setuptools给python包打包，和distutils打包没什么区别。这实在是没有任何理由不使用它。

setup.py应该放在你的项目的根目录。setup.py中最重要的一部分就是调用setuptools.setup，这里面包含了此包所需的所有元信息。这里就是sandman的setup.py的所有内容

~~~python
from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys
 
import sandman
 
here = os.path.abspath(os.path.dirname(__file__))
 
def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)
 
long_description = read('README.txt', 'CHANGES.txt')
 
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
 
    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)
 
setup(
    name='sandman',
    version=sandman.__version__,
    url='http://github.com/jeffknupp/sandman/',
    license='Apache Software License',
    author='Jeff Knupp',
    tests_require=['pytest'],
    install_requires=['Flask>=0.10.1',
                    'Flask-SQLAlchemy>=1.0',
                    'SQLAlchemy==0.8.2',
                    ],
    cmdclass={'test': PyTest},
    author_email='jeff@jeffknupp.com',
    description='Automated REST APIs for existing database-driven systems',
    long_description=long_description,
    packages=['sandman'],
    include_package_data=True,
    platforms='any',
    test_suite='sandman.test.test_sandman',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
~~~

（感谢Christian Heimes的建议让setup.py更符合人们的语言习惯。反过来，也让我借用其它的项目一目了然了。)

大多数内容浅显易懂，可以从setuptools文档查看到，所以我只会触及"有趣"的部分。使用`sandman.__version__`和`gettinglong_description`方法（尽管我也记不住是哪一个，但是却可以从其它项目的setup.py中获得）来减少我们需要写的引用代码。相反，维护项目的版本有三个地方(setup.py, 包自身的`__version__`， 以及文档)，我们也可以使用包的version来填充setup里面的version参数

`long_description`被Pypi在你项目的PyPI主页当做文档使用。这里有其他一个文件，README.md，其中包含几乎相同的内容，我使用[pandoc](http://pandoc.org/)依据`README.md`自动生成README.rst，因此我们只需看`README.rst`就行了，并将它的内容设置为`long_description`。

py.test (上面讨论过) 中有一个特殊的条目（pytest类）设置允许Python检查setup.py可否正常工作。这段代码直接来自py.test指导文档。

文件中的其他内容都是在设置文档中描述的安装参数。

#### 其他的setup.py参数
有一些sandman 用不到的启动参数，在你的包里可能会用到。举个例子，你可能正在分派一些脚本并希望你的用户能够从命令行执行。在这个例子中，脚本会和你其他的代码一起安装在正常的site-packages位置。用户安装完后，没有其他的简单方法运行它。基于这一点，setup可以带有一个的脚本参数来指明Python脚本应该如何安装。在包中安装一个调用go_foo.py的脚本，这个用来启动的调用包括下面这行：

~~~python
scripts = ['go_foo.py'],
~~~

确保在脚本中填入相对路径，并不仅仅是一个名称 (如scripts = ['scripts/foo_scripts/go_foo.py']).同样，你的脚本应该以"shebang"行和"python"开始，如下：

~~~python
#! /usr/bin/env python
~~~

distutils将会在安装过程中自动用当前解释器位置取代这一行。  
如果你的包比我们这里讨论的要复杂，你可在官方文档中参看[启动工具文档](https://pythonhosted.org/setuptools/setuptools.html)和[发布python模块](https://docs.python.org/2/distutils/index.html)。  
在这两者中，你可以解决一些你可能会遇到的问题。

## 代码管理：git， 项目管理：gitHub

在“以正确的方式开始一个Django项目”中，我建议版本控制使用git 或者 mercurial。如果对于以共享与贡献的项目来说，只有一个选择：git。事实上，从长远来说，如果你想人们能使用和参与贡献，那么不仅使用git很有必要，而且，你也能够使用GitHub来管理维护你的项目。

这并不是夸大其词（尽管很多人会以它为嚼头）。然而，管它好与差，git和GitHub事实上已经成为了开源项目的实际标准了。GitHub是很多潜在的贡献者最想注册的和最熟悉的。所以，我深信，这并不是掉以轻心，而是深思熟虑的产物。

#### 新建一个README.md文件
在GitHub的代码仓库中，项目的描述是从项目的根目录中的:README.md文件获取的。这个文件应该包含下面几点：

- 项目描述
- 项目ReadTheDocs页面连接[@Lesus 注：请查看 工具与概念 ]
- 一个用来显示当前构建状态的TravisCI按钮。
- "Quickstart" 文档 (怎么快速安装和使用你的项目)
- 若有非python依赖包，请列举它以及怎么安装它

它(README)读起来很傻的感觉，但是确是一个很重要的文件。它可能是你未来的用户或者贡献者首先从它了解你的项目的。花些时间来写一个清楚明白的说明和使用GFM（GitHubFlavoredMarkdown）来使它更好看。实际上，如果使用原生的Markdown来写文档不爽，那么可以在Github上使用立即预览来创建或者修改这个文件.

我们还没触及列表中的第二和第三项（ReadTheDocs和TravisCI），你会在接下来看到。

#### 使用"Issues"页
跟生活中的很多事情一样，你投入GitHub越多，你收获的越多。因为用户会使用GitHub的“Issues”页面反馈bug，使用该页面跟踪特性要求和改进是很有意义的。

更重要的是，它允许贡献者以一种优雅的方式看到：一个可能实现特性的列表以及自动化的管理合并请求流程（pull request）。GitHub的issues可以与评论、你项目里的其他issues及其他项目里的issues等交织，这使得“issues”页面成为一个有关所有bug修复、改进和新特性要求信息汇总的地方。

确保“Issues”及时更新，至少及时回应新的问题。作为一个贡献者，没有什么比修复bug后看着它呈现在issues页面并等待着被合并更有吸引力的了。

## 使用git-flow这个明智的git工作流

为使事情对自己和贡献者更容易，我建议使用非常流行的[git-flow分支模型](http://nvie.com/posts/a-successful-git-branching-model/)。

#### 概述
开发分支是你工作的主要分支，它也是将成为下一个release.feature的分支，代表着即将实现的新特性和尚未部署的修复内容（一个完整的功能分支有开发分支合并而来）。通过release的创建更新master。

#### 安装
按照你系统平台的git-flow安装指导操作，[在这里](https://github.com/nvie/gitflow/wiki/Installation)。

安装完后，你可以使用下附命令迁移你的已有项目

~~~bash
$ git flow init
~~~

#### Branch细节
脚本将询问你一些配置问题，git-flow的默认建议值可以很好的工作。你可能会注意到你的默认分支被设置成develop。现在，让我们后头描述一下git-flow…嗯，flow，更详细一点。这样做的最简单的方法是讨论一下不同的分支及模型中的分支类型。

#### Master
master分支一直是存放“生产就绪”的代码。所有的提交都不应该提交到master分支上。当然，master分支上的代码只会从一个产品发布分支创建并结束后合并进来。这样在master上的代码一直是可以发布为产品的。并且，master也是一直处于可预计的状态，所以你永远不需要担心如果master分支修改了而某一个其他分支没有相应的修改。

#### Develop
你的大部分工作是在develop分支上完成的。这个分支包含所有的完成的特性和修改的bug以便发布；每日构建或者持续集成服务器需要针对develop分支来进行，因为它代表着将会被包含在下一个发布里的代码。  
对于一次性的提交，可以随便提交到develop上。

#### 特性
对于一些大的特性，就需要创建一个特性分支。特性分支从develop分支创建出来。它们可以是对于下一个发布的一些小小的增强或者更进一步的修改。而这，依然需要从现在开始工作。为了从一个新的分支上开始工作，使用：

~~~bash
$ git flow feature start <feature name>
~~~

这命令创建了一个新的分支：feature/<feature name>。通常会把代码提交到这个分支。当特性已经完成并且准备好发布的时候，它就应当用一下的命令将它合并会develop分支：

~~~bash
$ git flow feature finish <feature name>
~~~

这会把代码合并进develop分支，并且删除 `feature/<feature name>`分支

#### Release
一个release分支是当你准备好进行产品发布的时候从develop分支创建出来的。使用以下的命令来创建：

~~~bash
$ git flow release start <release number>
~~~

注意，这是发布版本号第一次创建。所有完成的，准备好发布的分支必须已经合并到develop分支上。在release分支创建后，发布你的代码。任何小的bug修改需要提交到 release/<release number>分支上。当所有的bug被修复之后，运行以下的命令：

~~~bash
$ git flow release finish <release number>
~~~

这个命令会把你的release/<release number> 分支合并到master和develop分支，这意味着你永远不需要担心这几个分支会缺少一些必要的产品变更（可能是因为一个快速的bug修复导致的）。

### Hotfix

然而hotfix分支可能会很有用，在现实世界中很少使用，至少我是这样认为的。hotfix就像master分支下创建的feature分支： 如果你已经关闭了release分支，但是之后又认识到还有一些很重要的东西需要一起发布，那么就在master分支（由$git flow release finish <release number>创建的标签）下创建一个hotfix分支，就像这样：

~~~bash
$ git flow hotfix start <release number>
~~~
当你完成改变和增加你的版本号使之独一无二(bump your version number)，然后完成hotfix分支： 

~~~bash
$ git flow hotfix finish <release number>
~~~

这好像一个release分支（因为它本质上就是一种release分支），会在master和develop分支上提交修改。

我猜想它们很少使用的原因是因为已经存在一种可以给已发布的代码做出修改的机制：提交到一个未完成的release分支。当然，可能一开始，团队使用git flow release finish .. 太早了，然后第二天又发现需要快速修改。随着时间的推移，他们就会为一个release 分支多留一些时间，所以，不会再需要hotfix分支。另一种需要hotfix分支情况就是如果你立即需要在产品中加入新的特性，等不及在develop分支中加入改变。不过（期望）这些都是小概率事件。

## virtualenv和virtualenvwrapper

lan Bicking的virtualenv工具事实上已经成为了隔离Python环境的标准途径了。它的目标很简单：如果你的一台机子中有很多Python项目，每个都有不同的依赖（可能相同的包，但是依赖不同的版本），仅仅在一个Python安装环境中管理这些依赖几乎是不可能的。
virtualenv创建了一个“虚拟的”Python安装环境，每个环境都是相互隔离的，都有自己的site-packages, distribute和 使用pip安装包到虚拟环境而不是系统Python安装环境。 而且在你的虚拟环境中来回切换只是一个命令的事。

Doug Hellmann的virtualenvwrapper使创建和管理多个虚拟环境更容易的隔离工具。让我们继续前进，马上安装这两个工具：

~~~bash
$ pip install `virtualenvwrapper`
...
Successfully installed `virtualenvwrapper` `virtualenv` `virtualenv`-clone stevedore
Cleaning up...
~~~

如你所见，后者依赖于前者，所以简单的安装virtualenvwrapper就足够了。注意，如果你使用的是Python3，[PEP-405](https://www.python.org/dev/peps/pep-0405/)通过venv包和pyvenv命令提供了Python原生虚拟环境的支持，在python3.3中已实现。你应该使用这个而不是前面提到的工具。

一旦你安装了virtualenvwrapper，你需要添加一行内容到你的.zhsrc文件(对bash用户来说是.bashrc文件)：

~~~bash
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.zshrc
~~~

这样在你的shell中增加了一些有用的命令（记得第一次使用时source一下你的.zshrc文件以使它生效）。虽然你可以使用mkvirtualenv命令直接创建一个virtualenv，但使用mkproject [OPTIONS] DEST_DIR创建一个“项目”将更有用。因为我们已经有一个现有的项目了，所有我们只需为我们的项目创建一个新的virtualenv，下附命令可以达到这效果：

~~~bash
$ mkvirtualenv ossproject
 
New python executable in ossproject/bin/python
Installing setuptools............done.
Installing pip...............done.
(ossproject)$
~~~
你会注意到你的shell提示符在你的virtualenv之后（我的是“ossproject”，你可以使用任何你喜欢的名字）。现在任何通过pip安装的模块将安装到你的virtualenv下的site-packages。  

要停止在你的项目上工作并切换回系统使用deactivate命令。你会看到命令提示符前你的virtualenv名字消失了。要重新回到你的项目上工作的话运行workon <project name>，你会回到你的virtualenv。

## 使用py.test测试

在Python的自动测试系统里有两个主要的Python标准单元测试包（很有用）的替代品：nose和py.test。两个方案都将单元测试拓展的易于使用且增加额外的功能。说真的，哪个都是很好的选择。我更喜欢py.test因为下述几个原因：

- 支持setuptools/distutils项目
	- Python的setup.py测试技能始终其作用
- 支持常见的断言（assert）语法 (而不是需要记住所有jUnit风格的断言函数)
- 更少的样板
- 支持多种测试风格
	- 单元测试
	- 文档测试
	- nose测试

##### 注意
如果你已经有了一个自动测试的解决方案那继续使用它吧，跳过这一节。但请记住以后的章节你将被认为在使用py.test测试，这可能会影响到配置值。

#### 测试安装
在测试目录里，无论你如何决定都要有这个目录，创建一个名为`test_<project_name>.py`的文件。py.test的测试发现机制将把所有test_前缀的文件当做测试文件处理（除非明确告知）。

在这个文件里放什么很大程度上取决于你。写测试是一个很大的话题，超出这篇文章的范围。最重要的，测试对你的和潜在的捐助者都是有用的。应该标识清楚每个用例是测试的什么函数。用例应该以相同的“风格”书写，这样潜在的贡献者不必猜测在你的项目中他/她应该使用三种测试风格中的哪种。

#### 覆盖测试
自动化测试的覆盖率是一个有争议的话题。一些人认为它给出了错误的保证是一个毫无意义的度量，其他人认为它很有用。在我看在，我建议如果你已经使用自动化测试但从来没有检查过你的测试覆盖率，现在做这样一个练习。
使用py.test，我们可以使用Ned Batchelder的覆盖测试工具。使用pip安装pytest-cov。如果你之前这样运行你的测试：

`$ py.test`

你可以通过传递一些新的标识生成覆盖率报告，下面是运行sandman的一个例子：

~~~bash
$ py.test --cov=path/to/package
$ py.test --cov=path/to/package --cov-report=term --cov-report=html
====================================================== test session starts =======================================================
platform darwin -- Python 2.7.5 -- pytest-2.3.5
plugins: cov
collected 23 items
 
sandman/test/test_sandman.py .......................
---------------------------------------- coverage: platform darwin, python 2.7.5-final-0 -----------------------------------------
Name                           Stmts   Miss  Cover
--------------------------------------------------
sandman/__init__                   5      0   100%
sandman/exception                 10      0   100%
sandman/model                     48      0   100%
sandman/sandman                  142      0   100%
sandman/test/__init__              0      0   100%
sandman/test/models               29      0   100%
sandman/test/test_sandman        114      0   100%
--------------------------------------------------
TOTAL                            348      0   100%
Coverage HTML written to dir htmlcov
 
=================================================== 23 passed in 1.14 seconds ===========================================================
~~~

当然不是所有项目都有100%的测试覆盖率（事实上，正如你读到的，sandman没有100%覆盖），但获得100%的覆盖率是一个有用的练习。它能够揭示我之前没有留意的缺陷与重构机会。

因为，作为测试本身，自动生成的测试覆盖报可以作为你持续集成的一部分。如果你选择这样做，部署一个标记来显示当前的测试覆盖率会为你的项目增加透明度（大多数时候会极大的鼓励他人贡献）。

## 使用Tox进行标准化测试

一个所有Python项目维护者都需要面对的问题是兼容性。如果你的目标是同时支持Python 2.x和Python 3.x（如果你目前只支持Python 2.x，应该这样做），实际中你如何确保你的项目支持你所说的所有版本呢？毕竟，当你运行测试时，你只使用特定的版本环境来运行测试，它很可能在Python2.7.5中运行良好但在Python 2.6和3.3出现问题。

幸运的是有一个工具致力于解决这个问题。tox提供了“Python的标准化测试”，它不仅仅是在多个版本环境中运行你的测试。它创造了一个完整的沙箱环境，在这个环境中你的包和需求被安装和测试。如果你做了更改在测试时没有异常，但意外地影响了安装，使用Tox你会发现这类问题。

通过一个.ini文件配置tox：tox.ini。它是一个很容易配置的文件，下面是从tox文档中摘出来的一个最小化配置的tox.ini：

~~~bash
# content of: tox.ini , put in same dir as setup.py
[tox]
envlist = py26,py27
[testenv]
deps=pytest       # install pytest in the venvs
commands=py.test  # or 'nosetests' or ...
~~~

通过设置envlist为py26和py27，tox知道需要在这两种版本环境下运行测试。tox大约支持十几个“默认”的环境沙箱，包括jython和pypy。tox这个强大的工具使用不同的版本进行测试，在不支持多版本时可配置警示。

deps是你的包依赖列表。你甚至可以让tox从PyPI地址安装所有或一些你依赖包。显然，相当多的想法和工作已融入了项目。
实际在你的所有环境下运行测试现在只需要四个按键：

`$ tox`

## 一个更复杂的设置

我的书——“[写地道的Python](http://www.jeffknupp.com/writing-idiomatic-python-ebook/)”，实际上写的是一系列的Python模块和代码。这样做是为了确保所有的示例代码按预期工作。作为我的构建过程的一部分，我运行tox来确保任何新的语法代码能正常运行。我偶尔也看看我的测试覆盖率，以确保没有语法在测试中被无意跳过。因此，我的tox.ini比上面的复杂一些，一起来看一看：

~~~bash
[tox]
envlist=py27, py34
 
[testenv]
deps=
    pytest
    coverage
    pytest-cov
setenv=
    PYTHONWARNINGS=all
 
[pytest]
adopts=--doctest-modules
python_files=*.py
python_functions=test_
norecursedirs=.tox .git
 
[testenv:py27]
commands=
    py.test --doctest-module
 
[testenv:py34]
commands=
    py.test --doctest-module
 
[testenv:py27verbose]
basepython=python
commands=
    py.test --doctest-module --cov=. --cov-report term
 
[testenv:py34verbose]
basepython=python3.4
commands=
    py.test --doctest-module --cov=. --cov-report term
~~~

这个配置文件依旧比较简单。而结果呢？

~~~bash
(idiom)~/c/g/idiom git:master >>> tox
GLOB sdist-make: /home/jeff/code/github_code/idiom/setup.py
py27 inst-nodeps: /home/jeff/code/github_code/idiom/.tox/dist/Writing Idiomatic Python-1.0.zip
py27 runtests: commands[0] | py.test --doctest-module
/home/jeff/code/github_code/idiom/.tox/py27/lib/python2.7/site-packages/_pytest/assertion/oldinterpret.py:3: DeprecationWarning: The compiler package is deprecated and removed in Python 3.x.
from compiler import parse, ast, pycodegen
=============================================================== test session starts ================================================================
platform linux2 -- Python 2.7.5 -- pytest-2.3.5
plugins: cov
collected 150 items
...
============================================================ 150 passed in 0.44 seconds ============================================================
py33 inst-nodeps: /home/jeff/code/github_code/idiom/.tox/dist/Writing Idiomatic Python-1.0.zip
py33 runtests: commands[0] | py.test --doctest-module
=============================================================== test session starts ================================================================
platform linux -- Python 3.3.2 -- pytest-2.3.5
plugins: cov
collected 150 items
...
============================================================ 150 passed in 0.62 seconds ============================================================
_____________________________________________________________________ summary ______________________________________________________________________
py27: commands succeeded
py33: commands succeeded
congratulations :)
~~~

（我从输出列表里截取了一部分）。如果想看我的测试对一个环境的覆盖率，只需运行：

~~~bash
$ tox -e py33verbose
-------------------------------------------------- coverage: platform linux, python 3.3.2-final-0 --------------------------------------------------
Name                                                                                           Stmts   Miss  Cover
------------------------------------------------------------------------------------------------------------------
control_structures_and_functions/a_if_statement/if_statement_multiple_lines                       11      0   100%
control_structures_and_functions/a_if_statement/if_statement_repeating_variable_name              10      0   100%
control_structures_and_functions/a_if_statement/make_use_of_pythons_truthiness                    20      3    85%
control_structures_and_functions/b_for_loop/enumerate                                             10      0   100%
control_structures_and_functions/b_for_loop/in_statement                                          10      0   100%
control_structures_and_functions/b_for_loop/use_else_to_determine_when_break_not_hit              31      0   100%
control_structures_and_functions/functions/2only/2only_use_print_as_function                       4      0   100%
control_structures_and_functions/functions/avoid_list_dict_as_default_value                       22      0   100%
control_structures_and_functions/functions/use_args_and_kwargs_to_accept_arbitrary_arguments      39     31    21%
control_structures_and_functions/zexceptions/aaa_dont_fear_exceptions                              0      0   100%
control_structures_and_functions/zexceptions/aab_eafp                                             22      2    91%
control_structures_and_functions/zexceptions/avoid_swallowing_exceptions                          17     12    29%
general_advice/dont_reinvent_the_wheel/pypi                                                        0      0   100%
general_advice/dont_reinvent_the_wheel/standard_library                                            0      0   100%
general_advice/modules_of_note/itertools                                                           0      0   100%
general_advice/modules_of_note/working_with_file_paths                                            39      1    97%
general_advice/testing/choose_a_testing_tool                                                       0      0   100%
general_advice/testing/separate_tests_from_code                                                    0      0   100%
general_advice/testing/unit_test_your_code                                                         1      0   100%
organizing_your_code/aa_formatting/constants                                                      16      0   100%
organizing_your_code/aa_formatting/formatting                                                      0      0   100%
organizing_your_code/aa_formatting/multiple_statements_single_line                                17      0   100%
organizing_your_code/documentation/follow_pep257                                                   6      2    67%
organizing_your_code/documentation/use_inline_documentation_sparingly                             13      1    92%
organizing_your_code/documentation/what_not_how                                                   24      0   100%
organizing_your_code/imports/arrange_imports_in_a_standard_order                                   4      0   100%
organizing_your_code/imports/avoid_relative_imports                                                4      0   100%
organizing_your_code/imports/do_not_import_from_asterisk                                           4      0   100%
organizing_your_code/modules_and_packages/use_modules_where_other_languages_use_object             0      0   100%
organizing_your_code/scripts/if_name                                                              22      0   100%
organizing_your_code/scripts/return_with_sys_exit                                                 32      2    94%
working_with_data/aa_variables/temporary_variables                                                12      0   100%
working_with_data/ab_strings/chain_string_functions                                               10      0   100%
working_with_data/ab_strings/string_join                                                          10      0   100%
working_with_data/ab_strings/use_format_function                                                  18      0   100%
working_with_data/b_lists/2only/2only_prefer_xrange_to_range                                      14     14     0%
working_with_data/b_lists/3only/3only_unpacking_rest                                              16      0   100%
working_with_data/b_lists/list_comprehensions                                                     13      0   100%
working_with_data/ca_dictionaries/dict_dispatch                                                   23      0   100%
working_with_data/ca_dictionaries/dict_get_default                                                10      1    90%
working_with_data/ca_dictionaries/dictionary_comprehensions                                       21      0   100%
working_with_data/cb_sets/make_use_of_mathematical_set_operations                                 25      0   100%
working_with_data/cb_sets/set_comprehensions                                                      12      0   100%
working_with_data/cb_sets/use_sets_to_remove_duplicates                                           34      6    82%
working_with_data/cc_tuples/named_tuples                                                          26      0   100%
working_with_data/cc_tuples/tuple_underscore                                                      15      0   100%
working_with_data/cc_tuples/tuples                                                                12      0   100%
working_with_data/classes/2only/2only_prepend_private_data_with_underscore                        43     43     0%
working_with_data/classes/2only/2only_use_str_for_human_readable_class_representation             18     18     0%
working_with_data/classes/3only/3only_prepend_private_data_with_underscore                        45      2    96%
working_with_data/classes/3only/3only_use_str_for_human_readable_class_representation             18      0   100%
working_with_data/context_managers/context_managers                                               16      7    56%
working_with_data/generators/use_generator_expression_for_iteration                               16      0   100%
working_with_data/generators/use_generators_to_lazily_load_sequences                              44      1    98%
------------------------------------------------------------------------------------------------------------------
TOTAL                                                                                            849    146    83%
 
============================================================ 150 passed in 1.73 seconds ============================================================
_____________________________________________________________________ summary ______________________________________________________________________
py33verbose: commands succeeded
congratulations :)
~~~

结果很可怕啊。

### setuptools整合

tox可以和setuptools整合，这样python的setup.py测试可以运行你的tox测试。将下面的代码段放到你的setup.py文件里，这段代码是直接从tox的文档里拿来的：

~~~python
from setuptools.command.test import test as TestCommand
import sys
 
class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)
 
setup(
    #...,
    tests_require=['tox'],
    cmdclass = {'test': Tox},
    )
~~~
现在Python的setup.py测试将下载tox并运行它。真的很酷并且很节省时间。

## Sphinx文档生成器

Sphinx是由pocoo团队开发的工具[@Lesus 注：pocoo团队开发了很多优秀的产品：如Flask, Jinja2等等]。它已经用来生成Python官方文档和大多数流行的Python包的文档。它以更容易的方式从Python代码中自动产生Python文档。

#### 使用它完成工作
Sphinx不用了解Python程序以及怎样从它们中提取出来。它只能翻译reStructuredText文件，也就意味着你的代码文档的reStructuredText译文需要让Sphinx知道才能工作，但是管理维护所有的.py文件[至少是函数和类的部分]的reStructuredText译文显然是不可行的。

幸运的是，Sphinx有一个类似javadoc的扩展，叫做autodoc,可以用来从你的代码文档中萃取出reStructuredText。为了能够充分利用Sphinx和autodoc的能力，你需要已一种特别的方式格式化你的文档。特别是，你需要使用Sphinx的Python指令时。这里就是使用reStructuredText指令来为一个函数生成文档，使输出结果的HTML文档更漂亮：

~~~python
def _validate(cls, method, resource=None):
"""Return ``True`` if the the given *cls* supports the HTTP *method* found
on the incoming HTTP request.
 
:param cls: class associated with the request's endpoint
:type cls: :class:`sandman.model.Model` instance
:param string method: HTTP method of incoming request
:param resource: *cls* instance associated with the request
:type resource: :class:`sandman.model.Model` or None
:rtype: bool
 
"""
if not method in cls.__methods__:
    return False
 
class_validator_name = 'validate_' + method
 
if hasattr(cls, class_validator_name):
    class_validator = getattr(cls, class_validator_name)
    return class_validator(resource)
 
return True
~~~

文档需要花费一点功夫，但是为了你的使用者，这个付出是值得的。好吧，好的文档使一个可用的项目去其糟粕。

Sphinx的autodoc扩展让我们可以使用很多指令，而这些指令可以自动的从你文档中生成文档。

#### 安装
确认将Sphinx安装在你的virtualenv内，因为文档在项目里也是按版本来的。Sphinx不同的版本可能会产生不同的HTML输出。通过将其安装在你的virtualenv内，你可以以受控的方式升级你的文档。

我们要保持我们的文档在docs文件夹，将文档生成到docs/generated文件夹。在项目的根目录运行以下命令将根据你的文档字符自动重构文本文档：

`$ sphinx-apidoc -F -o docs <package name>`

这将产生一个包含多个文档文件的docs文件夹。此外，它创建了一个叫conf.py的文件，它将负责你的文档配置。你还会发现一个Makefile，方便使用一个命令（生成html）构建HTML文档。

在你最终生成文档之前，确保你已经在本地安装了相应的包（尽管可以使用pip，但python setup.py develop是最简单的保持更新的方法），否则sphinx-apidoc无法找到你的包。

#### 配置:conf.py
conf.py文件创建用来控制产生的文档的各个方面。它自己会很好生成文档，所以我只简单地触及两点。

##### 版本和发布

首先，确保你的版本和发布版本号保持最新。这些数字会作为生成的文档的一部分显示，所以你不希望它们远离了实际值。

保持你的版本最新的最简单方式就是在你的文档和setup.py文件中都从你的包的`__version__`属性读取。我从Flask的conf.py借用过来配置sandman的conf.py：

~~~python
import pkg_resources
try:
    release = pkg_resources.get_distribution('sandman').version
except pkg_resources.DistributionNotFound:
    print 'To build the documentation, The distribution information of sandman'
    print 'Has to be available.  Either install the package into your'
    print 'development environment or run "setup.py develop" to setup the'
    print 'metadata.  A virtualenv is recommended!'
    sys.exit(1)
del pkg_resources
 
version = '.'.join(release.split('.')[:2])
~~~

这就是说，为了让文档产生正确的版本号，你只需在你的项目的虚拟环境中简单的需要运行$python setup.py develop即可。现在你只需担心保持`__version__`为最新，因为setup.py会使用它。

##### html_theme 

考虑到更改default到html_theme，我更喜欢原生态的东西，显然这是一个个人喜好的问题。我之所以提出这个问题是因为Python官方文档在Python 2和Python 3将默认主题更改为Pydoc主题（后者的主题是一个自定义主题仅在CPython源代码中可用）。对一些人来说，默认的主题使一个项目看起来“老”一些。

## PyPI

[PyPI](http://pypi.python.org/pypi)，Python包索引（以前被称为“Cheeseshop”）是一个公开可用的Python包中央数据库。PyPI是你的项目发布的地方。一旦你的包（及其相关的元数据）上传到PyPI，别人通过pip或easy_instal可以下载并安装它。这一点得强调一下：即使你的项目托管在GitHub，直到被上传到PyPI后你的项目才是有用的。当然，有些人可以复制你的git库任何直接手工安装它，但更多的人想使用pip来安装它。


#### 最后的一步
如果你已经完成了所有的前面部分中的步骤，你可能急着想把你的包上传到PyPI，供其他人使用！
先别急着做上述事情，在分发你的包之前，有一个叫做cheesecake的有用的工具有助于运行最后一步。它分析你的包并指定一个分类的数字分数。它衡量你的包在打包、安装、代码质量以及文档的数量和质量方面是否容易/正确。
除了作粗略衡量的“准备”，cheesecake在完整性检查方面很优秀。你会很快看到你的setup.py文件是否有错或者有没有忘记为一个文件制作文档。我建议在上传每个项目到PyPI之前运行一下它，而不仅只是第一个。


#### 初始化上传
现在，你已经确定了你的代码不是垃圾和当人们安装它时不会崩溃，让我们把你的包放到PyPI上吧！你将会通过setuptools和setup.py脚本交互。如果这是第一次上传到PyPI，你将首先注册它：

`$ python setup.py register`

注意：如果你还没有一个免费的PyPI账户，你将需要现在去注册一个，才能注册这个包[@Lesus 注：注册之后还需要到邮箱去验证才行]。在你已使用了上面注册之后，你就可以创建发布包和上传到PyPI了: 

`$ python setup.py sdist upload`

上面这个命令建立一个源码发布版(sdist)，然后上传到PyPI.如果你的包不是纯粹的Python（也就是说，你有二进制需要编译进去），你就需要发布一个二进制版，请看setuptools文档，了解更多。


#### 发布及版本号
PyPI使用发行版本模型来确定你软件包的哪个版本是默认可用的。初次上传后，为使你软件包的每次更新后在PyPI可用，你需要指定一个新版本号创建一个发布。版本号管理是一个相当复杂的课题，PEP有专门的内容：PEP 440——版本识别和依赖指定。我建议参照[PEP 400指南](https://www.python.org/dev/peps/pep-0440/)（明显地），但如果你选择使用不同版本的方案，在setup.py中使用的版本比目前PyPI中的版本“高”，这样PyPI才会认为这是一个新版本。

#### 工作流
将你的第一个发布版本上传到PyPI后，基本的工作流程如下：

1. 继续在你的项目上工作 (比如修复bug，添加新特性等等)
1. 确保测试通过
1. 在git-flow中创建一个发布分支“冻结”你的代码
1. 在你项目的`__init__.py`文件里更新`__version__`number版本变量
1. 多次测试运行setup.py，将新版本上传到PyPI
用户希望你保持足够的更新频率以修复bug。你要管理好你的版本号，不要“过于频繁”的发布。记住：你的用户不会手工维护他们每个安装模块的不同的版本。

## 使用TravisCI持续集成

持续集成是指一个项目中所有变化不断整合的过程（不是周期性的批量更新）。就我们而言，这意味每次我们GitHub提交时，我们通过测试运行来发现是否有什么异常，正如你想象的，这是一个非常有价值的实践。不要有“忘记运行测试”的提交。如果你的提交通不过测试，你将收到一封电子邮件被告知。

TravisCI是一种使GitHub项目持续集成更容易的服务。如果你还没有账号到这看一下注册一个，完成这些之后，在我们进入CI之前我们先需要创建一个简单的文件。

#### 通过.travis.yml配置
在TravisCI上的不同项目通过一个.travis.yml文件来配置，这个文件在项目的根目录。简要地说，我们需要告诉Travis：

1. 我们项目使用的语言是什么
1. 它使用的是语言的哪个版本
1. 使用什么命令安装它
1. 使用什么命令运行项目的测试

这些都是很直接的东西。下面是`sandman.travis.yml`的内容：

~~~
language: python
python:
    - "2.7"
install:
    - "pip install -r requirements.txt --use-mirrors"
    - "pip install coverage"
    - "pip install coveralls"
script:
    - "coverage run --source=sandman setup.py test"
after_success:
    coveralls
~~~

在列出语言和版本后，我们告诉Travis如何安装我们的包。在install这行，确认包含下面这行：

`- "pip install -r requirements.txt --use-mirrors"`

这是pip安装我们项目的要求（如果有必要的话使用PyPI镜像站点）。另外的两行内容是sandman特有的。它使用一个额外的服务（[coveralls.io](https://coveralls.io/)）来连续监测测试用例的覆盖率，这不是所有项目都需要的。

script：列出能运行该项目测试的命令。与上面一样，sandman还需要做一些额外的工作。你的项目需要的只有Python的setup.py测试，after_success部分也可以一块删掉

一旦你提交了这个文件并在TravisCI中激活了你的项目的，push到GitHub。一会儿后，你会看到一个基于你最近提交的编译结束结果。如果成功了，你的编译呈现“绿色”和并且状态页会显示编译通过。你可以看到你项目在任何时间的编译历史。这对对人开发特别有用，在历史页可以看到特定开发者出错和编译的频率…

你还会收到一封通知你编译成功的电子邮件。当然你也可以设置只有在出错或错误被修复时才有邮件通知，但编译输出结果相同时也不会发送。这是非常有用的，你在不必被无用的“编译通过！”邮件淹没的同时在发生改变仍会收到警示。

## 用ReadTheDocs做持续文档集成

尽管PyPI有一个官方文档站点（[pythonhosted.org](http://www.pythonhosted.org/)），但是ReadTheDocs提供了一个更好的体验。为什么？[ReadTheDocs](https://readthedocs.org/)有针对GitHub非常棒的集成。当你注册ReadTheDocs的时候，你就会看到你的所有GitHub 代码库。选择合适的代码库，做一些小幅的配置，那么你的文档就会在你每次提交到GitHub之后自动重新生成。

配置你的项目应该是一个很直观的事情。只有一些事需要记住，尽管，这里有一个配置字段的列表，对应的值可能不一定是你直接用得上的：

- Repo: https://github.com/github\_username/project_name.git
- Default Branch:develop
- Default Version:latest
- Python configuration file: (leave blank)
- Usevirtualenv: (checked)
- Requirements file:requirements.txt
- Documentation Type: Sphinx HTML

## DRY 不要重复你自己

现在你已经完成了对于一个现存代码基础的所有艰难的开源工作，你可能不会想在开始一个新项目的时候把这些事重来一遍。幸运的是，你并不需要这么做。有Andrey Roy的[Cookiecutter工具](http://www.pydanny.com/cookie-project-templates-made-easy.html)（我链接到了Python版本，尽管还有一些不同语言的版本在[the main repo](https://github.com/audreyr/cookiecutter-pypackage))）

Cookiecutter是一个命令行工具能够自动执行新建项目的一些步骤来做这篇文章里提到的一些事情。 Daniel Greenfeld ( [@pydanny](http://www.twitter.com/pydanny) )写了一篇很好的关于它的博客并且提到了如何与这篇文章里提到的实践联系上。你可以从这里看看这篇文章： [Cookiecutter: Project Templates Made Easy](http://www.pydanny.com/cookie-project-templates-made-easy.html) .

## 结论
我们已经介绍了所有用来开源一个Python包的命令，工具和服务。当然，你可以直接把它扔到GitHub上并且说“自己安装它”，但是没人会这么做。并且你仅仅是开发源代码并不算是真正的开源软件。

另外，你可能不会为你的项目吸引外部贡献者。通过这里列出的方法来设立你的项目，你就已经创建了一个容易维护的Python包并且会鼓励大家来使用和贡献代码。而这，就是开源软件的真正精神，不是吗？

--------

终于转完了...搬砖还是要花力气的...


------
