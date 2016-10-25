---
layout: post
title: 重装Mac系统
date: 2016-10-17 03:46:39
categories: IT
tags: Mac OS System
---




Macbook Pro系列在2012 Late后出的款基本SSD都是类似NGFF(MD.2)类型的SSD, 但是其接口又跟别人不同!!! NND.. 在JD创见上一条适合2012 late(A1425)的256G SSD居然就要999...

后来发现某宝上面有转接口, 虽然非官方, 但理论上只是转接不影响速度, 所以就买来尝试一下, 买的是msata转2012 mac 接口的. 还有NGFF转的, 下次试试~

随后就要重装系统了!! 其实更快的方法应该是使用Time Machine来把旧硬盘内容备份后再重装过去.. 懒得搞了, 因为实在想系统重新弄一下.

---------

准备工作: 下载好一个你最终想运行的mac os 的镜像(dmg), 一个8G以上的**空**U盘, 给力的网络.

- 格式化U盘: `磁盘工具`里选中U盘( 别选错了!! ) 后, 选`抹掉`, 格式`Mac OS 扩展 (日志式)`, 名称随意, 例如叫MacInstall. 
- 系统安装到U盘: 随后选`恢复`, *原磁盘* 是mac os镜像文件, *目的磁盘*是格式好的U盘, 然后点 *恢复* 即可. 
- 重启电脑, 按住option, 进去后选择刚才的U盘(名字应该是你自己起的, 颜色是橙黄色). 同时选择好网络
- 然后进入 `Mac OS X` 使用工具, 如果升级或者覆盖就选`重新安装Mac OS X`, 也可以选磁盘工具重新格式化硬盘后再安装
- 安装进入后, 就是继续, 选中需要安装的系统, 同意协议, 然后就慢慢安装了. 等啊等, 可能重启两次, 就装好了~

如果出现以下问题, 根据说明解决就可以了, 尤其旧版的OS, 需要更改系统时间. 

如果下载的是`app`应用格式, 安装方法略有差异. 

- 将app拉到左侧的`应用程序` (即 Applications) 里
- 使用命令行来将系统刻到U盘, 其中U盘的盘号这里叫 MacInstall , 根据自己上面定义的更改这部分即可, 别的OS类似更改地址. 再后续的和之前一样:

~~~bash
sudo /Applications/Install\ OS\ X\ Yosemite.app/Contents/Resources/createinstallmedia --volume /Volumes/MacInstall --applicationpath /Applications/Install\ OS\ X\ Yosemite.app --nointeraction
# Erasing Disk: 0%... 10%... 20%... 30%...100%...
# Copying installer files to disk...
# Copy complete.
# Making disk bootable...
# Copying boot files...
# Copy complete.
# Done.
~~~

---------

> 安装 OS X Yosemite”应用程序副本不能验证。它在下载过程中可能已遭破坏或篡改

这是由于Apple更新开发者证书后导致的副本无法验证. 只要将日期改后即可. 如果以及在启动后进入安装状态下, 可以在菜单-`实用工具`找到里面的 `terminal` 程序, 打开运行以下即可

~~~bash
date 062614102014.30
~~~

如果不是在重启后进入的安装状态而是正常系统里, 就要前面加`sudo`咯

> 准备安装时发生错误 请尝试重新运行此应用程序

这个问题发生在我直接双击下载的os.app 又解决了上述副本问题后出现的提示. 原因是, 不能直接在正常运行的系统里面这样搞, 要把os.app 刻到符合格式的盘里 ([官方解释](https://support.apple.com/zh-cn/HT203600)). 只要把系统盘刻到U盘用重启安装法即可.

> 无效的校验和

打开dmg镜像时出现这个. 可以 `md5 ./Install\ OS\ X\ El\ Capitan.app/Contents/SharedSupport/InstallESD.dmg` 检查一下md5, 去网上搜一下该版本md5对不对. 不对的话就是这个dmg镜像损毁了.

- 更改主机名： `sudo scutil --set HostName MacBookPro`
- 修改共享电脑名: `sudo scutil --set ComputerName MacBookPro`

- X11 [XQuartz](https://www.xquartz.org/)
- NTFS-3G: 使用brew来安装比较方便: `brew cask install osxfuse; brew install homebrew/fuse/ntfs-3g; sudo mv /sbin/mount_ntfs /sbin/mount_ntfs.original; sudo ln -s /usr/local/sbin/mount_ntfs /sbin/mount_ntfs`


### Office 

2016版15.14.0 [Microsoft Office 2016 for Mac 15.14.0安装包与和谐方法](http://bbs.feng.com/read-htm-tid-9928890.html), 很简明扼要 挺好用. 可以解15.15.
2016版15.19 [Microsoft Office 2016 For Mac正式版+破解补丁](http://bbs.feng.com/read-htm-tid-9704285.html), 使用官方的[最新版](http://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/OfficeMac/Microsoft_Office_2016_Installer.pkg), 补丁是[Patch Office 15.3.1 v1.3.pkg.zip](http://bbs.feng.com/plugin.php?id=attachment_download:tongji&aid=12561885&name=patch+office+15.3.1+v1.3.pkg.zip&server=http://att4.weiphone.net&url=201609/26/150806h54zmkgg4s39ms52.zip)

### Links

- [Mac OS X各系统版本下载(10.5.X-10.11.6)](http://www.applex.net/threads/64332/) :这个帖子是每个系统最后一个版本都需要回复才能下载, 但是嘛~这些升级包都是比较容易在官网找到的
- [国外Macdrug](http://macdrug.com/download-yosemite-dmg-os-x-10-10-without-apple-store/#)提供的[Yosemite app下载](http://eshareload.com/download/dl/guest/eshareload.com_Yosemite%20DMG%20Mac%20OS%20X.zip)
- [Mac OS X Yosemite 10.10.5 更新包官方下载](https://support.apple.com/kb/DL1832?viewlocale=en_US&locale=en_US): 仅适于对Yosemite系统升级, 不能用于安装. 下载后双击在运行里面的pkg即可.
- [XClient](http://xclient.info/) 有不少好的Mac工具下载

------
