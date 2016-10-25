---
layout: post
title: JS利用FILE-API读取操作文件
date: 2015-07-13 21:15:06
categories: Coding
tags: HTML JS
---

今天要写个脚本能够对上传文件进行分析, 需要HTML客户端使用JS分析文件.

-------

## About File API

HTML5为我们提供了一种与本地文件系统交互的标准方式：**File API**。该规范主要定义了以下数据结构：

- File: 文件对象,包含有文件名,文件大小,mimetype类型和对文件句柄引用等.
- FileList: 一个文件对象的数组.
- Blob: 操作分割文件到字节

#### To check your browser whether support HTML5 File-API

~~~javascript
// Check for the various File API support.
function isSupportFileApi() {
    if(window.File && window.FileList && window.FileReader && window.Blob) {
        alert('The File APIs are supported in this browser!');//return true;
    } else{
    alert('The File APIs are not fully supported in this browser.');//return false;
}}
//A button to call this function
~~~

<script>function isSupportFileApi() {if(window.File && window.FileList && window.FileReader && window.Blob) {alert("The File API are supported in this browser!");}else{alert('The File APIs are not fully supported in this browser.');}}</script><input type="button" value="检测" onclick="isSupportFileApi()">

## Use File Handle

### Use Form: input type=file

- 可以使用新multiple属性来进行多选, 此时files需要用数组.
- output标签也是新对象,用来定义不同类型的输出,例如脚本的输出.

~~~javascript
<input type="file" id="files" name="files[]" multiple />
<output id="list"></output>

<script>
  function handleFileSelect(evt) {
    var files = evt.target.files; // FileList object

    // files is a FileList of File objects. List some properties.
    var output = [];
    for (var i = 0, f; f = files[i]; i++) {
      output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
                  f.size, ' bytes, last modified: ',
                  f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a',
                  '</li>');
    }
    document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';
  }

  document.getElementById('files').addEventListener('change', handleFileSelect, false);
</script>
~~~

<input type="file" id="files" name="files[]" multiple />

<output id="list"></output>

<script>  function handleFileSelect(evt) {var files = evt.target.files;var output = [];for (var i = 0, f; f = files[i]; i++) {output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',f.size, ' bytes, last modified: ',f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a','</li>');} document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';}document.getElementById('files').addEventListener('change', handleFileSelect, false);</script>


### Use drag method

拖拽通过一个叫`dataTransfer`的接口来获得拖拽的文件列表，更多关于[dataTransfer](http://www.w3.org/TR/2011/WD-html5-20110113/dnd.html#the-datatransfer-interface)。拖拽同样支持多选，用户可以拖拽多个文件。

~~~javascript
<div id="drop_zone">Drop files here</div>
<output id="list2"></output>

<script>
  function handleFileSelect2(evt) {
    evt.stopPropagation();
    evt.preventDefault();

    var files = evt.dataTransfer.files; // FileList object.

    // files is a FileList of File objects. List some properties.
    var output = [];
    for (var i = 0, f; f = files[i]; i++) {
      output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
                  f.size, ' bytes, last modified: ',
                  f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a',
                  '</li>');
    }
    document.getElementById('list2').innerHTML = '<ul>' + output.join('') + '</ul>';
  }

  function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
    evt.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
  }

  // Setup the dnd listeners.
  var dropZone = document.getElementById('drop_zone');
  dropZone.addEventListener('dragover', handleDragOver, false);
  dropZone.addEventListener('drop', handleFileSelect2, false);
</script>
~~~

<div id="drop_zone" style="width:10em;height:2em;margin:auto;color:red;background:yellow;text-align:center;padding:auto;font-size:20pt">Drop files here</div>

<output id="list2"></output>

<script>  function handleFileSelect2(evt) {evt.stopPropagation(); evt.preventDefault();var files = evt.dataTransfer.files;var output = [];for (var i = 0, f; f = files[i]; i++) {output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ', f.size, ' bytes, last modified: ',f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a',  '</li>');}document.getElementById('list2').innerHTML = '<ul>' + output.join('') + '</ul>';  }  function handleDragOver(evt) { evt.stopPropagation(); evt.preventDefault(); evt.dataTransfer.dropEffect = 'copy'; } var dropZone = document.getElementById('drop_zone');  dropZone.addEventListener('dragover', handleDragOver, false);  dropZone.addEventListener('drop', handleFileSelect2, false);</script>


