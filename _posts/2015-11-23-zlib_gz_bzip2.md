---
layout: post_toc
title: Python:zlib-gz-bzip2模块
date: 2015-11-23 08:04:13
categories: Coding
tags: Python
---

其余一些库如:

- patool: 支持各种格式 [Github](https://github.com/wummel/patool), [pypi](https://pypi.python.org/pypi/patool)
- rarfile: 支持rar, 类似zipfile用法. [Github](https://github.com/markokr/rarfile), [pypi](https://pypi.python.org/pypi/rarfile/), [docs](http://rarfile.readthedocs.org/en/latest/api.html)
- pylzma: 支持LZMA格式. [官网](http://www.joachim-bauch.de/projects/pylzma/), [Github](https://github.com/fancycode/pylzma), [pypi](https://pypi.python.org/pypi/pylzma)

# zlib gz bzip2 modules reference

## zlib — Compression compatible with gzip
For applications that require data compression, the functions in this module allow compression and decompression, using the zlib library. The zlib library has its own home page at <http://www.zlib.net>. There are known incompatibilities between the Python module and versions of the zlib library earlier than 1.1.3; 1.1.3 has a security vulnerability, so we recommend using 1.1.4 or later.

zlib’s functions have many options and often need to be used in a particular order. This documentation doesn’t attempt to cover all of the permutations; consult the zlib manual at <http://www.zlib.net/manual.html> for authoritative information.

For reading and writing .gz files see the gzip module.

The available exception and functions in this module are:

#### exception zlib.error
Exception raised on compression and decompression errors.

#### zlib.adler32(data[, value])
Computes an Adler-32 checksum of data. (An Adler-32 checksum is almost as reliable as a CRC32 but can be computed much more quickly.) If value is present, it is used as the starting value of the checksum; otherwise, a fixed default value is used. This allows computing a running checksum over the concatenation of several inputs. The algorithm is not cryptographically strong, and should not be used for authentication or digital signatures. Since the algorithm is designed for use as a checksum algorithm, it is not suitable for use as a general hash algorithm.

This function always returns an integer object.

> Note: To generate the same numeric value across all Python versions and platforms use adler32(data) & *0xffffffff. If you are only using the checksum in packed binary format this is not necessary as the return value is the correct 32bit binary representation regardless of sign.

Changed in version 2.6: The return value is in the range [-2\*\*31, 2*\*31-1] regardless of platform. In older versions the value is signed on some platforms and unsigned on others.

Changed in version 3.0: The return value is unsigned and in the range [0, 2**32-1] regardless of platform.

#### zlib.compress(string[, level])
Compresses the data in string, returning a string contained compressed data. level is an integer from 0 to 9 controlling the level of compression; 1 is fastest and produces the least compression, 9 is slowest and produces the most. 0 is no compression. The default value is 6. Raises the error exception if any error occurs.

#### zlib.compressobj([level[, method[, wbits[, memlevel[, strategy]]]]])
Returns a compression object, to be used for compressing data streams that won’t fit into memory at once. level is an integer from 0 to 9 controlling the level of compression; 1 is fastest and produces the least compression, 9 is slowest and produces the most. 0 is no compression. The default value is 6.

method is the compression algorithm. Currently, the only supported value is DEFLATED.

wbits is the base two logarithm of the size of the window buffer. This should be an integer from 8 to 15. Higher values give better compression, but use more memory. The default is 15.

memlevel controls the amount of memory used for internal compression state. Valid values range from 1 to 9. Higher values using more memory, but are faster and produce smaller output. The default is 8.

strategy is used to tune the compression algorithm. Possible values are Z\_DEFAULT\_STRATEGY, Z\_FILTERED, and Z\_HUFFMAN\_ONLY. The default is Z\_DEFAULT_STRATEGY.

#### zlib.crc32(data[, value])
Computes a CRC (Cyclic Redundancy Check) checksum of data. If value is present, it is used as the starting value of the checksum; otherwise, a fixed default value is used. This allows computing a running checksum over the concatenation of several inputs. The algorithm is not cryptographically strong, and should not be used for authentication or digital signatures. Since the algorithm is designed for use as a checksum algorithm, it is not suitable for use as a general hash algorithm.

This function always returns an integer object.

> Note: To generate the same numeric value across all Python versions and platforms use crc32(data) & 0xffffffff. If you are only using the checksum in packed binary format this is not necessary as the return value is the correct 32bit binary representation regardless of sign.

Changed in version 2.6: The return value is in the range [-2\*\*31, 2*\*31-1] regardless of platform. In older versions the value would be signed on some platforms and unsigned on others.

Changed in version 3.0: The return value is unsigned and in the range [0, 2**32-1] regardless of platform.

#### zlib.decompress(string[, wbits[, bufsize]])
Decompresses the data in string, returning a string containing the uncompressed data. The wbits parameter controls the size of the window buffer, and is discussed further below. If bufsize is given, it is used as the initial size of the output buffer. Raises the error exception if any error occurs.

The absolute value of wbits is the base two logarithm of the size of the history buffer (the “window size”) used when compressing data. Its absolute value should be between 8 and 15 for the most recent versions of the zlib library, larger values resulting in better compression at the expense of greater memory usage. When decompressing a stream, wbits must not be smaller than the size originally used to compress the stream; using a too-small value will result in an exception. The default value is therefore the highest value, 15. When wbits is negative, the standard gzip header is suppressed.

bufsize is the initial size of the buffer used to hold decompressed data. If more space is required, the buffer size will be increased as needed, so you don’t have to get this value exactly right; tuning it will only save a few calls to malloc(). The default size is 16384.

#### zlib.decompressobj([wbits])
Returns a decompression object, to be used for decompressing data streams that won’t fit into memory at once. The wbits parameter controls the size of the window buffer.

------------

Compression objects support the following methods:

#### Compress.compress(string)
Compress string, returning a string containing compressed data for at least part of the data in string. This data should be concatenated to the output produced by any preceding calls to the compress() method. Some input may be kept in internal buffers for later processing.

#### Compress.flush([mode])
All pending input is processed, and a string containing the remaining compressed output is returned. mode can be selected from the constants Z\_SYNC\_FLUSH, Z\_FULL\_FLUSH, or Z\_FINISH, defaulting to Z\_FINISH. Z\_SYNC\_FLUSH and Z\_FULL\_FLUSH allow compressing further strings of data, while Z\_FINISH finishes the compressed stream and prevents compressing any more data. After calling flush() with mode set to Z\_FINISH, the compress() method cannot be called again; the only realistic action is to delete the object.

#### Compress.copy()
Returns a copy of the compression object. This can be used to efficiently compress a set of data that share a common initial prefix.

New in version 2.5.

------------------

Decompression objects support the following methods, and two attributes:

#### Decompress.unused_data
A string which contains any bytes past the end of the compressed data. That is, this remains "" until the last byte that contains compression data is available. If the whole string turned out to contain compressed data, this is "", the empty string.

The only way to determine where a string of compressed data ends is by actually decompressing it. This means that when compressed data is contained part of a larger file, you can only find the end of it by reading data and feeding it followed by some non-empty string into a decompression object’s decompress() method until the unused_data attribute is no longer the empty string.

#### Decompress.unconsumed_tail
A string that contains any data that was not consumed by the last decompress() call because it exceeded the limit for the uncompressed data buffer. This data has not yet been seen by the zlib machinery, so you must feed it (possibly with further data concatenated to it) back to a subsequent decompress() method call in order to get correct output.

#### Decompress.decompress(string[, max_length])
Decompress string, returning a string containing the uncompressed data corresponding to at least part of the data in string. This data should be concatenated to the output produced by any preceding calls to the decompress() method. Some of the input data may be preserved in internal buffers for later processing.

If the optional parameter max\_length is non-zero then the return value will be no longer than max\_length. This may mean that not all of the compressed input can be processed; and unconsumed data will be stored in the attribute unconsumed\_tail. This string must be passed to a subsequent call to decompress() if decompression is to continue. If max\_length is not supplied then the whole input is decompressed, and unconsumed_tail is an empty string.

#### Decompress.flush([length])
All pending input is processed, and a string containing the remaining uncompressed output is returned. After calling flush(), the decompress() method cannot be called again; the only realistic action is to delete the object.

The optional parameter length sets the initial size of the output buffer.

#### Decompress.copy()
Returns a copy of the decompression object. This can be used to save the state of the decompressor midway through the data stream in order to speed up random seeks into the stream at a future point.

New in version 2.5.

> See also  
	- Module gzip  
	Reading and writing gzip-format files.  
	- <http://www.zlib.net>  
	The zlib library home page.  
	- <http://www.zlib.net/manual.html>  
	The zlib manual explains the semantics and usage of the library’s many functions.

## gzip — Support for gzip files

This module provides a simple interface to compress and decompress files just like the GNU programs gzip and gunzip would.

The data compression is provided by the zlib module.

The gzip module provides the GzipFile class which is modeled after Python’s File Object. The GzipFile class reads and writes gzip-format files, automatically compressing or decompressing the data so that it looks like an ordinary file object.

Note that additional file formats which can be decompressed by the gzip and gunzip programs, such as those produced by compress and pack, are not supported by this module.

The module defines the following items:

#### class gzip.GzipFile([filename[, mode[, compresslevel[, fileobj[, mtime]]]]])
Constructor for the GzipFile class, which simulates most of the methods of a file object, with the exception of the readinto() and truncate() methods. At least one of fileobj and filename must be given a non-trivial value.

The new class instance is based on fileobj, which can be a regular file, a StringIO object, or any other object which simulates a file. It defaults to None, in which case filename is opened to provide a file object.

When fileobj is not None, the filename argument is only used to be included in the gzip file header, which may include the original filename of the uncompressed file. It defaults to the filename of fileobj, if discernible; otherwise, it defaults to the empty string, and in this case the original filename is not included in the header.

The mode argument can be any of 'r', 'rb', 'a', 'ab', 'w', or 'wb', depending on whether the file will be read or written. The default is the mode of fileobj if discernible; otherwise, the default is 'rb'. If not given, the ‘b’ flag will be added to the mode to ensure the file is opened in binary mode for cross-platform portability.

The compresslevel argument is an integer from 0 to 9 controlling the level of compression; 1 is fastest and produces the least compression, and 9 is slowest and produces the most compression. 0 is no compression. The default is 9.

The mtime argument is an optional numeric timestamp to be written to the stream when compressing. All gzip compressed streams are required to contain a timestamp. If omitted or None, the current time is used. This module ignores the timestamp when decompressing; however, some programs, such as gunzip, make use of it. The format of the timestamp is the same as that of the return value of time.time() and of the st_mtime attribute of the object returned by os.stat().

Calling a GzipFile object’s close() method does not close fileobj, since you might wish to append more material after the compressed data. This also allows you to pass a StringIO object opened for writing as fileobj, and retrieve the resulting memory buffer using the StringIO object’s getvalue() method.

GzipFile supports iteration and the with statement.

Changed in version 2.7: Support for the with statement was added.

Changed in version 2.7: Support for zero-padded files was added.

New in version 2.7: The mtime argument.

#### gzip.open(filename[, mode[, compresslevel]])
This is a shorthand for GzipFile(filename, mode, compresslevel). The filename argument is required; mode defaults to 'rb' and compresslevel defaults to 9.

### Examples of usage
Example of how to read a compressed file:

~~~python
import gzip
with gzip.open('file.txt.gz', 'rb') as f:
    file_content = f.read()
~~~

Example of how to create a compressed GZIP file:

~~~python
import gzip
content = "Lots of content here"
with gzip.open('file.txt.gz', 'wb') as f:
    f.write(content)
~~~
Example of how to GZIP compress an existing file:

~~~python
import gzip
import shutil
with open('file.txt', 'rb') as f_in, gzip.open('file.txt.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)
~~~

> See also
>  
> - Module zlib  
> The basic data compression module needed to support the gzip file format.

## bz2 — Compression compatible with bzip2
New in version 2.3.

This module provides a comprehensive interface for the bz2 compression library. It implements a complete file interface, one-shot (de)compression functions, and types for sequential (de)compression.

Here is a summary of the features offered by the bz2 module:

- BZ2File class implements a complete file interface, including readline(), readlines(), writelines(), seek(), etc;
- BZ2File class implements emulated seek() support;
- BZ2File class implements universal newline support;
- BZ2File class offers an optimized line iteration using the readahead algorithm borrowed from file objects;
- Sequential (de)compression supported by BZ2Compressor and BZ2Decompressor classes;
- One-shot (de)compression supported by compress() and decompress() functions;
- Thread safety uses individual locking mechanism.

### (De)compression of files
Handling of compressed files is offered by the BZ2File class.

#### class bz2.BZ2File(filename[, mode[, buffering[, compresslevel]]])
Open a bz2 file. Mode can be either 'r' or 'w', for reading (default) or writing. When opened for writing, the file will be created if it doesn’t exist, and truncated otherwise. If buffering is given, 0 means unbuffered, and larger numbers specify the buffer size; the default is 0. If compresslevel is given, it must be a number between 1 and 9; the default is 9. Add a 'U' to mode to open the file for input in universal newlines mode. Any line ending in the input file will be seen as a '\n' in Python. Also, a file so opened gains the attribute newlines; the value for this attribute is one of None (no newline read yet), '\r', '\n', '\r\n' or a tuple containing all the newline types seen. Universal newlines are available only when reading. Instances support iteration in the same way as normal file instances.

BZ2File supports the with statement.

Changed in version 2.7: Support for the with statement was added.

> Note: This class does not support input files containing multiple streams (such as those produced by the pbzip2 tool). When reading such an input file, only the first stream will be accessible. If you require support for multi-stream files, consider using the third-party bz2file module (available from PyPI). This module provides a backport of Python 3.3’s BZ2File class, which does support multi-stream files.

###### close()
Close the file. Sets data attribute closed to true. A closed file cannot be used for further I/O operations. close() may be called more than once without error.

###### read([size])
Read at most size uncompressed bytes, returned as a string. If the size argument is negative or omitted, read until EOF is reached.

###### readline([size])
Return the next line from the file, as a string, retaining newline. A non-negative size argument limits the maximum number of bytes to return (an incomplete line may be returned then). Return an empty string at EOF.

###### readlines([size])
Return a list of lines read. The optional size argument, if given, is an approximate bound on the total number of bytes in the lines returned.

###### xreadlines()
For backward compatibility. BZ2File objects now include the performance optimizations previously implemented in the xreadlines module.

> Deprecated since version 2.3: This exists only for compatibility with the method by this name on file objects, which is deprecated. Use for line in file instead.

###### seek(offset[, whence])
Move to new file position. Argument offset is a byte count. Optional argument whence defaults to os.SEEK\_SET or 0 (offset from start of file; offset should be >= 0); other values are os.SEEK\_CUR or 1 (move relative to current position; offset can be positive or negative), and os.SEEK_END or 2 (move relative to end of file; offset is usually negative, although many platforms allow seeking beyond the end of a file).

> Note: that seeking of bz2 files is emulated, and depending on the parameters the operation may be extremely slow.

###### tell()
Return the current file position, an integer (may be a long integer).

###### write(data)
Write string data to file. Note that due to buffering, close() may be needed before the file on disk reflects the data written.

###### writelines(sequence\_of\_strings)
Write the sequence of strings to the file. Note that newlines are not added. The sequence can be any iterable object producing strings. This is equivalent to calling write() for each string.

### Sequential (de)compression
Sequential compression and decompression is done using the classes BZ2Compressor and BZ2Decompressor.

#### class bz2.BZ2Compressor([compresslevel])
Create a new compressor object. This object may be used to compress data sequentially. If you want to compress data in one shot, use the compress() function instead. The compresslevel parameter, if given, must be a number between 1 and 9; the default is 9.

###### compress(data)
Provide more data to the compressor object. It will return chunks of compressed data whenever possible. When you’ve finished providing data to compress, call the flush() method to finish the compression process, and return what is left in internal buffers.

###### flush()
Finish the compression process and return what is left in internal buffers. You must not use the compressor object after calling this method.

#### class bz2.BZ2Decompressor
Create a new decompressor object. This object may be used to decompress data sequentially. If you want to decompress data in one shot, use the decompress() function instead.

###### decompress(data)
Provide more data to the decompressor object. It will return chunks of decompressed data whenever possible. If you try to decompress data after the end of stream is found, EOFError will be raised. If any data was found after the end of stream, it’ll be ignored and saved in unused_data attribute.

### One-shot (de)compression
One-shot compression and decompression is provided through the compress() and decompress() functions.

#### bz2.compress(data[, compresslevel])
Compress data in one shot. If you want to compress data sequentially, use an instance of BZ2Compressor instead. The compresslevel parameter, if given, must be a number between 1 and 9; the default is 9.

#### bz2.decompress(data)
Decompress data in one shot. If you want to decompress data sequentially, use an instance of BZ2Decompressor instead.

## Reference

1. [zlib referece](https://docs.python.org/2/library/zlib.html)
2. [gzip referece](https://docs.python.org/2/library/gzip.html)
3. [gzip source code](https://hg.python.org/cpython/file/2.7/Lib/gzip.py)
4. [bz2 referece](https://docs.python.org/2/library/bz2.html)

------
