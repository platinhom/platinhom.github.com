---
layout: post
title: Pybel和OpenBabel的安装
date: 2015-10-11 12:37:28
categories: CompCB
tags: CompChem Python ChemInfo
---

openbabel是个好工具.但是要想实现跨平台使用, 就要保证在各平台上都能安装...window安装是最简易的, 直接装就好了, 不建议使用mingw或cygwin来安装. 安装OpenBabel下载地址:[Openbabel-SF](http://sourceforge.net/projects/openbabel/),安装Pybel下载地址: [Openbabel-Python-SF](http://sourceforge.net/projects/openbabel/files/openbabel-python/), 经使用pybel 1.8+配合openbabel 2.3.2好使. 装好就能使用图形界面, 命令行, python处理了.

----

下面是重点: 在mac和linux上安装, 也就是源码安装. 在SF上提供2.3.1的mac包, 但没有2.3.2的. 他也提供[源码下载](http://sourceforge.net/projects/openbabel/files/openbabel/2.3.2/).linux上安装所谓稳定版也有点问题.而mac所谓推荐使用的ibabel绑定的是2.3.1的.

这里先说直接成功的安装方法...openbabel使用cmake方法安装, 比较傻,自己检查,生成Makefile. 一般而言就是cmake, 然后make, 测试一下make test, 再sudo make install.

## 预备

安装以下的工具(已装有可忽略,分别brew install 名字   即可):

- cc c++编译器:废话
- cmake: openbabel安装生成makefile需要
- eigen (version>2): 安装其余语言绑定时需要(可选)
- wxWidgets: GUI图形界面需要(可选,可以用obgui打开图形界面)
- Cairo: PNG生成需要(可选)
- zlib: 压缩文件需要(可选)
- libxml2: cml/xml文件处理需要(可选)
- pil: 用来画2D分子显示. 已经不怎么更新,die掉了,推荐使用folk的pillow.

### PIL的问题:  

- PIL不再更新了,所以推荐使用pillow. `pip install pillow` (装有PIL 请pip uninstall PIL). 
- PIL的类, 如Image是直接用的,如pillow则是 PIL.Image. 因此, 我们对文件的头import部分需要进行修改
- 在pybel.py文件内(如*/usr/local/lib/python2.7/site-packages/*目录下),找到 *import Image as PIL* 和 *import ImageTk as piltk*, 改为**from PIL import Image as PIL** 和 **from PIL import ImageTk as piltk**. OK. 保存. 或者使用`pip install pil-compat` 安装一个软件,可以转化pillow为pil.
- 在python中执行`import Tkinter as tk; tk._test()`测试tk好使不. 好使的话, 再`help(tk)`直接跳到底部看版本.例如8.6, 8.5(记住!)
- 查看PIL此时的_imagingtk.so的库连接信息: `otool -L /usr/local/lib/python2.7/site-packages/PIL/_imagingtk.so` (目录可能有所差异), 看看现在链接的库是不是如`/System/Library/Frameworks/Tk.framework/Versions/8.5/Tk`,如果链接的版本和Tkinter的tk版本不同, 会报错!!
- 重新链接: 跑到_imagingtk.so所在目录下,执行 `install_name_tool -change /System/Library/Frameworks/Tk.framework/Versions/8.5/Tk /usr/local/Cellar/tcl-tk/8.6.4/lib/libtk8.6.dylib _imagingtk.so`. 这句命令是更改库文件的连接库, 将原来的8.5的库定向到8.6的库上. 当然这句命令根据自己机子情况更改了. 另外tcl也要相应更改(我找了半天才知道Tk和Tcl这里两个原链接是动态库 囧...).
- 这时再在python测试: `from PIL import Image as PIL; from PIL import ImageTk as piltk; import Tkinter as tk; root=tk.Yk(); pic=Image.open("test.jpeg");imagedata=piltk.PhotoImage(pp)`如果没有segment fault, 恭喜~

## Mac

- 先安装好git, 没有就brew install git. (没有brew就装!)
- `git clone https://github.com/openbabel/openbabel`, 安装github上的版本
- `cd openbabel;mkdir build; cd build` 新建一个文件夹,进入里面
- `cmake ../ -DBUILD_GUI=ON -DPYTHON_BINDINGS=ON -DRUN_SWIG=ON` 这里需要装pybel, 需要用swig转换c++对象给python,openbabel-python_wrap.cpp,所以不同于官网说明, 需要打开`-DRUN_SWIG=ON`. 另外也可以.configure --prefix=path/来指明的,cmake可以用`-DCMAKE_INSTALL_PREFIX=~/Tools`
- 若是mac系统使用brew, 请参考bug error处理修改`libpython2.7.dylib`的位置.
- `make`, 漫长等待(可以`make -j2` 来指定双核并行)
- `make test` 检查是否报错.我用的github版本检查153项, 2.3.2检查60项.注意有无fail. 很容易fail在最后三项pybel相关的.
- `sudo make install` 将相关文件复制安装到相应目录. 之后可以python, import pybel测试.
- 要是之前生成过别的版本,可以删除相关垃圾: 生成openbabel的lib在:**/usr/local/lib/openbabel**,share文件在**/usr/local/share/openbabel/**,可以删掉没用的版本.
- 最后这个openbabel的文件夹可以整个删掉了.

PS: 进一步测试:python之后,`import pybel; mol = pybel.readstring("smi", "CC(=O)Br"); mol.make3D(); print(mol.write("sdf"))`,测试显示还可以`mol.draw()`

PS: 这里有个帖子很厉害的人搞的[openbabel-homebrew](https://github.com/mcs07/homebrew-cheminformatics),我没测试..我见他还要安装rdkit就不想弄了.

### bug error (可忽略)

- 当使用cmake后再使用make时报错:

~~~
alias.h:19:
/Users/Hom/Downloads/openbabel-2.3.2/include/openbabel/shared_ptr.h:25:14: fatal error:
      'tr1/memory' file not found
    #include <tr1/memory>
~~~

  - 原因: 参考这个[帖子](http://forums.openbabel.org/OpenBabel-2-3-2-and-OS-X-10-9-td4656759.html), 原因是OS X 10.9以后clang使用libc++库而不是libstdc++库. libc++ 提供 C++11库, 而libstdc++ 提供 C++03 库支持 tr1.
  - 解决办法: 使用libstdc++库.编辑build目录下cmake生成的`CMakeCache.txt`文件,这个文件是cmake重要参数. 修改其中的*CMAKE_CXX_FLAGS:STRING=*为`CMAKE_CXX_FLAGS:STRING=-stdlib=libstdc++`, 就可以解决. 另外更方便的方法是: `cmake ../ -DBUILD_GUI=ON -DPYTHON_BINDINGS=ON -DRUN_SWIG=ON -DCMAKE_CXX_FLAGS=-stdlib=libstdc++`使用-D定义.
  - 曾经尝试: 使用指定linux版(brew安装)c++/cc/g++/gcc来代替clang,失败. *cmake ../ -DBUILD_GUI=ON -DPYTHON_BINDINGS=ON -DCMAKE_CXX_COMPILER=g++-4.9 -DCMAKE_C_COMPILER=gcc-4.9* 原因是编译测试失败.

- 同样cmake后make报错:

~~~
/usr/local/Cellar/wxmac/3.0.2/include/wx-3.0/wx/strvararg.h:25:14: fatal error: 'type_traits' file
      not found
    #include <type_traits>
~~~

这个问题是wxWidgets在stdc++的问题了. 此时..只能不安装.`cmake ../ -DBUILD_GUI=OFF -DPYTHON_BINDINGS=ON -DRUN_SWIG=ON -DCMAKE_CXX_FLAGS=-stdlib=libstdc++`. (但我随后测试依然pybel挂掉,放弃治疗了,但一般的openbabel还是能用的)

- make test时报错最后三项fail

~~~
        Start 151: pybindtest_bindings
151/153 Test #151: pybindtest_bindings ..............***Failed    1.48 sec
        Start 152: pybindtest__pybel
152/153 Test #152: pybindtest__pybel ................***Failed    0.72 sec
        Start 153: pybindtest_example
153/153 Test #153: pybindtest_example ...............***Failed    0.73 sec
~~~

注意上面make或make install 过程是否安装了pybel: 

~~~
-- Installing: /usr/local/lib/python2.7/site-packages/_openbabel.so
-- Installing: /usr/local/lib/python2.7/site-packages/openbabel.py
-- Installing: /usr/local/lib/python2.7/site-packages/pybel.py
~~~

没有的话,注意是否开启了cmake的`-DPYTHON_BINDINGS=ON -DRUN_SWIG=ON`加上一般就会调用swig安装这三个文件(其实pybel也就这三个文件).

如果安装了, 那就运行python,然后import pybel 一下: 我出现这个:

~~~
import pybel
Fatal Python error: PyThreadState_Get: no current thread
[1]    31380 abort      python
~~~

这个问题是我的动态库设置的问题, 我的python版本注册的主程序是正常的在brew内的,但使用的lib地址有点问题(虽然/usr/lib也是个软链接,但这里的结果不太好).修正这个问题只需更改CMakeCache.txt里的`/usr/lib/libpython2.7.dylib`的路径为`/usr/local/Frameworks/Python.framework/Versions/2.7/lib/libpython2.7.dylib` 即可.总共有三处. 如果你的python依然有问题,参考[Mac Install Python](https://wolfpaulus.com/journal/mac/installing_python_osx/). (用brew其实brew update; brew upgrade python即可)

- 使用pip或者相应的包([openbabel-1.8.4.tar.gz](https://pypi.python.org/pypi/openbabel)):

pip原理也是抓取网上的2.3.2然后setup.py, 将带有的openbabel-python_wrap.i 用swig转为cpp并转为相应的`_openbabel.o`和两个py文件. 然并卵, 因为2.3.2的bug. 所以pip方法最后怎样都解决不了. 不过要是能正常弄2.3.2的话,pip方法最为简单了.

## Linux

我这里使用的是HPCC. 也是使用git clone 来下载github版本, 然后也是cmake安装. 和Mac相比有两个问题:

1. 集群软件.例如我需要module load Eigen 这样, 保证一些基础软件能找到.
2. 集群默认安装位置权限. 默认位置/usr/local/在公共机子里很可能是没有权限的.

解决第二个问题,要以下方法:

1. cmake命令时加入 `-DCMAKE_INSTALL_PREFIX=~/local` 将默认安装的地方由/usr/local改为~/local

可以在cmake中设置,也可以修改CMakeCache.txt(有很多项相应要修改!)相应项来获取.随后即可安装,出问题再参考上面的.

安装后,将下面的内容写入到`~/.bashrc`文件. 

~~~bash
export PYTHONPATH="/mnt/home/zhaozx/local/lib/python2.7:/mnt/home/zhaozx/local/lib/python2.7/site-packages:$PYTHONPATH"
export LD_LIBRARY_PATH="/mnt/home/zhaozx/local/lib:$LD_LIBRARY_PATH"
export C_INCLUDE_PATH="/mnt/home/zhaozx/local/include:$C_INCLUDE_PATH"
export BABEL_DATADIR="/mnt/home/zhaozx/local/share/openbabel/2.3.90"
export BABEL_LIBDIR="/mnt/home/zhaozx/local/lib/openbabel/2.3.90"
~~~

不加的话找不到支持文件类型会卡住, 内存不停涨.

## Reference

1. [Python Package Index: openbabel](https://pypi.python.org/pypi/openbabel)
2. [Install Python bindings](http://open-babel.readthedocs.org/en/latest/UseTheLibrary/PythonInstall.html)
3. [ibabel](http://openbabel.org/wiki/IBabel)
4. [SWIG](https://en.wikipedia.org/wiki/SWIG), [官网](http://www.swig.org/)
5. [Pybel](http://open-babel.readthedocs.org/en/latest/UseTheLibrary/Python_Pybel.html); [PyBel-API](http://open-babel.readthedocs.org/en/latest/UseTheLibrary/Python_PybelAPI.html#pybel-api)
6. [Openbabel install](http://open-babel.readthedocs.org/en/latest/Installation/install.html)



------
