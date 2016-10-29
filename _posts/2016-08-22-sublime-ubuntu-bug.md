---
layout: post
title: ubuntu中使用sublime问题-中文输入和中英文不对齐
date: 2016-08-21 18:28:47
categories: IT
tags: IDE Ubuntu
---

## Sublime利用Fcitx输入中文

> 注意这是针对Fcitx的方法, 针对IBus是不行的(经测试). Ibus可以去搜一个叫[InputHelper](https://github.com/xgenvn/InputHelper)来尝试..

最简单自动化方法是使用[lyfeyaj的git库](https://github.com/lyfeyaj/sublime-text-imfix)自动处理:

~~~bash
git clone https://github.com/lyfeyaj/sublime-text-imfix.git
cd sublime-text-imfix && ./sublime-imfix
~~~

自己一步一步正常解决方法:

#### 编写一个`sublime_imfix.c`文件(内容如下): 

~~~cpp
#include <gtk/gtkimcontext.h>

void gtk_im_context_set_client_window (GtkIMContext *context,
         GdkWindow  *window)
{
 GtkIMContextClass *klass;
 g_return_if_fail (GTK_IS_IM_CONTEXT (context));
 klass = GTK_IM_CONTEXT_GET_CLASS (context);

 if (klass->set_client_window)
   klass->set_client_window (context, window);

 g_object_set_data(G_OBJECT(context),"window",window);

 if(!GDK_IS_WINDOW (window))
   return;

 int width = gdk_window_get_width(window);
 int height = gdk_window_get_height(window);

 if(width != 0 && height !=0)
   gtk_im_context_focus_in(context);
}
~~~

> 还有个很长的版本参考[完美解决 Linux 下 Sublime Text 中文输入](http://my.oschina.net/tsl0922/blog/113495). 测试均可使用

#### 编译`libsublime-imfix.so`

~~~bash
sudo apt install gtk+-2.0
gcc -shared -o libsublime-imfix.so sublime_imfix.c  `pkg-config --libs --cflags gtk+-2.0` -fPIC
~~~

#### 复制库文件到sublime, 并将库提前加载

~~~bash
sudo mv libsublime-imfix.so /opt/sublime_text/
sudo echo '#!/bin/sh
LD_PRELOAD=/opt/sublime_text/libsublime-imfix.so
exec /opt/sublime_text/sublime_text "$@"' > /usr/bin/subl
~~~

#### 修改桌面打开时没有加载的问题

就是修改`/usr/share/applications/sublime_text.desktop`的内容. 这里使用env命令来执行加载我们编译的库,也可以用 `bash -c "commands..."`方式来处理.

~~~bash
sudo echo '[Desktop Entry]
Version=1.0
Type=Application
Name=Sublime Text
GenericName=Text Editor
Comment=Sophisticated text editor for code, markup and prose
#Exec=/opt/sublime_text/sublime_text %F
Exec=env LD_PRELOAD=/opt/sublime_text/libsublime-imfix.so /opt/sublime_text/sublime_text %F                                                 
Terminal=false
MimeType=text/plain;
Icon=sublime-text
Categories=TextEditor;Development;
StartupNotify=true
Actions=Window;Document;

[Desktop Action Window]
Name=New Window
#Exec=/opt/sublime_text/sublime_text -n
Exec=env LD_PRELOAD=/opt/sublime_text/libsublime-imfix.so /opt/sublime_text/sublime_text -n
OnlyShowIn=Unity;

[Desktop Action Document]
Name=New File
#Exec=/opt/sublime_text/sublime_text --command new_file
Exec=env LD_PRELOAD=/opt/sublime_text/libsublime-imfix.so /opt/sublime_text/sublime_text --command new_file
OnlyShowIn=Unity;' > /usr/share/applications/sublime_text.desktop

echo '[Desktop Entry]                                                                 
Encoding=UTF-8
Version=1.0
Type=Application
Name=Sublime Text 3
Icon=sublime_text.png
Path=/
#Exec=/opt/sublime_text/sublime_text
Exec=subl %F
StartupNotify=false
StartupWMClass=Sublime_text
OnlyShowIn=Unity;
X-UnityGenerated=true' > ~/.local/share/applications/sublime_text.desktop
~~~

> 如果在打开菜单右键选项或者Dash里打开不支持中文,那就要相应编辑`~/.local/share/applications/sublime_text.desktop`

## 中英文字体不对其

用sublime默认打开含有中英文的文件编辑时,中英文并不对齐,如下图所示:

![](/other/pic/blog-tmp/sublime-font.png)

解决办法:

1. 菜单 Preference->Settings->User 打开用户配置文件`Preferences.sublime-settings` (中文版是【首选项】→【设置--用户】)
2. 在里面添加`"font_face":"微软雅黑",`这里使用微软雅黑可以解决问题.然后Ctrll+S保存即可(默认字体Consolas). 

可以探索别的字体. "Courier New bold" 中的bold是粗体. Consolas是微软为程序狗设置的字体,但不支持中文. YaHei Consolas Hybrid是整合了雅黑字体的,效果比微软雅黑好点.安装如下: 

~~~bash
git clone https://github.com/cypro666/yahei.consolas-font.git
cd yahei.consolas-font
./install.sh
~~~

以上是使用一个git库简化安装,含有1.12版本.其中install.sh包含内容见下:

~~~bash
#!/bin/bash
sudo mkdir /usr/share/fonts/consolas
sudo cp ./*.ttf /usr/share/fonts/consolas
cd /usr/share/fonts/consolas
sudo chmod 644 *.ttf
sudo mkfontdir
sudo mkfontscale
sudo fc-cache -fv
sudo fc-list|grep "YaHei Consolas Hybrid"
echo "install finished"
~~~

> 依旧存在着字不跟随光标的问题, 而[IMESupport](https://github.com/chikatoike/IMESupport)只支持Win啊..

------
