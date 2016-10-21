---
layout: post
title: Sublime编译build设置
date: 2015-06-20 23:29:25
categories: IT
tags: IDE Software
---

### 配置文件 : 使用 JsoN [百度百科](http://baike.baidu.com/view/136475.htm) 编写
####Build系统: 
参考说明: [中文版](http://jaylabs.sinaapp.com/Sublime_unofficial/reference/build_systems.html ),[英文版](http://sublimetext.info/docs/en/reference/build_systems.html  )  [非官方文档](http://sublime-text.readthedocs.org/en/latest/reference/build_systems.html  )
C++自带版本:

~~~javascript
{
	"cmd": ["g++", "${file}", "-o", "${file_path}/${file_base_name}"],
	"file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
	"working_dir": "${file_path}",
	"selector": "source.c, source.c++",

	"variants":
	[
		{
			"name": "Run",
			"cmd": ["bash", "-c", "g++ '${file}' -o '${file_path}/${file_base_name}' && '${file_path}/${file_base_name}'"]
		}
	]
}
~~~

gfortran version

~~~ javascript
{
     "cmd": ["gfortran", "-g", "-Wall", "${file}", "-o", "${file_path}/${file_base_name}"],
     "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
     "working_dir": "${file_path}",
     "selector": "source.f, source.f90",
     "shell": true,
     "variants":
     [
          {
               "name": "Run",
               //"cmd": [ "start", "${file_path}/${file_base_name}.exe"]
               "cmd" : ["${file_path}/${file_base_name}"]
          }
     ]
}
~~~

ifort in window64 version

~~~ javascript
{
	"cmd": ["cmd", "/E:on", "/V:on", "/K", "ipsxe-comp-vars.bat intel64 vs2010 && ifort ${file} -o ${file_path}/${file_base_name}"],
     "file_regex": "^.*\\\\([0-9A-Za-z_]+\\.[A-Za-z0-9]+)\\(([0-9]+)\\):[ ]+error[ ]+#([0-9]+):[ ]+(.*)$",
     "working_dir": "${file_path}",
     "selector": "source.f, source.f90,source.for,source.fortran90",
    "encoding":"cp936",
     //add the IVF path as follow to run the ipsxe-comp-vars.bat
      "path":"C:\\Program Files (x86)\\Intel\\Composer XE 2013\\bin;${path}",
     "variants":
     [
          {
               "name": "Run",
               //"cmd": ["cmd", "/e:on", "/v:on", "/c", "ipsxe-comp-vars intel64 vs2010 && ifort ${file} && ${file_base_name}"]
               "cmd" : ["${file_path}/${file_base_name}"]
          }
     ]
}
~~~


---