## Read the file

FileReader 包括四个异步读取文件的选项：

- FileReader.readAsBinaryString(Blob/File) - result 属性将包含二进制字符串形式的 file/blob 数据。每个字节均由一个 [0..255] 范围内的整数表示。
- FileReader.readAsText(Blob/File, opt_encoding) - result属性将包含文本字符串形式的 file/blob 数据。该字符串在默认情况下采用“UTF-8”编码。使用可选编码参数可指定其他格式。
- FileReader.readAsDataURL(Blob/File) - result 属性将包含编码为数据网址的 file/blob 数据。
- FileReader.readAsArrayBuffer(Blob/File) - result属性将包含 ArrayBuffer 对象形式的 file/blob 数据。

当您获取了 File 引用后，实例化 FileReader 对象，以便将其内容读取到内存中。加载结束后，将触发读取程序的 onload 事件，而其 result 属性可用于访问文件数据。  
对您的 FileReader 对象调用其中某一种读取方法后，可使用 onloadstart、onprogress、onload、onabort、onerror 和 onloadend 跟踪其进度。

### 选择图片文件并预览

使用`reader.readAsDataURL()`进行文件调用.

~~~javascript
<style>
  .thumb {
    height: 75px;
    border: 1px solid #000;
    margin: 10px 5px 0 0;
  }
</style>

<input type="file" id="files3" name="files[]" multiple />
<output id="list3"></output>

