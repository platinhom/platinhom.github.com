---
layout: post
title: Jsmol全屏
date: 2015-07-30 21:41:01
categories: CompCB
tags: CompBiol Visualize
---

JMol/JSmol fullscreen
-----

Jmol 全屏功能默认是没有的. 但可以想办法实现.  
首先要知道jmol的窗口究竟是什么构成的.假设窗口对象id叫 *jmolApplet0* .  

那么一个jmol窗口实际等于:

~~~html
<div id="jmolApplet0_appletinfotablediv" style="position:relative;....">
<div id="jmolApplet0_appletdiv" style="z-index:9001;position:absolute;display:block;....">
<canvas id="jmolApplet0_canvas2d" style="z-index:9002;....">
</div>
<div id="jmolApplet0_2dappletdiv" style="position:absolute;display:none;overflow:hidden;....">
..
</div>
<div id="jmolApplet0_infotablediv" style="position:absolute;display:none;....">
..
</div>
</div>
~~~

其中的canvas是显示的主窗口,包在*jmolApplet0_appletinfotablediv*内.下面还有两个div不显示任何东东.因此我们可以控制最外的div全屏,而canvas和*jmolApplet0_appletdiv*都100%就可以了.

不过注意,我们可以设置jmol长宽为"100%",但是其大小取决于上层div的大小,所以这里用一个div *jmolwindow* 再包起jmol,日常大小控制这个div即可.

全屏化必须在一个函数内通过事件才能调用.  
另外注意全屏由于浏览器的问题,有几种可能,所以这里有if else判断.

~~~javascript
//<div id="jmolwindow" style="position:relative; width: 512px; height:512px;margin: 0;padding:0;">
//<script>initJmol('1ajj.pdb','"100%"');</script> 
//</div>

function initJmol(inmol,winsize){
    var  script_run = 'load '+inmol+'; cartoon only; color cartoons structure;';
    var Info0 = {
      width: winsize,
      height: winsize,
      color: "black",
      serverURL: "jsmol/php/jsmol.php",
      use: "HTML5",
      jarPath: "jsmol/java",
      j2sPath: "jsmol/j2s",
      //console: "JmolApplet0_Console.jar",
      //jarFile: "../jsmol/java/JmolApplet0",
      script: script_run,//The command defined before.
      disableInitialConsole: true
    }
      Jmol.getApplet("jmolApplet0", Info0)//use applet name and info.
      Jmol.script(jmolApplet0,'set antialiasDisplay false');
      Jmol.script(jmolApplet0,'set platformSpeed 5');

}

function JmolFullScreen(){
    var jm=document.getElementById("jmolApplet0_appletinfotablediv");
    if (jm.requestFullscreen) {
      jm.requestFullscreen();
    } else if (jm.webkitRequestFullscreen) {
      jm.webkitRequestFullscreen();
    } else if (jm.mozRequestFullScreen) {
      jm.mozRequestFullScreen();
    } else if (jm.msRequestFullscreen) {
      jm.msRequestFullscreen();
    }
}
Jmol.jmolButton(jmolApplet0, "javascript JmolFullScreen()", "Fullscreen", "Fullscreen", "View Mol in Fullscreen");
~~~

## Reference
1. [Fullscreen](http://www.sitepoint.com/use-html5-full-screen-api/),[HTML5 Full-Screen API ](http://www.sitepoint.com/use-html5-full-screen-api/)

------
