---
layout: post
title: PHP搭建简单的服务器-ESES
date: 2015-06-30 17:46:37
categories: Coding
tags: Website PHP
---

昨晚干到很晚,连续两天通顶,最近生活还真充实. 自从有了这个博客,就有事可做了, 争取每天都学点什么, 上来灌灌水. 昨天把William的界面拿来, 利用本地服务器自己写了底层的PHP处理. 成功了, 还接上了MIBPB. 不错~~这里就放放源码和分析吧.

## 网页主界面部分:
主要是一些输入框, 还有submit后调用的php脚本. 这里用的是POST方法提交表单.

~~~ html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!-- saved from url=(0033)http://23.239.23.221/Surface.html -->
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title></title>
<meta name="keywords" content="">
<meta name="description" content="">
<link href="http://fonts.googleapis.com/css?family=Varela" rel="stylesheet">
<link href="./Surface_files/defaultgreen.css" rel="stylesheet" type="text/css" media="all">
<link href="./Surface_files/fonts.css" rel="stylesheet" type="text/css" media="all">

<!--[if IE 6]><link href="default_ie6.css" rel="stylesheet" type="text/css" /><![endif]-->

</head>
<body>
<div id="wrapper">
	<div id="header-wrapper">
	<div id="header" class="container">
		<div id="logo">
			<h1><a href="http://23.239.23.221/index.html">The Wei Lab @ MSU</a></h1>
		</div>
		<div id="menu">
			<ul>
				<li><a href="http://23.239.23.221/index.html" accesskey="1" title="">Homepage</a></li>
				<li class="current_page_item"><a href="http://23.239.23.221/research.html" accesskey="3" title="">Research Projects</a></li>
				<li><a href="http://23.239.23.221/publications.html" accesskey="5" title="">Publications</a></li>
				<li><a href="http://versasphere.net/labsite/wiki/index.php/Main_Page" accesskey="6" target="_blank">Wiki</a></li>
				<li><a href="http://23.239.23.221/MTL.html" accesskey="7" title="">Meet the lab</a></li>
				<li><a href="http://23.239.23.221/about.html" accesskey="7" title="">About the lab</a></li>
			</ul>
		</div>
	</div>
	</div>

<center>
		<div id="extra" class="container">
			<div class="title">
				<h2>Surface Model</h2>
			</div>
</div>

<div>
<!--表单部分,注意action和method部分. 在本地服务器,不知道为啥原来的cgi-bin的文件夹就不行.奇怪.-->
<form action="./cgibin/prac.php" method="post" enctype="multipart/form-data">
<table style="width:500px" border="1">
		<!--$_POST通过name来调用值-->
		<tbody><tr><td><p>Upload input type file: <input type="file" name="files"></p></td></tr>
		<tr><td><p>Enter Buffer Size <input type="number" step="any" name="buffersize" value="2.0"></p></td></tr>
		<tr><td><p>Enter the probe radius <input type="number" step="any" name="probe" value="1.4"></p></td></tr>
		<tr><td><p>Enter the gride size <input type="number" step="any" name="gride" value="1.0"></p></td></tr>
		<tr><td><p>Submit to show the result <input type="submit" name="Submit" value="Submit Form"></p></td></tr>
	
</tbody></table>
</form>

<table style="500px" border="1">
		<tbody><tr>
			<td>Linux Download</td>
			<td width="10%" align="center"><a href="http://23.239.23.221/MS_Intersection" download=""> 
			<img border="1" src="./Surface_files/linux.png" alt="Linux" width="50px" height="50px"> </a></td>
		</tr>
</tbody></table>
</div></center>
</div>

<div id="copyright" class="container">
	<p>© Michigan State University. All rights reserved.</p>
</div>
</body></html>
~~~

## 服务器处理页面部分:
这里不是用原页面输出,而是转到另一个页面.具体细节看注释吧.

~~~ php
<!DOCTYPE html>
<html>
<body>

<?php
$JobID=uniqid("mibpb");
$RunResult=array();
$CWDir=getcwd();

