---
layout: post
title: 最小二乘法实现
date: 2015-09-08 00:47:26
categories: MathStat
tags: Math Stat Matlab Python
---

~~~matlab
clear all;
clc;

% load data
D=load('data.txt');
% Energy, Area, Surface, H 1.1,C 1.87,O 1.76,N 1.40,Cl 1.82,F 2.4,S 2.15

%S=load('test.txt');
%ET=S(:,1);ET=ET';
%T=S(:,2:10);

%Energy
E=D(:,1);
E=E';   %Nonpolar energy

A=D(:,2:10);

I=eye(9);
lambda=500;
para=(inv(A'*A+lambda*I))*(A'*E');

Pred_Eng=A*para;
delta_Eng=E'-Pred_Eng;
%pred_test=T*para;

RMS=sqrt(sum((E-Pred_Eng').*(E-Pred_Eng'))/length(Pred_Eng))
%RMS2=sqrt(sum((ET-pred_test').*(ET-pred_test'))/length(pred_test))

save par9.txt -ascii para;
save pred9.txt -ascii Pred_Eng;
save rms9.txt -ascii RMS;
save delta9.txt -ascii delta_Eng;
~~~

~~~python
#! /usr/bin/env python
# -*- coding: utf8 -*-
import os,sys
import numpy as np

#load data
data=np.loadtxt('data.txt') #n*10

#load test data
#S=np.loadtxt('test.txt');
#ET=S[:,0];
#T=S[:,1:10];

#Nonpolar Energy
E=data[:,0] #6*1

A=data[:,1:10] #6*9
I=np.eye(9) #9*9
para=(np.linalg.inv(A.T.dot(A)+500*I)).dot(A.T.dot(E)) #9*1
np.savetxt('par9.txt',para)

#Predicted Energy
Pred_Eng=A.dot(para);#6*1
delta_Eng=E-Pred_Eng;
#pred_test=T.dot(para);
RMS=np.sqrt(np.sum((E-Pred_Eng)*(E-Pred_Eng))/len(Pred_Eng))
#RMS2=np.sqrt(np.sum((ET-pred_test).*(ET-pred_test))/len(pred_test))

np.savetxt('pred9.txt',Pred_Eng)
np.savetxt('delta9.txt',delta_Eng)
np.savetxt('rms9.txt',np.array([RMS]))
~~~

------
