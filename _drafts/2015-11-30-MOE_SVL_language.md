---
layout: post_small
title: MOE:SVL函数
date: 2015-11-30 06:46:56
categories: CompCB
tags: Software
---

[MOE2010-Help](http://platinhom.github.io/ManualHom/MOE/moe2010/html/). 转自老的有道笔记(居然以前写了这么多啊...).

## MASK和Tagged向量
- get [vector,index\_list]~~读向量中index索引号的元素==v[index_list]如v[[2,3,4]],取单元素可用v(1),v[1]. 
- put [vector,index_list,data]~~写向量中index索引号的元素为data返回新向量，但不改变原向量的值。类似于v[n]=[x]赋值,但后者改变v的值.注意赋值时index大于长度会补[]去顶替. (多元素赋值注意长度一致!)
- peek [vector,index\_list]~~读向量中index索引号的元素==v(index_list),取单元素可用v(1),v[1]. 
- poke [vector,index_list,data]~~写向量中index索引号的元素为data返回新向量，但不改变原向量的值。v(n)=[x]

ps: get,put相当于v[n]法, peek,poke相当于v(n)法. 注意a=[1,2,[3,4]],a([3,1])=5时 a=[1,2,[5,4]],即put法[1,2]指top-level,poke法则指各层相应index

- mget[v,mask]==v\|m ~~mask表中1对应的元素被读取出来
- mput[v,mask,data]和v\|m=[data] ~~mask表中1对应的元素被替换，注意后者原向量会被替换！前者和get相同，不改变原值
^
- tagpeek[v,'tag']==v.tag(无' ')~~查看返回向量v中标签tag的值，因为tag输入虽然没有'  '但储存有，所以加''!;  
- tagpoke[v,'tag',data]==v.tag(无' ')=data~~返回改变向量v中标签tag的值的结果，不改变原值
- tagget [v, tags] 获取向量v指定的tag的第一个的值
- tagput [v, tags] 给向量v指定的tag的第一个赋值
- tagcat [v1, v2...] ~~ 合并多个向量. 实际去除空的tag后,取集合,tag的值取第一个出现的.
- taguniq v ~~ 去重复和空tag.实际第一步去除空的tag, 第二步保留第一个tag的值,将重复的tag删掉.
- tags v~~返回字典中的键名列表，返回为键名的向量[键名]
- untag v~~将字典展开成普通['tag',value]的形式后，转化并返回[[键名],[键值]]的向量
- tag [[键名],[键值]]~~以[[键名],[键值]]为准转化为tag向量形式并返回, 和untag相对


## vector操作
- cat [[i]]~ ~展开嵌套，返回[[1],['a']]top-level元素[1]['a']合并的结果[1,'a'].可多次操作
- nest v ~~ 给向量的元素加一层壳,对于scalar无影响.
- app func [v1,v2] ~~ 使func对v1,v2...top-level的元素进行操作、
- tr [i]~~转置函数，将toplevel内的元素重新按其子元素1,2,3顺序组合，需要等长和单位子向量。例如将[[x],[y],[z]]重新组合成原子坐标。原意是行列互换(矩阵)。
- apt function [vector]~~使函数应用于所有第一级子向量的转置向量，而非向量本身，相当于先tr再app
- indexof[d,vector]~~查找d在向量首个位置，d可以是子向量[a,b]，返回第一个出现时的index，不存在返回0.返回的实际是[index]。
- indicesof[d,vector]~~查找d在向量的所有位置，d可以是子向量[a,b]，返回所有出现的indices，返回时为[[indices]]，不存在返回[]。
- freq [va,vb]~~查找向量va中元素在vb中出现的次数，没有为0.返回次数的序列，形式和va一致。不会进行展开，只对top-level元素进行统计如[[2,3]]则统计[2,3]这子向量出现次数
^
- sort [i]~~排序，返回排序结果向量
- x_sort [i]~~将向量排序，返回排序结果中对应的index列表。(该函数蛮复杂似的)
- x_fsort[i]~~将向量排序，返回排序结果中对应的index列表,相同元素会用第一个的index代替后面重复的。
- sortE [v]~~叶元素级别sort. 先把子元素扩展到同样结构,然后,对每个位置进行相应排序.
- sortuniq [v]~~sort并取唯一元素.
- x_sortuniq [v] ~~sort取唯一元素后,返回在原序列中的index
- rank [i]~~将向量sort,返回原始vector在排序结果中的index列表.比较和x_sort区别.
- frank [i]~~将向量sort,返回原始vector在排序结果中的index列表,其中,重复的元素用之前的index代替.
- l_frank [v1,v2...]~~==(frank tr x) 先倒置再frank
- prank [i]~~sortuniq后的rank
^
- rot [x,n]~~将x中最后n个元素（右）移到最前面（左）。 当n为负数，则将最前(左）n个元素移到最后（右)
- rotl/rotr [x] ~~ 将x向量最左/右的一个元素移到另一侧(rot过去,排列全变化) : [1,2,3] > [2,3,1]
- shiftl/shiftr [x] ~~ 将x向量所有元素向左/右移动一格,空的位置由反侧的元素补上. [1,2,3] > [1,1,2]
- reverse [x] ~~ 反向排列
- length [x] ~~ 返回向量长度或top-level元素数
- perm [v,idx\_index] ~~ 按idx_index来重新排列v,返回重排列后的向量.
- x\_perm [idx\_list] ~~返回按该idx\_list排列的新序列中在原序列的index_list,可传递给get
- parity [v] ~~将rank v和x_id v作比较,返回宇称性. (将一个list变到另一个list所需步数的奇偶性)
- sam [v]~~先sort,返回在旧vector中相应的index,还有唯一的元素的mask的list [new_index,masklist]
- sac [v]~~先sort,返回在旧vector中相应的index,还有在新list中每个元素出现的次数.[new\_index,el_count]
- split[x,n]~~将x根据n个元素为一组而组合成一子向量。如split [igen 5,2]~~[[1,2],[3,4],5]
- pack [i]~~去掉向量中所有0的元素并返回向量。注意向量i不能嵌套，并且所有元素只能是数字或字母（token也不行，非所有标量）
- x\_pack [v]~~返回非0的元素的索引
- unpack [a,b,m]~~合并两个向量,mask中1表示从a中按顺序取出,0表示从b中按顺序取出.
- rep [x,n]~~返回有n个x元素的向量
- keep/drop [x,n]~~在x中保留/删去前n个元素并返回。当n是负数则对后n个元素进行操作。
- smear v ~~将数字vector中0的元素用之前的非零值代替.第一个若为0会当作非0处理,即后面几个0会继续跟它是0
- x\_smear v ~~ 返回smear结果所用的索引
- msmear [v, mask] ~~返回用mask来标识的取代方法,1为保留(第一个元素肯定为1),0为用smear方法替换.v可以为非数字的vector
- csmear [v, seg\_lengths]~~任意vector按seg\_lengths来分组进行smear取代,例如[2,3]对[1,2,3,4,5,6]则变成[1,1,3,3,3,6]

^
- token "abc"~~'abc', change string to token.
- atof 'number' ~~number in float.
- atoi 'number‘ ~~ number in integer.(会四舍五入)
- totok num~~ 转变数字等为token,char支持,但string变为['a','b','c'].
- tok\_cat ['a','1']~~'a1', 合并token为一新token(内容合并)
- tok\_length 'abc'~~ 3, 返回token字符串长度.
- string 'abc'~~"abc", return string from token
- swrite [{},'abc'/1234/[]]~~ "abc"/"1234", convert all data to string, note that swrite ['{}','a','b'] ~~"a"; swrite 'a''b'~~"ab"; swrite[1234]~~wrong; swrite['1234']~~"1234"; swrite ['{}',["a",'b',123,[456,"ok"]]] ~~"a b 123 456 ok", the comma will be changed to blank. 
- igen n 产生1到n的向量
- x\_id [i]~~返回向量长度的数字串[1,2,3...n]，相当于igen length [i]
- m\_id [i]~~返回向量长度的数字串[1,1,1...n]，相当于one x\_id [i]
- null v ~~ 返回null向量
- m\_null v ~~ 返回[0,0,...], 相当于zero x\_id [i]
- isnull v ~~ 判断是否null向量,相当于not length v
- join [va,vb]~~只返回va中在vb中也有的元素的向量，即删掉va中在vb里没出现的元素。(取交集,顺序按va)
- m\_join [va,vb]~~返回va中在vb中也有的元素的向量的mask。(取交集,顺序按va,选择与否看在不在交集)
- x\_join [va,vb] ~~返回va中在vb也有的元素的索引号,[a,b,c,b] [b] > [2,4]
- diff [va,vb]~~返回va中在vb中没有的元素的向量，即删掉va中在vb里重复的元素。(取非集,顺序按va)
- x\_diff [va,vb]~~返回va中在vb中没有的元素的索引号。(取非集,顺序按va)
- m\_diff [va,vb]~~返回va中在vb中没有的元素为1的mask。(取非集,顺序按va)
- sdiff [v,w]~~返回去除掉公有元素后v和w的并集,保留顺序,v在w前.
- uniq [i]~~返回去除重复top-level子向量后的向量，即找唯一的合集。子向量不展开
- x\_uniq [i]~~ 返回非重复top-level子向量的索引。子向量不展开
- m\_uniq [i]~~ 返回非重复top-level子向量后的对应1的mask向量。子向量不展开
- findmatch [['pat1','pat2',...],tokens] ~~返回tokens中所有可以符合pat1或pat2的vector
- m\_findmatch [['pat1','pat2',...],tokens] ~~返回tokens中所有可以符合pat1或pat2时的mask
- x\_findmatch [['pat1','pat2',...],tokens] ~~返回tokens中所有可以符合pat1或pat2的index
- fieldsplit [line, separators] ~~对line用满足separator里的分裂开,分隔符可以[,:]一起,对于vector可用某元素分开.对于[,,]会产生[].
- wordsplit [line, whitespace] ~~~对line用满足separator里的分裂开,和fieldsplit差异在于不会产生[].
- strpos [substr, superstr] ~~ 返回substr在superstr中位置的索引号
- splice [vec, pos, seg, val] ~~将pos起seg个元素删掉插入val的内容.seg可以反方向用负数. pos用负数是倒数.
- split [ w, n ] ~~将w每n个分为一组分开;n为[n1,n2..]则分成[n1个],[n2个]..分开;n为n1,n2..则先分按n1分组再按n2分组,[n11,n12,...], [n21,n22,...]则先按[n11,n12,...]分组,再按[n21,n22,...]分组.
- lhs [ v,w,w2...] ~~将v扩展到满足w,w2等所有格式的向量形式并返回
- uext [v1, v2, v3, ...] ~~所有v都扩展,使满足统一格式,并返回扩展结果
- uext1 [v1, v2, v3, ...] ~~将各个元素扩展到其余元素的length的长度.
- logfile 'filename'~~开始记录session到指定文件，停止记录为logfile [].
- Close[]~~关闭system，即删除一切
- Quit[]


### 系统
- cd 'dir' ~~ 返回并移动到token的文件夹。pwd= cd '.' ;pwd 返回当前文件夹。
- flist [ 'directory', 'pattern' ] ~~ pattern不指明为所有，dir不指明为当前。必须token。 flist [] 返回当前文件夹内容
- fmkdir [ 'directory1', 'directory2', ...] ~~ 创建文件夹. \_fmkdir 是另一种形式,但返回值: 0正常,1 已存在, -1指定文件夹不存在,不能创建(无法建多层)
- frmdir [ 'directory1', 'directory2', ...] ~~删除文件夹,非空出错. \_frmdir 是另外一种形式,0正常,1 非空, -1指定文件夹不存在或不能删除
- fdelete [ 'pathname1', 'pathname2', ...] ~~删除文件夹或文件夹,非空出错. \_fdelete是另外一种形式,0正常,1 非空, -1指定文件夹不存在或不能删除. 通配符不允许!!!
- frename ['filename1', 'filename2']  ~~重命名. \_frmdir 是另外一种形式,0正常,1 已存在, -1其他错误
- freplace ['filename1', 'filename2'] ~~替代或重命名.  \_freplace 是另外一种形式,0代换,1 重命名创建文件2, -1其他错误
- fabsname 'filename' / file\_number ~~返回绝对路径,支持文件名或key
- fname file\_number ~~返回key的文件名token
- fbase 'filename' ~~ 返回不含扩展名'.exe'的基础名 包括文件夹
- fext 'filename' ~~ 返回扩展名token
- fpath 'path\_and\_filename' ~~ 返回文件夹名或上一级文件夹(以/之前部分)
- ftail 'path\_or\_file\_name' ~~ 返回文件名或当前文件夹名(以/之后部分)
- ftype 'name' ~~返回'file','dir'或''(不存在)
- fuserpath 'user\_name' ~~返回用户的home文件夹位置 只适用unix
- fsize 'filename'/file\_number  ~~返回指定文件大小字节byte数
- fdate 'filename' ~~ 返回文件最近修改时间,使用1970.1.1开始秒算
- fstat 'filename'/file\_number ~~ 返回一系列文件相关信息 fstatp减少了一些
- fcopy ['filename1', 'filename2'] ~~复制. \_fcopy 是另外一种形式,0正常,1 已存在, -1其他错误
- fcopydel ['filename1', 'filename2'] ~~复制,若存在则删之. \_fcopydel 是另外一种形式,0正常,1 已存在, -1其他错误
- fmove ['filename1', 'filename2'] ~~移动. \_fmove 是另外一种形式,0正常,1 已存在, -1其他错误
- fmovedel ['filename1', 'filename2'] ~~ 移动,若存在则删之. \_fmovedel 是另外一种形式,0正常,1 已存在, -1其他错误
- fwriteable 'pathname' ~~ 该位置是否可写入 1为可写 0为否
- fseek [ file\_number, byte\_position ] ~~移动文件读写位置. 从0开始算
- pos = ftell file\_number ~~ 返回文件中读写位置
^
- consts [] 列出所有global 常量
- globals [] 列出所有global变量
- functions [] 列出所有公共函数
- modules [] 列出所有module的key,文件,title
- dumpmodules [flags] 列出module详细信息, flags可以是key 可以是title
- mod\_key, mod\_title, mod\_class, mod\_file and mod\_find 'token' ~~返回相应的内容,token其中一种

- serial n ~~产生返回一个序号,n在0~20之间, 按升序产生独特的数,例如0会每隔2产生1数字,1时每隔4产生一个数字
- sym\_file token ~~ 列出含有该token的公共标识符的文件,若build-in返回空
- sym\_line token ~~列出含有该token的公共标识符的文件的所在行, 若build-in返回0
- sym\_modules token ~~列出含有该token的公共标识符的所有模组
- where [] ~~返回Crash history,[fcn\_names, counts, file\_names, line\_numbers],最底一行是直接的错误所在,上面是调用的.
- task\_keylist [] ~~返回所有task的key
- task\_kill tkey ~~关闭任务
- clock [] ~~返回秒的时间
- cpuclock [] ~~返回当前cpu工作的时间
- asctime [] ~~返回"Fri Nov 22 11:57:09 2002" 样式的时间
- time [] ~~返回 timevec样式时间[year,mon,day,yday,yweek,wday,hour,min,sec,isdst] , time i可以指定i第几项返回
- clock\_to\_timevec clock\_to\_timeYMD timeYMD\_to\_clock  timevec\_to\_clock  ~~时间格式的转化 (YMD: [year, mon, day, hour, min, sec ])
- logfile 'logfilename' 保存svl对话log文件,停止使用logfile []
- Beep [] ~~发出beep一声..


### 读写文件输入输出

- print 打印输出;  pr 可以立即打印某个值并返回值 例如c=a * pr b,实际等于c=a * (pr [b])
- pr [i] 显示内容
- fopen* ~~fopen,不存在或不可写均返回错误;r,不存在返回错误;w,会覆盖,不可写报错;x,;类似w,但不覆盖内容;c,创建新文件读写,存在就报错;ct,创新临时文件,会作delmark;t,类似于ct,但存在并不报错和覆盖
- \_fopen* ~~和一般的打开类似,但不返回错误,而返回0
- Read/WriteAuto['filename',options,'format']:自动读取文件，format不指明则根据后缀自动读取，返回chain key
- Read/WritePDB/TriposMOL2/MOE/Maestro 'filename'~~写入/读取指定文件
- Read\_Formats[]~~返回可以读取的格式列表 Write\_Formats[]~~返回可以保存的格式列表
- xml\_fopenr/xml\_fopenw 'filename' ~~打开文件,读或写.
- xml\_fclose keys~~关闭文件取消key
- xml\_key/keyr/keyw keys~~对key进行判断
- xml\_fwrite [key,xmlnode]; xml\_fread key; xml\_next key ~~


### 显示相关
- DrawMeters/HBonds/Dipole/Constr/Axes/VDWContacts flag~~flag为[]时查询状态,0时关,1时开启显示.
- Meters [] ~~返回所有现在的量度量.[meter\_keys, types, atom\_vectors]形式,'distance,angle,dihedral'.
- MeterCreate [ types, atom\_vectors ] ~~创建并返回量度量,type见上.
- MeterChanged [] ~~返回一个序列号用于识别系统的测量值或限制等有否改变.
- MeterDestroy meter\_keys ~~根据key摧毁测量量


### 数学处理相关
- add [i]~~将所有元素相加
- neg [i] ~~ 取反
- mul [i] ~~取积
- log / log2 / log10 / log1p x~~log function,log for ln(loge),log1p for log(1+x). 当x小于0返回NaN
- logb [x,b] logaddexp[x1,x2,x3....]~~log function;logb for log(b)x,logaddexp[] for log∑exp(xi)
- pow [x,p]~~返回x^p,乘方
- sqr x~~返回x^2，x的平方
- sqrt [i]~~开方向量所有元素
- cube x~~x^3，求x的立方
- cbrt x~~开立方x
- exp x & expm1 [x]~~e^x 和(e^x)-1 求自然对数e的乘方及其减一值
- norm [a,b..] =sqrt (a^2 + b^2)=sqrt add sqr [a,b....] ：平方和的根
- rand/randE/randN/randU [i]~~根据输入向量的值而将其随机化，分别是随机化整数(值少于输入值n)，指数分布，正态分布(中心是n)，均匀分布(类似rand但是浮点数)。常结合rep使用生产随机表。 
- sample [v,n]~~在向量v中随机取n个元素组成保持原序新向量并返回该向量。
- x\_sample [v,n]~~对向量v的indices中随机取n个元素组成保持原序新向量并返回该向量。相当于sample [x\_id v, n]
- shuffle v~~随机打乱向量v中排列顺序并返回该向量
- x\_shuffle v~~随机打乱向量v中序列顺序并返回该向量，相当于shuffle x\_id v。
- one/zero [i]~~将向量所有元素，无论多深，均变0或1并返回
- first/second/third/last [i]~~返回第一，二,三或最后的一个元素
- drop [v,val1,val2]~~扔掉元素,v2可选. 若val1是正值,则从1~val1被扔掉;负值则从后面扔起;val2可以进行第二次扔除drop[drop[v,val1],val2]
- keep[v,val1,val2]~~保留元素,v2可选, 若val1是正值,则从1~val1被保留;负值则从后面保留;val2可以进行第二次保留keep[keep[v,val1],val2]
- dropfirst/last v ~~扔掉第一个或最后一个元素再返回
- m\_dropfirst/last v ~~返回drop后对应的在原vector中的mask
- x\_dropfirst/last v ~~返回drop后对应的在原vector中的x\_id,相当于 dropfirst x\_id [v]
- select [v,w,mask] ~~根据mask里面0/1来选择,1对v相应位置选择,0对w中相应位置选择,返回选择结果.v,w,mask要等长.
- eqE eqL ltE/L gtE/L leE/L geE/L [a,b...]~~eq lt gt代表等于小于大于，返回判断0/1。E代表对leaf元素操作，L代表top-level整体元素操作。当大于两项比较时，必须a<b<c小于才返回1.infix版本（就是a==b写法简写),eqE相当于==，eqL相当于===；ltE gtE相当于<和>, le/ge相当于<=和>=。
- neE<>和neL ~~不等于
- cmpL ~~用L字典式比较,是ltL返回-1,eqL返回0,gtL返回1.
- min max minE minL maxE maxL [a,b...]~~返回最小/大值。min/max只能对flat向量数字比较，L则是对top-level整体进行比较，子集时比较第一个元素原则；E则对leaf元素进行比较,minE[[1,3],[2,2]]返回[1,2]，主元素比较，因此需要向量等长或unit-ext。
- andE orE [a,b,c...]~~infix版本为and/or逻辑判断，leaf元素进行and/or操作，须向量等长或unit-ext。元素只能是数字。
- xorE [a,b,c...]~~leaf元素进行xor操作，须向量等长或unit-ext。元素只能是数字。只有xor[0,1]即有真有假才返回真。注意和and/or不同，受比较元素个数影响。如xor[1,2,3]==[1,[2,3]]==[1,0]~1但xor[1,2,3,4]==[1,[2,3,4]]==[1,1]~0
- odd/even x 判断奇偶,需要整数,否则四舍5入后再判断
- bitand [x]~~ 二进制and处理,返回and后共同部分

