---
layout: post
title: HTML5新元素
date: 2015-08-01 22:45:11
categories: Coding
tags: Website HTML
---

## [video](http://www.w3school.com.cn/tags/tag_video.asp)及[DOM](http://www.w3school.com.cn/jsref/dom_obj_video.asp): 视频

属性事件:

- 标签内含: 播放不成功时执行的内容或者显示
- src: 播放源文件.也可以通过source标签指明(要指明类型).
- controls: 控制按钮,设置了就会有按钮且不能通过脚本控制.
- width/height: 视频窗口大小.
- autoplay: 自动播放
- preload: 预加载,会被autoplay压制
- loop: 循环播放

DOM:

- play(): 播放
- pause(): 暂停
- paused: 是否暂停
- ended: 是否播放完成
- volume: 音量值或设置音量
- muted: 是否静音
- currentTime: 当前时间

~~~html
<video src="movie.ogg" width="320" height="240" controls="controls">
<source src="movie.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
~~~

## [audio](http://www.w3school.com.cn/tags/tag_audio.asp)及[DOM](http://www.w3school.com.cn/jsref/dom_obj_audio.asp)
属性事件DOM和video类似.

~~~ html
<audio src="song.ogg" controls="controls">
  <source src="song.mp3" type="audio/mpeg">
Your browser does not support the audio tag.
</audio>
~~~

## Canvas

------
