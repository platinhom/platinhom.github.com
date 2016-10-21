---
title: 云标签
layout: page_small
---

<div id='tag_cloud'>
{% for tag in site.tags %}
<a class="linknoline" href="#{{ tag[0] }}" title="{{ tag[0] }}" rel="{{ tag[1].size }}"> <span style="color:#A82918; font-size:0.8em;">{{ tag[0] }} <span style="color:#07e;"> #{{ tag[1].size }}</span></span></a>&nbsp;&nbsp;&nbsp;
{% endfor %}

<hr style="margin:5px;border-width:2px;">

<span style="font-size:0.8em">
<a class="linknoline" target='_blank' href="/1234/01/01/Python-Language/">Python语法</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1234/01/02/Python-BuildinModules/">Python内建模块</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1234/02/01/Bash-Language/">Bash语法</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1234/03/01/Cpp-Language/">C++语法</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1234/04/01/JS-Language/">JS语法</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1234/05/01/PHP-Language/">PHP语法</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1234/06/01/HTML-Language/">HTML语法</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1234/07/01/CSS-Language/">CSS语法</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1234/08/01/VB-Language/">VB语法</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1233/01/01/Github-related/">Github相关</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1233/02/01/Amber-Usage/">Amber使用</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1233/03/01/Amber-Usage/">Sublime使用</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1233/04/01/Amber-Usage/">MySQL使用</a>&nbsp;&nbsp;
<!--br/-->
<a class="linknoline" target='_blank' href="/1111/11/11/Plans/">备忘计划</a>&nbsp;&nbsp;
<a class="linknoline" target='_blank' href="/1111/11/10/important-blog/">重要博客</a>&nbsp;&nbsp;
</span>
</div>

<hr style="margin:5px;border-width:2px;">

<ul class="listing">
{% for tag in site.tags %}
  <li class="listing-seperator" id="{{ tag[0] }}">{{ tag[0] }}</li>
  <p class="listing-item">
{% for post in tag[1] %}
{% if post.archive != true %}
  <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>&nbsp;&nbsp;&nbsp;
  <a href="{{ post.url }}" target='_blank' title="{{ post.title }}">{{ post.title }}</a> ; <br/> 
{% endif %}
{% endfor %}
	</p> 
{% endfor %}
</ul>

<!--script src="/jscss/jquery.tagcloud.js" charset="utf-8"></script> 
<script language="javascript">
$.fn.tagcloud.defaults = {
    size: {start: 1, end: 1, unit: 'em'},
      color: {start: '#f8e0e6', end: '#ff3333'}
};

$(function () {
    $('#tag_cloud a').tagcloud();
});
</script-->

-----

Notice: [Archives](/pages/archives/index.html) are not listed here! 
