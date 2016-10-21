---
title: WebUpdate
layout: page_prism
---

<link rel="stylesheet" href="/css/HomGH_small.css" type="text/css">

## The _layout files means:

- default.html: A basic template for all.

- page.html: A template when create a main page for blog
- page_small.html: Similar to page.html, `p,ol,ul,li` with small font.
- page_prism/html: From page.html, add prism code highlight

- post.html: A template for posting blogs, with basic loading.
- post_mathjax.html: Posting blogs with mathjax loading.
- post_small.html: Posting blogs with mathjax loading and small font for `p,ol,ul,li`.
- post\_toc.html: add TOC to post, use post\_small as template.

- slide.html: I don't know..

## The CSS/JS files:

- HomGH.css: CSS for webpage, including TOC.
- HomGH_small: CSS to control `p,ol,ul,li` to small font.
- HomGH_prism.css: CSS style for prism code.
- prism.css: The origin prism style.
- TOC.js: Old prism and box()?  I will use prism.js instead.
- addTOC.js: To generate TOC for the page. Used in posttoc.html.
- embed.js: duoshuo js.

- /js/script.js; /js/jquery.fancybox.pack.js; /js/jquery.fancybox.css; /js/jquery.min.js; /css/style.css is used for search box.

- jscss fold: old css and js by the website template 

