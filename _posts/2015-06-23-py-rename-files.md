---
layout: post
title: Python-批量文件重命名(ZZ)
date: 2015-06-23 07:34:18
categories: Coding
tags: Python ZZ
---

### 转载: [Python - 批量文件重命名](http://www.cnblogs.com/tracydj/archive/2011/01/27/1945861.html)

- 两个目标两个：

1. 输入一组文件名，进行批量重命名；
2. 输入一组目录名，批量重命名各个目录下的文件。

- 附加功能：

1. 可根据文件的创建日期对文件重新排序；
2. 重命名方式为递增数列，可带前后缀；
3. 可以指定输出目录，如果不指定输出目录，则在原文件夹中重命名，默认为在原文件夹中进行重命名；
4. 可指定在重命名后删除原文件（只有输出目录不同时有效），默认为不删除。

~~~python
import os

# 获取目录下的子目录
def subdirs(path):
    dl = [];
    for i in os.walk(path, False):
        for d in i[1]:
            dl.append(os.path.join(path, d))
    return dl

# 获取目录下的子文件
def subfiles(path):
    fl = [];
    for i in os.walk(path, False):
        for f in i[2]:
            fl.append(os.path.join(path, f))
    return fl

# 根据文件创建时间对文件进行排序
def fsort(files):
    files.sort(key = lambda s: os.path.getctime(s))
    return files

# 递增数列生成器
class gen:
    def __init__(self, prefix = '', suffix = '', seed = 1, digit = 3):
        self.prefix = prefix
        self.suffix = suffix
        self.seed = seed
        self.digit = digit
        self.it = seed - 1
    
    def gennext(self):
        self.it += 1
        return '{0}{1:0{3}d}{2}'.format(self.prefix, self.it, self.suffix, self.digit)

    def copy(self):
        return gen(self.prefix, self.suffix, self.seed, self.digit)

class renamer:
    def __init__(self, files, ngen = None, delsrc = False, output = ''):
        self.it = 0
        self.total = 0
        self.files = files
        self.delsrc = delsrc
        self.target = output
        if(ngen is None): self.namegen = gen()
        elif(isinstance(ngen, gen)): self.namegen = ngen
        else: raise(TypeError, 'ngen参数只接受gen类型的对象')

    def rename(src, des, delsrc):
        os.rename(src, des)
        if(delsrc == True):
            os.remove(src)

    def run(self):
        self.it = 0
        self.total = len(self.files)
        for f in self.files:
            dn = os.path.dirname(f)
            ex = os.path.splitext(f)
            nn = self.namegen.gennext() + ex[1]
            np = ''
            sd = self.target == ''
            if(sd):
                np = os.path.join(dn, nn)
            else:
                np = os.path.join(self.target, nn)
            print('rename: %s' %(np))
            renamer.rename(f, np, sd and self.delsrc)
            self.it += 1
        print('%d work(s) done' %(self.it))
        print()

# 重命名给定列表中的所有文件
def fs_rename(files, resort = False, ngen = gen(), delsrc = False, output = ''):
    if(resort): fsort(files)
    rn = renamer(files, ngen.copy(), delsrc, output)
    rn.run()

# 重命名给定目录中的所有文件
def ds_rename(dirs, resort = False, ngen = gen(), delsrc = False, output = ''):
    for d in dirs:
        fs = subfiles(d)
        if(resort): fsort(fs)
        print('%d file(s) in %s' %(len(fs), d))
        if(output == '') ngen = ngen.copy()
        rn = renamer(fs, ngen, delsrc, output)
        rn.run()
~~~

### 说明:  

- fs_rename方法对一组文件进行批量重命名。  
参数说明:  
  - files: 文件列表；
  - resort: 是否重新排列文件（按创文件建时间），默认为False；
  - ngen: 一个gen类型的对象，用于产生文件名；
  - delsrc: 是否删除原文件，默认为False；
  - output: 输出路径，默认为''，表示在原文件家中重命名。
- ds_rename方法对一组目录中的文件进行批量重命名。  
参数说明： 
  - dirs: 目录列表；
  - resort: 是否重新排列文件（按创文件建时间），默认为False；
  - ngen: 一个gen类型的对象，用于产生文件名；
  - delsrc: 是否删除原文件，默认为False；
  - output: 输出路径，默认为''，表示在原文件家中重命名。
- gen类型构造函数创建数列发生器。  
参数说明：  
  - prefix: 前缀字符串；
  - suffix: 后缀字符串；
  - seed: 起始数；
  - digit: 数为宽，不够用0补齐。
- subdirs方法获取一个目录下的子目录，并返回完整路径。
- subfiles方法获取一个目录下的所有文件，并返回完整路径。
- fsort方法对一组文件根据其创建时间进行重新排序。

---
