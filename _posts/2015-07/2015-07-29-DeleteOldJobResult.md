---
layout: post_jq
title: 自动删除过时结果
date: 2015-07-28 21:01:52
categories: Coding
tags: Bash
---

该脚本用来检测指定文件夹下相应文件夹(名字匹配)的生成时间, 并判断其存在时间. 如果时间超过一定时间(这里是一周),就将其删除掉.检查频率为1小时(3600秒).

该脚本可用于监测文件,结合nohup使用可作为后台监控.缺点是每次重启都需要执行,可以加入到service或者启动脚本当中.

<pre><code class="language-bash" id="src"></code></pre>

<script>
$.get("/other/scripts/deleteOldJob.sh",function(data,status){
	$("#src").html(data);
	Prism.highlightAll();
});
</script>

------
