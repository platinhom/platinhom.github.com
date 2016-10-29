---
layout: post_mathjax
title: 蒙特卡洛方法采样算法(ZZ)
date: 2015-10-05 03:50:06
categories: MathStat
tags: ZZ Algorithm
---

原文: [Bin Wang Blog: 蒙特卡洛方法采样算法](http://imbinwang.github.io/blog/mcmc-and-gibbs-sampling/)

-------

蒙特卡罗方法(Monte Carlo Simulation)是一种随机模拟(或者统计模拟)方法，这个方法的发展始于20世纪40年代，和原子弹制造的曼哈顿计划密切相关，当时的几个学术大牛，包括乌拉姆、冯.诺依曼、费米、费曼、Nicholas Metropolis， 在美国洛斯阿拉莫斯国家实验室研究裂变物质的中子连锁反应的时候，开始使用统计模拟的方法，并在最早的计算机上进行编程实现。

给定统计样本集，如何估计产生这个样本集的随机变量概率密度函数。这是大多数人比较熟悉的概率密度估计问题，其求解算法(最大似然估计、最大后验估计等)，大多数人也都是比较了解的。大家试着思考下它的逆问题：给定一个概率分布$$p(x)$$，如何让计算机生成满足这个概率分布的样本。这个问题就是统计模拟中研究的重要问题--采样(Sampling)。本文将重点介绍其中两种重要的采样算法：**MCMC**(Markov Chain Monte Carlo) 算法和**Gibbs Sampling** 算法。

<!--more-->

### Sampling ###
我们知道，计算机本身是无法产生真正的随机数的，但是可以根据一定的算法产生伪随机数（pseudo-random numbers)。最古老最简单的莫过于线性同余随机数生成器：

$$
  x_{n+1}=(ax_n+c)~\textrm{mod}~m
$$

式中$a$，$c$，$m$是数学推导出的合适的常数。这种算法产生的下一个随机数完全依赖当前的随机数，当随机数序列足够大的时候，随机数会出现重复子序列的情况。当然，理论发展到今天，有很多更加先进的随机数产生算法出现，比如 python 数值运算库 numpy 用的是 Mersenne Twister 等。根据上面的算法现在我们有了均匀分布的随机数，但是如何产生满足其他分布下的随机数呢？

首先我们来看一个简单的例子，假设我们想对下面的二项分布进行采样，

$$
  P(X=0)=0.5 ~,~ P(X=1)=0.5
$$

我们如何采样得到$X$的值。我们会很毫不费力地想到“抛硬币”，如果硬币正面朝上，则$X=1$，否则，$X=0$。那计算机怎么做，使用随机数生成器生成0到1之间的随机数$r$，如果$r<0.5$，则$X=1$，否则，$X=0$。当分布是多项式分布

$$
  P(X=i)=1/6 ~,~ i\in{1,2,...,6}
$$

这也很简单，让算机生成0到1之间的随机数$r$，把0到1等分成6个子区间，$r$落在哪个区间，$X$就取值为那个区间的编号。我们在考虑更复杂的情况，假设分布是多元随机变量分布

$$
  P(X_1,X_2,...,X_n)
$$

当然这种情况下也有容易解决的例子，比如随机变量都是独立的情形，

$$
  P(X_1,X_2,...,X_n)=P(X_1)P(X_2)...P(X_n)
$$

我们可以利用前面的算法对每个变量单独进行采样。但是问题并不总是这么简单，当$P(X)$的形式很复杂，或者 $P(X)$ 是个高维的分布且不能分解的时候，样本的生成就可能很困难了。此时就需要使用一些更加复杂的随机模拟的方法来生成样本。而本节中将要重点介绍的 MCMC 算法和 Gibbs Sampling 算法就是最常用的两种，这两个方法在现代贝叶斯分析中被广泛使用。要了解这两个算法，我们首先要对马尔科夫链的平稳分布的性质有基本的认识。

### 马尔科夫链及其平稳分布
马尔科夫链的数学定义很简单

