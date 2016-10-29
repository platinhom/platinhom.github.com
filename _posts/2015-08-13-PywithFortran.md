---
layout: post
title: Python调用Fortran
date: 2015-08-13 11:53:56
categories: Coding
tags: Python Fortran
---

fortran90程序pow.f90：

~~~fortran
SUBROUTINE pow(x,n,p)
  IMPLICIT NONE
  !f2py intent(in) x
  !f2py intent(in) n
  !f2py intent(out) p
  REAL(KIND=8) :: x,n,p
  
  p = x**n

END SUBROUTINE pow
~~~

这三个 

~~~fortran
  !f2py intent(in) x
  !f2py intent(in) n
  !f2py intent(out) p
~~~
必须要有！

接着终端利用`f2py`编译,生成*pow.so*库.

~~~bash
f2py -m pow -c pow.f90
~~~

然后testf90.py内容：

~~~python
#!/usr/bin/env python

import pow as p

x = 3.
n = 4.0
out = p.pow(x,n)
print out
~~~

## Reference

1. [f2py官网](https://sysbio.ioc.ee/projects/f2py2e/)
2. [NumPy的f2py说明](http://docs.scipy.org/doc/numpy-dev/f2py/)
------
