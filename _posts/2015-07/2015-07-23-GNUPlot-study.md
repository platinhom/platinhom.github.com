---
layout: post
title: GNUPlot使用
date: 2015-07-22 16:24:55
categories: MathStat
tags: Visualize DataAnal
---

GNUPlot是开源的数据可视化软件(GPL协议).支持多平台,所以被广泛使用.比xmgrace要强大. gnuplot 是命令行驱动的，也可以支持很多非交互式的应用程序, 例如[GNU Octave](http://www.gnu.org/software/octave/), 还可以用于网站的交互出图. gnuplot 可以以批处理模式进行操作，提供了一个命令脚本来生成一个图形.

gnuplot 中有一个对应于 UNIX 的数学库的标准的数学库可以使用。函数的参数支持整型、实型和复型。可以将数学库配置成弧度或角度（默认为弧度）。

## 安装
- Window: 去SF[下载](http://sourceforge.net/projects/gnuplot/files/gnuplot/)exe版本安装.
- Linux/Mac: 同样去SF下载tar.gz版本然后编译
- Mac可以**brew install gnuplot**,前提是装了homebrew.

## 使用
主要使用plot产生2D图片和splot来产生三维图片. 不了解的可以使用 **help command** 来查询细节.

##### 简单的splot应用:

~~~
set samples 25
set isosamples 26
set title "Test 3D gnuplot"
set contour base
set hidden3d offset 1
splot [-12:12.01] [-12:12.01] sin(sqrt(x**2+y**2))/sqrt(x**2+y**2)
~~~
![来自Ref3](https://www.ibm.com/developerworks/cn/linux/l-datavistools/figure1.jpg)

~~~bash
set terminal png ##设置输出格式. set terminal 可以查看所有能用的terminal
set output "output.png" ##设置输出到文件,不设置输出文件名则输出到stdout. show output也是输出到stdout
plot "data.dat" with linespoints  ##将数据文件plot出来,以点线连线的方式
set grid  ##设置网格
set datafile separator "\t" ##设置文件中的分隔符是tab
set xrange [−2*pi:2*pi] ##设置范围
set xlabel "月份" ##设置x轴的注解.同理ylabel
set title "好好学习天天向上"  ##设置plot后的主标题.
unset key ##取消图例,恢复使用set key default
set xtics pi ##设置x主轴的主间距是pi
set mxtics 2 ##设置每个主间距分为2小份(就是中间有个刻度)
replot ##重新执行上次的plot
~~~

## Reference
1. [GNUPlot](http://www.gnuplot.info/)
2. [GNUPlot Tutorial-Duke](http://people.duke.edu/~hpgavin/gnuplot.html)
3. [Linux 上的数据可视化工具](https://www.ibm.com/developerworks/cn/linux/l-datavistools/)
4. [gnuplot调教记](http://www.codelast.com/?p=8348)
5. [使用GNUplot科学作图](http://www.phy.fju.edu.tw/~ph116j/gnuplot_tutorial.pdf)
6. [gnuplot 让您的数据可视化](http://www.ibm.com/developerworks/cn/linux/l-gnuplot/)

------