## Update:
Notice: Some code may be converted by Jekyll. Please check the original [WebUpdate.md file](https://github.com/platinhom/platinhom.github.com/blob/master/WebUpdate.md).

### Add busuanzi to default.html

~~~ markup
<!--in head-->
<!--busuanzi for statistics of static web-->
<script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>

<!--in body-->
<span id="busuanzi_container_site_pv">本站<a href="http://ibruce.info/2015/04/04/busuanzi">总访问量</a><span id="busuanzi_value_site_pv"></span>次,</span><span id="busuanzi_container_site_uv">访客数<span id="busuanzi_value_site_uv"></span>人</span>
~~~

### Add Google Analysis and Baidu Tongji to default.

- Control them based on `_config.yml`

~~~ markup
<!--add these in head-->
<!--For web statistics by GA/Baidu, config in _config.yml-->
{% if site.googleAnaly.config %}
<script>
	(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

	ga('create', '{{ site.googleAnaly.id }}', 'auto');
	ga('send', 'pageview');
</script>
{% endif %}

{% if site.baiduTongji.config %}
<script>
	var _hmt = _hmt || [];
	(function() {
		var hm = document.createElement("script");
		hm.src = "//hm.baidu.com/hm.js?{{ site.baiduTongji.id }}";
		var s = document.getElementsByTagName("script")[0]; 
		s.parentNode.insertBefore(hm, s);
	})();
</script>
{% endif %}

<!--add this into _config.yml for control-->
###User define variants
#googleAnaly, your id link UA-12345678-X
googleAnaly:
  config: true
  id: UA-63959820-1

#baidu tongji
baiduTongji:
  config: true
  id: 07b65937d246126401c393da419d851e

#comment config
disqus:
  config: false
  id: platinhom

duoshuo:
  config: true
  id: platinhom
  
#baidu share config
baiduShare:
  config: false
~~~

### Revise the time zone for website

~~~ markup
<!--modify the footer as -->
<span class="label label-info">Last updated: {{site.time | date:"%Y-%m-%d %H:%M:%S %Z"}}</span></br>

<!--add this into _config.yml for control-->
# Time Zone +8 China
timezone:      Asia/Shanghai
~~~

### Cancel ChemDoodleWeb in post.html and so on, only in posttoc.html.

~~~~ markup
<script src="/jscss/ChemDoodleWeb.js"></script>
~~~~

### Cancel Mathjax in many templates.

~~~~ markup
<script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({tex2jax:{processEscapes: true, inlineMath: [ ['$','$'], ["\\(","\\)"] ], skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']}});
MathJax.Hub.Config({TeX:{extensions: ["cancel.js", "enclose.js"],
Macros:{a:"\\alpha",b:"\\beta",c:"\\chi",d:"\\delta",e:"\\epsilon",f:"\\phi",g:"\\gamma",h:"\\eta",i:"\\iota",j:"\\varphi",k:"\\kappa",l:"\\lambda",m:"\\mu",n:"\\nu",o:"\\omicron",p:"\\pi",q:"\\theta",r:"\\rho",s:"\\sigma",t:"\\tau",u:"\\upsilon",v:"\\varpi",w:"\\omega",x:"\\xi",y:"\\psi",z:"\\zeta",D:"\\Delta",F:"\\Phi",G:"\\Gamma",J:"\\vartheta",L:"\\Lambda",P:"\\Pi",Q:"\\Theta",S:"\\Sigma",U:"\\Upsilon",V:"\\varsigma",W:"\\Omega",X:"\\Xi",Y:"\\Psi",ve:"\\varepsilon",vk:"\\varkappa",vq:"\\vartheta",vp:"\\varpi",vr:"\\varrho",vs:"\\varsigma",vf:"\\varphi",alg:"\\begin{align}", ealg:"\\end{align}",bmat:"\\begin{bmatrix}", Bmat:"\\begin{Bmatrix}", pmat:"\\begin{pmatrix}", Pmat:"\\begin{Pmatrix}", vmat:"\\begin{vmatrix}", Vmat:"\\begin{Vmatrix}",ebmat:"\\end{bmatrix}", eBmat:"\\end{Bmatrix}",  epmat:"\\end{pmatrix}",  ePmat:"\\end{Pmatrix}",  evmat:"\\end{vmatrix}",  eVmat:"\\end{Vmatrix}",AA:"\\unicode{x212B}", Sum:"\\sum\\limits", abs:['\\lvert #1\\rvert',1], rmd:['\\mathop{\\mathrm{d}#1}',1],bi:['\\boldsymbol{#1}', 1], obar:['0\\!\\!\\!\\raise{.05em}{-}'],opar:['\\frac{\\partial #1}{\\partial #2}', 2], oppar:['\\frac{\\partial^2 #1}{\\partial #2^2}', 2]}}});
MathJax.Hub.Queue(function(){
var all=MathJax.Hub.getAllJax(),i;for(i=0;i<all.length;i+=1){all[i].SourceElement().parentNode.className+=' has-jax';}});
</script>
~~~~

### Cancel the search Nav in Default.html, which was put between container and main.

- Move the nav search into page.

~~~~ markup
<div>
<nav id="sub-nav"><a id="nav-search-btn" class="nav-icon" title="Search"></a></nav>
<div id="search-form-wrap"><form action="//google.com/search" method="get" accept-charset="UTF-8" class="search-form"><input type="search" name="q" results="0" class="search-form-input" placeholder="Search"><input type="submit" value="&#xF002;" class="search-form-submit"><input type="hidden" name="q" value="site:http://platinhom.github.io"></form></div>
<link rel="stylesheet" href="/css/style.css" type="text/css">
<script src="/js/jquery.min.js"></script>
 <link rel="stylesheet" href="/css/jquery.fancybox.css" type="text/css">
 <script src="/js/jquery.fancybox.pack.js" type="text/javascript"></script>
<script src="/js/script.js" type="text/javascript"></script>
</div>
~~~~

### Cancel old prism highlight relative css/js in default.   
- Abandon TOC.js, to use origin prism.js
- Add the `prism.js/HomGH_prism.css` to post and page prism.

~~~ markup
<!--Origin: -->
<link rel="stylesheet" href="/jscss/MDprism.css">
<script src="/jscss/TOC.js"></script>

<!--To these: -->
<link rel="stylesheet" href="/css/HomPrism.css">
<script src="/js/prism.js"></script>
~~~

### Change file/directory
Use jcss directory to contain js/css/images
Use other directory to contain pic/jscss and other files
New reposit to save pdf and molecular website

### Add post_jq.html layout to load jquery.

### post_py.html
Add pygments.css. Support pygments highlight.
Add new pygments_*.css style for pygments highlight
Note that, it should control the *div.highlight pre* and *div.highlight pre code* style to over the origin prism style.  

### Delete old template ending script
Last ending script means nothing. I delete it in post layout. Only save in posttoc.html layout.

### TOC post_toc.html
move old postdoc.html to other/jscss. Move addtoc.js to TOC.js. modify the TOC style.