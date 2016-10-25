---
layout: post
title: Chimera用于CryoEM数据处理
date: 2015-07-21 04:38:26
categories: CompCB
tags: Visualize CompBiol
---


### [Slicing surfaces]
Tools-Depictions-Per-Model-Clipping 打开对话框. 
Enable clipping 开始切片
Use slab mode with thickness  切成一厚度的饼, 而不是砍一刀
Orient plane 根据视觉直接平切. 取决于视觉
Flip plane 切换被切掉和保留的部分.
Align plane 当有不同对象的切面时,将其对齐
Adjust clipping with mouse as below  点选后可以手动调整切面, 中间平移, 右键旋转切面.
Suface capping 里面可以控制切面处是显示表面, mesh还是不显示. 还有颜色等.

### [Volume Viewer](http://www.cgl.ucsf.edu/chimera/current/docs/ContributedSoftware/volumeviewer/framevolumeviewer.html  )

#### Command: [Volume](http://www.cgl.ucsf.edu/chimera/current/docs/UsersGuide/midas/volume.html  )
在view中ctrl键下点击isovalue可以多造一个surface。

#### Command: [vop](http://www.cgl.ucsf.edu/chimera/current/docs/UsersGuide/midas/vop.html )
`vop operation arguments options` 编辑volumetric data 并存作另一新map.

##### operation:
`vop add  volume-spec  [ scaleFactors f1,f2,... ] [ onGrid gridmap ] [ boundingGrid true|false ] [ gridStep N | Nx,Ny,Nz ] [ gridSubregion name | i1,j1,k1,i2,j2,k2 | all ]  general-options`:  两个map相加,可以通过scalefactor来调控map的权重,默认是1.0. onGrid是最后会生成的格点,默认是第一个map.boundingGrid是否调整grid来适应新的map, gridstep是对grid才子集, 可以每轴指定N个合并,也可以单独设置三轴. gridSubregion,是否使用某个子区域,可以采用已定义的子域(name指明)也可以指明xyz的范围,默认全部.
`vop subtract  map othermap  [ scaleFactors f1,f2 ] [ minRMS true|false ] [ onGrid gridmap ] [ boundingGrid true|false ] [ gridStep N | Nx,Ny,Nz ] [ gridSubregion name | i1,j1,k1,i2,j2,k2 | all ]  general-options`: 从map中扣除othermap的值.scaleFactors指明两个map的缩放比例,必须都指明;更常用minRMS可以自动调整othermap的比例,默认flase.onGrid可以指明格点使用某个map的格点打发,默认采用map的.
`vop resample  volume-spec  onGrid gridmap [ boundingGrid true|false ] [ gridStep N | Nx,Ny,Nz ] [ gridSubregion name | i1,j1,k1,i2,j2,k2 | all ]  general-options`: 重新采样,采用gridmap的格点打法来对指定map重新打格点,采用三线性插值的方法.
`vop minimum|maximum    volume-spec  [ scaleFactors f1,f2,... ] [ onGrid gridmap ] [ boundingGrid true|false ] [ gridStep N | Nx,Ny,Nz ] [ gridSubregion name | i1,j1,k1,i2,j2,k2 | all ]  general-options`: 对多个map中取最小/最大的值. 参见add的处理.

##### options:
- `vop scale  volume-spec  [ shift constant ] [ factor f ] [ rms new-rms | sd new-std-dev ] [ valueType value-type ]  general-options`: 对map进行一个常数的加减和变化.
- `modelId  N`
- `step  N | Nx,Ny,Nz`
- `subregion  name | i1,j1,k1,i2,j2,k2 | all`
- `nPlace true|false`

- ### [Segment Map](http://www.cgl.ucsf.edu/chimera/current/docs/ContributedSoftware/segger/segment.html)
#### Command: [Segment](http://www.cgl.ucsf.edu/chimera/current/docs/UsersGuide/midas/segment.html  )




### Fitting 
#### [Fit in Map](http://www.cgl.ucsf.edu/chimera/current/docs/ContributedSoftware/fitmaps/fitmaps.html ): 
 fit atoms into a map (volume data) or one map into another
