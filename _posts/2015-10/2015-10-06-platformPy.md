---
layout: post
title: Python:platform模块
date: 2015-10-06 04:57:11
categories: Coding
tags: Python
---

platform模块用来获得操作系统, 系统架构, python信息等.做相关版本区分执行相应命令时很有用.

2.7中ver=1.0.7的platform:

### 操作系统相关

- system() : 操作系统类型(见例)
- version(): 操作系统版本
- release(): 操作系统发布号, 例如win 7返回7, 还有如NT, 2.2.0之类.
- platform(aliased=0, terse=0): 操作系统信息字符串,扥与system()+win32_ver()[:3]
- win32_ver(release='', version='', csd='', ptype=''): win系统相关信息
- linux\_distribution(distname='', version='', id='', supported\_dists=('SuSE', 'debiaare', 'yellowdog', 'gentoo', 'UnitedLinux', 'turbolinux'), full\_distribution_name=1): Linux系统相关信息
- dist(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'fedora', 'redhat', 'centos', 'mandrake', 'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo', 'UnitedLinux', 'turbolinux')): 尝试获取Linux OS发布版本信息.返回(distname,version,id). dist是发布版本的意思.
- mac_ver(release='', versioninfo=('', '', ''), machine=''): mac版本
- java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', '')): java版本
- libc_ver(executable=r'c:\Python27\python.exe', lib='', version='', chunksize=2048): libc版本,linux相关吧.

以上相应版本查询的返回元组和其形参对应.

~~~python
platform.system()
'Linux' # python 3.3.2+ 64 bits on debian jessie 64 bits
'Windows' # python 3.3.2 32 bits on windows 8.1 64 bits
'Windows' # python 3.3.2 64 bits on windows 8.1 64 bits
'Darwin' # python 3.4.1 64 bits on mac os x 10.9.4
'Java' 

platform.version()
'#1 SMP Debian 3.10.11-1 (2013-09-10)' # python 3.3.2+ 64 bits on debian jessie 64 bits
'6.2.9200' # python 3.3.2 32 bits on windows 8.1 64 bits
'6.2.9200' # python 3.3.2 64 bits on windows 8.1 64 bits
'Darwin Kernel Version 13.3.0: Tue Jun  3 21:27:35 PDT 2014; root:xnu-2422.110.17~1/RELEASE_X86_64' # python 3.4.1 64 bits on mac os x 10.9.4

platform()
'Windows-7-6.1.7601-SP1'

win32_ver()
('7', '6.1.7601', 'SP1', u'Multiprocessor Free')

platform.dist()
('debian', 'jessie/sid', '') # python 3.3.2+ 64 bits on debian jessie 64 bits

~~~

### 系统信息

- uname(): 返回元组,system, node, release, version, machine, processor.
- architecture(executable=r'c:\Python27\python.exe', bits='', linkage=''): 系统架构
- machine() : CPU平台,AMD,x86?(见例)
- node() : 节点名(机器名,如Hom-T400)
- processor() : CPU信息
- system_alias(system, release, version): 返回相应元组..没何屌用.

~~~python
platform.architecture()
('64bit', 'ELF') # python 3.3.2+ 64 bits on debian jessie 64 bits
('32bit', 'WindowsPE') # python 2.7.2 32 bits on windows 7 64 bits
('64bit', 'WindowsPE') # python 3.3.2 64 bits on wndows 8.1 64 bits
('64bit', '') # python 3.4.1 64 bits on mac os x 10.9.4

platform.machine()
'x86_64' # python 3.3.2+ 64 bits on debian jessie 64 bits
'AMD64' # python 3.3.2 32 bits on windows 8.1 64 bits
'AMD64' # python 3.3.2 64 bits on windows 8.1 64 bits
'x86_64' # python 3.4.1 64 bits on mac os x 10.9.4

platform.node()
'Hom-T400' 

platform.processor()
'Intel64 Family 6 Model 23 Stepping 10, GenuineIntel'

platform.uname()
('Windows', 'Hom-T400', '7', '6.1.7601', 'AMD64', 'Intel64 Family 6 Model 23 Stepping 10, GenuineIntel')

uname_result(system='Linux', node='work', release='3.10-3-amd64', version='#1 SMP Debian 3.10.11-1 (2013-09-10)', machine='x86_64', processor='') # python 3.3.2+ 64 bits on debian jessie 64 bits
 
uname_result(system='Windows', node='work-xxx', release='8', version='6.2.9200', machine='AMD64', processor='Intel64 Family 6 Model 58 Stepping 9,GenuineIntel') # python 3.3.2 32 bits on windows 8.1 64 bits
 
uname_result(system='Darwin', node='mba', release='13.3.0', version='Darwin Kernel Version 13.3.0: Tue Jun  3 21:27:35 PDT 2014; root:xnu-2422.110.17~1/RELEASE_X86_64', machine='x86_64', processor='i386') # python 3.4.1 64 bits on mac os x 10.9.4

~~~

### python相关

- python_version(): py版本号
- python_branch(): python分支(子版本信息),一般为空.
- python_build(): python编译号(default)和日期.
- python_compiler(): py编译器信息
- python_implementation(): python安装履行方式,如CPython, Jython, Pypy, IronPython(.net)等.
- python_revision(): python类型修改版信息,一般为空.
- python\_version\_tuple():python版本号分割后的tuple.
- popen(cmd, mode='r', bufsize=None): portable popen() 接口,执行各种命令.

~~~python
python_verison()
'3.3.2+' # python 3.3.2+ 64 bits on debian jessie 64 bits
'3.3.3' # python 3.3.2 32 bits on windows 8.1 64 bits
python_version_tuple()
('2', '7', '2')
python_build()
('default', 'Jun 12 2011 15:08:59')
python_compiler()
'MSC v.1500 32 bit (Intel)'
pl.python_implementation()
'CPython'
~~~

------
