---
layout: post
title: 新电脑新系统-Win10+Ubuntu
date: 2016-05-31 23:26:46
categories: IT
tags: Ubuntu System
---

好久好久没有写blog了, 好像失踪si了一样. 忙着找工作啊, 结掉米国这边的东东. 

新买了一台Lenovo的Yoga 900, 看起来很酷, Bestbuy Open Box退伍军人节再打9折,900刀含税. Win10系统, 256GB硬盘, 有点少.. 用来日常办公吧. 不过和MBP有点冲突...

自带Win10系统, 打算装双系统, 就是日常办公调试, 可能也够用吧.

安装office 2013的话需要去找一个[microsoft KMS toolkit](http://forums.mydigitallife.info/threads/28669-Microsoft-Toolkit-Official-KMS-Solution-for-Microsoft-Products),这个据说是最早的发布网站.

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

## Win10 安装子系统 WSL

Win10可以安装自身内嵌的Ubuntu了(`WSL`, Windows Subsystem for Linux)! 搞法如下:

- 更新Win10系统到最新(右下角 全部设置, **更新和安全** -> 系统)
- 设置 -> 更新和安全 -> 针对开发人员 -> **开发人员模式**. 然后会下载开发人员模式包 (Developer Mode Package). 下载失败也没关系.
- 控制面板 -> 程序和功能 -> 启用或关闭Window功能 -> 选上 **适用于Linux的Window子系统** , 然后确认就好了
- 重启, 然后进去后 `win+R` 来运行cmd, 输入`bash`来运行. 或者直接在搜索里找ubuntu或者bash (可以创建一个快捷方式)
- `lsb_release -a` 可以知道ubuntu的版本
- 更新完系统发现C盘被占了很多空间, 在C盘发现有`Windows.old` 文件夹占了很大空间, 这个是为了让你可以恢复之前系统留下的. 解决办法: C盘右键后, 在**常规**或者**工具**里找到磁盘清理, 然后点左下角 **清理系统文件**, 可以找到旧系统的垃圾. 不想要就都清了吧 (传递优化文件删不掉..不知道为啥).
- 内嵌ubuntu和win的文件系统怎么分呢? window的文件在ubuntu里是在`/mnt/c/` 来表达NTFS里的C盘, 而 ubuntu系统文件则是在`C:\Users\Yourname\AppData\Local\lxss\rootfs` 里面(lxss文件夹系统文件式隐藏), 我这里的ubuntu的 `home, root, mnt, temp` 不是放在rootfs 而是同等级的, rootfs里的相应文件夹为空(即这些文件夹为单独分区处理). 注意在ubuntu里并不能通过上述路径(rootfs)来访问自身文件系统的. 可以创建相应的`C:\Users\Yourname\AppData\Local\lxss`文件夹到桌面快捷方式.
- ubuntu和win里的执行文件并不互通!!切记! 不能像mingw那样直接在命令行里执行exe文件. 
- 如果要移除WSL, 可以在cmd命令行使用`lxrun /uninstall`, 这样不会移除root和home文件夹, `lxrun /uninstall /full`, 再安装可以`lxrun /install`. 上述卸载方式并不会卸载bash, 只是卸载ubuntu系统. 要卸载bash, 请参看第三条, 取消 **适用于Linux的Window子系统**

WSL 还是有很多问题的, 有很多东西并不能很好安装(例如要创建假网卡的n2n), 先玩玩咯.

### Win 10 WSL 的X server问题

WSL 是不支持 X server的. 但是呢, 可以在win10里面安装另外的Xserver来接上WSL的x需求. 推荐使用[vcXsrv](https://sourceforge.net/projects/vcxsrv/)或者[Xming](https://sourceforge.net/projects/xming/?source=recommended), 也可以使用[cygwin-x](http://x.cygwin.com/). 安装完毕, 打开X server相关的就好了.

安装好后, 尝试安装几个东东: gedit(文本编辑器), nautilus (文件管理器), unity (就是打开程序那个面板罗), ubuntu-desktop (就是桌面咯). 后面三个就不太建议安装了, 比较大, 而且要桌面干嘛?! 而且不稳定 会有些问题, 等以后更好的版本发布了再折腾吧

~~~bash
sudo apt-get install gedit
gedit myfile

###### Maybe some errors, record as follow
## error: XDG_RUNTIME_DIR not set in the environment.
export DISPLAY=localhost:0
echo "export DISPLAY=locahost:0" >> ~/.bashrc

## failed to commit changes to dconf: Failed to execute child process "dbus-launch" (No such file or directory)
sudo apt-get install --reinstall dbus dbus-x11

## dconf-WARNING **: failed to commit changes to dconf: Error sending credentials: Error sending message: Invalid argument
## dbus uses unix sockets to communication, which windows bash at the moment doesn't support. So we just need to tell it to use tcp. In /etc/dbus-1/session.conf, you need to replace <listen>unix:tmpdir=/tmp</listen> with <listen>tcp:host=localhost,port=0</listen> and then you are done
sudo sed -i 's$<listen>.*</listen>$<listen>tcp:host=localhost,port=0</listen>$' /etc/dbus-1/session.conf

## If you want to install GUI
sudo apt-get install nautilus unity compizconfig-settings-manager
## Setup ccsm like: https://github.com/microsoft/bashonwindows/issues/637
compiz
~~~

----------

附虚拟桌面快捷键：

- 贴靠窗口：Win +左/右> Win +上/下>窗口可以变为1/4大小放置在屏幕4个角落
- 切换窗口：Alt + Tab（不是新的，但任务切换界面改进）
- 任务视图：Win + Tab（松开键盘界面不会消失）
- 创建新的虚拟桌面：Win + Ctrl + D
- 关闭当前虚拟桌面：Win + Ctrl + F4
- 切换虚拟桌面：Win + Ctrl +左/右
- 最大化/恢复/最小化: ctrl + win + up / ctrl + win + down / ctrl + win + down down


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



------
