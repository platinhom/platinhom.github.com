---
layout: post
title: Securimage验证码工具
date: 2015-12-18 15:58:57
categories: Coding
tags: PHP Website
---

验证码识别工具有很多，之前我们为大家分享了一个CSDN技术识别技术，这个技术算是比较成熟的。这里介绍一个PHP验证码工具，SECUR IMAGE。这款软件支持了AJAX调用。除此之外，这个还是一个比较不错的开源的免费脚本，专门可供我们工程师们进行验证码的生成。

那么Securimage特性，在下面为大家展示了：

* 仅用三行代码即可显示验证码
* 仅用六行代码即可对验证码的输入进行验证
* 自定义验证码长度
* 自定义字符集
* 支持TTF
* 使用自定义的GD字体（若TTF不支持）
* 轻松添加自定义背景图片
* 丰富的文本支持，包括颜色／角度／透明度选项
* 文字淆乱Arched lines through text
* 生成wav格式的CAPTCHA音频文件
* 自定义CAPTCHA的验证码列表

接下来，我们就通过实际代码来进行操作，帮助大家理解一下

~~~php
<html>
<head>
  <title>Securimage Test Form</title>
</head>
<body>
<?php
if (empty($_POST)){?>
<form method="POST">
Username:<br />
<input type="text" name="username" /><br />
PassWord:<br />
<input type="text" name="password" /><br />
 
<!-- 调用securimage，显示验证码图片，sid是用来防止被cache住的 -->
<img src="securimage_show.php?sid=<?php echomd5(uniqid(time()));?>"><br/>
<input type="text" name="code" /><br />
<input type="submit" value="Submit Form" />
</form>
 
<?php
} else{//form is posted
 include("securimage.php");
 $img=new Securimage();
 $valid=$img->check($_POST[‘code‘]);//检查用户的输入是否正确
 
 if($valid==true) {
   echo "<center>Thanks, you entered the correctcode.</center>";
 } else{
   echo "<center>Sorry, the code you entered wasinvalid.  <a href="javascript:history.go(-1)">Go back</a> to tryagain.</center>";
 }
}
 
?>
 
</body>
</html>
securimage_show.php的代码：

<?php
include ‘securimage.php‘;//下载包里面的核心类库代码
$img=new securimage();
$img->show();// alternate use: $img->show(‘/path/to/background.jpg‘);
?>
~~~

以上内容就是使用PHP验证码工具来生成较为复杂的验证码，避免SPAM

~~~html
<html>
    <head>
        <title>Для просмотра статьи разгадайте капчу</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style = "background:white">
        <div>
            <table style = "width:100%;height:100%"><tr><td style = "vertical-align:middle;text-align:center">
            <h2 style = "color:gray;font-family:sans-serif;padding:18px">для просмотра статьи разгадайте капчу</h2>
            <p></p>
            <form action = "" method = "POST">
                <p><img id="captcha" src="/captcha/securimage_show.php" /></p>
                <input type="text" maxlength="6" name="captcha_code" style = "width:256px;font-size:18px;height:36px;margin-top:18px;text-align:center" /><br>
                <a style = "color:gray;text-decoration:none" href="#" onclick="document.getElementById('captcha').src = '/captcha/securimage_show.php?' + Math.random(); return false">[ показать другую картинку ]</a>
                <p style = "margin-top:22px"><input type = "submit" value= "Продолжить"></p>
            </form>
            </td></tr></table>
        </div>
    </body>
</html>
~~~

以上是使用securimage防止抓取的例子(客户端代码).


------