## 分子模拟对象(原子,残基,链,蛋白)相关 
设置属性Set,基本不返回值(null)

#### System级别--ps:默认打开的system是key为0.
- SystemOpen [sys\_key] ~~打开一个新系统(包含一切对象的总对象). 不填sys\_key表示创建一个新对象,返回创建的系统skey
- SystemCurrent [skey]  ~~设置当前系统为skey的系统,返回就系统的key. 不填写skey返回当前系统skey
- SystemClose skey ~~关闭skey的某系统
- SystemPush [] ~~创建并切换系统, 返回[o,n],o是旧系统key,n是新系统key
- SystemPop [o,n] ~~切换回原系统,[o,n]是之前创建的
- SystemValid [skey] ~~验证系统key的有效性
- SystemNonviewState [] ~~返回计数数字,除了视觉改变(拖动旋转)外的任何改变对象属性的操作都会刻意导致其加1.用于检测系统是否变化.
- SystemTopologyState []~~返回计数数字,该变键的操作都会刻意导致其加1,例如增减键,改变杂化态离子状态等,但改变位置不影响.用于检测系统是否变化.
^
- Atoms[]~~返回当前sys下所有原子key
- nAtoms [] ~~返回当前sys下所有原子数
- Residues[]~~返回当前sys下所有残基key
- nResidues[]~~返回当前sys下所有残基数
- Chains[]~~返回当前sys下所有链的key
- nChains[]~~返回当前sys下所有链数
^
- oParent [obj] ~~ 找出对象的父辈(如链)
- oChildren [obj] ~~ 找出对象的子辈(如原子) (会铺展)
- oAtoms [obj] ~~返回对象下面所有原子keys,原子返回自身.
- oResidues [obj] ~~返回对象下面所有残基keys,残基原子返回所属残基.
- oChains [obj] ~~返回对象所属链的keys.
- oChildCount [obj] ~~返回对象的子对象总数.
- oIndex [obj] ~~ 返回对象在上一级对象下的索引,可以是残基,链,原子等
- oCreate [parent\_key]~~在母对象下创建子对象,返回子对象key.原子作母对象出错
- oDestroy [object] ~~摧毁某对象,连子对象一起删掉.成功返回1,不存在失败返回0
- oValid [keys] ~~返回该key是否一存在对象,不是返回0,是返回1.
^
- oType [keys] ~~ 返回该key的类型,'system', 'chain', 'residue' and 'atom',不存在返回''.
- oReparent   [obj\_keys, new\_parent\_keys] ~~返回旧的母对象的key,移动对象到新的母对象之下. 移动必须是合理的层次之下.
- oSerialNumber [okey] ~~返回对象的序列号,不唯一,有意义于undo操作
- oSetSerialNumber [obj\_keys, ser] ~~设置对象的序列号.

