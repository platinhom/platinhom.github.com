---
layout: post
title: HTML拾色器和色彩代码
date: 2015-11-11 22:28:29
categories: IT
keywords: Color Picker, Html
tags: HTML CSS JS
---

<style>

#colorchart{border:0;padding:0;border-collapse:collapse;}
#colorchart td{width:23px;height:23px;}
.wrapper{height:100px;display:none}
.holder{width:68px;height:68px;float:left;margin-right:1px;}
.wrapper div div{height:68px;float:left;}
.wrapper div div div{width:38px;height:38px;margin:15px;}
.off{background-image:url('/other/pic/blog-tmp/onoff_001.png');background-position:0 -68px;}
.on{background-image:url('/other/pic/blog-tmp/onoff_001.png');background-position:-68px -136px;}
.yui-picker-hue-thumb{cursor:default;width:28px;height:28px;top:-6px;left:0px;z-index:9;position:absolute;}
.yui-picker-hue-bg{-moz-outline:none;outline:0 none;position:absolute;left:375px;height:366px;width:28px;background:url(/other/pic/blog-tmp/hue_bg.png) no-repeat;top:4px;}
.yui-picker-bg{-moz-outline:none;outline:0 none;position:absolute;top:4px;left:4px;height:364px;width:364px;background-color:#F00;background-image:url(/other/pic/blog-tmp/picker_mask_001.png);}
*html .yui-picker-bg{background-image:none;filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='/other/pic/blog-tmp/picker_mask_001.png',sizingMethod='scale');}
.yui-picker-thumb{cursor:default;width:11px;height:11px;z-index:9;position:absolute;top:-4px;left:-4px;}
.yui-picker-swatch{position:absolute;left:415px;top:10px;height:155px;width:195px;border:2px solid #7c7c7c;}.yui-picker-controls{position:absolute;top:180px;left:415px;font:20px monospace;}
.yui-picker-controls .hd{background:transparent;border-width:0!important;}.yui-picker-controls .bd{height:100px;border-width:0!important;}.yui-picker-controls ul{float:left;padding:0 2px 0 0;margin:0;}.yui-picker-controls li{padding:2px;list-style:none;margin:0;}
.yui-picker-controls input{font-size:20px;width:2.4em;}
.yui-picker-hex-controls{clear:both;padding:20px 0 0 0;font:20px monospace;border-top:0em solid #1BC4F7;}
.yui-picker-hex-controls input{width:160px;font:20px monospace;margin-left:0px;}.yui-picker-controls a{font:20px arial,helvetica,clean,sans-serif;display:block;*display:inline-block;padding:0;color:#000;}
.htmlcode{border:1px solid gray;background-color:gray;color:white;padding:5px;}
#container2{background-color:#eee;height:380px;width:625px;position:relative;font:16px; align:center}
#insertcolor{background-color:#EEE;width:615px;font-size:20px;position:relative;text-align:right;padding:5px;margin:5px 0;}input#startcolor{font-size:16px;width:90px;}button#newcolor{font-size:16px;}-moz-box-sizing:content-box;-webkit-box-sizing:content-box;box-sizing:content-box;
</style>

<!-- javascript -->

<script type="text/javascript" src="/other/pic/blog-tmp/cpcc_003.js"></script>
<script type="text/javascript" language="javascript">
(function() {
 var Event = YAHOO.util.Event, picker, hexcolor;

 Event.onDOMReady(function() {
 picker = new YAHOO.widget.ColorPicker("container2", {
 showhsvcontrols: true,
 showhexcontrols: true,
 showwebsafe: false });
			picker.skipAnim=true;	
			var onRgbChange = function(o) {
				setTimeout ("document.getElementById('yui-picker-hex').select()", 50);}
			picker.on("rgbChange", onRgbChange);
			Event.on("newcolor", "click", function(e) {
				hexcolor = cc(document.getElementById('startcolor').value);
				picker.setValue([HexToR(hexcolor), HexToG(hexcolor), HexToB(hexcolor)], false); 
			});
 });
})();
</script>

<p><b>HTML色彩代码</b> 网站提供一件有关于色彩方面的免费工具，来帮助您查找贵站中的 <b>HTML色彩</b> 。 
功能卓越的 <a href="#Html_Color_Chart">HTML色彩表格工具</a> , <a href="#HTML_Color_Picker">HTML色彩提取利器</a> 和<a href="#HTML_Picture_Color_Picker">HTML图片色彩提取器</a> 让这个过程易如反掌。</p>
 
<p>要想在您的网站上快速使用 <b>HTML色彩</b> ，请查阅 <a href="#How_to_use_html_color_codes">“如何使用HTML色彩代码？”</a> 。
如果您愿意学习 <b>HTML色彩代码</b> 中字符组合的真实意思，请查阅 <a href="#HTML_Color_Codes_Theory">“HTML色彩代码理论”</a>部分。</p>

<p><a href="http://html-color-codes.info/web-safe-colors/">网络安全色彩</a> 指的是通用于任何操作系统中的颜色清单。如果您患有色盲症疾病，可以阅读 <a href="http://html-color-codes.info/color-names/">HTML色彩名称</a> 来克服由看不清颜色所带来的困扰。</p>

<!-- color chart -->		
<a name="Html_Color_Chart"></a>
<h2>HTML色彩表格工具</h2>
<p>利用这张动态<strong>HTML色彩表格工具</strong>您可以获取基本色彩的HTML代码。<br>
点击任何一个颜色块来获取<strong>HTML色彩代码</strong>。 底下是一张最近所提取颜色的清单。若要保存HTML色彩以便下次访问，单击它的徽章。</p>
<div id="TD" class="wrapper"></div>
<table id="colorchart">
 <tbody><tr><td bgcolor="#FBEFEF"></td><td bgcolor="#FBF2EF"></td><td bgcolor="#FBF5EF"></td><td bgcolor="#FBF8EF"></td><td bgcolor="#FBFBEF"></td><td bgcolor="#F8FBEF"></td><td bgcolor="#F5FBEF"></td><td bgcolor="#F2FBEF"></td><td bgcolor="#EFFBEF"></td><td bgcolor="#EFFBF2"></td><td bgcolor="#EFFBF5"></td><td bgcolor="#EFFBF8"></td><td bgcolor="#EFFBFB"></td><td bgcolor="#EFF8FB"></td><td bgcolor="#EFF5FB"></td><td bgcolor="#EFF2FB"></td><td bgcolor="#EFEFFB"></td><td bgcolor="#F2EFFB"></td><td bgcolor="#F5EFFB"></td><td bgcolor="#F8EFFB"></td><td bgcolor="#FBEFFB"></td><td bgcolor="#FBEFF8"></td><td bgcolor="#FBEFF5"></td><td bgcolor="#FBEFF2"></td><td bgcolor="#FFFFFF"></td></tr>
 <tr><td bgcolor="#F8E0E0"></td><td bgcolor="#F8E6E0"></td><td bgcolor="#F8ECE0"></td><td bgcolor="#F7F2E0"></td><td bgcolor="#F7F8E0"></td><td bgcolor="#F1F8E0"></td><td bgcolor="#ECF8E0"></td><td bgcolor="#E6F8E0"></td><td bgcolor="#E0F8E0"></td><td bgcolor="#E0F8E6"></td><td bgcolor="#E0F8EC"></td><td bgcolor="#E0F8F1"></td><td bgcolor="#E0F8F7"></td><td bgcolor="#E0F2F7"></td><td bgcolor="#E0ECF8"></td><td bgcolor="#E0E6F8"></td><td bgcolor="#E0E0F8"></td><td bgcolor="#E6E0F8"></td><td bgcolor="#ECE0F8"></td><td bgcolor="#F2E0F7"></td><td bgcolor="#F8E0F7"></td><td bgcolor="#F8E0F1"></td><td bgcolor="#F8E0EC"></td><td bgcolor="#F8E0E6"></td><td bgcolor="#FAFAFA"></td></tr>
 <tr><td bgcolor="#F6CECE"></td><td bgcolor="#F6D8CE"></td><td bgcolor="#F6E3CE"></td><td bgcolor="#F5ECCE"></td><td bgcolor="#F5F6CE"></td><td bgcolor="#ECF6CE"></td><td bgcolor="#E3F6CE"></td><td bgcolor="#D8F6CE"></td><td bgcolor="#CEF6CE"></td><td bgcolor="#CEF6D8"></td><td bgcolor="#CEF6E3"></td><td bgcolor="#CEF6EC"></td><td bgcolor="#CEF6F5"></td><td bgcolor="#CEECF5"></td><td bgcolor="#CEE3F6"></td><td bgcolor="#CED8F6"></td><td bgcolor="#CECEF6"></td><td bgcolor="#D8CEF6"></td><td bgcolor="#E3CEF6"></td><td bgcolor="#ECCEF5"></td><td bgcolor="#F6CEF5"></td><td bgcolor="#F6CEEC"></td><td bgcolor="#F6CEE3"></td><td bgcolor="#F6CED8"></td><td bgcolor="#F2F2F2"></td></tr>
 <tr><td bgcolor="#F5A9A9"></td><td bgcolor="#F5BCA9"></td><td bgcolor="#F5D0A9"></td><td bgcolor="#F3E2A9"></td><td bgcolor="#F2F5A9"></td><td bgcolor="#E1F5A9"></td><td bgcolor="#D0F5A9"></td><td bgcolor="#BCF5A9"></td><td bgcolor="#A9F5A9"></td><td bgcolor="#A9F5BC"></td><td bgcolor="#A9F5D0"></td><td bgcolor="#A9F5E1"></td><td bgcolor="#A9F5F2"></td><td bgcolor="#A9E2F3"></td><td bgcolor="#A9D0F5"></td><td bgcolor="#A9BCF5"></td><td bgcolor="#A9A9F5"></td><td bgcolor="#BCA9F5"></td><td bgcolor="#D0A9F5"></td><td bgcolor="#E2A9F3"></td><td bgcolor="#F5A9F2"></td><td bgcolor="#F5A9E1"></td><td bgcolor="#F5A9D0"></td><td bgcolor="#F5A9BC"></td><td bgcolor="#E6E6E6"></td></tr>
 <tr><td bgcolor="#F78181"></td><td bgcolor="#F79F81"></td><td bgcolor="#F7BE81"></td><td bgcolor="#F5DA81"></td><td bgcolor="#F3F781"></td><td bgcolor="#D8F781"></td><td bgcolor="#BEF781"></td><td bgcolor="#9FF781"></td><td bgcolor="#81F781"></td><td bgcolor="#81F79F"></td><td bgcolor="#81F7BE"></td><td bgcolor="#81F7D8"></td><td bgcolor="#81F7F3"></td><td bgcolor="#81DAF5"></td><td bgcolor="#81BEF7"></td><td bgcolor="#819FF7"></td><td bgcolor="#8181F7"></td><td bgcolor="#9F81F7"></td><td bgcolor="#BE81F7"></td><td bgcolor="#DA81F5"></td><td bgcolor="#F781F3"></td><td bgcolor="#F781D8"></td><td bgcolor="#F781BE"></td><td bgcolor="#F7819F"></td><td bgcolor="#D8D8D8"></td></tr>
 <tr><td bgcolor="#FA5858"></td><td bgcolor="#FA8258"></td><td bgcolor="#FAAC58"></td><td bgcolor="#F7D358"></td><td bgcolor="#F4FA58"></td><td bgcolor="#D0FA58"></td><td bgcolor="#ACFA58"></td><td bgcolor="#82FA58"></td><td bgcolor="#58FA58"></td><td bgcolor="#58FA82"></td><td bgcolor="#58FAAC"></td><td bgcolor="#58FAD0"></td><td bgcolor="#58FAF4"></td><td bgcolor="#58D3F7"></td><td bgcolor="#58ACFA"></td><td bgcolor="#5882FA"></td><td bgcolor="#5858FA"></td><td bgcolor="#8258FA"></td><td bgcolor="#AC58FA"></td><td bgcolor="#D358F7"></td><td bgcolor="#FA58F4"></td><td bgcolor="#FA58D0"></td><td bgcolor="#FA58AC"></td><td bgcolor="#FA5882"></td><td bgcolor="#BDBDBD"></td></tr>
 <tr><td bgcolor="#FE2E2E"></td><td bgcolor="#FE642E"></td><td bgcolor="#FE9A2E"></td><td bgcolor="#FACC2E"></td><td bgcolor="#F7FE2E"></td><td bgcolor="#C8FE2E"></td><td bgcolor="#9AFE2E"></td><td bgcolor="#64FE2E"></td><td bgcolor="#2EFE2E"></td><td bgcolor="#2EFE64"></td><td bgcolor="#2EFE9A"></td><td bgcolor="#2EFEC8"></td><td bgcolor="#2EFEF7"></td><td bgcolor="#2ECCFA"></td><td bgcolor="#2E9AFE"></td><td bgcolor="#2E64FE"></td><td bgcolor="#2E2EFE"></td><td bgcolor="#642EFE"></td><td bgcolor="#9A2EFE"></td><td bgcolor="#CC2EFA"></td><td bgcolor="#FE2EF7"></td><td bgcolor="#FE2EC8"></td><td bgcolor="#FE2E9A"></td><td bgcolor="#FE2E64"></td><td bgcolor="#A4A4A4"></td></tr>
 <tr><td bgcolor="#FF0000"></td><td bgcolor="#FF4000"></td><td bgcolor="#FF8000"></td><td bgcolor="#FFBF00"></td><td bgcolor="#FFFF00"></td><td bgcolor="#BFFF00"></td><td bgcolor="#80FF00"></td><td bgcolor="#40FF00"></td><td bgcolor="#00FF00"></td><td bgcolor="#00FF40"></td><td bgcolor="#00FF80"></td><td bgcolor="#00FFBF"></td><td bgcolor="#00FFFF"></td><td bgcolor="#00BFFF"></td><td bgcolor="#0080FF"></td><td bgcolor="#0040FF"></td><td bgcolor="#0000FF"></td><td bgcolor="#4000FF"></td><td bgcolor="#8000FF"></td><td bgcolor="#BF00FF"></td><td bgcolor="#FF00FF"></td><td bgcolor="#FF00BF"></td><td bgcolor="#FF0080"></td><td bgcolor="#FF0040"></td><td bgcolor="#848484"></td></tr>
 <tr><td bgcolor="#DF0101"></td><td bgcolor="#DF3A01"></td><td bgcolor="#DF7401"></td><td bgcolor="#DBA901"></td><td bgcolor="#D7DF01"></td><td bgcolor="#A5DF00"></td><td bgcolor="#74DF00"></td><td bgcolor="#3ADF00"></td><td bgcolor="#01DF01"></td><td bgcolor="#01DF3A"></td><td bgcolor="#01DF74"></td><td bgcolor="#01DFA5"></td><td bgcolor="#01DFD7"></td><td bgcolor="#01A9DB"></td><td bgcolor="#0174DF"></td><td bgcolor="#013ADF"></td><td bgcolor="#0101DF"></td><td bgcolor="#3A01DF"></td><td bgcolor="#7401DF"></td><td bgcolor="#A901DB"></td><td bgcolor="#DF01D7"></td><td bgcolor="#DF01A5"></td><td bgcolor="#DF0174"></td><td bgcolor="#DF013A"></td><td bgcolor="#6E6E6E"></td></tr>
 <tr><td bgcolor="#B40404"></td><td bgcolor="#B43104"></td><td bgcolor="#B45F04"></td><td bgcolor="#B18904"></td><td bgcolor="#AEB404"></td><td bgcolor="#86B404"></td><td bgcolor="#5FB404"></td><td bgcolor="#31B404"></td><td bgcolor="#04B404"></td><td bgcolor="#04B431"></td><td bgcolor="#04B45F"></td><td bgcolor="#04B486"></td><td bgcolor="#04B4AE"></td><td bgcolor="#0489B1"></td><td bgcolor="#045FB4"></td><td bgcolor="#0431B4"></td><td bgcolor="#0404B4"></td><td bgcolor="#3104B4"></td><td bgcolor="#5F04B4"></td><td bgcolor="#8904B1"></td><td bgcolor="#B404AE"></td><td bgcolor="#B40486"></td><td bgcolor="#B4045F"></td><td bgcolor="#B40431"></td><td bgcolor="#585858"></td></tr>
 <tr><td bgcolor="#8A0808"></td><td bgcolor="#8A2908"></td><td bgcolor="#8A4B08"></td><td bgcolor="#886A08"></td><td bgcolor="#868A08"></td><td bgcolor="#688A08"></td><td bgcolor="#4B8A08"></td><td bgcolor="#298A08"></td><td bgcolor="#088A08"></td><td bgcolor="#088A29"></td><td bgcolor="#088A4B"></td><td bgcolor="#088A68"></td><td bgcolor="#088A85"></td><td bgcolor="#086A87"></td><td bgcolor="#084B8A"></td><td bgcolor="#08298A"></td><td bgcolor="#08088A"></td><td bgcolor="#29088A"></td><td bgcolor="#4B088A"></td><td bgcolor="#6A0888"></td><td bgcolor="#8A0886"></td><td bgcolor="#8A0868"></td><td bgcolor="#8A084B"></td><td bgcolor="#8A0829"></td><td bgcolor="#424242"></td></tr>
 <tr><td bgcolor="#610B0B"></td><td bgcolor="#61210B"></td><td bgcolor="#61380B"></td><td bgcolor="#5F4C0B"></td><td bgcolor="#5E610B"></td><td bgcolor="#4B610B"></td><td bgcolor="#38610B"></td><td bgcolor="#21610B"></td><td bgcolor="#0B610B"></td><td bgcolor="#0B6121"></td><td bgcolor="#0B6138"></td><td bgcolor="#0B614B"></td><td bgcolor="#0B615E"></td><td bgcolor="#0B4C5F"></td><td bgcolor="#0B3861"></td><td bgcolor="#0B2161"></td><td bgcolor="#0B0B61"></td><td bgcolor="#210B61"></td><td bgcolor="#380B61"></td><td bgcolor="#4C0B5F"></td><td bgcolor="#610B5E"></td><td bgcolor="#610B4B"></td><td bgcolor="#610B38"></td><td bgcolor="#610B21"></td><td bgcolor="#2E2E2E"></td></tr>
 <tr><td bgcolor="#3B0B0B"></td><td bgcolor="#3B170B"></td><td bgcolor="#3B240B"></td><td bgcolor="#3A2F0B"></td><td bgcolor="#393B0B"></td><td bgcolor="#2E3B0B"></td><td bgcolor="#243B0B"></td><td bgcolor="#173B0B"></td><td bgcolor="#0B3B0B"></td><td bgcolor="#0B3B17"></td><td bgcolor="#0B3B24"></td><td bgcolor="#0B3B2E"></td><td bgcolor="#0B3B39"></td><td bgcolor="#0B2F3A"></td><td bgcolor="#0B243B"></td><td bgcolor="#0B173B"></td><td bgcolor="#0B0B3B"></td><td bgcolor="#170B3B"></td><td bgcolor="#240B3B"></td><td bgcolor="#2F0B3A"></td><td bgcolor="#3B0B39"></td><td bgcolor="#3B0B2E"></td><td bgcolor="#3B0B24"></td><td bgcolor="#3B0B17"></td><td bgcolor="#1C1C1C"></td></tr>
 <tr><td bgcolor="#2A0A0A"></td><td bgcolor="#2A120A"></td><td bgcolor="#2A1B0A"></td><td bgcolor="#29220A"></td><td bgcolor="#292A0A"></td><td bgcolor="#222A0A"></td><td bgcolor="#1B2A0A"></td><td bgcolor="#122A0A"></td><td bgcolor="#0A2A0A"></td><td bgcolor="#0A2A12"></td><td bgcolor="#0A2A1B"></td><td bgcolor="#0A2A22"></td><td bgcolor="#0A2A29"></td><td bgcolor="#0A2229"></td><td bgcolor="#0A1B2A"></td><td bgcolor="#0A122A"></td><td bgcolor="#0A0A2A"></td><td bgcolor="#120A2A"></td><td bgcolor="#1B0A2A"></td><td bgcolor="#220A29"></td><td bgcolor="#2A0A29"></td><td bgcolor="#2A0A22"></td><td bgcolor="#2A0A1B"></td><td bgcolor="#2A0A12"></td><td bgcolor="#151515"></td></tr>
 <tr><td bgcolor="#190707"></td><td bgcolor="#190B07"></td><td bgcolor="#191007"></td><td bgcolor="#181407"></td><td bgcolor="#181907"></td><td bgcolor="#141907"></td><td bgcolor="#101907"></td><td bgcolor="#0B1907"></td><td bgcolor="#071907"></td><td bgcolor="#07190B"></td><td bgcolor="#071910"></td><td bgcolor="#071914"></td><td bgcolor="#071918"></td><td bgcolor="#071418"></td><td bgcolor="#071019"></td><td bgcolor="#070B19"></td><td bgcolor="#070719"></td><td bgcolor="#0B0719"></td><td bgcolor="#100719"></td><td bgcolor="#140718"></td><td bgcolor="#190718"></td><td bgcolor="#190714"></td><td bgcolor="#190710"></td><td bgcolor="#19070B"></td><td bgcolor="#000000"></td></tr>
</tbody></table>

<div>
<!-- color picker -->	
<a name="HTML_Color_Picker"></a>
<h2>HTML色彩提取利器</h2>
<p>滚动垂直的滚动条来选择色彩，然后点击HTML色彩代码左边的颜色块来选择所要呈现的颜色。</p>
<p>您可以通过上边的输入区块来编写色彩代码，调配出您特有的颜色。</p>

<div id="insertcolor" style="align:center">
<button onclick="CPklik()" style="float:left">Save color</button>
插入您的色彩代码：
<input type="text" maxlength="7" value="FFFFFF" id="startcolor" name="startcolor">
<button id="newcolor">GO</button>
</div>
<div ID="CP" class="wrapper" ></div>
<div id="container2" style="align:center"></div>

</div>

<!-- video -->	
<a name="Color_codes_how_to_video"></a>
<h2>色彩代码使用教程视频</h2>
<p>
如果您还不会在这个网站上使用色彩工具，那么可以看看本视频：
<br>
<iframe width="640" height="390" src="http://www.youtube.com/v/8aIUnYel4dU&autoplay=0" frameborder="0" allowfullscreen=""></iframe>
</p>

<!-- how to use -->	
<a name="How_to_use_html_color_codes"></a>
<h2>如何使用HTML色彩代码？</h2>
<p>利用HTML色彩代码，您可以设置网站背景颜色、文本颜色、子表格颜色等等等等。</p>
<p><strong>使用HTML色彩代码设置网站背景颜色：</strong></p>
<div class="htmlcode">&lt;body style="background:#80BFFF"&gt;</div>
<p><strong>使用HTML色彩代码设置字体/文本颜色：</strong></p>
<div class="htmlcode">&lt;span style="color:#80BFFF"&gt;</div>
<p><strong>使用HTML色彩代码设置表格背景颜色：</strong></p>
<div class="htmlcode">&lt;table style="background:#80BFFF"&gt;</div>
<p><strong>使用HTML色彩代码设置链接颜色：</strong></p>
<div class="htmlcode">&lt;a style="color:#80BFFF"&gt;</div>

<!-- theory -->	
<a name="HTML_Color_Codes_Theory"></a>
<h2>HTML色彩代码理论</h2>
<p>
于是您一定在思索这样一个问题：“这种字幕与数字的奇怪组合有其独特的内涵吗？”。答案是：确实有！并且下面这些即为它的运作方式
<br>
<strong>HTML代码格式：</strong>
<br>
每一个HTML代码包含有“#”符号以及6个字幕和数字。这些数字都是十六进制的。比如“FF”在十六进制中代表十进制的数字255。
<br>
<strong>符号意义：</strong>
<br>
HTML色彩代码中前两个符号表示红色的浓度。00指的是颜色最淡而FF则指的是颜色最浓。第三个和第四个符号表示绿色的浓度，第五个和第六个符号表示蓝色的浓度。由此，将各种浓度的红、绿、蓝三种颜色进行组合，我们可以调配出任何所需色彩
<br>
<strong>示例：</strong>
<br>
<strong style="color:#FF0000">#FF0000</strong> - 利用这个HTML代码，我们让浏览器显示不掺杂任何绿色和蓝色成分的最鲜艳的红色。其结果当然就是纯红: <span style="background:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</span>
<br>
<strong style="color:#00FF00">#00FF00</strong> - 这个HTML代码表示只有绿色且不掺杂任何红色和蓝色。其结果是: <span style="background:#00FF00">&nbsp;&nbsp;&nbsp;&nbsp;</span>
<br>
<strong style="color:#0000FF">#0000FF</strong> - 这个HTML代码表示只有蓝色且不掺杂任何红色和绿色。其结果是: <span style="background:#0000FF">&nbsp;&nbsp;&nbsp;&nbsp;</span>
<br>
<strong style="color:#FFFF00; background:#000000">#FFFF00</strong> - 红绿组合生成黄色: <span style="background:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</span>
<br>
<strong style="color:#cceeff; background:#000000">#CCEEFF</strong> - 一些红色、一点绿色以及最高浓度的蓝色，组合成天蓝色: <span style="background:#cceeff">&nbsp;&nbsp;&nbsp;&nbsp;</span>
<br>
</p>

<!-- For Pick in Chart -->
<a name="HTML_Picture_Color_Picker"></a>
<h2>从图片中取色</h2>

1. 选择文件, 选择本地的照片
2. 点击"加载显示图片"按钮, 加载图片
3. 图片加载成功后,在图片中右键点取一个位置, 定位, 在右上小方框显示放大后9*9像素.
4. 在右上的小方框再点右键点取一个放大后的位置, 右下就是相应颜色以及HTML颜色码.

<script type="text/javascript">
function httpGet(theUrl)
{
var xmlHttp = null;
xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", theUrl, false );
xmlHttp.send( null );
return xmlHttp.responseText;
}(function() { ChartLoadEvent();})(); </script>

<!-- Picture color picker -->
<script type="text/javascript">
var ev=0;
var cnvHeight;
var cnvWidth;
var mousePos;
var c;
var ctx;
var cPix;
var ctxPix;
var img;
var imgHeight;
var imgWidth;

oFReader = new FileReader(), rFilter = /^(?:image\/bmp|image\/cis\-cod|image\/gif|image\/ief|image\/jpeg|image\/jpeg|image\/jpeg|image\/pipeg|image\/png|image\/svg\+xml|image\/tiff|image\/x\-cmu\-raster|image\/x\-cmx|image\/x\-icon|image\/x\-portable\-anymap|image\/x\-portable\-bitmap|image\/x\-portable\-graymap|image\/x\-portable\-pixmap|image\/x\-rgb|image\/x\-xbitmap|image\/x\-xpixmap|image\/x\-xwindowdump)$/i;

oFReader.onload = function (oFREvent) {
  document.getElementById("slika").src = oFREvent.target.result;
};

function loadImageFile() {
  if (document.getElementById("uploadImage").files.length === 0) { return; }
  var oFile = document.getElementById("uploadImage").files[0];
  if (!rFilter.test(oFile.type)) { alert("You must select a valid image file!"); return; }
  oFReader.readAsDataURL(oFile);

}

var onclickListener = function(evt) {
	imageData = ctxPix.getImageData(0,0,150,150);
	var barva='#'+d2h(imageData.data[45300+0])+d2h(imageData.data[45300+1])+d2h(imageData.data[45300+2]);
	document.getElementById("pixcolor").value = barva;
	document.getElementById("pixcolor").select();
	document.getElementById("barvadiv").style.backgroundColor=barva;
	istat=!istat;
};

function myFunction()
{
	istat=true;
	cnvWidth=600;
	cnvHeight=450;

	c=document.getElementById("myCanvas");
	ctx=c.getContext("2d");

	cPix=document.getElementById("pixCanvas");
	ctxPix=cPix.getContext("2d");

	ctxPix.mozImageSmoothingEnabled = false;
	ctxPix.webkitImageSmoothingEnabled = false;

	img=document.getElementById("slika");
	imgHeight = img.height;
	imgWidth = img.width;
	
	if (imgHeight<cnvHeight && imgWidth<cnvWidth){
		ctx.mozImageSmoothingEnabled = false;
		ctx.webkitImageSmoothingEnabled = false;
	}

	if ((imgWidth/imgHeight)<1.56667){
		cnvWidth=imgWidth/imgHeight*cnvHeight;
	}else{
		cnvHeight=cnvWidth/(imgWidth/imgHeight);
	}
	ctx.clearRect(0, 0, c.width, c.height);
	ctx.drawImage(img,0,0,cnvWidth,cnvHeight);
	
	var onmoveListener = function(evt) {
		ev=1;
		if (istat){
			mousePos = getMousePos(c, evt);
			drawPix(cPix, ctxPix, img, Math.round(mousePos.x*(imgWidth/cnvWidth)), Math.round(mousePos.y*(imgHeight/cnvHeight)));
		}
	};
	c.addEventListener('mousemove', onmoveListener, false);
	c.addEventListener('mousedown', onclickListener, false);
	
	var onMiniclickListener = function(evt) {
		mousePos = getMousePos(cPix, evt);
		imageData = ctxPix.getImageData(0,0,150,150);
		var loc= Math.round(mousePos.y)*600+Math.round(mousePos.x)*4;
		var barva='#'+d2h(imageData.data[loc+0])+d2h(imageData.data[loc+1])+d2h(imageData.data[loc+2]);
		document.getElementById("pixcolor").value = barva;
		document.getElementById("pixcolor").select();
		document.getElementById("barvadiv").style.backgroundColor=barva;
	};
	cPix.addEventListener('mousedown', onMiniclickListener, false);
	  
}
function drawPix(cPix, ctxPix, img, x, y) {
	ctxPix.clearRect(0, 0, cPix.width, cPix.height);
	if (x<5) x=5;
	if (y<5) y=5;
	if (x>imgWidth-4) x=imgWidth-4;
	if (y>imgHeight-4) y=imgHeight-4;
	ctxPix.drawImage(img,x-5,y-5,9,9,0,0,cPix.width,cPix.height);
}
function getMousePos(canvas, evt) {
	var rect = canvas.getBoundingClientRect();
	return { x: evt.clientX - rect.left, y: evt.clientY - rect.top	};
}
function d2h(d){
	return ("0"+d.toString(16)).slice(-2).toUpperCase();
}
function greenbox(c, x, y){
	c.beginPath();
    c.rect(x-5, y-5, 9, 9);
    c.lineWidth = 1;
    c.strokeStyle = '#00FF00';
    c.stroke();
}

</script>

<div id="Picinsertcolor" style="width:612px;">
<input style="float:left;" id="uploadImage" type="file" name="myPhoto" onchange="loadImageFile();" /><button onclick="myFunction()"> 加载显示图片 </button>
</div>
<div style="width:752px;height:452px;position: relative;background-color: #EEE;">
<canvas id="myCanvas" width="600" height="450" style="border:1px solid #d3d3d3;position: absolute; left: 0; top: 0; z-index: 0;">Your browser does not support the HTML5 canvas tag.</canvas>
<canvas id="pixCanvas" width="150" height="150" style="border:1px solid #d3d3d3;position: absolute; left: 600px; top: 0; z-index: 0;">Your browser does not support the HTML5 canvas tag.</canvas>
<div id="barvadiv" style="border:25px solid #d3d3d3;height:100px;width:100px;background-color:#d3d3d3;position: absolute; left: 602px; top: 152px; z-index: 0;"></div>
<div id="Picinsertcolor" style="width:150px;font-size:20px;position: absolute;absolute; left: 602px; top: 304px;z-index: 0;">
	Color Code: <br/><input type="text" maxlength="7" id="pixcolor" name="pixcolor" style="font-size:20px;width:100px;">
</div>
</div>


<img id="slika" src="data:image/svg+xml,%3C%3Fxml%20version%3D%221.0%22%3F%3E%0A%3Csvg%20width%3D%22153%22%20height%3D%22153%22%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%3E%0A%20%3Cg%3E%0A%20%20%3Ctitle%3ENo%20image%3C/title%3E%0A%20%20%3Crect%20id%3D%22externRect%22%20height%3D%22150%22%20width%3D%22150%22%20y%3D%221.5%22%20x%3D%221.500024%22%20stroke-width%3D%223%22%20stroke%3D%22%23666666%22%20fill%3D%22%23e1e1e1%22/%3E%0A%20%20%3Ctext%20transform%3D%22matrix%286.66667%2C%200%2C%200%2C%206.66667%2C%20-960.5%2C%20-1099.33%29%22%20xml%3Aspace%3D%22preserve%22%20text-anchor%3D%22middle%22%20font-family%3D%22Fantasy%22%20font-size%3D%2214%22%20id%3D%22questionMark%22%20y%3D%22181.249569%22%20x%3D%22155.549819%22%20stroke-width%3D%220%22%20stroke%3D%22%23666666%22%20fill%3D%22%23000000%22%3E%3F%3C/text%3E%0A%20%3C/g%3E%0A%3C/svg%3E" alt="Image preview" style="display:none" />


## Reference

1. [HTML色彩代码](http://html-color-codes.info/chinese/)
2. [11个JavaScript颜色选择器插件](http://www.admin10000.com/document/1391.html)
3. [W3Schools-Color-picker](http://www.w3schools.com/tags/ref_colorpicker.asp)

------
