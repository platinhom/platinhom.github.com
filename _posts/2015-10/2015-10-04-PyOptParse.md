---
layout: post
title: Python分析命令行输入:OptParse模块
date: 2015-10-04 07:42:22
categories: Coding
tags: Python
---

要自己定制程序的参数选项控制, 以前我们自己也有optparser, 但python就自带了! 真好!! 之前一直很暴力直接使用sys.argv,直接调用, 因为bash也用习惯了..不过要做些大点的, 还是要借用optparse的. 这里只介绍optparse. 

optparse支持一般性GNU的选项方法,包括:

- 无参选项, -v
- 有参选项, -p value, --para=value
- 值参一体, -pvalue (不支持长参数)
- 合并选项, -abc, -abcp value (最后一个可以是有参, 其余均无参)

解析时, 要是`--`直接读后面的值; 要是`-`, 就看后面的值, 要是无参的, 那继续读下一个; 要是有参的,就把参数读进来(分隔或一体).


optparse现在不再更新了,更新版本叫argparse..和其余的都不介绍了..可以参考ref1.

## optparse module

### 类级别

~~~python
exceptions.Exception(exceptions.BaseException)
    OptParseError
        BadOptionError
        OptionError
            OptionConflictError
        OptionValueError
HelpFormatter
    IndentedHelpFormatter
    TitledHelpFormatter
Option
OptionContainer
    OptionGroup
    OptionParser
Values
~~~

### OptionParser类
我们一般只使用其 OptionParser 这个类:

~~~python
class OptionParser(OptionContainer):
	# Class attributes:
	#   standard_option_list : [Option]
	#     list of standard options that will be accepted by all instances
	#     of this parser class (intended to be overridden by subclasses).

	# Instance attributes:
	#   usage : string
	#     a usage string for your program.  Before it is displayed
	#     to the user, "%prog" will be expanded to the name of
	#     your program (self.prog or os.path.basename(sys.argv[0])).
	#   prog : string
	#     the name of the current program (to override
	#     os.path.basename(sys.argv[0])).
	#   description : string
	#     A paragraph of text giving a brief overview of your program.
	#     optparse reformats this paragraph to fit the current terminal
	#     width and prints it when the user requests help (after usage,
	#     but before the list of options).
	#   epilog : string
	#     paragraph of help text to print after option help

	#   option_groups : [OptionGroup]
	#     list of option groups in this parser (option groups are
	#     irrelevant for parsing the command-line, but very useful
	#     for generating help)

	#   allow_interspersed_args : bool = true
	#     if true, positional arguments may be interspersed with options.
	#     Assuming -a and -b each take a single argument, the command-line
	#       -ablah foo bar -bboo baz
	#     will be interpreted the same as
	#       -ablah -bboo -- foo bar baz
	#     If this flag were false, that command line would be interpreted as
	#       -ablah -- foo bar -bboo baz
	#     -- ie. we stop processing options as soon as we see the first
	#     non-option argument.  (This is the tradition followed by
	#     Python's getopt module, Perl's Getopt::Std, and other argument-
	#     parsing libraries, but it is generally annoying to users.)

	#   process_default_values : bool = true
	#     if true, option default values are processed similarly to option
	#     values from the command line: that is, they are passed to the
	#     type-checking function for the option's type (as long as the
	#     default value is a string).  (This really only matters if you
	#     have defined custom types; see SF bug #955889.)  Set it to false
	#     to restore the behaviour of Optik 1.4.1 and earlier.

	#   rargs : [string]
	#     the argument list currently being parsed.  Only set when
	#     parse_args() is active, and continually trimmed down as
	#     we consume arguments.  Mainly there for the benefit of
	#     callback options.
	#   largs : [string]
	#     the list of leftover arguments that we have skipped while
	#     parsing options.  If allow_interspersed_args is false, this
	#     list is always empty.
	#   values : Values
	#     the set of option values currently being accumulated.  Only
	#     set when parse_args() is active.  Also mainly for callbacks.

	# Because of the 'rargs', 'largs', and 'values' attributes,
	# OptionParser is not thread-safe.  If, for some perverse reason, you
	# need to parse command-line arguments simultaneously in different
	# threads, use different OptionParser instances.

	# Methods defined here:

	# __init__(self, usage=None, option_list=None, option_class=<class optparse.Option>, version=None, conflict_handler='error', description=None, formatter=None, add_help_option=True, prog=None, epilog=None)

	# add_option_group(self, *args, **kwargs)

	# check_values(self, values, args)
	#     check_values(values : Values, args : [string])
	#     -> (values : Values, args : [string])

	#     Check that the supplied option values and leftover arguments are
	#     valid.  Returns the option values and leftover arguments
	#     (possibly adjusted, possibly completely new -- whatever you
	#     like).  Default implementation just returns the passed-in
	#     values; subclasses may override as desired.

	# destroy(self)
	#     Declare that you are done with this OptionParser.  This cleans up
	#     reference cycles so the OptionParser (and all objects referenced by
	#     it) can be garbage-collected promptly.  After calling destroy(), the
	#     OptionParser is unusable.

	# disable_interspersed_args(self)
	#     Set parsing to stop on the first non-option. Use this if
	#     you have a command processor which runs another command that
	#     has options of its own and you want to make sure these options
	#     don't get confused.

	# enable_interspersed_args(self)
	#     Set parsing to not stop on the first non-option, allowing
	#     interspersing switches with command arguments. This is the
	#     default behavior. See also disable_interspersed_args() and the
	#     class documentation description of the attribute
	#     allow_interspersed_args.

	# error(self, msg)
	#     error(msg : string)

	#     Print a usage message incorporating 'msg' to stderr and exit.
	#     If you override this in a subclass, it should not return -- it
	#     should either exit or raise an exception.

	# exit(self, status=0, msg=None)

	# expand_prog_name(self, s)

	# format_epilog(self, formatter)

	# format_help(self, formatter=None)

	# format_option_help(self, formatter=None)

	# get_default_values(self)

	# get_description(self)

	# get_option_group(self, opt_str)

	# get_prog_name(self)

	# get_usage(self)

	# get_version(self)

	# parse_args(self, args=None, values=None)
	#     parse_args(args : [string] = sys.argv[1:],
	#                values : Values = None)
	#     -> (values : Values, args : [string])

	#     Parse the command-line options found in 'args' (default:
	#     sys.argv[1:]).  Any errors result in a call to 'error()', which
	#     by default prints the usage message to stderr and calls
	#     sys.exit() with an error message.  On success returns a pair
	#     (values, args) where 'values' is an Values instance (with all
	#     your option values) and 'args' is the list of arguments left
	#     over after parsing options.

	# print_help(self, file=None)
	#     print_help(file : file = stdout)

	#     Print an extended help message, listing all options and any
	#     help text provided with them, to 'file' (default stdout).

	# print_usage(self, file=None)
	#     print_usage(file : file = stdout)

	#     Print the usage message for the current program (self.usage) to
	#     'file' (default stdout).  Any occurrence of the string "%prog" in
	#     self.usage is replaced with the name of the current program
	#     (basename of sys.argv[0]).  Does nothing if self.usage is empty
	#     or not defined.

	# print_version(self, file=None)
	#     print_version(file : file = stdout)

	#     Print the version message for this program (self.version) to
	#     'file' (default stdout).  As with print_usage(), any occurrence
	#     of "%prog" in self.version is replaced by the current program's
	#     name.  Does nothing if self.version is empty or undefined.

	# set_default(self, dest, value)

	# set_defaults(self, **kwargs)

	# set_process_default_values(self, process)

	# set_usage(self, usage)

	# ----------------------------------------------------------------------
	# Data and other attributes defined here:

	# standard_option_list = []

	# ----------------------------------------------------------------------
	# Methods inherited from OptionContainer:

	# add_option(self, *args, **kwargs)
	#     add_option(Option)
	#     add_option(opt_str, ..., kwarg=val, ...)

	# add_options(self, option_list)

	# format_description(self, formatter)

	# get_option(self, opt_str)

	# has_option(self, opt_str)

	# remove_option(self, opt_str)

	# set_conflict_handler(self, handler)

	# set_description(self, description)
