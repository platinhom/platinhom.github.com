---
layout: post
title: Amber小bug小trick
date: 2016-03-15 20:27:42
categories: CompCB
tags: CompBiol
---

干活活中遇到的问题:

#### PDB结构中残基只含有少量原子

极个别的cases. 部分残基处理完后也只有5-6个原子, 其实是邻近残基延拓到这个残基时只有1-2个原子(例如羧基的羰基部分,NH2的N)然后补充出来. 该残基严重缺原子. 这种情况下, 暂时没有脚本自动处理, 只能手动删掉相应的行. 最后后面加上TER来保证末端化(如果中间缺失一大段的话), 保证MD正常.

#### CYS的HSG问题

在AMBERTOOL14使用tleap时, 莫名其妙对CYS的硫原子加入了HSG氢原子, 但是我原来的残基就有HSG原子啊...推测是tleap的bug了. 解决方法是对pqr文件删掉HSG原子让tleap自己添加HSG.

例如在我的HIS处理脚本中(在`# first line of HIS residue`注释打的前面)加入这句:

~~~python
            # For error when CYS has HSG in pqr..silly in tleap
            if restype=="CYS" and "HSG" in line:
                continue
~~~

<script src="https://gist.github.com/platinhom/bcef539bd97bc192e231.js?file=HIS-HIE-HID-HIP-rename.py"></script>

使得处理HIS问题时同时删掉该原子(不写入到新文件).

#### HIS 不同链不处理的问题

跑出来部分结构的最后末端HIS没有处理而报错, 检查后发现, 其实是上面的HIS处理脚本处理多条链有问题. 经输出可以发现, 并没有处理第一条链以外的HIS残基. 因为在下面代码中, elif没有发生. 

~~~python
            if (startH and i<endH):
                continue;
            elif (startH and i==endH):
                startH=False;
~~~

当新链的时候, 要经历一个`TER`行. 该脚本逻辑是找到HIS残基, 并读取残基相应行预先处理. 处理完后将该残基的行用`startH`标记在该行在残基内, `endH`判断该残基的结束行. 在有TER或者空行或者别的东西时,endH记录的是该TER行的行号. 而该部分判断在`ATOM`开头的行内执行. 所以关闭StartH(即已处理完该残基)此时就没有被执行. 后来补加入了`else`分支得以解决:

~~~python
                continue
        else:
            startH=False
        fw.write(line)
~~~

也可以把elif判断句放在ATOM判断外, 效果差不多.

#### 碳原子名CL

有一个配体的原子名字叫`CL`虽然是个碳原子, 但是antechamber处理时居然把他当作了`Cl`! 导致这个分子死活报错..

例如以下分子,第13个原子CL. 理论的电子总数是134, 但`sqm`总判断为144/146电子 (pdb/mol2都报错).

~~~
@<TRIPOS>MOLECULE
:LIG
44   46    1
SMALL
USER_CHARGES


