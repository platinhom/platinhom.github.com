---
layout: post
title: JMol加载显示静电势表面
date: 2015-06-27 03:32:39
categories: CompCB
tags: CompBiol Visualize Website
---

这周折腾了很久的Jmol加载静电势表面, 这里大致总结一下流程和关键代码.这里表面都使用对象名s1储存.

## 加载表面

主要使用`isosurface`命令.  
产生表面主要靠JMol程序内置方法, 也可以通过加载表面文件来实现. JMol内置支持方法包括vdw表面,溶剂可及,溶剂排除,分子表面这几种.另外也可以进一步对分子表面进行dots/mesh处理.  

- 产生表面: `isosurface s1 vdw`, 表面名支持: `vdw`,`sasurface`,`solvent`,`molecular`
- 加载表面: `isosurface s1 "surface.jvxl"`,`isosurface s1 MSMS "surface.vert"`. 表面文件需用`""`包括.支持EFVET, JVXL, KINEMAGE, PMESH, MSMS, OBJ几种格式,后两种要在文件名之前指明`MSMS/OBJ`类型. MSMS需要vert和face两种文件同时存在才可以.
- 设置表面形式: `isosurface s1 mesh nofill`. 在使用不同形式之前,要关闭别的类型(类型前加no).主要常用`fill`,`mesh`,`dots`三种.
- 设置透明度: `isosurface s1 translucent 4`或者`color $s1 translucent 4`来进行.透明度为0或`color $s1 opaque`都可以恢复不透明.JMol透明度范围是0-8.

## 加载静电势并Mapping静电势到表面

主要使用 `isosurface map`命令. mapping过程可以在创建表面时同时进行, 也可以对已创建的表面(通过ID指明)进行.  
静电势可以用多种volumetric的格点文件加载,原理就是将格点上的值以颜色映射到表面上(所以颜色策略及对应的静电势范围很重要).这里以ABPS的dx文件为例.

- 对已有表面: `isosurface s1 map 'ESP.dx'`
- 同时产生表面: `isosurface s1 OBJ "1234.obj" map 'ESP.dx'`
- 同时设置颜色策略及范围: `isosurface s1 colorscheme "rwb" color absolute -5 5 OBJ '1234.obj' map 'ESP.dx'`

## 调整颜色策略和对应静电势范围

调整颜色策略主要使用`isosurface colorscheme`, 调整对应静电势范围主要使用`isosurface color range min max`

- 调整颜色策略: `isosurface s1 colorscheme "rwb"`,策略需要用双引号.策略包括roygb(彩虹,默认),bwr(蓝白红),rwb(红白蓝),rgb(红绿蓝),high(黄蓝),low(红绿),wb,bw(白黑和黑白),friendly(色盲用?)几种. 还可以自定义..
- 调整对应颜色范围的静电势范围: `isosurface color range -5 5`,也有用`color absolute`写法的.

下面网页代码为几个关键代码:

~~~ html

      <table valign="center" style="text-align:left; font-family:Arial; margin:0px;padding:0px;">
      <tr>
      <td colspan="3">
      <!--Selecting for JMol Surface method-->
        JMol Surface: 
        <select id="selJmolSurface" onkeypress='SelJmolsurface()' onchange='SelJmolsurface()' style='width:120pt'>
        <option value="off">off</option>
        <option value='vdw'>van der Waals</option>
        <option value="sasurface">Solvent-Accessible</option>
        <option value="solvent">Solvent-Excluded</option>
        <option value="molecular">Molecular</option>
        <option value="mesh nofill nodots">Mesh</option>
        <option value="dots nofill nomesh">Dots</option>
        <option value="delete">Delete</option>
        </select>
      </td>

	  <!--Selecting for Surface Transparency, large value, more transparent-->
      <td colspan="3">
      Translucent:
      <select id="selTranslucent" onkeypress='SurfaceTranslucent()' onchange='SurfaceTranslucent()' style='width:30pt'>
        <option value='0'>0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option></select>

      <!--Selecting for JMol Surface color scheme or color-->
      Color:
      <select id="selSurfaceColor" onkeypress='SelSurfaceColor()' onchange='SelSurfaceColor()' style='width:50pt'>
        <option value='bwr'>BWR</option>
        <option value="rwb">RWB</option>
        <option value="rgb">RGB</option>
        <option value="high">High</option>
        <option value="low">Low</option>
        <option value="roygb">Rainbow</option>
        <!--Directly coloring-->
        <option value="red">Red</option>
        <option value="green">Green</option>
        <option value="white">White</option>
        <option value="blue">Blue</option>
      </select>
      </td>
      </tr>

      <tr>
      <!--Setting ESP range min/max by text/scroll bar,scroll bar code is not shown here-->
      <td >ESP min:</td><td valign="top"><input id="espmin" value='-5' style='width:20pt;text-align:right' onkeypress='SetESPRange()'> 
      <img src="transp.gif" height=20px width=1px></td>
      <td  valign="top">
      <script type="text/javascript">document.write(newScroller("min","","doScroll",150,-1,-1,false,-50,50,-5,4, "mouseup"));</script>
      <!--div id="src_min" onscroll="checkScroll('min')"style="position:absolute; font-size: 2pt; height:30px; width:300px; overflow:auto"><img src="transp.gif" height=1 width=1000></div-->
      </td>
      <td>max:</td><td valign="top"><input id="espmax" value='5' style='width:20pt;text-align:right' onkeypress='SetESPRange()'> 
      <img src="transp.gif" height=20px width=1px></td>
      <td valign="top">
      <script type="text/javascript">document.write(newScroller("max","","doScroll",150,-1,-1,false,-50,50,-5,4, "mouseup"));</script>
        <!--div id="src_max"  onscroll="checkScroll('max')" style="position:absolute; font-size: 2pt; height:30px; width:300px; overflow:auto"><img src="transp.gif" height=1 width=1000></div-->
      </td>
      </tr>

    </table>
    <script type="text/javascript">
    Jmol.jmolButton(jmolApplet0, "javascript LoadESPfile('output.dx');", "Load ESP", "LoadDX", "Mapping the electrostatic potential to the surface"); </script>>



<script type="text/javascript">

<!--Showing Surface by Jmol method-->
function SelJmolsurface(){
	var showas=document.getElementById("selJmolSurface").value
	Jmol.script(jmolApplet0,'isosurface s1 '+showas);
	SurfaceTranslucent();
	SelSurfaceColor();
}

<!--Setting Surface Transparancy-->
function SurfaceTranslucent(){
  var showas=document.getElementById("selTranslucent").value
  Jmol.script(jmolApplet0,'isosurface s1 translucent '+showas);
}

<!--Setting Color Scheme or Surface color-->
function SelSurfaceColor(){
	var showas=document.getElementById("selSurfaceColor").value
	if (showas=='rwb' || showas=='bwr' || showas=='rgb'){
		Jmol.script(jmolApplet0,'isosurface s1 colorscheme '+showas);
	}
	else if (showas=='roygb' || showas=='low' || showas=='high'){
		Jmol.script(jmolApplet0,'isosurface s1 colorscheme '+showas);
	}
	else {
		Jmol.script(jmolApplet0,'color $s1 '+showas);
		SurfaceTranslucent();
	}
}

<!--Setting ESP range for the colorscheme-->
function SetESPRange(Relay){
	//Relay when change by scroller
	if (Relay){
		setTimeout("SetESPRange()", 100)
		return
	}
	var showas=document.getElementById("selSurfaceColor").value
	if (showas=='rwb' || showas=='bwr' || showas=='rgb' || showas=='roygb' || showas=='low' || showas=='high'){
		Jmol.script(jmolApplet0,'color $s1 "'+showas+'" range '+document.getElementById("espmin").value+" "+document.getElementById("espmax").value);
	}
}

<!--Mapping the electrostatic potential to the surface-->
function LoadESPfile(infile){
	Jmol.script(jmolApplet0,"isosurface s1 map '"+infile+"';");
	SetESPRange();
}

</script>
~~~

## Reference:

1. [Jmol/JSmol interactive scripting documentation](http://chemapps.stolaf.edu/jmol/docs/#isosurface)
2. [JSMol指令](http://platinhom.github.io/2015/06/24/JSMol-command/)
3. [MIBPB-server](http://platinhom.github.io/wei/mibpb)

---
