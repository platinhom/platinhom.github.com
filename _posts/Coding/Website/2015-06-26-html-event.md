---
layout: post
title: HTML事件属性
date: 2015-06-26 15:15:28
categories: Coding
tags: Website HTML
---

## Window 事件属性(应用到body标签)

- `onafterprint`	文档打印之后运行的脚本。
- `onbeforeprint`	文档打印之前运行的脚本。
- `onbeforeunload`	文档卸载之前运行的脚本。
- `onerror`	在错误发生时运行的脚本。
- `onhaschange`	当文档已改变时运行的脚本。
- `onload`	页面结束加载之后触发。
- `onmessage`	在消息被触发时运行的脚本。
- `onoffline`	当文档离线时运行的脚本。
- `ononline`	当文档上线时运行的脚本。
- `onpagehide`	当窗口隐藏时运行的脚本。
- `onpageshow`	当窗口成为可见时运行的脚本。
- `onpopstate`	当窗口历史记录改变时运行的脚本。
- `onredo`	当文档执行撤销（redo）时运行的脚本。
- `onresize`	当浏览器窗口被调整大小时触发。
- `onstorage`	在 Web Storage 区域更新后运行的脚本。
- `onundo`	在文档执行 undo 时运行的脚本。
- `onunload`	一旦页面已下载时触发（或者浏览器窗口已被关闭）。

## Form 事件(几乎到所有HTML元素,最常用)

- `onblur`		元素失去焦点时运行的脚本。
- `onchange`	在元素值被改变时运行的脚本。
- `oncontextmenu`	当上下文菜单被触发时运行的脚本。
- `onfocus`		当元素失去焦点时运行的脚本。
- `onformchange`	在表单改变时运行的脚本。
- `onforminput`	当表单获得用户输入时运行的脚本。
- `oninput`		当元素获得用户输入时运行的脚本。
- `oninvalid`	当元素无效时运行的脚本。
- `onreset`		当表单中的重置按钮被点击时触发。HTML5 中不支持。P
- `onselect`	在元素中文本被选中后触发。
- `onsubmit`	在提交表单时触发。

## Keyboard 事件

- `onkeydown`	在用户按下按键时触发。
- `onkeypress`	在用户敲击按钮时触发。
- `onkeyup`		当用户释放按键时触发。

## Mouse 事件

- `onclick`			元素上发生鼠标点击时触发。
- `ondblclick`		元素上发生鼠标双击时触发。
- `ondrag`			元素被拖动时运行的脚本。
- `ondragend`		在拖动操作末端运行的脚本。
- `ondragenter`		当元素元素已被拖动到有效拖放区域时运行的脚本。
- `ondragleave`		当元素离开有效拖放目标时运行的脚本。
- `ondragover`		当元素在有效拖放目标上正在被拖动时运行的脚本。
- `ondragstart`		在拖动操作开端运行的脚本。
- `ondrop`			当被拖元素正在被拖放时运行的脚本。
- `onmousedown`		当元素上按下鼠标按钮时触发。
- `onmousemove`		当鼠标指针移动到元素上时触发。
- `onmouseout`		当鼠标指针移出元素时触发。
- `onmouseover`		当鼠标指针移动到元素上时触发。
- `onmouseup`		当在元素上释放鼠标按钮时触发。
- `onmousewheel`	当鼠标滚轮正在被滚动时运行的脚本。
- `onscroll`		当元素滚动条被滚动时运行的脚本。

## Media 事件(常见于`<audio>`、`<embed>`、`<img>`、`<object>` 以及 `<video>`）

- `onabort`					在退出时运行的脚本。
- `oncanplay`					当文件就绪可以开始播放时运行的脚本（缓冲已足够开始时）。
- `oncanplaythrough`					当媒介能够无需因缓冲而停止即可播放至结尾时运行的脚本。
- `ondurationchange`					当媒介长度改变时运行的脚本。
- `onemptied`				当发生故障并且文件突然不可用时运行的脚本（比如连接意外断开时）。
- `onended`					当媒介已到达结尾时运行的脚本（可发送类似“感谢观看”之类的消息）。
- `onerror`					当在文件加载期间发生错误时运行的脚本。
- `onloadeddata`					当媒介数据已加载时运行的脚本。
- `onloadedmetadata`					当元数据（比如分辨率和时长）被加载时运行的脚本。
- `onloadstart`					在文件开始加载且未实际加载任何数据前运行的脚本。
- `onpause`				当媒介被用户或程序暂停时运行的脚本。
- `onplay`					当媒介已就绪可以开始播放时运行的脚本。
- `onplaying`					当媒介已开始播放时运行的脚本。
- `onprogress`					当浏览器正在获取媒介数据时运行的脚本。
- `onratechange`					每当回放速率改变时运行的脚本（比如当用户切换到慢动作或快进模式）。
- `onreadystatechange`					每当就绪状态改变时运行的脚本（就绪状态监测媒介数据的状态）。
- `onseeked`					当 seeking 属性设置为 false（指示定位已结束）时运行的脚本。
- `onseeking`					当 seeking 属性设置为 true（指示定位是活动的）时运行的脚本。
- `onstalled`					在浏览器不论何种原因未能取回媒介数据时运行的脚本。
- `onsuspend`					在媒介数据完全加载之前不论何种原因终止取回媒介数据时运行的脚本。
- `ontimeupdate`					当播放位置改变时（比如当用户快进到媒介中一个不同的位置时）运行的脚本。
- `onvolumechange`					每当音量改变时（包括将音量设置为静音）时运行的脚本。
- `onwaiting`					当媒介已停止播放但打算继续播放时（比如当媒介暂停已缓冲更多数据）运行脚本

## Reference

1. [HTML 事件属性](http://www.w3school.com.cn/tags/html_ref_eventattributes.asp)

---
