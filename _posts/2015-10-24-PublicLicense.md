---
layout: post
title: 开源许可证Public License
date: 2015-10-24 09:08:20
categories: IT
tags: System
---

将项目与代码开源，可以让更多的人与你共享代码，协同合作，让产品质量更高，更加适应社会的需求。然而，这并不代表该项目是可以被随意甚至是滥用的，想要成为真正的开源项目，不是单单把源代码开放在网上即可，必须在释出的项目当中说明，其代码是以某个开源许可证 (Open Source License, Public License) 来进行许可，将特定权利赋予给用户的同时，也规范公众的利用行为，让人们正确的享受开源所带来的好处与乐趣。

为了维护作者和贡献者的合法权利，保证这些软件不被一些商业机构或个人窃取，影响软件的发展，开源社区开发出了各种的开源许可协议。许可证是具有法律效应的协议，目前已有超过 100 种以上([GNU License List](http://www.gnu.org/licenses/license-list.html))被开放源代码促进会 (Open Source Initiative, OSI) 通过，其中 [GPL](http://www.gnu.org/licenses/gpl.html)、[LGPL](http://www.gnu.org/copyleft/lesser.html)、[Apache](http://www.apache.org/licenses/LICENSE-2.0)、[BSD](https://en.wikipedia.org/wiki/BSD_licenses)、[MIT](https://en.wikipedia.org/wiki/MIT_License), [Mozilla](https://www.mozilla.org/en-US/MPL/) 等是最常见的。

如何选择开源许可证呢? 这里提供一个简单的图例(源于[阮一峰博客](http://www.ruanyifeng.com/blog/2011/05/how_to_choose_free_software_licenses.html)):

![free_software_licenses](http://image.beekka.com/blog/201105/free_software_licenses.png)

具体而言，这几种开源许可证的特点为：

- GNU Lesser General Public License (LGPL)  
允许商业软件通过类库引用 (link) 方式使用 LGPL 类库而不需要开源商业软件的代码，但是如果修改 LGPL 协议的代码或者衍生，则所有修改的代码，涉及修改部分的额外代码和衍生的代码都必须采用 LGPL 协议。。

- Mozilla Public License (MPL)  
除了接口程序的源代码以 MPL 许可证的形式对外许可外，源代码库中的源代码就可以不用 MPL 许可证的方式强制对外许可。

- GNU General Public License (GPL)  
可以开源或者免费地使用代码与引用、修改衍生代码，但强制修改后和衍生的代码必须在发布和销售时也必须开放源代码给用户，因此经常与闭源商业软件的商业模式有所冲突。

- BSD  
可以自由的使用，修改源代码，也可以将修改后的代码作为开源或者专有软件再发布，要包含许可协议的声明，但是不可以用开源代码的作者/机构名字和原来产品的名字做市场推广。

- MIT  
你必须在你的发行版里包含原许可协议的声明，无论你是以二进制发布的还是以源代码发布的。

- Apache Licence  
著名的非盈利开源组织 Apache 基金会采用的协议。该协议鼓励代码共享和尊重原作者的著作权，同样允许代码修改，作为开源或者商业软件再发布。

当我们在Github/Gitcafe上新建一个开源项目时, 可以选择创建相应的License, 所以无需考虑额外添加license. 

![](https://camo.githubusercontent.com/4dcf62ebccf699ae4e956b3acf8ab599f5c41652/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f323732332f3634363333342f64633739383332612d643363362d313165322d393266332d3932636635383134663837342e706e67) 

## Reference

1. [给你的项目添加一个合适的开源许可证](http://blog.gitcafe.com/?tag=license)
2. [Choosing an Open Source License](https://github.com/blog/1530-choosing-an-open-source-license)

------
