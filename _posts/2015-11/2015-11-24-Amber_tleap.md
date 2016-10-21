---
layout: post
title: Amber:tleap
date: 2015-11-16 21:05:53
categories: CompCB
tags: CompBiol MD
---

xleap术语:head/tail:具有头或尾:T5,A3,T(两者均有)TN(None),残基为NALA,CALA（在前,大写).对于肽链,以N***开始,C***结尾,若要分隔不同链必须以TER(否则以最后一个C***结尾)！

`xleap -s -f $AMBERHOME/dat/leap/cmd/leaprc.ff99`  (xleap可能有bug,要关闭numlock才能选菜单)
cmd文件夹含很多力场,例如leaprc.ff03 (FF03 force field), leaprc.ff02ep(FF02 polarisable force field with lone pairs)
-s 忽略加载用户指明的参数的缺省值; -f **.ff99表示加载何力场脚本 -I 增加搜索路径,-h help
在xleap里,dna1=loadpdb “abc.pdb" 是读入pdb文件建立一个对象。
可用edit dna1来进入图形界面编辑
不合理的结构如没有标准残基，TER错误等回导致创建新的残基，并且没有连接.
命令list会列出现在已定义的对象。help列出所有xleap指令,help command可以查看指定命令帮助。
obj2=copy obj1 可以复制对象obj1到obj2

在Editor里,左键选择中建旋转右键平移,中右键倍率.选中后去选择也按住Shift.Relax selection选项是优化结构。关闭必须用close,否则整个xleap关闭。

saveamberparm model(对象)  polyAT\_vac.prmtop polyAT\_vac.inpcrd 将对象保存为top和crd文件
addions model Na+ 0 # 加反离子, 0代表中和掉,不为0则是加的数量,可以一次性再加多种指定离子（num!=0）
solvatebox model TIP3PBOX 8.0    # 长方体溶剂化,对于长条形分子最好指定立方体。此处使用TIP3P盒子溶剂化，加到8A长。
solvateoct model2 TIP3PBOX 8.0  # 8面体溶剂化。

xleap 指令

`xleap/tleap -s -f leaprc.ff03` (script)

source 脚本 # 加载脚本,当前文件夹或path文件夹
list # 查看所有定义的变量(unit,residue等)
check unit # 检查单元,很重要
desc var  #  显示变量信息
com=combine {pro lig}    合并对象
edit unit  #  xleap开图形界面编辑和查看单元
help command_string #  查看帮助
quit 退出

charge unit # 检查电荷
addions unit Na+ 10  # 加反离子,设0会自己判断,但-6.999会加6个,最好自己判断
setBox unit vdw/centers [buffer] #  设置周期盒子,如果已平衡用centers
solvateBox/Oct unit SOLVENT radius #  加载溶剂，注意溶剂许多都是大写

var=loadpdb/mol2 file #  加载文件
loadoff file #  加载对象库OFF,lib,所有unit和parmset将被加载
var=loadAmberParams file #  加载参数文件如dat
loadAmberPrep file # 加载amber的prep文件，如prep，in等

saveAmberParm unit top crd # 将单元保存为top和crd文件！
savePdb unit file #   保存为pdb文件
saveOff unit file 将对象创建/添加到off或lib文件中

loadamberparams frcmod.ionsjc_tip3p  # 其中tip3p可以换成别的水分子

不常用
var=copy unit 复制单元

------
