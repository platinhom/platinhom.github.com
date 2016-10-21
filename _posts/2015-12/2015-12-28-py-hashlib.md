---
layout: post
title: Python:hashlib库
date: 2015-12-28 01:55:02
categories: Coding
tags: Python
---

hashlib库支持把字符串等进行hash加密处理, 加密后生成的字符串可以用于验证输入是否相等,但又不能直接翻译出原本的内容, 从而实现安全保全和验证. 在检查数字签名时也经常用到hash处理.  
secure hash和message digest 是一个概念, 现在更流行前者的用法.

- sha的全称是secure-hash algorithm, 有各种不同的算法.
- md5的全称是message-digest algorithm 5（信息-摘要算法）, 在90年代初由mit laboratory for computer science和rsa data security inc的ronald l. rivest开发出来，经md2、md3和md4发展而来。它的作用是让大容量信息在用数字签名软件签署私人密匙前被“压缩”成一种保密的格式（就是把一个任意长度的字节串变换成一定长的大整数）。

### hashlib库

import hashlib 即可

- 算法名([context]) : 构造出一个对应算法的hash对象. 可以指定内容context. 例如 `md5()`, `sha1()`, `sha224()`, `sha256()`, `sha384()` 和 `sha512()`.
- new('算法名') : 和上类似, 使用算法名去构造, 可以构造出非内建的算法hash对象. 一般使用上述方法构建hash对象更好.
- pbkdf2_hmac(name, password, salt, rounds, dklen=None)
- algorithm : 返回保证这个模块可以支持的算法的tuple
- algorithms_guaranteed : 返回保证这个模块可以在所有平台都支持的算法的set  
^
> 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'
^
- algorithm_available : 返回当前环境支持的算法名.可能有重复. 
^
> 'DSA', 'DSA-SHA', 'MD4', 'MD5', 'MDC2', 'RIPEMD160', 'SHA', 'SHA1', 'SHA224', 'SHA256', 'SHA384', 'SHA512', 'dsaEncryption', 'dsaWithSHA', 'ecdsa-with-SHA1', 'md4', 'md5', 'mdc2', 'ripemd160', 'sha', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'whirlpool'
^
- pbkdf2_hmac(hash\_name, password, salt, iterations, dklen=None) : Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as pseudorandom function. 第一个参数是hash方法名, 后面是密码, salt可能用于派生键过程随机化相关,要求大于16byte. iterations,建议大于10000. dklen是派生键的长度, 不给定时使用算法对应digest size. 一个用于给密码加密的方法. 总之password和salt都会影响产生的结果.

~~~python
>>> import hashlib, binascii
>>> dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
>>> binascii.hexlify(dk)
b'0394a2ede332c9a13eb82e9b24631604c31df978b4e2f0fbd2c549944f9d79a5'
~~~

### hash对象

通过md5()或者new('md5')等方法构造出来的hash对象.

- name : 使用的算法名, 例如md5
- digest_size : hash出来字符串的字节数.
- block_size : hash算法使用的block的大小
- **update**(str) : 更新hash对象的内容, 多次用update实际等于将字符串进行**串联**.
- digest() : 将现有的内容hash化成字符串, 字符串大小等于digest_size, 可能含有很多非ascii的字符
- **hexdigest**() : double长度的字符串,只含有16进制字符. **最常用**的方法
- copy() : 克隆当前的hash对象并返回新hash对象. 好处是可以对相同的头使用同一个hash对象,分支再在其基础上update.

~~~python
>>> hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()
'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'
~~~

和base64的不同, base64可以加密和解密, hash法只能加密不能解. 要解只能用暴力破解咯. 但由于可调参数多, 所以其实都不好破.

----

一个可以在线计算各种HASH值的[网站](http://www.whatsmyip.org/hash-generator/).  

一篇介绍加密编码和破解的[博客](http://simeon.blog.51cto.com/18680/217051/)

[Python Library hashlib](https://docs.python.org/2/library/hashlib.html)

------
