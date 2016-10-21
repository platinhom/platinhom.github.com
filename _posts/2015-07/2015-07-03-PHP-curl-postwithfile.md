---
layout: post
title: PHP利用curl来Post表单和上传文件
date: 2015-07-03 09:58:03
categories: Coding
tags: PHP Website
---

弄了一个通宵.终于把异步提交任务完成了....两个主要问题: 1. 利用curl进行异步(终止页面加载); 2. 利用curl进行post,包括上传文件. 只要是文件上传因为有版本差异, 网上的帖子都是旧方法, 旧方法又在我测试的5.6+中失效...所以弄了半天,乱摸了半天都失败 ╮(╯▽╰)╭

## 利用curl进行异步计算

- 首先,得安装php-curl. 有些服务器没有的, 就`sudo apt-get install php5-curl`然后重启`sudo service apache2 restart`,要是有php-fpm(??)就`sudo service php5-fpm restart`.
- 这里异步计算使用php-curl已经封装到函数`httpRequest`内,相比上一篇博客, 该版本更优秀在对上传文件的判断上. 
- `curl_setopt($curl, CURLOPT_TIMEOUT, 1);`控制curl执行某个php后停止在现在页面继续运行的时间,最少一秒.
- 更多参数说明请参考另一篇博客.[Ref1](http://platinhom.github.io/2015/07/03/php-curl/).
- 任务简单的根据文件来判断状态: 没运行/已完成/正在运行.据此刷新页面.

## curl模拟POST上传文件
这是这篇的关键,也是耗了很多时间才弄明白的...

- PHP curl里面有两种上传文件指定方式, 旧版使用`postname=>@文件名`放到`CURLOPT_POSTFIELDS`对应数组; 新版是`postname=>CURLFile类`.另外curl_setopt有项很关键的: `curl_setopt($curl, CURLOPT_SAFE_UPLOAD, true);`,安全传输是不支持旧版`@`方法的. 要是使用旧版方法,这个选项就要关闭false. 这个脚本加入了控制方法,主要是考虑这个这个类是否定义,常量是否定义,参考自Ref4.
- CURLFile类(>=PHP 5.5.0版),该类有三个属性: `(文件路径, 文件类型, 在$_FILES中对应name)`. 缺省值类型是`application/octet-stream`(一般文件都是),缺省name和第一参数相同. 可以用`new CURLFile(file, type, name)`来创建, 也可以用`curl_file_create`函数来创建.该类储存了文件对象信息, 5.6版后废除旧版上传方法,只能用这种. 更多细节参见Ref3. 不用管下面示例一堆opt的 ╮(╯▽╰)╭.
- 控制好`CURLOPT_SAFE_UPLOAD`常量(curl_setopt),主要是控制支持不支持`@filename`上传方式. 5.5后引入.这里用defined函数判断是否已定义.使用CURLFile类就要打开true.
- 在setopt里的`CURLOPT_PUT,CURLOPT_INFILE,CURLOPT_INFILESIZE`都是和POST上传文件无关的, 是HTTP PUT时用的. `CURLOPT_UPLOAD`这个也是无关的..

##### A case for asynchronous computation using php-curl

~~~php
<!-- Author: Platinhom; 2015-07-03 
A practical case for asynchronous computation using php-curl
-->
<?php
	function httpRequest($url,$method,$params=array()){
		$method=strtolower($method);
		if(trim($url)==''||!in_array($method,array('get','post'))||!is_array($params)){
			return false;
		}
		$curl=curl_init();
		curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);
		curl_setopt($curl,CURLOPT_HEADER,0 ) ;
		switch($method){
			case 'get':
				$str='?';
				foreach($params as $k=>$v){
					$str.=$k.'='.$v.'&';
				}
				$str=substr($str,0,-1);
				$url.=$str;//$url=$url.$str;
				curl_setopt($curl,CURLOPT_URL,$url);
				$result='';
			break;
			case 'post':
				//judge the upload file method
			    if (class_exists('CURLFile')) {//new method
    				curl_setopt($curl, CURLOPT_SAFE_UPLOAD, true);
				} elseif (defined('CURLOPT_SAFE_UPLOAD')) {//may be defined in old method.
        			curl_setopt($curl, CURLOPT_SAFE_UPLOAD, false);
    			}
				curl_setopt($curl,CURLOPT_URL,$url);
				curl_setopt($curl,CURLOPT_POST,1 );
				curl_setopt($curl,CURLOPT_POSTFIELDS,$params);
				curl_setopt($curl, CURLOPT_TIMEOUT, 1);
				$result='';
			break;
			default:
				$result='';
			break;
		}
		if(isset($result)){
			$result=curl_exec($curl);
		}
		//echo 'Here is some more debugging info:'.curl_error($curl);
		curl_close($curl);
		return $result;
	}

    if (! empty($_POST["JOBID"])){
      $JobID = $_POST["JOBID"];
    }
    else{
      $JobID = $_GET["JobID"];
    }

   	$ScriptDir=dirname($_SERVER['SCRIPT_FILENAME']);
    $uploaddir = $ScriptDir.'/MIBPBRun/';

    //mission completed
	if (file_exists($uploaddir.$JobID."/Result_$JobID.zip")){
		echo "<script>window.location='http://localhost/wei/mibpb2.php?software=mibpb&JobID=$JobID';</script>";
	}
	//start asyn-job by curl.
	elseif (!file_exists($uploaddir.$JobID)){
		$uploadfile = $uploaddir . basename($_FILES['files']['name']);
		//copy the upload file from tmp path to local path
		if (move_uploaded_file($_FILES['files']['tmp_name'], $uploadfile)) {
    		;//echo "File is valid, and was successfully uploaded.\n";
		} else {
    		echo "Possible file upload error!<br>";
		}

		//judge the upload file class
		if (class_exists('CURLFile')) {//new method.
    		$_POST['files'] = curl_file_create($uploadfile,$_FILES['files']['type'],$_FILES['files']['name']);
		} else {
    		$_POST['files'] = '@' . $uploadfile;//old method.
		}

		//use curl to submit job and stop
    	httpRequest("http://localhost/wei/mibpb2.php?JobID=$JobID",'POST',$_POST,$uploadfile);

		echo "Your Job ID: $JobID has been submitted!<br>Please wait or close your page and take your result later. ";
    	echo "<script>setTimeout('window.location.reload()',5000);</script>"; //指定5秒刷新一次
    	unlink($uploadfile);//enough time to upload?
    }
    //is still running
	elseif (file_exists($uploaddir.$JobID)){
		echo "Your Job ID: $JobID is still running....<br>Please wait or close your page and take your result later.";
    	echo "<script>setTimeout('window.location.reload()',5000);</script>"; //指定5秒刷新一次
	}
?>
~~~

## Reference

1. [PHP使用Curl](http://platinhom.github.io/2015/07/03/php-curl/)
2. [PHP-Curl](http://php.net/manual/en/book.curl.php)
3. [PHP-Curl-CURLFile类](http://php.net/manual/en/class.curlfile.php)
4. [考虑 PHP 5.0~5.6 各版本兼容性的 cURL 文件上传](http://segmentfault.com/a/1190000000725185)

---
