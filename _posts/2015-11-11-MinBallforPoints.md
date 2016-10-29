---
layout: post
title: 点集的最小球模拟退火算法
date: 2015-11-11 00:32:59
categories: MathStat
tags: Algorithm C++ ZZ
---

[原文点我](http://www.cnblogs.com/DreamUp/archive/2010/10/13/1850431.html)

-----

变步长法属于模拟退火算法的一种。pku2790就可以使用这种方法求解。
 
题意：是求一些空间点集的最小外接球半径。选取一个初始点，然后按一定步长前进，前进的方向选择为指向最靠近它的点。不断让步长衰减，过程中记录最优值。pku2420也是这种题型，可以参考IOI集训队2008年顾研的论文。
 
题目链接：<http://poj.org/problem?id=2069>

~~~cpp
#include<stdio.h>
#include<math.h>
using namespace std;
const int MAX=120;
const double INF=1e20;
const double eps=1e-6;
struct point
{
    double x,y,z;
}ps[MAX],q;
int n;

double dist(point a,point b)
{
    a.x-=b.x;  a.y-=b.y;  a.z-=b.z;
    return sqrt(a.x*a.x+a.y*a.y+a.z*a.z);
}

int maxD(point p)
{
    double res=0;
    int k=0;
    for(int i=0;i<n;++i) {
        double tmp=dist(p,ps[i]);
        if(tmp>res) {
            k=i;
            res=dist(p,ps[i]);
        }
    }
    return k;
}

int main()
{
    while(scanf("%d",&n),n)
    {
        for(int i=0;i<n;++i)
            scanf("%lf%lf%lf",&ps[i].x,&ps[i].y,&ps[i].z);
        double step=100;
        double ans=INF;
        q.x=q.y=q.z=0.0;
        int k=1;
        while(step>eps)
        {
                int d=maxD(q);
                   double tmp=dist(ps[d],q);
            if(tmp<ans)
                ans=tmp;
            double dx=ps[d].x-q.x;
            double dy=ps[d].y-q.y;
            double dz=ps[d].z-q.z;
            dx/=tmp;dy/=tmp;dz/=tmp;
            q.x=q.x+dx*step;
            q.y=q.y+dy*step;
            q.z=q.z+dz*step;
            step*=0.98;
        }
        printf("%.5f\n",ans+1e-7);
    }
    return 0;
}
~~~

------