$$
  P(X_{t+1}=x|X_t,X_{t-1},...)=P(X_{t+1}=x|X_t)
$$

也就是状态空间的转换关系，下一个状态的决定只取决于当前的状态。

**马尔科夫链定理**:如果一个非周期马尔科夫链具有转移概率矩阵$P$，且它的任何两个状态是连通的，那么$$\lim_{n \rightarrow \infty}P_{ij}^{n}$$存在且与$$i$$ 无关，记$$\lim_{n \rightarrow \infty}P_{ij}^{n} = \pi(j)$$，有

1. $$
	\lim_{n \rightarrow \infty}P_{ij}^{n} =
	\left(
	\begin{align}
	\pi(1)  \pi(2) \ldots \pi(j) \ldots \\\
	\pi(1) \pi(2)  \ldots \pi(j) \ldots \\\
	\vdots \vdots \vdots \vdots \vdots \\\
	\end{align}
	\right)
   $$
2. $$
     \pi(j) = \sum_{i=0}^{\infty}\pi(i)P_{ij}
   $$

  $\pi$是方程$\pi~P=\pi$的唯一非负解,其中$\pi=[\pi(1),\pi(2),\ldots,\pi(j),\ldots],~\sum_{i=0}^{\infty}\pi(i)=1$, $\pi$称为马尔科夫链的平稳分布。

 马尔科夫链定理非常重要，所有的MCMC方法都是以这个定理作为理论基础的。定理的证明相对复杂，我们就不用纠结它的证明了，直接用这个定理的结论。
 从初始概率分布$\pi_0$出发，我们在马尔科夫链上做状态转移，记$X_i$ 的概率分布为$\pi_i$，则有

 $$
 	X_0\backsim\pi_0(x)
 $$

 $$
 	X_i\backsim\pi_i(x),~\pi_i(x)=\pi_{i-1}(x)P=\pi_0(x)P^n
 $$

 由马尔科夫链定理, 概率分布$\pi_i(x)$将收敛到平稳分布$\pi(x)$。假设到第$n$步的时候马氏链收敛，则有

 $$
 X_0\backsim\pi_0(x)
 $$

 $$
 X_1\backsim\pi_1(x)
 $$

 $$
 \ldots
 $$

 $$
 X_n\backsim\pi_n(x)=\pi(x)
 $$

 $$
 X_{n+1}\backsim\pi(x)
 $$

 $$
 X_{n+2}\backsim\pi(x)
 $$

 $$
 \ldots
 $$

 如果我们从一个具体的初始状态$x_0$开始，沿着马尔科夫链按照概率转移矩阵做跳转，那么我们得到一个转移序列$$x_0,x_1,x_2,\ldots,x_n,x_{n+1},\ldots$$，由于马尔科夫链的收敛行为， $$x_n,x_{n+1},\ldots$$都将是平稳分布$\pi(x)$的样本。

### MCMC采样算法 ###
对于给定的概率分布$p(x)$，我们希望能有便捷的方式生成它对应的样本。由于马尔科夫链能收敛到平稳分布，于是一个很的漂亮想法是：如果我们能构造一个转移矩阵为$P$的马尔科夫链，使得该马尔科夫链的平稳分布恰好是$p(x)$，那么我们从任何一个初始状态$x_0$出发沿着马尔科夫链转移，得到一个转移序列$$x_0,x_1,x_2,\ldots,x_n,x_{n+1},\ldots$$，如果马尔科夫在第n步已经收敛了，于是我们就得到了$p(x)$,的样本$x_n,x_{n+1},\ldots$。这个绝妙的想法在1953 年被 Metropolis想到了，首次提出了基于马氏链的蒙特卡罗方法，即Metropolis 算法，并在最早的计算机上编程实现。Metropolis 算法是首个普适的采样方法，并启发了一系列 MCMC方法。Metropolis 的这篇论文被收录在《统计学中的重大突破》中，Metropolis算法也被遴选为二十世纪的十个最重要的算法之一。