<script>
  function handleFileSelect(evt) {
    var files = evt.target.files; // FileList object

    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {
      // Only process image files.
      if (!f.type.match('image.*')) {
        continue;
      }
      var reader = new FileReader();

      // Closure to capture the file information.
      reader.onload = (function(theFile) {
        return function(e) {
          // Render thumbnail.
          var span = document.createElement('span');
          span.innerHTML = ['<img class="thumb" src="', e.target.result,
                            '" title="', escape(theFile.name), '"/>'].join('');
          document.getElementById('list3').insertBefore(span, null);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
    }
  }

  document.getElementById('files3').addEventListener('change', handleFileSelect, false);
</script>
~~~

<style>.thumb {height: 75px;border: 1px solid #000 margin: 10px 5px 0 0;}</style>

<input type="file" id="files3" name="files[]" multiple />

<output id="list3"></output>

<script>function handleFileSelect(evt) {var files = evt.target.files;for (var i = 0, f; f = files[i]; i++) {if (!f.type.match('image.*')) {continue;}var reader = new FileReader();reader.onload = (function(theFile) {return function(e) {var span = document.createElement('span');span.innerHTML = ['<img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/>'].join('');document.getElementById('list3').insertBefore(span, null);};})(f);reader.readAsDataURL(f);}}document.getElementById('files3').addEventListener('change', handleFileSelect, false);</script>

### 选择Text型文件并查看

使用`reader.readAsText()`进行文件调用.

~~~javascript
<input type="file" id="files4" name="files[]" multiple />

<output id="list4"></output>

<script>
function handleFileTextSelect(evt) {
  var files = evt.target.files;
  for (var i = 0, f; f = files[i]; i++) {
    var reader = new FileReader();
    reader.onload = (function(theFile) {
      return function(e) {
        var span = document.createElement('span');
        span.innerHTML = [e.target.result].join('');
        document.getElementById('list4').insertBefore(span, null);
        }
    ;}    
    )(f);
    // Read in the file context.
    reader.readAsText(f);}
}
document.getElementById('files4').addEventListener('change', handleFileTextSelect, false);
</script>
~~~

<input type="file" id="files4" name="files[]" multiple />

<output id="list4"></output>

<script>function handleFileTextSelect(evt) {var files = evt.target.files;for (var i = 0, f; f = files[i]; i++) {var reader = new FileReader();reader.onload = (function(theFile) {return function(e) {var span = document.createElement('span');span.innerHTML = [e.target.result].join('');document.getElementById('list4').insertBefore(span, null);};})(f);reader.readAsText(f);}}document.getElementById('files4').addEventListener('change', handleFileTextSelect, false);</script>

### 分割文件

该示例使用 onloadend 并检查 evt.target.readyState，而不是使用 onload 事件。

~~~javascript
<style>
  #byte_content {
    margin: 5px 0;
    max-height: 100px;
    overflow-y: auto;
    overflow-x: hidden;
  }
  #byte_range { margin-top: 5px; }
</style>

<input type="file" id="files5" name="file" /> Read bytes: 
<span class="readBytesButtons">
  <button data-startbyte="0" data-endbyte="4">1-5</button>
  <button data-startbyte="5" data-endbyte="14">6-15</button>
  <button data-startbyte="6" data-endbyte="7">7-8</button>
  <button>entire file</button>
</span>
<div id="byte_range"></div>
<div id="byte_content"></div>

<script>
  function readBlob(opt_startByte, opt_stopByte) {

    var files = document.getElementById('files5').files;
    if (!files.length) {
      alert('Please select a file!');
      return;
    }

    var file = files[0];
    var start = parseInt(opt_startByte) || 0;
    var stop = parseInt(opt_stopByte) || file.size - 1;

    var reader = new FileReader();

    // If we use onloadend, we need to check the readyState.
    reader.onloadend = function(evt) {
      if (evt.target.readyState == FileReader.DONE) { // DONE == 2
        document.getElementById('byte_content').textContent = evt.target.result;
        document.getElementById('byte_range').textContent = 
            ['Read bytes: ', start + 1, ' - ', stop + 1,
             ' of ', file.size, ' byte file'].join('');
      }
    };
    //The following sentence help to make it work
    var blob = file.slice(start, stop + 1);
    if (file.webkitSlice) {
      var blob = file.webkitSlice(start, stop + 1);
    } else if (file.mozSlice) {
      var blob = file.mozSlice(start, stop + 1);
    }
    reader.readAsBinaryString(blob);
  }
  
  document.querySelector('.readBytesButtons').addEventListener('click', function(evt) {
    if (evt.target.tagName.toLowerCase() == 'button') {
      var startByte = evt.target.getAttribute('data-startbyte');
      var endByte = evt.target.getAttribute('data-endbyte');
      readBlob(startByte, endByte);
    }
  }, false);
</script>
~~~

<style>#byte_content {margin: 5px 0;  max-height: 100px; overflow-y: auto; overflow-x: hidden;} #byte_range {margin-top: 5px;}</style>

<input type="file" id="files5" name="file" /> Read bytes: 

<span class="readBytesButtons"><button data-startbyte="0" data-endbyte="4">1-5</button><button data-startbyte="5" data-endbyte="14">6-15</button><button data-startbyte="6" data-endbyte="7">7-8</button><button>entire file</button></span>

<div id="byte_range"></div>

<div id="byte_content"></div>

<script>  function readBlob(opt_startByte, opt_stopByte) {    var files = document.getElementById('files5').files; if (!files.length) { alert('Please select a file!'); return;    }    var file = files[0];    var start = parseInt(opt_startByte) || 0;    var stop = parseInt(opt_stopByte) || file.size - 1;    var reader = new FileReader();    reader.onloadend = function(evt) { if (evt.target.readyState == FileReader.DONE) { document.getElementById('byte_content').textContent = evt.target.result; document.getElementById('byte_range').textContent = ['Read bytes: ', start + 1, ' - ', stop + 1, ' of ', file.size, ' byte file'].join(''); } }; var blob = file.slice(start, stop + 1);if (file.webkitSlice) {var blob = file.webkitSlice(start, stop + 1); } else if (file.mozSlice) { var blob = file.mozSlice(start, stop + 1); } reader.readAsBinaryString(blob);  }  document.querySelector('.readBytesButtons').addEventListener('click', function(evt) { if (evt.target.tagName.toLowerCase() == 'button') { var startByte = evt.target.getAttribute('data-startbyte'); var endByte = evt.target.getAttribute('data-endbyte'); readBlob(startByte, endByte); }  }, false);</script>

### 监控读取进度

在使用异步事件处理时还能顺便获得一项优势，那就是能够监控文件的读取进度；这对于读取大文件、查找错误和预测读取完成时间非常实用。`onloadstart` 和 `onprogress` 事件可用于监控读取进度。以下示例演示了如何通过显示进度条来监控读取状态。要查看进度指示器的实际效果，请尝试读取大文件或远程驱动器中的文件。

~~~javascript
<style>
  #progress_bar {
    margin: 10px 0;
    padding: 3px;
    border: 1px solid #000;
    font-size: 14px;
    clear: both;
    opacity: 0;
    -moz-transition: opacity 1s linear;
    -o-transition: opacity 1s linear;
    -webkit-transition: opacity 1s linear;
  }
  #progress_bar.loading {
    opacity: 1.0;
  }
  #progress_bar .percent {
    background-color: #99ccff;
    height: auto;
    width: 0;
  }