### 原子

#### 原子基本属性
- aChain/Residue [atom] ~~返回原子所属的链或残基的key
- aMass [atomkey]~~返回原子质量
- aElement[atomkey]~~返回原子元素名(token)。
- aName[atomkey]~~返回原子当前名字。
- aPos[atomkey]~~返回原子位置坐标[x,y,z],记得是[[x1,x2..],[y1y2...][z1,z2...]]
- aAngleDeg[atomkey]~~返回原子间夹角，三个原子一子向量！
- aBond [atoms] ~~ 返回所有相连的原子的key,注意会展开.
- aBondOrder [atoms] ~~返回所有相连的原子的相连时的键级,1,2,3键,顺序和aBond一致.
- aRSChirality [atoms] ~~返回RS, R=1,S=-1,不定为0,翻转可用neg
- aRadius [Atoms] ~~ 返回原子半径,力场中设置
^
- aSetElement[atomkey,'X']~~设置原子的元素-token输入
- aSetName[atomkey,'X']~~设置原子的名字X-token输入
- aSetPos[atomkey,[x,y,z]]~~设置原子的位置-输入[x,y,z]子向量, 记得是[[x1,x2..],[y1y2...][z1,z2...]]
- aSetAngleDeg[atomkey,value]~~设置原子的键角-数字输入
- aSetBackbone [atoms, 1] ~~设置为backbone
- aSetGeometry [atoms, 'sp2'] ~~设置原子的几何状态


