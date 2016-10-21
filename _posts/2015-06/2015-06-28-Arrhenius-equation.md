---
layout: post_mathjax
title: Arrhenius阿伦尼乌斯方程与反应速率
date: 2015-06-27 20:33:11
categories: CompCB
tags: CompChem PhysChem HTML OnlineTool JS
---

阿伦尼乌斯方程（或公式）是化学反应的速率常数与温度之间的关系式，适用于基元反应和非基元反应，甚至某些非均相反应. 其一般数学式(不定积分)为:  

$$\alg k= Ae^{-E_a/RT} \quad or \quad \ln k = - \frac{E_a}{RT}+\ln A \ealg$$

通过下式可知,lnk 随 T 的变化率与活化能 $E_a$ 成正比。因此活化能越高，温度升高时反应速率增加得越快，反应速率对温度越敏感。如果同时存在多个活化能值不同的反应，则高温对活化能高的反应有利，低温对活化能低的反应有利。

$$\alg E_a \equiv -R \left [ \frac{\partial \ln k}{\partial (1/T)} \right ]_P \ealg$$

对温度作变量, 微分形式和定积分形式为: 

$$\alg \frac{d \ln k}{d T} = \frac{-E_a}{RT^2} \quad and \quad \ln \frac{k_2}{k_1} = - \frac{E_a}{R} \left ( \frac{1}{T_1} - \frac{1}{T_2}\right ) \ealg$$

实验中, 测得不同温度 T 下的速率常数 k 值，其lnk--1/T图应为一直线，直线的斜率和截距分别为 $$-\frac{E_a}{R}$$ 和 ln A，从此可以分别求得活化能 $E_a$ 和指前因子A。

其中,k 为反应的速率常数；A 称为指前因子/阿伦尼乌斯常数，单位与 k 相同；$E_a$ 为反应的活化能，单位为焦（J）或千焦（kJ），在温度变化范围不大时被视为常数；R 为气体常数；T 为绝对温标下的温度，单位为开尔文（K）。

## 阿伦尼乌斯在反应中的应用.

当温度一定, 比较两个不同反应状态(如加入催化剂)的速度差异:

$$\alg \ln \frac{k_2}{k_1} = - \frac{\Delta E_a}{RT} \ealg$$

若通过过渡态计算后, 算得不同过渡态和反应物的能垒的差为$\Delta E_a$, 就可以推算得速度比:

$$\alg \frac{k_2}{k_1}= e^{-\Delta E_a/RT} \ealg$$

从下面的在线计算我们可以知道, 1 kcal/mol的能垒差异, 速度比为5.4倍. 

## 简易的在线计算. 
Online Calculation for activation energy Ea and reaction rate.

<form>Enter Ea for: <label for="EA2">Reaction 2: </label><input type="text" id="EA2" value="1.0">; <label for="EA1">Reaction 1:</label><input type="text" id="EA1" value="2.0"> <br/>Energy unit: <input type="radio" name="Eunit" value="4.184"> cal/mol; <input type="radio" name="Eunit" value="4184" checked> kcal/mol;<input type="radio" name="Eunit" value="1"> J/mol; <input type="radio" name="Eunit" value="1000"> kJ/mol; <input type="radio" name="Eunit" value="26255000"> hartree <br/><label for="TT">Temperature:</label><input type="text" id="TT" value="298"> K<br/><input type="button" onclick="calck()" value="Calculate"><br/>Result: k<sub>2</sub>/k<sub>1</sub> = <span id="Result"></span></form>

<script>function GetValueFromNames(name){var chkObjs = document.getElementsByName(name);for(var i=0;i<chkObjs.length;i++){if(chkObjs[i].checked){stype=chkObjs[i].value;return stype;}}}; function calck(){var ea2=document.getElementById("EA2").value; var ea1=document.getElementById("EA1").value;var unit=GetValueFromNames("Eunit"); var tt=document.getElementById("TT").value; var dea=(ea1-ea2)*unit/(8.314*tt); var result=Math.pow(Math.E,dea); document.getElementById("Result").innerHTML=result;}</script>

## Reference
1. [中文维基](https://zh.wikipedia.org/wiki/%E9%98%BF%E4%BC%A6%E5%B0%BC%E4%B9%8C%E6%96%AF%E6%96%B9%E7%A8%8B)和[英文维基](https://en.wikipedia.org/wiki/Arrhenius_equation)

---
