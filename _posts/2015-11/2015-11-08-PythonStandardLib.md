---
layout: post_toc
title: The Python Standard Library (Copy)
date: 2015-11-08 04:13:15
categories: Coding
tags: Python
---

## The Python Standard Library {#STL}

Copy the document Python 2.7.10 standard library. [link](](https://docs.python.org/2/library/)  

While The Python Language Reference describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.

Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.

The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.

In addition to the standard library, there is a growing collection of several thousand components (from individual programs and modules to packages and entire application development frameworks), available from the Python Package Index.

1. Introduction
2. [Built-in Functions](#BuildInFunc)
3. [Non-essential Built-in Functions](#non-essential-built-in-functions)
4. [Built-in Constants](https://docs.python.org/2/library/constants.html)
	1. Constants added by the site module
5. [Built-in Types](#BuildInTypes)
	1. Truth Value Testing
	2. Boolean Operations — and, or, not
	3. Comparisons
	4. Numeric Types — int, float, long, complex
	5. Iterator Types
	6. Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange
	7. Set Types — set, frozenset
	8. Mapping Types — dict
	9. File Objects
	10. memoryview type
	11. Context Manager Types
	12. Other Built-in Types
	13. Special Attributes
6. [Built-in Exceptions](https://docs.python.org/2/library/exceptions.html)
	1. Exception hierarchy
7. [String Services](https://docs.python.org/2/library/strings.html)
	1. string — Common string operations
	2. re — Regular expression operations
	3. struct — Interpret strings as packed binary data
	4. difflib — Helpers for computing deltas
	5. StringIO — Read and write strings as files
	6. cStringIO — Faster version of StringIO
	7. textwrap — Text wrapping and filling
	8. codecs — Codec registry and base classes
	9. unicodedata — Unicode Database
	10. stringprep — Internet String Preparation
	11. fpformat — Floating point conversions
8. [Data Types](https://docs.python.org/2/library/datatypes.html)
	1. datetime — Basic date and time types
	2. calendar — General calendar-related functions
	3. collections — High-performance container datatypes
	4. heapq — Heap queue algorithm
	5. bisect — Array bisection algorithm
	6. array — Efficient arrays of numeric values
	7. sets — Unordered collections of unique elements
	8. sched — Event scheduler
	9. mutex — Mutual exclusion support
	10. Queue — A synchronized queue class
	11. weakref — Weak references
	12. UserDict — Class wrapper for dictionary objects
	13. UserList — Class wrapper for list objects
	14. UserString — Class wrapper for string objects
	15. types — Names for built-in types
	16. new — Creation of runtime internal objects
	17. copy — Shallow and deep copy operations
	18. pprint — Data pretty printer
	19. repr — Alternate repr() implementation
9. [Numeric and Mathematical Modules](https://docs.python.org/2/library/numeric.html)
	1. numbers — Numeric abstract base classes
	2. math — Mathematical functions
	3. cmath — Mathematical functions for complex numbers
	4. decimal — Decimal fixed point and floating point arithmetic
	5. fractions — Rational numbers
	6. random — Generate pseudo-random numbers
	7. itertools — Functions creating iterators for efficient looping
	8. functools — Higher-order functions and operations on callable objects
	9. operator — Standard operators as functions
10. [File and Directory Access](https://docs.python.org/2/library/filesys.html)
	1. os.path — Common pathname manipulations
	2. fileinput — Iterate over lines from multiple input streams
	3. stat — Interpreting stat() results
	4. statvfs — Constants used with os.statvfs()
	5. filecmp — File and Directory Comparisons
	6. tempfile — Generate temporary files and directories
	7. glob — Unix style pathname pattern expansion
	8. fnmatch — Unix filename pattern matching
	9. linecache — Random access to text lines
	10. shutil — High-level file operations
	11. dircache — Cached directory listings
	12. macpath — Mac OS 9 path manipulation functions
11. [Data Persistence](https://docs.python.org/2/library/persistence.html)
	1. pickle — Python object serialization
	2. cPickle — A faster pickle
	3. copy_reg — Register pickle support functions
	4. shelve — Python object persistence
	5. marshal — Internal Python object serialization
	6. anydbm — Generic access to DBM-style databases
	7. whichdb — Guess which DBM module created a database
	8. dbm — Simple “database” interface
	9. gdbm — GNU’s reinterpretation of dbm
	10. dbhash — DBM-style interface to the BSD database library
	11. bsddb — Interface to Berkeley DB library
	12. dumbdbm — Portable DBM implementation
	13. sqlite3 — DB-API 2.0 interface for SQLite databases
12. [Data Compression and Archiving](https://docs.python.org/2/library/archiving.html)
	1. zlib — Compression compatible with gzip
	2. gzip — Support for gzip files
	3. bz2 — Compression compatible with bzip2
	4. zipfile — Work with ZIP archives
	5. tarfile — Read and write tar archive files
13. [File Formats](https://docs.python.org/2/library/fileformats.html)
	1. csv — CSV File Reading and Writing
	2. ConfigParser — Configuration file parser
	3. robotparser — Parser for robots.txt
	4. netrc — netrc file processing
	5. xdrlib — Encode and decode XDR data
	6. plistlib — Generate and parse Mac OS X .plist files
14. [Cryptographic Services](https://docs.python.org/2/library/crypto.html)
	1. hashlib — Secure hashes and message digests
	2. hmac — Keyed-Hashing for Message Authentication
	3. md5 — MD5 message digest algorithm
	4. sha — SHA-1 message digest algorithm
15. [Generic Operating System Services](https://docs.python.org/2/library/allos.html)
	1. os — Miscellaneous operating system interfaces
	2. io — Core tools for working with streams
	3. time — Time access and conversions
	4. argparse — Parser for command-line options, arguments and sub-commands
	5. optparse — Parser for command line options
	6. getopt — C-style parser for command line options
	7. logging — Logging facility for Python
	8. logging.config — Logging configuration
	9. logging.handlers — Logging handlers
	10. getpass — Portable password input
	11. curses — Terminal handling for character-cell displays
	12. curses.textpad — Text input widget for curses programs
	13. curses.ascii — Utilities for ASCII characters
	14. curses.panel — A panel stack extension for curses
	15. platform — Access to underlying platform’s identifying data
	16. errno — Standard errno system symbols
	17. ctypes — A foreign function library for Python
16. [Optional Operating System Services](https://docs.python.org/2/library/someos.html)
	1. select — Waiting for I/O completion
	2. threading — Higher-level threading interface
	3. thread — Multiple threads of control
	4. dummy_threading — Drop-in replacement for the threading module
	5. dummy_thread — Drop-in replacement for the thread module
	6. multiprocessing — Process-based “threading” interface
	7. mmap — Memory-mapped file support
	8. readline — GNU readline interface
	9. rlcompleter — Completion function for GNU readline
17. [Interprocess Communication and Networking](https://docs.python.org/2/library/ipc.html)
	1. subprocess — Subprocess management
	2. socket — Low-level networking interface
	3. ssl — TLS/SSL wrapper for socket objects
	4. signal — Set handlers for asynchronous events
	5. popen2 — Subprocesses with accessible I/O streams
	6. asyncore — Asynchronous socket handler
	7. asynchat — Asynchronous socket command/response handler
18. [Internet Data Handling](https://docs.python.org/2/library/netdata.html)
	1. email — An email and MIME handling package
	2. json — JSON encoder and decoder
	3. mailcap — Mailcap file handling
	4. mailbox — Manipulate mailboxes in various formats
	5. mhlib — Access to MH mailboxes
	6. mimetools — Tools for parsing MIME messages
	7. mimetypes — Map filenames to MIME types
	8. MimeWriter — Generic MIME file writer
	9. mimify — MIME processing of mail messages
	10. multifile — Support for files containing distinct parts
	11. rfc822 — Parse RFC 2822 mail headers
	12. base64 — RFC 3548: Base16, Base32, Base64 Data Encodings
	13. binhex — Encode and decode binhex4 files
	14. binascii — Convert between binary and ASCII
	15. quopri — Encode and decode MIME quoted-printable data
	16. uu — Encode and decode uuencode files
19. [Structured Markup Processing Tools](https://docs.python.org/2/library/markup.html)
	1. HTMLParser — Simple HTML and XHTML parser
	2. sgmllib — Simple SGML parser
	3. htmllib — A parser for HTML documents
	4. htmlentitydefs — Definitions of HTML general entities
	5. XML Processing Modules
	6. XML vulnerabilities
	7. xml.etree.ElementTree — The ElementTree XML API
	8. xml.dom — The Document Object Model API
	9. xml.dom.minidom — Minimal DOM implementation
	10. xml.dom.pulldom — Support for building partial DOM trees
	11. xml.sax — Support for SAX2 parsers
	12. xml.sax.handler — Base classes for SAX handlers
	13. xml.sax.saxutils — SAX Utilities
	14. xml.sax.xmlreader — Interface for XML parsers
	15. xml.parsers.expat — Fast XML parsing using Expat
20. [Internet Protocols and Support](https://docs.python.org/2/library/internet.html)
	1. webbrowser — Convenient Web-browser controller
	2. cgi — Common Gateway Interface support
	3. cgitb — Traceback manager for CGI scripts
	4. wsgiref — WSGI Utilities and Reference Implementation
	5. urllib — Open arbitrary resources by URL
	6. urllib2 — extensible library for opening URLs
	7. httplib — HTTP protocol client
	8. ftplib — FTP protocol client
	9. poplib — POP3 protocol client
	10. imaplib — IMAP4 protocol client
	11. nntplib — NNTP protocol client
	12. smtplib — SMTP protocol client
	13. smtpd — SMTP Server
	14. telnetlib — Telnet client
	15. uuid — UUID objects according to RFC 4122
	16. urlparse — Parse URLs into components
	17. SocketServer — A framework for network servers
	18. BaseHTTPServer — Basic HTTP server
	19. SimpleHTTPServer — Simple HTTP request handler
	20. CGIHTTPServer — CGI-capable HTTP request handler
	21. cookielib — Cookie handling for HTTP clients
	22. Cookie — HTTP state management
	23. xmlrpclib — XML-RPC client access
	24. SimpleXMLRPCServer — Basic XML-RPC server
	25. DocXMLRPCServer — Self-documenting XML-RPC server
21. [Multimedia Services](https://docs.python.org/2/library/mm.html)
	1. audioop — Manipulate raw audio data
	2. imageop — Manipulate raw image data
	3. aifc — Read and write AIFF and AIFC files
	4. sunau — Read and write Sun AU files
	5. wave — Read and write WAV files
	6. chunk — Read IFF chunked data
	7. colorsys — Conversions between color systems
	8. imghdr — Determine the type of an image
	9. sndhdr — Determine type of sound file
	10. ossaudiodev — Access to OSS-compatible audio devices
22. [Internationalization](https://docs.python.org/2/library/i18n.html)
	1. gettext — Multilingual internationalization services
	2. locale — Internationalization services
23. [Program Frameworks](https://docs.python.org/2/library/frameworks.html)
	1. cmd — Support for line-oriented command interpreters
	2. shlex — Simple lexical analysis
24. [Graphical User Interfaces with Tk](https://docs.python.org/2/library/tk.html)
	1. Tkinter — Python interface to Tcl/Tk
	2. ttk — Tk themed widgets
	3. Tix — Extension widgets for Tk
	4. ScrolledText — Scrolled Text Widget
	5. turtle — Turtle graphics for Tk
	6. IDLE
	7. Other Graphical User Interface Packages
25. [Development Tools](https://docs.python.org/2/library/development.html)
	1. pydoc — Documentation generator and online help system
	2. doctest — Test interactive Python examples
	3. unittest — Unit testing framework
	4. 2to3 - Automated Python 2 to 3 code translation
	5. test — Regression tests package for Python
	6. test.test_support — Utility functions for tests
26. [Debugging and Profiling](https://docs.python.org/2/library/debug.html)
	1. bdb — Debugger framework
	2. pdb — The Python Debugger
	3. Debugger Commands
	4. The Python Profilers
	5. hotshot — High performance logging profiler
	6. timeit — Measure execution time of small code snippets
	7. trace — Trace or track Python statement execution
27. [Software Packaging and Distribution](https://docs.python.org/2/library/distribution.html)
	1. distutils — Building and installing Python modules
	2. ensurepip — Bootstrapping the pip installer
28. [Python Runtime Services](https://docs.python.org/2/library/python.html)
	1. sys — System-specific parameters and functions
	2. sysconfig — Provide access to Python’s configuration information
	3. \_\_builtin\_\_ — Built-in objects
	4. future_builtins — Python 3 builtins
	5. \_\_main\_\_ — Top-level script environment
	6. warnings — Warning control
	7. contextlib — Utilities for with-statement contexts
	8. abc — Abstract Base Classes
	9. atexit — Exit handlers
	10. traceback — Print or retrieve a stack traceback
	11. \_\_future\_\_ — Future statement definitions
	12. gc — Garbage Collector interface
	13. inspect — Inspect live objects
	14. site — Site-specific configuration hook
	15. user — User-specific configuration hook
	16. fpectl — Floating point exception control
29. [Custom Python Interpreters](https://docs.python.org/2/library/custominterp.html)
	1. code — Interpreter base classes
	2. codeop — Compile Python code
30. [Restricted Execution](https://docs.python.org/2/library/restricted.html)
	1. rexec — Restricted execution framework
	2. Bastion — Restricting access to objects
31. [Importing Modules](https://docs.python.org/2/library/modules.html)
	1. imp — Access the import internals
	2. importlib – Convenience wrappers for \_\_import\_\_()
	3. imputil — Import utilities
	4. zipimport — Import modules from Zip archives
	5. pkgutil — Package extension utility
	6. modulefinder — Find modules used by a script
	7. runpy — Locating and executing Python modules
32. [Python Language Services](https://docs.python.org/2/library/language.html)
	1. parser — Access Python parse trees
	2. ast — Abstract Syntax Trees
	3. symtable — Access to the compiler’s symbol tables
	4. symbol — Constants used with Python parse trees
	5. token — Constants used with Python parse trees
	6. keyword — Testing for Python keywords
	7. tokenize — Tokenizer for Python source
	8. tabnanny — Detection of ambiguous indentation
	9. pyclbr — Python class browser support
	10. py_compile — Compile Python source files
	11. compileall — Byte-compile Python libraries
	12. dis — Disassembler for Python bytecode
	13. pickletools — Tools for pickle developers
33. [Python compiler package](https://docs.python.org/2/library/compiler.html)
	1. The basic interface
	2. Limitations
	3. Python Abstract Syntax
	4. Using Visitors to Walk ASTs
	5. Bytecode Generation
34. [Miscellaneous Services](https://docs.python.org/2/library/misc.html)
	1. formatter — Generic output formatting
35. [MS Windows Specific Services](https://docs.python.org/2/library/windows.html)
	1. msilib — Read and write Microsoft Installer files
	2. msvcrt – Useful routines from the MS VC++ runtime
	3. _winreg – Windows registry access
	4. winsound — Sound-playing interface for Windows
36. [Unix Specific Services](https://docs.python.org/2/library/unix.html)
	1. posix — The most common POSIX system calls
	2. pwd — The password database
	3. spwd — The shadow password database
	4. grp — The group database
	5. crypt — Function to check Unix passwords
	6. dl — Call C functions in shared objects
	7. termios — POSIX style tty control
	8. tty — Terminal control functions
	9. pty — Pseudo-terminal utilities
	10. fcntl — The fcntl and ioctl system calls
	11. pipes — Interface to shell pipelines
	12. posixfile — File-like objects with locking support
	13. resource — Resource usage information
	14. nis — Interface to Sun’s NIS (Yellow Pages)
	15. syslog — Unix syslog library routines
	16. commands — Utilities for running commands
37. [Mac OS X specific services](https://docs.python.org/2/library/mac.html)
	1. ic — Access to the Mac OS X Internet Config
	2. MacOS — Access to Mac OS interpreter features
	3. macostools — Convenience routines for file manipulation
	4. findertools — The finder‘s Apple Events interface
	5. EasyDialogs — Basic Macintosh dialogs
	6. FrameWork — Interactive application framework
	7. autoGIL — Global Interpreter Lock handling in event loops
	8. Mac OS Toolbox Modules
	9. ColorPicker — Color selection dialog
38. [MacPython OSA Modules](https://docs.python.org/2/library/macosa.html)
	1. gensuitemodule — Generate OSA stub packages
	2. aetools — OSA client support
	3. aepack — Conversion between Python variables and AppleEvent data containers
	4. aetypes — AppleEvent objects
	5. MiniAEFrame — Open Scripting Architecture server support
39. [SGI IRIX Specific Services](https://docs.python.org/2/library/sgi.html)
	1. al — Audio functions on the SGI
	2. AL — Constants used with the al module
	3. cd — CD-ROM access on SGI systems
	4. fl — FORMS library for graphical user interfaces
	5. FL — Constants used with the fl module
	6. flp — Functions for loading stored FORMS designs
	7. fm — Font Manager interface
	8. gl — Graphics Library interface
	9. DEVICE — Constants used with the gl module
	10. GL — Constants used with the gl module
	11. imgfile — Support for SGI imglib files
	12. jpeg — Read and write JPEG files
40. [SunOS Specific Services](https://docs.python.org/2/library/sun.html)
	1. sunaudiodev — Access to Sun audio hardware
	2. SUNAUDIODEV — Constants used with sunaudiodev
41. [Undocumented Modules](https://docs.python.org/2/library/undoc.html)
	1. Miscellaneous useful utilities
	2. Platform specific modules
	3. Multimedia
	4. Undocumented Mac OS modules
	5. Obsolete
	6. SGI-specific Extension modules


## 2. Built-in Functions {#BuildInFunc}
The Python interpreter has a number of functions built into it that are always available. They are listed here in alphabetical order.

Built-in Functions		

abs()		|	divmod()	|	input()			|	open()		|	staticmethod()
all()		|	enumerate()	|	int()			|	ord()		|	str()
any()		|	eval()		|	isinstance()	|	pow()		|	sum()
basestring()|	execfile()	|	issubclass()	|	print()		|	super()
bin()		| 	file()		|	iter()			|	property()	|	tuple()
bool()		| 	filter()	|	len()			|	range()		|	type()
bytearray()	|	float()		|	list()			|	raw_input()	|	unichr()
callable()	|	format()	|	locals()		|	reduce()	|	unicode()
chr()		|	frozenset()	|	long()			|	reload()	|	vars()
classmethod()|	getattr()	|	map()			|	repr()		|	xrange()
cmp()		|	globals()	|	max()			|	reversed()	|	zip()
compile()	|	hasattr()	|	memoryview()	|	round()		|	\_\_import\_\_()
complex()	|	hash()		|	min()			|	set()	
delattr()	|	help()		|	next()			|	setattr()	
dict()		|	hex()		|	object()		|	slice()	
dir()		|	id()		|	oct()			|	sorted()

In addition, there are other four built-in functions that are no longer considered essential: apply(), buffer(), coerce(), and intern(). They are documented in the Non-essential Built-in Functions section.

#### abs(x)
Return the absolute value of a number. The argument may be a plain or long integer or a floating point number. If the argument is a complex number, its magnitude is returned.

#### all(iterable)
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

~~~python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
~~~
New in version 2.5.

#### any(iterable)
Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

~~~python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
~~~
New in version 2.5.

#### basestring()
This abstract type is the superclass for str and unicode. It cannot be called or instantiated, but it can be used to test whether an object is an instance of str or unicode. isinstance(obj, basestring) is equivalent to isinstance(obj, (str, unicode)).

New in version 2.3.

#### bin(x)
Convert an integer number to a binary string. The result is a valid Python expression. If x is not a Python int object, it has to define an \_\_index\_\_() method that returns an integer.

New in version 2.6.

#### class bool([x])
Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise it returns True. bool is also a class, which is a subclass of int. Class bool cannot be subclassed further. Its only instances are False and True.

New in version 2.2.1.

Changed in version 2.3: If no argument is given, this function returns False.

#### class bytearray([source[, encoding[, errors]]])
Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods that the str type has, see String Methods.

The optional source parameter can be used to initialize the array in a few different ways:

If it is unicode, you must also give the encoding (and optionally, errors) parameters; bytearray() then converts the unicode to bytes using unicode.encode().

If it is an integer, the array will have that size and will be initialized with null bytes.

If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.

If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial contents of the array.

Without an argument, an array of size 0 is created.

New in version 2.6.

#### callable(object)
Return True if the object argument appears callable, False if not. If this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); class instances are callable if they have a \_\_call\_\_() method.

#### chr(i)
Return a string of one character whose ASCII code is the integer i. For example, chr(97) returns the string 'a'. This is the inverse of ord(). The argument must be in the range [0..255], inclusive; ValueError will be raised if i is outside that range. See also unichr().

#### classmethod(function)
Return a class method for function.

A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:

~~~python
class C(object):
    @classmethod
    def f(cls, arg1, arg2, ...):
        ...
~~~
The @classmethod form is a function decorator – see the description of function definitions in Function definitions for details.

It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is passed as the implied first argument.

Class methods are different than C++ or Java static methods. If you want those, see staticmethod() in this section.

For more information on class methods, consult the documentation on the standard type hierarchy in The standard type hierarchy.

New in version 2.2.

Changed in version 2.4: Function decorator syntax added.

#### cmp(x, y)
Compare the two objects x and y and return an integer according to the outcome. The return value is negative if x < y, zero if x == y and strictly positive if x > y.

#### compile(source, filename, mode[, flags[, dont_inherit]])
Compile the source into a code or AST object. Code objects can be executed by an exec statement or evaluated by a call to eval(). source can either be a Unicode string, a Latin-1 encoded string or an AST object. Refer to the ast module documentation for information on how to work with AST objects.

The filename argument should give the file from which the code was read; pass some recognizable value if it wasn’t read from a file ('<string>' is commonly used).

The mode argument specifies what kind of code must be compiled; it can be 'exec' if source consists of a sequence of statements, 'eval' if it consists of a single expression, or 'single' if it consists of a single interactive statement (in the latter case, expression statements that evaluate to something other than None will be printed).

The optional arguments flags and dont\_inherit control which future statements (see PEP 236) affect the compilation of source. If neither is present (or both are zero) the code is compiled with those future statements that are in effect in the code that is calling compile(). If the flags argument is given and dont\_inherit is not (or is zero) then the future statements specified by the flags argument are used in addition to those that would be used anyway. If dont\_inherit is a non-zero integer then the flags argument is it – the future statements in effect around the call to compile are ignored.

Future statements are specified by bits which can be bitwise ORed together to specify multiple statements. The bitfield required to specify a given feature can be found as the compiler_flag attribute on the _Feature instance in the \_\_future\_\_ module.

This function raises SyntaxError if the compiled source is invalid, and TypeError if the source contains null bytes.

If you want to parse Python code into its AST representation, see ast.parse().

Note When compiling a string with multi-line code in 'single' or 'eval' mode, input must be terminated by at least one newline character. This is to facilitate detection of incomplete and complete statements in the code module.

Changed in version 2.3: The flags and dont_inherit arguments were added.

Changed in version 2.6: Support for compiling AST objects.

Changed in version 2.7: Allowed use of Windows and Mac newlines. Also input in 'exec' mode does not have to end in a newline anymore.

#### class complex([real[, imag]])
Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the function serves as a numeric conversion function like int(), long() and float(). If both arguments are omitted, returns 0j.

Note When converting from a string, the string must not contain whitespace around the central + or - operator. For example, complex('1+2j') is fine, but complex('1 + 2j') raises ValueError.
The complex type is described in Numeric Types — int, float, long, complex.

#### delattr(object, name)
This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.

#### class dict(**kwarg); class dict(mapping, **kwarg); lass dict(iterable, **kwarg)
Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types — dict for documentation about this class.

For other containers see the built-in list, set, and tuple classes, as well as the collections module.

#### dir([object])
Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

If the object has a method named \_\_dir\_\_(), this method will be called and must return the list of attributes. This allows objects that implement a custom \_\_getattr\_\_() or \_\_getattribute\_\_() function to customize the way dir() reports their attributes.

If the object does not provide \_\_dir\_\_(), the function tries its best to gather information from the object’s \_\_dict\_\_ attribute, if defined, and from its type object. The resulting list is not necessarily complete, and may be inaccurate when the object has a custom \_\_getattr\_\_().

The default dir() mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:

If the object is a module object, the list contains the names of the module’s attributes.

If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.

Otherwise, the list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.
The resulting list is sorted alphabetically. For example:

~~~python
>>>
>>> import struct
>>> dir()   # show the names in the module namespace
['__builtins__', '__doc__', '__name__', 'struct']
>>> dir(struct)   # show the names in the struct module
['Struct', '__builtins__', '__doc__', '__file__', '__name__',
 '__package__', '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
>>> class Shape(object):
        def __dir__(self):
            return ['area', 'perimeter', 'location']
>>> s = Shape()
>>> dir(s)
['area', 'perimeter', 'location']
~~~

Note Because dir() is supplied primarily as a convenience for use at an interactive prompt, it tries to supply an interesting set of names more than it tries to supply a rigorously or consistently defined set of names, and its detailed behavior may change across releases. For example, metaclass attributes are not in the result list when the argument is a class.

#### divmod(a, b)
Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using long division. With mixed operand types, the rules for binary arithmetic operators apply. For plain and long integers, the result is the same as `(a // b, a % b)`. For floating point numbers the result is `(q, a % b)`, where q is usually math.floor(a / b) but may be 1 less than that. In any case `q * b + a % b` is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).

Changed in version 2.3: Using divmod() with complex numbers is deprecated.

#### enumerate(sequence, start=0)
Return an enumerate object. sequence must be a sequence, an iterator, or some other object which supports iteration. The next() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over sequence:

~~~python
>>>
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
# Equivalent to:

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
~~~
New in version 2.3.

Changed in version 2.6: The start parameter was added.

#### eval(expression[, globals[, locals]])
The arguments are a Unicode or Latin-1 encoded string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.

Changed in version 2.4: formerly locals was required to be a dictionary.

The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace. If the globals dictionary is present and lacks ‘\_\_builtins\_\_’, the current globals are copied into globals before expression is parsed. This means that expression normally has full access to the standard \_\_builtin\_\_ module and restricted environments are propagated. If the locals dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is executed in the environment where eval() is called. The return value is the result of the evaluated expression. Syntax errors are reported as exceptions. Example:

~~~python
>>>
>>> x = 1
>>> print eval('x+1')
2
~~~
This function can also be used to execute arbitrary code objects (such as those created by compile()). In this case pass a code object instead of a string. If the code object has been compiled with 'exec' as the mode argument, eval()‘s return value will be None.

Hints: dynamic execution of statements is supported by the exec statement. Execution of statements from a file is supported by the execfile() function. The globals() and locals() functions returns the current global and local dictionary, respectively, which may be useful to pass around for use by eval() or execfile().

See ast.literal_eval() for a function that can safely evaluate strings with expressions containing only literals.

#### execfile(filename[, globals[, locals]])
This function is similar to the exec statement, but parses a file instead of a string. It is different from the import statement in that it does not use the module administration — it reads the file unconditionally and does not create a new module. [1]

The arguments are a file name and two optional dictionaries. The file is parsed and evaluated as a sequence of Python statements (similarly to a module) using the globals and locals dictionaries as global and local namespace. If provided, locals can be any mapping object. Remember that at module level, globals and locals are the same dictionary. If two separate objects are passed as globals and locals, the code will be executed as if it were embedded in a class definition.

Changed in version 2.4: formerly locals was required to be a dictionary.

If the locals dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is executed in the environment where execfile() is called. The return value is None.

Note The default locals act as described for function locals() below: modifications to the default locals dictionary should not be attempted. Pass an explicit locals dictionary if you need to see effects of the code on locals after function execfile() returns. execfile() cannot be used reliably to modify a function’s locals.
file(name[, mode[, buffering]])
Constructor function for the file type, described further in section File Objects. The constructor’s arguments are the same as those of the open() built-in function described below.

When opening a file, it’s preferable to use open() instead of invoking this constructor directly. file is more suited to type testing (for example, writing isinstance(f, file)).

New in version 2.2.

#### filter(function, iterable)
Construct a list from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If iterable is a string or a tuple, the result also has that type; otherwise it is always a list. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.

Note that filter(function, iterable) is equivalent to [item for item in iterable if function(item)] if function is not None and [item for item in iterable if item] if function is None.

See itertools.ifilter() and itertools.ifilterfalse() for iterator versions of this function, including a variation that filters for elements where the function returns false.

#### class float([x])
Return a floating point number constructed from a number or string x.

If the argument is a string, it must contain a possibly signed decimal or floating point number, possibly embedded in whitespace. The argument may also be [+\|-]nan or [+\|-]inf. Otherwise, the argument may be a plain or long integer or a floating point number, and a floating point number with the same value (within Python’s floating point precision) is returned. If no argument is given, returns 0.0.

Note When passing in a string, values for NaN and Infinity may be returned, depending on the underlying C library. Float accepts the strings nan, inf and -inf for NaN and positive or negative infinity. The case and a leading + are ignored as well as a leading - is ignored for NaN. Float always represents NaN and infinity as nan, inf or -inf.

The float type is described in Numeric Types — int, float, long, complex.

#### format(value[, format_spec])
Convert a value to a “formatted” representation, as controlled by format\_spec. The interpretation of format\_spec will depend on the type of the value argument, however there is a standard formatting syntax that is used by most built-in types: Format Specification Mini-Language.

Note format(value, format\_spec) merely calls value.\_\_format\_\_(format\_spec).
New in version 2.6.

#### class frozenset([iterable])
Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class. See frozenset and Set Types — set, frozenset for documentation about this class.

For other containers see the built-in set, list, tuple, and dict classes, as well as the collections module.

New in version 2.4.

#### getattr(object, name[, default])
Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.

#### globals()
Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

#### hasattr(object, name)
The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an exception or not.)

#### hash(object)
Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).

#### help([object])
Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated.

This function is added to the built-in namespace by the site module.

New in version 2.2.

#### hex(x)
Convert an integer number (of any size) to a lowercase hexadecimal string prefixed with “0x”, for example:

~~~python
>>>
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
>>> hex(1L)
'0x1L'
~~~
If x is not a Python int or long object, it has to define an \_\_index\_\_() method that returns an integer.

See also int() for converting a hexadecimal string to an integer using a base of 16.

Note To obtain a hexadecimal string representation for a float, use the float.hex() method.
Changed in version 2.4: Formerly only returned an unsigned literal.

#### id(object)
Return the “identity” of an object. This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

CPython implementation detail: This is the address of the object in memory.

#### input([prompt])
Equivalent to eval(raw_input(prompt)).

This function does not catch user errors. If the input is not syntactically valid, a SyntaxError will be raised. Other exceptions may be raised if there is an error during evaluation.

If the readline module was loaded, then input() will use it to provide elaborate line editing and history features.

Consider using the raw_input() function for general input from users.

#### class int(x=0); class int(x, base=10)
Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x is a number, it can be a plain integer, a long integer, or a floating point number. If x is floating point, the conversion truncates towards zero. If the argument is outside the integer range, the function returns a long object instead.

If x is not a number or if base is given, then x must be a string or Unicode object representing an integer literal in radix base. Optionally, the literal can be preceded by + or - (with no space in between) and surrounded by whitespace. A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 10 to 35. The default base is 10. The allowed values are 0 and 2-36. Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O/0, or 0x/0X, as with integer literals in code. Base 0 means to interpret the string exactly as an integer literal, so that the actual base is 2, 8, 10, or 16.

The integer type is described in Numeric Types — int, float, long, complex.

#### isinstance(object, classinfo)
Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. Also return true if classinfo is a type object (new-style class) and object is an object of that type or of a (direct, indirect or virtual) subclass thereof. If object is not a class instance or an object of the given type, the function always returns false. If classinfo is a tuple of class or type objects (or recursively, other such tuples), return true if object is an instance of any of the classes or types. If classinfo is not a class, type, or tuple of classes, types, and such tuples, a TypeError exception is raised.

Changed in version 2.2: Support for a tuple of type information was added.

#### issubclass(class, classinfo)
Return true if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked. In any other case, a TypeError exception is raised.

Changed in version 2.3: Support for a tuple of type information was added.

#### iter(o[, sentinel])
Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, o must be a collection object which supports the iteration protocol (the \_\_iter\_\_() method), or it must support the sequence protocol (the \_\_getitem\_\_() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then o must be a callable object. The iterator created in this case will call o with no arguments for each call to its next() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.

One useful application of the second form of iter() is to read lines of a file until a certain line is reached. The following example reads a file until the readline() method returns an empty string:

~~~python
with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)
~~~
New in version 2.2.

#### len(s)
Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

#### class list([iterable])
Return a list whose items are the same and in the same order as iterable‘s items. iterable may be either a sequence, a container that supports iteration, or an iterator object. If iterable is already a list, a copy is made and returned, similar to iterable[:]. For instance, list('abc') returns ['a', 'b', 'c'] and list( (1, 2, 3) ) returns [1, 2, 3]. If no argument is given, returns a new empty list, [].

list is a mutable sequence type, as documented in Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange. For other containers see the built in dict, set, and tuple classes, and the collections module.

#### locals()
Update and return a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks.

Note The contents of this dictionary should not be modified; changes may not affect the values of local and free variables used by the interpreter.

#### class long(x=0); class long(x, base=10)
Return a long integer object constructed from a string or number x. If the argument is a string, it must contain a possibly signed number of arbitrary size, possibly embedded in whitespace. The base argument is interpreted in the same way as for int(), and may only be given when x is a string. Otherwise, the argument may be a plain or long integer or a floating point number, and a long integer with the same value is returned. Conversion of floating point numbers to integers truncates (towards zero). If no arguments are given, returns 0L.

The long type is described in Numeric Types — int, float, long, complex.

#### map(function, iterable, ...)
Apply function to every item of iterable and return a list of the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. If one iterable is shorter than another it is assumed to be extended with None items. If function is None, the identity function is assumed; if there are multiple arguments, map() returns a list consisting of tuples containing the corresponding items from all iterables (a kind of transpose operation). The iterable arguments may be a sequence or any iterable object; the result is always a list.

#### max(iterable[, key]); max(arg1, arg2, *args[, key])
Return the largest item in an iterable or the largest of two or more arguments.

If one positional argument is provided, iterable must be a non-empty iterable (such as a non-empty string, tuple or list). The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.

The optional key argument specifies a one-argument ordering function like that used for list.sort(). The key argument, if supplied, must be in keyword form (for example, max(a,b,c,key=func)).

Changed in version 2.5: Added support for the optional key argument.

#### memoryview(obj)
Return a “memory view” object created from the given argument. See memoryview type for more information.

#### min(iterable[, key]); min(arg1, arg2, *args[, key])
Return the smallest item in an iterable or the smallest of two or more arguments.

If one positional argument is provided, iterable must be a non-empty iterable (such as a non-empty string, tuple or list). The smallest item in the iterable is returned. If two or more positional arguments are provided, the smallest of the positional arguments is returned.

The optional key argument specifies a one-argument ordering function like that used for list.sort(). The key argument, if supplied, must be in keyword form (for example, min(a,b,c,key=func)).

Changed in version 2.5: Added support for the optional key argument.

#### next(iterator[, default])
Retrieve the next item from the iterator by calling its next() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

New in version 2.6.

#### class object
Return a new featureless object. object is a base for all new style classes. It has the methods that are common to all instances of new style classes.

New in version 2.2.

Changed in version 2.3: This function does not accept any arguments. Formerly, it accepted arguments but ignored them.

#### oct(x)
Convert an integer number (of any size) to an octal string. The result is a valid Python expression.

Changed in version 2.4: Formerly only returned an unsigned literal.

#### open(name[, mode[, buffering]])
Open a file, returning an object of the file type described in section File Objects. If the file cannot be opened, IOError is raised. When opening a file, it’s preferable to use open() instead of invoking the file constructor directly.

The first two arguments are the same as for stdio‘s fopen(): name is the file name to be opened, and mode is a string indicating how the file is to be opened.

The most commonly-used values of mode are 'r' for reading, 'w' for writing (truncating the file if it already exists), and 'a' for appending (which on some Unix systems means that all writes append to the end of the file regardless of the current seek position). If mode is omitted, it defaults to 'r'. The default is to use text mode, which may convert '\n' characters to a platform-specific representation on writing and back on reading. Thus, when opening a binary file, you should append 'b' to the mode value to open the file in binary mode, which will improve portability. (Appending 'b' is useful even on systems that don’t treat binary and text files differently, where it serves as documentation.) See below for more possible values of mode.

The optional buffering argument specifies the file’s desired buffer size: 0 means unbuffered, 1 means line buffered, any other positive value means use a buffer of (approximately) that size (in bytes). A negative buffering means to use the system default, which is usually line buffered for tty devices and fully buffered for other files. If omitted, the system default is used. [2]

Modes 'r+', 'w+' and 'a+' open the file for updating (reading and writing); note that 'w+' truncates the file. Append 'b' to the mode to open the file in binary mode, on systems that differentiate between binary and text files; on systems that don’t have this distinction, adding the 'b' has no effect.

In addition to the standard fopen() values mode may be 'U' or 'rU'. Python is usually built with universal newlines support; supplying 'U' opens the file as a text file, but lines may be terminated by any of the following: the Unix end-of-line convention '\n', the Macintosh convention '\r', or the Windows convention '\r\n'. All of these external representations are seen as '\n' by the Python program. If Python is built without universal newlines support a mode with 'U' is the same as normal text mode. Note that file objects so opened also have an attribute called newlines which has a value of None (if no newlines have yet been seen), '\n', '\r', '\r\n', or a tuple containing all the newline types seen.

Python enforces that the mode, after stripping 'U', begins with 'r', 'w' or 'a'.

Python provides many file handling modules including fileinput, os, os.path, tempfile, and shutil.

Changed in version 2.5: Restriction on first letter of mode string introduced.

#### ord(c)
Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. For example, ord('a') returns the integer 97, ord(u'\u2020') returns 8224. This is the inverse of chr() for 8-bit strings and of unichr() for unicode objects. If a unicode argument is given and Python was built with UCS2 Unicode, then the character’s code point must be in the range [0..65535] inclusive; otherwise the string length is two, and a TypeError will be raised.

#### pow(x, y[, z])
Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than pow(x, y) % z). The two-argument form pow(x, y) is equivalent to using the power operator: x**y.

The arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators apply. For int and long int operands, the result has the same type as the operands (after coercion) unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, 10\*\*2 returns 100, but 10\*\*-2 returns 0.01. (This last feature was added in Python 2.2. In Python 2.1 and before, if both arguments were of integer types and the second argument was negative, an exception was raised.) If the second argument is negative, the third argument must be omitted. If z is present, x and y must be of integer types, and y must be non-negative. (This restriction was added in Python 2.2. In Python 2.1 and before, floating 3-argument pow() returned platform-dependent results depending on floating-point rounding accidents.)

#### print(*objects, sep=' ', end='\n', file=sys.stdout)
Print objects to the stream file, separated by sep and followed by end. sep, end and file, if present, must be given as keyword arguments.

All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.

The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Output buffering is determined by file. Use file.flush() to ensure, for instance, immediate appearance on a screen.

Note This function is not normally available as a built-in since the name print is recognized as the print statement. To disable the statement and use the print() function, use this future statement at the top of your module:

`from __future__ import print_function`{: .language-python}

New in version 2.6.

#### class property([fget[, fset[, fdel[, doc]]]])
Return a property attribute for new-style classes (classes that derive from object).

fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.

A typical use is to define a managed attribute x:

~~~python
class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
~~~
If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.

If given, doc will be the docstring of the property attribute. Otherwise, the property will copy fget‘s docstring (if it exists). This makes it possible to create read-only properties easily using property() as a decorator:

~~~python
class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage
~~~
The @property decorator turns the voltage() method into a “getter” for a read-only attribute with the same name, and it sets the docstring for voltage to “Get the current voltage.”

A property object has getter, setter, and deleter methods usable as decorators that create a copy of the property with the corresponding accessor function set to the decorated function. This is best explained with an example:

~~~python
class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
~~~

This code is exactly equivalent to the first example. Be sure to give the additional functions the same name as the original property (x in this case.)

The returned property object also has the attributes fget, fset, and fdel corresponding to the constructor arguments.

New in version 2.2.

Changed in version 2.5: Use fget‘s docstring if no doc given.

Changed in version 2.6: The getter, setter, and deleter attributes were added.

#### range(stop); range(start, stop[, step])
This is a versatile function to create lists containing arithmetic progressions. It is most often used in for loops. The arguments must be plain integers. If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0. The full form returns a list of plain integers `[start, start + step, start + 2 * step, ...]`{: .language-python}. If step is positive, the last element is the largest start + i * step less than stop; if step is negative, the last element is the smallest start + i * step greater than stop. step must not be zero (or else ValueError is raised). Example:

~~~python
>>>
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)
[0, 3, 6, 9]
>>> range(0, -10, -1)
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]
raw_input([prompt])
~~~
If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:

~~~python
>>>
>>> s = raw_input('--> ')
#--> Monty Python's Flying Circus
>>> s
"Monty Python's Flying Circus"
~~~
If the readline module was loaded, then raw_input() will use it to provide elaborate line editing and history features.

#### reduce(function, iterable[, initializer])
Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, `reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)`{: .language-python}. The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned. Roughly equivalent to:

~~~python
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value
~~~

#### reload(module)
Reload a previously imported module. The argument must be a module object, so it must have been successfully imported before. This is useful if you have edited the module source file using an external editor and want to try out the new version without leaving the Python interpreter. The return value is the module object (the same as the module argument).

When reload(module) is executed:

Python modules’ code is recompiled and the module-level code reexecuted, defining a new set of objects which are bound to names in the module’s dictionary. The init function of extension modules is not called a second time.

As with all other objects in Python the old objects are only reclaimed after their reference counts drop to zero.

The names in the module namespace are updated to point to any new or changed objects.
Other references to the old objects (such as names external to the module) are not rebound to refer to the new objects and must be updated in each namespace where they occur if that is desired.
There are a number of other caveats:

When a module is reloaded, its dictionary (containing the module’s global variables) is retained. Redefinitions of names will override the old definitions, so this is generally not a problem. If the new version of a module does not define a name that was defined by the old version, the old definition remains. This feature can be used to the module’s advantage if it maintains a global table or cache of objects — with a try statement it can test for the table’s presence and skip its initialization if desired:

~~~python
try:
    cache
except NameError:
    cache = {}
~~~
It is generally not very useful to reload built-in or dynamically loaded modules. Reloading sys, \_\_main\_\_, builtins and other key modules is not recommended. In many cases extension modules are not designed to be initialized more than once, and may fail in arbitrary ways when reloaded.

If a module imports objects from another module using from ... import ..., calling reload() for the other module does not redefine the objects imported from it — one way around this is to re-execute the from statement, another is to use import and qualified names (module.\*name\*) instead.

If a module instantiates instances of a class, reloading the module that defines the class does not affect the method definitions of the instances — they continue to use the old class definition. The same is true for derived classes.

#### repr(object)
Return a string containing a printable representation of an object. This is the same value yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operation as an ordinary function. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a \_\_repr\_\_() method.

#### reversed(seq)
Return a reverse iterator. seq must be an object which has a \_\_reversed\_\_() method or supports the sequence protocol (the \_\_len\_\_() method and the \_\_getitem\_\_() method with integer arguments starting at 0).

New in version 2.4.

Changed in version 2.6: Added the possibility to write a custom \_\_reversed\_\_() method.

#### round(number[, ndigits])
Return the floating point value number rounded to ndigits digits after the decimal point. If ndigits is omitted, it defaults to zero. The result is a floating point number. Values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done away from 0 (so, for example, round(0.5) is 1.0 and round(-0.5) is -1.0).

Note The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See Floating Point Arithmetic: Issues and Limitations for more information.
class set([iterable])
Return a new set object, optionally with elements taken from iterable. set is a built-in class. See set and Set Types — set, frozenset for documentation about this class.

For other containers see the built-in frozenset, list, tuple, and dict classes, as well as the collections module.

New in version 2.4.

#### setattr(object, name, value)
This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.

#### class slice(stop); class slice(start, stop[, step])
Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). They have no other explicit functionality; however they are used by Numerical Python and other third party extensions. Slice objects are also generated when extended indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i]. See itertools.islice() for an alternate version that returns an iterator.

#### sorted(iterable[, cmp[, key[, reverse]]])
Return a new sorted list from the items in iterable.

The optional arguments cmp, key, and reverse have the same meaning as those for the list.sort() method (described in section Mutable Sequence Types).

cmp specifies a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument: cmp=lambda x,y: cmp(x.lower(), y.lower()). The default value is None.

key specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower. The default value is None (compare the elements directly).

reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

In general, the key and reverse conversion processes are much faster than specifying an equivalent cmp function. This is because cmp is called multiple times for each list element while key and reverse touch each element only once. Use functools.cmp\_to\_key() to convert an old-style cmp function to a key function.

The built-in sorted() function is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).

For sorting examples and a brief sorting tutorial, see Sorting HOW TO.

New in version 2.4.

#### staticmethod(function)
Return a static method for function.

A static method does not receive an implicit first argument. To declare a static method, use this idiom:

~~~python
class C(object):
    @staticmethod
    def f(arg1, arg2, ...):
        ...
~~~

The @staticmethod form is a function decorator – see the description of function definitions in Function definitions for details.

It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class.

Static methods in Python are similar to those found in Java or C++. Also see classmethod() for a variant that is useful for creating alternate class constructors.

For more information on static methods, consult the documentation on the standard type hierarchy in The standard type hierarchy.

New in version 2.2.

Changed in version 2.4: Function decorator syntax added.

#### class str(object='')
Return a string containing a nicely printable representation of an object. For strings, this returns the string itself. The difference with repr(object) is that str(object) does not always attempt to return a string that is acceptable to eval(); its goal is to return a printable string. If no argument is given, returns the empty string, ''.

For more information on strings see Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange which describes sequence functionality (strings are sequences), and also the string-specific methods described in the String Methods section. To output formatted strings use template strings or the % operator described in the String Formatting Operations section. In addition see the String Services section. See also unicode().

#### sum(iterable[, start])
Sums start and the items of an iterable from left to right and returns the total. start defaults to 0. The iterable‘s items are normally numbers, and the start value is not allowed to be a string.

For some use cases, there are good alternatives to sum(). The preferred, fast way to concatenate a sequence of strings is by calling ''.join(sequence). To add floating point values with extended precision, see math.fsum(). To concatenate a series of iterables, consider using itertools.chain().

New in version 2.3.

#### super(type[, object-or-type])
Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. The search order is same as that used by getattr() except that the type itself is skipped.

The \_\_mro\_\_ attribute of the type lists the method resolution search order used by both getattr() and super(). The attribute is dynamic and can change whenever the inheritance hierarchy is updated.

If the second argument is omitted, the super object returned is unbound. If the second argument is an object, isinstance(obj, type) must be true. If the second argument is a type, issubclass(type2, type) must be true (this is useful for classmethods).

Note super() only works for new-style classes.
There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages.

The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement the same method. Good design dictates that this method have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).

For both use cases, a typical superclass call looks like this:

~~~python
class C(B):
    def method(self, arg):
        super(C, self).method(arg)
~~~

Note that super() is implemented as part of the binding process for explicit dotted attribute lookups such as super().\_\_getitem\_\_(name). It does so by implementing its own \_\_getattribute\_\_() method for searching classes in a predictable order that supports cooperative multiple inheritance. Accordingly, super() is undefined for implicit lookups using statements or operators such as super()[name].

Also note that super() is not limited to use inside methods. The two argument form specifies the arguments exactly and makes the appropriate references.

For practical suggestions on how to design cooperative classes using super(), see guide to using super().

New in version 2.2.

#### tuple([iterable])
Return a tuple whose items are the same and in the same order as iterable‘s items. iterable may be a sequence, a container that supports iteration, or an iterator object. If iterable is already a tuple, it is returned unchanged. For instance, tuple('abc') returns ('a', 'b', 'c') and tuple([1, 2, 3]) returns (1, 2, 3). If no argument is given, returns a new empty tuple, ().

tuple is an immutable sequence type, as documented in Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange. For other containers see the built in dict, list, and set classes, and the collections module.

#### class type(object)
class type(name, bases, dict)
With one argument, return the type of an object. The return value is a type object. The isinstance() built-in function is recommended for testing the type of an object.

With three arguments, return a new type object. This is essentially a dynamic form of the class statement. The name string is the class name and becomes the \_\_name\_\_ attribute; the bases tuple itemizes the base classes and becomes the \_\_bases\_\_ attribute; and the dict dictionary is the namespace containing definitions for class body and becomes the \_\_dict\_\_ attribute. For example, the following two statements create identical type objects:

~~~python
>>>
>>> class X(object):
...     a = 1
...
>>> X = type('X', (object,), dict(a=1))
~~~
New in version 2.2.

#### unichr(i)
Return the Unicode string of one character whose Unicode code is the integer i. For example, unichr(97) returns the string u'a'. This is the inverse of ord() for Unicode strings. The valid range for the argument depends how Python was configured – it may be either UCS2 [0..0xFFFF] or UCS4 [0..0x10FFFF]. ValueError is raised otherwise. For ASCII and 8-bit strings see chr().

New in version 2.0.

#### unicode(object=''); unicode(object[, encoding[, errors]])
Return the Unicode string version of object using one of the following modes:

If encoding and/or errors are given, unicode() will decode the object which can either be an 8-bit string or a character buffer using the codec for encoding. The encoding parameter is a string giving the name of an encoding; if the encoding is not known, LookupError is raised. Error handling is done according to errors; this specifies the treatment of characters which are invalid in the input encoding. If errors is 'strict' (the default), a ValueError is raised on errors, while a value of 'ignore' causes errors to be silently ignored, and a value of 'replace' causes the official Unicode replacement character, U+FFFD, to be used to replace input characters which cannot be decoded. See also the codecs module.

If no optional parameters are given, unicode() will mimic the behaviour of str() except that it returns Unicode strings instead of 8-bit strings. More precisely, if object is a Unicode string or subclass it will return that Unicode string without any additional decoding applied.

For objects which provide a \_\_unicode\_\_() method, it will call this method without arguments to create a Unicode string. For all other objects, the 8-bit string version or representation is requested and then converted to a Unicode string using the codec for the default encoding in 'strict' mode.

For more information on Unicode strings see Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange which describes sequence functionality (Unicode strings are sequences), and also the string-specific methods described in the String Methods section. To output formatted strings use template strings or the % operator described in the String Formatting Operations section. In addition see the String Services section. See also str().

New in version 2.0.

Changed in version 2.2: Support for \_\_unicode\_\_() added.

#### vars([object])
Return the \_\_dict\_\_ attribute for a module, class, instance, or any other object with a \_\_dict\_\_ attribute.

Objects such as modules and instances have an updateable \_\_dict\_\_ attribute; however, other objects may have write restrictions on their \_\_dict\_\_ attributes (for example, new-style classes use a dictproxy to prevent direct dictionary updates).

Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored.

#### xrange(stop); xrange(start, stop[, step])
This function is very similar to range(), but returns an xrange object instead of a list. This is an opaque sequence type which yields the same values as the corresponding list, without actually storing them all simultaneously. The advantage of xrange() over range() is minimal (since xrange() still has to create the values when asked for them) except when a very large range is used on a memory-starved machine or when all of the range’s elements are never used (such as when the loop is usually terminated with break). For more information on xrange objects, see XRange Type and Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange.

CPython implementation detail: xrange() is intended to be simple and fast. Implementations may impose restrictions to achieve this. The C implementation of Python restricts all arguments to native C longs (“short” Python integers), and also requires that the number of elements fit in a native C long. If a larger range is needed, an alternate version can be crafted using the itertools module: islice(count(start, step), (stop-start+step-1+2*(step<0))//step).

#### zip([iterable, ...])
This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The returned list is truncated in length to the length of the shortest argument sequence. When there are multiple arguments which are all of the same length, zip() is similar to map() with an initial argument of None. With a single sequence argument, it returns a list of 1-tuples. With no arguments, it returns an empty list.

The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a data series into n-length groups using zip(*[iter(s)]*n).

zip() in conjunction with the * operator can be used to unzip a list:

~~~python
>>>
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zipped)
>>> x == list(x2) and y == list(y2)
True
~~~
New in version 2.0.

Changed in version 2.4: Formerly, zip() required at least one argument and zip() raised a TypeError instead of returning an empty list.

#### \_\_import\_\_(name[, globals[, locals[, fromlist[, level]]]])
Note This is an advanced function that is not needed in everyday Python programming, unlike importlib.import_module().

This function is invoked by the import statement. It can be replaced (by importing the \_\_builtin\_\_ module and assigning to \_\_builtin\_\_.\_\_import\_\_) in order to change semantics of the import statement, but nowadays it is usually simpler to use import hooks (see PEP 302). Direct use of \_\_import\_\_() is rare, except in cases where you want to import a module whose name is only known at runtime.

The function imports the module name, potentially using the given globals and locals to determine how to interpret the name in a package context. The fromlist gives the names of objects or submodules that should be imported from the module given by name. The standard implementation does not use its locals argument at all, and uses its globals only to determine the package context of the import statement.

level specifies whether to use absolute or relative imports. The default is -1 which indicates both absolute and relative imports will be attempted. 0 means only perform absolute imports. Positive values for level indicate the number of parent directories to search relative to the directory of the module calling \_\_import\_\_().

When the name variable is of the form package.module, normally, the top-level package (the name up till the first dot) is returned, not the module named by name. However, when a non-empty fromlist argument is given, the module named by name is returned.

For example, the statement import spam results in bytecode resembling the following code:

`spam = __import__('spam', globals(), locals(), [], -1)`{: .language-python}

The statement import spam.ham results in this call:

`spam = __import__('spam.ham', globals(), locals(), [], -1)`{: .language-python}

Note how \_\_import\_\_() returns the toplevel module here because this is the object that is bound to a name by the import statement.

On the other hand, the statement from spam.ham import eggs, sausage as saus results in

~~~python
_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], -1)
eggs = _temp.eggs
saus = _temp.sausage
~~~
Here, the spam.ham module is returned from \_\_import\_\_(). From this object, the names to import are retrieved and assigned to their respective names.

If you simply want to import a module (potentially within a package) by name, use `importlib.import_module()`.

Changed in version 2.5: The level parameter was added.

Changed in version 2.5: Keyword support for parameters was added.

## 3. Non-essential Built-in Functions {#non-essential-built-in-functions}
There are several built-in functions that are no longer essential to learn, know or use in modern Python programming. They have been kept here to maintain backwards compatibility with programs written for older versions of Python.

Python programmers, trainers, students and book writers should feel free to bypass these functions without concerns about missing something important.

#### apply(function, args[, keywords])
The function argument must be a callable object (a user-defined or built-in function or method, or a class object) and the args argument must be a sequence. The function is called with args as the argument list; the number of arguments is the length of the tuple. If the optional keywords argument is present, it must be a dictionary whose keys are strings. It specifies keyword arguments to be added to the end of the argument list. Calling apply() is different from just calling function(args), since in that case there is always exactly one argument. The use of apply() is equivalent to function(*args, **keywords).

Deprecated since version 2.3: Use function(*args, **keywords) instead of apply(function, args, keywords) (see Unpacking Argument Lists).

#### buffer(object[, offset[, size]])
The object argument must be an object that supports the buffer call interface (such as strings, arrays, and buffers). A new buffer object will be created which references the object argument. The buffer object will be a slice from the beginning of object (or from the specified offset). The slice will extend to the end of object (or will have a length given by the size argument).

#### coerce(x, y)
Return a tuple consisting of the two numeric arguments converted to a common type, using the same rules as used by arithmetic operations. If coercion is not possible, raise TypeError.

#### intern(string)
Enter string in the table of “interned” strings and return the interned string – which is string itself or a copy. Interning strings is useful to gain a little performance on dictionary lookup – if the keys in a dictionary are interned, and the lookup key is interned, the key comparisons (after hashing) can be done by a pointer compare instead of a string compare. Normally, the names used in Python programs are automatically interned, and the dictionaries used to hold module, class or instance attributes have interned keys.

Changed in version 2.3: Interned strings are not immortal (like they used to be in Python 2.2 and before); you must keep a reference to the return value of intern() around to benefit from it.

#### Footnotes

1. It is used relatively rarely so does not warrant being made into a statement.
2. Specifying a buffer size currently has no effect on systems that don’t have setvbuf(). The interface to specify the buffer size is not done using a method that calls setvbuf(), because that may dump core when called after any I/O has been performed, and there’s no reliable way to determine whether this is the case.
3. In the current implementation, local variable bindings cannot normally be affected this way, but variables retrieved from other scopes (such as modules) can be. This may change.

## 5. Built-in Types {#BuildInTypes}
The following sections describe the standard types that are built into the interpreter.

> Note: Historically (until release 2.2), Python’s built-in types have differed from user-defined types because it was not possible to use the built-in types as the basis for object-oriented inheritance. This limitation no longer exists.

The principal built-in types are numerics, sequences, mappings, files, classes, instances and exceptions.

Some operations are supported by several object types; in particular, practically all objects can be compared, tested for truth value, and converted to a string (with the repr() function or the slightly different str() function). The latter function is implicitly used when an object is written by the print() function.

### 5.1. Truth Value Testing
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below. The following values are considered false:

- None
- False
- zero of any numeric type, for example, 0, 0L, 0.0, 0j.
- any empty sequence, for example, '', (), [].
- any empty mapping, for example, {}.
- instances of user-defined classes, if the class defines a `__nonzero__()` or `__len__()` method, when that method returns the integer zero or bool value False. [1]

All other values are considered true — so objects of many types are always true.

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)

### 5.2. Boolean Operations — and, or, not
These are the Boolean operations, ordered by ascending priority:

Operation	|	Result	|	Notes
----|----|----
x or y	|	if x is false, then y, else x		|	(1)
x and y	|	if x is false, then x, else y		|	(2)
not x	|	if x is false, then True, else False		|	(3)

Notes:

1. This is a short-circuit operator, so it only evaluates the second argument if the first one is False.
2. This is a short-circuit operator, so it only evaluates the second argument if the first one is True.
3. not has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b), and a == not b is a syntax error.

### 5.3. Comparisons
Comparison operations are supported by all objects. They all have the same priority (which is higher than that of the Boolean operations). Comparisons can be chained arbitrarily; for example, x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).

This table summarizes the comparison operations:

Operation	|	Meaning	|	Notes
----|----|----
<	|	strictly less than	 |
<=	|	less than or equal	 |
\>	|	strictly greater than|	 
\>=	|	greater than or equal|	 
==	|	equal	 |
!=	|	not equal|	(1)
is	|	object identity|	 
is not |	negated object identity	 |

Notes:

1. != can also be written <>, but this is an obsolete usage kept for backwards compatibility only. New code should always use !=.


Objects of different types, except different numeric types and different string types, never compare equal; such objects are ordered consistently but arbitrarily (so that sorting a heterogeneous array yields a consistent result). Furthermore, some types (for example, file objects) support only a degenerate notion of comparison where any two objects of that type are unequal. Again, such objects are ordered arbitrarily but consistently. The <, <=, > and >= operators will raise a TypeError exception when any operand is a complex number.

Non-identical instances of a class normally compare as non-equal unless the class defines the `__eq__()` method or the `__cmp__()` method.

Instances of a class cannot be ordered with respect to other instances of the same class, or other types of object, unless the class defines either enough of the rich comparison methods `(__lt__(), __le__(), __gt__(), and __ge__())` or the `__cmp__()` method.

> CPython implementation detail: Objects of different types except numbers are ordered by their type names; objects of the same types that don’t support proper comparison are ordered by their address.

Two more operations with the same syntactic priority, in and not in, are supported only by sequence types (below).

### 5.4. Numeric Types — int, float, long, complex
There are four distinct numeric types: plain integers, long integers, floating point numbers, and complex numbers. In addition, Booleans are a subtype of plain integers. Plain integers (also just called integers) are implemented using long in C, which gives them at least 32 bits of precision (`sys.maxint` is always set to the maximum plain integer value for the current platform, the minimum value is `-sys.maxint - 1`). Long integers have unlimited precision. Floating point numbers are usually implemented using double in C; information about the precision and internal representation of floating point numbers for the machine on which your program is running is available in sys.float_info. Complex numbers have a real and imaginary part, which are each a floating point number. To extract these parts from a complex number z, use z.real and z.imag. (The standard library includes additional numeric types, fractions that hold rationals, and decimal that hold floating-point numbers with user-definable precision.)

Numbers are created by numeric literals or as the result of built-in functions and operators. Unadorned integer literals (including binary, hex, and octal numbers) yield plain integers unless the value they denote is too large to be represented as a plain integer, in which case they yield a long integer. Integer literals with an 'L' or 'l' suffix yield long integers ('L' is preferred because 1l looks too much like eleven!). Numeric literals containing a decimal point or an exponent sign yield floating point numbers. Appending 'j' or 'J' to a numeric literal yields a complex number with a zero real part. A complex numeric literal is the sum of a real and an imaginary part.

Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the “narrower” type is widened to that of the other, where plain integer is narrower than long integer is narrower than floating point is narrower than complex. Comparisons between numbers of mixed type use the same rule. [2] The constructors int(), long(), float(), and complex() can be used to produce numbers of a specific type.

All built-in numeric types support the following operations. See The power operator and later sections for the operators’ priorities.

Operation	|	Result	|	Notes
----|----|----
x + y	|	sum of x and y	 |	
x - y	|	difference of x and y	|	 
x * y	|	product of x and y	 |	
x / y	|	quotient of x and y	|	(1)
x // y	|	(floored) quotient of x and y	|	(4)(5)
x % y	|	remainder of x / y	|	(4)
-x		|	x negated	 |	
+x		|	x unchanged	 |	
abs(x)	|	absolute value or magnitude of x	|	(3)
int(x)	|	x converted to integer	|	(2)
long(x)	|	x converted to long integer	|	(2)
float(x)|	x converted to floating point	|	(6)
complex(re,im)	|	a complex number with real part re, imaginary part im. im defaults to zero.	 |	
c.conjugate()	|	conjugate of the complex number c. (Identity on real numbers)	|	 
divmod(x, y)	|	the pair (x // y, x % y)	|	(3)(4)
pow(x, y)	|	x to the power y	|	(3)(7)
x ** y	|	x to the power y	|	(7)

Notes:

1. For (plain or long) integer division, the result is an integer. The result is always rounded towards minus infinity: 1/2 is 0, (-1)/2 is -1, 1/(-2) is -1, and (-1)/(-2) is 0. Note that the result is a long integer if either operand is a long integer, regardless of the numeric value.
2. Conversion from floats using int() or long() truncates toward zero like the related function, math.trunc(). Use the function math.floor() to round downward and math.ceil() to round upward.
3. See Built-in Functions for a full description.
4. Deprecated since version 2.3: The floor division operator, the modulo operator, and the divmod() function are no longer defined for complex numbers. Instead, convert to a floating point number using the abs() function if appropriate.
5. Also referred to as integer division. The resultant value is a whole integer, though the result’s type is not necessarily int.
6 .float also accepts the strings “nan” and “inf” with an optional prefix “+” or “-” for Not a Number (NaN) and positive or negative infinity. New in version 2.6.
7. Python defines pow(0, 0) and 0 ** 0 to be 1, as is common for programming languages.

All numbers.Real types (int, long, and float) also include the following operations:

Operation	|	Result	Notes
----|----
math.trunc(x)	|	x truncated to Integral	 
round(x[, n])	|	x rounded to n digits, rounding ties away from zero. If n is omitted, it defaults to 0.	 
math.floor(x)	|	the greatest integral float <= x	 
math.ceil(x)	|	the least integral float >= x	

#### 5.4.1. Bitwise Operations on Integer Types
Bitwise operations only make sense for integers. Negative numbers are treated as their 2’s complement value (this assumes a sufficiently large number of bits that no overflow occurs during the operation).

The priorities of the binary bitwise operations are all lower than the numeric operations and higher than the comparisons; the unary operation ~ has the same priority as the other unary numeric operations (+ and -).

This table lists the bitwise operations sorted in ascending priority:

Operation	|	Result	|	Notes
----|----|----
x | y	|	bitwise or of x and y	 |	
x ^ y	|	bitwise exclusive or of x and y	 |	
x & y	|	bitwise and of x and y	 |	
x << n	|	x shifted left by n bits	|	(1)(2)
x >> n	|	x shifted right by n bits	|	(1)(3)
~x		|	the bits of x inverted	 |	

Notes:

1. Negative shift counts are illegal and cause a ValueError to be raised.
2. A left shift by n bits is equivalent to multiplication by pow(2, n). A long integer is returned if the result exceeds the range of plain integers.
3. A right shift by n bits is equivalent to division by pow(2, n).

#### 5.4.2. Additional Methods on Integer Types
The integer types implement the numbers.Integral abstract base class. In addition, they provide one more method:

- `int.bit_length()`; `long.bit_length()`
Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros:

~~~python
>>>
>>> n = -37
>>> bin(n)
'-0b100101'
>>> n.bit_length()
6
~~~
More precisely, if x is nonzero, then x.bit\_length() is the unique positive integer k such that 2\*\*(k-1) <= abs(x) < 2**k. Equivalently, when abs(x) is small enough to have a correctly rounded logarithm, then k = 1 + int(log(abs(x), 2)). If x is zero, then x.bit_length() returns 0.

Equivalent to:

~~~python
def bit_length(self):
    s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
    s = s.lstrip('-0b') # remove leading zeros and minus sign
    return len(s)       # len('100101') --> 6
~~~
New in version 2.7.

#### 5.4.3. Additional Methods on Float
The float type implements the numbers.Real abstract base class. float also has the following additional methods.

##### float.as\_integer_ratio()
Return a pair of integers whose ratio is exactly equal to the original float and with a positive denominator. Raises OverflowError on infinities and a ValueError on NaNs.

New in version 2.6.

##### float.is_integer()
Return True if the float instance is finite with integral value, and False otherwise:

~~~python
>>>
>>> (-2.0).is_integer()
True
>>> (3.2).is_integer()
False
~~~
New in version 2.6.

Two methods support conversion to and from hexadecimal strings. Since Python’s floats are stored internally as binary numbers, converting a float to or from a decimal string usually involves a small rounding error. In contrast, hexadecimal strings allow exact representation and specification of floating-point numbers. This can be useful when debugging, and in numerical work.

##### float.hex()
Return a representation of a floating-point number as a hexadecimal string. For finite floating-point numbers, this representation will always include a leading 0x and a trailing p and exponent.

New in version 2.6.

##### float.fromhex(s)
Class method to return the float represented by a hexadecimal string s. The string s may have leading and trailing whitespace.

New in version 2.6.

Note that float.hex() is an instance method, while float.fromhex() is a class method.

A hexadecimal string takes the form:

`[sign] ['0x'] integer ['.' fraction] ['p' exponent]`{: .language-python}

where the optional sign may by either + or -, integer and fraction are strings of hexadecimal digits, and exponent is a decimal integer with an optional leading sign. Case is not significant, and there must be at least one hexadecimal digit in either the integer or the fraction. This syntax is similar to the syntax specified in section 6.4.4.2 of the C99 standard, and also to the syntax used in Java 1.5 onwards. In particular, the output of float.hex() is usable as a hexadecimal floating-point literal in C or Java code, and hexadecimal strings produced by C’s %a format character or Java’s Double.toHexString are accepted by float.fromhex().

Note that the exponent is written in decimal rather than hexadecimal, and that it gives the power of 2 by which to multiply the coefficient. For example, the hexadecimal string 0x3.a7p10 represents the floating-point number (3 + 10./16 + 7./16\*\*2) * 2.0**10, or 3740.0:

~~~python
>>>
>>> float.fromhex('0x3.a7p10')
3740.0
# Applying the reverse conversion to 3740.0 gives a different hexadecimal string representing the same number:

>>>
>>> float.hex(3740.0)
'0x1.d380000000000p+11'
~~~

### 5.5. Iterator Types
New in version 2.2.

Python supports a concept of iteration over containers. This is implemented using two distinct methods; these are used to allow user-defined classes to support iteration. Sequences, described below in more detail, always support the iteration methods.

One method needs to be defined for container objects to provide iteration support:

##### container.\_\_iter__()
Return an iterator object. The object is required to support the iterator protocol described below. If a container supports different types of iteration, additional methods can be provided to specifically request iterators for those iteration types. (An example of an object supporting multiple forms of iteration would be a tree structure which supports both breadth-first and depth-first traversal.) This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.

The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:

##### iterator.\_\_iter__()
Return the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements. This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.

##### iterator.next()
Return the next item from the container. If there are no further items, raise the StopIteration exception. This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.

Python defines several iterator objects to support iteration over general and specific sequence types, dictionaries, and other more specialized forms. The specific types are not important beyond their implementation of the iterator protocol.

The intention of the protocol is that once an iterator’s next() method raises StopIteration, it will continue to do so on subsequent calls. Implementations that do not obey this property are deemed broken. (This constraint was added in Python 2.3; in Python 2.2, various iterators are broken according to this rule.)

#### 5.5.1. Generator Types
Python’s generators provide a convenient way to implement the iterator protocol. If a container object’s `__iter__()` method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the `__iter__()` and next() methods. More information about generators can be found in the documentation for the yield expression.

### 5.6. Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange
There are seven sequence types: strings, Unicode strings, lists, tuples, bytearrays, buffers, and xrange objects.

For other containers see the built in dict and set classes, and the collections module.

String literals are written in single or double quotes: 'xyzzy', "frobozz". See String literals for more about string literals. Unicode strings are much like strings, but are specified in the syntax using a preceding 'u' character: u'abc', u"def". In addition to the functionality described here, there are also string-specific methods described in the String Methods section. Lists are constructed with square brackets, separating items with commas: [a, b, c]. Tuples are constructed by the comma operator (not within square brackets), with or without enclosing parentheses, but an empty tuple must have the enclosing parentheses, such as a, b, c or (). A single item tuple must have a trailing comma, such as (d,).

Bytearray objects are created with the built-in function bytearray().

Buffer objects are not directly supported by Python syntax, but can be created by calling the built-in function buffer(). They don’t support concatenation or repetition.

Objects of type xrange are similar to buffers in that there is no specific syntax to create them, but they are created using the xrange() function. They don’t support slicing, concatenation or repetition, and using in, not in, min() or max() on them is inefficient.

Most sequence types support the following operations. The in and not in operations have the same priorities as the comparison operations. The + and * operations have the same priority as the corresponding numeric operations. [3] Additional methods are provided for Mutable Sequence Types.

This table lists the sequence operations sorted in ascending priority. In the table, s and t are sequences of the same type; n, i and j are integers:

Operation	|	Result	|	Notes
----|----|----
x in s		|	True if an item of s is equal to x, else False	|	(1)
x not in s		|	False if an item of s is equal to x, else True	|	(1)
s + t		|	the concatenation of s and t	|	(6)
s * n, n * s		|	equivalent to adding s to itself n times	|	(2)
s[i]		|	ith item of s, origin 0	|	(3)
s[i:j]		|	slice of s from i to j	|	(3)(4)
s[i:j:k]		|	slice of s from i to j with step k	|	(3)(5)
len(s)		|	length of s	 |	
min(s)		|	smallest item of s	 |	
max(s)		|	largest item of s	 |	
s.index(x)		|	index of the first occurrence of x in s	 |	
s.count(x)		|	total number of occurrences of x in s	|	

Sequence types also support comparisons. In particular, tuples and lists are compared lexicographically by comparing corresponding elements. This means that to compare equal, every element must compare equal and the two sequences must be of the same type and have the same length. (For full details see Comparisons in the language reference.)

Notes:

1. When s is a string or Unicode string object the in and not in operations act like a substring test. In Python versions before 2.3, x had to be a string of length 1. In Python 2.3 and beyond, x may be a string of any length.
2. Values of n less than 0 are treated as 0 (which yields an empty sequence of the same type as s). Note that items in the sequence s are not copied; they are referenced multiple times. This often haunts new Python programmers; consider:

		lists = [[]] * 3
		lists
		# [[], [], []]
		lists[0].append(3)
		lists
		# [[3], [3], [3]]
	{: .language-python}
What has happened is that [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are references to this single empty list. Modifying any of the elements of lists modifies this single list. You can create a list of different lists this way:

		lists = [[] for i in range(3)]
		lists[0].append(3)
		lists[1].append(5)
		lists[2].append(7)
		lists
		# [[3], [5], [7]]
	{: .language-python}
Further explanation is available in the FAQ entry How do I create a multidimensional list?.
3. If i or j is negative, the index is relative to the end of the string: len(s) + i or len(s) + j is substituted. But note that -0 is still 0.
4. The slice of s from i to j is defined as the sequence of items with index k such that i <= k < j. If i or j is greater than len(s), use len(s). If i is omitted or None, use 0. If j is omitted or None, use len(s). If i is greater than or equal to j, the slice is empty.
5. The slice of s from i to j with step k is defined as the sequence of items with index x = i + n\*k such that 0 <= n < (j-i)/k. In other words, the indices are i, i+k, i+2\*k, i+3\*k and so on, stopping when j is reached (but never including j). If i or j is greater than len(s), use len(s). If i or j are omitted or None, they become “end” values (which end depends on the sign of k). Note, k cannot be zero. If k is None, it is treated like 1.
6. CPython implementation detail: If s and t are both strings, some Python implementations such as CPython can usually perform an in-place optimization for assignments of the form s = s + t or s += t. When applicable, this optimization makes quadratic run-time much less likely. This optimization is both version and implementation dependent. For performance sensitive code, it is preferable to use the str.join() method which assures consistent linear concatenation performance across versions and implementations.

Changed in version 2.4: Formerly, string concatenation never occurred in-place.

#### 5.6.1. String Methods
Below are listed the string methods which both 8-bit strings and Unicode objects support. Some of them are also available on bytearray objects.

In addition, Python’s strings support the sequence type methods described in the Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange section. To output formatted strings use template strings or the % operator described in the String Formatting Operations section. Also, see the re module for string functions based on regular expressions.

##### str.capitalize()
Return a copy of the string with its first character capitalized and the rest lowercased.

For 8-bit strings, this method is locale-dependent.

str.center(width[, fillchar])
Return centered in a string of length width. Padding is done using the specified fillchar (default is a space).

Changed in version 2.4: Support for the fillchar argument.

str.count(sub[, start[, end]])
Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

##### str.decode([encoding[, errors]])
Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding. errors may be given to set a different error handling scheme. The default is 'strict', meaning that encoding errors raise UnicodeError. Other possible values are 'ignore', 'replace' and any other name registered via codecs.register_error(), see section Codec Base Classes.

New in version 2.2.

Changed in version 2.3: Support for other error handling schemes added.

Changed in version 2.7: Support for keyword arguments added.

##### str.encode([encoding[, errors]])
Return an encoded version of the string. Default encoding is the current default string encoding. errors may be given to set a different error handling scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any other name registered via codecs.register_error(), see section Codec Base Classes. For a list of possible encodings, see section Standard Encodings.

New in version 2.0.

Changed in version 2.3: Support for 'xmlcharrefreplace' and 'backslashreplace' and other error handling schemes added.

Changed in version 2.7: Support for keyword arguments added.

##### str.endswith(suffix[, start[, end]])
Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position.

Changed in version 2.5: Accept tuples as suffix.

##### str.expandtabs([tabsize])
Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size. Tab positions occur every tabsize characters (default is 8, giving tab positions at columns 0, 8, 16 and so on). To expand the string, the current column is set to zero and the string is examined character by character. If the character is a tab (\t), one or more space characters are inserted in the result until the current column is equal to the next tab position. (The tab character itself is not copied.) If the character is a newline (\n) or return (\r), it is copied and the current column is reset to zero. Any other character is copied unchanged and the current column is incremented by one regardless of how the character is represented when printed.

~~~python
>>>
>>> '01\t012\t0123\t01234'.expandtabs()
'01      012     0123    01234'
>>> '01\t012\t0123\t01234'.expandtabs(4)
'01  012 0123    01234'
~~~

##### str.find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found, such that sub is contained in the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

> Note: The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator:

~~~python
>>>
>>> 'Py' in 'Python'
True
~~~

##### str.format(*args, **kwargs)
Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.

~~~python
>>>
>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'
~~~

See Format String Syntax for a description of the various formatting options that can be specified in format strings.

This method of string formatting is the new standard in Python 3, and should be preferred to the % formatting described in String Formatting Operations in new code.

New in version 2.6.

##### str.index(sub[, start[, end]])
Like find(), but raise ValueError when the substring is not found.

##### str.isalnum()
Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.

For 8-bit strings, this method is locale-dependent.

##### str.isalpha()
Return true if all characters in the string are alphabetic and there is at least one character, false otherwise.

For 8-bit strings, this method is locale-dependent.

##### str.isdigit()
Return true if all characters in the string are digits and there is at least one character, false otherwise.

For 8-bit strings, this method is locale-dependent.

##### str.islower()
Return true if all cased characters [4] in the string are lowercase and there is at least one cased character, false otherwise.

For 8-bit strings, this method is locale-dependent.

##### str.isspace()
Return true if there are only whitespace characters in the string and there is at least one character, false otherwise.

For 8-bit strings, this method is locale-dependent.

##### str.istitle()
Return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return false otherwise.

For 8-bit strings, this method is locale-dependent.

##### str.isupper()
Return true if all cased characters [4] in the string are uppercase and there is at least one cased character, false otherwise.

For 8-bit strings, this method is locale-dependent.

##### str.join(iterable)
Return a string which is the concatenation of the strings in the iterable iterable. The separator between elements is the string providing this method.

##### str.ljust(width[, fillchar])
Return the string left justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than or equal to len(s).

Changed in version 2.4: Support for the fillchar argument.

##### str.lower()
Return a copy of the string with all the cased characters [4] converted to lowercase.

For 8-bit strings, this method is locale-dependent.

##### str.lstrip([chars])
Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped:

~~~python
>>>
>>> '   spacious   '.lstrip()
'spacious   '
>>> 'www.example.com'.lstrip('cmowz.')
'example.com'
~~~
Changed in version 2.2.2: Support for the chars argument.

##### str.partition(sep)
Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.

New in version 2.5.

##### str.replace(old, new[, count])
Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

##### str.rfind(sub[, start[, end]])
Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

##### str.rindex(sub[, start[, end]])
Like rfind() but raises ValueError when the substring sub is not found.

##### str.rjust(width[, fillchar])
Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than or equal to len(s).

Changed in version 2.4: Support for the fillchar argument.

##### str.rpartition(sep)
Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.

New in version 2.5.

##### str.rsplit([sep[, maxsplit]])
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a separator. Except for splitting from the right, rsplit() behaves like split() which is described in detail below.

New in version 2.4.

##### str.rstrip([chars])
Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:

~~~python
>>>
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'
~~~
Changed in version 2.2.2: Support for the chars argument.

##### str.split([sep[, maxsplit]])
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].

If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].

For example, `' 1  2   3  '.split()` returns `['1', '2', '3']`, and `'  1  2   3  '.split(None, 1)` returns `['1', '2   3  ']`.

##### str.splitlines([keepends])
Return a list of the lines in the string, breaking at line boundaries. This method uses the universal newlines approach to splitting lines. Line breaks are not included in the resulting list unless keepends is given and true.

For example, `'ab c\n\nde fg\rkl\r\n'.splitlines()` returns `['ab c', '', 'de fg', 'kl']`, while the same call with splitlines(True) returns `['ab c\n', '\n', 'de fg\r', 'kl\r\n']`.

Unlike split() when a delimiter string sep is given, this method returns an empty list for the empty string, and a terminal line break does not result in an extra line.

##### str.startswith(prefix[, start[, end]])
Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.

Changed in version 2.5: Accept tuples as prefix.

##### str.strip([chars])
Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:

~~~python
>>>
>>> '   spacious   '.strip()
'spacious'
>>> 'www.example.com'.strip('cmowz.')
'example'
~~~
Changed in version 2.2.2: Support for the chars argument.

##### str.swapcase()
Return a copy of the string with uppercase characters converted to lowercase and vice versa.

For 8-bit strings, this method is locale-dependent.

##### str.title()
Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions and possessives form word boundaries, which may not be the desired result:

~~~python
>>>
>>> "they're bill's friends from the UK".title()
"They'Re Bill'S Friends From The Uk"
~~~
A workaround for apostrophes can be constructed using regular expressions:

~~~python
>>>
>>> import re
>>> def titlecase(s):
...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0)[0].upper() +
...                              mo.group(0)[1:].lower(),
...                   s)
...
>>> titlecase("they're bill's friends.")
"They're Bill's Friends."
~~~
For 8-bit strings, this method is locale-dependent.

##### str.translate(table[, deletechars])
Return a copy of the string where all characters occurring in the optional argument deletechars are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256.

You can use the maketrans() helper function in the string module to create a translation table. For string objects, set the table argument to None for translations that only delete characters:

~~~python
>>>
>>> 'read this short text'.translate(None, 'aeiou')
'rd ths shrt txt'
~~~

New in version 2.6: Support for a None table argument.

For Unicode objects, the translate() method does not accept the optional deletechars argument. Instead, it returns a copy of the s where all characters have been mapped through the given translation table which must be a mapping of Unicode ordinals to Unicode ordinals, Unicode strings or None. Unmapped characters are left untouched. Characters mapped to None are deleted. Note, a more flexible approach is to create a custom character mapping codec using the codecs module (see encodings.cp1251 for an example).

##### str.upper()
Return a copy of the string with all the cased characters [4] converted to uppercase. Note that str.upper().isupper() might be False if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. “Lt” (Letter, titlecase).

For 8-bit strings, this method is locale-dependent.

##### str.zfill(width)
Return the numeric string left filled with zeros in a string of length width. A sign prefix is handled correctly. The original string is returned if width is less than or equal to len(s).

New in version 2.2.2.

The following methods are present only on unicode objects:

##### unicode.isnumeric()
Return True if there are only numeric characters in S, False otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH.

##### unicode.isdecimal()
Return True if there are only decimal characters in S, False otherwise. Decimal characters include digit characters, and all characters that can be used to form decimal-radix numbers, e.g. U+0660, ARABIC-INDIC DIGIT ZERO.

#### 5.6.2. String Formatting Operations
String and Unicode objects have one unique built-in operation: the % operator (modulo). This is also known as the string formatting or interpolation operator. Given format % values (where format is a string or Unicode object), % conversion specifications in format are replaced with zero or more elements of values. The effect is similar to the using sprintf() in the C language. If format is a Unicode object, or if any of the objects being converted using the %s conversion are Unicode objects, the result will also be a Unicode object.

If format requires a single argument, values may be a single non-tuple object. [5] Otherwise, values must be a tuple with exactly the number of items specified by the format string, or a single mapping object (for example, a dictionary).

A conversion specifier contains two or more characters and has the following components, which must occur in this order:

1. The '%' character, which marks the start of the specifier.
1. Mapping key (optional), consisting of a parenthesised sequence of characters (for example, (somename)).
1. Conversion flags (optional), which affect the result of some conversion types.
Minimum field width (optional). If specified as an '*' (asterisk), the actual width is read from the next element of the tuple in values, and the object to convert comes after the minimum field width and optional precision.
1. Precision (optional), given as a '.' (dot) followed by the precision. If specified as '*' (an asterisk), the actual width is read from the next element of the tuple in values, and the value to convert comes after the precision.
1. Length modifier (optional).
1. Conversion type.

When the right argument is a dictionary (or other mapping type), then the formats in the string must include a parenthesised mapping key into that dictionary inserted immediately after the '%' character. The mapping key selects the value to be formatted from the mapping. For example:

~~~python
>>>
>>> print '%(language)s has %(number)03d quote types.' % \
...       {"language": "Python", "number": 2}
Python has 002 quote types.
~~~
In this case no * specifiers may occur in a format (since they require a sequential parameter list).

The conversion flag characters are:

Flag	|	Meaning
-----|-----
'#'	|	The value conversion will use the “alternate form” (where defined below).
'0'	|	The conversion will be zero padded for numeric values.
'-'	|	The converted value is left adjusted (overrides the '0' conversion if both are given).
' '	|	(a space) A blank should be left before a positive number (or empty string) produced by a signed conversion.
'+'	|	A sign character ('+' or '-') will precede the conversion (overrides a “space” flag).

A length modifier (h, l, or L) may be present, but is ignored as it is not necessary for Python – so e.g. %ld is identical to %d.

The conversion types are:

Conversion	|	Meaning	|	Notes
----|-----|-----
'd'	|	Signed integer decimal.	 |	
'i'	|	Signed integer decimal.	 |	
'o'	|	Signed octal value.	|	(1)
'u'	|	Obsolete type – it is identical to 'd'.	|	(7)
'x'	|	Signed hexadecimal (lowercase).	|	(2)
'X'	|	Signed hexadecimal (uppercase).	|	(2)
'e'	|	Floating point exponential format (lowercase).	|	(3)
'E'	|	Floating point exponential format (uppercase).	|	(3)
'f'	|	Floating point decimal format.	|	(3)
'F'	|	Floating point decimal format.	|	(3)
'g'	|	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	|	(4)
'G'	|	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	|	(4)
'c'	|	Single character (accepts integer or single character string).|		 
'r'	|	String (converts any Python object using repr()).	|	(5)
's'	|	String (converts any Python object using str()).	|	(6)
'%'	|	No argument is converted, results in a '%' character in the result.	 |	

Notes:

1. The alternate form causes a leading zero ('0') to be inserted between left-hand padding and the formatting of the number if the leading character of the result is not already a zero.
2. The alternate form causes a leading '0x' or '0X' (depending on whether the 'x' or 'X' format was used) to be inserted between left-hand padding and the formatting of the number if the leading character of the result is not already a zero.
3. The alternate form causes the result to always contain a decimal point, even if no digits follow it.  
   The precision determines the number of digits after the decimal point and defaults to 6.
4. The alternate form causes the result to always contain a decimal point, and trailing zeroes are not removed as they would otherwise be.  
The precision determines the number of significant digits before and after the decimal point and defaults to 6.
5. The %r conversion was added in Python 2.0.  
The precision determines the maximal number of characters used.
6. If the object or format provided is a unicode string, the resulting string will also be unicode.  
The precision determines the maximal number of characters used.
7. See PEP 237.

Since Python strings have an explicit length, `%s` conversions do not assume that `'\0'` is the end of the string.

Changed in version 2.7: `%f` conversions for numbers whose absolute value is over 1e50 are no longer replaced by `%g` conversions.

Additional string operations are defined in standard modules string and re.

#### 5.6.3. XRange Type
The xrange type is an immutable sequence which is commonly used for looping. The advantage of the xrange type is that an xrange object will always take the same amount of memory, no matter the size of the range it represents. There are no consistent performance advantages.

XRange objects have very little behavior: they only support indexing, iteration, and the len() function.

#### 5.6.4. Mutable Sequence Types
List and bytearray objects support additional operations that allow in-place modification of the object. Other mutable sequence types (when added to the language) should also support these operations. Strings and tuples are immutable sequence types: such objects cannot be modified once created. The following operations are defined on mutable sequence types (where x is an arbitrary object):

Operation	|	Result	|	Notes
s[i] = x	|	item i of s is replaced by x	|	 
s[i:j] = t	|	slice of s from i to j is replaced by the contents of the iterable t|		 
del s[i:j]	|	same as s[i:j] = []	 |	
s[i:j:k] = t 	|		the elements of s[i:j:k] are replaced by those of t	|	(1)
del s[i:j:k]	|		removes the elements of s[i:j:k] from the list	|	 
s.append(x)		|	same as s[len(s):len(s)] = [x]	|	(2)
s.extend(x) or s += t	|	for the most part the same as s[len(s):len(s)] = x	|	(3)
s *= n	|	updates s with its contents repeated n times	|	(11)
s.count(x)	|	return number of i‘s for which s[i] == x	|	 
s.index(x[, i[, j]])	|	return smallest k such that s[k] == x and i <= k < j	|	(4)
s.insert(i, x)	|	same as s[i:i] = [x]	|	(5)
s.pop([i])	|	same as x = s[i]; del s[i]; return x	|	(6)
s.remove(x)	|	same as del s[s.index(x)]	|	(4)
s.reverse()	|	reverses the items of s in place	|	(7)
s.sort([cmp[, key[, reverse]]])	|	sort the items of s in place	|	(7)(8)(9)(10)

Notes:

1. t must have the same length as the slice it is replacing.
2. The C implementation of Python has historically accepted multiple parameters and implicitly joined them into a tuple; this no longer works in Python 2.0. Use of this misfeature has been deprecated since Python 1.4.
3. x can be any iterable object.
4. Raises ValueError when x is not found in s. When a negative index is passed as the second or third parameter to the index() method, the list length is added, as for slice indices. If it is still negative, it is truncated to zero, as for slice indices.  
Changed in version 2.3: Previously, index() didn’t have arguments for specifying start and stop positions.
5. When a negative index is passed as the first parameter to the insert() method, the list length is added, as for slice indices. If it is still negative, it is truncated to zero, as for slice indices.  
Changed in version 2.3: Previously, all negative indices were truncated to zero.
6. The pop() method’s optional argument i defaults to -1, so that by default the last item is removed and returned.
7. The sort() and reverse() methods modify the list in place for economy of space when sorting or reversing a large list. To remind you that they operate by side effect, they don’t return the sorted or reversed list.
8. The sort() method takes optional arguments for controlling the comparisons.  
cmp specifies a custom comparison function of two arguments (list items) which should return a negative, zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument: cmp=lambda x,y: cmp(x.lower(), y.lower()). The default value is None.  
key specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower. The default value is None.  
reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.  
In general, the key and reverse conversion processes are much faster than specifying an equivalent cmp function. This is because cmp is called multiple times for each list element while key and reverse touch each element only once. Use functools.cmp\_to_key() to convert an old-style cmp function to a key function.  
Changed in version 2.3: Support for None as an equivalent to omitting cmp was added.  
Changed in version 2.4: Support for key and reverse was added.  
9. Starting with Python 2.3, the sort() method is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).
10. CPython implementation detail: While a list is being sorted, the effect of attempting to mutate, or even inspect, the list is undefined. The C implementation of Python 2.3 and newer makes the list appear empty for the duration, and raises ValueError if it can detect that the list has been mutated during a sort.
11. The value n is an integer, or an object implementing \_\_index__(). Zero and negative values of n clear the sequence. Items in the sequence are not copied; they are referenced multiple times, as explained for s * n under Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange.

### 5.7. Set Types — set, frozenset
A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference. (For other containers see the built in dict, list, and tuple classes, and the collections module.)

New in version 2.4.

Like other collections, sets support x in set, len(set), and for x in set. Being an unordered collection, sets do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.

There are currently two built-in set types, set and frozenset. The set type is mutable — the contents can be changed using methods like add() and remove(). Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. The frozenset type is immutable and hashable — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.

As of Python 2.7, non-empty sets (not frozensets) can be created by placing a comma-separated list of elements within braces, for example: {'jack', 'sjoerd'}, in addition to the set constructor.

The constructors for both classes work the same:

~~~python
class set([iterable])
class frozenset([iterable])
~~~
Return a new set or frozenset object whose elements are taken from iterable. The elements of a set must be hashable. To represent sets of sets, the inner sets must be frozenset objects. If iterable is not specified, a new empty set is returned.

Instances of set and frozenset provide the following operations:

##### len(s)
Return the cardinality of set s.

##### x in s
Test x for membership in s.

##### x not in s
Test x for non-membership in s.

##### isdisjoint(other)
Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.

New in version 2.6.

##### issubset(other)
- `set <= other`  
Test whether every element in the set is in other.
- `set < other`  
Test whether the set is a proper subset of other, that is, set <= other and set != other.

##### issuperset(other)
- `set >= other` 
Test whether every element in other is in the set.
- `set > other`  
Test whether the set is a proper superset of other, that is, set >= other and set != other.

##### union(other, ...), set | other | ...
Return a new set with elements from the set and all others.

Changed in version 2.6: Accepts multiple input iterables.

##### intersection(other, ...), set & other & ...
Return a new set with elements common to the set and all others.

Changed in version 2.6: Accepts multiple input iterables.

##### difference(other, ...), set - other - ...
Return a new set with elements in the set that are not in the others.

Changed in version 2.6: Accepts multiple input iterables.

##### symmetric_difference(other), set ^ other
Return a new set with elements in either the set or other but not both.

##### copy()
Return a new set with a shallow copy of s.

Note, the non-operator versions of union(), intersection(), difference(), and symmetric_difference(), issubset(), and issuperset() methods will accept any iterable as an argument. In contrast, their operator based counterparts require their arguments to be sets. This precludes error-prone constructions like set('abc') & 'cbs' in favor of the more readable set('abc').intersection('cbs').

Both set and frozenset support set to set comparisons. Two sets are equal if and only if every element of each set is contained in the other (each is a subset of the other). A set is less than another set if and only if the first set is a proper subset of the second set (is a subset, but is not equal). A set is greater than another set if and only if the first set is a proper superset of the second set (is a superset, but is not equal).

Instances of set are compared to instances of frozenset based on their members. For example, set('abc') == frozenset('abc') returns True and so does set('abc') in set([frozenset('abc')]).

The subset and equality comparisons do not generalize to a total ordering function. For example, any two non-empty disjoint sets are not equal and are not subsets of each other, so all of the following return False: a<b, a==b, or a>b. Accordingly, sets do not implement the \_\_cmp__() method.

Since sets only define partial ordering (subset relationships), the output of the list.sort() method is undefined for lists of sets.

Set elements, like dictionary keys, must be hashable.

Binary operations that mix set instances with frozenset return the type of the first operand. For example: `frozenset('ab') | set('bc')` returns an instance of frozenset.

The following table lists operations available for set that do not apply to immutable instances of frozenset:

##### update(other, ...), set |= other | ...
Update the set, adding elements from all others.

Changed in version 2.6: Accepts multiple input iterables.

##### intersection_update(other, ...), set &= other & ...
Update the set, keeping only elements found in it and all others.

Changed in version 2.6: Accepts multiple input iterables.

##### difference_update(other, ...); set -= other | ...
Update the set, removing elements found in others.

Changed in version 2.6: Accepts multiple input iterables.

##### symmetric\_difference_update(other); set ^= other
Update the set, keeping only elements found in either set, but not in both.

##### add(elem)
Add element elem to the set.

##### remove(elem)
Remove element elem from the set. Raises KeyError if elem is not contained in the set.

##### discard(elem)
Remove element elem from the set if it is present.

##### pop()
Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

##### clear()
Remove all elements from the set.

Note, the non-operator versions of the update(), intersection\_update(), difference\_update(), and symmetric\_difference_update() methods will accept any iterable as an argument.

Note, the elem argument to the \_\_contains__(), remove(), and discard() methods may be a set. To support searching for an equivalent frozenset, the elem set is temporarily mutated during the search and then restored. During the search, the elem set should not be read or mutated since it does not have a meaningful value.

> See also:  
[Comparison to the built-in set types](https://docs.python.org/2/library/sets.html#comparison-to-builtin-set)  
Differences between the sets module and the built-in set types.

### 5.8. Mapping Types — dict
A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary. (For other containers see the built in list, set, and tuple classes, and the collections module.)

A dictionary’s keys are almost arbitrary values. Values that are not hashable, that is, values containing lists, dictionaries or other mutable types (that are compared by value rather than by object identity) may not be used as keys. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (such as 1 and 1.0) then they can be used interchangeably to index the same dictionary entry. (Note however, that since computers store floating-point numbers as approximations it is usually unwise to use them as dictionary keys.)

Dictionaries can be created by placing a comma-separated list of key: value pairs within braces, for example: {'jack': 4098, 'sjoerd': 4127} or {4098: 'jack', 4127: 'sjoerd'}, or by the dict constructor.

~~~python
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
~~~
Return a new dictionary initialized from an optional positional argument and a possibly empty set of keyword arguments.

If no positional argument is given, an empty dictionary is created. If a positional argument is given and it is a mapping object, a dictionary is created with the same key-value pairs as the mapping object. Otherwise, the positional argument must be an iterable object. Each item in the iterable must itself be an iterable with exactly two objects. The first object of each item becomes a key in the new dictionary, and the second object the corresponding value. If a key occurs more than once, the last value for that key becomes the corresponding value in the new dictionary.

If keyword arguments are given, the keyword arguments and their values are added to the dictionary created from the positional argument. If a key being added is already present, the value from the keyword argument replaces the value from the positional argument.

To illustrate, the following examples all return a dictionary equal to {"one": 1, "two": 2, "three": 3}:

~~~python
>>>
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
~~~

Providing keyword arguments as in the first example only works for keys that are valid Python identifiers. Otherwise, any valid keys can be used.

New in version 2.2.

Changed in version 2.3: Support for building a dictionary from keyword arguments added.

These are the operations that dictionaries support (and therefore, custom mapping types should support too):

##### len(d)
Return the number of items in the dictionary d.

##### d[key]
Return the item of d with key key. Raises a KeyError if key is not in the map.

If a subclass of dict defines a method __missing__() and key is not present, the d[key] operation calls that method with the key key as argument. The d[key] operation then returns or raises whatever is returned or raised by the __missing__(key) call. No other operations or methods invoke __missing__(). If __missing__() is not defined, KeyError is raised. __missing__() must be a method; it cannot be an instance variable:

~~~python
>>>
>>> class Counter(dict):
...     def __missing__(self, key):
...         return 0
>>> c = Counter()
>>> c['red']
0
>>> c['red'] += 1
>>> c['red']
1
~~~
The example above shows part of the implementation of collections.Counter. A different __missing__ method is used by collections.defaultdict.

New in version 2.5: Recognition of __missing__ methods of dict subclasses.

##### d[key] = value
Set d[key] to value.

##### del d[key]
Remove d[key] from d. Raises a KeyError if key is not in the map.

##### key in d
Return True if d has a key key, else False.

New in version 2.2.

##### key not in d
Equivalent to not key in d.

New in version 2.2.

##### iter(d)
Return an iterator over the keys of the dictionary. This is a shortcut for iterkeys().

##### clear()
Remove all items from the dictionary.

##### copy()
Return a shallow copy of the dictionary.

##### fromkeys(seq[, value])
Create a new dictionary with keys from seq and values set to value.

fromkeys() is a class method that returns a new dictionary. value defaults to None.

New in version 2.3.

##### get(key[, default])
Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.

##### has_key(key)
Test for the presence of key in the dictionary. has_key() is deprecated in favor of key in d.

##### items()
Return a copy of the dictionary’s list of (key, value) pairs.

> CPython implementation detail: Keys and values are listed in an arbitrary order which is non-random, varies across Python implementations, and depends on the dictionary’s history of insertions and deletions.

If items(), keys(), values(), iteritems(), iterkeys(), and itervalues() are called with no intervening modifications to the dictionary, the lists will directly correspond. This allows the creation of (value, key) pairs using zip(): pairs = zip(d.values(), d.keys()). The same relationship holds for the iterkeys() and itervalues() methods: pairs = zip(d.itervalues(), d.iterkeys()) provides the same value for pairs. Another way to create the same list is pairs = [(v, k) for (k, v) in d.iteritems()].

##### iteritems()
Return an iterator over the dictionary’s (key, value) pairs. See the note for dict.items().

Using iteritems() while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries.

New in version 2.2.

##### iterkeys()
Return an iterator over the dictionary’s keys. See the note for dict.items().

Using iterkeys() while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries.

New in version 2.2.

##### itervalues()
Return an iterator over the dictionary’s values. See the note for dict.items().

Using itervalues() while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries.

New in version 2.2.

##### keys()
Return a copy of the dictionary’s list of keys. See the note for dict.items().

##### pop(key[, default])
If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.

New in version 2.3.

##### popitem()
Remove and return an arbitrary (key, value) pair from the dictionary.

popitem() is useful to destructively iterate over a dictionary, as often used in set algorithms. If the dictionary is empty, calling popitem() raises a KeyError.

##### setdefault(key[, default])
If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.

##### update([other])
Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.

update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). If keyword arguments are specified, the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).

Changed in version 2.4: Allowed the argument to be an iterable of key/value pairs and allowed keyword arguments.

##### values()
Return a copy of the dictionary’s list of values. See the note for dict.items().

##### viewitems()
Return a new view of the dictionary’s items ((key, value) pairs). See below for documentation of view objects.

New in version 2.7.

##### viewkeys()
Return a new view of the dictionary’s keys. See below for documentation of view objects.

New in version 2.7.

##### viewvalues()
Return a new view of the dictionary’s values. See below for documentation of view objects.

New in version 2.7.

Dictionaries compare equal if and only if they have the same (key, value) pairs.

#### 5.8.1. Dictionary view objects
The objects returned by `dict.viewkeys()`, `dict.viewvalues()` and `dict.viewitems()` are view objects. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.

Dictionary views can be iterated over to yield their respective data, and support membership tests:

##### len(dictview)
Return the number of entries in the dictionary.

##### iter(dictview)
Return an iterator over the keys, values or items (represented as tuples of (key, value)) in the dictionary.

Keys and values are iterated over in an arbitrary order which is non-random, varies across Python implementations, and depends on the dictionary’s history of insertions and deletions. If keys, values and items views are iterated over with no intervening modifications to the dictionary, the order of items will directly correspond. This allows the creation of (value, key) pairs using zip(): pairs = zip(d.values(), d.keys()). Another way to create the same list is pairs = [(v, k) for (k, v) in d.items()].

Iterating views while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries.

##### x in dictview
Return True if x is in the underlying dictionary’s keys, values or items (in the latter case, x should be a (key, value) tuple).

Keys views are set-like since their entries are unique and hashable. If all values are hashable, so that (key, value) pairs are unique and hashable, then the items view is also set-like. (Values views are not treated as set-like since the entries are generally not unique.) Then these set operations are available (“other” refers either to another view or a set):

##### dictview & other
Return the intersection of the dictview and the other object as a new set.

##### dictview | other
Return the union of the dictview and the other object as a new set.

##### dictview - other
Return the difference between the dictview and the other object (all elements in dictview that aren’t in other) as a new set.

##### dictview ^ other
Return the symmetric difference (all elements either in dictview or other, but not in both) of the dictview and the other object as a new set.

An example of dictionary view usage:

~~~python
>>>
>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.viewkeys()
>>> values = dishes.viewvalues()

>>> # iteration
>>> n = 0
>>> for val in values:
...     n += val
>>> print(n)
504

>>> # keys and values are iterated over in the same order
>>> list(keys)
['eggs', 'bacon', 'sausage', 'spam']
>>> list(values)
[2, 1, 1, 500]

>>> # view objects are dynamic and reflect dict changes
>>> del dishes['eggs']
>>> del dishes['sausage']
>>> list(keys)
['spam', 'bacon']

>>> # set operations
>>> keys & {'eggs', 'bacon', 'salad'}
{'bacon'}
~~~

### 5.9. File Objects
File objects are implemented using C’s stdio package and can be created with the built-in open() function. File objects are also returned by some other built-in functions and methods, such as os.popen() and os.fdopen() and the makefile() method of socket objects. Temporary files can be created using the tempfile module, and high-level file operations such as copying, moving, and deleting files and directories can be achieved with the shutil module.

When a file operation fails for an I/O-related reason, the exception IOError is raised. This includes situations where the operation is not defined for some reason, like seek() on a tty device or writing a file opened for reading.

Files have the following methods:

##### file.close()
Close the file. A closed file cannot be read or written any more. Any operation which requires that the file be open will raise a ValueError after the file has been closed. Calling close() more than once is allowed.

As of Python 2.5, you can avoid having to call this method explicitly if you use the with statement. For example, the following code will automatically close f when the with block is exited:

~~~python
from __future__ import with_statement # This isn't required in Python 2.6

with open("hello.txt") as f:
    for line in f:
        print line,
~~~
In older versions of Python, you would have needed to do this to get the same effect:

~~~python
f = open("hello.txt")
try:
    for line in f:
        print line,
finally:
    f.close()
~~~
Note Not all “file-like” types in Python support use as a context manager for the with statement. If your code is intended to work with any file-like object, you can use the function contextlib.closing() instead of using the object directly.

##### file.flush()
Flush the internal buffer, like stdio‘s fflush(). This may be a no-op on some file-like objects.

> Note: flush() does not necessarily write the file’s data to disk. Use flush() followed by os.fsync() to ensure this behavior.

##### file.fileno()
Return the integer “file descriptor” that is used by the underlying implementation to request I/O operations from the operating system. This can be useful for other, lower level interfaces that use file descriptors, such as the fcntl module or os.read() and friends.

> Note: File-like objects which do not have a real file descriptor should not provide this method!

##### file.isatty()
Return True if the file is connected to a tty(-like) device, else False.

> Note: If a file-like object is not associated with a real file, this method should not be implemented.

##### file.next()
A file object is its own iterator, for example iter(f) returns f (unless f is closed). When a file is used as an iterator, typically in a for loop (for example, for line in f: print line.strip()), the next() method is called repeatedly. This method returns the next input line, or raises StopIteration when EOF is hit when the file is open for reading (behavior is undefined when the file is open for writing). In order to make a for loop the most efficient way of looping over the lines of a file (a very common operation), the next() method uses a hidden read-ahead buffer. As a consequence of using a read-ahead buffer, combining next() with other file methods (like readline()) does not work right. However, using seek() to reposition the file to an absolute position will flush the read-ahead buffer.

New in version 2.3.

##### file.read([size])
Read at most size bytes from the file (less if the read hits EOF before obtaining size bytes). If the size argument is negative or omitted, read all data until EOF is reached. The bytes are returned as a string object. An empty string is returned when EOF is encountered immediately. (For certain files, like ttys, it makes sense to continue reading after an EOF is hit.) Note that this method may call the underlying C function fread() more than once in an effort to acquire as close to size bytes as possible. Also note that when in non-blocking mode, less data than was requested may be returned, even if no size parameter was given.

> Note: This function is simply a wrapper for the underlying fread() C function, and will behave the same in corner cases, such as whether the EOF value is cached.

##### file.readline([size])
Read one entire line from the file. A trailing newline character is kept in the string (but may be absent when a file ends with an incomplete line). [6] If the size argument is present and non-negative, it is a maximum byte count (including the trailing newline) and an incomplete line may be returned. When size is not 0, an empty string is returned only when EOF is encountered immediately.

> Note: Unlike stdio‘s fgets(), the returned string contains null characters ('\0') if they occurred in the input.

##### file.readlines([sizehint])
Read until EOF using readline() and return a list containing the lines thus read. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read. Objects implementing a file-like interface may choose to ignore sizehint if it cannot be implemented, or cannot be implemented efficiently.

##### file.xreadlines()
This method returns the same thing as iter(f).

New in version 2.1.

> Deprecated since version 2.3: Use for line in file instead.

##### file.seek(offset[, whence])
Set the file’s current position, like stdio‘s fseek(). The whence argument is optional and defaults to os.SEEK\_SET or 0 (absolute file positioning); other values are os.SEEK\_CUR or 1 (seek relative to the current position) and os.SEEK\_END or 2 (seek relative to the file’s end). There is no return value.

For example, f.seek(2, os.SEEK\_CUR) advances the position by two and f.seek(-3, os.SEEK_END) sets the position to the third to last.

Note that if the file is opened for appending (mode 'a' or 'a+'), any seek() operations will be undone at the next write. If the file is only opened for writing in append mode (mode 'a'), this method is essentially a no-op, but it remains useful for files opened in append mode with reading enabled (mode 'a+'). If the file is opened in text mode (without 'b'), only offsets returned by tell() are legal. Use of other offsets causes undefined behavior.

Note that not all file objects are seekable.

Changed in version 2.6: Passing float values as offset has been deprecated.

##### file.tell()
Return the file’s current position, like stdio‘s ftell().

Note On Windows, tell() can return illegal values (after an fgets()) when reading files with Unix-style line-endings. Use binary mode ('rb') to circumvent this problem.

##### file.truncate([size])
Truncate the file’s size. If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position. The current file position is not changed. Note that if a specified size exceeds the file’s current size, the result is platform-dependent: possibilities include that the file may remain unchanged, increase to the specified size as if zero-filled, or increase to the specified size with undefined new content. Availability: Windows, many Unix variants.

##### file.write(str)
Write a string to the file. There is no return value. Due to buffering, the string may not actually show up in the file until the flush() or close() method is called.

##### file.writelines(sequence)
Write a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings. There is no return value. (The name is intended to match readlines(); writelines() does not add line separators.)

Files support the iterator protocol. Each iteration returns the same result as readline(), and iteration ends when the readline() method returns an empty string.

File objects also offer a number of other interesting attributes. These are not required for file-like objects, but should be implemented if they make sense for the particular object.

##### file.closed
bool indicating the current state of the file object. This is a read-only attribute; the close() method changes the value. It may not be available on all file-like objects.

##### file.encoding
The encoding that this file uses. When Unicode strings are written to a file, they will be converted to byte strings using this encoding. In addition, when the file is connected to a terminal, the attribute gives the encoding that the terminal is likely to use (that information might be incorrect if the user has misconfigured the terminal). The attribute is read-only and may not be present on all file-like objects. It may also be None, in which case the file uses the system default encoding for converting Unicode strings.

New in version 2.3.

##### file.errors
The Unicode error handler used along with the encoding.

New in version 2.6.

##### file.mode
The I/O mode for the file. If the file was created using the open() built-in function, this will be the value of the mode parameter. This is a read-only attribute and may not be present on all file-like objects.

##### file.name
If the file object was created using open(), the name of the file. Otherwise, some string that indicates the source of the file object, of the form <...>. This is a read-only attribute and may not be present on all file-like objects.

##### file.newlines
If Python was built with universal newlines enabled (the default) this read-only attribute exists, and for files opened in universal newline read mode it keeps track of the types of newlines encountered while reading the file. The values it can take are '\r', '\n', '\r\n', None (unknown, no newlines read yet) or a tuple containing all the newline types seen, to indicate that multiple newline conventions were encountered. For files not opened in universal newlines read mode the value of this attribute will be None.

##### file.softspace
Boolean that indicates whether a space character needs to be printed before another value when using the print statement. Classes that are trying to simulate a file object should also have a writable softspace attribute, which should be initialized to zero. This will be automatic for most classes implemented in Python (care may be needed for objects that override attribute access); types implemented in C will have to provide a writable softspace attribute.

> Note: This attribute is not used to control the print statement, but to allow the implementation of print to keep track of its internal state.

### 5.10. memoryview type
New in version 2.7.

memoryview objects allow Python code to access the internal data of an object that supports the buffer protocol without copying. Memory is generally interpreted as simple bytes.

~~~python
class memoryview(obj)
~~~

Create a memoryview that references obj. obj must support the buffer protocol. Built-in objects that support the buffer protocol include str and bytearray (but not unicode).

A memoryview has the notion of an element, which is the atomic memory unit handled by the originating object obj. For many simple types such as str and bytearray, an element is a single byte, but other third-party types may expose larger elements.

len(view) returns the total number of elements in the memoryview, view. The itemsize attribute will give you the number of bytes in a single element.

A memoryview supports slicing to expose its data. Taking a single index will return a single element as a str object. Full slicing will result in a subview:

~~~python
>>>
>>> v = memoryview('abcefg')
>>> v[1]
'b'
>>> v[-1]
'g'
>>> v[1:4]
<memory at 0x77ab28>
>>> v[1:4].tobytes()
'bce'
~~~
If the object the memoryview is over supports changing its data, the memoryview supports slice assignment:

~~~python
>>>
>>> data = bytearray('abcefg')
>>> v = memoryview(data)
>>> v.readonly
False
>>> v[0] = 'z'
>>> data
bytearray(b'zbcefg')
>>> v[1:4] = '123'
>>> data
bytearray(b'z123fg')
>>> v[2] = 'spam'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot modify size of memoryview object
~~~
Notice how the size of the memoryview object cannot be changed.

memoryview has two methods:

##### tobytes()
Return the data in the buffer as a bytestring (an object of class str).

~~~python
>>>
>>> m = memoryview("abc")
>>> m.tobytes()
'abc'
tolist()
~~~
Return the data in the buffer as a list of integers.

~~~python
>>>
>>> memoryview("abc").tolist()
[97, 98, 99]
~~~
There are also several readonly attributes available:

##### format
A string containing the format (in struct module style) for each element in the view. This defaults to 'B', a simple bytestring.

##### itemsize
The size in bytes of each element of the memoryview.

##### shape
A tuple of integers the length of ndim giving the shape of the memory as a N-dimensional array.

##### ndim
An integer indicating how many dimensions of a multi-dimensional array the memory represents.

##### strides
A tuple of integers the length of ndim giving the size in bytes to access each element for each dimension of the array.

##### readonly
A bool indicating whether the memory is read only.

### 5.11. Context Manager Types
New in version 2.5.

Python’s with statement supports the concept of a runtime context defined by a context manager. This is implemented using two separate methods that allow user-defined classes to define a runtime context that is entered before the statement body is executed and exited when the statement ends.

The context management protocol consists of a pair of methods that need to be provided for a context manager object to define a runtime context:

##### contextmanager.\_\_enter__()
Enter the runtime context and return either this object or another object related to the runtime context. The value returned by this method is bound to the identifier in the as clause of with statements using this context manager.

An example of a context manager that returns itself is a file object. File objects return themselves from \_\_enter__() to allow open() to be used as the context expression in a with statement.

An example of a context manager that returns a related object is the one returned by decimal.localcontext(). These managers set the active decimal context to a copy of the original decimal context and then return the copy. This allows changes to be made to the current decimal context in the body of the with statement without affecting code outside the with statement.

##### contextmanager.\_\_exit\_\_(exc\_type, exc\_val, exc\_tb)
Exit the runtime context and return a Boolean flag indicating if any exception that occurred should be suppressed. If an exception occurred while executing the body of the with statement, the arguments contain the exception type, value and traceback information. Otherwise, all three arguments are None.

Returning a true value from this method will cause the with statement to suppress the exception and continue execution with the statement immediately following the with statement. Otherwise the exception continues propagating after this method has finished executing. Exceptions that occur during execution of this method will replace any exception that occurred in the body of the with statement.

The exception passed in should never be reraised explicitly - instead, this method should return a false value to indicate that the method completed successfully and does not want to suppress the raised exception. This allows context management code (such as contextlib.nested) to easily detect whether or not an __exit__() method has actually failed.

Python defines several context managers to support easy thread synchronisation, prompt closure of files or other objects, and simpler manipulation of the active decimal arithmetic context. The specific types are not treated specially beyond their implementation of the context management protocol. See the contextlib module for some examples.

Python’s generators and the contextlib.contextmanager decorator provide a convenient way to implement these protocols. If a generator function is decorated with the contextlib.contextmanager decorator, it will return a context manager implementing the necessary __enter__() and __exit__() methods, rather than the iterator produced by an undecorated generator function.

Note that there is no specific slot for any of these methods in the type structure for Python objects in the Python/C API. Extension types wanting to define these methods must provide them as a normal Python accessible method. Compared to the overhead of setting up the runtime context, the overhead of a single class dictionary lookup is negligible.

### 5.12. Other Built-in Types
The interpreter supports several other kinds of objects. Most of these support only one or two operations.

#### 5.12.1. Modules
The only special operation on a module is attribute access: m.name, where m is a module and name accesses a name defined in m‘s symbol table. Module attributes can be assigned to. (Note that the import statement is not, strictly speaking, an operation on a module object; import foo does not require a module object named foo to exist, rather it requires an (external) definition for a module named foo somewhere.)

A special attribute of every module is __dict__. This is the dictionary containing the module’s symbol table. Modifying this dictionary will actually change the module’s symbol table, but direct assignment to the __dict__ attribute is not possible (you can write m.__dict__['a'] = 1, which defines m.a to be 1, but you can’t write m.__dict__ = {}). Modifying __dict__ directly is not recommended.

Modules built into the interpreter are written like this: <module 'sys' (built-in)>. If loaded from a file, they are written as <module 'os' from '/usr/local/lib/pythonX.Y/os.pyc'>.

#### 5.12.2. Classes and Class Instances
See Objects, values and types and Class definitions for these.

#### 5.12.3. Functions
Function objects are created by function definitions. The only operation on a function object is to call it: func(argument-list).

There are really two flavors of function objects: built-in functions and user-defined functions. Both support the same operation (to call the function), but the implementation is different, hence the different object types.

See Function definitions for more information.

#### 5.12.4. Methods
Methods are functions that are called using the attribute notation. There are two flavors: built-in methods (such as append() on lists) and class instance methods. Built-in methods are described with the types that support them.

The implementation adds two special read-only attributes to class instance methods: m.im_self is the object on which the method operates, and m.im_func is the function implementing the method. Calling m(arg-1, arg-2, ..., arg-n) is completely equivalent to calling m.im_func(m.im_self, arg-1, arg-2, ..., arg-n).

Class instance methods are either bound or unbound, referring to whether the method was accessed through an instance or a class, respectively. When a method is unbound, its im_self attribute will be None and if called, an explicit self object must be passed as the first argument. In this case, self must be an instance of the unbound method’s class (or a subclass of that class), otherwise a TypeError is raised.

Like function objects, methods objects support getting arbitrary attributes. However, since method attributes are actually stored on the underlying function object (meth.im_func), setting method attributes on either bound or unbound methods is disallowed. Attempting to set an attribute on a method results in an AttributeError being raised. In order to set a method attribute, you need to explicitly set it on the underlying function object:

~~~python
>>>
>>> class C:
...     def method(self):
...         pass
...
>>> c = C()
>>> c.method.whoami = 'my name is method'  # can't set on the method
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'instancemethod' object has no attribute 'whoami'
>>> c.method.im_func.whoami = 'my name is method'
>>> c.method.whoami
'my name is method'
~~~
See The standard type hierarchy for more information.

#### 5.12.5. Code Objects
Code objects are used by the implementation to represent “pseudo-compiled” executable Python code such as a function body. They differ from function objects because they don’t contain a reference to their global execution environment. Code objects are returned by the built-in compile() function and can be extracted from function objects through their func_code attribute. See also the code module.

A code object can be executed or evaluated by passing it (instead of a source string) to the exec statement or the built-in eval() function.

See The standard type hierarchy for more information.

#### 5.12.6. Type Objects
Type objects represent the various object types. An object’s type is accessed by the built-in function type(). There are no special operations on types. The standard module types defines names for all standard built-in types.

Types are written like this: <type 'int'>.

#### 5.12.7. The Null Object
This object is returned by functions that don’t explicitly return a value. It supports no special operations. There is exactly one null object, named None (a built-in name).

It is written as None.

#### 5.12.8. The Ellipsis Object
This object is used by extended slice notation (see Slicings). It supports no special operations. There is exactly one ellipsis object, named Ellipsis (a built-in name).

It is written as Ellipsis. When in a subscript, it can also be written as ..., for example seq[...].

#### 5.12.9. The NotImplemented Object
This object is returned from comparisons and binary operations when they are asked to operate on types they don’t support. See Comparisons for more information.

It is written as NotImplemented.

#### 5.12.10. Boolean Values
Boolean values are the two constant objects False and True. They are used to represent truth values (although other values can also be considered false or true). In numeric contexts (for example when used as the argument to an arithmetic operator), they behave like the integers 0 and 1, respectively. The built-in function bool() can be used to convert any value to a Boolean, if the value can be interpreted as a truth value (see section Truth Value Testing above).

They are written as False and True, respectively.

#### 5.12.11. Internal Objects
See The standard type hierarchy for this information. It describes stack frame objects, traceback objects, and slice objects.

### 5.13. Special Attributes
The implementation adds a few special read-only attributes to several object types, where they are relevant. Some of these are not reported by the dir() built-in function.

##### object.\_\_dict__
A dictionary or other mapping object used to store an object’s (writable) attributes.

##### object.\_\_methods__
> Deprecated since version 2.2: Use the built-in function dir() to get a list of an object’s attributes. This attribute is no longer available.
##### object.\_\_members__
> Deprecated since version 2.2: Use the built-in function dir() to get a list of an object’s attributes. This attribute is no longer available.

##### instance.\_\_class__
The class to which a class instance belongs.

##### class.\_\_bases__
The tuple of base classes of a class object.

##### class.\_\_name__
The name of the class or type.

The following attributes are only supported by new-style classes.

##### class.\_\_mro__
This attribute is a tuple of classes that are considered when looking for base classes during method resolution.

##### class.mro()
This method can be overridden by a metaclass to customize the method resolution order for its instances. It is called at class instantiation, and its result is stored in __mro__.

##### class.\_\_subclasses__()
Each new-style class keeps a list of weak references to its immediate subclasses. This method returns a list of all those references still alive. Example:

~~~python
>>>
>>> int.__subclasses__()
[<type 'bool'>]
~~~

### Footnotes

1.	Additional information on these special methods may be found in the Python Reference Manual (Basic customization).
2.	As a consequence, the list [1, 2] is considered equal to [1.0, 2.0], and similarly for tuples.
3.	They must have since the parser can’t tell the type of the operands.
4.	(1, 2, 3, 4) Cased characters are those with general category property being one of “Lu” (Letter, uppercase), “Ll” (Letter, lowercase), or “Lt” (Letter, titlecase).
5.	To format only a tuple you should therefore provide a singleton tuple whose only element is the tuple to be formatted.
6.	The advantage of leaving the newline on is that returning an empty string is then an unambiguous EOF indication. It is also possible (in cases where it might matter, for example, if you want to make an exact copy of a file while scanning its lines) to tell whether the last line of a file ended in a newline or not (yes this happens!).


## Reference

1. [The Python Standard Library](https://docs.python.org/2/library/)
2. [Build-in Function](https://docs.python.org/2/library/functions.html)
3. [Build-in Type](https://docs.python.org/2/library/stdtypes.html)

------
