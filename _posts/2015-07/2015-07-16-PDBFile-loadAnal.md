---
layout: post
title: PDB文件上载前本地JS分析
date: 2015-07-15 16:41:20
categories: CompCB
tags: CompBiol JS
---

- 主要使用HTML5 的 FILE API实现, 使用FileReader的readAsText方法实现对文件的读取分析.
- 使用addEventListener来监听文件选择(change)
- 数组储存链:残基编号,然后据此进行分析和对select标签进行修改.

遇到的问题:

- 在监听事件时引入document.write会莫名其妙挂掉.
- 监听事件执行顺序在onchange事件之后
- 监听事件一句应该在HTML中调用!

~~~javascript
//File API analysis for pKa
function isSupportFileApi() {
    if(window.File && window.FileList && window.FileReader && window.Blob) {
        alert('The File APIs are supported in this browser!');//return true;
    } else{
    alert('The File APIs are not fully supported in this browser.');//return false;
}}
//check whether browser supports FILE API
//isSupportFileApi();

var resARG=new Array();
var resLYS=new Array();
var resHIS=new Array();
var resASP=new Array();
var resGLU=new Array();
var resCYS=new Array();
var resTYR=new Array();

function pKaOptionChoose(){
  var inmethodobj=document.getElementsByName('PKA_CALU')[0];
  if (inmethodobj.checked){
    document.getElementsByName('PKASEL_RESTYPE')[0].disabled=false;
    document.getElementsByName('PKASEL_RESID')[0].disabled=false;
  }else{
    document.getElementsByName('PKASEL_RESTYPE')[0].disabled=true;
    document.getElementsByName('PKASEL_RESID')[0].disabled=true;	
  }
}

function handleFileTextSelect(evt) {
  var files = evt.target.files;
  for (var i = 0, f; f = files[i]; i++) {
    var reader = new FileReader();
    reader.onload = (function(theFile) {
      return function(e) {
		var output=[e.target.result].join('');
		var lines=output.split('\n');
		resARG.splice(0,resARG.length);
		resLYS.splice(0,resLYS.length);
		resHIS.splice(0,resHIS.length);
		resCYS.splice(0,resCYS.length);
		resGLU.splice(0,resGLU.length);
		resASP.splice(0,resASP.length);
		resTYR.splice(0,resTYR.length);
		var tmprn="";
		for (var j=0;j<lines.length;j++){
			var pre6=lines[j].substr(0,6);
			if (pre6=="ATOM  "){
				var rnum=lines[j].substr(21,1)+":"+lines[j].substr(22,4);
				if (rnum!=tmprn){
					var rname=lines[j].substr(17,3);
					tmprn=rnum;
					switch (rname) {
					case "ARG": resARG.push(rnum);break;
					case "LYS": resLYS.push(rnum);break;
					case "HIS": resHIS.push(rnum);break;
					case "CYS": resCYS.push(rnum);break;
					case "GLU": resGLU.push(rnum);break;
					case "ASP": resASP.push(rnum);break;
					case "TYR": resTYR.push(rnum);break;
					default: ;
					}
				}	
			}
		}
		changepKaSelRes();
    }    
    ;})(f);
    // Read in the file context.
    reader.readAsText(f);}
}
//document.getElementsByName('files')[0].addEventListener('change', handleFileTextSelect, false);

function changepKaSelRes(){
	var sel1 = document.getElementsByName('PKASEL_RESTYPE')[0];
	var sel2 = document.getElementsByName('PKASEL_RESID')[0];
	var selres=sel1.value;
	switch (selres) {
	case "ARG": ResetpKaSelResOption(resARG);break;
	case "LYS": ResetpKaSelResOption(resLYS);break;
	case "HIS": ResetpKaSelResOption(resHIS);break;
	case "CYS": ResetpKaSelResOption(resCYS);break;
	case "GLU": ResetpKaSelResOption(resGLU);break;
	case "ASP": ResetpKaSelResOption(resASP);break;
	case "TYR": ResetpKaSelResOption(resTYR);break;
	default: ;}
}

function ResetpKaSelResOption(ary){
	var sel2 = document.getElementsByName('PKASEL_RESID')[0];
	sel2.options.length=0;
	for (var i=0;i<ary.length;i++){
		rnum=ary[i];
		var newopt=document.createElement('option');
		newopt.value=rnum;
		newopt.text=rnum;
		sel2.add(newopt);
	}
}
~~~


<div><input type="file" name="files" onchange="InputFileChoose()"><br>Residue Type: <select size="1" name="PKASEL_RESTYPE" onchange="changepKaSelRes()"><option value ="ARG">ARG</option><option value ="LYS">LYS</option><option value ="HIS">HIS</option><option value ="ASP">ASP</option><option value ="GLU">GLU</option><option value ="CYS">CYS</option><option value ="TYR">TYR</option></select>Residue ID:<select size="1" name="PKASEL_RESID"></select></div>

<script>var resARG=new Array();var resLYS=new Array();var resHIS=new Array();var resASP=new Array();var resGLU=new Array();var resCYS=new Array();var resTYR=new Array();function handleFileTextSelect(evt) {var files = evt.target.files;for (var i = 0, f; f = files[i]; i++) {var reader = new FileReader();reader.onload = (function(theFile) {return function(e) {var output=[e.target.result].join('');var lines=output.split('\n');resARG.splice(0,resARG.length);resLYS.splice(0,resLYS.length);resHIS.splice(0,resHIS.length);resCYS.splice(0,resCYS.length);resGLU.splice(0,resGLU.length);resASP.splice(0,resASP.length);resTYR.splice(0,resTYR.length);var tmprn="";for (var j=0;j<lines.length;j++){var pre6=lines[j].substr(0,6);if (pre6=="ATOM  "){var rnum=lines[j].substr(21,1)+":"+lines[j].substr(22,4);if (rnum!=tmprn){var rname=lines[j].substr(17,3);tmprn=rnum;switch (rname) {case "ARG": resARG.push(rnum);break;case "LYS": resLYS.push(rnum);break;case "HIS": resHIS.push(rnum);break;case "CYS": resCYS.push(rnum);break;case "GLU": resGLU.push(rnum);break;case "ASP": resASP.push(rnum);break;case "TYR": resTYR.push(rnum);break;default: ;}}}}changepKaSelRes();};})(f);reader.readAsText(f);}}document.getElementsByName('files')[0].addEventListener('change', handleFileTextSelect, false);function changepKaSelRes(){var sel1 = document.getElementsByName('PKASEL_RESTYPE')[0];var sel2 = document.getElementsByName('PKASEL_RESID')[0];var selres=sel1.value;switch (selres) {case "ARG": ResetpKaSelResOption(resARG);break;case "LYS": ResetpKaSelResOption(resLYS);break;case "HIS": ResetpKaSelResOption(resHIS);break;case "CYS": ResetpKaSelResOption(resCYS);break;case "GLU": ResetpKaSelResOption(resGLU);break;case "ASP": ResetpKaSelResOption(resASP);break;case "TYR": ResetpKaSelResOption(resTYR);break;default: ;}}function ResetpKaSelResOption(ary){var sel2 = document.getElementsByName('PKASEL_RESID')[0];sel2.options.length=0;for (var i=0;i<ary.length;i++){rnum=ary[i];var newopt=document.createElement('option');newopt.value=rnum;newopt.text=rnum;sel2.add(newopt);}}</script>

------