@<TRIPOS>ATOM
      1 CP         -7.5018  -32.0104  -14.9786 C.3       1 LIG        -0.1200 
      2 CA         -9.2546  -27.3657  -14.5030 C.ar      1 LIG        -0.1150 
      3 CB         -9.4880  -26.9665  -15.8435 C.ar      1 LIG        -0.1150 
      4 CC        -10.7821  -26.6610  -16.3027 C.ar      1 LIG        -0.1150 
      5 CD        -11.8805  -26.7511  -15.4322 C.ar      1 LIG        -0.1150 
      6 CE        -11.6770  -27.1568  -14.1029 C.ar      1 LIG        -0.1150 
      7 CF        -10.3803  -27.4602  -13.6494 C.ar      1 LIG        -0.1150 
      8 CG         -7.8235  -27.6819  -13.9824 C.3       1 LIG         0.3850 
      9 CH         -6.7666  -26.7735  -14.6995 C.3       1 LIG        -0.1200 
     10 CI         -6.9883  -25.2664  -14.4657 C.3       1 LIG        -0.1200 
     11 CJ         -6.9519  -24.9175  -12.9788 C.3       1 LIG        -0.1200 
     12 CK         -7.8721  -25.8222  -12.1539 C.3       1 LIG        -0.1200 
     13 CL         -7.6411  -27.3060  -12.4798 C.3       1 LIG        -0.1200 
     14 NM         -7.4957  -29.1604  -14.1020 N.4       1 LIG        -0.1000 
     15 CN         -8.5816  -30.0959  -13.6694 C.3       1 LIG         0.1500 
     16 CO         -8.1542  -31.5826  -13.6610 C.3       1 LIG        -0.1200 
     17 CQ         -6.3941  -31.0281  -15.3451 C.3       1 LIG        -0.1200 
     18 CR         -6.9678  -29.6150  -15.4094 C.3       1 LIG         0.1500 
     19 HP1        -7.0965  -33.0158  -14.8879 H         1 LIG         0.0600 
     20 HP2        -8.2503  -32.0414  -15.7707 H         1 LIG         0.0600 
     21 HB         -8.6843  -26.8604  -16.5495 H         1 LIG         0.1150 
     22 HC        -10.9269  -26.3533  -17.3267 H         1 LIG         0.1150 
     23 HD        -12.8741  -26.5152  -15.7833 H         1 LIG         0.1150 
     24 HE        -12.5149  -27.2393  -13.4269 H         1 LIG         0.1150 
     25 HF        -10.2660  -27.7740  -12.6290 H         1 LIG         0.1150 
     26 HH1        -6.7385  -26.9288  -15.7751 H         1 LIG         0.0600 
     27 HH2        -5.7695  -27.0367  -14.3503 H         1 LIG         0.0600 
     28 HI1        -7.9406  -24.9481  -14.8856 H         1 LIG         0.0600 
     29 HI2        -6.2221  -24.6979  -14.9913 H         1 LIG         0.0600 
     30 HJ1        -7.2479  -23.8794  -12.8476 H         1 LIG         0.0600 
     31 HJ2        -5.9281  -25.0119  -12.6225 H         1 LIG         0.0600 
     32 HK1        -8.9100  -25.5570  -12.3283 H         1 LIG         0.0600 
     33 HK2        -7.7009  -25.6511  -11.0923 H         1 LIG         0.0600 
     34 HL1        -6.6209  -27.5448  -12.1915 H         1 LIG         0.0600 
     35 HL2        -8.2630  -27.9093  -11.8249 H         1 LIG         0.0600 
     36 HNM        -6.7343  -29.3098  -13.4521 H         1 LIG         0.2900 
     37 HN1        -9.4414  -29.9993  -14.3335 H         1 LIG         0.0600 
     38 HN2        -8.9178  -29.8319  -12.6730 H         1 LIG         0.0600 
     39 HO1        -7.4717  -31.7877  -12.8404 H         1 LIG         0.0600 
     40 HO2        -9.0266  -32.2079  -13.4674 H         1 LIG         0.0600 
     41 HQ1        -5.9635  -31.3001  -16.3091 H         1 LIG         0.0600 
     42 HQ2        -5.5900  -31.0688  -14.6110 H         1 LIG         0.0600 
     43 HR1        -6.1835  -28.9755  -15.7958 H         1 LIG         0.0600 
     44 HR2        -7.8148  -29.6307  -16.0875 H         1 LIG         0.0600 
@<TRIPOS>BOND
     1    1   17 1    
     2    1   16 1    
     3    1   19 1    
     4    1   20 1    
     5    2    8 1    
     6    2    7 ar   
     7    2    3 ar   
     8    3    4 ar   
     9    3   21 1    
    10    4    5 ar   
    11    4   22 1    
    12    5    6 ar   
    13    5   23 1    
    14    6    7 ar   
    15    6   24 1    
    16    7   25 1    
    17    8   14 1    
    18    8   13 1    
    19    8    9 1    
    20    9   10 1    
    21    9   26 1    
    22    9   27 1    
    23   10   11 1    
    24   10   28 1    
    25   10   29 1    
    26   11   12 1    
    27   11   30 1    
    28   11   31 1    
    29   12   13 1    
    30   12   32 1    
    31   12   33 1    
    32   13   34 1    
    33   13   35 1    
    34   14   15 1    
    35   14   18 1    
    36   14   36 1    
    37   15   16 1    
    38   15   37 1    
    39   15   38 1    
    40   16   39 1    
    41   16   40 1    
    42   17   18 1    
    43   17   41 1    
    44   17   42 1    
    45   18   43 1    
    46   18   44 1    
@<TRIPOS>SUBSTRUCTURE
     1 LIG         1 GROUP             0       ****    0 ROOT 