$probe = $gride = $buffersize = $filename = "";
//处理必须输入的项. 因为下面的需要调用,所以要把php内容放前面.
$probeErr = $grideErr = $buffersizeErr = $filenameErr = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["probe"])) {
      $probeErr = "Probe is required! ";
  } else {
    $probe = format_input($_POST["probe"]);
    if (!is_finite($probe)) {
      $probeErr = "Enter valid probe radius! "; 
    }
  }
  //出错就提示并返回
  if ($probeErr!=""){
    echo "<script>alert('{$probeErr}');history.back();</script>";
  }

  if (empty($_POST["gride"])) {
    $grideErr = "Grid is required!";
  } else {
    $gride = format_input($_POST["gride"]);
    if (!is_finite($gride)) {
      $grideErr = "Enter valid grid size!"; 
    }
  }
  //另一种方法返回, 但这种方法是重载,不会保存刚才的值!
  if ($grideErr!=""){
      echo "<script>alert('{$grideErr}');location.href='../Surface.html';</script>";
  }

  if (empty($_POST["buffersize"])) {
    $buffersizeErr = "Buffer size is required!";
  } else {
    $buffersize = format_input($_POST["buffersize"]);
    if (!is_finite($buffersize)) {
      $buffersizeErr = "Enter valid buffer size!"; 
    }
  }
  if ($buffersizeErr!=""){
    echo "<script>alert('{$buffersizeErr}');history.back();</script>";
  }

  //这里用$_POST["files"]会出错!!
  if (empty($_FILES["files"])) {
    $filenameErr = "Please upload an input file!";
  }
  if ($filenameErr!=""){
    echo "<script>alert('{$filenameErr}');history.back();</script>";
  } 

  echo "Probe radius: ".$probe."; Grid size is: ".$gride."; Buffer size is: ".$buffersize,"<br/>";

  $filename=$_FILES["files"]["name"];
  // $_FILES["file"]["error"] - 由文件上传导致的错误代码
  if ($_FILES["files"]["error"] > 0)
    {
    echo "Return Code: " . $_FILES["files"]["error"] . "<br />";
    }
  else    {
    echo "Upload: " . $_FILES["files"]["name"] . "<br />";//上传文件basename
    //echo "Type: " . $_FILES["files"]["type"] . "<br />";//类型
    //echo "Size: " . ($_FILES["files"]["size"] / 1024) . " Kb<br />";//大小
    //echo "Temp file: " . $_FILES["files"]["tmp_name"] . "<br />";//上传后的临时文件
  }

  if (!file_exists("./MIBPBRun")){mkdir("./MIBPBRun");}//创建文件夹,要是不存在
  if (!file_exists("./MIBPBRun/$JobID")){mkdir("./MIBPBRun/$JobID");}

  if (file_exists("./MIBPBRun/$JobID/" . $_FILES["files"]["name"]))//检查是否已有该文件及目录
    {
    echo $_FILES["files"]["name"] . " already exists. ";
    }
  else
    {//将上传文件移动到指定目录和文件名
    move_uploaded_file($_FILES["files"]["tmp_name"],
    "./MIBPBRun/$JobID/" . $_FILES["files"]["name"]);
    //echo "Stored in: " . "./MIBPBRun/$JobID/" . $_FILES["files"]["name"];
    echo "Job ID is: ".$JobID."<br/><br/>";
  }
    chdir("./MIBPBRun/$JobID/");

   //获取文件名主部如1234而非1234.xyzr.第一句是多余的
  $nowfilename=realpath("./{$filename}");
  $filearray=pathinfo($nowfilename);
  $prefixfile=$filearray['filename'];
  
  copy("$CWDir/MS_Intersection","./MS_Intersection");
  copy("$CWDir/mibpb5","./mibpb5");
  //Window下不可行
  chmod("./mibpb5",0777);
  chmod("./MS_Intersection",0777);
  rename("$filename","1234.pqr");
 
  array_push($RunResult,"MIBPB output: ");
  exec("echo 'MIBPB output: '>{$JobID}.log");
  //执行程序,结果放到RunResult数组并输出到文件
  exec("./mibpb5 1234 | tee -a {$JobID}.log",$RunResult);
  rename("1234.pqr","$filename");
  rename("1234.dx","$prefixfile".".dx");
  rename("1234.xyzr","$prefixfile".".xyzr");
  rename("1234.eng","$prefixfile".".eng");
 
  array_push($RunResult,"Surface output: ");
  exec("echo '\n\nSurface output: ' >> {$JobID}.log");
  exec("./MS_Intersection {$prefixfile}.xyzr $probe $gride $buffersize | tee -a {$JobID}.log",$RunResult);
  exec("$CWDir/MarchingCubes",$RunResult);
  unlink("./mibpb5");
  unlink("./MS_Intersection");
  //压缩结果成压缩包
  exec("zip -r Result_{$JobID}.zip ./* > /dev/null");
  foreach ($RunResult as $resultline){
    echo $resultline."<br/>";
  }
  //列出结果文件
  echo "<br/><br/>Your Results: <br/>";
  //确定网页地址位置,不是好方法.但依然可用
  $webrelpath=str_replace($_SERVER['DOCUMENT_ROOT'],"",getcwd());
  //要是粗暴方法不适用...当脚本不在服务器子目录下时上面方法不适用
  if ($webrelpath===getcwd()){
      //use script relative path for web
      $webrelpath = dirname($_SERVER['SCRIPT_NAME']);
      $webrelpath.="/MIBPBRun/{$JobID}";
  }
  //找出所有文件
  $resultfiles=glob("*.*");
  //列出所有文件并连接
  foreach ($resultfiles as $eachfile){
    echo "<a href='{$webrelpath}/{$eachfile}'>{$eachfile}</a><br/>";
  }
 }

function format_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

?>
</body>
</html>
~~~

---