#### Command: [fitmap](http://www.cgl.ucsf.edu/chimera/current/docs/UsersGuide/midas/fitmap.html ) 也可用`fit`

`fitmap  fit-structure  ref-map  options   global-search-options` 
##### options:

`metric  overlap | correlation | cam`: map-in-map fitting使用的策略,默认overlap.cam是correlation about the mean
`resolution r`: 指明原子产生模拟volume的分辨率, 采用map-in-map策略, 不指明则用atom-in-map策略
`shift  true | false ` 或 `rotate  true | false `: 在局部优化时是否平移和旋转(默认true)
`moveWholeMolecules  true | false `: 是否整个分子移动还是只移动指定的原子. 默认true.只计算指定原子fitting.全局搜索时忽略.
`listFits  true | false`: 做完fitting是否显示fit list的对话框. 在全局优化中默认是, 一般默认否.
`envelope  true | false `: 对接对象(如分子自动模拟map)中大于coutour阈值的点才用于fitting,默认是. 否则,所有非零点均用于fit.
`symmetric  true | false`: 是否采用ref map的对称性用于fitting,默认否. 只能用于map-in-map对接和有对称性信息. 能避免直接sym时可能产生的冲突. [Sym Fitting movie](http://www.cgl.ucsf.edu/chimera/videodoc/SymFitDNAb/  )
`gridStepMax  max `: 初始化step size(缺省0.5). 参见[局部优化算法](http://www.cgl.ucsf.edu/chimera/current/docs/ContributedSoftware/fitmaps/fitmaps.html#optimization  ).
`gridStepMin  min `: 局部优化算法中收敛标准, 默认0.01.
`maxSteps  N `:局部优化中最大步数.
`eachModel  true | false`: 在指定了多个fit结构时用multifit时是否不考虑别的结构. 就是独立地fitting.默认false.
`sequence M `:用于multifit, 需要map-in-map方式, fit结构为多个#1,2,3. M为需要fit的次数,一般为fit结构个数, 若大于该数目则会循环fit. 理论是, 将其与结构现在的位置的密度临时扣除后进行fit,再进行下一个子结构fit,最好会收敛. 不能与eachModel共存. 暂不能用于对称fit以及global search. [Sequential Fitting例子](http://www.cgl.ucsf.edu/chimera/videodoc/FitSeq/  ).

##### Global Search Options:
`search  N `: 在map全局上产生N个起始位置并进行局部优化,最后结果在Fit List. 默认为0.
`placement s | r | sr `: 初始化起始位置时对model进行:s 平移 r 旋转 sr平移和旋转(默认)
`radius  maxdist`: 限制全局搜索时初始化放置位置在起始位置一定距离内.
`clusterAngle  angle `和`clusterShift  shift `: 在fit list中显示的unqiue的差异旋转度(默认6度)和平移度(默认3A)
`asymmetricUnit  true | false `: 是否将位置上对称等价的不对称单元作为同一结果处理.默认true.
`inside  fraction`: 达到最少保持在ref map中原子/grid point的比例才能作为结果.
 
 ### [Fit in Segment](http://www.cgl.ucsf.edu/chimera/current/docs/ContributedSoftware/segger/fitsegments.html ):
 fit structures into map segmentation regions
 
 ### [MultiFit](http://www.cgl.ucsf.edu/chimera/current/docs/ContributedSoftware/multifit/multifit.html ):
 fit multiple structures into density using a web service hosted by the UCSF RBVI

### Symmetry
 - #### Command: [measure symmetry](http://www.cgl.ucsf.edu/chimera/current/docs/UsersGuide/midas/measure.html#symmetry ): 
`measure symmetry  map-model(s)  [ minimumCorrelation mincorr ] [ nMax n ] [ points maxpts ] [ set true|false ] [ helix rise,angle[,n][,opt] ]`
! 测量对称性, 获得的对称性可用于`sym`和`fitmap`指令, 也可用于map文件生成. 要直接指定对称性使用volume symmetry.
! 常见对称性:  cyclic(C3/C6...), dihedral, tetrahedral, octahedral, and [icosahedral](http://www.cgl.ucsf.edu/chimera/current/docs/ContributedSoftware/icosahedron/icosahedron.html  ). Helical.
! 当对称化变化后两套map的相关不少于mincorr(默认0.99)将会反馈对称性信息. 
! set true时将会将对称性信息赋予map.
!!  helix时后面上升高度(A)和重复角度(度)要提供, 并且`,` 不能缺. n指明不对称单元的数目,不指明则取决于rise和helix长度; opt则指明是否在rise和angle基础上进行优化获得更准确的rise和angle.
!! nMax 指定Cn对称性搜索的最大的n(默认是8)
!! maxpts 指定用于相关计算时使用的最大数据点数目, 若实际数超过maxpts则会在map上随机取点
 - #### Command: [volume symmetry](http://www.cgl.ucsf.edu/chimera/current/docs/UsersGuide/midas/volume.html#symmetry  ): 
`volume symmetry sym-type` 
!给volume data指明对称性信息, 会储存于map信息,也用于`sym`和`fitmap`.
##### sym-type如下:
` #N ` 使用N模型/分子的对称信息.
`Cn`:  循环(轴)对称Cn,如C3对称
`Dn`:  二面体群对称Dn,如D4对称
`T[,orientation]` 四面体对称性,取向是222(缺省)或z3
`O` 八面体对称性
`I[,orientation]` 二十面体对称性, 常见如病毒.默认取向是222, 还有2n5,n25,2n3,222r,2n5r,n25r,2n3r
`H,rise,angle,n[,offset]` 螺旋对称, 不对称单元的轴移动,旋转角,不对称单元数,
`shift,n,distance`或`shift,n,x,y,z` 平移对称
`#N,pM`或`#N,pnM` cage model多边形对称
`c2*h,42,21,9` 对称群乘积`*`,混合
 - #### Command: [sym](http://www.cgl.ucsf.edu/chimera/current/docs/UsersGuide/midas/sym.html  )
`sym [ molmodel ] options`, 取消对称`~sym [ molmodel ]`
! 产生对称性复制的分子复合物结构
! molmodel 指明对称化对象, 如只有一个mol则默认用之. 用#N指明
#####option部分
`group symmetry`: 指定对称性,不指定默认使用biomt(即自身在输入文件中的对称性),其余对称性参见`volume symmetry`的sym-type部分
`coordinateSystem N`: 可简写成`coord N`, 指明坐标系统的参考分子, 默认是molmodel本身, 但更常用map本身. N就是#N的分子模型
`update true|false`: 自动更新对称copy的状态,随其移动. 默认false.
`center cen`: 指明对称性的中心, cen默认是0,0,0. 可以用`x,y,z`或指定对象(原子,surface等)的中心
`axis ax`: 指明对称轴. 默认是Z轴.可以使`x`,`y`,`z`,`x,y,z`向量, 或者指定的两个原子, 一个键(必须用sel选中指定).
`biomtSet true|false`: 是否产生BIOMT信息到molmodel, 会替代之前的信息.并可保存在PDB文件中. 默认true
`range dist`: 只产生molmodel中心一定dist距离到copy中心的模型
`contact dist`:  只产生molmodel到copy任何原子距离小于dist的模型
`modelId N`: 
`occupancy f`: 
`surface all | true | false  [ resolution r ]`: 是否用低分辨表面来代替原子结构.默认flase.all指包括molmodel自身.resoltion r指明分辨率(默认8A).
##从原子结构到模拟volume: [molmap](http://www.cgl.ucsf.edu/chimera/current/docs/UsersGuide/midas/molmap.html  )

## Reference
[EM Navigator](http://pdbj.org/emnavi/  ) ;[具体的](http://pdbj.org/emnavi/emnavi_detail.php?id=1022  )
[BCM的workshop](http://blake.bcm.edu/emanwiki/Workshop2011  )
[atom specifier](https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/midas/atom_spec.html  )

------