~~~

## OPTIONS 类:

~~~python
   class Option
	#  Instance attributes:
	#    _short_opts : [string]
	#    _long_opts : [string]
	#
	#    action : string
	#    type : string
	#    dest : string
	#    default : any
	#    nargs : int
	#    const : any
	#    choices : [string]
	#    callback : function
	#    callback_args : (any*)
	#    callback_kwargs : { string : any }
	#    help : string
	#    metavar : string
	#
	#  Methods defined here:
	#
	#  __str__(self)
	#
	#  check_value(self, opt, value)
	#
	#  convert_value(self, opt, value)
	#
	#  get_opt_string(self)
	#
	#  process(self, opt, value, values, parser)
	#
	#  take_action(self, action, dest, opt, value, values, parser)
	#
	#  takes_value(self)
~~~

ATTRS: action, type, dest, default, nargs, const, choices, callback, callback\_args, callback\_kwargs, help, metava

ACTIONS: store,store\_const,store\_true, store\_false, append, append\_const, count, callback, help, version

TYPES: 'string', 'int', 'long', 'float', 'complex', 'choice' 

## 基本用法:

1. 载入OptionParser类,新建对象: OptionParser()
2. 添加选项: add_option(...)
3. 参数解析: parse_args()

~~~python
from optparse import OptionParser 
parser = OptionParser() 
parser.add_option("-i", "--input", action="store", 
                  dest="input", 
                  help="read input data from input file") 
parser.add_option("-o", "--output", action="store", 
                  dest="output",  
                  help="write data to output file") 
parser.add_option("-v", "--version", action="store_true",
				  dest="version", default=False,
				  help="print the version")
parser.add_option("-q", "--quite", action="store_false",
				  dest="version",
				  help="don't print the version")