#### 原子力场相关
- aCharge[atomkey]~~返回原子电荷。
- aFixed [atoms] ~~ 返回原子固定与否状态,0,1
- aInert [atoms] ~~ 返回原子是否惰性,0,1
- aTether [atoms] ~~ [x,y,z],weight,lo,hi], 返回限制状态,xyz为对应vector坐标,weight是力场数,lo和hi是最小和最大的可移动距离.
- aForceRS [atoms, [1,0,-1]] ~~返回力场中限制的RS, 注意,表象RS和限制不一致时builder里显示红色(不合理).ZE也在这设,Z为1E为-1,双键两个原子要一致
- aSetCharge[atomkey,value]~~设置原子的电荷-数字输入
- aSetInert,aSetFixed [atoms, 0/1] ~~设置原子惰性或固定
- aSetTether [atom\_keys, [x,y,z], weight, lo, hi] ~~设置原子限制状态
- aSetForceRS [atoms, [1,0,-1]] ~~设置力场限制RS, 注意,设定完后不改变显示构象,需要MM一下

#### 原子显示属性
- AtomPrompt [] ~~进入手动选择,返回key
- aSelected Atoms [] ~~返回选中的原子的mask, Atoms [] \| aSelected Atoms [] 可返回选中的原子key
- aColorBy [atoms] ~~ 返回着色办法,例如'element'
- aSetSelected [v,  mask]设置v向量里的选择状态0不选1为已选，mask为需要对应的0/1mask。全选 aSetSelected [Atoms[],1] 会进行unit-extension.
- aSetColorBy [Atoms[], 'scalar'] ~~设置原子的着色,使用scalar方法(一般没有)
- aSetScalar [atoms,scalars] ~~设置原子的scalar属性, 0~1的值





