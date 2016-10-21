---
layout: post_small
title: Excel函数总结
date: 2015-09-03 20:10:10
categories: IT
tags: Excel
---

<style>
strong{font-size:16px;}
</style>


## 基本知识

### 运算符

- `:` :范围运算符,对于一个区域时使用
- `,`  :单元格区域并集运算符.
- ` `  :(单一空格)单元格区域交集运算符.例如`(B7:D7 C6:C8)`返回C7
- `$`      :绝对引用
- `&`      :字符串拼接
- `'`       :在单元格开头时标记为字符串而非数值型
- `".."`	 :表明是字符串
- `=`和`<>`  :相等和不等判断
- `^`  :求幂  `%`  :百分比
- `4**5`: 就是4E5的意思
- `*`和`?`: 通配符,尤其在查找等时适用.若要查找\*则要使用`~*`.支持通配函数如SUMIF,SUMIFS,COUNTIF,AVERAGEIF等.
- `~`: 转义字符...

### 技巧:

1. 将函数形式转为结果: 复制区域数据, 然后右键选择性黏贴, 这时选数值, 函数的值就被粘过来了.注意hyperlink不行
2. 绝对引用: A88=$A$88, 注意可以固定A或88, 按F4整体改变
3. 转置(行列转置)一般使用选择性黏贴->转置实现,也可以用TRANSPOSE函数
4. **数组公式**: 有些公式是某些函数返回值是数组,显示上是`{=transpose(A1:B3)}`这样.这个大括号表示数组公式.返回时会对相应选择的区域进行相应的对应数组位置的处理.输入公式后,需要按下**CTRL+SHIFT+ENTER**来起效(就是加上这个大括号)!


内置函数:
------

## 运算和数值统计

运算对象一般可以是地址,可以是数值,有些函数支持区域.

### 单数值处理