(options, args) = parser.parse_args() 

if options.input=="": 
    print 'input is blank' 
if options.version==True: 
    print 'version 1.0'
~~~

### 新建对象

`parser=OptionParser()` 

形参包括:

`__init__(self, usage=None, option_list=None, option_class=<class optparse.Option>, version=None, conflict_handler='error', description=None, formatter=None, add_help_option=True, prog=None, epilog=None)`

常用usage,version, description 指明一些相关帮助信息, formatter是help输出的格式化器.

prog是程序名,用于help等里面使用输出程序名, 可以不受sys.argv[0]文件名影响.

### 新建选项

两个方法: add\_option, add\_option\_group, add\_options

#### add_option(...): 

前面的是参数选项, 支持多个选项(等价), 一般就是前面短名后面长名. 其实实参化形参名:

- **dest**: 可以决定后来取值时的名字(parse后的options的属性名), 尤其适于有多个等价参数. 不指定时就是选项不加-的字符串.
- type: 默认选项对于的值是字符串, 这里可以指定别的类型
- **default**: 缺省值. 没有设置缺省值的为None,"".
- **help**: -h选项使用时打印的help.
- metavar: 表示显示到help中option的默认值；
- choices: 当设置type为choices时，需要设置此值
- const: 指定一个常量值给选项, 该常量值将用于后面store\_const和append\_const,一起合用.
- **action**: 很重要的选项. 控制对选项和参数处理,像无参数选项处理.
	- **store**: 储存值到属性,强制要求后面提供参数; (缺省)
	- **store\_true**: 当使用该选项时,后面的dest将设置为true. 不跟参数.
	- store\_false: 当使用该选项时,后面的dest将设置为false. 常配合另一个store_true选项使用同一个dest时使用. 不跟参数
	- **append**: 将后面的值追加到dest的列表中, 必须跟参数.
	- **store_const**: 将相应const对于的值储存给dest,常用于同dest名2个以上选项时的处理. 不跟参数.
	- append_const: 将相应const的值追加给dest列表. 不跟参数
	- count: 使用后将给后面的计数器加1,可以统计参数中出现次数.用途不大. 不跟参数.
	- callback: 后面指定回调函数名(不加括号),会将相应opt和args传给回调函数.[详细](https://docs.python.org/2/library/optparse.html). 
	- help, version: 对应为帮助和版本. 要另外自己设计时使用

##### 相关函数:

- set_default(dest1=value1,dest2=value2..): 可以用来同时设置多个选项的默认参数
- has_option(opt): 检查是否有相应选项(使用相应-f里的f)
- remove_option(opt): 删除选项(使用相应-f里的f)


#### add\_option\_group(.)
如果options很多的时候，可以进行分组. 分组的好处是, 有独立的description那些, 可以另外处理, 例如对一些列程序参数, 可以分一个组.使用如下：

~~~python
group = OptionGroup(parser) #创建分组
group.add_option() ##添加选项
parser.add_option_group(group) #将分组加入到解释器
~~~

#### add\_options([Option1,...])

将各个Option对象放在一个列表里再一起添加...意义不大.

### 参数解析

- 默认使用`parse_args()`是传递sys.argv[1:]作为参数, 也可以人为传递一个命令行参数列表到 `parse_args(list)`。
- parse_args() 返回的两个值：
	- **options**，它是一个对象（optpar.Values），保存有命令行参数值。只要知道命令行参数名，如input，就可以访问其对应的值： options.input 。
	- **args**，它是没被解析的命令行参数的列表。例如第一个不被处理的作为输入文件这种方式.

### 帮助文档

默认自动带有-h和--help来输出帮助文档, 输出后程序终止.

帮助文档由两部分组成: 第一部分是程序运行usage帮助, 第二部分是description描述, 第三部分是选项以及选项说明(选项加入时定义). -h, --help自动加入, 不用自己写.

usage帮助部分一般在OptionParser初始化时输入,为第一个参数, 也可以用具体形参名指定,如hstr是一个帮助文档解释字符串,`OptionParser(hstr)`就可以指定usage. 另外, `usage = "%prog [options] arg1 arg2"`中**%prog**会自动替换为程序名, [-options]表示选项及对应值, arg1,arg2是储存在args没被解释的参数中对应顺序的值.

描述部分需要使用OptionParser的`description`形参来指明.

OptionParser的形参version可以指定`--version`输出的字符串, 同样支持**%prog**, 如`version="%prog 1.0"`

get\_usage(), get\_description(), get\_version(): 获得对应的字符串.

print\_help(), print\_usage(), print\_description(), print\_version(): 输出相应内容

error(str): 出错并输出str.

## Reference
1. [Python中的命令行解析工具介绍](http://lingxiankong.github.io/blog/2014/01/14/command-line-parser/)
2. [python帮助的说明](https://docs.python.org/2/library/optparse.html)与[源文件](https://hg.python.org/cpython/file/2.7/Lib/optparse.py)

------
