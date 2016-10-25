---
layout: post
title: Ubuntu使用小结
date: 2016-09-10 06:21:46
categories: IT
tags: System Ubuntu
---

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


Firefox 的 Java插件问题: 安装icedtea插件: `sudo apt-get install icedtea-plugin`. 或者参考[How to install the Java plugin for Firefox?](http://askubuntu.com/questions/354361/how-to-install-the-java-plugin-for-firefox)来安装oracle的java.

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

添加库: `sudo add-apt-repository ppa:name`再apt update; 移除则编辑 `/etc/apt/sources.list`

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

#### 拨号网络

~~~bash
# open wired connectuib. maybe different name to eth0
sudo ifconfig eth0 up
# Interface to set up network
sudo pppoeconf
# Enter username and password, then Yes * 4 
sudo pon dsl-provider
# To stop connection
sudo poff dsl-provider
# Read log
plog
# Alternative, you can set up by System setting interface.
~~~

去除拨号重新使用直接连接:

~~~bash
## The following line can remove the dsl interface by add # in the interface file
# sudo vi /etc/network/interfaces
# restart the dhcp service
sudo dhclient enp4s0
# restart the network
sudo /etc/init.d/networking restart
~~~

`/etc/network/interfaces`文件内容

~~~
# interfaces(5) file used by ifup(8) and ifdown(8)                              
auto lo
iface lo inet loopback

#auto dsl-provider
#iface dsl-provider inet ppp
#pre-up /bin/ip link set enp4s0 up # line maintained by pppoeconf
#provider dsl-provider

auto enp4s0
iface enp4s0 inet dhcp #manual
~~~

为避免每次重启都要`sudo dhclient enp4s0`, 将网卡iface的manual改为dhcp.

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

#### 安装oh-my-zsh

~~~bash
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
chsh -s /usr/bin/zsh
~~~

退出再登入后起效. 可以把bashrc上的内容重新写到`.shrc` 然后 `.zshrc` 和`.bashrc` 都加载之. 否则直接zshrc加载bashrc会导致因为`complete`和`shopt` zsh不兼容而报错. 

更改别的用户, 可以用`sudo chsh -s /usr/bin/zsh username` 或者`sudo usermod -s /usr/bin/zsh username` 也可. 其实质是修改了`/etc/passwd` 文件里用户对应信息. 如果要查询可用sh, 可以`cat /etc/shells`. 查看当前shell`echo $SHELL`

#### 设置命令行提示有颜色:

编辑.bashrc, 取消注释: `force_color_prompt=yes` 一行

搜索-单行列出

`apt-cache search freetype | grep dev`

搜索-多行列出

`apt search freetype`

## 安装东东

可以使用官方的应用商店安装:

- Ubuntu Software Center : 另一个软件中心, 有更多软件选择
- Tweak Tool : 可以修改系统一些参数, 例如桌面显示home, 电源键响应等.
- FileZilla : FTP的软件罗
- 7zip: 压缩文件软件咯
- Ubuntu restricted extras : 一些常用软件依赖, 包括mp3支持啊, flash啊, codecs啊
- SMPlayer : 媒体播放软件
- ClassicMenu Indicator : 可以在菜单添加一个老式linux的所有应用的菜单栏
- Screenshot : 自带简介的截屏工具, 也可以用高级点的Shutter
- konsole : 多tab的命令行. 不过有点丑. 发现自带的Terminal可以设置新窗口为Tab, 所以就不用konsole了
- wine: window模拟器, 命令行`wine win_file`即可运行, `wine uninstaller`可以打开卸载器. c盘在`~/.wine/drive_c/`

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

如果遇到`sh: Syntax error: Bad fd number` 这个提示, 解决方法是`sudo mv /bin/sh /bin/sh.bak; sudo ln -s /bin/bash /bin/sh`, 这是由于脚本没写好而使用了bash语法造成的.

## 安装应用

需要下载的东东:

- [eclipse官方安装器](https://eclipse.org/downloads/) 其中[Linux版64位](https://www.eclipse.org/downloads/download.php?file=/oomph/epp/mars/R2/eclipse-inst-linux64.tar.gz): 下载后解压, 然后双击里面的`eclipse-inst`按着提示搞就是了. 需要系统有java支持.
- [Sublime text](https://www.sublimetext.com/3): 这个不用说了, 安装使用`dpkg -i abc.deb` 就可以了. [rockdrigo的gist](https://gist.github.com/rockdrigo/9ae723dc5bdaf1f49288)你懂.安装后的中文输入问题参考[ubuntu中使用sublime问题-中文输入和中英文不对齐](/2016/08/22/sublime-ubuntu), 中键问题参考[Linux系统sublime的中键选择和重映射鼠标键](/2016/08/26/sublime-linux-middle-button)
- [Chimera](https://www.cgl.ucsf.edu/chimera/download.html), Linux64位下载(bin文件), `chmod +x chimera.bin` 后
命令行运行即可. 如要安装到非home目录记得sudo.
- [Foxit Reader](https://www.foxitsoftware.com/downloads/) 下载免费的Linux 64位版本, 解压后得一个run文件直接运行安装即可. 安装后把安装文件夹的`Foxit Reader.desktop`复制到`/usr/share/applications`, pdf右键在所有应用中就可以找到foxit. Foxit优点是可以高亮和注释, 而默认pdf阅读器是不行的(但默认阅读器感觉更快一些)
- [TexMacs](http://www.texmacs.org/tmweb/download/unix.en.html) : Write latex as you see.
- [VMD](http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD) : 下载(我下的是LINUX_64 CUDA)后修改configure文件内两个目录(一个二进制文件所在,一个库所在(各种脚本)),然后`./configure LINUXAMD64 TK TCL OPENGL CUDA;cd src/; make install`安装,将二进制文件路径加入PATH(或者创建连接)
- MATLAB: 可能安装新版会有bug,参看[ubuntu16 安装matlab问题](/2016/08/21/matlab-ubuntu16)
- [网易云音乐](http://music.163.com/#/download): 不解释, 区分Ubuntu16和14不同deb版本
- [WPS](http://wps-community.org/download.html): 下载后dpkg一下就好了.打开会报错字体问题,下载这个[字体库](https://pan.baidu.com/s/1geF6dtp)再dpkg一下(来自[linuxidc.com](http://www.linuxidc.com/Linux/2013-06/85374.htm))
- [Chrome](http://www.google.cn/intl/zh-CN/chrome/browser/thankyou.html?platform=linux): 不解释.
- [dropbox](https://www.dropbox.com/install?os=lnx): 下载deb安装后, `cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -` 下载一个包解压到用户目录(如果网络不通,另外下载后再解压到用户目录也行,解压后是`.dropbox-dist`文件夹). 运行`~/.dropbox-dist/dropboxd` 执行底层背景程序. 然后再在应用中心打开dropbox. 国内的话打开后要在右上角dropbox图标右键后进去设置代理端口
- [百度云](https://yun.baidu.com/): 使用[bcloud](https://github.com/platinhom/bcloud-packages)来实现. 可以在ubuntu软件中心安装, 也可以安装pip3以后再安装. [图文介绍](http://www.mintos.org/skill/baidu-bcloud-linux.html). 如果打开后登陆有问题, 参看[Network error after login](https://github.com/LiuLang/bcloud/issues/244). 缺点是并不能同步啊..
- [DoubleCMD](https://sourceforge.net/p/doublecmd/wiki/Download/): 类似于total commander的软件.

~~~bash
## compiler & essential tools
sudo apt-get install cmake
sudo apt-get install gfortran
sudo apt-get install openjdk-8-jdk openjdk-8-jre
sudo apt-get install git
sudo apt-get install subversion
sudo apt-get install apache2 
sudo apt-get install php
sudo apt-get install libapache2-mod-php7.0 
sudo apt-get install php7.0-mcrypt php7.0-curl
sudo apt-get install csh xorg-dev
sudo apt-get install mysql-server php-mysql php-mbstring php-mysqli
sudo apt-get install openmpi-bin
~~~

安装pip3来安装bcloud

~~~bash
sudo apt-get install python3-dev python3-setuptools
sudo easy_install3 pip
sudo pip3 install --upgrade pycrypto
sudo pip3 install --upgrade keyring
# The following may change! Goto the repository to find bcloud_{version}_all.deb
wget https://github.com/LiuLang/bcloud-packages/raw/master/bcloud_3.8.2-1_all.deb
sudo dpkg -i bcloud_3.8.2-1_all.deb
sudo apt-get install -f
bcloud-gui

## Patch for the network err bug mentioned in https://github.com/LiuLang/bcloud/issues/244
cd /usr/lib/python3/dist-packages/bcloud
sudo echo "*** auth.py 2016-01-02 15:47:21.000000000 +0800
--- auth_new.py 2016-06-17 17:39:16.057669144 +0800
***************
*** 289,294 ****
--- 289,295 ----
      '''
      url = const.PAN_REFERER
      req = net.urlopen(url, headers={'Cookie': cookie.header_output()})
+     cookie.load_list(req.headers.get_all('Set-Cookie')) # SCRC
      if req:
          return parse_bdstoken(req.data.decode())
      else:" > auth.patch

sudo echo "*** pcs.py  2016-01-02 15:47:21.000000000 +0800
--- pcs_new.py  2016-06-17 17:38:52.909669250 +0800
***************
*** 542,548 ****
      ])
      req = net.urlopen(url, headers={
          'Content-type': const.CONTENT_FORM_UTF8,
!         'Cookie': cookie.sub_output('BAIDUID', 'BDUSS', 'PANWEB', 'cflag'),
      })
      if req:
          content = req.data
--- 542,548 ----
      ])
      req = net.urlopen(url, headers={
          'Content-type': const.CONTENT_FORM_UTF8,
!         'Cookie': cookie.sub_output('BAIDUID', 'BDUSS', 'PANWEB', 'cflag','SCRC','STOKEN'),
      })
      if req:
          content = req.data
***************
*** 717,723 ****
      dlink = metas['info'][0]['dlink']
      url = '{0}&cflg={1}'.format(dlink, cookie.get('cflag').value)
      req = net.urlopen_without_redirect(url, headers={
!         'Cookie': cookie.sub_output('BAIDUID', 'BDUSS', 'cflag'),
          'Accept': const.ACCEPT_HTML,
      })
      if not req:
--- 717,723 ----
      dlink = metas['info'][0]['dlink']
      url = '{0}&cflg={1}'.format(dlink, cookie.get('cflag').value)
      req = net.urlopen_without_redirect(url, headers={
!         'Cookie': cookie.sub_output('BAIDUID', 'BDUSS', 'cflag','SCRC','STOKEN'),
          'Accept': const.ACCEPT_HTML,
      })
      if not req:
***************
*** 907,913 ****
          data = ('dlink=0&target=' +
                  encoder.encode_uri_component(json.dumps(filelist)))
      req = net.urlopen(url, headers={
!         'Cookie': cookie.sub_output('BDUSS'),
          'Content-type': const.CONTENT_FORM,
          }, data=data.encode())
      if req:
--- 907,913 ----
          data = ('dlink=0&target=' +
                  encoder.encode_uri_component(json.dumps(filelist)))
      req = net.urlopen(url, headers={
!         'Cookie': cookie.sub_output('BDUSS','SCRC','STOKEN'),
          'Content-type': const.CONTENT_FORM,
          }, data=data.encode())
      if req:" > pcs.patch

# backup auth.py and pcs.py
sudo cp auth.py auth.py.bak
sudo cp pcs.py pcs.py.bak
# patch the files
sudo patch auth.py < auth.patch
sudo patch pcs.py < pcs.patch
# delete the previous account setup
rm -rf ~/.config/bcloud
~~~

解决WPS的word不能输入中文的问题(同理,ppt和excel是修改`wpp`和`et`文件加入以下两句):

编辑`/usr/bin/wps`, 加入以下两句:

~~~bash
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE="fcitx"
~~~

### openssh for sftp and ssh login (sshd)

~~~bash
sudo apt-get install openssh-server
sudo apt-get install dos2unix

sudo service apache2 restart
sudo /etc/init.d/mysql restart
sudo /etc/init.d/ssh restart
~~~

#### Github Pages/Jekyll

~~~bash
sudo gem install bundler
#### For error: mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.h
sudo apt-get install ruby2.3-dev
sudo gem install github-pages
~~~

## IDE
#### 不建议使用下面的方法安装eclipse-cdt, 推荐先安装java jdk+jre 8(对应版本)后, 用官网的安装器.

~~~bash
# sudo apt-get install eclipse-cdt
# sudo apt-get install eclipse-pydev
~~~

## python relative

~~~bash
sudo apt-get install idle idle3
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
sudo apt-get install libtiff-dev
sudo apt-get install libeigen3-dev
sudo apt-get install python-cairo
sudo pip install pillow
~~~

有些程序运行时报错, 例如缺*libtiff.so.3*, `apt-cache search libtiff`找一下, 发现有一个libtiff5. 那就`apt install libtiff5`. 装好后依然报错. 可以尝试`locate -b libtiff` 查找其库位置(有时需要先`sudo updatedb` 升级才能有locate找到). 例如这个库的32位在/usr/lib/i386-linux-gnu/libtiff.so.5, 64位版本在`/usr/lib/x86_64-linux-gnu/libtiff.so.5`. 找到后`ln -s /usr/lib/x86_64-linux-gnu/libtiff.so.5 /usr/lib/libtiff.so.3`就可以了!

## 计算化学/生物学

~~~bash
##### VMD 
##sudo apt-get install rlwrap ##?startup rlwrap command not found?

##### Modeller
# Download from http://salilab.org/modeller/download_installation.html
sudo env KEY_MODELLER=MODELIRANJE dpkg -i modeller_9.17-1_amd64.deb
mod9.17 ## Modeller installed at /usr/lib/modeller9.17/
# Documentation :  http://salilab.org/modeller/tutorial/
# Online server: https://toolkit.tuebingen.mpg.de/modeller

##### NAMD
# goto http://www.ks.uiuc.edu/Development/Download/download.cgi to download suitable version 
tar -xzf NAMD*.tar.gz

##### GROMACS
## Download from http://www.gromacs.org/Downloads. Install guide: http://www.gromacs.org/Documentation/Installation_Instructions_5.0
#wget ftp://ftp.gromacs.org/pub/gromacs/gromacs-5.1.3.tar.gz
tar -xzf gromacs-5.1.3.tar.gz
mkdir gromacs-5.1.3/build
cd gromacs-5.1.3/build
cmake .. -DREGRESSIONTEST_DOWNLOAD=ON -DGMX_BUILD_OWN_FFTW=ON -DCMAKE_INSTALL_PREFIX=~/Softwares/gromacs513 -DGMX_MPI=on -DGMX_GPU=on
make
make check
sudo make install
source ~/Softwares/gromacs513/bin/GMXRC

##### OpenBabel
sudo pip install pillow
sudo apt install swig libwxgtk3.0-dev python-wxgtk3.0-dev
git clone https://github.com/openbabel/openbabel.git
cmake ../ -DBUILD_GUI=ON -DPYTHON_BINDINGS=ON -DRUN_SWIG=ON -DCMAKE_INSTALL_PREFIX=~/Softwares/OpenBabel
# Assign 4 cores
make -j4
make test
sudo make install
# If use -DCMAKE_INSTALL_PREFIX, assign the runtime enviroment
echo '#### OpenBabel
export PATH="$PATH:~/Softwares/OpenBabel/bin"
export PYTHONPATH="$PYTHONPATH:~/Softwares/OpenBabel/lib/python2.7:~/Softwares/OpenBabel/lib/python2.7/site-packages"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:~/Softwares/OpenBabel/lib"
export C_INCLUDE_PATH="$C_INCLUDE_PATH:~/Softwares/OpenBabel/include"
export BABEL_DATADIR="~/Softwares/OpenBabel/share/openbabel/2.3.90"
export BABEL_LIBDIR="~/Softwares/OpenBabel/lib/openbabel/2.3.90"
' >> ~/.bashrc
# In Ubuntu test, pass normally and don't need to modify PIL problem.
~~~

安装AMBER参考[在新的ubuntu虚拟服务器建立服务器](/2016/07/12/install-weiserver)

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

创建一个`abc.desktop`文件, 放到应用库在`/usr/share/applications`里头(也可能在`~/.local/share/applications`里头), 将相应的desktop文件放到里面去即可. 打开右键打开文件时就可以使用该应用打开

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

这里`%F`是打开某个文件, 如果没有可能不会在右键打开菜单列出. 如果应用打不开, 例如需要环境变量, 可以写到`abc.sh`文件里配置好环境变量一类的东西再执行, 传递变量时使用`$@` 传递文件名即可.

### 删除左侧文件夹快捷方式:Music, Pictures, Videos等

参考[How to remove bookmarks from the Nautilus sidebar?](http://askubuntu.com/questions/79150/how-to-remove-bookmarks-from-the-nautilus-sidebar)

~~~bash
vi ~/.config/user-dirs.dirs
# comment the Not use DIR
#XDG_VIDEOS_DIR="$HOME/Videos"

# Stop retrieve to predefine setting:
echo "enabled=false" > ~/.config/user-dirs.conf
~~~

> PS: 主要不要取消Templates! 下面会提到!

#### 右键菜单新建项和新建文件添加新内容

- 要新建某类型文件, 十分简单, 比window还简单. 只要将作为模板的文件放入用户目录里的`Templates`目录即可! 名字就是你放进去的文件的名字哦!~ 如果之前关掉了, 那么要这个功能就哟重新编辑`~/.config/user-dirs.dirs` 并重新登陆
- 右键新建项: 可以安装一个`nautilus-actions` 程序然后运行`nautilus-actions-config-tool`. 进去后新建一个action, 然后绑定好command就好啦~

### 挂载ISO

~~~bash
sudo mount -o loop ubuntu16.iso /mnt/ubuntu16
#sudo mount -o rw,loop file.iso /mnt/writable
sudo umount /mnt/ubuntu16
~~~

### vim/gedit 中文乱码

乱码主要由于GBK编码不识别带照顾, 首先系统增加中文字符编码

~~~bash
sudo vim /var/lib/locales/supported.d/local
#添加下面的中文字符集

zh_CN.GBK GBK
zh_CN.GB2312 GB2312
zh_CN.GB18030 GB18030

#使其生效：
sudo dpkg-reconfigure locales
~~~

##### 使vim支持中文:

~~~bash
# 打开vim的配置文件，位置在/etc/vim/vimrc , 在其中加入
sudo vi /etc/vim/vimrc
set fileencodings=utf-8,gb2312,gbk,gb18030
set termencoding=utf-8
set encoding=prc

# 保存退出 :wq
# 加载设置, 其实可以不加
source /etc/vim/vimrc
~~~

##### 使gedit 3*支持中文
适用于Ubuntu 16的gedit 3.*

~~~bash
# 安装dconf-editor, 配置编辑器
sudo apt install dconf-editor
dconf-editor
# 展开org/gnome/gedit/preferences/encodings
# candidate-encodings 这项默认是[''], 根据国家语言来定, 我们修改他的值
# ['UTF-8','GB18030','GB2312','GBK','BIG5','CURRENT','UTF-16']

## 如果不想用图形化管理器, 使用以下命令
gsettings set org.gnome.gedit.preferences.encodings candidate-encodings "['UTF-8','GB18030','GB2312','GBK','BIG5','CURRENT','UTF-16']"
~~~

对于一些版本, 可能不是candidate-encodings, 可能是`auto-detected`.相应修改其值(所以最好用dconf-editor, 否则不知道键名)

##### 取消alt+中键的改变窗口大小功能

这个功能会和一些分子模拟可视化软件冲突, 因此要取消掉. 这个功能也可以通过alt+F8来实现

方法一: 安装 `compizconfig-settings-manager` 然后在应用中心打开, 随后在Window Managerment -> Resize Window设置
方法二: 安装`dconf-editor`然后在org->gnome->desktop->wm->preference里面设置`resize-with-right-button` 或者修改配合键Alt为`<Super>`

或者命令行:

~~~bash
#!/bin/bash
#  兼顾gnome 和新unity
gconftool-2 -s -t bool /apps/metacity/general/resize_with_right_button true
gsettings set org.gnome.desktop.wm.preferences resize-with-right-button true
~~~

### 设置开机启动服务

利用图形界面`sysv-rc-conf`或者使用`service`命令

#### 安装程序出现服务loop

`sudo apt install xxxx` 时出现报错, 上面还有些信息如

> insserv: warning: script 'service_name' missing LSB tags and overrides
> insserv: There is a loop at service plymouth if started

`sudo vi /etc/init.d/service_name` 在开头`#!/bin/sh`后加入以下类似内容 ([参考贴](http://unix.stackexchange.com/questions/289667/unable-to-install-anything-using-apt-get-because-of-insserv)):

~~~bash
### BEGIN INIT INFO
# Provides :          service_name
# Required-Start :
# Required-Stop :
# Default-Start :     2 3 4 5
# Default-Stop  :     0 1 6
# Short-Description : Some info
# Description :       Some more info
### END INIT INFO
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