- **SQRT**(number): 求平方根.
- **POWER**(value,n):求value^n 次方 
- **ABS**(number): 求出相应数字的绝对值。  
如果number参数不是数值，而是一些字符（如A等），则B2中返回错误值“#VALUE！”。
- **INT**(number)：将数值向下取整为最接近的整数。
- **MOD**(A,B): 求出两数相除A/B的余数。  
如果B为零，则显示错误值“#DIV/0!”；MOD函数可以借用函数INT来表示：上述公式可以修改为：=13-4*INT(13/4)。
- **FACT**(value):阶乘到value. 非整数会截尾处理.
- **GCD**/**LCM**(number1, [number2], ...): 求最大公约数/最小公倍数.
- **RAND**(): 产生[0,1) 的随机数.每次计算工作表时都会更新..
- **RANDBETWEEN**(bottom, top): 产生[bottom, top]之间的随机整数.
- **MOD**(number, divisor)：求余,number/divisor. 注意结果的符号与除数相同. `MOD(n, d) = n - d*INT(n/d)`
- **QUOTIENT**(number, divisor): 返回除法number/divisor的整数部分. 和int(number)有不同:对负数时(-10/3),前者返回-3,int返回-4.
- **CEILING**(number, significance): 向上取整到最接近significance倍数的值.例如整数取整significance=1,可以0.1,2等(如两者都是负数,实际向下取整..).


### 区域数值处理

#### 求和和平均
- **SUM**(Number1,Number2……)：计算所有参数数值的和。  
如果参数为数组或引用，只有其中的数字将被计算。数组或引用中的空白单元格、逻辑值、文本或错误值将被忽略；如果将上述公式修改为：=SUM(LARGE(D2:D63,{1,2,3,4,5}))，则可以求出前5名成绩的和。
- **SUMSQ**(Number1,Number2……)：计算所有参数数值的平方的和。 
- **SUMPRODUCT**(array1, [array2], [array3], ...): 在给定的几组数组中，将数组间对应的元素相乘，并返回乘积之和。
- **SUMXMY2**(array\_x, array\_y): 两组数据对应值的差的平方和. =SUMSQ(arrXi-arrYi)
- **SUMX2PY2**(array\_x, array\_y): 两组数据对应值的平方的和.=SUM(arrXi^2+arrYi^2)
- **SUMX2MY2**(array\_x, array\_y): 两组数据对应值的平方的差.=SUM(arrXi^2-arrYi^2)
数组必须具有相同维数,否则返回错误值.非数值型元素作0处理.
- **SUMIF**(条件判断的区域,条件表达式,需要计算的数值所在的单元格区域）：计算符合指定条件的单元格区域内的数值和。条件表达式如值,">10"这样.
- **AVERAGE**(number1,number2,……): 求出所有参数的算术平均值。    
如果引用区域中包含“0”值单元格，则计算在内；如果引用区域中包含空白或字符单元格，则不计算在内。
- **AVEDEV**(number1, [number2], ...): 返回一组数据点到其算术平均值的绝对偏差的平均值,等于AVERGER(Xi-Averger(range)). AVEDEV 是对一组数据中变化性的度量。
- **DEVSQ**(number1, [number2], ...):返回各数据点与数据均值点之差（数据偏差）的平方和。即SUMSQ(Xi-Averger(range)).
- **STDEV**(number1, [number2], ...):根据样本估计标准偏差。即SQRT(SUMSQ(Xi-Averger(range))/(n-1)).
- **VAR**(number1, [number2], ...):根据样本估计方差。即SUMSQ(Xi-Averger(range))/(n-1).

#### 统计值
- **MAX**/**MIN**(number1,number2……)：求出一组数中的最大值/最小值。如果参数中有文本或逻辑值，则忽略。
- **LARGE**/**SMALL**(array,k)：返回数据集中的第 k 个最大/小值。k为1时等价于max/min
- **COUNTIF**(Range,Criteria)：统计某个单元格区域中符合指定条件的单元格数目。 
Range代表要统计的单元格区域；Criteria表示指定的条件表达式,如">=80"。允许引用的单元格区域中有空白单元格出现。
- **DCOUNT**(database,field,criteria)：返回数据库或列表的列中满足指定条件并且包含数字的单元格数目。  
参数说明：Database表示需要统计的单元格区域；Field表示函数所使用的数据列（在第一行必须要有标志项）；Criteria包含条件的单元格区域。
应用举例：如图1所示，在F4单元格中输入公式：=DCOUNT(A1:D11,"语文",F1:G2)，确认后即可求出“语文”列中，成绩大于等于70，而小于80的数值单元格数目（相当于分数段人数）。
特别提醒：如果将上述公式修改为：=DCOUNT(A1:D11,,F1:G2)，也可以达到相同目的。
- **FREQUENCY**(data\_array,bins\_array)：以一列垂直数组返回某个区域中数据的频率分布。   
Data\_array表示用来计算频率的一组数据或单元格区域；Bins\_array表示为前面数组进行分隔的一列界限数值,例如分别有10,20,30,则表示区分为<=10,(10-20),[20,30),>=30四个区间。
返回值是垂直数组,所以要选择一列(bins数+1)作为接受结果，输入完成公式后按下“Ctrl+Shift+Enter”组合键进行公式数组确认，即可求出各段数值的出现频率数目。
- **RANK**(Number,ref,order）：返回某一数值在一列数值中的相对于其他数值的排位。  
Number代表需要排序的数值；ref代表排序数值所处的单元格区域；order代表排序方式参数（如果为“0”或者忽略，则按降序排名；如果为非“0”值，则按升序排名）。
- **SUBTOTAL**(function_num, ref1[, ref2, ...])：返回列表或数据库中的分类汇总。参考[link](https://support.office.com/zh-cn/article/SUBTOTAL-%E5%87%BD%E6%95%B0-7b027003-f060-4ade-9040-e478765b9939)  
Function_num为1到11（包含隐藏值）或101到111（忽略隐藏值）之间的数字，用来指定使用什么函数在列表中进行分类汇总计算;ref1, ref2,……代表要进行分类汇总区域或引用，不超过29个。  
如果采取自动筛选，无论function_num参数选用什么类型，SUBTOTAL函数忽略任何不包括在筛选结果中的行；SUBTOTAL函数适用于数据列或垂直区域，不适用于数据行或水平区域。  

### 矩阵处理

- **TRANSPOSE**(array): 转置矩阵.返回转置后的数组.注意这里先选择放置转置数据的区域,再输入公式并选择原始数据,最后使用数组公式处理ctrl+shift+enter.最好使用绝对位置.

## 文本类

- **LEN**(text)：统计文本字符串中字符数目。  
LEN要统计时，无论中全角字符，还是半角字符，每个字符均计为“1”；与之相对应的一个函数——**LENB**，在统计时半角字符计为“1”，全角字符计为“2”。
- **CONCATENATE**(Text1，Text……)：将多个字符文本或单元格中的数据连接在一起，显示在一个单元格中。效果和 `&` 基本相同  
如果参数不是引用的单元格，且为文本格式的，请给参数加上英文状态下的双引号.
- **TRIM**(text): 除了单词之间的单个空格外，清除文本中所有的空格。在从其他应用程序中获取带有不规则空格的文本时，可以使用函数TRIM。
- **CLEAN**(text): 删除字符串中不能打印的字符.
- **REPT**(text,num): 重复text内容num次.
- **LEFT**(text,num_chars)：从一个文本字符串的第一个字符开始，截取指定数目的字符。可参考RIGHT.另有**LEFTB**
- **RIGHT**(text,num\_chars)：从一个文本字符串的最后一个字符开始，截取指定数目的字符。另有**RIGHTB**  
参数说明：text代表要截字符的字符串；num_chars代表给定的截取数目。**
Num\_chars参数必须大于或等于0，如果忽略，则默认其为1；如果num\_chars参数大于文本长度，则函数返回整个文本。
- **MID**(text,start\_num,num\_chars)：从一个文本字符串的指定位置开始，截取指定数目的字符。另有**MIDB**  
text代表一个文本字符串；start\_num表示指定的起始位置；num\_chars表示要截取的数目。
- **EXACT**(text1,text2): 判断两个字符串是否完全一致(不包括显示格式).区分大小写.返回对错.
- **FIND**(findtext,intext[,start]): 查找在intext中的findtext的位置,区分大小写.返回位置.第三参数指定开始查找的位置(只能大于0),默认1.找不到返回错误值#VALUE!.
- **SEARCH**(findtext,intext,[start_num]): 查找在intext中的findtext的位置,不区分大小写.返回位置.和FIND类似但不区分大小写,而且findtext部分支持通配符,FIND不支持.
- **REPLACE**(oldtext, startnum, numchars, newtext): oldtext中startnum起将numchars个字符替换为newchars.即startnum, numchars定义出替换的地方,newtext为替换内容.
- **SUBSTITUTE**(text, oldtext, newtext, [instance\_num]):查找text中的oldtext并替换为newtext.第四参数为替换最大次数,否则全部替换.

### 转换格式

- **T**(text): 函数转为文本 (http://www.360doc.com/content/13/0107/15/83610_258773240.shtml)
- **TEXT**(value,format_text)：根据指定的数值格式将相应的数字转换为文本形式。[Text](https://support.office.microsoft.com/zh-tw/article/TEXT-%E5%87%BD%E6%95%B8-29cea14b-bd86-426c-9985-cb2f0b19df58?CorrelationId=0ebeeaca-58d9-40c4-84d1-9b64ac192a9d&ui=zh-TW&rs=zh-TW&ad=TW  )  
- **VALUE**(text): 将字符串转为数值,包括数字,日期时间格式.若不是这些格式会返回错误#VALUE!.
value代表需要转换的数值或引用的单元格；format_text为指定文字形式的数字格式。如保存有数值1280.45，输入公式：=TEXT(B1, "$0.00"), 确认后显示为“$1280.45".
- **LOWER**(text): 将一个文字串中的所有大写字母转换为小写字母。
- **UPPER**(text): 将文本所有字母转换成大写形式.
- **PROPER**(text): 将文字串的首字母及任何非字母字符之后的首字母转换成大写。将其余的字母转换成小写。
- **JIS**(text): 将字符串中的半角（单字节）英文字母或片假名更改为全角（双字节）字符。
- **ASC**(text): 将字符串中的全角（双字节）英文字母或片假名更改为半角（单字节）字符。
- **WIDECHAR**(text): 单字节字符转为双字节字符.
- **CHAR**(num): 将ascii数字转为字符.
- **CODE**(text):　返回字符串中第一个字符的数字代码，char的逆运算.
- **ENCODEURL**(text): 将网址转为url串,尤其中文处理.
- **DOLLAR**(value,decimal): 将数值转为相应小数点decimal位的美元格式,会进行四舍五入.如 *$1.23*
- **FIXED**(value,decimal[,no_commas]): 将数组四舍五入到指定小数位数.以文本形式返回结果.第三个参数若TRUE是不输出三位数输出时的逗号(默认false).

## 查找/定位数据

- **MATCH**(查找值,查找的连续区域,匹配方式)：返回在指定方式下与指定数值匹配的数组中元素的相应位置。  
如果匹配方式为-1，查找大于或等于查找值的最小数值，此时查找区域必须按降序排列; 若为1，查找小于或等于查找值的最大数值，此时查找区域必须按升序排列; 若为0，查找等于查找值 的第一个数值，查找区域可以按任何顺序排列；如果省略match_type，则默认为1。查找区域只能为一列或一行。
- **INDEX**(array,行号,列号)：返回列表或数组中的元素值，此元素由行序号和列序号的索引值进行确定。  
Array代表单元格区域或数组常量；如果省略行号，则必须有列号。可以用match函数用来定位某行.此处的行序号和列序号是相对于所引用的单元格区域而言的，不是Excel工作表中的行或列序号。  
index(范围2, match(值,范围1)) 可以查找在范围1的某列中某值的位置并返回该位置别的行的相应值
- **OFFSET**(reference, rows, cols, [height], [width]): 对某个单元格进行偏移(下右为正值,上左为负值)获取偏移后单元格的值.最后两个参数是引用的行高和列宽(ref可以是range,默认行列数和range一致,但也可以另外指定,此时会返回指定大小的range).
- **INDIRECT**(字符串):将字符串转换为相应的位置.   
如表示某格,原来是'sheet名'!A6 这样, 可以用INDIRECT("'8-" & B10 & "' ! A6") 去引用,假设B10储存了部分sheet名,8-是公有sheet名.indirect 函数只能引用打开的工作薄.
- **COLUMN**(reference)：显示所引用单元格的列标号值。reference为引用的单元格,不输入为当前列.  
如果在B11单元格中输入公式：=COLUMN()，显示出2.
- **ROW**(reference): 返回行标号值.
- **COLUMNS**(reference)：显示区域的列数
- **ROWS**(reference): 返回区域的行数.
- **Hyperlink**(link,name): 超链接,变量1是连接变量2是显示下划线名字.
关于自动超链接:在excel选项中找到自动更正选项-> 自动套用格式, 勾选替换为超链接. 点击超链接的cell, 然后在数值栏处enter一下就OK

## 功能类

### 逻辑类

- **IF**(逻辑判断表达式,正确时的值[,错误时的值])：根据对指定条件的逻辑判断的真假结果，返回相对应的内容。  
逻辑判断表达式如"C10>80";正确时的值表示当判断条件为逻辑“真”时的显示内容，如果忽略返回“TRUE”；错误时的值表示当判断条件为逻辑“假”时的显示内容，如果忽略返回“FALSE”。  
- **OR**(logical1,logical2, ...): 返回所有值的OR逻辑。
- **AND**(logical1,logical2, ...): 返回所有值的AND逻辑。   
- **NOT**(logical): 取反返回逻辑值.
如果指定的逻辑条件参数中包含非逻辑值时，则函数返回错误值“#VALUE!”或“#NAME”。
- **ISERROR**(value)：用于测试函数式返回的数值是否有错。如果有错，该函数返回TRUE，反之返回FALSE。  
Value表示需要测试的值或表达式。此函数通常与IF函数配套使用，如果公式为：=IF(ISERROR(A35/B35),"",A35/B35)，如果B35为空或“0”，则相应的单元格显示为空，反之显示A35/B35的结果。
- **ISERR**(value): 是否任意错误值(除去#N/A). ISERROR则包括#N/A
- **ISEVEN**/**ISODD**(value): 是否偶数/基数
- **ISNUMBER**/**ISTEXT**/**ISNONTEXT**/**ISLOGICAL**(value): 是否数字/文本/非文本(空单元格也是TRUE)/逻辑型
- **ISBLANK**/**ISREF**/**ISNA**(value): 是否空单元格/引用/错误值#N/A(不存在)

### 时间日期相关

serial_number是日期格式,例如"2013-8-20".

- **DATE**(year,month,day)：给出指定数值的日期(返回日期格式)。  year为指定的年份数值（小于9999）；month为指定的月份数值（可以大于12）；day为指定的天数.(超过公历值会进位,例如13月=下年1月)
- **NOW**()：给出当前系统日期和时间。该函数不需要参数。  
显示出来的日期和时间格式，可以通过单元格格式进行重新设置。如果系统日期和时间发生了改变，只要按一下F9功能键，即可让其随之改变。
- **YEAR**(serial_number)：求出指定日期或引用单元格中的日期的年份。(年,y)
- **MONTH**(serial_number)：求出指定日期或引用单元格中的日期的月份。(月,m)
- **DAY**(serial_number)：求出指定日期或引用单元格中的日期的天数。(日,d)  
如果是给定的日期，请包含在英文双引号中。
- **DATEDIF**(data1,data2,unit)：计算返回两个日期参数的差值。  
unit为"y","m","d",即指明相减的单位为年/月/日.  这是Excel中的一个隐藏函数，在函数向导中是找不到的，可以直接输入使用，对于计算年龄、工龄等非常有效。



## Reference

1. [Office官方:计算运算符和运算顺序](https://support.office.microsoft.com/zh-cn/article/%E8%AE%A1%E7%AE%97%E8%BF%90%E7%AE%97%E7%AC%A6%E5%92%8C%E8%BF%90%E7%AE%97%E9%A1%BA%E5%BA%8F-8fdfc95f-62b5-4b8d-8d5a-d089e7dbb8e9?ui=zh-CN&rs=zh-CN&ad=CN)
2. [Office官方:Excel 函数（按类别列出）](https://support.office.com/zh-cn/article/Excel-%E5%87%BD%E6%95%B0%EF%BC%88%E6%8C%89%E7%B1%BB%E5%88%AB%E5%88%97%E5%87%BA%EF%BC%89-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb?ui=zh-CN&rs=zh-CN&ad=CN)


------