### 残基相关
- ResiduePrompt [] ~~进入手动选择,返回key
- rName/Number/Color/RibbonColor/RibbonRGB[rkey]~~返回指定残基名称/序号/颜色0xRRGGBB.
- rType[rkey]/SetType[rkey,token]~~返回和设置残基类型,如'none,amino,dna,rna,heme,l-amino,d-amino'
- rUID[rkey]/SetUID[rkey,UID]~~返回和设置残基UID号
- rINS[rkey]/SetINS[rkey,INS]~~返回和设置残基的INS号
- rColorBy[rkey]/SetColorBy[rkey,token]~~返回/设置颜色模式.'rgb,tempfactor,r:rgb,c:rgb,r:aseg(二级结构),c:number,chain'
- rRibbonColorBy[rkey]/SetRibbonColorBy[rkey,token]~~返回/设置条带颜色模式.'rgb,tempfactor,r:rgb,c:rgb,r:aseg(二级结构),c:number,chain'
- rRibbonMode[rkey]/SetRibbonMode[rkey,token]~~返回和设置条带的模式'none,line,trace,flat,tube,slab,auto'.
- rRibbonEnable[rkey]/SetRibbonEnable[rkey,value]~~返回或设置是否显示条带,0不显示1显示.
- rRibbonWidth/Height和对应的Set ~~返回和设置条带的宽和厚度
- rSetName[rkey,'name']~~改变残基名称为name（token输入）
- rPos [rkey]/rSetPos [rkey,pos\_num] ~~ 返回和设置残基在SE中位置,若紧凑没有gap全为0,否则就出现2,3,5,6这样pos
- rSelected [key]/SetSelected[rkey,mask]~~返回/设置残基被选中状态，注意此为在SEQ面板中的选择，要开同步化才体现出来
- rAtomCount [rkeys]~~返回残基中原子数
- rLetter [rkeys]~~返回单字母的残基名
- rAtom/Chain [res] ~~返回残基相关的原子或链的key
- rScalar [rkey]/rSetScalar[rkey,scalar\_num,values]~~返回残基的scalar(三子向量);设置时,scalar\_num指的是对应三个向量的位置[1,2,3],值是要设置的.
- rSegment/rSetSegment ~~返回和设置残基所在的预测二级结构segment
- rActualSegment [rkey]~~返回根据原子坐标而定的实际的二级结构segment


### 链相关
- cName[ckey]~~返回指定链名称
- cNumber [ckey] ~~返回链的链号,如着色用.
- cColor [ckey] ~~返回链的颜色,0xRRGGBB形式,返回10进制数值
- cRGB [ckey] ~~ 返回链的内在颜色,这颜色用于rgb或c:rgb.
- cColorBy [ckey] ~~返回着色方案. 'rgb','c:rgb','c:number'
- cHeader [ckey]~~返回Header名.
- cTag [ckey]~~返回链的Tag名.
- cSelected [ckey]~~ 返回链在Sequence Editor中的选择状态,1表示选中.
- cSetSelected[ckey,mask]~~设置链被选中状态，注意此为在SEQ面板中的左侧的链选择
- cSetRGB [ ckeys, colors ] ~~设置RGB
- cSetColorBy [ckeys, token] ~~ 设置链的SE中着色方案,'rgb','c:rgb','c:number','tempfactor','residue','chain'
- cSetName/Header/Tag [ ckeys, 'tokens' ] 设置Name/Header/Tag
- ChainPrompt [] ~~进入手动选择,返回key
- cAtom/Residue [chain] ~~ 返回链内的原子/残基

