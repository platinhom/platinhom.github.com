---
layout: post
title: 如何识别高级的验证码(ZZ)
date: 2015-12-19 17:52:18
categories: IT
tags: Website ZZ
---

看到个不错的技术贴分享下~~

转载自: [如何识别高级的验证码](http://huaidan.org/archives/2085.html)

2008/06/19 21:15 | 鬼仔 [moonblue333](mailto:<moonblue333_at_hotmail.com>)

==Ph4nt0m Security Team==

Issue 0x02, Phile #0x09 of 0x0A

----------------------

## 一、验证码的基本知识

1. 验证码的主要目的是强制人机交互来抵御机器自动化攻击的。
2. 大部分的验证码设计者并不得要领，不了解图像处理，机器视觉，模式识别，人工智能的基本概念。
3. 利用验证码，可以发财，当然要犯罪：比如招商银行密码只有6位，验证码形同虚设，计算机很快就能破解一个有钱的账户，很多帐户是可以网上交易的。
4. 也有设计的比较好的，比如Yahoo,Google,Microsoft等。而国内Tencent的中文验证码虽然难，但算不上好。

## 二、人工智能，模式识别，机器视觉，图像处理的基本知识

### 1)主要流程：

比如我们要从一副图片中，识别出验证码；比如我们要从一副图片中，检测并识别出一张人脸。 大概有哪些步骤呢？

1. 图像采集：验证码呢，就直接通过HTTP抓HTML，然后分析出图片的url，然后下载保存就可以了。 如果是人脸检测识别，一般要通过视屏采集设备，采集回来，通过A/D转操作，存为数字图片或者视频频。
2. 预处理：检测是正确的图像格式，转换到合适的格式，压缩，剪切出ROI，去除噪音，灰度化，转换色彩空间这些。
3. 检测：车牌检测识别系统要先找到车牌的大概位置，人脸检测系统要找出图片中所有的人脸（包括疑似人脸）；验证码识别呢，主要是找出文字所在的主要区域。
4. 前处理：人脸检测和识别，会对人脸在识别前作一些校正，比如面内面外的旋转，扭曲等。我这里的验证码识别，“一般”要做文字的切割
5. 训练：通过各种模式识别，机器学习算法，来挑选和训练合适数量的训练集。不是训练的样本越多越好。过学习，泛化能力差的问题可能在这里出现。这一步不是必须的，有些识别算法是不需要训练的。
6. 识别：输入待识别的处理后的图片，转换成分类器需要的输入格式，然后通过输出的类和置信度，来判断大概可能是哪个字母。识别本质上就是分类。

### 2)关键概念：

- 图像处理：一般指针对数字图像的某种数学处理。比如投影，钝化，锐化，细化，边缘检测，二值化，压缩，各种数据变换等等。
	1. 二值化：一般图片都是彩色的，按照逼真程度，可能很多级别。为了降低计算复杂度，方便后续的处理，如果在不损失关键信息的情况下，能将图片处理成黑白两种颜色，那就最好不过了。
	2. 细化：找出图像的骨架，图像线条可能是很宽的，通过细化将宽度将为1，某些地方可能大于1。不同的细化算法，可能有不同的差异，比如是否更靠近线条中间，比如是否保持联通行等。
	3. 边缘检测：主要是理解边缘的概念。边缘实际上是图像中图像像素属性变化剧烈的地方。可能通过一个固定的门限值来判断，也可能是自适应的。门限可能是图像全局的，也可能是局部的。不能说那个就一定好，不过大部分时候，自适应的局部的门限可能要好点。被分析的，可能是颜色，也可能是灰度图像的灰度。
- 机器视觉：利用计算机来模式实现人的视觉。 比如物体检测，定位，识别。按照对图像理解的层次的差别，分高阶和低阶的理解。
- 模式识别：对事物或者现象的某种表示方式（数值，文字，我们这里主要想说的是数值），通过一些处理和分析，来描述，归类，理解，解释这些事物，现象及其某种抽象。
- 人工智能：这种概念比较宽，上面这些都属于人工智能这个大的方向。简单点不要过分学院派的理解就是，把人类的很“智能”的东西给模拟出来协助生物的人来处理问题，特别是在计算机里面。

## 三、常见的验证码的破解分析

以 <http://libcaca.zoy.org/wiki/PWNtcha> 这里PWNtcha项目中的资料为例分析，各种验证码的破解。（方法很多，仅仅从我个人乍看之下觉得可行的方法来分析）

#### 1)Authimage

![](http://huaidan.org/wp-content/uploads/img/yupoo/922715bdd0cd/h5hgdfd6.jpg)

##### 使用的反破解技巧：

1. 不连续的点组成字符
2. 有一定程度的倾斜

##### 设计不好的地方：

1. 通过纵横的直方图投影，可以找到字幕区域
2. 通过Hough变换，适当的参数，可以找到近似的横线，可以做倾斜矫正
3. 字符串的倾斜式面内的，没有太多的破解难度
4. 字母宽度一定，大小一定

#### 2)Clubic

![](http://huaidan.org/wp-content/uploads/img/yupoo/914715bdd0d3/s36cy743.jpg)

##### 使用的反破解技巧：

1. 字符是手写体

##### 设计不好的地方：

1. 检测切割阶段没有任何技术含量，属于设计的比较丑的
2. 只有数字，而且手写体变化不大
3. 表面看起来对识别阶段有难度，仔细分析，发现几乎不用任何高级的训练识别算法，就固定的招某些像素点是否有色彩就够了

#### 3)linuxfr.org

![](http://huaidan.org/wp-content/uploads/img/yupoo/029145bdd0cd/wnwz30i2.jpg)

##### 使用的反破解技巧：

1. 背景颜色块
2. 前景的横线或矩形

##### 设计不好的地方：

1. 背景色是单一色块，有形状，通过Region-Growth区域增长来很容易把背景给去掉
2. 前景色是标准的线条，色彩单一
3. 字母无粘连
4. 都是印刷体

#### 4)Ourcolony

![](http://huaidan.org/wp-content/uploads/img/yupoo/278335bdd0cf/wpdw3nuy.jpg)

##### 使用的反破解技巧：

1. 设计的太低级，不屑于去评价

##### 设计不好的地方：

1. 这种验证码，设计的最丑，但还是能把菜鸟搞定，毕竟学计算机的少，搞这个破解的更少，正所谓隔行如隔山

#### 5)LiveJournal

![](http://huaidan.org/wp-content/uploads/img/yupoo/662425bdd0d2/71jsdrn6.jpg)

##### 使用的反破解技巧：

1. 这个设计略微好点，使用个随机噪音，而且作为前景
2. 字母位置粗细都有变化

##### 设计不好的地方：

1. 字母没有粘连
2. 噪音类型单一
3. 通过在X轴的直方图投影，能准确分割字幕
4. 然后在Y周作直方图投影,能准确定位高度
5. 识别阶段，都是印刷体，简单地很

## 四、网上的一些高级验证码

### 1)ICQ
![](http://huaidan.org/wp-content/uploads/img/yupoo/700595bdd0c1/s3mme4h0.jpg)

### 2)IMDb
![](http://huaidan.org/wp-content/uploads/img/yupoo/451605bdd0c3/8qbljgnh.jpg)

### 3)MS MVPS
![](http://huaidan.org/wp-content/uploads/img/yupoo/348055bdd0c5/7tenrvma.jpg)

### 4)MVN Forum
![](http://huaidan.org/wp-content/uploads/img/yupoo/944405bdd0c7/78o419pr.jpg)


这些类型是被很多人认为比较难得类型，分析一下可以发现，字符检测，定位和分割都不是难。 唯一影响识别率的是IMDBb和MVPS这两类，字体变形略大。

总体来说，这些类型的破解也不难，很容易做到50%以上的识别率。

## 五、高级验证码的破解分析

时间关系，我简单介绍如何利用图像处理和模式识别技术，自动识别比较高级的验证码。
(以风头正劲的Google为例)

![](http://huaidan.org/wp-content/uploads/img/yupoo/416885bdd0c8/d31c2mon.jpg)

### 1)至少从目前的AI的发展程度看，没有简单的做法能自动处理各种不同的验证码，即使能力很强，那么系统自然也十分复杂强大。所以，要想在很简单的算法实现比较高级的验证码破解，必须分析不同验证码算法的特点：

作为一般的图像处理和计算机视觉，会考虑色彩，纹理，形状等直接的特征，同时也考虑直方图，灰度等统计特征，还考虑FFT，Wavelet等各种变换后的特征。但最终目标都是Dimension Reduction（降维）然后利于识别，不仅仅是速度的考虑。从图像的角度看，很多系统都考虑转换为灰度级甚者黑白图片。
　
Google的图片可以看出，颜色变化是虚晃一枪，不存在任何处理难度。难度是字体变形和字符粘连。
　
如果能成功的分割字符，那么后期识别无论是用SVM等分类算法，还是分析笔顺比划走向来硬识别，都相对好做。
　
### 2)图像处理和粘连分割

代码中的part1目录主要完成图像预处理和粘连字符分割

- 001：将图像从jpg等格式转换为位图便于处理
- 002：采用Fix/Adaptive的Threshold门限算法，将图片Bin-Value二值化。  
  （可用003算法）
- 003：采用OSTU分水岭算法，将图片Bin-Value二值化。  
  （更通用，大部分时候效果更好）
- 005：获取ROI感兴趣的区域。
- 006：Edge Trace边缘跟踪。
- 007：Edge Detection边界检测。
- 008：Thin细化去骨架。
- 009：做了一些Tidy整理。  
　　（这个一般要根据特定的Captcha算法调整）
- 010：做切割,注意图片中红色的交叉点。
- 011：将边缘检测和骨干交叉点监测的图像合并。  
　　（合并过程可以做分析: 比如X坐标偏移门限分析，交叉点区域纹理分析，线条走势分析，等等各种方法，找出更可能的切分点和分离后部件的组合管理。）

![](http://huaidan.org/wp-content/uploads/img/yupoo/749045bdd0ca/q24gs2ea.jpg)

代码：（代码质量不高，从其他项目拷贝过来，简单修改的。）

[查看代码(./pstzine_09_01.txt)](http://www.icylife.net/pstzine/0x02/html/pstzine_09_01.txt)

~~~cpp
{% raw %}
//SuperImage.h

#ifndef _SUPER_IMAGE_
#define _SUPER_IMAGE_

typedef short Pixel;

//
template <class T> 
class SuperImage 
{ 
public:
	SuperImage(const int w, const int h);
	~SuperImage();
public:
	T* data;
	int width;
	int height;
};

//

class EnhancedImage
{
public:
	SuperImage<Pixel>* superImage;
public:
	EnhancedImage();
	~EnhancedImage();
	int load(const char* name);
	int save(const char* name);
	int copy(EnhancedImage* copy);
	int film(EnhancedImage* film);
	int binv();
	int otsu();
	int line();
	int roii();
	int trac();
	int edge();
	int thin();
	int tidy();	
	int kerf();	
	int join();
};

#endif

//SuperImage.cpp
#include "superImage.h"
#include "ximage.h"

template <class T> 
SuperImage<T>::SuperImage(const int w, const int h) 
{
	width = w;
	height = h;
	data = new T[w * h];
};

template <class T> 
SuperImage<T>::~SuperImage() 
{
	if(data)
	{
		delete[] data; 
	}
};

EnhancedImage::EnhancedImage()
{
	superImage=NULL;
};

EnhancedImage::~EnhancedImage()
{
	if(superImage)
	{
		delete superImage;
	}
};

int EnhancedImage::load(const char* name)
{
	CxImage input;
    input.Load(name, CXIMAGE_SUPPORT_J2K);	
	if(!input.IsValid())
	{
		return 1;
	}
	else
	{
		int h=input.GetHeight();
		int w=input.GetWidth();		
		superImage = new SuperImage<Pixel>(w,h);
		for(int y=0;y<h;y++)
		{
			for(int x=0;x<w;x++)
			{
				RGBQUAD rgbQUAD = CxImage::RGBtoXYZ(input.GetPixelColor(x,y));
				Pixel pixel = 255;
				if(true)
				{
					pixel = (rgbQUAD.rgbRed + rgbQUAD.rgbGreen + rgbQUAD.rgbBlue) / 3.0;
				}
				else
				{
                	double yy = (0.299 * rgbQUAD.rgbRed + 0.587 * rgbQUAD.rgbGreen + 0.114 * rgbQUAD.rgbBlue) / 256.0;
	                pixel = (int) (219.0 * yy + 16.5);
				}
				superImage->data[y*w+x]=pixel;
			}
		}
	}
    return 0;
};

int EnhancedImage::save(const char* name)
{
	CxImage output;
	output.Create(superImage->width,superImage->height,24,CXIMAGE_SUPPORT_BMP);  //1 4 8 24
	for(int y=0;y<superImage->height;y++)
	{
		for(int x=0;x<superImage->width;x++)
		{			
			Pixel pixel = superImage->data[y*superImage->width + x];
			RGBQUAD rgbQUAD;
			if(pixel == -1)
			{
				rgbQUAD.rgbRed = 255;
				rgbQUAD.rgbGreen = 0;
				rgbQUAD.rgbBlue = 0;
			}
			else if(pixel == -2)
			{
				rgbQUAD.rgbRed = 0;
				rgbQUAD.rgbGreen = 255;
				rgbQUAD.rgbBlue = 0;
			}
			else if(pixel == -3)
			{
				rgbQUAD.rgbRed = 0;
				rgbQUAD.rgbGreen = 0;
				rgbQUAD.rgbBlue = 255;
			}
			else
			{
				rgbQUAD.rgbRed = pixel;
				rgbQUAD.rgbGreen = pixel;
				rgbQUAD.rgbBlue =pixel;
			}
			output.SetPixelColor(x,y,rgbQUAD);
		}
	}
	output.Save(name,CXIMAGE_SUPPORT_BMP);
    return 0;
};
int EnhancedImage::copy(EnhancedImage* copy)
{
	int w = copy->superImage->width;
	int h = copy->superImage->height;	
	short* cpy = copy->superImage->data;
	//
	this->superImage = new SuperImage<Pixel>(w,h);
	short* tgt = this->superImage->data;
	//
	for (int y=0; y<h; y++) 
	{
		for (int x=0; x<w; x++) 
		{
			tgt[w*(y)+(x)] = cpy[w*(y)+(x)];
		}
	}
	return 0;
}
int EnhancedImage::film(EnhancedImage* film)
{
	int h = film->superImage->height;
	int w = film->superImage->width;
	short* flm = film->superImage->data;
	short* tgt = this->superImage->data;
	//
	for (int y=0; y<h; y++) 
	{
		for (int x=0; x<w; x++) 
		{
			unsigned char source = flm[w*(y)+(x)];
			unsigned char target = tgt[w*(y)+(x)];	
			if(source < 0 || target < 0)
			{
                printf("x=%d  y=%d    src=%d  tgt=%d\n",x,y,source,target);
			}
			if(source==0 && target == 255)
			{
				tgt[w*(y)+(x)] = source;
			}
		}
	}
	return 0;
}
int EnhancedImage::binv()
{
	int threshold = 256 / 8 * 7;
	for(int y2=0;y2<superImage->height;y2++)
	{
		for(int x2=0;x2<superImage->width;x2++)
		{			
			Pixel pixel = superImage->data[y2*superImage->width+x2];
			if(pixel>=threshold)
			{
				superImage->data[y2*superImage->width+x2] = 255;
			}
			else
			{
				superImage->data[y2*superImage->width+x2] = 0;
			}
		}
	}
	return 0;
};

int EnhancedImage::otsu()
{
	int ihist[256];
	memset(ihist, 0, sizeof(ihist));	
	int gmin=255;
	int gmax=0;
	for (int y=0; y<superImage->height; y++) 
	{
		for (int x=0; x<superImage->width; x++) 
		{
			unsigned char point = superImage->data[y*superImage->width+x];
			ihist[point]++;
			if(point > gmax) 
			{
				gmax=point;
			}
			if(point < gmin) 
			{
				gmin=point;
			}
		}
	}	
	double sum = 0.0;
	int n = 0;	
	for (int k = 0; k <= 255; k++) 
	{
		sum += (double) k * (double) ihist[k];    // x*f(x) 质量矩
		n   += ihist[k];                          // f(x) 质量
	}	
	// do the otsu global thresholding method
	int threshold = 127;
	double fmax = -1.0;
	int n1 = 0;
	double csum = 0.0;
	for (k = 0; k < 255; k++) 
	{
		n1 += ihist[k];
		if (!n1) 
		{ 
			continue; 
		}
		int n2 = n - n1;
		if (n2 == 0) 
		{ 
			break; 
		}
		csum += (double) k *ihist[k];
		int m1 = csum / n1;
		int m2 = (sum - csum) / n2;
		int sb = (double) n1 *(double) n2 *(m1 - m2) * (m1 - m2);
		//note: can be optimized.
		if (sb > fmax) 
		{
			fmax = sb;
			threshold = k;
		}
	}
	//
	for(int y2=0;y2<superImage->height;y2++)
	{
		for(int x2=0;x2<superImage->width;x2++)
		{			
			Pixel pixel = superImage->data[y2*superImage->width+x2];
			if(pixel>threshold)
			{
				superImage->data[y2*superImage->width+x2] = 255;
			}
			else
			{
				superImage->data[y2*superImage->width+x2] = 0;
			}
		}
	}
	return 0;
};

/*************************************************************************
 *
 * 函数名称：
 *   Hough()
 *
 * 参数:
 *   LPSTR lpDIBBits    - 指向源DIB图像指针
 *   LONG  lWidth       - 源图像宽度（象素数，必须是4的倍数）
 *   LONG  lHeight      - 源图像高度（象素数）
 * 返回值:
 *   BOOL               - 运算成功返回TRUE，否则返回FALSE。
 *
 * 说明:
 * 该函数用于对检测图像中的平行直线。如果图像中有两条平行的直线，则将这两条平行直线
 * 提取出来。
 * 
 * 要求目标图像为只有0和255两个灰度值的灰度图像。
 ************************************************************************/

// 在计算图像大小时，采用公式：biSizeImage = biWidth' × biHeight。
// 是biWidth'，而不是biWidth，这里的biWidth'必须是4的整倍数，表示
// 大于或等于biWidth的，离4最近的整倍数。WIDTHBYTES就是用来计算
// biWidth'
#define WIDTHBYTES(bits)    (((bits) + 31) / 32 * 4)
#define pi 3.1415927
typedef struct{
	int Value;
	int Dist;
	int AngleNumber;
}MaxValue;
int EnhancedImage::line()
{
	//
	LONG lWidth = superImage->width;
	LONG lHeight = superImage->height;
	//
	LPSTR lpDIBBits = (char *)LocalAlloc(LHND, lWidth * lHeight);
	if (lpDIBBits == NULL)
	{
		return false ;
	}	
	lpDIBBits = (char *)LocalLock(lpDIBBits);
	//
	for (int y=0; y<superImage->height; y++) 
	{
		for (int x=0; x<superImage->width; x++) 
		{
			unsigned char point = superImage->data[y*superImage->width+x];            
			lpDIBBits[lWidth * y + x] = point; 
		}
	}
	//		
	//
	// 指向源图像的指针
	LPSTR	lpSrc;
	// 指向缓存图像的指针
	LPSTR	lpDst;
	// 指向变换域的指针
	LPSTR   lpTrans;
	// 图像每行的字节数
	LONG lLineBytes;
	// 指向缓存DIB图像的指针
	LPSTR	lpNewDIBBits;
	HLOCAL	hNewDIBBits;
	//指向变换域的指针
	LPSTR	lpTransArea;
	HLOCAL	hTransArea;
	//变换域的尺寸
	int iMaxDist;
	int iMaxAngleNumber;
	//变换域的坐标
	int iDist;
	int iAngleNumber;
	//循环变量
	long i;
	long j;
	//像素值
	unsigned char pixel;
	//存储变换域中的两个最大值
	MaxValue MaxValue1;
	MaxValue MaxValue2;
	// 暂时分配内存，以保存新图像
	hNewDIBBits = LocalAlloc(LHND, lWidth * lHeight);
	if (hNewDIBBits == NULL)
	{
		// 分配内存失败
		return FALSE;
	}
	// 锁定内存
	lpNewDIBBits = (char * )LocalLock(hNewDIBBits);
	// 初始化新分配的内存，设定初始值为255
	lpDst = (char *)lpNewDIBBits;
	memset(lpDst, (BYTE)255, lWidth * lHeight);
	//计算变换域的尺寸
	//最大距离
	iMaxDist = (int) sqrt(lWidth*lWidth + lHeight*lHeight);
	//角度从0－180，每格2度
	iMaxAngleNumber = 90;
	//为变换域分配内存
	hTransArea = LocalAlloc(LHND, lWidth * lHeight * sizeof(int));
	if (hNewDIBBits == NULL)
	{
		// 分配内存失败
		return FALSE;
	}
	// 锁定内存
	lpTransArea = (char * )LocalLock(hTransArea);
	// 初始化新分配的内存，设定初始值为0
	lpTrans = (char *)lpTransArea;
	memset(lpTrans, 0, lWidth * lHeight * sizeof(int));
	// 计算图像每行的字节数
	for(j = 0; j <lHeight; j++)
	{
		for(i = 0;i <lWidth; i++)
		{
			// 指向源图像倒数第j行，第i个象素的指针			
			lpSrc = (char *)lpDIBBits + lWidth * j + i;
			//取得当前指针处的像素值，注意要转换为unsigned char型
			pixel = (unsigned char)*lpSrc;
			//目标图像中含有0和255外的其它灰度值
			if(pixel != 255 && *lpSrc != 0)
				return FALSE;
			//如果是黑点，则在变换域的对应各点上加1
			if(pixel == 0)
			{
				//注意步长是2度
				for(iAngleNumber=0; iAngleNumber<iMaxAngleNumber; iAngleNumber++)
				{
					iDist = (int) fabs(i*cos(iAngleNumber*2*pi/180.0) + j*sin(iAngleNumber*2*pi/180.0));
					//变换域的对应点上加1
					*(lpTransArea+iDist*iMaxAngleNumber+iAngleNumber) = *(lpTransArea+iDist*iMaxAngleNumber+iAngleNumber) +1;
				}
			}
		}
	}
	//找到变换域中的两个最大值点
	MaxValue1.Value=0;
	MaxValue2.Value=0;
	//找到第一个最大值点
	for (iDist=0; iDist<iMaxDist;iDist++)
	{
		for(iAngleNumber=0; iAngleNumber<iMaxAngleNumber; iAngleNumber++)
		{
			if((int)*(lpTransArea+iDist*iMaxAngleNumber+iAngleNumber)>MaxValue1.Value)
			{
				MaxValue1.Value = (int)*(lpTransArea+iDist*iMaxAngleNumber+iAngleNumber);
				MaxValue1.Dist = iDist;
				MaxValue1.AngleNumber = iAngleNumber;
			}
		}
	}
	//将第一个最大值点附近清零
	for (iDist = -9;iDist < 10;iDist++)
	{
		for(iAngleNumber=-1; iAngleNumber<2; iAngleNumber++)
		{
			if(iDist+MaxValue1.Dist>=0 && iDist+MaxValue1.Dist<iMaxDist && iAngleNumber+MaxValue1.AngleNumber>=0 && iAngleNumber+MaxValue1.AngleNumber<=iMaxAngleNumber)
			{
				*(lpTransArea+(iDist+MaxValue1.Dist)*iMaxAngleNumber+(iAngleNumber+MaxValue1.AngleNumber))=0;
			}
		}
	}
	//找到第二个最大值点
	for (iDist=0; iDist<iMaxDist;iDist++)
	{
		for(iAngleNumber=0; iAngleNumber<iMaxAngleNumber; iAngleNumber++)
		{
			if((int)*(lpTransArea+iDist*iMaxAngleNumber+iAngleNumber)>MaxValue2.Value)
			{
				MaxValue2.Value = (int)*(lpTransArea+iDist*iMaxAngleNumber+iAngleNumber);
				MaxValue2.Dist = iDist;
				MaxValue2.AngleNumber = iAngleNumber;
			}
		}
	}
	//判断两直线是否平行
	if(abs(MaxValue1.AngleNumber-MaxValue2.AngleNumber)<=2)
	{
		//两直线平行，在缓存图像中重绘这两条直线
		for(j = 0; j <lHeight; j++)
		{
			for(i = 0;i <lWidth; i++)
			{	
				// 指向缓存图像倒数第j行，第i个象素的指针			
				lpDst = (char *)lpNewDIBBits + lLineBytes * j + i;	
				//如果该点在某一条平行直线上，则在缓存图像上将该点赋为黑
				//在第一条直线上
				iDist = (int) fabs(i*cos(MaxValue1.AngleNumber*2*pi/180.0) + j*sin(MaxValue1.AngleNumber*2*pi/180.0));
				if (iDist == MaxValue1.Dist)
					*lpDst = (unsigned char)0;
				//在第二条直线上
				iDist = (int) fabs(i*cos(MaxValue2.AngleNumber*2*pi/180.0) + j*sin(MaxValue2.AngleNumber*2*pi/180.0));
				if (iDist == MaxValue2.Dist)
					*lpDst = (unsigned char)0;
			}
		}
	}
	// 复制腐蚀后的图像
	memcpy(lpDIBBits, lpNewDIBBits, lWidth * lHeight);
	// 释放内存
	LocalUnlock(hNewDIBBits);
	LocalFree(hNewDIBBits);
	// 释放内存
	LocalUnlock(hTransArea);
	LocalFree(hTransArea);
	//
	//
	for (int yy=0; yy<superImage->height; yy++) 
	{
		for (int xx=0; xx<superImage->width; xx++) 
		{
			unsigned char point = lpDIBBits[lWidth * yy + xx];            
            superImage->data[yy*superImage->width+xx] = point; 
		}
	}
	//
	LocalUnlock(lpDIBBits);
	LocalFree(lpDIBBits);
	// 返回
	return TRUE;
}
int EnhancedImage::roii()
{
    int minX = superImage->width;
	int minY = superImage->height;
	int maxX = 0;
	int maxY = 0;
	//
	for (int y=0; y<superImage->height; y++) 
	{
		for (int x=0; x<superImage->width; x++) 
		{
			unsigned char point = superImage->data[y*superImage->width+x];
			if(point==0)
			{
				if(x<minX)
				{
					minX = x;					
				}
				if(y<minY)
				{
                    minY = y;
				}
				//
				if(x>maxX)
				{
					maxX = x;
				}
				if(y>maxY)
				{
					maxY = y;
				}
			}
		}
	}
	//
	if(minX>maxX)
	{
		minX=maxX=0;
	}
	if(minY>maxY)
	{
		minY=maxY=0;
	}
	//
	if(minX>0)
		minX = minX -1;
	if(minY>0)
		minY = minY -1;
	if(maxX<superImage->width-1)
		maxX= maxX+1;
	if(maxY<superImage->height-1)
		maxY = maxY+1;
	//
	int tmpW = maxX - minX+1;
	int tmpH = maxY - minY+1;
	SuperImage<Pixel>* tmpD = new SuperImage<Pixel>(tmpW,tmpH);
	//
	for(int y2=minY,y3=0;y3<tmpH;y2++,y3++)
	{
		for(int x2=minX,x3=0;x3<tmpW;x2++,x3++)
		{			
			Pixel pixel = superImage->data[y2*superImage->width+x2];
			tmpD->data[y3*tmpW+x3] = pixel;
		}
	}
	//
	if(superImage)
	{
		delete superImage;
		superImage = NULL;
	}
	//
	superImage = tmpD;
	//
	return 0;
};
/*************************************************************************
 *
 * 函数名称：
 *   TraceDIB()
 *
 * 参数:
 *   LPSTR lpDIBBits    - 指向源DIB图像指针
 *   LONG  lWidth       - 源图像宽度（象素数，必须是4的倍数）
 *   LONG  lHeight      - 源图像高度（象素数）
 * 返回值:
 *   BOOL               - 运算成功返回TRUE，否则返回FALSE。
 *
 * 说明:
 * 该函数用于对图像进行轮廓跟踪运算。
 * 
 * 要求目标图像为只有0和255两个灰度值的灰度图像。
 ************************************************************************/
int EnhancedImage::trac()
{
	typedef struct
	{
		int Height;
		int Width;
	}Point;
	//
	LONG lWidth = superImage->width;
	LONG lHeight = superImage->height;
	//
	LPSTR lpDIBBits = (char *)LocalAlloc(LHND, lWidth * lHeight);
	if (lpDIBBits == NULL)
	{
		return false ;
	}	
	lpDIBBits = (char *)LocalLock(lpDIBBits);
	//
	for (int y=0; y<superImage->height; y++) 
	{
		for (int x=0; x<superImage->width; x++) 
		{
			unsigned char point = superImage->data[y*superImage->width+x];            
			lpDIBBits[lWidth * y + x] = point; 
		}
	}
	//		
	//
	// 指向源图像的指针
	LPSTR	lpSrc;
	// 指向缓存图像的指针
	LPSTR	lpDst;
	// 指向缓存DIB图像的指针
	LPSTR	lpNewDIBBits;
	HLOCAL	hNewDIBBits;

	//循环变量
	long i;
	long j;
	//像素值
	unsigned char pixel;
	//是否找到起始点及回到起始点
	bool bFindStartPoint;
	//是否扫描到一个边界点
	bool bFindPoint;
	//起始边界点与当前边界点
	Point StartPoint,CurrentPoint;
	//八个方向和起始扫描方向
	int Direction[8][2]={{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0}};
	int BeginDirect;
	// 图像每行的字节数
	//LONG lLineBytes;
	// 计算图像每行的字节数
	//lLineBytes = WIDTHBYTES(lWidth * 8);
	// 暂时分配内存，以保存新图像
	hNewDIBBits = LocalAlloc(LHND, lWidth * lHeight);
	if (hNewDIBBits == NULL)
	{
		// 分配内存失败
		return FALSE;
	}
	// 锁定内存
	lpNewDIBBits = (char * )LocalLock(hNewDIBBits);
	// 初始化新分配的内存，设定初始值为255
	lpDst = (char *)lpNewDIBBits;
	memset(lpDst, (BYTE)255, lWidth * lHeight);
	//先找到最左上方的边界点
	bFindStartPoint = false;
	for (j = 0;j < lHeight && !bFindStartPoint;j++)
	{
		for(i = 0;i < lWidth && !bFindStartPoint;i++)
		{
			// 指向源图像倒数第j行，第i个象素的指针			
			lpSrc = (char *)lpDIBBits + lWidth * j + i;
			//取得当前指针处的像素值，注意要转换为unsigned char型
			pixel = (unsigned char)*lpSrc;
			if(pixel == 0)
			{
				bFindStartPoint = true;
				StartPoint.Height = j;
				StartPoint.Width = i;
				// 指向目标图像倒数第j行，第i个象素的指针			
				lpDst = (char *)lpNewDIBBits + lWidth * j + i;	
				*lpDst = (unsigned char)0;
			}		
		}
	}
	//由于起始点是在左下方，故起始扫描沿左上方向
	BeginDirect = 0;
	//跟踪边界
	bFindStartPoint = false;
	//从初始点开始扫描
	CurrentPoint.Height = StartPoint.Height;
	CurrentPoint.Width = StartPoint.Width;
	while(!bFindStartPoint)
	{
		bFindPoint = false;
		while(!bFindPoint)
		{
			//沿扫描方向查看一个像素
			lpSrc = (char *)lpDIBBits + lWidth * ( CurrentPoint.Height + Direction[BeginDirect][1]) + (CurrentPoint.Width + Direction[BeginDirect][0]);
			pixel = (unsigned char)*lpSrc;
			if(pixel == 0)
			{
				bFindPoint = true;
				CurrentPoint.Height = CurrentPoint.Height + Direction[BeginDirect][1];
				CurrentPoint.Width = CurrentPoint.Width + Direction[BeginDirect][0];
				if(CurrentPoint.Height == StartPoint.Height && CurrentPoint.Width == StartPoint.Width)
				{
					bFindStartPoint = true;
				}
				lpDst = (char *)lpNewDIBBits + lWidth * CurrentPoint.Height + CurrentPoint.Width;
				*lpDst = (unsigned char)0;
				//扫描的方向逆时针旋转两格
				BeginDirect--;
				if(BeginDirect == -1)
					BeginDirect = 7;
				BeginDirect--;
				if(BeginDirect == -1)
					BeginDirect = 7;
			}
			else
			{
				//扫描方向顺时针旋转一格
				BeginDirect++;
				if(BeginDirect == 8)
					BeginDirect = 0;
			}
		}
	}
	// 复制腐蚀后的图像
	memcpy(lpDIBBits, lpNewDIBBits, lWidth * lHeight);
	// 释放内存
	LocalUnlock(hNewDIBBits);
	LocalFree(hNewDIBBits);
	//
	//
	for (int yy=0; yy<superImage->height; yy++) 
	{
		for (int xx=0; xx<superImage->width; xx++) 
		{
			unsigned char point = lpDIBBits[lWidth * yy + xx];            
            superImage->data[yy*superImage->width+xx] = point; 
		}
	}
	//
	LocalUnlock(lpDIBBits);
	LocalFree(lpDIBBits);
	// 返回
	return TRUE;
}
int EnhancedImage::edge()
{
	//
	LONG lWidth = superImage->width;
	LONG lHeight = superImage->height;
	//
	LPSTR lpDIBBits = (char *)LocalAlloc(LHND, lWidth * lHeight);
	if (lpDIBBits == NULL)
	{
		return false ;
	}	
	lpDIBBits = (char *)LocalLock(lpDIBBits);
	//
	for (int y=0; y<superImage->height; y++) 
	{
		for (int x=0; x<superImage->width; x++) 
		{
			unsigned char point = superImage->data[y*superImage->width+x];            
			lpDIBBits[lWidth * y + x] = point; 
		}
	}
	//		
	//
	// 指向源图像的指针
	LPSTR	lpSrc;
	// 指向缓存图像的指针
	LPSTR	lpDst;
	// 指向缓存DIB图像的指针
	LPSTR	lpNewDIBBits;
	HLOCAL	hNewDIBBits;
	//循环变量
	long i;
	long j;
	unsigned char n,e,s,w,ne,se,nw,sw;
	//像素值
	unsigned char pixel;
	// 暂时分配内存，以保存新图像
	hNewDIBBits = LocalAlloc(LHND, lWidth * lHeight);
	if (hNewDIBBits == NULL)
	{
		// 分配内存失败
		return FALSE;
	}
	// 锁定内存
	lpNewDIBBits = (char * )LocalLock(hNewDIBBits);
	// 初始化新分配的内存，设定初始值为255
	lpDst = (char *)lpNewDIBBits;
	memset(lpDst, (BYTE)255, lWidth * lHeight);
	for(j = 1; j <lHeight-1; j++)
	{
		for(i = 1;i <lWidth-1; i++)
		{
			// 指向源图像倒数第j行，第i个象素的指针	
			lpSrc = (char *)lpDIBBits + lWidth * j + i;
			// 指向目标图像倒数第j行，第i个象素的指针
			lpDst = (char *)lpNewDIBBits + lWidth * j + i;
			//取得当前指针处的像素值，注意要转换为unsigned char型
			pixel = (unsigned char)*lpSrc;
			if(pixel == 0)
			{
				*lpDst = (unsigned char)0;
				nw = (unsigned char)*(lpSrc + lWidth -1);
				n  = (unsigned char)*(lpSrc + lWidth );
				ne = (unsigned char)*(lpSrc + lWidth +1);
				w = (unsigned char)*(lpSrc -1);
				e = (unsigned char)*(lpSrc +1);
				sw = (unsigned char)*(lpSrc - lWidth -1);
				s  = (unsigned char)*(lpSrc - lWidth );
				se = (unsigned char)*(lpSrc - lWidth +1);
				//如果相邻的八个点都是黑点
				if(nw+n+ne+w+e+sw+s+se==0)
				{
					*lpDst = (unsigned char)255;
				}
			}
		}
	}
	// 复制腐蚀后的图像
	memcpy(lpDIBBits, lpNewDIBBits, lWidth * lHeight);
	// 释放内存
	LocalUnlock(hNewDIBBits);
	LocalFree(hNewDIBBits);
	//
	//
	for (int yy=0; yy<superImage->height; yy++) 
	{
		for (int xx=0; xx<superImage->width; xx++) 
		{
			unsigned char point = lpDIBBits[lWidth * yy + xx];            
            superImage->data[yy*superImage->width+xx] = point; 
		}
	}
	//
	LocalUnlock(lpDIBBits);
	LocalFree(lpDIBBits);
	// 返回
	return TRUE;
}

int EnhancedImage::thin()
{
	//
	LONG lWidth = superImage->width;
	LONG lHeight = superImage->height;
	//
	LPSTR lpDIBBits = (char *)LocalAlloc(LHND, lWidth * lHeight);
	if (lpDIBBits == NULL)
	{
		return false ;
	}	
	lpDIBBits = (char *)LocalLock(lpDIBBits);
	//
	for (int y=0; y<superImage->height; y++) 
	{
		for (int x=0; x<superImage->width; x++) 
		{
			unsigned char point = superImage->data[y*superImage->width+x];            
            lpDIBBits[lWidth * y + x] = point; 
		}
	}
	//
	//
	LPSTR	lpSrc;				
	LPSTR	lpDst;	
	LPSTR	lpNewDIBBits;	
	HLOCAL	hNewDIBBits;	
	BOOL bModified;				
	long i,j,m,n;		
	
	BOOL con1;
	BOOL con2;
	BOOL con3;
	BOOL con4;
	
	unsigned char nCount;		
	unsigned char pixel;		
	unsigned char ne[5][5];	
	
	hNewDIBBits = LocalAlloc(LHND, lWidth * lHeight);
	if (hNewDIBBits == NULL)
	{
		return false ;
	}
	
	lpNewDIBBits = (char * )LocalLock(hNewDIBBits);
	
	// 初始化新分配的内存，设定初始值为255
	lpDst = (char *)lpNewDIBBits;
	memset(lpDst, (BYTE)255, lWidth * lHeight);
	
	bModified = TRUE;
	while(bModified)
	{
		bModified = FALSE;
		lpDst = (char *)lpNewDIBBits;
		memset(lpDst, (BYTE)255, lWidth * lHeight);
		
		for(j = 2; j <lHeight-2; j++)
		{
			for(i = 2;i <lWidth-2; i++)
			{
				con1 = FALSE;
				con2 = FALSE;
				con3 = FALSE;
				con4 = FALSE;
				
				lpSrc = (char *)lpDIBBits + lWidth * j + i;		
				lpDst = (char *)lpNewDIBBits + lWidth * j + i;
				
				pixel = (unsigned char)*lpSrc;
				if(pixel != 255 && *lpSrc != 0)
				{
					continue;
				}
				else if(pixel == 255)
				{
					continue;
				}
				
				//白色用0代表，黑色用1代表
				for (m = 0;m < 5;m++ )
				{
					for (n = 0;n < 5;n++)
					{
						ne[m][n] =(255 - (unsigned char)*(lpSrc + ((4 - m) - 2)*lWidth + n - 2 )) / 255;
					}
				}
				//判断2<=NZ(P1)<=6
				nCount =  ne[1][1] + ne[1][2] + ne[1][3] 
					+ ne[2][1]            + ne[2][3] 
					+ ne[3][1] + ne[3][2] + ne[3][3];
				if ( nCount >= 2 && nCount <=6)
				{
					con1 = TRUE;
				}
				
				//判断Z0(P1)=1
				nCount = 0;
				if (ne[1][2] == 0 && ne[1][1] == 1)
					nCount++;
				if (ne[1][1] == 0 && ne[2][1] == 1)
					nCount++;
				if (ne[2][1] == 0 && ne[3][1] == 1)
					nCount++;
				if (ne[3][1] == 0 && ne[3][2] == 1)
					nCount++;
				if (ne[3][2] == 0 && ne[3][3] == 1)
					nCount++;
				if (ne[3][3] == 0 && ne[2][3] == 1)
					nCount++;
				if (ne[2][3] == 0 && ne[1][3] == 1)
					nCount++;
				if (ne[1][3] == 0 && ne[1][2] == 1)
					nCount++;
				if (nCount == 1)
					con2 = TRUE;
				//判断P2*P4*P6=0 or Z0(p4)!=1
				if (ne[1][2]*ne[2][1]*ne[3][2] == 0)
				{
					con3 = TRUE;
				}
				else
				{
					nCount = 0;
					if (ne[1][1] == 0 && ne[1][0] == 1)
						nCount++;
					if (ne[1][0] == 0 && ne[2][0] == 1)
						nCount++;
					if (ne[2][0] == 0 && ne[3][0] == 1)
						nCount++;
					if (ne[3][0] == 0 && ne[3][1] == 1)
						nCount++;
					if (ne[3][1] == 0 && ne[3][2] == 1)
						nCount++;
					if (ne[3][2] == 0 && ne[2][2] == 1)
						nCount++;
					if (ne[2][2] == 0 && ne[1][2] == 1)
						nCount++;
					if (ne[1][2] == 0 && ne[1][1] == 1)
						nCount++;
					if (nCount != 1)
						con3 = TRUE;
				}
				//判断P2*P4*P8=0 or Z0(p2)!=1
				if (ne[1][2]*ne[2][1]*ne[2][3] == 0)
				{
					con4 = TRUE;
				}
				else
				{
					nCount = 0;
					if (ne[0][2] == 0 && ne[0][1] == 1)
						nCount++;
					if (ne[0][1] == 0 && ne[1][1] == 1)
						nCount++;
					if (ne[1][1] == 0 && ne[2][1] == 1)
						nCount++;
					if (ne[2][1] == 0 && ne[2][2] == 1)
						nCount++;
					if (ne[2][2] == 0 && ne[2][3] == 1)
						nCount++;
					if (ne[2][3] == 0 && ne[1][3] == 1)
						nCount++;
					if (ne[1][3] == 0 && ne[0][3] == 1)
						nCount++;
					if (ne[0][3] == 0 && ne[0][2] == 1)
						nCount++;
					if (nCount != 1)
						con4 = TRUE;
				}
				
				if(con1 && con2 && con3 && con4)
				{
					*lpDst = (unsigned char)255;
					bModified = TRUE;
				}
				else
				{
					*lpDst = (unsigned char)0;
				}
			}
		}		
		memcpy(lpDIBBits, lpNewDIBBits, lWidth * lHeight);
	}
	memcpy(lpDIBBits, lpNewDIBBits, lWidth * lHeight);
	LocalUnlock(hNewDIBBits);
	LocalFree(hNewDIBBits);
	//
	//
	for (int yy=0; yy<superImage->height; yy++) 
	{
		for (int xx=0; xx<superImage->width; xx++) 
		{
			unsigned char point = lpDIBBits[lWidth * yy + xx];            
            superImage->data[yy*superImage->width+xx] = point; 
		}
	}
	//
	LocalUnlock(lpDIBBits);
	LocalFree(lpDIBBits);
}
int EnhancedImage::tidy()
{
	//一个更好的算法，是要求整理之后，还保证原来的联通性，现在还不够好
	int h = this->superImage->height;
	int w = this->superImage->width;
	short* src = this->superImage->data;
	//
	for (int y=0; y<h; y++) 
	{
		for (int x=0; x<w; x++) 
		{
			unsigned char o = src[w*(y)+(x)];
			//
			unsigned char u = -1;					
			unsigned char ur = -1;					
			unsigned char r = -1;					
			unsigned char br = -1;					
			unsigned char b = -1;					
			unsigned char bl = -1;					
			unsigned char l = -1;					
			unsigned char ul = -1;	
			//
			if(y<h)
			{
				u = src[w*(y+1)+(x)];
			}
			if(y<h && x< w)
			{
				ur =src[w*(y+1)+(x+1)];
			}
			if(x<w)
			{
				r=src[w*(y)+(x+1)];
			}
			if(y>0 && x<w)
			{
				br = src[w*(y-1)+(x+1)];
			}
			if(y>0)
			{
				b = src[w*(y-1)+(x)];
			}
			if(y>0 && x>0)
			{
				bl = src[w*(y-1)+(x-1)];
			}
			if(x>0)
			{
				l = src[w*(y)+(x-1)];
			}
			if(y<h && x>0)
			{
				ul = src[w*(y+1)+(x-1)];
			}		
			//
			if(o==0)
			{
				if(r==0 && u==0 &&  br==0)
				{
					src[w*(y)+(x+1)] = 255;
				}
				if(r==0 && ur==0 &&  r==0)
				{
					src[w*(y)+(x+1)] = 255;
				}
				if(r==0 && ul==0 &&  br==0)
				{
					src[w*(y)+(x+1)] = 255;
				}
				//
				if(l==0 && u==0 &&  bl==0)
				{
                    src[w*(y)+(x-1)] = 255;
				}
				if(l==0 && u==0 &&  ur==0)
				{
                    src[w*(y)+(x-1)] = 255;
				}
				if(l==0 && bl==0 &&  ur==0)
				{
                    src[w*(y)+(x-1)] = 255;
				}
				if(l==0 && bl==0 &&  r==0)
				{
                    src[w*(y)+(x-1)] = 255;
				}
				if(l==0 && ul==0 &&  r==0)
				{
                    src[w*(y)+(x-1)] = 255;
				}
				if(l==0 && ul==0 &&  br==0)
				{
                    src[w*(y)+(x-1)] = 255;
				}
			}
		}
	}
	return 0;
}

int EnhancedImage::kerf()
{
	int w = this->superImage->width;
	int h = this->superImage->height;	
	short* src = this->superImage->data;
	//
	SuperImage<Pixel>* tmpD = new SuperImage<Pixel>(w,h);
	short* tgt = tmpD->data;
	//
	for (int y=0; y<h; y++) 
	{
		for (int x=0; x<w; x++) 
		{
			int count = 0;
			unsigned char p = src[y*w+x];
			tgt[y*w+x] = p;
			//			
			if(y<h && src[w*(y+1)+(x)]  == 0)
			{
				count = count + 1;
			}
			if(y<h && x< w && src[w*(y+1)+(x+1)]  == 0)
			{
				count = count + 1;
			}
			if(x<w && src[w*(y)+(x+1)]  == 0)
			{
				count = count + 1;
			}
			if(y>0 && x<w && src[w*(y-1)+(x+1)]  == 0)
			{
				count = count + 1;
			}
			if(y>0 && src[w*(y-1)+(x)]  == 0)
			{
				count = count + 1;
			}
			if(y>0 && x>0 && src[w*(y-1)+(x-1)]  == 0)
			{
				count = count + 1;
			}
			if(x>0 && src[w*(y)+(x-1)]  == 0)
			{
				count = count + 1;
			}
			if(y<h && x>0 && src[w*(y+1)+(x-1)]  == 0)
			{
				count = count + 1;
			}
			//
			if(p == 0 && count > 2)
			{
				tgt[y*w+x] = -1;
			}
		}
	}
	//
	if(superImage)
	{
		delete superImage;
		superImage = NULL;
	}
	//
	superImage = tmpD;
	//
	return 0;
}
int EnhancedImage::join()
{
	return 0;
}

//AntiCaptchaPart1.cpp
#include <stdio.h>
#include <string>
#include <windows.h>
#include "common.h"
//
void process(char* loadPathName,char* tempPathName)
{
	EnhancedImage otsuImage;
	otsuImage.load(loadPathName);
	if(1)
	{
		char convPathName[MAX_PATH];
		sprintf(convPathName,"%s%s",tempPathName,".001.conv.bmp");
		otsuImage.save(convPathName);
	}
	if(1)
	{
		char binvPathName[MAX_PATH];
		sprintf(binvPathName,"%s%s",tempPathName,".002.binv.bmp");
		otsuImage.binv();
		otsuImage.save(binvPathName);
	}
	if(1)
	{
		char otsuPathName[MAX_PATH];
		sprintf(otsuPathName,"%s%s",tempPathName,".003.otsu.bmp");
		otsuImage.otsu();
		otsuImage.save(otsuPathName);
	}
	if(0)
	{
		char linePathName[MAX_PATH];
		sprintf(linePathName,"%s%s",tempPathName,".004.line.bmp");
		otsuImage.line();
		otsuImage.save(linePathName);
	}
	if(1)
	{
		char roiiPathName[MAX_PATH];
		sprintf(roiiPathName,"%s%s",tempPathName,".005.roii.bmp");
		otsuImage.roii();
		otsuImage.save(roiiPathName);
	}
	EnhancedImage tracImage;
	tracImage.copy(&otsuImage);
	if(1)
	{
		char tracPathName[MAX_PATH];
		sprintf(tracPathName,"%s%s",tempPathName,".006.trac.bmp");
		tracImage.trac();
		tracImage.save(tracPathName);
	}
	//
	EnhancedImage edgeImage;
	edgeImage.copy(&otsuImage);
	if(1)
	{
		char edgePathName[MAX_PATH];
		sprintf(edgePathName,"%s%s",tempPathName,".007.edge.bmp");
		edgeImage.edge();
		edgeImage.save(edgePathName);
	}
	//
	EnhancedImage thinImage;
	thinImage.copy(&otsuImage);
	if(1)
	{
		char thinPathName[MAX_PATH];
		sprintf(thinPathName,"%s%s",tempPathName,".008.thin.bmp");
		thinImage.thin();
		thinImage.save(thinPathName);
	}
	if(1)
	{
		char tidyPathName[MAX_PATH];
		sprintf(tidyPathName,"%s%s",tempPathName,".009.tidy.bmp");
		thinImage.tidy();
		thinImage.save(tidyPathName);
	}
	EnhancedImage kerfImage;
	kerfImage.copy(&thinImage);
	if(1)
	{
		char kerfPathName[MAX_PATH];
		sprintf(kerfPathName,"%s%s",tempPathName,".010.kerf.bmp");
		kerfImage.kerf();
		kerfImage.save(kerfPathName);
	}
	EnhancedImage filmImage;
	filmImage.copy(&kerfImage);
	if(1)
	{	
		char filmPathName[MAX_PATH];
		sprintf(filmPathName,"%s%s",tempPathName,".011.film.bmp");
		filmImage.film(&edgeImage);
	    filmImage.save(filmPathName);
	}
}
//
void travel()
{
    char homePathName[MAX_PATH];
	GetCurrentDirectory(MAX_PATH,homePathName);
	//
	SetCurrentDirectory(homePathName);
	SetCurrentDirectory(".\\output");
	WIN32_FIND_DATA	findDataDelete;
	HANDLE	hHandleDelete  =  FindFirstFile("*.*", &findDataDelete);
	int hasNextFileDelete = (hHandleDelete !=  INVALID_HANDLE_VALUE);
	while (hasNextFileDelete !=  0)
	{
		char deletePathName[MAX_PATH];
		GetFullPathName(findDataDelete.cFileName, MAX_PATH, deletePathName, NULL);
		printf("Delete %s\n",deletePathName);
		DeleteFile(deletePathName);
        hasNextFileDelete = FindNextFile(hHandleDelete, &findDataDelete);
	}
	if(hHandleDelete !=  INVALID_HANDLE_VALUE)
	{
		FindClose(hHandleDelete);
	}
	//
	//
	SetCurrentDirectory(homePathName);
	SetCurrentDirectory(".\\sample");
	WIN32_FIND_DATA	findData;
	HANDLE	hFindHandle  =  FindFirstFile("*.jpg", &findData);
	int hasNextFile = (hFindHandle !=  INVALID_HANDLE_VALUE);
	while (hasNextFile !=  0)
	{
		char loadPathName[MAX_PATH];
		GetFullPathName(findData.cFileName, MAX_PATH, loadPathName, NULL);		
		//
		char tempPathName[MAX_PATH];
        sprintf(tempPathName,"%s",loadPathName);
		for(int i=strlen(tempPathName);i>=0;i--)
		{
			if(tempPathName[i]=='\\')
			{
				break;
			}
			else
			{
				tempPathName[i]='\0';
			}
		}
		strcat(tempPathName,"..\\output\\");
		strcat(tempPathName,findData.cFileName);
		//
		printf("Process %s to %s\n",loadPathName,tempPathName);
		process(loadPathName,tempPathName);
		//
		//
		hasNextFile = FindNextFile(hFindHandle, &findData);
	}
	if(hFindHandle !=  INVALID_HANDLE_VALUE)
	{
		FindClose(hFindHandle);
	}
}
//
void main(int argc, char* argv[])
{
	printf("Anti Captcha ...\n");
	travel();
	printf("Anti Captcha !!!\n");
}
{% endraw %}
~~~

注： 在这里，我们可以看到，基本的部件（字母是分割开了，但可以造成统一字母的被切割成多个Component。 一种做法是：利用先验知识，做分割； 另外一种做法是，和第二部分的识别结合起来。 比如按照从左至右，尝试增加component来识别，如果不能识别而且component的总宽度，总面积还比较小，继续增加。 当然不排除拒识的可能性。 ）

### 3)字符部件组合和识别。

part2的代码展示了切割后的字母组合，和基于svm的字符识别的训练和识别过程。Detection.cpp中展示了ImageSpam检测过程中的一些字符分割和组合，layout的分析和利用的简单技术。 而Google的验证码的识别，完全可以不用到，仅做参考。

SVM及使用：

本质上，SVM是一个分类器，原始的SVM是一个两类分类的分类器。可以通过1:1或者1:n的方式来组合成一个多类分类的分类器。 天生通过核函数的使用支持高维数据的分类。从几何意义上讲，就是找到最能表示类别特征的那些向量（支持向量SV）,然后找到一条线，能最大化分类的Margin。

libSVM是一个不错的实现。

训练间断和识别阶段的数据整理和归一化是一样的。 这里的简单做法是：

- 首先：

~~~cpp
#define SVM_MAX +0.999
#define SVM_MIN +0.001
~~~

- 其次：

扫描黑白待识别字幕图片的每个像素，如果为0(黑色，是字母上的像素),那么svm中该位置就SVM_MAX,反之则反。

- 最后：

训练阶段，在svm的input的前面，为该类打上标记，即是那一个字母。
识别阶段，当然这个类别标记是SVM分类出来。

- 注意：

如果是SVM菜鸟，最好找一个在SVM外边做了包装的工具，比如样本选择，交叉验证，核函数选择这些，让程序自动选择和分析。

-----

代码：通过ReginGrowth来提取单个单个的字符，然后开始识别。

[查看代码(./pstzine_09_02.txt)](http://www.icylife.net/pstzine/0x02/html/pstzine_09_02.txt)

~~~cpp
{% raw %}
#include "SpamImage.h"
#include "svm-predict.h"
#include <algorithm>
#include <string>
#include <stdio.h>

#ifndef MAX
#define MAX(x,y) (((x) > (y)) ? (x) : (y))
#endif

#ifndef ABS
#define ABS(x) ((x<0) ? (-x) : (x))
#endif

bool x_more_than(const XBlock & m1, const XBlock & m2)
{
	return m1.x < m2.x;
};
void Layout::insert(int i,int x,int y)
{
    layout.insert(std::map<int,Point>::value_type(i,Point(x,y)));
};
void Layout::compute(Config& config,std::map<int,std::string>& lines,std::string& final)
{
	std::map<int,Point>::iterator it;
	std::vector<XBlock> xList;
	//
	int newFile = 1;
	while(layout.size() > 0)
	{
		int startY = -1;
		int startX = -1;
		int startI = -1;
		for(it=layout.begin();it!=layout.end();it++)
		{
			int i = (*it).first;
			Point xy=(*it).second;
			int x=xy.x;
			int y=xy.y;
			if(y > startY || startY == -1)
			{
				startY = y;
				startX = x;
				startI = i;
			}
		}
		//
		for(it=layout.begin();it!=layout.end();it++)
		{
			int i = (*it).first;
			Point xy=(*it).second;
			int x=xy.x;
			int y=xy.y;
		}
		//
		xList.clear();
		for(it=layout.begin();it!=layout.end();it++)
		{			
			int i = (*it).first;
			Point xy=(*it).second;
			int x=xy.x;
			int y=xy.y;
			if(y > startY - 12)
			{
				XBlock xBlock(i,x,y);
				xList.push_back(xBlock);
			}
		}
		//
		std::sort(xList.begin(), xList.end(), x_more_than);
		//
		for(int i=0;i<xList.size();i++)
		{
			XBlock xBlock=xList[i];
			layout.erase(xBlock.i);
			//
			char output='?';
			std::map<int,std::string>::iterator li = lines.find(xBlock.i);
			if(li!=lines.end())
			{
				const char* line = (*li).second.c_str();
				//printf("%s\n",line);
				output = predict_take((char*)line);
				//printf("output1=%c\n",output);
				char temp[2];
				temp[0]=output;
				temp[1]=0;
				final.append(temp);
				//printf("final=%s\n",final.c_str());
			}
			else
			{
				printf("Error case 1\n");
			}
			if(config.trainData)
			{
				char zFile[MAX_PATH];
				sprintf(zFile,"%s\\Z%08d.bmp",config.midstPath,xBlock.i);
				char aFile[MAX_PATH];
				sprintf(aFile,"%s\\A%08d(%c).bmp",config.midstPath,newFile,output);
				rename(zFile,aFile);
				//printf("%s --> %s\n\n",zFile,aFile);
			}
			//
			newFile = newFile + 1;
		}
	}
};

Project::Project(char* fileName)
{
	FILE* fp=fopen(fileName,"r");
	if(!fp)
	{
		printf("Can not load chararters project file.");
		return;
	}
	Charater* oneChar;
	while(true)
	{
		char flag;
		int result = fscanf(fp,"%c",&flag);
		if(result <=0)
		{
			break;
		}
		else
		{
			std::map<char,Charater>::iterator li = chars.find(flag);
			if(li != chars.end())
			{
				oneChar=&((*li).second);
			}
			else
			{
				oneChar=new Charater();
			}
			int size = 0;
			fscanf(fp,"(%d)",&size);
			int data;
			double diff = 0.0;
			std::string line;
			char buff[256];
			for(int i=0;i<size;i++)
			{
				fscanf(fp,"%d:",&data);
				sprintf(buff,"%d",data);
				line.append(buff);
			}			
			//printf("flag=%c  line=%s\n",flag,line.c_str());
			oneChar->lines.push_back(line);
			fscanf(fp,"\n",buff);
		}
		chars.insert(std::map<char,Charater>::value_type(flag,*oneChar));
	}
	if(fp)
	{
		fclose(fp);
		fp=NULL;
	}	
};

RegionGrow::RegionGrow(int maxWidth,int maxHeight)
{
	nMaxWidth = maxWidth;
	nMaxHeight = maxHeight;
	//
	pucRegion = new unsigned char[maxWidth * maxHeight];
	//
	pbMirror = new bool*[maxHeight];
	for(int cy=0;cy<maxHeight;cy++)
	{
		pbMirror[cy] = new bool[maxWidth];
		for(int cx=0;cx<maxWidth;cx++)
		{			
			pbMirror[cy][cx] = true;
		}
	}
	//
	pnGrowQueueX = new int[maxWidth*maxHeight];
	pnGrowQueueY = new int[maxWidth*maxHeight];
};
RegionGrow::~RegionGrow()
{
	delete []pnGrowQueueX;
	delete []pnGrowQueueY;
	pnGrowQueueX = NULL ;
	pnGrowQueueY = NULL ;
	//
	for (int dy=0;dy<nMaxHeight;dy++) 
	{
		delete[] pbMirror[dy];
	}
	delete[] pbMirror;
	//
	delete []pucRegion;
	pucRegion = NULL  ;
};

bool RegionGrow::isNeighbor(RGBQUAD sourceCS,RGBQUAD targetCS,int average)
{
	int sourceGray=(sourceCS.rgbRed+sourceCS.rgbGreen+sourceCS.rgbBlue)/3.0;
	int targetGray=(targetCS.rgbRed+targetCS.rgbGreen+targetCS.rgbBlue)/3.0;	
	if( abs(sourceGray - targetGray) < 256/4 )
	{
		return true;
	}
	else
	{
		return false;
	}
};
void RegionGrow::recognizeSave(std::map<int,std::string> &lines,unsigned char* pUnRegion,int nWidth,int nHeight,int nLeftX,int nLeftY,int nRightX,int nRightY,Config& config,int saveName,char* line)
{
	if(line != NULL)
	{
		sprintf(line,"%d ",saveName);
		int index = 1;
		for(int y=nLeftY;y<=nRightY;y++)
		{
			for(int x=nLeftX;x<=nRightX;x++)
			{
				if(pUnRegion[y*nWidth+x] == 1)
				{
					sprintf(line,"%s%d:%lf ",line,index++,SVM_MAX);
				}
				else
				{
					sprintf(line,"%s%d:%lf ",line,index++,SVM_MIN);
				}
			}
		}
		lines.insert(std::map<int,std::string>::value_type(saveName,line));
	}
    //
	if(config.trainData)
	{
		CxImage image;
		int nWidthROI = nRightX-nLeftX+1;
		int nHeightROI = nRightY-nLeftY+1;
		image.Create(nWidthROI,nHeightROI,24,CXIMAGE_SUPPORT_BMP);
		RGBQUAD rgbSet;
		for(int sy=nLeftY;sy<=nRightY;sy++)
		{
			for(int sx=nLeftX;sx<=nRightX;sx++)
			{
				if(pUnRegion[sy*nWidth+sx] == 1)
				{
					rgbSet.rgbRed=255;
					rgbSet.rgbGreen=0;
					rgbSet.rgbBlue=0;
				}
				else
				{
                    rgbSet.rgbRed=0;
					rgbSet.rgbGreen=0;
					rgbSet.rgbBlue=0;
				}
				image.SetPixelColor(sx-nLeftX,sy-nLeftY,rgbSet);
			}
		}
		char file[MAX_PATH];
		if(line == NULL)
		{
			static int notText = 1;
			sprintf(file,"%s\\N%08d.bmp",config.midstPath,notText++);
		}
		else
		{
		    sprintf(file,"%s\\Z%08d.bmp",config.midstPath,saveName);
		}
		image.Save(file,CXIMAGE_SUPPORT_BMP);
	}
}
void RegionGrow::runRegionGrow(CxImage* cxImage,int nWidth,int nHeight,Config& config,Project &project,std::string& final) 
{
#define ROI_X_LEFT  1
#define ROI_X_RIGHT  1
#define ROI_Y_LEFT  1
#define ROI_Y_RIGHT  1
	
	//static int nDn = 4;
	//static int nDx[]={-1,+0,+1,+0};
	//static int nDy[]={+0,+1,+0,-1};
	
    static int nDn = 8;
	static int nDx[]={-1,+0,+1,+0, -1,-1,+1,+1};
	static int nDy[]={+0,+1,+0,-1, +1,-1,+1,-1};
	
    //static int nDn = 20;
	//static int nDx[]={-1,+0,+1,+0, -1,-1,+1,+1, -2,+2,-2,+2,-2,+2,+0,+0,-1,-1,+1,+2};
	//static int nDy[]={+0,+1,+0,-1, +1,-1,+1,-1, +0,+0,+1,+1,-1,-1,+2,-2,+2,-2,+1,-2};
	
	if(nWidth <= ROI_X_LEFT+ROI_X_RIGHT || nHeight <= ROI_Y_LEFT+ROI_Y_RIGHT)
	{
		printf("The image must be bigger than %d x %d (width * height)!\n",(ROI_X_LEFT+ROI_X_RIGHT),(ROI_Y_LEFT+ROI_Y_RIGHT));
		exit(1);
	}

	int nLocAvg = 0;
	for(int cy=nHeight-ROI_Y_RIGHT;cy>ROI_Y_LEFT;cy--)
	{
		for(int cx=ROI_X_LEFT;cx<nWidth-ROI_X_RIGHT;cx++)
		{
            RGBQUAD rgbCS = cxImage->GetPixelColor(cx,cy);
			RGBQUAD yuvCS = CxImage::RGBtoXYZ(rgbCS); 
			int gray = (yuvCS.rgbRed + yuvCS.rgbGreen + yuvCS.rgbBlue) / 3.0;
			RGBQUAD gryCS;
			gryCS.rgbRed = gray;
			gryCS.rgbGreen = gray;
			gryCS.rgbBlue = gray;
			cxImage->SetPixelColor(cx,cy,gryCS);			
			nLocAvg = nLocAvg + gray;
		}
	}
	nLocAvg /= ( (nHeight-ROI_Y_RIGHT-ROI_Y_LEFT) * (nWidth-ROI_X_RIGHT-ROI_X_LEFT) ) ;

	int nPixel = 0;
	int nLeftX = 0;
	int nLeftY = 0;
	int nRightX = 0;
	int nRightY = 0;
    int debugFile=1;
	std::map<int,std::string> lines;
	
	for(int my=nHeight-ROI_Y_RIGHT;my>ROI_Y_LEFT;my--)
	{
		for(int mx=ROI_X_LEFT;mx<nWidth-ROI_X_RIGHT;mx++)
		{
			if(pbMirror[my][mx])
			{
				memset(pucRegion,0,sizeof(unsigned char)* nWidth * nHeight);
				nPixel = 1;
                nLeftX = mx;
				nLeftY = my;
				nRightX = mx;
				nRightY = my;
				int nStart = 0 ;
				int nEnd   = 0 ;
				pnGrowQueueX[nEnd] = mx;
				pnGrowQueueY[nEnd] = my;
				int nCurrX ;
				int nCurrY ;
				int xx;
				int yy;
				int k ;
				while (nStart<=nEnd)
				{
					nCurrX = pnGrowQueueX[nStart];
					nCurrY = pnGrowQueueY[nStart];
					for (k=0;k<nDn;k++)	
					{	
						xx = nCurrX+nDx[k];
						yy = nCurrY+nDy[k]; 
						if ((xx < nWidth) && (xx>=0) && (yy<nHeight) && (yy>=0) && (pucRegion[yy*nWidth+xx]==0) )
						{
							if(isNeighbor(cxImage->GetPixelColor(xx,yy),cxImage->GetPixelColor(nCurrX,nCurrY),nLocAvg))
							{
								nEnd++;
								pnGrowQueueX[nEnd] = xx;
								pnGrowQueueY[nEnd] = yy;
								pucRegion[yy*nWidth+xx] = 1;
								nPixel++;
								if(xx < nLeftX) 
								{
									nLeftX=xx;
								}
								else if(xx > nRightX)
								{
									nRightX=xx;
								}
								if(yy < nLeftY) 
								{
									nLeftY=yy;
								}
								else if(yy > nRightY)
								{
									nRightY=yy;
								}
                                pbMirror[yy][xx] = false;
								pbMirror[nCurrY][nCurrX] = false;   //FAST
							}
						}
					}
					nStart++;
				}		
				const static int TOO_SMALL = 11;
				const static int TOO_HIGH = 19;
				const static int TOO_SHORT = 6;				
				if(nPixel < TOO_SMALL)   //Ãæ»ýÌ«Ð¡
				{
					//printf("xxx: found no-text region case: too small (pixels: %d<%d)\n",nPixel,TOO_SMALL);
					//recognizeSave(lines,pucRegion,nWidth,nHeight,nLeftX,nLeftY,nRightX,nRightY,config,debugFile,NULL);
					continue;
				}
				else if(nRightY-nLeftY > TOO_HIGH)  //Ì«¸ß
				{
					//printf("xxx: found no-text region case: too high (height: %d>%d)\n",nRightY-nLeftY,TOO_HIGH);
					//recognizeSave(lines,pucRegion,nWidth,nHeight,nLeftX,nLeftY,nRightX,nRightY,config,debugFile,NULL);
					continue;
				}
				else if(nRightY-nLeftY < TOO_SHORT)  //Ì«°«
				{
					//printf("xxx: found no-text region case: too short (height: %d<%d)\n",nRightY-nLeftY,TOO_SHORT);
					//recognizeSave(lines,pucRegion,nWidth,nHeight,nLeftX,nLeftY,nRightX,nRightY,config,debugFile,NULL);
					continue;
				}
				else if( (nRightX-nLeftX) >= (nRightY-nLeftY) * 1.6 )  //¿í´óÓÚ¸ß
				{
					//printf("???: found merged block: (%d,%d) --> (%d,%d)\n",nLeftX,nLeftY,nRightX,nRightY);
					//Ô¤ÇÐ
					int nWidthROI = nRightX-nLeftX+1;
					int nHeightROI = nRightY-nLeftY+1;
					int aLeftY=nLeftY;
					int aRightY=nRightY;
					int aLeftX=nLeftX;
					int aRightX=nLeftX+nHeightROI-1;   // *1.1
					while(true)
					{
						int aW=aRightX-aLeftX+1;
						int aH=aRightY-aLeftY+1;
						char* line = new char[aW*aH*32];
						memset(line, 0, aW*aH*32);
						recognizeSave(lines,pucRegion,nWidth,nHeight,aLeftX,aLeftY,aRightX,aRightY,config,debugFile,line);
						layout.insert(debugFile,nLeftX,nLeftY);
						debugFile = debugFile + 1;
						//Ê¶±ð
						char output = predict_take(line);
						delete line;
						//XÍ¶Ó° (ÉÏÂÖÀª + ÏÂÂÖÀª)
						int* projectX =  new int[aW];
						int* projectXScaled =  new int[aW];
						for(int px1=aLeftX,index=0;px1<=aRightX;px1++,index++)
						{
							projectX[index] = 0;
							for(int py1=aLeftY;py1<=aRightY;py1++)
							{
								if(pucRegion[py1*nWidth+px1] == 1)
								{
									projectX[index] = projectX[index]+1;
								}
							}
							//5-scale
							projectXScaled[index] = (int)( (double)projectX[index] / (double)aH * 5.0 );
						}
						//ÂÖÀª
						Charater oneChar;
						std::map<char,Charater>::iterator li = project.chars.find(output);
						if(li != project.chars.end())
						{
							oneChar=(*li).second;			
						}
						int matchedSize = 0;
						double matchedDiff = aW * 5.0;		
						for(int c=0;c<oneChar.lines.size();c++)
						{
							const char* line=oneChar.lines[c].c_str();
							int size=strlen(line);
							double diff = 0.0;
							for(int i=0;i<size && i<aW;i++)
							{
								char temp[2];
								temp[0]=line[i];
								temp[1]=0;
								int data=atoi(temp);
								diff = diff + abs(projectXScaled[i]-data);
								//printf("project=%d  current=%d    diff=%lf\n",projectXScaled[i],data,diff);
							}
							//ÐèÒªÉè¼ÆÕâÀïµÄÆÀ¼Ûº¯Êý size/aW, size/matchedSize, diff/matchedDiff
							if(diff < matchedDiff)
							{
								matchedDiff = diff;
								matchedSize = size;
							}
						}
						delete projectXScaled;
						delete projectX;
						//printf("matchedSize=%d  matchedDiff=%lf\n",matchedSize,matchedDiff);
						//
						if(matchedSize == 0)
						{
							matchedSize = nHeightROI;
						}
						aLeftX=aLeftX+matchedSize;
						aRightX=aLeftX+nHeightROI-1;	//*1.1
						if(aLeftX >= nRightX-1)
						{
							break;
						}
						if(aRightX > nRightX)
						{
							aRightX=nRightX;
						}
					}				
				}
				else
				{
					//printf("vvv: found ok-text region case: other condition\n");
					int aW=nRightX-nLeftX+1;
					int aH=nRightY-nLeftY+1;
					char* line = new char[aW*aH*32];
					memset(line, 0, aW*aH*32);					
					RegionGrow::recognizeSave(lines,pucRegion,nWidth,nHeight,nLeftX,nLeftY,nRightX,nRightY,config,debugFile,line);
					layout.insert(debugFile,nLeftX,nLeftY);
					debugFile =  debugFile + 1;
					delete line;
				}
			}
		}
	}
    layout.compute(config,lines,final);
};
{% endraw %}
~~~

## 六、对验证码设计的一些建议

1. 在噪音等类型的使用上，尽力让字符和用来混淆的前景和背景不容易区分。尽力让坏人（噪音）长得和好人（字母）一样。
2. 特别好的验证码的设计，要尽力发挥人类擅长而AI算法不擅长的。 比如粘连字符的分割和手写体（通过印刷体做特别的变形也可以）。 而不要一味的去加一些看起来比较复杂的噪音或者其他的花哨的东西。即使你做的足够复杂，但如果人也难识别，显然别人认为你是没事找抽型的。
3. 从专业的机器视觉的角度说，验证码的设计，一定要让破解者在识别阶段，反复在低阶视觉和高阶视觉之间多反复几次才能识别出来。 这样可以大大降低破解难度和破解的准确率。

## 七、个人郑重申明

1. 这个问题，本身是人工智能，计算机视觉，模式识别领域的一个难题。我是虾米，菜得不能再菜的那种。作为破解者来说，是出于劣势地位。要做的很好，是很难得。总体来说，我走的是比较学院派的线路，能真正的破解难度比较高的验证码，不同于网上很多不太入流的破解方法。我能做的只有利用有限的知识，抛砖引玉而已。 很多OCR的技术，特别是离线手写体中文等文字识别的技术，个人了解有限的很，都不敢在这里乱写。
2. 希望不要把这种技术用于非法用途。

------
