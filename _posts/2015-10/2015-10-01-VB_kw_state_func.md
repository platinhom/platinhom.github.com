---
layout: post
title: VB关键词-过程-语句-常用函数汇总
date: 2015-10-01 08:23:30
categories: Coding
tags: VB
---

<style>ol li{font-size:16px;padding:0;margin:2px 0 2px 36px} ol li strong{font-size:16px;padding:0;}</style>

## 关键词

|End		|If 		|Else 		|Elseif 	|Select 	|Case 		|
|Do 		|Loop 		|While 		|Until 		|Each 		|For 		|
|To 		|Step		|Next 		|With		|Try		|Catch		|
|Finally	|Enum 		|Sub 		|Function	|Return 	|Continue	|
|Exit 		|Property 	|Class 		|Public 	|Private 	|New 		|
|Integer 	|Double 	|ByVal 		|
|Shared 	|Dim		|As 		

## 语句 Statement

- If .. Elseif .. Else .. End If
- Select Case 
- For .. To .. Step .. Next
- For Each .. In .. Next
- Do While\|Until .. Loop 和 Do .. Loop While\|Until ..
- Function
- Sub
- Property
- Try .. Catch .. Finally

- End { Function \| Property \| Select \| Sub \| Try \| While \| With }
- Continue { Do \| For \| While }
- Exit { Do \| For \| Function \| Property \| Select \| Sub \| Try \| While }  

## 内置函数
"Application.DisplayAlerts = False
"							关闭窗口提示
…							
Application.DisplayAlerts = True							
							
1. 字符串相关函数
	1.	Asc	返回一个Integer，代表字符串中首字母的字符代码					
	2.	Chr	返回String，其中包含有与指定的字符代码相关的字符					
	3.	InStr	指定一字符串在另一字符串中最先出现的位置					
	4.	InStrRev*	返回一个字符串在另一个字符串中出现的位置，从字符串的末尾算起					
	5.	LCase	返回转成小写的String					
	6.	BCase	返回Variant(String)，其中包含转成大写的字符串					
	7.	Left	返回Variant(String)，其中包含字符串中从左边算起指定数量的字体					
	8.	Len	返回Long，其中包含字符串内字符的数目或存储变量所需的字节数					
	9.	LTrin	返回Variant(String)，去除指定字符串的前导空格					
	10.	Mid	返回Variant(String)，其中包含字符串中指定数量的字符					
	11.	Reptace*	返回一个字符串，该字符串中指定的子字符串已被替换成另一子字符串，并且替换发生的次数也是指定的。					
	12.	Right	返回Variant(String)，其中包含字符串中从右边算起指定数量的字符					
	13.	RTrim	返回Variant(String)，去除指定字符串的尾随空格					
	14.	Space	返回特定数目空格的Variant(String)					
	15.	Str	返回代表一数值的返回Variant(String)					
	16.	StrComp	返回Variant(String)，为字符串比较的结果					
	17.	StrConv	返回按指定类型转换的Variant(String)					
	18.	String	返回Variant(String)，其中包含指定长度重复字符的字符串					
	19.	StrRcverse*	返回一个字符串，其中一个指定子字符串的字符顺序是反向的０					
	20.	Trim	返回Variant(String)，去除指定字符串的前导和尾随空格																
2. 日期与时间函数							
	21.	Date	返回包含系统日期					
	22.	DateAdd	返回包含一个日期的Variant(Date)，这一日期还加上了一段时间间隔					
	23.	DateDiff	返回Variant(Long)的值，表示两个指定日期间的时间间隔数目					
	24.	DatePart	返回一个包含已知日期的指定时间部分的Variant(Integer)					
	25.	DateSerial	返回包含指定的年、月、日的Variant(Date)					
	26.	DateValue	返回一个Variant(Date)					
	27.	Day	返回一个Variant(Integer)，其值为1~31之间的整数，表示一个月中的某一日					
	28.	Hour	返回一个Variant(Integer)，其值为0~23之间的整数，表示一天之中的某一钟点					
	29.	Minute	返回一个Variant(Integer)，其值为0~59之间的整数，表示一小时中的某分钟					
	30.	Month	返回一个Variant(Integer)，其值为1~12之间的整数，表示一年中的某月					
	31.	MonthName	返回一个表示指定月份的字符串					
	32.	Now	返回一个Variant(Date),根据计算机系统设置的日期和时间来指定日期和时间					
	33.	Time	返回一个指明当前系统时间的Variant(Date)					
	34.	Timer	返回一个Single，代表从午夜开始到现在经过的秒数					
	35.	TimeSerial	返回一个Variant(Date)，包含其有其体时、分、秒的时间					
	36.	TimeValue	返回一个包含时间的Variant(Date)					
	37.	Second	返回一个Variant(Integer)，其值为0~59之间的整数，表示一分钟之中的某个秒					
	38.	Weckday	返回一个.Variant(Integer)，包含一个整数，代表某个日期是星期几					
	39.	WeekdayName*	返回一个字符串，表示一星期中的某天					
	40.	Year	返回Variant(Integer)，包含表示年份的整数								
