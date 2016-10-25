### This's Hom's Blog! Welcome!

- 模板取自于 [哲科文](http://jerkwin.github.io/),此博客采用了 [卢克进](http://geeklu.com/) 的主题, 并稍加修改.
- 此博客使用[kramdown](http://kramdown.gettalong.org/)作为markdown解析.
- 此博客的代码高亮默认使用[Rouge](http://rouge.jneen.net/), 兼容之前使用的[prism](http://prismjs.com/). (之前模板使用Prism ~~,也可使用`post_py`模板来使用[pygment](http://pygments.org/)~~ ).
- 此博客的网站统计使用了[静态网页统计: 不蒜子](http://ibruce.info/2015/04/04/busuanzi/),[GA](http://www.google.com/analytics/ce/mws/),[百度统计](http://tongji.baidu.com/web/welcome/login).
- 此博客的评论功能使用了[多说](http://duoshuo.com/) 或[Disqus](https://disqus.com/).
- 此博客可以使用数学公式处理: [MathJax](https://www.mathjax.org/), 需要使用`post_mathjax`模板.
- 此博客支持左侧显示文章骨架总目录(TOC). 需要使用`post_toc`模板.
- 此博客基础模板post不使用jquery, 需要使用请用`post_jq`模板.
- 博文可以在下方直接点`Source`进入Github源文件进行查看编辑

### 简要文件介绍

- `index.html` : 博客首页以及博文分页器. 
- `_config.yml` : Jekyll 配置文件
- `404.md`: 404 页面定义 (错误时页面)
- `CNAME`: 指明指向域名. 此处指向`gohom.win`. Go Hom ~ :)
- `.gitignore`: 提交时忽略的文件/文件夹列表
- `robots.txt` : 对搜索引擎搜索的处理. 例如禁止被搜索
- `google12345678.html` : Google Analysis 的识别文件.

### 简要目录介绍

- `_posts`: 博文目录.博文格式`YYYY-MM-DD-name.md/html`.可以不管子目录.
- `_layouts`: Jekyll 博客基本页面布局. 在每篇blog开头`layout: ` 部分定义
- `_includes`: Jekyll插件或其余加载的内容, 这里只有 **评论** 的加载
- `_drafts`: 草稿文件, 不会被发布. 
- `_site` : Jekyll 生成的网站架构和页面, 一般只在本地存在.
- `pages` : 首页以外各个页面的储存. 因为新版的Jekyll处理非`_posts`的档案时会以`/pages/文件名/index.html`来生成链接, 因此要用`原文件名.html`的需要博客开头使用`permalink: `.
- `blogpic` : 放博文的图片
- `jcss` : image,css,js 等素材和配置
	- jcss/images: 一些必要的网页页面需要用到的图片素材
	- jcss/css: 一些页面用到的css
	- jcs/js: 一些页面用到的js脚本.
- `other`: 其余一些较杂的资料
	- other/jscss: 保留的旧模板 js/css 配置文件(备用)
	- other/pic: 博客使用的图片
	- other/scripts: 博客发布的脚本

### 功能脚本介绍

- `newblog.sh` : 自动创建新博客. 
	- 用法 : `./newblog.sh blogname catagory tag1 tag2..`
	- 博客名不要有`:`,有特殊符号请用双引号`".."`. 
	- **第一标签**名比较重要, 影响后续子文件夹分类, **建议将该博文最具特点最易关联的作为第一标签**
- `gitsubmit.sh` : 提交更新到github. 
	- 用法 : `./gitsubmit.sh`. 可以加一参数作为commit comment, 如有空格请加双引号 `" .. "`. 
	- ( Gitcaft 已作废, 此功能失效 ) 也可以提交到gitcafe,后面随便跟个选项如`./gitsubmit.sh comment a` 
- `_posts/classfy.sh` : 根据博文的分类和第一标签来将博文分配到对应子文件夹 `_posts/分类名/第一标签/博文.md`. 
	- 用法 `./classfy.sh`
	- 会自动删除子目录并重新生成目录和并将原有文件转移出来再进行分配. 
	- 建议定期分配博文.

## Update

- 2016.10: 重置整个blog, 清空旧的所有commits, 更改新域名(重置了不蒜子的计数). 移除总结性博文和Mark形式博文, 引入跳转Github编辑博文. 


