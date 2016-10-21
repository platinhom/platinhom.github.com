---
layout: post
title: 新电脑新系统-Win10+Ubuntu
date: 2016-05-31 23:26:46
categories: IT
tags: System
---

好久好久没有写blog了, 好像失踪si了一样. 忙着找工作啊, 结掉米国这边的东东. 

新买了一台Lenovo的Yoga 900, 看起来很酷, Bestbuy Open Box退伍军人节再打9折,900刀含税. Win10系统, 256GB硬盘, 有点少.. 用来日常办公吧. 不过和MBP有点冲突...

自带Win10系统, 打算装双系统, 就是日常办公调试, 可能也够用吧.

安装office 2013的话需要去找一个[microsoft toolkit](http://forums.mydigitallife.info/threads/28669-Microsoft-Toolkit-Official-KMS-Solution-for-Microsoft-Products),这个据说是最早的发布网站.

## Win10系统初探

Win10是针对触屏进行改进的系统, 和Win7还是有很大区别的(Win8就忽略了吧), 感觉上Win10 2 in 1 本有以下区别:

- App应用: 和一般exe装程序不同, app应用通过微软Store来安装.例如qq或者网易云音乐就是更贴切平板控制模式, 更适合触屏. 另外, 空间也省点. 换句话, 就是Win10既可以像以往操作系统那样安装程序, 也可以像手机平板那样从商店安装APP.
- 操作中心: 类似于安卓那种顶部提示中心和一些功能的快捷控制(例如wifi,定位,飞行模式等). 这种设计就是为了Win10用于手机和平板吧. 我电脑可以右划调出操作中心, 也可以按个右下角一个信息提示一样的图标调出.
- 虚拟桌面和任务视图: 就是Win键+Tab的功能, 不过现在还可以设置多个桌面, 有点像Mac里面的任务-桌面控制视图.
- 平板模式: 在操作中心里面就有, 选了以后键盘禁用, 开始菜单变得更像手机里面一个一个大图标(Win8那种全屏列表). 另外, 旋转控制的键这时就可以用了, 电脑就像平板一样.
- Cortana, 类似于Siri吧, 我就用来搜索..
- 开始菜单: 变得更复杂, 可以定制菜单位置啊, 内容了, 还有平板模式. Win8是横向列出程序, Win10是纵向的, 怪怪的...
- EDGE浏览器: 感觉还可以, 速度也OK.
- 新的设置菜单: 也是为了平板设计的吧, 图标大大的, 功能和控制面板类似, 摆放得不习惯, 需要学习周期.
- 高分屏设计: 分辨率, 自定义DPI, 字体等都有所改进, 为了4K屏吧.

总体感觉, Win10系统和Win7其实差异也不大, 更兼容于手机和平板的系统, 比Win8又更像桌面系统. 如果更偏向于桌面系统, Win7足矣 (反正国人也是用盗版..Win10免费特性也用不上).

----------

附虚拟桌面快捷键：

- 贴靠窗口：Win +左/右> Win +上/下>窗口可以变为1/4大小放置在屏幕4个角落
- 切换窗口：Alt + Tab（不是新的，但任务切换界面改进）
- 任务视图：Win + Tab（松开键盘界面不会消失）
- 创建新的虚拟桌面：Win + Ctrl + D
- 关闭当前虚拟桌面：Win + Ctrl + F4
- 切换虚拟桌面：Win + Ctrl +左/右


## Win10安装双系统

1. 去[Ubuntu官网](http://www.ubuntu.com/)下载系统, 这里下载的是[个人桌面版](http://www.ubuntu.com/download/desktop). 下载文件是iso文件, 可以写到光盘或者U盘.
2. 找个U盘4G左右大小, 备份好数据后, 格式化掉.
3. 下载[UltraISO](https://www.ezbsystems.com/ultraiso/download.htm),试用版即可, 使用不介绍了(打开iso,写入硬盘映像,选择U盘写入即可)
4. 然后准备好一个分区空间用来安置Ubuntu, 打开 **磁盘管理**, 我从C盘里选择压缩磁盘, 压缩出48G出来. (记住盘符哦!)
5. 准备好后,重启, 使用自己电脑设置boot顺序的方法选择U盘启动(例如Yoga 900是完全关机后捅侧面的小键). 然后进去就可以开始安装Ubuntu了.
6. 安装一些常规就不说了, 有两步很重要: 第一是安装类型选择其他选项(Other option), 来自定义分区(比较稳妥), 第二是设置分区表.
7. 分区表, 选择刚才释放空间出来的分区(空闲空间), 点击下面的`+`号用来添加分区, 主要是三个:
	- 系统文件, `/`, 分区类型主分区, 分区位置空间起始位置, Ext4 日志文件系统, 挂载点: `/`
	- 虚拟内存交换分区, `swap`, 内存较小(<2G)时建议是物理内存2倍大小,较大的话一倍内存也就够了,再大也是8G据说就够了(例如我8G内存就是8192 MB). 逻辑分区, 空间起始位置, 用于Swap (没有挂载点)
	- 启动分区, `/boot`, 设置200MB就够了, 逻辑分区, 空间起始位置, Ext4 日志文件系统, 挂载点: `/boot`
	- 理论上还需要挂载一个`/home`分区来放用户文件(例如我就是16G给`/`,16G给`/home`), 但其实不挂也可以.
8. 分区表弄好后, 选中`/boot`分区, 看清楚是`/dev/sda?`,下面安装启动引导器的设备选择相应的/boot分区的`/dev/sda?` ( **很重要**). 
9. 然后其余就随意设置, 安装完后重启, 然后就会出现系统选择的界面(默认第一个是ubuntu, 不按键就会进入, 第三个是Win10). 如果没有系统选择界面而是进入了Win10, 可能需要更改BIOS里面EFI boot顺序(将Ubuntu的提前到第一)

图文安装参考Volcanoo的[Windows10+Ubuntu双系统安装(多图)](http://www.jianshu.com/p/2eebd6ad284d). 里面的快速启动可以关闭掉(以前帮Li qianhuan也不知道什么原因关过),禁用安全启动和后面的我后来就没有搞了, 不成功. 电脑主板和系统限制了. 

如能开机有Ubuntu的选择登入界面, 能就成功了, 如果没有, 直接进入ubuntu, 或者想修改ubuntu的开机Grub2. 可以参考:

1. Ubuntu内编辑 `sudo gedit /etc/default/grub`, `GRUB_HIDDEN_TIMEOUT=0` 和 `GRUB_HIDDEN_TIMEOUT_QUIET=true`两行注释掉(前面加`#`)
2. `sudo update-grub`, 更新grub信息. 实际上,grub的信息在`/boot/grub/grub.cfg` 文件内, 不太建议直接修改. 然后重启试试
3. 如果想登入时默认win10而不是ubuntu, 可以修改`/etc/default/grub`的`GRUB_DEFAULT=0`为`GRUB_DEFAULT=2` (第三项就是2),再`sudo update-grub`
4. 我是高分辨屏,选择时很不清, 可以更改上述文件的`#GRUB_GFXMODE=640x480`一行去掉注释. 再`sudo update-grub`
5. 如果只是想偶尔进去看看这个选择界面(包括什么安全模式),旧版ubuntu按着`shift`重启, 新版用按着`Esc`

PS: 

- 在上面的安装教程里有些东东是不需要的了, 例如EasyBCD. 新电脑的话都有[UEFI 统一可扩展固件接口](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface), 这玩意限制了对自由系统Linux的安装和双启动. 即使安装了EasyBCD也不能搞掂双系统选择, 有个帖子说要禁用UEFI后还要再重装Win10才可以(至少我根据帖子里的方法, 不用UEFI, 设置了Legacy的, 首选Legacy不是UEFI, 禁用Secure Boot, 停用了快速启动, 但都不能正常使用EasyBCD设置多启动选择, 所以可以不用白费力气安装EasyBCD和进行一大堆的BIOS设置了. 现在的Ubuntu兼容Win10的启动,将首boot设为Ubuntu就可以了, 就是没有这篇博文那样启动时那么fancy)
- 这篇[如何在 Win8 上禁用 UEFI 安全引导以安装Linux](https://linux.cn/article-3061-1.html)讲解禁用UEFI, 但我测试无效. 其实用 高级重启->疑难解答->UEFI设置重启电脑进入BIOS界面和直接进入BIOS界面是一样的. 另外, 高级重启在帖子里是用更新恢复->高级启动->立即重启实现, 更简单方法是, 开始菜单->电源->按着Shift键点重启就可以了.
- 帮朋友在Win7上面安装, 发现Ubuntu识别不了刚才压缩的空闲卷, 经研究, 因为刚硬盘分区是动态磁盘, 而不是基础磁盘. 解决方法是使用分区助手将其从[动态分区](http://disktool.cn)转为基础分区. 很奇怪, 还需要把有个盘删掉才可以.因为基础磁盘MBR分区最多四个分区(包含隐藏的一个),所以最多CDE三个盘. 当我转换为基础分区后, 新添加F盘就又变回去动态磁盘...然后空间太多, 想帮中间一个D盘扩展..一扩展就坏了, 尼玛将一大块又叫D盘,实际D盘变成了两块...然后删掉吧..然后D盘就挂了消失了... 大家小心...另外主分区只能有1-4号,逻辑分区从5-16号. 最后尝试使用[DiskGenius](http://www.diskgenius.cn/), [4.8破解](http://www.repaik.com/thread-66789-1-1.html)修复丢失的分区,修复能找到, 设置为GPT的分区格式就分区表损坏了..慎用..
- 旧版BIOS没有Boot顺序(也没有UEFI),这时可以用[EasyBCD](http://neosmart.net/EasyBCD/)来设置开机引导.具体可以参加上面提到的帖子. 据说UEFI可以用[EasyUEFI](http://www.easyuefi.com/index-cn.html),但设置看起来比较怪, 我直接改Ubuntu的Grub更容易.

## Ubuntu初探

这里安装的是Ubuntu 16.04 LTS 长期稳定版. 调用命令行`ctrl+alt+T`. 

不想不停地敲sudo就用`su -i`先登录root.

安装后先用apt-get测试安装pymol失败.. 

~~~bash
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package <package> 
~~~

原因是某些东东太老了. 先要更新一下ubuntu的所有软件:

`sudo apt-get update; sudo apt-get upgrade`

PS: 这句命令依赖于 设置->软件和更新->更新 里面的三个更新内容, 如果都不勾选就不更新哦(例如我都取消勾选就装不了gfortran).这里的 `Other Software`的tab可以设置软件更新源, 即后面提到的 `apt-get-repository`命令添加的内容

然后就可以`sudo apt-get install pymol`,`sudo apt-get install python-pip`等来安装软件啦~ 安装软件需要在软件源里存在哦. 可以在ubuntu软件包里面搜索: [http://packages.ubuntu.com/](http://packages.ubuntu.com/)


#### 安装sogou拼音中文输入法

安装是在**Ubuntu 16.04 LTS 长期稳定版**测试

1. 到[官网](http://pinyin.sogou.com/linux/?r=pinyin)下载新版本的输入法
2. 不要双击安装, 因为默认安装器是GNOME的. 
3. cd到Download文件夹, `sudo dpkg -i sogoupinyin_2.0.0.0070_amd64.deb` 尝试使用dpkg安装
4. 上一步会失败(提示 *Error were encountered while processing sogoupinyin*), 此时再用 `sudo apt-get install -f` 自动解决上步失败的依赖关系
5. 重新`sudo dpkg -i sogoupinyin_2.0.0.0070_amd64.deb`, 可能会出现 *No such key 'Gtk/IMMOdule' in schema 'org.gnome.settings-daemon-plugins.xsetting' as specified in override file '/usr/share/glib-2.0/schemas/50_sogoupinyin.gschema.override'; ignoring override for this key* 这样的提示. 忽略它.
6. 点系统设置 *System Settings* -> 语言支持 *Language Support* -> 如果没有中文,点 `Install/Remove Languages` 安装简体中文. 会提示安装, 等.
7. **Keyboard input method system** (键盘输入法系统)那里选择fcitx (默认ibus, fcitx是支持搜狗输入法的中国人自制的输入法系统哦! 输入法图标重新登入后会变成一个键盘, 界面也和先前的不同)
8. Log out登出再登入(或者重启),这时输入法图标应该变成了fcitx.
9. 点击输入法图标, 设置, 进入输入法设置面板 (也可以命令行`fcitx-configtool`直接打开设置面板). 点击左下角的`+` 号添加输入法(默认就一个英语). 去掉那个Only show Current language 的选项, 然后搜索sogou,找到后OK. 好了添加完成了. 重启或者登出.

> 如果不想要ibus, 可以`sudo apt-get remove ibus scim` 卸掉, 不介意的话就不用卸了.  
> 据说12.04老版自带fcitx版本太旧, 需要升级. 可以用更新管理器,软件源添加 `ppa:fcitx-team/nightly`, 重新载入后搜出fcitx来更新. 或者用命令`sudo apt-get-repository ppa:fcitx-team/nightly`添加源再 `sudo apt-get update`自动升级. 
> 如果update时出现 `GPG error: http://.... all Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3C962022012520A0` 类似的, 用`sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3C962022012520A0` 这样去添加key (对应提示错误的key换掉这里的数字串).

## 设置东东

#### 开启多桌面和显示桌面图标

在 **设置-> Appearance -> Behavior** , 勾选开启workspaces和添加desktop icon 即可. 快捷键对应是 `win+S` 和`win+D`

#### 更改主机名 change hostname

~~~bash
sudo -i
hostname <newname>
~~~

if occur: `_IceTransSocketUNIXConnect: Cannot connect to non-local host oldname`

then change the `/etc/hosts` and `/etc/hostname` at the localhost name to newname

log out or restart the computer then new setup will be used.

#### 更改vi change vi

change vi configuration (further see [VIM启动设置](/2015/08/19/VIM_startupSetup/):

~~~bash
echo "set backspace=indent,eol,start
set nocompatible
set whichwrap=>
set hls
syntax on
set ruler
set showmatch
set nobackup
set cursorline
filetype on
set expandtab
set tabstop=4
set shiftwidth=4
set autoindent
" > ~/.vimrc
~~~

Then try to vi any file, if occur:

`Sorry, the command is not available in this version: syntax on`

try `vi` and then enter `:version`, if you are in `Small version without GUI.`, then you need to update your vi with gui. Try (indeed, only need first command in many cases):

~~~bash
sudo apt-get install vim-gui-common
sudo apt-get install vim-runtime
~~~

#### 设置命令行提示有颜色:

编辑.bashrc, 取消注释: `force_color_prompt=yes` 一行

搜索-单行列出
apt-cache search freetype | grep dev
搜索-多行列出
apt search freetype 

## 安装东东

可以使用官方的应用商店安装:

- Ubuntu Software Center : 另一个软件中心, 有更多软件选择
- FileZilla : FTP的软件罗
- 7zip: 压缩文件软件咯
- Ubuntu restricted extras : 一些常用软件依赖, 包括mp3支持啊, flash啊, codecs啊
- SMPlayer : 媒体播放软件
- ClassicMenu Indicator : 可以在菜单添加一个老式linux的所有应用的菜单栏
- Screenshot : 自带简介的截屏工具, 也可以用高级点的Shutter
- konsole : 多tab的命令行. 不过有点丑. 发现自带的Terminal可以设置新窗口为Tab, 所以就不用konsole了


###### Fix for some 32-bit software: 

Sometimes, it will say "No such file or directory: ** ", but indeed the file exists! In that case, it may be/need a 32-bit version file but the system is 64-bit. [Ref](http://askubuntu.com/questions/133389/no-such-file-or-directory-but-the-file-exists), use `file filename` and get “ELF 32-bit LSB executable …”, meaning the executable file is 32-bit. 

If some libraries is missing, use `ldd bin-file` to view its dependant library. And find it in google. If it's 32-bit library, you could:

~~~bash
## Missing libGL.so.1 32-bit
# Install 32-bit architecture (first to view foreign archi:i386)
sudo dpkg --print-foreign-architectures
sudo dpkg --add-architecture i386
# old version may install ia32-libs, newer ubuntu may install following two libraries
sudo apt-get install lib32ncurses5 lib32z1
# 32bit gcc-based compiler, may need degrade for some core libraries. In this case, use aptitude instead
sudo apt-get install aptitude
sudo aptitude install gcc-multilib
sudo aptitude install libgl1-mesa-glx:i386 libgl1-mesa-dri:i386 libxrender1:i386 libsm6:i386
~~~

Library in ubuntu in 32bit can be marked by `:i386` at last.

## 安装应用

需要下载的东东:

- [eclipse官方安装器](https://eclipse.org/downloads/) 其中[Linux版64位](https://www.eclipse.org/downloads/download.php?file=/oomph/epp/mars/R2/eclipse-inst-linux64.tar.gz): 下载后解压, 然后双击里面的`eclipse-inst`按着提示搞就是了. 需要系统有java支持.
- [Sublime text](https://www.sublimetext.com/3): 这个不用说了, 安装使用`dpkg -i abc.deb` 就可以了. [rockdrigo的gist](https://gist.github.com/rockdrigo/9ae723dc5bdaf1f49288)你懂.
- [Chimera](https://www.cgl.ucsf.edu/chimera/download.html), Linux64位下载(bin文件), `chmod +x chimera.bin` 后
命令行运行即可. 如要安装到非home目录记得sudo.
- [Foxit Reader](https://www.foxitsoftware.com/downloads/) 下载免费的Linux 64位版本, 解压后得一个run文件直接运行安装即可. 安装后把安装文件夹的`Foxit Reader.desktop`复制到`/usr/share/applications`, pdf右键在所有应用中就可以找到foxit. Foxit优点是可以高亮和注释, 而默认pdf阅读器是不行的(但默认阅读器感觉更快一些)
- [TexMacs](http://www.texmacs.org/tmweb/download/unix.en.html) : Write latex as you see.
- [VMD](http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD) : 下载(我下的是LINUX_64 CUDA)后修改configure文件内两个目录(一个二进制文件所在,一个库所在(各种脚本)),然后`./configure LINUXAMD64 TK TCL OPENGL CUDA;cd src/; make install`安装,将二进制文件路径加入PATH(或者创建连接)

~~~bash
## compiler & essential tools
sudo apt-get install cmake
sudo apt-get install gfortran
sudo apt-get install openjdk-8-jdk openjdk-8-jre
sudo apt-get install git
sudo apt-get install apache2 
sudo apt-get install php
sudo apt-get install libapache2-mod-php7.0 
sudo apt-get install php7.0-mcrypt php7.0-curl
sudo apt-get install csh xorg-dev
sudo apt-get install mysql-server php-mysql php-mbstring php-mysqli
sudo apt-get install openmpi-bin

### openssh for sftp and ssh login (sshd)
sudo apt-get install openssh-server
sudo apt-get install dos2unix

sudo service apache2 restart
sudo /etc/init.d/mysql restart
sudo /etc/init.d/ssh restart

## IDE
#### 不建议使用下面的方法安装eclipse-cdt, 推荐先安装java jdk+jre 8(对应版本)后, 用官网的安装器.
# sudo apt-get install eclipse-cdt
# sudo apt-get install eclipse-pydev

## python relative
sudo apt-get install python-pip
sudo pip install --upgrade pip
sudo pip install numpy scipy ipython jupyter pandas sympy nose
sudo apt-get install pyqt5-dev

sudo pip install virtualenv
sudo pip install requests
sudo pip install beautifulsoup4
sudo pip install pdfminer
sudo apt-get python-mysqldb

### scienctic calculation  
sudo apt-get install libfreetype6-dev
sudo apt-get install pkg-config
sudo pip install matplotlib

## Modelling
sudo apt-get install pymol

### openbabel
sudo apt-get install libjpeg-dev
sudo apt-get install libeigen3-dev
sudo apt-get install python-cairo
sudo pip install pillow
~~~

有些程序运行时报错, 例如缺*libtiff.so.3*, `apt-cache search libtiff`找一下, 发现有一个libtiff5. 那就`apt install libtiff5`. 装好后依然报错. 可以尝试`locate -b libtiff` 查找其库位置(有时需要先`sudo updatedb` 升级才能有locate找到). 例如这个库的32位在/usr/lib/i386-linux-gnu/libtiff.so.5, 64位版本在`/usr/lib/x86_64-linux-gnu/libtiff.so.5`. 找到后`ln -s /usr/lib/x86_64-linux-gnu/libtiff.so.5 /usr/lib/libtiff.so.3`就可以了!


## 用户管理

~~~bash
sudo adduser username
sudo userdel username
sudo vim /etc/sudoers
## add a line in this file :
## User privilege specification
#root ALL=(ALL) ALL
#username ALL=(ALL) ALL
~~~

## 安装rpm包:

~~~bash
# install alien
sudo apt install alien
# convert rpm to deb by alien
sudo alien app.rpm 
dpkg -i app.deb
~~~

## 安装NVIDIA显卡

- 下载好名为 `NVIDIA-Linux-x86_64-****.run`的驱动
- 按shift开机或者直接有系统选择的菜单时选择高级模式(Advanced options for ubuntu)的`Recovery Mode`
- 进去后选`root  Drop to root shell prompt`
- `mount -o remount,rw /` 使得可以读写(原来是只读read-only)
- `vi /etc/modprobe.d/blacklist.conf` 将某些冲突的模块加入黑名单 (见下)
- `apt-get remove --purge nvidia-*; apt-get remove --purge xserver-xorg-video-noveau;` 删除旧的驱动和原生驱动.
- 重启, 重新进入上述的带写权限的root命令行.
- `/etc/init.d/gdm stop`或者`/etc/init.d/lightdm stop` 关闭一个服务
- `./NVIDIA-Linux-x86_64-****.run` 来运行安装, 可能会遇到'the distribution-provided pre-install script failed'不必理会. 一直continue, 如果重装就让他重装, 最后`nvidia-xconfig`要运行就让他运行.
- `/etc/init.d/gdm restart`或者`/etc/init.d/lightdm restart` 重启一个服务,然后重启电脑

~~~
blacklist vga16fb

blacklist nouveau

blacklist rivafb

blacklist nvidiafb

blacklist rivatv

~~~

最后进入了无限登录循环..无法进入桌面.

`CTRL+ALT+F1` 进入命令行后, 输入 `startx`, 弹出:
xf86EnableIOPorts: failed to set IOLP for I/O (Operation not permitted) modprobe: ERROR: could not insert 'nvidia': No such device. Fatal server error: AddScreen/ScreenInit failed for driver 0. Check /home/user/.local/share/xorg/Xorg.1.log

更多可以参考[ubuntu14安装nvidia驱动的方法](http://askubuntu.com/questions/451221/ubuntu-14-04-install-nvidia-driver)去考证上述为啥错了

最后是重新用最简单的方法...就是直接apt安装...如下..在上述错误后执行,依然好使~

~~~bash
sudo apt-get search nvidia-libopencl | grep nvidia-libopencl
sudo apt-get install nvidia-361
~~~

### 设置应用启动快捷方式(启动器)

创建一个`abc.desktop`文件, 放到应用库在`/usr/share/applications`里头, 将相应的desktop文件放到里面去即可. 打开右键打开文件时就可以使用该应用打开

~~~
[Desktop Entry]
Version=1.0
Name=eclipse
Exec=/home/hom/eclipse/eclipse %F
Terminal=false
Icon=/home/hom/eclipse/icon.xpm
Type=Application
Categories=Development
~~~

这里`%F`是打开某个文件, 如果没有可能不会再右键打开菜单列出. 如果应用打不开, 例如需要环境变量, 可以写到`abc.sh`文件里配置好环境变量一类的东西再执行, 传递变量时使用`$@` 传递文件名即可.

### 挂载ISO

~~~bash
sudo mount -o loop ubuntu16.iso /mnt/ubuntu16
#sudo mount -o rw,loop file.iso /mnt/writable
sudo umount /mnt/ubuntu16
~~~

## Bug

在Yoga 900使用Ubuntu 16.04 LTS中, 发现有如下问题:

1. 关屏幕睡眠重新打开后触摸板失控
2. 进入了飞行模式后再退出, wifi失效
3. 功能键F6对应的触摸板控制功能失效.

貌似14.04 LTS会有更多问题, 例如没有驱动要更新kernal..

解决: 

1. 对于触摸板失控:  
	- 最简单方法是触摸屏打开设置->鼠标触摸板->关闭再重新打开触摸板功能
	- `Ctrl+Alt+Fn+F1`进入命令行模式后再`Ctrl+Alt+Fn+F7`返回图形界面模式可以解决这个问题
	- `xinput list` 查看设备(包括pointer和keyboard)可以知道设备对应ID. Pointer是鼠标控制,其中 *SYNA2B29:00 06CB:77C6 id=10*这个是触摸板, *ELAN21EF:00 04F3:21EF id=11*是触屏, 接下来使用`xinput set-prop 10 "Device Enabled" 0; xinput set-prop 10 "Device Enabled" 1;` (等价于`xinput disable 10;xinput enable 10`)来关闭并重新打开触摸板可以解决. 有说用`synclient TouchpadOff=1`再设0的方法, 不sleep测试也可以,但sleep过后这个方法就无效了,推测是不能判断这个设备为触摸板吧.
	- 究竟suspend时会进行何种加载呢? 有帖子说放一个执行脚本在`/etc/pm/sleep.d/`就可以, 但我执行`pm-suspend`时可行,但点击suspend或者关闭盖子时并没有执行..最后基本解决参看我的这个帖子:[Yoga900触摸板在Ubuntu16.04睡眠后无法再识别](/2016/06/09/ubuntu16-suspend-touchpad/)
2. 貌似可以通过`sudo service network-manager restart`解决

------
