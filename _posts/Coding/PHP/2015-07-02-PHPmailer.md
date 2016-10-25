---
layout: post
title: 服务器利用PHPMailer发送邮件
date: 2015-07-02 05:07:49
categories: Coding
tags: PHP Website
---

今天折腾了半天,终于把email系统弄通了.死人头Tom邮箱简直就是一坨屎...去注册新的gmail,随便选了一年,然后说我年龄不够,根据法规不允许我注册.....╮(╯▽╰)╭ ....

## 安装PHPMailer

1. 先去下载: [PHPMailer下载](https://github.com/PHPMailer/PHPMailer)
2. 解压后复制`class.phpmailer.php`和`class.smtp.php`两个文件到需要调用发email的页面目录.
3. 复制下面内容创建一个新文件,然后在PHP中调用这个脚本,加载函数. 也可以将这个函数写到主页面里面,因为PHP内容不显示,所以也无所谓了.

里面有test的PHP网页,也有选项说明.有兴趣的自己琢磨吧. 我就是用而已,功能搭通就OK了 ╮(╯▽╰)╭. 要是想收邮件就要`class.pop3.php`了.

## 服务器使用

1. 先去注册个使用邮箱.这里我最后用的是hotmail的,因为google说我太年轻了 ╮(╯▽╰)╭.163使用SMTP要手机绑定...最后找了个TOM, 然后发现其发送总是被拒收, 我开始还以为是我服务器不好, 后来才发现TOM mail太狗屎了...这里示例是tom的.Hotmail新注册验证后会防机器人要你验证几次, 几次之后就好了.
2. 在需要使用邮箱的PHP页面中,`require_once("sendmailfuntion.php");`,注意路径了.也可以将该脚本和另外两个类一起放到PHP的路径中也可以. 另外也可以将该脚本的函数直接引入PHP页面中.
3. `sendmail("receiver@email.com","Email Title","Email Contents");` 调用函数,写上收件人,题目,内容.OK了.要是有附件(例如某些文件),可以取消掉`mail->AddAttachment`那行并写上文件的地址.
4. 收件人地址和题目比较好办. 邮件主体内容是HTML格式的, 所以换行需要`<br>`,超链接需要`<a href="" target=_blank>...</a>`, 图片需要`<img src='..'>`. 一般这样子也就够了吧 ╮(╯▽╰)╭. 比较麻烦的就是PHP的字符串的引号,变量和HTML引号的问题了,要是像python一样支持字符串块那多好...
5. 调用函数后, 就会发送邮件. 注意会占用页面加载时间. 然后找个测试邮箱收收看吧! 有超链接的时候很容易被判断为垃圾邮件....请注意查收.

##### sendmailfunction.php

~~~ php
<!-- file: sendmailfuntion.php
 Please take this script and class.phpmailer.php class.smtp.php together.
 To use: 
 require_once("sendmailfuntion.php");//load the function
 sendmail("receiver@email.com","Email Title","Email Contents");
-->
<?php
function sendmail($to,$subject = "",$body = ""){
    //$to 表示收件人地址 $subject 表示邮件标题 $body表示邮件正文
    date_default_timezone_set("America/Detroit");//设定时区东八区
    require_once('class.phpmailer.php');
    include("class.smtp.php"); 
    $mail             = new PHPMailer(); //new一个PHPMailer对象出来
    $body             = eregi_replace("[\]",'',$body); //对邮件内容进行必要的过滤
    $mail->CharSet ="UTF-8";//设定邮件编码，默认ISO-8859-1，如果发中文此项必须设置，否则乱码
    $mail->IsSMTP(); // 设定使用SMTP服务
    $mail->SMTPDebug  = 1;                     // 启用SMTP调试功能
                                           // 1 = errors and messages
                                           // 2 = messages only
    $mail->SMTPAuth   = true;                  // 启用 SMTP 验证功能
    //$mail->SMTPSecure = "tls";//"ssl";      // 安全协议,163用ssl,hotmail gmail用tls.
    $mail->Host       = "smtp.tom.com";      // SMTP 服务器
    $mail->Port       = 25;//25,465,587;                   // SMTP服务器的端口号
    $mail->Username   = "fuckTom@tom.com";  // SMTP服务器用户名
    $mail->Password   = "password";            // SMTP服务器密码
    $mail->SetFrom('fuckTom@tom.com', 'Platinhom');//发送邮件的邮箱和用户名
    $mail->AddReplyTo("myMail@hotmail.com","Zhixiong");//没啥用
    $mail->Subject    = $subject;  //邮件题目
    $mail->AltBody    = "To view the message, please use an HTML compatible email viewer!"; // optional, comment out and test
    $mail->MsgHTML($body);  //邮件内容
    $address = $to;     //收件人地址
    $mail->AddAddress($address, "Dear User");
    //$mail->AddAttachment("images/phpmailer.gif");      // attachment 
    //$mail->AddAttachment("images/phpmailer_mini.gif"); // attachment
    if(!$mail->Send()) {
        echo "Mailer Error: " . $mail->ErrorInfo; //调用错误提示.
    } else {
        ;//echo "Message sent successfully！";//你不想在页面中出现这句吧.
        }
    }
?>
~~~

### 一些细节

- SMTPAuth验证一般都是需要的.
- SMTPSecure取决于邮箱服务器,有些不需要,有些需要ssl(163),有些需要tls(hotmail,gmail).有别的时候再补充吧.多试试..
- Host去百度一下就知道了,比较容易,一般不会错,就是前面pop3/smtp后面是主页面网址.
- 端口号一般有常用的. 也可以百度一下.下面也会总结一些.
- Username,有时是不带`@email.com`,但大部分还是要带的.

~~~
一般POP3端口110/995, SMTP端口25/465. 括号后面是可能的协议及端口.一般加密都是SSL.hotmail貌似除外(总之就不停失败)

Hotmail:
POP3服务器地址:pop3.live.com (tls: 995)
SMTP服务器地址:smtp.live.com (tls: 25/587)

Gmail邮箱
POP3：pop.gmail.com (SSL/TLS:995)
SMTP：smtp.gmail.com (SSL/TLS:465/587)
IMAP: imap.gmail.com (SSL/TLS:993)

网易系列: 均需ssl验证. 一般是POP3:110,SMTP:25,IMAP:143
126邮箱： 
126免费邮箱目前不直接开放smtp、pop3，但是对于126至尊邮(vip.126)开放pop3和smtp
POP：POP.126.com 
SMTP：SMTP.126.com 
http://mail.126.com/help/client_04.htm 

163邮箱： 
IMAP: imap.163.com (143,ssl: 993)
POP：pop.163.com (110,ssl: 995)
SMTP：smtp.163.com (25,ssl: 465,994)
http://mail.163.com/help/help_client_04.htm 

新浪收费邮箱
POP3：pop3.vip.sina.com
SMTP：smtp.vip.sina.com

网易@yeah.net邮箱： 
POP3: pop.yeah.net;
SMTP: smtp.yeah.net  

网易@netease.com邮箱：
POP3: pop.netease.com;            
SMTP: smtp.netease.com  

网易188财富邮
POP3：pop.188.com
SMTP：smtp.188.com

263.net: 
POP3服务器地址:pop3.263.net 
SMTP服务器地址:smtp.263.net 

QQ邮箱
POP：pop.qq.com  (110,ssl:995)
SMTP：smtp.qq.com  (25,ssl:465/587)
为了保障用户邮箱的安全，QQ邮箱设置了POP3/SMTP的开关。系统缺省设置是“关闭”，在用户需要POP3/SMTP功能时请“开启”。 

新浪邮箱： 
POP：pop.sina.com.cn 或：pop3.sina.com.cn 
SMTP：smtp.sina.com.cn 
http://tech.sina.com.cn/sinahelp/2002-06-14/120714.shtml 

阿里云
POP3: pop3.aliyun.com(无密:110,ssl:995);
SMTP: smtp.aliyun.com(无密,ssl:465);

TOM邮箱： (比较垃圾啊..)
POP：pop.tom.com 
SMTP：smtp.tom.com (不支持ssl:25)
http://mail.tom.com/help/ 

搜狐邮箱： 
POP：pop3.sohu.com 
SMTP：smtp.sohu.com 
http://help.sohu.com/help_2.php?fatherid=2 

信网@eyou.com：         
POP3: pop3.eyou.com；               
SMTP: mx.eyou.com 

亿唐@etang.com：　      
POP3: pop.free.etang.com            
SMTP: smtp.free.etang.com  

21世纪@21cn.com： 　
POP3: pop.21cn.com； 　　　　　
SMTP: smtp.21cn.com 
注意: 网页新注册的用户不支持使用外部电子邮件客户端程序发送邮件 

中华网免费邮件@mail.china.com：不支持pop3和smtp服务，因此，不可以使用outlook、foxmail等软件来进行邮件的收发，只能通过登陆网页进行收发。 

雅虎@yahoo.com.cn：作为一种基于 web 的电子邮件服务，雅虎中国目前不提供对 POP 或者 SMTP 服务器的访问。这意味着不能用外部电子邮件客户端程序（例如 Netscape Mail、Foxmail 或 Outlook）来访问雅虎中国的电邮帐户。 
接收服务器：pop.mail.yahoo.com
发送服务器：smtp.mail.yahoo.com

~~~

## Reference

1. [PHPMailer新GitHub](https://github.com/PHPMailer/PHPMailer)和[旧wiki](https://code.google.com/a/apache-extras.org/p/phpmailer/)
2. [关于PHP邮件发送](http://www.cnblogs.com/sinllychen/p/3243034.html)
3. [腾讯粑粑客户端设置](http://service.exmail.qq.com/cgi-bin/help?subtype=1&id=28&no=1000564)
---
