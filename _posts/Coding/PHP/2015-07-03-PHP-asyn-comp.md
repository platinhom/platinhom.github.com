---
layout: post
title: PHP-POST-异步调用
date: 2015-07-03 11:42:24
categories: Coding
tags: PHP Website
---

## php 通过fsocket模块 post 提交请求

~~~php
<?php
function sock_post($url,$query){
	$info=parse_url($url);
	$fp=fsockopen($info["host"],80,$errno,$errstr,3);
	$head="POST ".$info['path']." HTTP/1.0\r\n";
	$head.="Host: ".$info['host']."\r\n";
	$head.="Referer: http://".$info['host'].$info['path']."\r\n";
	$head.="Content-type: application/x-www-form-urlencoded\r\n";
	$head.="Content-Length: ".strlen(trim($query))."\r\n";
	$head.="\r\n";
	$head.=trim($query);
	$write=fputs($fp,$head);
	while(!feof($fp)){
		$line=fgets($fp);
		echo $line."<br>";
	}
}
?>
~~~

## php 通过 curl 模拟 post 提交请求

~~~php
<?php
$url='http://www.phpernote.com/post.php';
$fields=array(
	'lname'=>'justcoding',
	'fname'=>'phplover',
	'title'=>'myapi',
	'email'=>'403656085@qq.com',
	'phone'=>'13611975347'
);
$ch=curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch,CURLOPT_POST,count($fields));
curl_setopt($ch,CURLOPT_POSTFIELDS,$fields);
ob_start();
curl_exec($ch);
$result=ob_get_contents();
ob_end_clean();
echo $result;
curl_close($ch);
?>
~~~

## Reference

1. [php 不等待返回的实现方法（异步调用）](http://blog.csdn.net/openn/article/details/8212847)
2. [使用fscok实现异步调用PHP](http://www.laruence.com/2008/04/16/98.html)
3. [使用PHP进行异步HTTP请求](http://86er.sinaapp.com/?p=147)

---