接下来介绍的MCMC算法是Metropolis算法的一个改进变种，即常用的 Metropolis-Hastings 算法。由上一节定理我们看到了，马尔科夫链的收敛性质主要由转移矩阵$P$ 决定, 所以基于马尔科夫链做采样的关键问题是如何构造转移矩阵$P$，使得平稳分布恰好是我们要的分布$p(x)$。如何能做到这一点呢？我们主要使用如下的定理。

**细致平稳条件**

如果非周期马尔科夫链的转移矩阵$P$和分布$\pi(x)$满足

$$
 \pi(i)P_{ij}=\pi(j)P_{ji} \qquad \textrm{对所有状态}~i,j
$$

则$\pi(x)$是马尔科夫链的平稳分布，上式被称为细致平稳条件(detailed balance condition)。
其实这个定理是显而易见的，因为细致平稳条件的物理含义就是对于任何两个状态$i,j$, 从 $i$ 转移出去到$j$而丢失的概率质量，恰好会被从$j$转移回$i$的概率质量补充回来，所以状态$i$上的概率质量$\pi(i)$是稳定的，从而$\pi(x)$是马尔科夫链的平稳分布。

假设我们已经有一个转移矩阵为$Q$马尔科夫链，$q(i,j)$表示从状态$i$转移到状态$j$的概率，也可以表示为$q(j \vert i)$或者$q(i \rightarrow j)$。 显然，通常情况下

$$
 p(i)q(i,j)\not=p(j)q(j,i)
$$

也就是细致平稳条件不成立，所以$p(x)$不太可能是这个马尔科夫链的平稳分布。我们对马尔科夫链做一个改造，使得细致平稳条件成立。引入一个$\alpha$，我们希望

 $$
 p(i)q(i,j)\alpha(i,j)=p(j)q(j,i)\alpha(j,i)
 $$

 取什么样的$\alpha$以上等式能成立呢？最简单的，按照对称性，我们可以取

 $$
 \alpha(i,j) = p(j)q(j,i) ~,~\alpha(j,i) = p(i)q(i,j)
 $$

 于是上述式成立了。
 在改造$Q$的过程中引入的$\alpha(i,j)$称为接受率，物理意义可以理解为在原来的马尔科夫链上，从状态 $i$ 以$q(i,j)$的概率转跳转到状态$j$的时候，我们以$\alpha(i,j)$的概率接受这个转移，于是得到新的马尔科夫链的转移概率为$q(i,j)\alpha(i,j)$。假设我们已经有一个转移矩阵$Q$，对应元素为$q(i,j)$，整理上述过程就得到了如下的用于采样概率分布$p(x)$的算法。

<hr />

**MCMC采样算法**<br>

1. 初始化马尔科夫链初始状态$X_0=x_0$ <br>
2. 对$t=0,1,2,\ldots$，循环以下步骤进行采样 <br>
	1. 第$t$时刻马尔科夫链状态为$X_t=x_t$，采样$y~\backsim~q(x \vert x_t)$<br>
	2. 从均匀分布采样$u~\backsim~Uniform[0,1]$<br>
	3. 如果$u<a(x_t,y)=p(y)q(x_t \vert y)$则接受转移$x_t~\backsim~y$，即$X_{t+1}=y$<br>
	4. 否则不接受转移，即$X_{t+1}=x_t$<br>
  
<hr />

以上的 MCMC 采样算法已经能很漂亮的工作了，不过它有一个小的问题：马尔科夫链$Q$在转移的过程中的接受率$\alpha(i,j)$可能偏小，这样采样过程中容易原地踏步，拒绝大量的跳转，使得马尔科夫链收敛到平稳分布$p(x)$的速度太慢。

