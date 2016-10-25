---
layout: post
title: 数据专家必知必会的7款Python工具(ZZ)
date: 2015-07-22 14:11:35
categories: MathStat
tags: Python DataAnal ZZ
---

如果你有志于做一个数据专家，你就应该保持一颗好奇心，总是不断探索，学习，问各种问题。在线入门教程和视频教程能帮你走出第一步，但是最好的方式就是通过熟悉各种已经在生产环境中使用的工具而为成为一个真正的数据专家做好充分准备。

我咨询了我们真正的数据专家，收集整理了他们认为所有数据专家都应该会的七款 Python 工具。The Galvanize Data Science 和 GalvanizeU 课程注重让学生们花大量的时间沉浸在这些技术里。当你找第一份工作的时候，你曾经投入的时间而获得的对工具的深入理解将会使你有更大的优势。下面就了解它 们一下吧：



## IPython
IPython 是一个在多种编程语言之间进行交互计算的命令行 shell，最开始是用 python 开发的，提供增强的内省，富媒体，扩展的 shell 语法，tab 补全，丰富的历史等功能。IPython 提供了如下特性:

- 更强的交互 shell（基于 Qt 的终端）
- 一个基于浏览器的记事本，支持代码，纯文本，数学公式，内置图表和其他富媒体
- 支持交互数据可视化和图形界面工具
- 灵活，可嵌入解释器加载到任意一个自有工程里
- 简单易用，用于并行计算的高性能工具
- 由数据分析总监，Galvanize 专家 Nir Kaldero 提供。

## GraphLab Greate
GraphLab Greate 是一个 Python 库，由 C++ 引擎支持，可以快速构建大型高性能数据产品。
这有一些关于 GraphLab Greate 的特点：

可以在您的计算机上以交互的速度分析以 T 为计量单位的数据量。

- 在单一平台上可以分析表格数据、曲线、文字、图像。
- 最新的机器学习算法包括深度学习，进化树和 factorization machines 理论。
- 可以用 Hadoop Yarn 或者 EC2 聚类在你的笔记本或者分布系统上运行同样的代码。
- 借助于灵活的 API 函数专注于任务或者机器学习。
- 在云上用预测服务便捷地配置数据产品。
- 为探索和产品监测创建可视化的数据。

由 Galvanize 数据科学家 Benjamin Skrainka 提供。

## Pandas
pandas 是一个开源的软件，它具有 BSD 的开源许可，为 Python 编程语言提供高性能，易用数据结构和数据分析工具。在数据改动和数据预处理方面，Python 早已名声显赫，但是在数据分析与建模方面，Python 是个短板。Pands 软件就填补了这个空白，能让你用 Python 方便地进行你所有数据的处理，而不用转而选择更主流的专业语言，例如 R 语言。

整合了劲爆的 IPyton 工具包和其他的库，它在 Python 中进行数据分析的开发环境在处理性能，速度，和兼容方面都性能卓越。Pands 不会执行重要的建模函数超出线性回归和面板回归；对于这些，参考 statsmodel 统计建模工具和 scikit-learn 库。为了把 Python 打造成顶级的统计建模分析环境，我们需要进一步努力，但是我们已经奋斗在这条路上了。

由 Galvanize 专家，数据科学家 Nir Kaldero 提供。



## PuLP
线性编程是一种优化，其中一个对象函数被最大程度地限制了。PuLP 是一个用 Python 编写的线性编程模型。它能产生线性文件，能调用高度优化的求解器，GLPK，COIN CLP/CBC，CPLEX，和GUROBI，来求解这些线性问题。

由 Galvanize 数据科学家 Isaac Laughlin 提供



## Matplotlib
matplotlib 是基于 Python 的 2D（数据）绘图库，它产生（输出）出版级质量的图表，用于各种打印纸质的原件格式和跨平台的交互式环境。matplotlib 既可以用在 python 脚本,  python 和 ipython 的 shell 界面 (ala MATLAB® 或 Mathematica®)，web 应用服务器，和6类 GUI 工具箱。

matplotlib 尝试使容易事情变得更容易，使困难事情变为可能。你只需要少量几行代码，就可以生成图表，直方图，能量光谱（power spectra），柱状图，errorcharts，散点图（scatterplots）等,。

为简化数据绘图，pyplot 提供一个类 MATLAB 的接口界面，尤其是它与 IPython 共同使用时。对于高级用户，你可以完全定制包括线型，字体属性，坐标属性等，借助面向对象接口界面，或项 MATLAB 用户提供类似（MATLAB）的界面。

Galvanize 公司的首席科学官 Mike Tamir 供稿。



## Scikit-Learn
Scikit-Learn 是一个简单有效地数据挖掘和数据分析工具（库）。关于最值得一提的是，它人人可用，重复用于多种语境。它基于 NumPy，SciPy 和 mathplotlib 等构建。Scikit 采用开源的 BSD 授权协议，同时也可用于商业。Scikit-Learn 具备如下特性:

- 分类（Classification） – 识别鉴定一个对象属于哪一类别
- 回归（Regression） – 预测对象关联的连续值属性
- 聚类（Clustering） – 类似对象自动分组集合
- 降维（Dimensionality Reduction） – 减少需要考虑的随机变量数量
- 模型选择（Model Selection） –比较、验证和选择参数和模型
- 预处理（Preprocessing） – 特征提取和规范化

Galvanize 公司数据科学讲师，Isaac Laughlin提供



## Spark
Spark 由一个驱动程序构成，它运行用户的 main 函数并在聚类上执行多个并行操作。Spark 最吸引人的地方在于它提供的弹性分布数据集（RDD），那是一个按照聚类的节点进行分区的元素的集合，它可以在并行计算中使用。RDDs 可以从一个 Hadoop 文件系统中的文件（或者其他的 Hadoop 支持的文件系统的文件）来创建，或者是驱动程序中其他的已经存在的标量数据集合，把它进行变换。用户也许想要 Spark 在内存中永久保存 RDD，来通过并行操作有效地对 RDD 进行复用。最终，RDDs 无法从节点中自动复原。

Spark 中第二个吸引人的地方在并行操作中变量的共享。默认情况下，当 Spark 在并行情况下运行一个函数作为一组不同节点上的任务时，它把每一个函数中用到的变量拷贝一份送到每一任务。有时，一个变量需要被许多任务和驱动程序共享。 Spark 支持两种方式的共享变量：广播变量，它可以用来在所有的节点上缓存数据。另一种方式是累加器，这是一种只能用作执行加法的变量，例如在计数器中和加法运算 中。

由 Galvanize 数据科学家 Benjamin Skrainka 提供。

如果您想对数据科学进行更深入了解，请点击进入我们的项目 our data science giveaway 来获取关于数据研讨会的入场券：诸如 PyData Seattle 和 Data Science Summit，或者获得 Python 资源的优惠，像： Effective Python 和 Data Science from Scratch。

## Reference
1. [转载自](http://acoder.cc/index.php/Article/view/aid/362.html#0-sqq-1-85782-9737f6f9e09dfaf5d3fd14d775bfee85)

------
