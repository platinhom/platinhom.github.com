---
layout: post
title: Python:requests-cookies
date: 2016-01-13 08:36:48
categories: Coding
tags: Python Internet
---


Cookies就像字典一样储存了各个项的值并保存起来, 例如我们的用户名, 密码, 登录信息等都可以保存起来. 当网页再次被加载时可以从cookies中找到相关的信息并从而免除再次输入赋值的过程.

在requests中使用get等请求时同样可以赋予cookies信息. 例如我们从浏览器中获取某次网页加载时请求的cookies, 可以同样赋予requests再次使用. 

requests请求时加入`cookies={key:value}`参数即可传递cookies.

~~~python
import requests
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
r.text
#'{"cookies": {"cookies_are": "working"}}'
~~~

查询某次请求的cookies很简单, 就像获得headers一样使用`cookies`属性即可:

~~~python
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

r.cookies['example_cookie_name']
# 'example_cookie_value'
~~~

以下函数可以分解浏览器获得的cookies字符串到一个字典,从而帮助我们模拟requests请求.

~~~python
def browsercookiesdict(s):
	'''Covert cookies string from browser to a dict'''
	ss=s.split(';')
	outdict={}
	for item in ss:
		i1=item.split('=',1)[0].strip()
		i2=item.split('=',1)[1].strip()
		outdict[i1]=i2
	return outdict
~~~

------
