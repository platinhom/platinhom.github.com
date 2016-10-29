---
layout: post
title: Selenium控制Chrome初探
date: 2016-02-02 00:01:09
categories: IT
tags: Software Python Internet
---

#### 安装selenium模块:

`pip install selenium`

#### 下载ChromeDriver

首先去下载ChromeDriver的控制程序 [ChromeDriver下载](https://sites.google.com/a/chromium.org/chromedriver/downloads)

下载后, 放到一个位置, 在用selenium时调用webdriver时需要调用ChromeDriver(要知道路径). 这里假设把运行脚本和ChromeDriver放在一个目录下, 使用getcwd获取路径. 也可以使用一个自定义路径, 这时就可以用该绝对路径来定义启动位置.

~~~python
import os, time
from selenium import webdriver
cwd = os.getcwd() + '/'
driver = webdriver.Chrome(cwd + 'chromedriver') # 设置chromedriver, 执行后会打开一个新的浏览器窗口
driver.get('http://www.google.com/'); # 设置浏览器前往位置
time.sleep(3) # 等待3秒缓冲
search_box = driver.find_element_by_name('q') # 取得搜索框,用name去获取DOM
search_box.send_keys('Github') # 在搜尋框內輸入 'Github'
search_box.submit() # 令 chrome 按下 submit按钮.
time.sleep(5) # 缓冲5秒
driver.quit() # 关闭chromedriver(关闭浏览器)
~~~

还有

- `clicksave=driver.find_element_by_id('save')` 这样根据id获取DOM对象
- `clicksave.click()` 模拟点击按钮

例如我抓取sci-hub的文献:

~~~python
import os, time
from selenium import webdriver
cwd = os.getcwd() + '/'
driver = webdriver.Chrome(cwd + 'chromedriver')
driver.get("http://sci-hub.io/10.1021/a19600193")
# Also can use: `driver.get("http://sci-hub.io/10.1021/a19600193?download=True")` directly download
elem=driver.find_element_by_id('save')
elem.click()
# Or more operation in iteration
driver.quit()
~~~

先就简介一下吧, 没空深入研究..待续...

# Reference

1. [Introducing the Selenium Webdriver API by Example](http://docs.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example)
2. [Python Selenium 2.0 Documentation](http://selenium.googlecode.com/svn/trunk/docs/api/py/index.html)
3. [Selenium Documentation](http://docs.seleniumhq.org/docs/)
4. [ChromeDriver-Wiki](https://code.google.com/p/selenium/wiki/ChromeDriver)和[list](https://code.google.com/p/selenium/w/list)



------

