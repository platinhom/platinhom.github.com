---
layout: post
title: PHP学习笔记-超全局变量
date: 2015-06-30 08:35:36
categories: Coding
tags: PHP HTML Website
---

## [超全局变量](http://www.w3school.com.cn/php/php_superglobals.asp)

- 可以全局调用,包括函数内.
- `$GLOBALS`: 储存了所有全局变量, 通过变量名可以获取全局变量.
- `$_SERVER`: 保存关于报头,路径,脚本位置信息. 如`$_SERVER["PHP_SELF"] `返回脚本文件名;  `$_SERVER["REQUEST_METHOD"]` 提交方法,如POST/GET.
- `$_REQUEST`: 收集HTML表单提交的数据.很重要,例如`$_REQUEST['hi']`可以获得表单提交后name为hi的标签的数据.通过在`<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">`指明脚本文件(这里是脚本自身),然后就可以调用`$_REQUEST`来收集值.
- `$_POST`: 收集提交`method="post"`的HTML表单收据,也常用于变量传递.见上例,不过用的是`$_POST['hi']`来收集.
- `$_GET`: 收集提交`method="get"`的表单数据,也可收集URL发送的数据. `<a href="test_get.php?subject=PHP&web=W3school.com.cn">测试 $GET</a>`, 在test_get.php中用`$_GET['subject']`就可以获取相应`?`后的数据.
- `$_FILES`:收集上传的文件信息,索引是`<input type="file" name="abc"\>`的name.还有二级数组储存文件基础信息.
- `$_ENV`: 环境变量.从系统传递到脚本中环境变量信息.
- `$_COOKIE`: 用于识别用户.[参见](http://www.w3school.com.cn/php/php_cookies.asp)
- `$_SESSION`: 存储有关用户会话的信息，或更改用户会话的设置.Session 的工作机制是：为每个访问者创建一个唯一的 id (UID)，并基于这个 UID 来存储变量。UID 存储在 cookie 中，亦或通过 URL 进行传导。[参见](http://www.w3school.com.cn/php/php_sessions.asp)

`$_GET` 是通过 URL 参数传递到当前脚本的变量数组,这时变量名和值都在网址上,可以添加到标签,可用于发送非敏感数据(例如密码就不要这么干)。`$_POST` 是通过 HTTP POST 传递到当前脚本的变量数组。用的method也不同.  
`htmlspecialchars(str)` 函数能够避免 `$_SERVER["PHP_SELF"]` 被利用,可以将特殊字符转为HTML实体,避免`<>`被利用.  

##### 利用POST验证表单输入的示例.
~~~ php
<!DOCTYPE html>
<html>
<body>

<?php
//预处理提交信息
// 定义变量并设置为空值
$name = $email = $gender = $comment = $website = "";
//处理必须输入的项. 因为下面的需要调用,所以要把php内容放前面.
$nameErr = $emailErr = $genderErr = $websiteErr = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $name = test_input($_POST["name"]);
    // 检查名字是否包含字母和空格
    if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
      $nameErr = "Only letters and white space allowed"; 
    }
  }

  if (empty($_POST["email"])) {
    $emailErr = "Email is required";
  } else {
    $email = test_input($_POST["email"]);
    // 检查电邮地址语法是否有效
    if (!preg_match("/([\w\-]+\@[\w\-]+\.[\w\-]+)/",$email)) {
      $emailErr = "Invalid email format"; 
    }
  }

  if (empty($_POST["website"])) {
    $website = "";
  } else {
    $website = test_input($_POST["website"]);
    // 检查 URL 地址语言是否有效（此正则表达式同样允许 URL 中的下划线）
    if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%
    =~_|]/i",$website)) {
      $websiteErr = "Invalid URL"; 
    }
  }

  if (empty($_POST["comment"])) {
    $comment = "";
  } else {
    $comment = test_input($_POST["comment"]);
  }

  if (empty($_POST["gender"])) {
    $genderErr = "Gender is required";
  } else {
    $gender = test_input($_POST["gender"]);
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
  $nameErr = "只允许字母和空格！"; 
}

?>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
<!--first php recover the enter value; second is for hints for required item-->
Name: <input type="text" name="name" value="<?php echo $name;?>"><span class="error">* <?php echo $nameErr;?></span><br><br>
E-mail: <input type="text" name="email" value="<?php echo $email;?>"><span class="error">* <?php echo $emailErr;?></span><br><br>
Website: <input type="text" name="website" value="<?php echo $website;?>"><span class="error"><?php echo $websiteErr;?></span><br><br>
Comment: <textarea name="comment" rows="5" cols="40" value="<?php echo $comment;?>"></textarea><br><br>
Gender:
<input type="radio" name="gender" <?php if (isset($gender) && $gender=="female") echo "checked";?> value="female">Female
<input type="radio" name="gender" <?php if (isset($gender) && $gender=="male") echo "checked";?> value="male">Male
<span class="error">* <?php echo $genderErr;?></span><br><br>
<input type="submit" name="submit" value="Submit"> 
</form>

</body>
</html>
~~~

##### 文件上传处理示例

~~~ php
<html>
<body>
<!--enctype 属性规定了在提交表单时要使用哪种内容类型。在表单需要二进制数据时，比如文件内容，请使用 "multipart/form-data"-->
<form action="upload_file.php" method="post"
enctype="multipart/form-data">
<label for="file">Filename:</label>
<input type="file" name="file" id="file" /> 
<br />
<input type="submit" name="submit" value="Submit" />
</form>

</body>
</html>

// upload_file.php
<?php
//利用$_FILES["name"]确定文件,这里判断文件类型和大小
if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/pjpeg"))
&& ($_FILES["file"]["size"] < 20000))
  {
  // $_FILES["file"]["error"] - 由文件上传导致的错误代码
  if ($_FILES["file"]["error"] > 0)
    {
    echo "Return Code: " . $_FILES["file"]["error"] . "<br />";
    }
  else
    {//$_FILES["file"]["name"] - 被上传文件的名称
    echo "Upload: " . $_FILES["file"]["name"] . "<br />";
    //$_FILES["file"]["type"] - 被上传文件的类型
    echo "Type: " . $_FILES["file"]["type"] . "<br />";
    //$_FILES["file"]["size"] - 被上传文件的大小，以字节计
    echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
    //$_FILES["file"]["tmp_name"] - 存储在服务器的文件的临时副本的名称
    echo "Temp file: " . $_FILES["file"]["tmp_name"] . "<br />";

    //指定一个upload文件夹存放上传的文件,判断是否已存在.
    if (file_exists("upload/" . $_FILES["file"]["name"]))
      {
      echo $_FILES["file"]["name"] . " already exists. ";
      }
    else
      {//将上传文件移动到指定目录和文件名
      move_uploaded_file($_FILES["file"]["tmp_name"],
      "upload/" . $_FILES["file"]["name"]);
      echo "Stored in: " . "upload/" . $_FILES["file"]["name"];
      }
    }
  }
else
  {
  echo "Invalid file";
  }
?>
~~~

## Reference
1. [超全局变量](http://www.w3school.com.cn/php/php_superglobals.asp)
2. 

---