3. 类型转换函数					
	41.	CBool	将表达式转换为Boolean类型数据					
	42.	CByte	将表达式转换为Byte类型数据					
	43.	Ceur	将表达式转换为Currency类型数据					
	44.	CDate	将表达式转换为Date类型数据					
	45.	CDbl	将表达式转换为Double类型数据					
	46.	CDec	将表达式转换为Decimal类型数据					
	47.	Cint	将表达式转换为Integer类型数据					
	48.	CLng	将表达式转换为Long类型数据					
	49.	CSng	将表达式转换为Single类型数据					
	50.	CStr	将表达式转换为String类型数据					
	51.	Cvar	将表达式转换为Variant类型数据					
	52.	CVDate	返回一个Variant类型数据，它的子类型是Date					
	53.	CVErr	返回一个Variant类型数据，它的子类型是Error					
	54.	Val	返回字符串内的数字											
4. 数组处理函数																
	55.	Array	返回一个包含数组的Variartt					
	56.	Split*	返回一个下标从零开始的一维数组，它包含指定数目的子字符串					
	57.	Filter	返回一个下标从玲开始的数组，该数组包含基于指定筛选条件的一个字符串数组的子集					
	58.	Join*	返回一个字符串，该字符串是通过连接某个数组中的多个子字符串而创建的					
	59.	LBound	返回一个Long型数据，其值为指定数组可用的最小下标					
	60.	UBound	返回一个Long型数据，其值为指定的数组可用的最大下标			
5. 格式化函数			
	61.	Format	返回Variant(String)，其中含有一个表达式，它是根据格式表达式中的指令来格式化的					
	62.	FormatCurrency*	返回一个货币值格式的表达式，它使用系统控制面板中定义的货币符号					
	63.	ForrmatDateTime*	返回一个日期或时间格式的表达式					
	64.	FormatNumber*	返回一个数字格式的表达式					
	65.	FormatPercent*	返回一个百分比格式（乘以100）的表达式，后面有%符号						
6. 数学与三角函数				
	66.	Abs	返回参数的绝对值，其类型和参数相同					
	67.	Atn	返回一个Double，指定一个数的反正切值					
	68.	Cos	返回一个Double，指定一个角的余弦值					
	69.	Exp	返回Double，指定e（自然对数的底）的某次方					
	70.	Fix	返回参数的整数部分					
	71.	Hex	返回代表十六进制数值的String					
	72.	Int	返回参数的整数部分					
	73.	Log	返回一个Double，指定参数的自然对数值					
	74.	Oct	返回Variant(String)，代表一数值的八进制值					
	75.	Rnd	返回一个包含随机数值的Single					
	76.	Round	返回一个数值，该数值是按照指定的小数位数进行四舍五入运算的结果					
	77.	Sgn	返回一个Variant(Integer)，指出参数的正负号					
	78.	Sin	返回一个Double，指定参数的sine（正弦）值					
	79.	Sqr	 返回一个Double，指定参数的平方根					
	80.	Tan	返回一个Double的值，指定一个角的正切值					
7. 文件处理函数	
	81.	FileAttr	返回一个Long，表示使用Open语句打开该文件的方式					
	82.	FileDateTime	返回一个Variant(Date)，此为一个文件被创建或最后修改后的日期和时间					
	83.	FileLen	返回一个Long，代表一个文件的长度，单位是字节					
	84.	FreeFile	返回一个Integer，代表下一个可供Open语句使用的文件号					
	85.	GetAttr	返回一个Integer，此为一个文件、目录或文件夹的属性					
	86.	SetAttr	为一个文件设置属性信息					
	87.	Input	返回String，它包含以Input或Binary方式打开的文件中的字符					
	88.	Loc	返回一个Long，在已打开的文件中指定当前读/写位置					
	89.	EOF	返回一个Integer，它包含Boolean值 True，表明已经到达为Random或顺序 Input打开的文件的结尾					
	90.	LOF	返回一个Long，表明用 Open语句打开的文件的大小，该大小以字节为单位					
	91.	Seek	返回一个Long，在 Open语句打开的文件中指定当前的读／定位置					
	92.	Spc	与Print#语句或Print方法一起使用，对输出进行定位					
	93.	Tab	与Print#语句或Print方法一起使用，对输出进行定位　　							