### 键相关
- Boud [a,b] ~~ ab两原子间成键
- UnBoud [a,b] ~~ ab两原子间取消成键
- bOrder [a,b] ~~ ab是两个原子,返回键的级别,0~3
- bInRing [a,b] ~~ ab形成的键是否在环内,0,1
- bInHRing [a,b] ~~ ab形成的键是否在芳香环内, 0,1
- bIn#Ring [a,b] ~~ #是3~8,表示该键是否在3~8元环之内
- bRotatable [a,b] ~~ 返回键是否可旋转键,是的返回1,否则0.
- bInteraction [a,b] ~~ 返回两原子间关系,1是同一原子,2是成键,3是成键角,4是扭转角,0是均不对.
- bInvertStereoBond [a, b] ~~ 旋转立体键,针对ZE式.
- RotateBond [a, b, angles] ~~旋转ab形成的键,键角用弧度,头b尾a的向量进行逆时针旋转.
- BondList atom\_keys ~~ 返回[A\_Keys,B\_Keys], 返回所有指定原子相关的键的原子对,A代表原子A,B代表原子B.
- BondListExclusive atom\_keys ~~ 返回[A\_Keys,B\_Keys], 返回所有只含有指定原子相关的键的原子对,必须两个原子都在指定了,A代表原子A,B代表原子B.
- BondGraph atom\_keys ~~返回原子的相应的nbrlist,即相应的1,2,3,4形式的图形学描述
- SmallestRings atom\_keys ~~返回最小环信息, [[ringA\_atoms],[ringB\_atoms],...]