假设$\alpha(i,j)=0.1,\alpha(j,i)=0.2$，此时满足细致平稳条件，于是

 $$
   p(i)q(i,j) \cdot 0.1=p(j)q(j,i) \cdot 0.2
 $$

 上式两边同时扩大5倍，等式变为

 $$
  p(i)q(i,j) \cdot 0.5=p(j)q(j,i) \cdot 1
 $$

 我们提高了接受率，而细致平稳条件并没有打破。这启发我们可以把细致平稳条件中$\alpha(i,j),\alpha(j,i)$等比例放大，使得两数中较大的一个放大到1，如此提高了采样中的跳转接受率。故可以

 $$
  \alpha(i,j)=\min{\bigg\{\frac{p(j)q(j,i)}{p(i)q(i,j)},1\bigg\}}
 $$

 于是，经过对上述MCMC 采样算法中接受率的改造，我们就得到了最常见的 Metropolis-Hastings算法。

<hr />

**Metropolis-Hastings采样算法**<br>

1.  初始化马尔科夫链初始状态$X_0=x_0$<br>
2.  对$t=0,1,2,\ldots$，循环以下步骤进行采样<br>
	1. 第$t$时刻马尔科夫链状态为$X_t=x_t$，采样$y~\backsim~q(x \vert x_t)$<br>
	2. 从均匀分布采样$u~\backsim~Uniform[0,1]$<br>
	3. 如果$u<a(x_t,y)=\min{\bigg\\{\frac{p(j)q(j,i)}{p(i)q(i,j)},1\bigg\\}}$ 则接受转移$x_t~\backsim~y$，即$X_{t+1}=y$
	4. 否则不接受转移，即$$X_{t+1}=x_t$$

<hr />

### Gibbs Sampling ###
对于高维空间的数据采样，Stuart Geman和Donald Geman这两兄弟于1984 年提出来了Gibbs Sampling算法。此时的细致平稳条件可以表示为

$$
   p(x_1,y_1)p(y_2|x_1)=p(x_1,y_2)p(y_1|x_1)
$$

 此时转移矩阵$Q$由条件分布$p(y \vert x_1)$定义。所以n维空间中对于概率分布$p(x_1,x_2,\ldots,x_n)$可以如下定义转移矩阵:
<br>&nbsp;&nbsp;&nbsp;&nbsp;如果当前状态为$x_1,x_2,\ldots,x_n$,转移的过程中，只能沿着坐标轴做转移。沿着$x_i$坐标轴做转移的时候，转移概率由条件概率$$p(x_i \vert x_1,x_2,\ldots,x_{i-1},x_{i+1},\ldots,x_n)$$ 定义；
<br>&nbsp;&nbsp;&nbsp;&nbsp;其它无法沿着单根坐标轴进行的跳转，转移概率都设置为0。

 于是Gibbs Smapling算法可以描述为

<hr />

**Gibbs Sampling采样算法**<br>

1.  随机初始化${x_i:i=1,2,\ldots,n}$
2.  对$t=0,1,2,\ldots$，循环以下步骤进行采样
	1. $$x_{1}^{t+1}~\backsim~p(x_1 \vert x_{2}^{t},x_{3}^{t},\ldots,x_{n}^{t})$$ 
	2. $$x_{2}^{t+1}~\backsim~p(x_2 \vert x_{1}^{t+1},x_{3}^{t},\ldots,x_{n}^{t})$$
	3. $\ldots$ .
	4. $$x_{j}^{t+1}~\backsim~p(x_j \vert x_{1}^{t+1},\ldots,x_{j-1}^{t+1},x_{j+1}^{t},x_{n}^{t})$$ 
	5. $\ldots$ .
	6. $$x_{n}^{t+1}~\backsim~p(x_n \vert x_{1}^{t+1},x_{2}^{t+1},\ldots,x_{n-1}^{t+1})$$

--------

## reference

1. <http://www.quora.com/In-laymans-terms-how-does-Gibbs-Sampling-work>
1. <http://www.people.fas.harvard.edu/~plam/teaching/methods/mcmc/mcmc.pdf>
1. <http://www.52nlp.cn/lda-math-mcmc-%E5%92%8C-gibbs-sampling1>
1. <http://www.xperseverance.net/blogs/2012/04/902/>
1. <http://www.cnblogs.com/daniel-D/p/3388724.html>

------
