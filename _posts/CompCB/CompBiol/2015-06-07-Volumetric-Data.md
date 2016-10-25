---
layout: post
title: 电镜数据 Volumetric Data
date: 2015-06-07 11:25:15
categories: CompCB
tags: CompBiol DataAnal Fortran
---
美国博后的工作和之前没有什么交集,做的东西也很无聊. 2015年后,主要处理冷冻电镜数据. 在这里做个简要介绍,包括:

- 文件格式介绍
- 文件读写
- 数据可视化
- 数据的操作变换

-------

### 文件格式介绍
- 电镜数据以volumetric data形式储存, 即3D空间网格grids形式储存.电镜数据可以通过[EMDatabank](http://emdatabank.org/)中[搜索](http://www.emdatabank.org/search.html)获得. 以下以[EMD2936](http://emsearch.rutgers.edu/atlas/2936_mapparams.html)为例介绍.
  - 数据在网格立方体中储存,其中包含有数个等大小的正方体,边长为数据中`Voxel spacing`的值(一般是正立方体),也就是常说的网格大小`grid szie`.网格大小是真实空间的大小.
  - 网格立方体各边长X,Y,Z,共`X*Y*Z`个小正方体,也可以认为是多少个像素点,这里是`Dimensions(Voxels)`的值.所以整个电镜数据大小是`grid size^3 * (x*y*z)`
  - Origin储存数据开始于真实空间那个位置开始,例如-39表示`-39*gridsize`的空间坐标.
  - 具体数据储存在正方体的顶角位置,代表该位置的实验数值(对于电镜数据是相对的电子密度),一般称contour level,isovalue等. `Map Statistic`统计了该电镜数据数值的范围,中位数及标准差.
  - 数据可视化一般针对一定数值时所构成的等值面进行可视化.指定一定的数值,就会有相应的等值面.为了反映研究物质的外形,一般有一个推荐值`recommand contour level`对数据进行可视化.

- 电镜数据以`.map`后缀储存,其实质是一种`mrc`Image 格式文件.`ccp4`格式文件也是mrc格式文件. [MRC文件说明](http://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/image-processing-software/)可参考剑桥MRC分子生物学实验室.
  - 在文件开头有1024 bytes的开头部分,储存了各种基础信息.从1025 byte开始数据为具体每个格点的数据.
  - map大小以长整形储存于1-3位(XYZ).第四位整形为储存数据的类型,比较重要.

### map文件读写
- mrc格式文件以二进制格式(binary)储存. 读取数值时要注意类型以及XYZ的map大小,逐一读取. 如何使用matlab读写map可参考[scripps-mrctools](http://ami.scripps.edu/software/mrctools/mrc_specification.php).稍后贴出fortran读写的示例代码.

~~~~ fortran  
!* map file read and write
!* Author Platinhom
!* 2015.6.7
!* This is only an example code for how to read the map.

program mapread
character*80 mapname
integer*4 :: headinfo(256)
integer*2,allocatable:: iv(:,:,:),bv(:,:,:)
real*4,allocatable :: rv(:,:,:)
integer*4 :: datatype,nx,ny,nz
integer*8 :: ixyz
mapname="emd_1234.map"

!! CCP4 Map header: 56 4-byte fields and space for ten 80 character(200 4-byte)
!! Reference: http://lsbr.niams.nih.gov/3demc/3demc_maplib.html
!! 1-3,int: total nx ny nz for grip; Dimensions(voxels)
!! 4,int: data type, normally =2 (real*4, 32bit) or =1(integer*2, 16bit)
!! 5-7,int: first position of x,y,z in map ; Origin(voxels)
!! 
!! 11-13,float: Cell Dimensions
!! 14-16,float: Cell Angles(alpha,beta,gamma)
!! 17-19,int: 
!! 20-22,float: Min/Max/Average density value
!! 26-34,float[3][3]: skew matrix


!! Note that, access="direct" is used when you are using in gfortran and so on. 
!! But in Visual Studio based on ifort, you have to use access="stream" instead.

open (77, file = trim(mapname), iostat = ios, status='old', &
    	ACCESS='DIRECT', Form = 'Unformatted', RecL = 4)
	if (ios /= 0) stop
		read(77,rec=1) nx
		read(77,rec=2) ny
		read(77,rec=3) nz
		read(77,rec=4,iostat=ios) datatype
	if (ios /= 0) stop
	ixyz=nx*ny*nz
	print '(a,I5,I5,I5,I15,I2)','NX,NY,NZ,NX*NY*NZ,datatype: ',nx,ny,nz,ixyz,datatype
close (77)

open (78, file = trim(mapname), iostat = ios, &
    	ACCESS='DIRECT', Form = 'Unformatted', RecL = ixyz*4+1024)

allocate(rv(nx,ny,nz),stat=error)
if (error/=0) then
	write(*,*) 'No enough memory!'
	stop
endif

if (datatype==2) then
	read(78,rec=1,iostat = ios) headinfo(:),rv(:,:,:)
elseif (datatype == 1) then
	allocate(iv(nx,ny,nz))
	read(78,rec=1,iostat = ios) headinfo(:),iv(:,:,:)
	rv=dble(iv)
elseif (datatype == 0 ) then
	allocate(bv(nx,ny,nz))
	read(78,rec=1,iostat = ios) headinfo(:),bv(:,:,:)
	rv=dble(bv)
endif
if (ios /= 0) stop
close(78)
end program mapread

! To write into map, you can use same method to open.
! And then write nx,ny,nz,datetype in integer*4.
! And then 252 num=1 in integer*4
! Finally write the data.
~~~~

### map文件可视化
- Chimera: 推荐使用.不仅可用于map的可视化,亦能用于更复杂的操作.
Map文件可以用Chimera直接打开. 随后出现Volume Viewer,可以看到不同density下的分布.拉动竖线来调节不同contour level.可以在density图中按着`ctrl`再添加一个surface表示. 可以调节颜色及透明度.可以保存新的map.

- VMD: 注意`.map`文件不能直接打开因为有很多后缀map的文件,可以改后缀ccp4或mrc.或者打开后选择合适的map.再用`Representations`里draw metho选择`Isosurface`,draw选`solid surface`或`wireframe`. 拉动`Isovalue`的bar来调节不同isovalue获得不同等值面.


### map的操作转换
- 直接使用Matlab读入并操作
- 使用Chimera读入,使用`Volume Filter`进行简单操作,包括高斯光滑化,傅里叶变化,简单的数值变化(scale,可加减乘除),格点变换(bin).最后对map重新保存.
- 使用Chimera读入,使用命令[vop](http://www.cgl.ucsf.edu/chimera/current/docs/UsersGuide/midas/vop.html)进行操作,包括两个map的加减操作,插值等.
- 更多可视化操作来选择区域数据并删减,可以用Chimera进行,包括`volume eraser`选择区域删除(快捷键es,删除外部eo);选择subregion后用快捷键eb删除;用`Segment map`区块化后选择删除等.

### [电镜相关软件](http://www.emdatabank.org/emsoftware.html)

该blog只作个初步简介.随后会进一步介绍如何可视化map数据以及如何用Chimera进行数据操作.
To be continued....

---
