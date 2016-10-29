---
layout: post_py
title: ACM 计算几何 最小圆覆盖算法
date: 2015-11-11 00:35:18
categories: MathStat
tags: Algorithm C++ VB ZZ
---

[原文点我](http://wenku.baidu.com/view/584b6d3e5727a5e9856a610d.html)

----

平面上有n个点，给定n个点的坐标，试找一个半径最小的圆，将n 个点全部包围，点可以在圆上, 这个圆叫最小包围圆, 求出求出这个圆的圆心坐标和半径.  

实现思路：
先求出两点间的最长距离。以这两点的距离为直径画一个圆，如果包含了所有的点那么 就是所求的解。如果不能包含就说明有三点及三点在这个圆上 根据三点确定一个圆,只要枚举出所有的三点成立的圆,再比较所有成立的圆的半径最小的就是所求的点。

1. 在点集中任取3点A,B,C。
2. 作一个包含A,B,C三点的最小圆,圆周可能通过这3点，也可能只通过其中两点,但包含第3点.后一种情况圆周上的两点一定是位于圆的一条直径的两端。 
3. 在点集中找出距离第2步所建圆圆心最远的D点，若D点已在圆内或圆周上，则该圆即为所求的圆，算法结束.否则，执行第4步。
4. 在A,B,C,D中选3个点,使由它们生成的一个包含这4个点的圆为最小，这3 点成为新的A,B,C，返回执行第2步。若在第4步生成的圆的圆周只通过A,B,C,D 中的两点，则圆周上的两点取成新的A和B,从另两点中任取一点作为新的C。 

程序设计题解上的解题报告：

对于一个给定的点集A，记 `MinCircle(A)`为点集A的最小外接圆，显然，对于所有的点集情况A,MinCircle(A)都是存在且惟一的。需要特别说明的是，当A为空集时，MinCircle(A)为空集，当A={a}时，MinCircle(A)圆心坐标为a，半径为0； 显然，MinCircle(A)可以有A边界上最多三个点确定(当点集A中点的个数大于 1时，有可能两个点确定了MinCircle(A))，也就是说存在着一个点集B，\|B\|<=3 且B包含与A，有MinCircle(B)=MinCircle(A).所以，如果a不属于B，则 MinCircle(A-{a})=MinCircle(A);如果MinCircle(A-{a})不等于MinCircle(A),则 a属于B。 所以我们可以从一个空集R开始，不断的把题目中给定的点集中的点加入R，同时维护R的外接圆最小，这样就可以得到解决该题的算法。

不断添加圆，维护最小圆。如果添加的点i在圆内，不动，否则：
问题转化为求1~I的最小圆：求出1与I的最小圆，并且扫描j=2~I-1，维护（1）+（i）+(2~j)的最小圆，如果找到J不在最小圆内，问题转化为：求(1~J)+(i)的最小圆。求出I与J的最小圆，继续扫描K=1~j-1,找到第一个不在最小圆内的，求出I J K三者交点即可，此时找到了(1~j)+(i)的最小圆，可以回到上一步（三点定一圆，所以1~J-1一定都在求出的最小圆上）。

实际上利用了这么个定理：

1. 若I不在1~I-1的最小圆上，则I在1~I的最小圆上。
2. 若J不在(i)+(1~j-1)的最小圆上，则j在(i)+(1~J)的最小圆上。

证明可以考虑这么做：最小圆必定是可以通过不断放大半径，直到所有以任意点为圆心，半径为半径的圆存在交点，此时的半径就是最小圆。所以上述定理可以通过这个思想得到。

这个做法复杂度是O(n)的，当加入圆的顺序随机时，因为三点定一圆，所以不在圆内概率是3/i,求出期望可得是On.

## C/C++ 思路

~~~cpp
#include<stdio.h>
#include<math.h>
struct   TPoint   
{   
         double x,y;   
}; 
TPoint a[1005],d; 
double r;

double   distance(TPoint   p1,   TPoint   p2)   
{   
          return (sqrt((p1.x-p2.x)*(p1.x -p2.x)+(p1.y-p2.y)*(p1.y-p2.y)));       
}
double multiply(TPoint   p1,   TPoint   p2,   TPoint   p0)   
{   
          return   ((p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y));           
}   
void MiniDiscWith2Point(TPoint   p,TPoint   q,int   n)
{
d.x=(p.x+q.x)/2.0;
d.y=(p.y+q.y)/2.0;
r=distance(p,q)/2;
int k;
double c1,c2,t1,t2,t3;
for(k=1;k<=n;k++)
{
if(distance(d,a[k])<=r)continue;
if(multiply(p,q,a[k])!=0.0) ////不平行
{
   c1=(p.x*p.x+p.y*p.y-q.x*q.x-q.y*q.y)/2.0;
   c2=(p.x*p.x+p.y*p.y-a[k].x*a[k].x-a[k].y*a[k].y)/2.0;

   d.x=(c1*(p.y-a[k].y)-c2*(p.y-q.y))/((p.x-q.x)*(p.y-a[k].y)-(p.x-a[k].x)*(p.y-q.y));
   d.y=(c1*(p.x-a[k].x)-c2*(p.x-q.x))/((p.y-q.y)*(p.x-a[k].x)-(p.y-a[k].y)*(p.x-q.x));
   r=distance(d,a[k]);
}
else        //平行
{
    t1=distance(p,q);
    t2=distance(q,a[k]);
    t3=distance(p,a[k]);
    if(t1>=t2&&t1>=t3)
    {d.x=(p.x+q.x)/2.0;d.y=(p.y+q.y)/2.0;r=distance(p,q)/2.0;}
    else if(t2>=t1&&t2>=t3)
    {d.x=(a[k].x+q.x)/2.0;d.y=(a[k].y+q.y)/2.0;r=distance(a[k],q)/2.0;}
    else 
    {d.x=(a[k].x+p.x)/2.0;d.y=(a[k].y+p.y)/2.0;r=distance(a[k],p)/2.0;}
}
}

}
void MiniDiscWithPoint(TPoint   pi,int   n)
{
d.x=(pi.x+a[1].x)/2.0;
d.y=(pi.y+a[1].y)/2.0;
r=distance(pi,a[1])/2.0;
int j;
for(j=2;j<=n;j++)
{
if(distance(d,a[j])<=r)continue;
else
{
   MiniDiscWith2Point(pi,a[j],j-1);
}
}

}

int main()
{
int i,n;
while(scanf("%d",&n)&&n)
{
for(i=1;i<=n;i++)
{
   scanf("%lf %lf",&a[i].x,&a[i].y);
}
if(n==1)
{ printf("%.2lf %.2lf 0.00\n",a[1].x,a[1].y);continue;}
r=distance(a[1],a[2])/2.0;
d.x=(a[1].x+a[2].x)/2.0;
d.y=(a[1].y+a[2].y)/2.0;
for(i=3;i<=n;i++)
{
   if(distance(d,a[i])<=r)continue;
   else
    MiniDiscWithPoint(a[i],i-1);
}
printf("%.2lf %.2lf %.2lf\n",d.x,d.y,r);
}
return 0;
}
~~~


## VB写法：

~~~vb
Option Explicit
 
Const MAXPOINT = 10
 
Private Type mypoint
    x As Double
    y As Double
End Type
 
Dim p(0 To MAXPOINT - 1) As mypoint
Dim mincx As Double
Dim mincy As Double
Dim minr As Double
Dim p1 As Long
Dim p2 As Long
Dim maxr As Double
Dim centerx As Long
Dim centery As Long
 
Private Sub Form_Load()
    '黑色的比较清楚
    Me.BackColor = vbBlack
    Me.AutoRedraw = True
     
    Me.Width = 800 * Screen.TwipsPerPixelX
    Me.Height = 600 * Screen.TwipsPerPixelY
     
    '所有图形都进行平移，多少无所谓，是一个数值就行
    centerx = Me.ScaleWidth / 2 - 2000
    centery = Me.ScaleHeight / 2 - 2000
     
    Command1.Left = Me.ScaleWidth - Command1.Width
    Command1.Top = Me.ScaleHeight - Command1.Height
End Sub
 
Private Function equ(ByVal a As Double, ByVal b As Double) As Boolean
    If Abs(a - b) < 0.000001 Then
        equ = True
    Else
        equ = False
    End If
End Function
 
Private Function Is_Three_Point_In_A_Line(ByVal x1 As Double, ByVal y1 As Double, ByVal x2 As Double, ByVal y2 As Double, ByVal x3 As Double, ByVal y3 As Double) As Boolean
    Dim a As Double, b As Double, e As Double
     
    a = (x1 + x2) * (x1 - x2) + (y1 + y2) * (y1 - y2)
    b = (x3 + x2) * (x3 - x2) + (y3 + y2) * (y3 - y2)
    e = (x1 - x2) * (y3 - y2) - (x2 - x3) * (y2 - y1)
 
    Is_Three_Point_In_A_Line = equ(e, 0)
 
End Function
 
Private Sub Calc_TPC(ByVal x1 As Double, ByVal y1 As Double, ByVal x2 As Double, ByVal y2 As Double, ByVal x3 As Double, ByVal y3 As Double, cx As Double, cy As Double, r As Double)
    Dim a As Double, b As Double, e As Double
 
    a = (x1 + x2) * (x1 - x2) + (y1 + y2) * (y1 - y2)
    b = (x3 + x2) * (x3 - x2) + (y3 + y2) * (y3 - y2)
    e = (x1 - x2) * (y3 - y2) - (x2 - x3) * (y2 - y1)
 
    cx = (a * (y3 - y2) + b * (y2 - y1)) / (2 * e)
    cy = (a * (x2 - x3) + b * (x1 - x2)) / (2 * e)
    r = Sqr((x1 - cx) * (x1 - cx) + (y1 - cy) * (y1 - cy))
     
     
End Sub
 
Private Function incircle(ByVal cx As Double, ByVal cy As Double, ByVal r As Double, ByVal px As Double, ByVal py As Double) As Boolean
    Dim l1 As Double, l2 As Double
    Dim a As Double
     
    l1 = px - cx
    l2 = py - cy
     
    a = (l1 ^ 2 + l2 ^ 2)
    If a <= (r ^ 2) + 0.1 Then
        incircle = True
    Else
        incircle = False
    End If
     
End Function
Private Sub Command1_Click()
    Me.FillStyle = vbTransparent
    Me.FillColor = 0
    Cls
     
    Randomize Timer
     
    '开始时将minr都置成很大，很重要
    minr = 1E+90
    maxr = 0
     
    Dim i As Long, j As Long, k As Long
    Dim l As Long
    Dim xxx As Double
    Dim cx As Double, cy As Double, r As Double
    Dim count As Long
     
    '先生成50个点
    For i = 0 To MAXPOINT - 1
        p(i).x = Rnd * 4000
        p(i).y = Rnd * 4000
    Next i
     
    '先求 两个距离最远点，如果求出来，计算所形成的圆是否能够包含所有的点
    '如果不能包含，就再用穷举的方法
    For i = 0 To MAXPOINT - 1
        For j = 0 To MAXPOINT - 1
            '求两点的距离，找出最大的
            xxx = Sqr((p(i).x - p(j).x) ^ 2 + (p(i).y - p(j).y) ^ 2)
            cx = (p(i).x + p(j).x) / 2
            cy = (p(i).y + p(j).y) / 2
            r = Sqr((p(i).x - cx) ^ 2 + (p(i).y - cy) ^ 2)
             
            If r > maxr Then
                p1 = i
                p2 = j
                maxr = r
            End If
        Next j
    Next i
     
    '计算所有的点是否在圆内
    cx = (p(p1).x + p(p2).x) / 2
    cy = (p(p1).y + p(p2).y) / 2
    r = Sqr((p(p1).x - cx) ^ 2 + (p(p1).y - cy) ^ 2)
    count = 0
    For l = 0 To MAXPOINT - 1
        If incircle(cx, cy, r, p(l).x, p(l).y) Then
            count = count + 1
        End If
    Next l
    If count = MAXPOINT Then
        '所有的点都在圆内
        '画出最大的圆
        cx = (p(p1).x + p(p2).x) / 2
        cy = (p(p1).y + p(p2).y) / 2
        r = Sqr((p(p1).x - cx) ^ 2 + (p(p1).y - cy) ^ 2)
         
        Circle (cx + centerx, cy + centery), r, vbBlue
    Else
        '计算所有的圆
        For i = 0 To MAXPOINT - 1
            For j = 0 To MAXPOINT - 1
                For k = 0 To MAXPOINT - 1
                    If Not Is_Three_Point_In_A_Line(p(i).x, p(i).y, p(j).x, p(j).y, p(k).x, p(k).y) Then
                        '三点可求圆
                         
                        '求圆
                        Calc_TPC p(i).x, p(i).y, p(j).x, p(j).y, p(k).x, p(k).y, cx, cy, r
                         
                        '计算所有的点是否在圆内
                        count = 0
                        For l = 0 To MAXPOINT - 1
                            If incircle(cx, cy, r, p(l).x, p(l).y) Then
                                count = count + 1
                            End If
                        Next l
                         
                        If count = MAXPOINT Then
                            '所有的点都在圆内
                            If r < minr Then
                                mincx = cx
                                mincy = cy
                                minr = r
                            End If
                        End If
                    End If
                Next k
            Next j
        Next i
         
        '画出最小的圆
        Circle (mincx + centerx, mincy + centery), minr, vbGreen
    End If
     
    '将50个点显示在屏幕上
    Me.FillStyle = vbSolid
    Me.FillColor = vbRed
    For i = 0 To MAXPOINT - 1
        Me.Circle (p(i).x + centerx, p(i).y + centery), 30, vbRed
    Next i
End Sub
~~~


------
