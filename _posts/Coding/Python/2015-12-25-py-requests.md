---
layout: post
title: Python:Requests外插
date: 2015-12-25 05:26:58
categories: Coding
tags: Python
---

Requests 就是熟知的[Requests: HTTP for Humans](http://cn.python-requests.org/zh_CN/latest/) , 是个开源在[Github](https://github.com/kennethreitz/requests/)上的项目. 功能十分强大. 而且十分方便, 除了一般的网络连接功能外, 基本支持所有HTTP 的动作, 另外还可以很方便操作cookie, 保持session等. requests实际封装了[urllib3](https://urllib3.readthedocs.org/en/latest/)([Github](https://github.com/shazow/urllib3)). 

安装: `pip install requests` 搞掂...

<iframe src="http://cn.python-requests.org/zh_CN/latest/" width="100%" height="600px"></iframe>

## 基本使用

使用相应函数返回 **Response** 对象. 然后就对该对象调用方法或属性进行进一步操作.

可以使用各种HTTP类型请求来获取响应对象, 最常用是get的方法.

- requests.get(url, *args): 打开网页, 并获取响应对象. 
- requests.post(url, *args): 
- requests.put
- requests.delete
- requests.patch
- requests.request (需要使用Request)
- requests.head
- requests.options

更多相关网络处理工具在`requests.utils`里, 而加载的包可以在`requests.packages` 找到(absolute_import,sys,urllib3,chardet).

requests.utils有以下工具 (其实很多内建库, 所以可以加载requests来简单使用 `from requests.utils import *`):

- `CaseInsensitiveDict`
- `DEFAULT_CA_BUNDLE_PATH`
- `FileModeWarning`
- `InvalidURL`
- `NETRC_FILES`
- `OrderedDict`
- `RequestsCookieJar`
- `UNRESERVED_SET`
- `add_dict_to_cookiejar`
- `address_in_network`
- `basestring`
- `builtin_str`
- `bytes`
- `certs`
- `cgi`
- `codecs` : 一般的codecs库.
- `collections`
- `cookiejar_from_dict`
- `default_headers`
- `default_user_agent`
- `dict_from_cookiejar`
- `dict_to_sequence`
- `dotted_netmask`
- `from_key_val_list`
- `get_auth_from_url`
- `get_encoding_from_headers`
- `get_encodings_from_content`
- `get_environ_proxies`
- `get_netrc_auth`
- `get_unicode_from_response`
- `getproxies`
- `guess_filename`
- `guess_json_utf`
- `io` : 一般的io库
- `is_ipv4_address`
- `is_py2`
- `is_valid_cidr`
- `iter_slices`
- `os` : 一般的os库, 包括os.path哦
- `parse_dict_header`
- `parse_header_links`
- `parse_list_header`
- `platform`
- `prepend_scheme_if_needed`
- `proxy_bypass`
- `quote` : url编码化字符串
- `re` : 一般的re库.
- `requote_uri`
- `select_proxy`
- `should_bypass_proxies`
- `socket`
- `str`
- `stream_decode_response_unicode`
- `struct`
- `super_len`
- `sys` : 一般的sys库
- `to_key_val_list`
- `to_native_string`
- `unquote` : 反编码url字符串
- `unquote_header_value`
- `unquote_unreserved`
- `urldefragauth`
- `urlparse`
- `urlunparse`
- `warnings`

### get等方法的功能参数

- params : 传递参数给GET/POST等行为. 实参需要字典.
- allow_redirects : 运行自动跳转, 默认False. 可以设置False禁止跳转.
- timeout : 连接超时的设定, 单位秒的浮点数.
- cookies : 可以设定发送cookies, 实参要字典.
- data : POST传递的数据
- files : 在post时可以上传文件. 看例子.

### Response对象

#### 属性

- url : 获取相应网址, 包括传递的参数如`?key=value,key2=value2`等.
- `text` : 网页响应内容, 一般就是相应网页内容 
- content : 二进制的相应内容, 
- encoding : 网页编码
- `status_code` : 状态吗, int型. 例如404, 正常200. 跳转可能302,303.
- history: 返回请求历史的一个列表. 可以查看出重定向过程. 
- cookies: 返回cookies的一个字典.
- headers: 响应头, 一个字典.

> 注意:

- 防止warning (disable request wanrning): 因为HTTPS的SSL/TLS验证有时经常报warning, 可以通过[关闭urllib3的warning](https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning)来进行:`urllib3.disable_warnings()`, 在requests中是: `requests.packages.urllib3.disable_warnings()`.


### 应用例子

##### 传递参数给操作(例如GET 的参数)

可以传递各种参数给类型请求的方法.

~~~python
# google scholar search shoichet, >=2015 , 3 record per page
searchargv = {'q': 'shoichet', 'as_ylo': '2015', 'num':'3'}
r = requests.get("http://scholar.google.com/scholar", params=payload)
~~~

##### 定制header模拟浏览器

使用headers参数可以自己定制头部, 还可以写成一个多User-Agent的列表, 从中随机挑选一个(`uagents[random.randint(0,len(uagents)-1)]`), 再构建头部, 这样就可以伪装成不同浏览器访问了~~

~~~python
bingacademicurl="http://www.bing.com/academic/"
hdr={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',\
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',\
'Connection':'keep-alive','Content-Encoding': 'gzip','Content-Type': 'text/html; charset=utf-8','Host':'www.bing.com'}
param={"mkt":"zh-CN",'q':"keyword",'first':"1"}
r=requests.get(self.bingacademicurl,params=param,headers=self.hdr)
~~~


##### 获取自动跳转真实地址

~~~python
import urllib2, requests
u=urllib2.urlopen("http://dx.doi.org/10.1016/S1093-3263(00)80106-0")
# -> 报错"HTTPError: HTTP Error 404: Not Found" 
# -> 因为网站有防抓取功能
r = requests.get("http://dx.doi.org/10.1016/S1093-3263(00)80106-0")
print r.url
# -> http://www.sciencedirect.com/science/article/pii/S1093326300801060
print r.text 
#.... 网页html内容
~~~

##### 防止跳转

使用allow_redirects参数可以限制不跳转.

~~~python
r = requests.get("http://dx.doi.org/10.1016/S1093-3263(00)80106-0")
print r.url
# r"http://www.sciencedirect.com/science/article/pii/S1093326300801060"
print r.status_code
# 200
r = requests.get("http://dx.doi.org/10.1016/S1093-3263(00)80106-0", allow_redirects=False)
print r.url
# r"http://dx.doi.org/10.1016/S1093-3263(00)80106-0"
print r.status_code
# 303
~~~

##### 设置timeout和max retries (超时设定和最大尝试数)

- timeout是get/post等的参数, 单位秒. 
- max_retries需要构建一个HTTPAdapter并设置其max\_retries, 最后将该Adaptor加载给requests的Session对象. mount时的链接是前端最大匹配, 使用"http://"和"https://"可以分别对应两大类网址. 也可以更具体针对某网站.   
可以参考讨论: [Cleanly setting max_retries on Python requests get or post method](http://stackoverflow.com/questions/21371809/cleanly-setting-max-retries-on-python-requests-get-or-post-method)和[Can I set max_retries for requests.request?](http://stackoverflow.com/questions/15431044/can-i-set-max-retries-for-requests-request). 

~~~python
#### Example to avoid exceed retry.
# Firstly use a Session
requestsSession = requests.Session()
# Using the HTTPAdapter
requestsAdapterA = requests.adapters.HTTPAdapter(max_retries=3)
# session mount the HTTPAdapter. Use for all the http:// url
requestsSession.mount('http://', requestsAdapterA)
# Another method, directly give the HTTPAdapter. Use for all the https:// url
#requestsSession.mount('https://', requests.adapters.HTTPAdapter(max_retries=3))
# Open the url link
requestsSession.get(url , timeout=20)
~~~

##### 抓取二进制文件如pdf

注意对于二进制文件(如图片,pdf), 打开文件方式应该是`'wb'`, 写入内容应该是`r.content`而不是r.text. 这里加了个根据header的类型判断是否pdf,不是就扔掉. 更好的方法是用`with`来执行啦.

~~~python
def getwebpdf(link,fname):
	'''Get a PDF from a link. if fail, return False'''
	try:
		rpdf=requests.get(link)
		if (rpdf.status_code is 200 and rpdf.headers['Content-Type'].lower().strip()=='application/pdf'):
			fpdf=open(fname,'wb')
			fpdf.write(rpdf.content)
			fpdf.close()
			return True
	except requests.exceptions.ConnectionError:
		print "Error to get pdf linK: "+link+" for file: "+fname
	return False
~~~

##### 上传多个文件 
以一个为例, 相当于把相应post的id对应为一个字典的键.

~~~python
>>> url = 'http://httpbin.org/post'
>>> files = {'file': open('report.xls', 'rb')}
# 还可以设置文件名,类型和请求头:
>>> files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

>>> r = requests.post(url, files=files)
>>> r.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
~~~

更复杂应用可以学习: 

- [使用Python模拟登陆知乎和v2ex](http://iwww.me/395.html)
- [用Python Requests抓取知乎用户信息](http://zihaolucky.github.io/using-python-to-build-zhihu-cralwer/)
- [python模拟登陆登陆一：验证码与cookies的同步处理思路](http://www.dabu.info/python-login-crawler-captcha-cookies.html)

## Reference

1. [快速入门](http://cn.python-requests.org/zh_CN/latest/user/quickstart.htm)
2. [高级入门](http://cn.python-requests.org/zh_CN/latest/user/advanced.html)


------
