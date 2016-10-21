---
layout: post
title: Github升级Jekyll3.0-强制使用rouge语法高亮
date: 2016-02-04 05:22:45
categories: IT
tags: Git Software
---

Github今日发了公告说要升级Jekyll到3.0, 要更快更简... [GitHub Pages now faster and simpler with Jekyll 3.0](https://github.com/blog/2100-github-pages-now-faster-and-simpler-with-jekyll-3-0). 的确, 从提交修改到生成页面, 的确是比以前要快了. 这是好事. 不过我的blog就要改动不少了.  

这次升级最大的两个变化是:

- 强制只能使用`kramdown`做markdown解释 (幸亏我就是学的和用的kramdown语法...kramdown和一般的markdown差异参看以前写的[kramdown和markdown较大的差异比较](/2015/11/06/Kramdown-note/))
- 强制只能使用`rouge`做语法解释(原来是`pygments`).

另外还不再支持`relative_permalinks`和`Textile`了.   

后者已经死了, 不支持也正常..Pygment没死啊...不能因为为了统一Ruby你就不支持Pygments啊啊啊啊 !!!

----------

升级带来的后果是.. 一堆东西不支持...简直是SB啊啊啊啊....今天收到邮件说Page建立失败, 因为升级的问题... 一看, 所有的代码block全部失去了语法高亮, 进行整修后, 还有一堆的奇葩bug (例如这篇[Pygments语法高亮](/2015/07/29/pygments-highlight/)... 

我以前是用`Pygments`解释, 然后用`prism`来进一步解析, 用prism的着色方案(因为我blog模板是使用prism的..), 特殊的不支持的语言如VB, 会选择使用 Jekyll的 `highlight tag`来进行解析, 解析后再用pygments着色方案. 一般情况使用``` ~~~code~~~ ```是使用prism解析的, 而特殊的使用highlight tag时调用`post_py` 模板使用pygments处理. 现在嘛就出事了...还多了个rouge还默认的..

探索了一下.. 暂时这么解决: 

### 统一使用Rouge着色方案CSS来着色

现在使用代码fenced block 解析后变得和以前不一样了. 默认以前是不会细节解析每个词哪个种类, 就是`<div class="highlight"><pre><code class="language-python"> 源码 </code></pre></div>`{:.language-html}, 现在源码部分变掉了对关键词加入`span-class`, 用于后面的css着色. 这种风格以前是使用highlight tag才有的, 所以一个解决办法就是...统一使用那种风格的CSS. 

> 解决方案: 在所有post的layout中样式都加入以前Pygments的css. 

`<link rel="stylesheet" href="/jcss/css/pygments_monokai.css">`{:.language-html}

颜色是出现了, 问题又来了...背景不像以前那样了..

看了看CSS后发现, 自己以前手动添加过背景(因为Pygments产生的style不含背景.). 而新的Rough的HTML标签是诡异的, 有两种风格:

使用 ```` ``` ```` 风格产生的是:

`<div class="highlighter-rouge"><pre class="highlight"><code>`{:.language-html}

使用highlight tag产生的风格是:

`<div class="highlight"><pre><code class="language-visualbasic" data-lang="visualbasic">`{:.language-html}.

原来Pygments处理时产生的风格属于后者类型, 所以CSS当然出问题啦..复制以前的syle再设置一个就好了. 需要将div的class改掉, pre增加class, code的class去掉.

#### 生成CSS可以:

`rougify style monokai.sublime > rouge_monkai.css` 把这个css拷贝到自己的css处就好了.

以下是monokai的css内容 (这是rouge生成的monokai.sublime的) 再自己修改的:

~~~css
.highlight table td { padding: 5px; }
.highlight table pre { margin: 0; }
.highlight .gh {
  color: #999999;
}
.highlight .sr {
  color: #f6aa11;
}
.highlight .go {
  color: #888888;
}
.highlight .gp {
  color: #555555;
}
.highlight .gs {
}
.highlight .gu {
  color: #aaaaaa;
}
.highlight .nb {
  color: #f6aa11;
}
.highlight .cm {
  color: #75715e;
}
.highlight .cp {
  color: #75715e;
}
.highlight .c1 {
  color: #75715e;
}
.highlight .cs {
  color: #75715e;
}
.highlight .c, .highlight .cd {
  color: #75715e;
}
.highlight .err {
  color: #960050;
}
.highlight .gr {
  color: #960050;
}
.highlight .gt {
  color: #960050;
}
.highlight .gd {
  color: #49483e;
}
.highlight .gi {
  color: #49483e;
}
.highlight .ge {
  color: #49483e;
}
.highlight .kc {
  color: #66d9ef;
}
.highlight .kd {
  color: #66d9ef;
}
.highlight .kr {
  color: #66d9ef;
}
.highlight .no {
  color: #66d9ef;
}
.highlight .kt {
  color: #66d9ef;
}
.highlight .mf {
  color: #ae81ff;
}
.highlight .mh {
  color: #ae81ff;
}
.highlight .il {
  color: #ae81ff;
}
.highlight .mi {
  color: #ae81ff;
}
.highlight .mo {
  color: #ae81ff;
}
.highlight .m, .highlight .mb, .highlight .mx {
  color: #ae81ff;
}
.highlight .sc {
  color: #ae81ff;
}
.highlight .se {
  color: #ae81ff;
}
.highlight .ss {
  color: #ae81ff;
}
.highlight .sd {
  color: #e6db74;
}
.highlight .s2 {
  color: #e6db74;
}
.highlight .sb {
  color: #e6db74;
}
.highlight .sh {
  color: #e6db74;
}
.highlight .si {
  color: #e6db74;
}
.highlight .sx {
  color: #e6db74;
}
.highlight .s1 {
  color: #e6db74;
}
.highlight .s {
  color: #e6db74;
}
.highlight .na {
  color: #a6e22e;
}
.highlight .nc {
  color: #a6e22e;
}
.highlight .nd {
  color: #a6e22e;
}
.highlight .ne {
  color: #a6e22e;
}
.highlight .nf {
  color: #a6e22e;
}
.highlight .vc {
  color: #ffffff;
}
.highlight .nn {
  color: #ffffff;
}
.highlight .nl {
  color: #ffffff;
}
.highlight .ni {
  color: #ffffff;
}
.highlight .bp {
  color: #ffffff;
}
.highlight .vg {
  color: #ffffff;
}
.highlight .vi {
  color: #ffffff;
}
.highlight .nv {
  color: #ffffff;
}
.highlight .w {
  color: #ffffff;
}
.highlight {
  color: #ffffff;
}
.highlight .n, .highlight .py, .highlight .nx {
  color: #ffffff;
}
.highlight .ow {
  color: #f92672;
}
.highlight .nt {
  color: #f92672;
}
.highlight .k, .highlight .kv {
  color: #f92672;
}
.highlight .kn {
  color: #f92672;
}
.highlight .kp {
  color: #f92672;
}
.highlight .o {
  color: #f92672;
}
div[class="highlight"] > pre > code[class*="language-"] {
  background:black;
  color:#f8f8f2;
}
div[class="highlight"] > pre {
  background:black;
}
figure[class="highlight"] > pre > code[class*="language-"] {
  text-align:left;
  background:black;
  color:#f8f8f2;
}
figure[class="highlight"] > pre > code[class*="language-"] td > pre{
  text-align:left;
  background:black;
  color:#f8f8f2;
}
figure[class="highlight"] > pre {
  text-align:left;
  background:black;
}
div[class="highlighter-rouge"] > pre[class="highlight"] > code{
  background:black;
  color:#f8f8f2;
}
div[class="highlighter-rouge"] > pre[class="highlight"] {
  background:black;
}
.lineno {color: #f8f8f2 } /*Number of line*/
~~~

想尝试修正以前 prism 的着色方案的, 但Fail了. 原因嘛, Prism通过JS去分析考察是何种语言再语法着色, 细心就会发现..fenced block产生出来的html代码里面失去了何种语法的信息(以前是在`code`的class里定义的,如`class="language-python"` ) 所以只能放弃以前的Prism JS和CSS了..

#### 另外问题

- 在我这篇[Pygments语法高亮](/2015/07/29/pygments-highlight/)里面本地生成的blog像以下[汇报的bug](https://github.com/jekyll/jekyll/issues/4432)一样出现了bug. 就是highlight tag使用linenos 选项时, 不会产生结尾的`</div>`, 真奇葩..
- 后来升级到Jekyll 3.0后貌似解决了这个问题, 但很奇葩的, 他把以前那个`div pre code`的结构改掉了...这次变成了`figure pre code`......真TM应付人...因为figure有另外的css, 妈蛋, 又乱了!
- 行内code语法种类指明还是支持kramdown的, 但是出来的效果就看上面吧..哎, 有空重新搞套css吧..

> PS: Pygments里vb叫vb.net, 现在叫vb或者visualbasic. 所有Rouge的支持语法称呼参考这里: [Rouge: List of supported languages and lexers](https://github.com/jneen/rouge/wiki/List-of-supported-languages-and-lexers)

## Local的Jekyll

使用`gem update jekyll` 去升级jekyll, 使其和Github一致. 

另外, 配置文件还要改掉(pygments改为rouge, 否则报错, Github也一样):

~~~yaml
highlighter: rouge

kramdown:
  syntax_highlighter: rouge
~~~

### 分页器错误

然后使用`jekyll server`就出现:

> Deprecation: You appear to have pagination turned on, but you haven't included the `jekyll-paginate` gem. Ensure you have `gems: [jekyll-paginate]` in your configuration file.

仔细看看Jekyll 升级到3 (官方:[Upgrading from 2.x to 3.x](http://jekyllrb.com/docs/upgrading/2-to-3/))后 抛弃了很多以前的基本功能(变成optional 了...),最重要的是分页器`paginate`.  

不过Github还是都装了, 所以Github上并没有这个分页器问题, 但是我本地的就不能分页了.. 

#### 解决方案:

`gem install jekyll-paginate` 然后在配置文件 `_config.yml` 里面增加: `gems: [jekyll-paginate]`一行, 检查有没有`safe:true`, 有就注释掉 (`#safe:true`).

> 最后一个`safe:true` 会不例外地关闭使用插件, 开启`safe:true`是因为Github 默认是开启了这种模式, 但有例外. 但本地一旦开启了, 就用不了了(但是在Github上是正常的, 估计额外处理了).  
> [官方说明plugin](http://jekyllrb.com/docs/plugins/)还可以通过手动改Gemfile再bundle, 或者将插件放到`_plugins`文件夹. 连上自己gem install 再修改配置文件共三种方法, 选一种即可.

### 旧的定义在layou中头的 page.var失效 -> layout.var

这个我是在主页page中发现的(local时出现, 在github上没问题), 当时左上角的page页面的title跑到下面去了, 奇怪应该有控制的才对. 后来仔细阅读 [Upgrading from 2.x to 3.x](http://jekyllrb.com/docs/upgrading/2-to-3/) 后发现 `Layout metadata` 这个改变, 就是说,以前在博客顶部YAML中标注的自定义变量调用从`page.var`变为`layout.var`.我有不少自定义变量啊混蛋...例如有`page_title: true`, `comment: true` 这样的. 这个专门是针对layout的, 为了把blog里面的page变量和layout中的变量分隔开..

但奇怪的是, 我在Github上改成了layout.page反而挂了..估计两边没有统一标准...

### 在site级别的abc.md 会生成abc/index.html而非abc.html

site级别就是说在你博客这个文件夹内所有的(之前_post里面才会一个md生成一个`文件名命名文件夹/index.html`) markdown文件都会变成`文件名命名文件夹/index.html`...所以404.md 就变成了`404/index.html`, 404页面就不work了..另外,以前一些链接也不work了...好好检查吧...

#### 解决办法:

> Update

在404.md 前面加入`permalink: /404.html` 来指定其生成的绝对路径就可以解决这个问题了. 原来更新上面写的relative_permalinks 是指这个问题...

------

总体来说, 这次Github并没有很好调试好Jekyll就搞了..导致一堆问题..也没有解决方案. 真是stuck了. 为了一点没必要的速度折腾用户, 真TNND.

------
