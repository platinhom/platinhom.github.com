---
layout: post
title: Yoga900触摸板在Ubuntu16.04睡眠后无法再识别
date: 2016-06-08 16:53:09
categories: IT
tags: System
---

# Touchpad doesn't work after suspend in Ubuntu 16.04 for Yoga900

发现Yoga900每次关闭盖子后再打开触摸板都失控, 需要使用触屏来操作. 探索了一天终于找到一个可用的解决方法了. 貌似网上没有正式的解法, 或者等ubuntu更新吧.

## 1. Know you Touchpad ID

Run `xinput list` to find the device for pointer and keyboard. We only pay attention to the *Virtual core pointer* part. 

~~~
hom@Yoga900:~$ xinput list
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ ELAN21EF:00 04F3:21EF                   	id=11	[slave  pointer  (2)]
⎜   ↳ SYNA2B29:00 06CB:77C6                   	id=10	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Power Button                            	id=6	[slave  keyboard (3)]
    ↳ Video Bus                               	id=7	[slave  keyboard (3)]
    ↳ Power Button                            	id=8	[slave  keyboard (3)]
    ↳ Lenovo EasyCamera                       	id=9	[slave  keyboard (3)]
    ↳ Ideapad extra buttons                   	id=12	[slave  keyboard (3)]
    ↳ AT Translated Set 2 keyboard            	id=13	[slave  keyboard (3)]
~~~

Here, the ELAN device is the touchscreen and SYNA device is the touchpad for my Yoga900. The ID for touchpad is **10** here.

To make sure the unknown name for your device, you can try `xinput disable ID` to disable and then test it. Then `xinput enable ID` to recover it. 

> The id may be catch by command `` tp_id=`xinput list | grep -i touchpad | awk '{ print $5 }' | sed 's/id=//'` `` (Here SYNA instead of "touchpad"). If the device id will change, the following device id can be replaced by `` `xinput list | grep -i touchpad | awk '{ print $5 }' | sed 's/id=//'` ``

## 2. Create a executable script to reset touchpad after resume from suspend 

This step to fix the problem when using `pm-suspend` command to suspend. Indeed, when computer pm suspend/resume, it will run the commands in the `case` part. 

`xinput disable diviceID; xinput enable diviceID` is the command to restart the device. Other commands as: 

- `xinput set-prop 10 "Device Enabled" 0; xinput set-prop 10 "Device Enabled" 1` is the same. the device ID can also be the name as "SynPS/2 Synaptics Touchpad". This method can also set other properties!~
- `sudo synclient TouchpadOff=1; sudo synclient TouchpadOff=0;` can restart when normally in ubuntu, but failed when resume from suspend.
- Some places say: `modprobe -r psmouse; modprobe psmouse;`. Or using `rmmod` instead `modprobe -r`. I tried, but nothing happen... 


To create a script (The name can as you like~) at *pm-sleep.d* folder: 

`sudo gedit /etc/pm/sleep.d/99_touchpad`

Contents for `/etc/pm/sleep.d/99_touchpad` (**Change the user name 'hom' to your user name! Also device id 10 here!**):

~~~bash
#! /bin/bash

case $1 in
	# For suspend action
     suspend|suspend_hybrid|hibernate)
        DISPLAY=:0.0 su hom -c 'xinput disable 10'
        ;;
    # For resume action
     resume|thaw)
        DISPLAY=:0.0 su hom -c 'xinput list'
        DISPLAY=:0.0 su hom -c 'xinput disable 10'
        DISPLAY=:0.0 su hom -c 'xinput enable 10'
        ;;
esac
~~~

Become executable: `sudo chmod +x /etc/pm/sleep.d/99_touchpad`

> Notice: to generate this script at `/etc/pm/sleep.d/` folder can help to fix the same problem when run `pm-suspend` command. If you done above step, try to run `pm-suspend` to suspend your computer and then resume it. Can it work? No? Further check what's wrong..

## Use systemd service to hook for suspend

Generate the service configuration file as follow: 

`/etc/systemd/system/touchpad-resume.service` : 

~~~
[Unit]
Description=Local system resume actions for touchpad
After=suspend.target

[Service]
Type=simple
ExecStart=-/etc/pm/sleep.d/99_touchpad resume

[Install]
WantedBy=suspend.target
~~~

And then run `sudo systemctl enable root-resume.service` to enable the service, which will automatically generate `/etc/systemd/system/suspend.target.wants/touchpad-resume.service` file.

OK, now try to restart and close the lid~

> Maybe sometimes will fail and resolution will change to too high.. At that time, try:  
- press `Ctrl+Alt+F1` then `Ctrl+Alt+F7` to reload the X window.
- Or press `xinput disable 10; xinput enable 10` to restart it in command line. (Change to your device ID)
- Or use graphic system setup~

## 附录: 尝试 The tries..

1. [Touchpad doesn't work after suspend](http://ubuntuforums.org/showthread.php?t=2182922) 这篇介绍了使用/etc/pm/sleep.d/新建脚本处理的方法, 但测试并不行, 上面提到了, Ubuntu16并不是使用pm-suspend来睡眠的,而是systemd处理. 使用该方法后, 再用`pm-suspend`睡眠, 再恢复时是有效的. 但重开盖子或者在总菜单里点suspend按钮睡眠恢复都无效.
2. [Laptop does not suspend when lid is closed](http://askubuntu.com/questions/395428/laptop-does-not-suspend-when-lid-is-closed): 这篇文章介绍使用`acpi`监控设备服务来监控设备关闭就执行`pm-suspend`. 经测试也无效, 出现现象是, 关闭盖子恢复后还会再执行一次suspend. 而两次都没有恢复触摸板. 所以我开始怀疑, ubuntu16使用另外的服务来监控和执行另一个suspend. 这篇文章也提到了修改`/etc/systemd/logind.conf` 可以[更改关闭盖子时的行为](http://ubuntuhandbook.org/index.php/2016/05/ubuntu-16-04-shutdown-hibernate-your-laptop-lid-closed/)(例如休眠或者关机). 其实就执行最后一个先创建`/etc/acpi/events/lidbtn`来设置监控盖子的服务, 然后执行相应脚本`/etc/acpi/lidbtn.sh` 就可以了, 脚本内容可以按照他grep设备状态的写法. `/etc/acpi/`里面的是监控设备的脚本, `/proc/acpi/button/lid/LID0/state`是设备(这里是盖)的状态.
3. [Ubuntu 15.04 Suspend doesn't run `pm-suspend`](http://askubuntu.com/questions/620494/ubuntu-15-04-suspend-doesnt-run-pm-suspend) 最后关键就是要找到Ubuntu16究竟是用什么运行suspend, 直到看到这篇帖子的方法. 实际上Ubuntu15/16 使用`systemd`而不是`upstart`来执行suspend动作, 而其并不执行pm-utils. 所以上一次的测试失败了. 据此写了第三步.
4. [how to execute a command after resume from suspend?](http://askubuntu.com/questions/92218/how-to-execute-a-command-after-resume-from-suspend): 这篇帖子介绍将脚本放在`/lib/systemd/system-sleep/`来执行, 经测试无效.

- [Understanding Suspend by ACPI ](https://wiki.ubuntu.com/UnderstandingSuspend): 官方wiki关于电源管理
- [pm-action](http://manpages.ubuntu.com/manpages/precise/man8/pm-action.8.html)

------