</style>

<input type="file" id="files6" name="file" />
<button onclick="abortRead();">Cancel read</button>
<div id="progress_bar"><div class="percent">0%</div></div>

<script>
  var reader_;
  var progress = document.querySelector('.percent');

  function abortRead() {
    reader_.abort();
  }

  function errorHandler(evt) {
    switch(evt.target.error.code) {
      case evt.target.error.NOT_FOUND_ERR:
        alert('File Not Found!');
        break;
      case evt.target.error.NOT_READABLE_ERR:
        alert('File is not readable');
        break;
      case evt.target.error.ABORT_ERR:
        break; // noop
      default:
        alert('An error occurred reading this file.');
    };
  }

  function updateProgress(evt) {
    // evt is an ProgressEvent.
    if (evt.lengthComputable) {
      var percentLoaded = Math.round((evt.loaded / evt.total) * 100);
      // Increase the progress bar length.
      if (percentLoaded < 100) {
        progress.style.width = percentLoaded + '%';
        progress.textContent = percentLoaded + '%';
      }
    }
  }

  function handleFileSelect(evt) {
    // Reset progress indicator on new file selection.
    progress.style.width = '0%';
    progress.textContent = '0%';

    reader_ = new FileReader();
    reader_.onerror = errorHandler;
    reader_.onprogress = updateProgress;
    reader_.onabort = function(e) {
      alert('File read cancelled');
    };
    reader_.onloadstart = function(e) {
      document.getElementById('progress_bar').className = 'loading';
    };
    reader_.onload = function(e) {
      // Ensure that the progress bar displays 100% at the end.
      progress.style.width = '100%';
      progress.textContent = '100%';
      setTimeout("document.getElementById('progress_bar').className='';", 2000);
    }

    // Read in the image file as a binary string.
    reader_.readAsBinaryString(evt.target.files[0]);
  }

  document.getElementById('files6').addEventListener('change', handleFileSelect, false);
</script>
~~~

<style>#progress_bar {  margin: 10px 0;  padding: 3px;  border: 1px solid #000;  font-size: 14px;  clear: both;  opacity: 0;  -moz-transition: opacity 1s linear;  -o-transition: opacity 1s linear;  -webkit-transition: opacity 1s linear;}#progress_bar.loading {  opacity: 1.0;}#progress_bar .percent {  background-color: #99ccff;  height: auto;  width: 0;}</style>

<input type="file" id="files6" name="file" />

<button onclick="abortRead();">Cancel read</button>

<div id="progress_bar"><div class="percent">0%</div></div>

<script>
var reader_;
var progress = document.querySelector('.percent');
function abortRead() {reader_.abort();}
function errorHandler(evt) {
switch(evt.target.error.code) {
case evt.target.error.NOT_FOUND_ERR:alert('File Not Found!');break;case evt.target.error.NOT_READABLE_ERR:alert('File is not readable');break;
case evt.target.error.ABORT_ERR:break;
default:alert('An error occurred reading this file.');};}
function updateProgress(evt) {if (evt.lengthComputable) {var percentLoaded = Math.round((evt.loaded / evt.total) * 100);if (percentLoaded < 100) {progress.style.width = percentLoaded + '%';progress.textContent = percentLoaded + '%';}}}
function handleFileSelect(evt) {
progress.style.width = '0%';progress.textContent = '0%';reader_ = new FileReader();reader_.onerror = errorHandler;
reader_.onprogress = updateProgress;
reader_.onabort = function(e) {alert('File read cancelled');};
reader_.onloadstart = function(e) {document.getElementById('progress_bar').className = 'loading';};
reader_.onload = function(e) {
progress.style.width = '100%';progress.textContent = '100%';
setTimeout("document.getElementById('progress_bar').className='';", 2000);}
reader_.readAsBinaryString(evt.target.files[0]);}
document.getElementById('files6').addEventListener('change', handleFileSelect, false);
</script>


## Reference

1. [Reading files in JavaScript using the File APIs](http://www.html5rocks.com/en/tutorials/file/dndfiles/)
2. [W3-File API](http://www.w3.org/TR/file-upload/)
3. [HTML5读取本地文件](http://hushicai.com/2014/03/29/html5-du-qu-ben-di-wen-jian.html)

------
