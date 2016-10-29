---
layout: post
title: Pygame介绍(ZZ)
date: 2015-06-23 07:47:42
categories: Coding
tags: Python ZZ
---

### [转载: Pygame介绍](http://www.cnblogs.com/kex1n/archive/2010/03/19/2286509.html)

------

 Pygame是一套用来写游戏的Python模块。它是基于SDL库的，它使你可以用Python语言创建完全界面化的游戏和多媒体程序。Pygame可以运行在几乎所有的平台和操作系统上。  
 Pygame是免费的，它是在LGPL许可证下发布的，你可以用它来创建免费软件、共享软件和商业游戏。  

-----

下面，我们用一个例子来了解一下用Pygame来写游戏：

~~~python
import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < orballrectright> width:
        speed[0] = -speed[0]
    if ballrect.top < orballrectbottom> height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
~~~

上面的代码创建了一个跳动的球的动画。

- 说明：
import pygame：引入pygame包中的所有有效的模块（必须）。  
pygame.init()：初始化所有引入的模块。在你需要用pygame做任何事之前，你必须初始化它。  
第8行：创建了一个图形化窗口，pygame用surface对象来描述图象。display.set_mode()函数创建一个新的surface来描述实际显示的图形。你在surface上画的任何东西都将在显示器上可见。  
第10行：我们装入了名为"ball.bmp"的图象。pygame支持多种图象格式，包括：JPG、PNG、TGA和GIF。pygame.image.load("ball.bmp")返回一个带有ball.bmp数据的surface。  
第11行：ball.get_rect()返回一个覆盖整个surface的矩形并赋给变量ballrect。这个矩形的左上角位于窗口的（0，0）的处，大小和所装入的图形一样。
第13行：我们开始一上无限的循环：检测用户的输入、移动图象、画图象。  
第17行~第21行：移动ballrect代表的矩形。  
第23行：用黑色填充窗口，以抹去以前的图形。  
第24行：重画图象。screen.blit(ball, ballrect)将变量ball中的图象数据画到变量ballrect指定的区域。到目前为止，图象还不可见。  
pygame.display.flip()：使你所画的在窗口中可见。  

------

另一个例子：

~~~ python
# picView - A simple image viewer written using PyGame library.
#
# Copyleft 2008 Bruce Jia
#

import os
import pygame
import pygame.image
from pygame import display

def isImageFile(filePath):
    lowerFilePath = filePath.lower()
    if (lowerFilePath.endswith('.jpg') or
        lowerFilePath.endswith('.png') or
        lowerFilePath.endswith('.bmp') or
        lowerFilePath.endswith('.gif') or
        lowerFilePath.endswith('.jpeg')):
        return True

    return False

class ImageFolder:
    def CurrentImage(self):
        if self.index == -1 or len(self.images) == 0:
            return ""
        return self.images[self.index]
    def NextImage(self):
        if 0 == len(self.images) or self.index == len(self.images) - 1:
            return ""
        
        self.index = self.index + 1
        return self.images[self.index]
        
    def PrevImage(self):
        if 0 == len(self.images) or self.index == -1:
            return ""
        
        self.index = self.index - 1
        if self.index >= 0:
            return self.images[self.index]
        pass
    def __init__(self, folderPath):
        self.images = []
        # TODO: add recursive search
        for file in os.listdir(folderPath):
            if (os.path.isfile(os.path.join(folderPath, file))):
                if (isImageFile(file)):
                    self.images.append(os.path.join(folderPath, file))
        self.index = -1
        pass

def ShowImageWithFitScale(screen, imageFilePath, angle=0):
    if (imageFilePath == None or imageFilePath == ""):
        return
    
    image = pygame.image.load(imageFilePath)
    scrWidth, scrHeight = screen.get_size()
    image = pygame.transform.rotate(image, angle)
        
    imgWidth, imgHeight = image.get_size()
    ratio = 1.0 * imgWidth / imgHeight
    if imgWidth > imgHeight:
        if imgWidth > scrWidth:
            imgWidth = scrWidth
            imgHeight = imgWidth / ratio
            if imgHeight > scrHeight:
                imgHeight = scrHeight
                imgWidth = imgHeight * ratio
    else:
        if imgHeight > scrHeight:
            imgHeight = scrHeight
            imgWidth = imgHeight * ratio
            if (imgWidth > scrWidth):
                imgWidth = scrWidth
                imgHeight = imgWidth / ratio

    image = pygame.transform.scale(image, (int(imgWidth), int(imgHeight)))
    posX = (scrWidth - imgWidth) / 2.0
    posY = (scrHeight - imgHeight) / 2.0
    screen.fill((0, 0, 0))
    screen.blit(image, (posX, posY))
    pygame.display.flip()
        
if __name__ == "__main__":
    from sys import argv
    if(len(argv) < 2):
        print "Usage: picView.py "
        sys.exit(1)
    folderPath = argv[1]
    print "Showing pictures in " + folderPath
    imageFolder = ImageFolder(folderPath)
    display.init()
    screen = display.set_mode((0,0), pygame.FULLSCREEN)
    quit = False
    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
                    break
                elif event.key in [pygame.K_UP, pygame.K_PAGEUP, pygame.K_F7, pygame.K_BACKSPACE]:
                    angle = 0
                    ShowImageWithFitScale(screen, imageFolder.PrevImage(), angle)
                elif event.key in [pygame.K_DOWN, pygame.K_PAGEDOWN, pygame.K_F8, pygame.K_RETURN, pygame.K_SPACE]:
                    angle = 0
                    ShowImageWithFitScale(screen, imageFolder.NextImage(), angle)
                elif event.key == pygame.K_LEFT:
                    angle = angle + 90
                    ShowImageWithFitScale(screen, imageFolder.CurrentImage(), angle)
                elif event.key == pygame.K_RIGHT:
                    angle = angle - 90
                    ShowImageWithFitScale(screen, imageFolder.CurrentImage(), angle)
                elif event.key == pygame.K_F5:
                    angle = 0
                    ShowImageWithFitScale(screen, imageFolder.CurrentImage(), angle)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ShowImageWithFitScale(screen, imageFolder.NextImage())
        if quit:
            break
    print "Byebye!"
    display.quit()

~~~

------