8.信息函数
	94.	IsArray	返回Boolean值，指出变量是否为一个数组					
	95.	IsDate	返回Boolean值，指出一个表达式是否可以转换成日期					
	96.	IsEmpty	返回Boolean值，指出变量是否已经初始化					
	97.	IsEttor	返回Boolean值，指出表达式是否为一个错误值					
	98.	IsMissing	返回Boolean值，指出一个可选的Varint参数是否已经传递给过程					
	99.	IsNull	返回Boolean值，指出表达式是否不包含任何有效数据（Null）					
	100.	IsNumeric	返回Boolean值，指出表达式的运算结果是否为数					
	101.	IsObject	返回Boolean值，指出标识符是否表示对象变量					
	102.	TypeName	返回一个String，提供有关变量的信息					
	103.	VarType	返回一个Integer，指出变量的子类型					
9. 颜色函数				
	104.	QBColor	返回一个Long，用来表示所对应颜色值的RGB颜色码					
	105.	RGB	返回一个Long整数，用来表示一个RGB颜色值						
10. 财务函数		
	106.	DDB	返回一个Double，指定一笔资产在一特定期间内的折旧可使用双下落收复平衡方法或其他指定的方法进行计算					
	107.	FV	返回一个Double，指定未来的定期定额支付且利率固定的年金					
	108.	IRR	返回一个Double，指定一系列周期性现金流（支出或收入）的内部利率					
	109.	Ipmt	返回一个Double，指定在一段时间内对定期定额支付且利率固定的年金所支付的利息值					
	110.	MIRR	返回一个Double，指定根据一系列修改过的周期性现金流（支付和收入）的内部利率					
	111.	NPer	返回一个Double，指定定期定额支付且利率固定的总期数					
	112.	NPV	返回一个Double，指定根据一系列定期的现金流（支付和收入）和贴现率而定的投资净现值					
	113.	Pmt	返回一个Double，指定根据定期定额支付且利率固定的年金支付额					
	114.	Ppmt	返回一个Double，指定在定期定额支付且利率固定的年金的指定期间内的本金偿付额					
	115.	PV	返回一个Double指定在未来定期、定额支付且利率固定的年金现值					
	116.	Rate	返回一个Double，指定每一期的年金利率					
	117.	SLN	返回一个Double，在一期里指定一项资产的直线折旧					
	118.	SYD	返回一个Double，指定某项资产在一指定期间用年数总计法计算的折旧						
11. 判断函数				
	119.	Choose	从参数列表中选择并返回一个值					
	120.	IIF	根据表达式的值，来返回两部分中的一个					
	121.	Switch	计算一组表达式列表的值，然后返回与表达式列表中最先为True的表达式所相关的Variant数组或表达式			
12. 目录函数
	122.	CurDir	返回一个Variant(String)，用来代表当前的路径					
	123.	Dir	返回 一个String，用来表示一个文件名，目录名或文件夹名称，它必须与指定的模式或文件属性、磁盘卷标相匹配					
	124.	ChDir	改变当前的目录或文件夹					
	125.	ChDrive	改变当前的驱动器					
	126.	MkDir	创建一个新的目录或文件夹					
	127.	RmDir	删除一个存在的目录或文件夹
13. 其他函数			
	128.	CallByName*	执行一个对象的方法，或者设置或返回一个对象的属性					
	129.	CreateObject	创建并返回一个对ActiveX对象的引用					
	130.	DoEvents	转让控制权，以便让操作系统处理其他的事件					
	131.	Envnon	返回String，它关连于一个操作系统环境变量在Macintosh中不可用					
	132.	Err	含有关于运行时错误的信息					
	133.	Error	返回对应于已知错误的信息					
	134.	GetAllSetrings	从Windows注册表或（ Macintosh中）应用程序初始化文件的信息中返回应用程序项目的所有注册表项设置及其相应值（开始是由 SaveSetting产生）					
	135.	GetObject	返回文件中的ActiveX对象的引用					
	136.	GetSetting	从Windows注册表或（ Macintosh中）应用程序初始化文件的信息中返回应用程序项目的所有注册表项设置及其相应值					
	137.	InputBox	在一对话框来中显示提示，等待用户输入正文或按下按钮，并返回包含文本框内容的String					
	138.	MsgBox	在对话框中显示消息，等待用户单击按钮，并返回一个Integer告诉用户单击哪一个按钮					
	139.	Partition	返回一个Variant(String)，指定一个范围，在一系列计算的范围中指定的数字出现在这个范围内					
	140.	Shell	执行一个可执行文件，返回一个Variant(Date），如果成功的话，代表这个程序的任务ID，若小成功，则会返回0

## 指令 (编译时控制)

- #Const
- #ExternalSource
- #If ..Then..#End if
- #Region
- #Disable, #Enable

~~~vb
#If expression Then
   statements
[ #ElseIf expression Then
   [ statements ] ]
[ #Else
   [ statements ] ]
#End If
~~~

------
