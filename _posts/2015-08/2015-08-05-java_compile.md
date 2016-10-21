---
layout: post
title: JAVA编译
date: 2015-08-05 14:12:27
categories: Coding
tags: Java
---

今天使用一个分子描述符的软件,下载源码后里面全是`.java`源文件,不能编译. 查了一下编译过程, 总结一下.

## [JRE](https://zh.wikipedia.org/wiki/JRE) (Java Runtime Environment)

是一个软件, 可以让电脑执行java程序,内部具有JVM和一些标准的类函数库.可以认为是电脑中运行java最小需求软件包.一般说的升级java其实是指升级JRE.

## [JVM](https://zh.wikipedia.org/wiki/Java%E8%99%9A%E6%8B%9F%E6%9C%BA), (Java Virtual Machine)
JAVA虚拟机,能够运行java字节码的虚拟机.Java虚拟机有自己完善的硬体架构，如处理器、堆栈、寄存器等，还具有相应的指令系统。JVM屏蔽了与具体操作系统平台相关的信息，使得Java程序只需生成在Java虚拟机上运行的目标代码（字节码），就可以在多种平台上不加修改地运行。一般地,java编译器(如javac)将java源码编译为`.class`文件(字节码),再交由JVM(java程序)解释执行. 任何正确编译成java bytecode的都可以在JVM上运行.

## [JDK](https://zh.wikipedia.org/wiki/JDK) (Java Development Kit)

就是JAVA开发用的免费软件开发工具包(SDK), 最为广发使用. 开发者一般才需要, 用户一般只需要安装JRE就可以运行java了. 开发者利用JDK编译调试程序.里面包括javac,java,jar等等程序. JDK一般比较大,还包括了完整的JRE.

- javac – 编译器，将后缀名为.java的源代码编译成后缀名为.class的字节码
- java – 运行工具，运行.class的字节码
- jar – 打包工具，将相关的类文件打包成一个文件
- javadoc – 文档生成器，从源码注释中提取文档，注释需符合规范
- jdb debugger - 调试工具
- jps – 显示当前java程序运行的进程状态
- javap – 反编译程序
- appletviewer – 运行和调试applet程序的工具，不需要使用浏览器
- javah – 从Java类生成C头文件和C源文件。这些文件提供了连接胶合，使Java和C代码可进行交互
- javaws – 运行JNLP程序
- extcheck – 一个检测jar包冲突的工具
- apt – 注释处理工具
- jhat – java堆分析工具
- jstack – 栈跟踪程序
- jstat – JVM检测统计工具
- jstatd – jstat守护进程
- jinfo – 获取正在运行或崩溃的java程序配置信息
- jmap – 获取java进程内存映射信息
- idlj – IDL-to-Java编译器。将IDL语言转化为java文件
- policytool – 一个GUI的策略文件创建和管理工具
- jrunscript – 命令行脚本运行

### 一般编译

1. `javac [options] [sourcefiles] [@files]`  
- @可以指定一个文件名,该文件包含要编译的源文件名.  
- -d 选项指定class文件存放位置.默认存放在当前目录  
- -classpath 搜索编译所需的class文件，指出编译所用到的class文件的位置
- -sourcepath用于搜索编译所需的源文件（即java文件），指定要搜索的源文件的位置，如jar、zip或其他包含java文件的目录  
2. `java [options] classfile`  
- classfile这里*com.csdn.javacode.EncryptClasses* 前面相当于javac时的路径`com/csdn/javacode/EncryptClasses.java`生成的相应的class.直接运行它.
-  -classpath 指定要执行的文件所在的位置以及需要用到的类路径，包括jar、zip和class文件目录  
3. `jar cvf hello.jar hello.class world.class`  
将class文件打包为jar. 和tar差不多..jar可以作为库,也可以直接运行.  

## ANT
ANT是基于java的,可以认为是java版本的make,用于对 *build.xml* 内容进行相应编译操作.

### 安装

- 首先需要安装JDK, 指明JAVA_HOME环境变量为安装后JDK所在的目录; 还有说要加入jdk的bin到PATH,并设置CLASS\_PATH.
- 其次要下载安装[Apache Ant](http://ant.apache.org/bindownload.cgi), 下载一个zip包解压后,环境变量**ANT_HOME**指明ANT文件夹地址,并将子文件夹bin加到环境变量path.(如: `ANT_HOME:D:\apache-ant-1.8.2,PATH:%ANT_HOME%\bin`)
- 最后使用需要一个build.xml 文件,相当于make的makefile. [ANT build.xml文件详解](http://my.oschina.net/willSoft/blog/29314), [ANT-build.xml文件详解2](http://www.blogjava.net/zhengtengfeng/archive/2007/04/20/zhtfeng.html), [Java Ant build.xml详解(带例子)](http://www.cnblogs.com/wufengxyz/archive/2011/11/24/2261797.html)
- 然后在有build.xml的文件夹内,敲`ant` 就可以了(环境变量存在前提下)~


*ant [options] [target [target2 [target3] ...]]*  
Options:

-  -help, -h              print this message and exit
-  -projecthelp, -p       print project help information and exit
-  -version               print the version information and exit
-  -diagnostics           print information that might be helpful to diagnose or report problems and exit
-  -quiet, -q             be extra quiet
-  -silent, -S            print nothing but task outputs and build failures
-  -verbose, -v           be extra verbose
-  -debug, -d             print debugging information
-  -emacs, -e             produce logging information without adornments
-  -lib <path>            specifies a path to search for jars and classes
-  -logfile <file>        use given file for log
-    -l     <file>                ''
-  -logger <classname>    the class which is to perform logging
-  -listener <classname>  add an instance of class as a project listener
-  -noinput               do not allow interactive input
-  -buildfile <file>      use given buildfile
-    -file    <file>              ''
-    -f       <file>              ''
-  -D<property>=<value>   use value for given property
-  -keep-going, -k        execute all targets that do not depend on failed target(s)
-  -propertyfile <name>   load all properties from file with -D properties taking precedence
-  -inputhandler <class>  the class which will handle input requests
-  -find <file>           (s)earch for buildfile towards the root of
-    -s  <file>           the filesystem and use it
-  -nice  number          A niceness value for the main thread: 1 (lowest) to 10 (highest); 5 is the default
-  -nouserlib             Run ant without using the jar files from ${user.home}/.ant/lib
-  -noclasspath           Run ant without using CLASSPATH
-  -autoproxy             Java1.5+: use the OS proxy settings
-  -main <class>          override Ant's normal entry point


## Reference
1. [Apache ANT](http://ant.apache.org/index.html)

------