~~~

解决办法是把名字改名为C1啥的罗.

#### Antechamber的SQM总电荷处理

SQM的电荷会从mol2中读取, 然后计算总电荷值, 四舍五入后成为当前分子总电荷, 然后再和电子总数和自旋比较. 如果电荷有大问题, 偏差了总电荷对不上自旋, 分子就不能正常处理(像上面的CL误判问题也是)

~~~
@<TRIPOS>MOLECULE
Molecule Name
5 4 1 0 0
SMALL
USER_CHARGES
 
 
@<TRIPOS>ATOM
  1 N1      -3.3822     1.0985     0.0000 N.4   1 <1>  -0.8000
  2 H2      -3.0400     0.1305    -0.0000 H     1 <1>   0.4500
  3 H3      -3.0400     1.5825     0.8383 H     1 <1>   0.4500
  4 H4      -3.0400     1.5825    -0.8383 H     1 <1>   0.4500
  5 H5      -4.4089     1.0986     0.0000 H     1 <1>   0.4500
@<TRIPOS>BOND
  1   1   2  1
  2   1   3  1
  3   1   4  1
  4   1   5  1
@<TRIPOS>SUBSTRUCTURE
  1 ****   1 GROUP 4 **** **** 0
 
~~~

例如下面的`NH4+`分子, N虽然是标+但负电荷. 如果误改为电荷+0.1, 那么此时运行报错 (理论上10电子+1电荷):

~~~bash
Total number of electrons: 9; net charge: 2
INFO: Number of electrons is odd: 9
      Please check the total charge (-nc flag) and spin multiplicity (-m flag)
 
Running: /opt/software/Amber/14v19--Intel-13.0.1.117/bin/sqm -O -i sqm.in -o sqm.out
Error: cannot run "/opt/software/Amber/14v19--Intel-13.0.1.117/bin/sqm -O -i sqm.in -o sqm.out" of bcc() in charge.c properly, exit
~~~

一般正常而言, 上述问题不会出现. 因为没发现`CL`的问题时, 之前那个分子电子总数总不对, 当时修改了N的电荷就发现了这个问题.

#### 部分PDB残基号16A 引发的问题

有一些PDB没有很规范, 可选残基结构的区分写在残基编号后, 例如16A,16B这样. 使用`PDB2PQR`后发现没有正常处理, 出现了残基16, 16A, 16, 16B这样, 都在结果里面, 自然tleap就报错了. 正常的话, 这个可选残基位置在行的17位置, PDB格式中叫`Character Alternate location indicator`, 而残基编号是`23 - 26`.  

解决办法就是判断行中27的位置有木有这个ABCD区分号. 一般该行留空. 所以以下脚本中加入了`if (line[26].strip()):continue`的处理, 这样该残基就不会写到新文件中去 (这是个规范化命名H2O分子被tleap识别的脚本,可以处理pdb/pqr文件). 注意这个区分可选残基的要在`pdb->pqr`之前对结构进行预处理! 

NOTE: 27的位置PDB中叫 `AChar Code for insertion of residues.` 但其实更常用是在`Character Alternate location indicator`处理, PDB2PQR就是这样的. 

~~~python
#! /usr/bin/env python
import sys
fin=sys.argv[1]; fout=sys.argv[2]
fi=open(fin); fo=open(fout,'w')
op=0
for line in fi:
    if (line[:6]=='ATOM  ' or line[:6]=='HETATM'):
        # Ignore optional residue..
        if (line[26].strip()):
            continue;
        if ( line[17:20]=='WAT' or line[17:20]=='HOH'):
            if (line[13]=='O'):
                op=0
                fo.write(line[:13]+'O   HOH'+line[20:])
            elif (line[13]=='H'):
                op+=1
                if op is 1:
                    fo.write(line[:13]+'H1  HOH'+line[20:])
                else:
                    fo.write(line[:13]+'H2  HOH'+line[20:])
                    op=0
            elif (line[12]=='H'):
                op+=1
                if op is 1:
                    fo.write(line[:12]+' H1  HOH'+line[20:])
                else:
                    fo.write(line[:12]+' H2  HOH'+line[20:])
                    op=0
            else: fo.write(line)
        else: fo.write(line)
    else:fo.write(line)
fi.close(); fo.close()
~~~

------