### 蛋白相关
- pro\_Builder [] ~~打开构建蛋白的面板
- pro\_ResAppend/Prepend [key, res\_name\_tokens, dihedral\_angles]~~添加残基,key为链的key,为0时为创建新链.token为残基token的vector,  dihedral\_angles为3-vector [phi,psi,omega].Append追加Prepend前加
- pro\_Join chain\_keys ~~连接蛋白链
- pro\_Standardize residue\_keys ~~将和标准残基原子名字删掉,重建.键也重建,除了肽键. 必须要有主链四原子
- pro\_ResStandardBonds residue\_keys~~参考标准库重建键,不匹配原子忽略.除了肽键. 必须要有主链四原子
- pro\_StandardRes [residue\_names] ~~返回标准库中残基的具体信息.token,若不填返回库中有的标准残基名.
- pro\_Omega/Phi/Psi residue\_keys ~~返回各残基对应蛋白角度参数,第一个残基没有值. 返回[angles, idx] idx是残基索引号
- pro\_SetOmega/Phi/Psi [ residue\_keys, [ angles, idx ] ]~~返回各残基对应蛋白角度参数,idx是残基索引号
- pro\_Chi/SetChi [residue\_keys]/[residue\_key,data] ~~ 返回Chi数据,data查看手册
- pro\_BackboneDihedrals [res\_keys] ~~返回'psi,phi,omega'三个tag向量,里面[angles, idx].
- pro\_ResCopy [src\_residue\_keys, dst\_residue\_keys] ~~复制残基,先删掉dst残基原子,然后复制残基主链及beta碳到该残基..注意空间位置无变化,不连接
- pro\_AtomCreate [ res\_keys, mol\_data ] ~~ 根据mol\_data创建或修改res\_key的原子,res和mol\_data中要一致长度,res信息不被复制,原子信息全复制.mol\_data可用mol\_Extract等获得.
- pro\_AtomCheck [res\_keys] ~~检查res的重原子名字和标准库对不对,缺失不对返回0
- pro\_PeptideFlags [res\_keys]~~检查res与下一个res是否成肽键,有则返回1,无则返回0
- pro\_BackboneAtoms [residue\_keys] ~~返回[N,CA,C,O] 的主链原子key的四个vector
- pro\_SegmentToDihedrals res\_keys ~~根据rSegment res\_keys的值设置主链二面角参数.
- pro\_Polymerize res\_key ~~构建多肽键??
- pro\_Mutate [ residue\_keys, residue\_names ] ~~ 突变,将指定key的残基进行突变
^
- pro\_Contacts [] ~~打开protein\_contact面板,可以设置更详细参数拿返回值, 具体查index
- pro\_HydrogenBonds mol\_object\_keys ~~返回[donors, acceptors]形式的原子对代表氢键.
- pro\_SaltBridges [Atoms [],[cutoff :4.5, basic\_his:1]]~~返回[acidic\_O, basic\_N]形式的原子keys的vector.cutoff是距离截断,basic\_his是是否处理His为碱性,后两项是option,此处是缺省值.
- pro\_Superpose [ chainkeys, options ] ~~叠合,返回RMSD. 参看[语法](http://platinhom.github.io/ManualHom/MOE/moe2010/html/proteins/fcnref/pro_sup.html)
- model\_chain\_key = pro\_HomologyModel [ chains, options ] ~~同源建模,返回链,参看[语法](http://platinhom.github.io/ManualHom/MOE/moe2010/html/proteins/fcnref/pro_mod.html)
- [chains, options] =run ['$MOE/lib/svl/run/promodel\_ui.svl', [], 'pro\_Model\_Prompt']  同源建模,弹出框提示,返回pro\_HomologyModel的[chains, options]
- pro\_Align [ chains, options ]~~序列比对,chains,options用pro\_Align\_Prompt []搞到
- [chains, options] = pro\_Align\_Prompt [] ~~提示面板进行align参数设置
^
- pro\_SeqCreate [ "residue\_letter\_names", options ] ~~根据单字母残基序列创建链,具体参看[语法](http://platinhom.github.io/ManualHom/MOE/moe2010/html/proteins/fcnref/pro_seq.html)
- pro\_Predict2Struct [chain\_keys] ~~预测二级结构,返回tag向量,对应helix等的概率,参看[语法](http://platinhom.github.io/ManualHom/MOE/moe2010/html/proteins/fcnref/pro_pred.html)
- pro\_PredictAccessibility [chain\_keys]~~预测溶剂可及程度'buried','exposed',对应各概率.参看[语法](http://platinhom.github.io/ManualHom/MOE/moe2010/html/proteins/fcnref/pro_pred.html)
- pro\_ResHydrophobicity res\_names ~~返回残基疏水性.注意残基三字母大写.
- Hydrophobic\_Fitness\_Z [ res\_names, mol\_data, align\_pos ] ~~返回Z-score打分,第三项是可选.
- pro\_SearchPDB [ query\_set, search\_options] ~~同源搜索,返回family\_lists

### 序列相关
Seq\_NameToLetter res\_names ~~三字母token残基vector到单字母(大写)
Seq\_LetterToName letter\_codes ~~单字母token残基vector到三字母(大写)

### 分子相关
mol\_Extract [atoms/residues/chains] ~~提取分子 可以储存为一变量,mdb格式分子结构,第四个也是最后一个vector是所有原子信息的.(4)(1)是元素(EL),(2)是离子化态(3)是杂化态(GEOM),(4)是手性(CHIRALITY),(5)是孤对电子提示(HINTLP),(6)是连接atoms(相当于BONDS),(7)部分电荷(CHARGE),(8)NAME,(9)BACKBONE(10~12)是XYZ.如mol(4)(MOL\_ATOM\_Z) 
mol\_Create [mol] ~~按mol分子格式创建分子

### MOE函数和功能


#### Smile操作
- sm\_Build 'CC=O' ~~build mol, return atoms keys [17,25,31,45]
- sm\_Match ['pattern',atomkey] ~~匹配pattern的原子情况，返回相当于Mask，pattern如'C=O'，匹配的第一个原子呈现1，不匹配为0.
- sm\_MatchAtoms['pattern',atoms]~~匹配一定pattern的所有原子信息返回,和Match类似;匹配返回这个pattern占的原子key信息，不匹配为[]。
- sm\_ExtractUnique [atomkey] ~~从原子中提取出独特的smiles字符串


import function  
MM


- Restraints [] ~~返回[restraint\_keys, types, atom\_vecs, target\_vecs, weights]的所有限制条件
- RestraintCreate [ types, atom\_vecs, target\_vecs, weights ]~~创建限制条件,'distance,angle,dihedral'三种,atom项是指定的原子,target项是想限定的值,weight是限制强度,返回限制条件key
- RestraintDestroy res\_keys ~~删除限制条件

#### 药效团
- ph4\_TypeList [] ~~返回可用的简称的原子的ph4类型'+,-,A,D,H,P,X' 对应+-离子,氢键受体供体,疏水极性和其他.
- ph4\_aType [akeys] ~~返回原子的ph4简写的类型,见ph4\_TypeList
- ph4\_a** [akeys] ~~**部分对应很多性质,具体参照[连接](http://platinhom.github.io/ManualHom/MOE/moe2010/html/moe/fcnref/ph4_tlst.html),有此属性返回1,否则0.除了aGeometry特别点,sp返回1,sp2返回2,其他3,分离为0.


### GUI

- Plot [[xi..],[xj...]]~~生成位置N和xi的二维plot图，x轴是N，y轴是x值，返回对象key，可以画多条i,j。。
- PlotH [[xi..],[xj...]]~~生成位置N和xi的二维plot直方图，返回对象key，和Plot类似，但是x值采用柱形直方图表示，可以画多条i,j。。
- PlotS [[[xi..],[yi..]][[xj...],[yj...]]]~~生成位置x:xi和y:yi的二维plot图，返回对象key.可以画多条i,j。。
- PlotC [matrix data]~~生成s维plot图，返回对象key。 如PlotC[ [sin t]\*cos t] t=0.01*igen300

#### Graph

- graph\_neighbors [xA, xB,n] ~~ 返回由edge list转化为nbrlist,有向,n可选,为vertex数,超出指明vertex号会补孤立点,少于vertex号会自动删去多余的点影响.
- graph\_uneighbors [xA, xB,n] ~~ 类似于graph\_neighbors,自动转化为无向形图形,会自动补全关系.
- graph\_edges nbrlist ~~转化nbrlist为edge list[xA,xB]形式,有向
- graph\_uedges nbrlist ~~转化nbrlist为edge list[xA,xB]形式,无向,自动补全关系

- graph\_tr nbrlist ~~转化有向的edge为反向,无向的不受影响.返回nbrlist
- graph\_rot [nbrlist,k] ~~向右挪动edge,k为挪动步数,负值表示向左挪动. 相当于连接位+1且连接的index+1. 注意越界时变化.
- graph\_vcut [nbrlist, idx] ~~删掉图形nbrlist中idx的点及相关关系,返回新图形
- graph\_ecut [nbrlist, [idx1, idx2]] ~~删掉图形中一点在idx1,一点在idx2的edge,返回新图形
- graph\_ecutE [nbrlist, [idx1, idx2]] ~~删掉图形中[idx1,idx2]的edge list的无向的边,返回新图形

- graph\_adjacency nbrlist ~~ 返回n*n的matrix,n是最大vertex数. 每个子向量代表了该vertex和其他vertex连接关系,1连0没连.
- graph\_distance nbrlist ~~返回n*n的matrix, 每个子向量代表了该vertex和其他vertex连接的最短距离,自身相连返回0,不相连返回n,注意方向性
- graph\_eccentricity nbrlist ~~返回图形中vertex i到任意vertices距离中最长的距离
- graph\_radius nbrlist ~~ 返回 graph\_eccentricity 结果中最短距离的值,代表了图形行进的半径
- graph\_diameter nbrlist ~~ 返回 graph\_eccentricity 结果中最长距离的值,代表了图形行进的直径
- graph\_center nbrlist ~~返回mask,表征vertices是否在 graph\_eccentricity 结果中的值等于graph\_radius
- graph\_perimeter nbrlist ~~返回mask,表征vertices是否在 graph\_eccentricity 结果中的值等于graph\_diameter
- graph\_chain [nbrlist, [x, p]] ~~根据图形,给定第几个顶点x,x必须是1度点(末端),路径中的点必须是2度的,终点不限,返回最长的路径.p可选,指定p会先断开x-p
- graph\_ear [nbrlist, [a, b]] ~~a和b是两个起点,先断开a-b,再返回两条最长路径如graph\_chain. 若a终结于b,则第二路径只含b.
- graph\_dfs2 nbrlist ~~深度优先搜索,返回 [dis, fin, par, low, cc, tc, ebc, bc],其中ebc第七项是block识别,每个环系从1起,非环为0

### DB/DBV相关函数 
注意很多db\_key的可用db\_name代替'abc.mdb'

- db\_Open ['filename','mode']~~打开数据库，返回数据库的key; mode为'read' ,'read-write', 'create'，若不指名为读写，因此[]也省. 注意CLI里运行会自动追加db\_Close,所以要写在一行. db\_Open [] 不加参数返回所有打开的db,不作变量指定时返回'$key $file\_token',而变量赋值时直接返回文件的token. 
- db\_Close dbkey~~关闭db数据库，使用要和dbOpen一样多.
- db\_KeyList [] ~~返回所有打开数据库的key
- db\_Key dbkeys~~ 验证某个key是否可用状态
- db\_Filename mdb\_keys ~~返回db的文件名
- db\_Read [dbkey,entrykey]~~读取db中指定entry的数据，返回读取的数据[fieldname1:data1,fieldname2:data2.....],因为是tag可以再用mdb.field来提取指定数据。
- db\_Write [dbkey,entrykey,[fieldname:MDBdata]]~~将data写入到db中，如果entry设0表示新追加。fieldname为写入到某指定field，tag格式，MDBdata可用mol\_Extract获得。返回写入的entry的key。指定mdb时除了用dbkey也可以用文件名,entrykey也可以用某entry的key，0为追加！。
- db\_CreateField ['mdb\_filename','fieldname','fieldtype']~~在指定mdb仲创建新的列field，类型指定入'molecule,int,float,double,char,byte'
- db\_Entries[dbkey]~~返回所有entry的key，可用index来指明key
- db\_ReadColumn [dbkey,'fieldname'] ~~读取整列的数据,包含所有entries
- db\_ReadFields [ mdb\_key, entry\_key, field\_tokens ] ~~读取某个cell的值,靠entry和field定位
- db\_Delete [dbkey,entrykey] ~~删除entry
- db\_DeleteField [ mdb\_key, ['fieldname1', 'fieldname2',... ] ~~删除field,连数据一起删除.
- db\_nEntries mdbkey ~~返回entry总数
- db\_Entries mdbkey ~~返回所有entry的key
- db\_NextEntry/PrevEntry [ mdb, entry\_key ] ~~返回下一条和上一条的entry的key.对于下/上一个不存在返回0,
- db\_EntryKey [ mdb, entry\_key ] ~~返回0/1,验证该entrykey存在否
- db\_FieldType [ mdb\_key, field\_tokens ] ~~返回field的类型
- db\_NumericFields mdb\_key ~~返回所有数字类型的field
- db\_FirstFieldType [ mdb\_key, 'fieldtype' ] ~~指定类型的第一个field的名字返回.
- db\_Fields mdb\_key ~~返回[fieldnames,type],mdb里面所有field的信息
- db\_RequireField [mdb\_key, 'fieldname', 'fieldtype' ] ~~需要有名为fieldname且为指定类型的field,否则会终止工作
- db\_RequireFieldType [ mdb\_key, 'fieldtype' ] ~~找寻有无指定类型的field,无则会终止工作,有则返回field的name
- db\_EnsureField [ mdb\_key, 'fieldname', 'fieldtype' ] ~~检查field名字和类型有否和指定的一致,无则新建(若类型不一致,旧的会删掉再重建),确保有该类field
- db\_State/DataState/EntriesState/FieldState mdbkey~~ 返回邮戳,用来记录数据是否变化,state是状态,如选择,可见性变化;其余对应相应的数据变化.
- db\_Prefix [ mdb, entry\_keys ] ~~按entry\_key指定的顺序将指定的entries插入到最前面.
- db\_FieldPrefix [ mdb, field\_name ] ~~按field\_name指定的顺序将指定的fields插入到最前面.
- db\_ReorderFields [ mdb, field\_names, field\_pos ] ~~将指定的fields移动到指明的index的地方(两者len需相等),返回先前field的顺序.
- db\_RenameField [ mdb\_key, 'fieldname', 'new\_name' ] ~~field改名
- db\_Sort [ mdb, fields, sort\_order\_flag ]~~排序,field可指定多个,第一个是主要排序标准,依此类推;sort\_order为0升序,1降序;返回值为已排序后的entries 的unique与否的mask,若独特的标为1.
- db\_Proxy [ mdb, fields, sort\_order\_flag ]~~排序后返回rank,db\_Sort差不多
- db\_ImportDB ['dst\_db','src\_db',fields,names,types,options] ~~载入mdb内容,names是目的地的field name. [参见](http://platinhom.github.io/ManualHom/MOE/moe2010/html/moe/fcnref/db_port.html)
- db\_ExportDB [ 'dst\_db', 'src\_db', field\_names, entry\_keys ] ~~输出mdb内容,
^
- dbv\_Open 'filename' ~~用db viewer打开数据库，返回dbkey; 不指名file,将使用文件选择器; dbv\_OpenFile 'filename' ~~和open类似,但不打开文件选择器
- dbv\_Close, dbv\_KeyList, dbv\_Key [] 和db相同
- dbv\_Entries mdb ~~同db\_Entries,但不用对硬盘操作,会更快.
- dbv\_SelectedEntries/VisibleEntries mdb ~~ 返回被选中或可见的entry
- dbv\_nSelectedEntries/nVisibleEntries mdb ~~ 返回被选中或可见的entry数目
- dbv\_EntrySelected/EntryVisible [ mdb, ekeys ] ~~返回指定entry是被选择或可见与否
- dbv\_EntrySetSelected/dbv\_EntrySetVisible [ mdb, ekeys, states ] ~~设置entry的选择或可见状态.
- dbv\_EntryHeight [ mdb, new\_height ] ~~设置新高度,并返回旧高度.
- dbv\_Fields mdb ~~返回所有field name
- dbv\_ShowField [ mdb, new\_field\_order ] ~~返回旧的field顺序,如果设了顺序则改变显示顺序,注意,并不写入硬盘.
- dbv\_FieldSelection [ mdb, new\_states ] ~~返回旧的选择状态,可控制选择状态,[1,0,1]
- dbv\_FieldHide/FieldPlot/FieldWrap/FieldWidth/FieldPrecision [ mdb, new\_states ] ~~各种控制和看状态
- dbv\_DefaultView[]~~返回运行调用函数的db viewer的key ,同理  dbv\_DefaultEntry []    dbv\_DefaultField []
- dbv\_SetDatabase [ dbvkey, 'mdb\_filename' ] ~~设置该窗口打开某个db base
- dbv\_ReadOnly [ dbvkey, new\_state ] ~~返回或设置某db的只读状态(1为只读,0读写)



### 常量

- PI  π
- INT\_BITS 机器位数

------
