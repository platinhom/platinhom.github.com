---
layout: post_small
title: Jekyll使用
date: 2015-07-26 21:20:19
categories: IT
tags: Website Git Software
---

Jekyll是Github Page的静态页面自动生成器. 一般只要知道一些基础用法就可以了, 并不需要安装.在linux/mac上可以装来自己玩玩. 尤其在断网时想查看自己博客时.更新十分快, 很方便本地预览. 但是对于github的项目子页面功能相关的链接会失效(因为交叉了).  
Jekyll预设了[Pygment](http://pygments.org/)语法着色. 

## 安装
Jekyll是基于ruby的.先要安装ruby和ruby gem.  
`gem install jekyll` 命令行安装.然后就可以使用jekyll命令了.  
window版安装[参见官方](http://jekyllcn.com/docs/windows/#installation) (不推荐.)或者我博客的[Ref6](/2015/07/30/jekyll-window/).

## 基本使用
jekyll 2.5.3 -- Jekyll is a blog-aware, static site generator in Ruby

Usage:

  jekyll <subcommand> [options]

Options:

- -s, --source [DIR]  Source directory (defaults to **./**)
- -d, --destination [DIR]  Destination directory (defaults to **./_site**)
-     --safe         Safe mode (defaults to false)
- -p, --plugins PLUGINS\_DIR1[,PLUGINS\_DIR2[,...]]  Plugins directory (defaults to **./_plugins**)
-     --layouts DIR  Layouts directory (defaults to **./_layouts**)
- -h, --help         Show this message
- -v, --version      Print the name and version
- -t, --trace        Show the full backtrace when an error occurs

Subcommands:

-  build, b              Build your site
-  docs                  Launch local server with docs for Jekyll v2.5.3
-  doctor, hyde          Search site and print specific deprecation warnings
-  help                  Show the help message, optionally for a given subcommand.
-  new                   Creates a new Jekyll site scaffold in PATH
-  serve, server, s      Serve your site locally

##### `jekyll serve` 使用本地服务器服务
Server address: http://127.0.0.1:4000/  
Server running... press ctrl-c to stop.  
自动具有根据修改保存重新生成的功能. Auto-regeneration（自动再生成文件）: 开启。使用 `--no-watch` 来关闭。  
`jekyll serve --detach` 直接背景运行,需要kill来取消. Update: 在mingw使用--detach会出错, 推荐`jekyll server -q &`静默不显示并背景运行.

##### `jekyll build` 生成文件到_site
*jekyll build --watch*  会监控更新  
*jekyll build --source <source> --destination <destination>* 指定相应源文件夹以及生成文件夹,也可在_config.yml中指定.

### 目录结构
在根目录下一般有以下文件夹和文件: (要是github想禁用jekyll,建一个 *.nojekyll* )

- `_config.yml` 配置文件,配置jekyll的一切以及变量 
- `index.md/html` 主页文件,必须的
- `.gitignore` 被忽略上传到github的文件(夹)列表
- `.jekyll-metadata` 用来记录追踪文件修改情况,以便更新.
- `_layout` 模板文件夹,用来生成相应子页面的模板,在子页面中 *layout: page* 指定
- `_post` 相应子页面(博客)所在位置,文件名规则:2015-07-24-name.md/html
- `_includes` 用来包含一些常用需要的结构块文件,例如comment.使用 `\{\% include file.ext \%\}` 来包含(`\`去掉).非必须.
- `_site` 如果使用jekyll本地版生成页面就会有该文件夹.一般会被判断为不上传到github.非必须.
- `_drafts` 草稿文件,不会被生成到网页中.非必须.
- `_data` 格式化好的网站数据应放在这里。jekyll 的引擎会自动加载在该目录下所有的 yaml 文件（后缀是 .yml 或者 .yaml).作用不明..非必须

### 配置文件
配置文件_config.yml里保存了各种程序变量的配置. 更多信息请参考[这个](http://jekyllcn.com/docs/configuration/).这里只列出些常用的配置,另外也可以自定义. 列表使用["a","b"..]的形式. config文件内使用YAML格式可以定义很多自定义内容,从而实现更多控制.

- markdown: kramdown    (指定使用的markdown方法)
- permalink: /:year/:month/:day/:title/  (指定永久链接的形式,:这里调用变量值)
- pygments: true   (是否使用pygments语法着色)
- safe: true   (禁用自定义插件。)
- paginate: 25   (分页器一页最多页码,更多分页相关参考[分页功能](http://jekyllcn.com/docs/pagination/))
- encoding: "utf-8"  (编码)
- timezone: Asia/Shanghai   (时区)

### 撰写博客和组织网页结构
只需要在_post文件夹内生成 **年-月-日-标题.md** 的文件就可以了(当然可以还支持textile,html等),文件一般包括一个YAML头信息(见下)定义使用的模板,标题等. 后面就是一般的征文内容, 然后正文内容会以 \{\{ content \}\} 来插入到模板中,生成相应子页面.更多请参考ref3. 还不了解参看[jekyll自己介绍](http://jekyllcn.com/docs/posts/)吧..

如何组织网站的页面结构参考[这个](http://jekyllcn.com/docs/pages/).我喜欢把各个子页面放到pages文件夹里,每个子页面都一个文件夹和对应的index.html(减少主文件夹显示的数量,sublime方便点).随各人喜好罢了.其实没有硬性规定,在主页面的index.html相应链接改一下就OK了.

### [插件](http://jekyllcn.com/docs/plugins/)
Jekyll支持使用插件来进行加载和处理,例如生成sitemap,rss等.但是github并不支持(自动safe=ture). 可以使用本地处理后再上传也行. 

## 语法
Jekyll语法比较混杂. 配置文件和头信息中信息储存使用[YAML](https://zh.wikipedia.org/wiki/YAML)标记语言(后缀名.yml)记录, 网页内容处理使用基于ruby的[Liquid模板工具](https://docs.shopify.com/themes/liquid-documentation/basics)来进行. 

### YAML头信息
YAML头信息是写在每篇博客开头的像下面所示,包含在两个三横之内. 头信息里面用来定义各种变量,包括预设变量以及可以自定义变量,变量名的冒号后记得要加空格!

~~~
---
layout: post
title: Hello world
tags: tag1 tag2
---
~~~

预定义的变量包括:

- layout: 如果设置的话，会指定使用该模板文件。指定模板文件时候不需要扩展名。模板文件需要放在 _layouts 目录下。
- permalink: 如果你需要让你的博客中的 URL 地址不同于默认值 /year/month/day/title.html 这样，那么当你设置这个变量后，就会使用最终的 URL 地址。(一般不用,用配置文件设置值)
- published: 当站点生成的时候，如果你不需要展示一个具体的博文，可以设置这个变量为 false。(一般不用)
- category/categories: 除过将博客文章放在某个文件夹下面外，你还可以根据文章的类别来给他们设置一个或者多个分类属性。这样当你的博客生成的时候这些文章就可以根据这些分类来阅读。在一个文章中多个类别可以通过 YAML list 来指定，或者用空格隔开。
- tags: 类似分类，一篇文章也可以给它增加一个或者多个标签。同样多个标签之间可以通过 YAML 列表或者空格隔开。
- date: 这里的日期会覆盖文章名字中的日期。这样就可以用来保障文章排序的正确.注意这个时间是GMT标准时间.

还可以自定义变量,例如title, 在相应位置使用 **\{\{ page.title \}\}** 来调用该变量.

### 模板/内容使用jekyll语法插入内容
使用 **\{\{ .. \}\}** 来插入相应变量/对象属性等.常见插入内容(就是代替里面两点):

- content: 整篇博客的真实内容,就是YAML头后面的内容.要是MD会相应处理成html. 

使用 `\{\% .. \%\}` (把反斜杠`\`去掉)使用Liquid标签.常用例如以下内容(代替..):

- include file.ext : 调用_include内的文件.
- for var in list .... endfor : for循环,例如下面的列post的方法. \{\{ var \}\} 这样来调用循环变量.
- if expression ......endif : if语句块.
- highlight python ..... endhighlight : 代码块语句块

~~~
\{\% for post in site.posts \%\}
    <li>
      <a href="\{\{ post.url \}\}">\{\{ post.title \}\}</a>
    </li>
  \{\% endfor \%\}
~~~

### 预定义变量
预定义变量对于页面模板十分重要, 基本上就是预定义变量和Liquid语法来构建页面的, 也是使用jekyll构建自己想要网页时最关键的.不懂的话,可以先看看别人的模板,自己再模仿.

#### 全局(Global)变量

- site : 来自_config.yml文件，全站范围的信息+配置。详细的信息请参考下文
- page : 页面专属的信息 + YAML 头文件信息。通过 YAML 头文件自定义的信息都可以在这里被获取。详情请参考下文。
- content : 被 layout 包裹的那些 Post 或者 Page 渲染生成的内容。但是又没定义在 Post 或者 Page 文件中的变量。
- paginator : 每当 paginate 配置选项被设置了的时候，这个变量就可用了。详情请看分页。

除了主页面要使用paginator分页器外, 一般主要是使用site和page, site主要是全站范围的(包括config文件),page针对该页面的变量.

#### 全站(site)变量

- `site.time` : 当前时间（运行jekyll这个命令的时间点）。
- `site.pages` : 所有 Pages 的清单。
- `site.posts` : 一个按照时间倒序的所有 Posts 的清单。
- `site.related_posts` : 如果当前被处理的页面是一个 Post，这个变量就会包含最多10个相关的 Post。默认的情况下， 相关性是低质量的，但是能被很快的计算出来。如果你需要高相关性，就要消耗更多的时间来计算。 用jekyll 这个命令带上 --lsi (latent semantic indexing) 选项来计算高相关性的 Post。
- `site.categories.CATEGORY` : 所有的在 CATEGORY 类别下的帖子。
- `site.tags.TAG` : 所有的在 TAG 标签下的帖子。
- `site.[CONFIGURATION_DATA]` : 所有的通过命令行和 _config.yml 设置的变量都会存到这个 site 里面。 举例来说，如果你设置了 url: http://mysite.com 在你的配置文件中，那么在你的 Posts 和 Pages 里面，这个变量就被存储在了 site.url。Jekyll 并不会把对 _config.yml 做的改动放到 watch 模式，所以你每次都要重启 Jekyll 来让你的变动生效。

#### 页面(page)变量

- `page.content` : 页面内容的源码。
- `page.title` : 页面的标题。
- `page.excerpt` : 页面摘要的源码。
- `page.url` : 帖子以斜线打头的相对路径，例子： /2008/12/14/my-post.html。
- `page.date` : 帖子的日期。日期的可以在帖子的头信息中通过用以下格式 YYYY-MM-DD HH:MM:SS (假设是 UTC), 或者 YYYY-MM-DD HH:MM:SS +/-TTTT ( 用于声明不同于 UTC 的时区， 比如 2008-12-14 10:30:00 +0900) 来显示声明其他 日期/时间 的方式被改写，
- `page.id` : 帖子的唯一标识码（在RSS源里非常有用），比如 /2008/12/14/my-post
- `page.categories` : 这个帖子所属的 Categories。Categories 是从这个帖子的 \_posts 以上 的目录结构中提取的。距离来说, 一个在 /work/code/_posts/2008-12-24-closures.md 目录下的 Post，这个属性就会被设置成 ['work', 'code']。不过 Categories 也能在 YAML 头文件信息 中被设置。
- `page.tags` : 这个 Post 所属的所有 tags。Tags 是在YAML 头文件信息中被定义的。
- `page.path` : Post 或者 Page 的源文件地址。举例来说，一个页面在 GitHub 上的源文件地址。 这可以在 YAML 头文件信息 中被改写。
- `page.自定义变量` : 任何你自定义的头文件信息都会在 page 中可用。 距离来说，如果你在一个 Page 的头文件中设置了 custom\_css: true， 这个变量就可以这样被取到 page.custom\_css。

#### 分页器(Paginator) 相关

- `paginator.per_page` : 每一页 Posts 的数量。
- `paginator.posts` : 这一页可用的 Posts。
- `paginator.total_posts` : Posts 的总数。
- `paginator.total_pages` : Pages 的总数。
- `paginator.page` : 当前页号。
- `paginator.previous_page` : 前一页的页号。
- `paginator.previous_page_path` : 前一页的地址。
- `paginator.next_page` : 下一页的页号。
- `paginator.next_page_path` : 下一页的地址。

##### 后记:
由于jekyll会对其符合语法的进行内容进行处理, 写起来可能会有些`\`的出现. 本来想贴写代码块的, 实在太不方便了.

## Reference
1. [Jekyll CN](http://jekyllcn.com/)
2. [YAML官网](http://yaml.org/)
3. [使用Github搭建博客](http://platinhom.github.io/2015/06/05/Build-Blog-Github/)
4. [Liquid模板工具](https://docs.shopify.com/themes/liquid-documentation/basics)
5. [Shopify-liquid](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers)
6. [Jekyll-window安装](/2015/07/30/jekyll-window/)

------
