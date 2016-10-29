---
layout: post
title: Packmol:溶剂化程序
date: 2015-11-20 18:43:22
categories: CompCB
tags: CompBiol Software MD
---

packmol是一个自由软件
主页http://www.ime.unicamp.br/~martinez/packmol/
安装过程很简单，最后生成一个名为packmol的可执行程序，把它扔到一个系统默认运行目录里面（～/bin/  /usr/bin/  之类的），就可以工作了。

它的主要用途是排布大量分子,做一个大分子的模拟，用分子的pdb加水就行了，要是做20个大分子呢？要用packmol。
使用环境：linux系统（可以找找有没有win版)
输入：自己编写的inp文件，pdb文件
输出：pdb文件
！！**packmol中，单位全部是埃，gromacs中是纳米，要注意换算。
我的一个例子（文件名a.inp）

~~~
tolerance 2.0                ----------距离误差控制,一般不用改
filetype pdb                ----------文件格式：pdb           
output dar.pdb                ----------输出文件名：pdb

structure 1.pdb                 ----------输入文件名，待排布分子1
  number 25                    ----------排布25个分子
  inside box 0. 0. 85. 50. 50. 100.        ----------排布在（0，0，85）（50，50，100）为顶点的立方体中，小数点是必须输入的，即使不想用小数。
  atoms 1 2                    ----------具体限制原子1 2，
    over plane 0. 0. 1. 92.            ----------这两个原子要在平面z=92以上，前面的001是xyz坐标系数
  end atoms                    ----------原子限制完成
  atoms 33 32                    ----------再限制原子33 32
    below plane 0. 0. 1. 90.            ----------这两个原子要在z=90以下，这样我的原子就均匀同向排布了
  end atoms                    ----------原子限制完成
end structure                    ----------这种分子排布完成（不一定要限制所有的原子，其他原子自由分布）

structure 1.pdb                 ----------再排布位于另一区域的分子1，这是允许的，gromacs也会认为它们是同一种分子
  number 25
  inside box 0. 0. 20. 50. 50. 35.
  atoms 32 33
    over plane 0. 0. 1. 30.
  end atoms
  atoms 1 2
    below plane 0. 0. 1. 28.
  end atoms
end structure

structure oct.pdb                ----------排布另一种分子（有机溶剂）
  number 400
  inside box 0. 0. -10. 50. 50. 130.
  outside box 0. 0. 20. 50. 50. 100.    -----------两个条件，这样设计是可以的，有多种条件时，程序会全部满足
end structure                    ----------溶剂分子没有必要具体到原子进行排布

structure water.pdb                ----------加入水分子（要自己画一个水分子的pdb文件）（最好写在最后，不然genion加离子的时候出错，原因尚未找到……）
  number 7000
  inside box 0. 0. 30. 50. 50. 90.
end structure                ----------文件末尾不必加结束符
~~~

- 写完inp文件，放进工作目录，运行”packmol <a.inp “（不要输入引号，这个程序只有这种运行格式），程序就开始排布分子了。
- 分子排布不一定都是立方体和平面，网站帮助里面有很多种排布方式（圆形，球形，棱柱等等），需要的同学自己看吧。
- 不要输入过于苛刻的条件，例如pdb文件中，原子1和15距离10埃，限制原子最多让他们距离9埃，再多就要出错了，packmol绝对不会改变分子的构象。
- 提前计算好一种分子大致占位体积，偏差过大将来模拟时容易爆炸。
- 允许多种分子排布在一个区域内，先来先排，后来的可以见缝插针。

希望对大家有帮助

- packmol <http://www.ime.unicamp.br/~martinez/packmol/>
- archive <http://archive.ambermd.org/201007/0754.html>  <http://archive.ambermd.org/201104/0345.html> <http://archive.ambermd.org/200911/0038.html> 
- amber 格式 <http://ambermd.org/formats.html>
- amber 教程 <http://www.rosswalker.co.uk/tutorials/amber_workshop/Tutorial_one/section3.htm>

<http://simulation.5d6d.com/viewthread.php?tid=7406>



------
