---
layout: post_small
title: MOE自定义高级菜单窗口
date: 2015-11-29 13:18:11
categories: CompCB
tags: Software
---


$HOME/.moe-rc 有一些设置 

菜单相关文件有三个: 默认`$MOE/lib/moe-menus`, 用户 menu file `$HOME/moe-menus` (if it exists) followed by `$HOME/.moe-menus` (if it exists). Menu files are read by MOE in the following order. Subsequent menus override previous menus.

- MOE standard distribution menus, found in `$MOE/lib`.
- `$MOE/lib/svl/custom/moe-menus`, if it exists.
- `$HOME/moe-menus` if it exists, otherwise `$HOME/.moe-menus` if it exists.

MOE启动选项: 

- -mpu 4 #指定多核运行  
- -gfxvisual 0x01  #指定显卡  

`$MOE/lib/svl` and its subdirectories 是默认的, environment variable `MOE_SVL_LOAD` 会加载某文件或某文件夹. 自定义加载可以`$HOME/svl` 

SVL加载顺序

- Standard MOE distribution source files, from $MOE/lib/svl.
- Patches (if any) to the standard MOE distribution, found in $MOE/lib/svl/patch.
- Custom files from $MOE/lib/svl/custom. If there is a file called moe-menus or .moe-menus found here, it will also be read in.
- If the environment variable `MOE_SVL_LOAD` has been set to a directory, then files from that directory.
- If the directory $HOME/svl exists, then files from that directory.

runable svl文件执行顺序(以第一个遇到为准)

- The current working directory (as returned by the cd function).
- `MOE_SVL_RUNPATH`, if set to a valid directory.
- Custom directory, $MOE/lib/svl/custom/run.
- Standard MOE distribution patch directory, $MOE/lib/svl/patch/run.
- Standard MOE distribution, $MOE/lib/svl/run.

`moe -load` 可加载svl文件或文件夹
`moe -std` 不加载用户的,只加载标准的和patch的

> [Configuring and Customizing MOE](http://platinhom.github.io/ManualHom/MOE/moe2010/html/appendix/moeconfig.htm)
> [Menu File Format](http://platinhom.github.io/ManualHom/MOE/moe2010/html/moe/fcnref/menufile.htm)


~~~bash
ReadMenuFile 'asurf.menu' at the SVL command line
new\_value = EchoMenuCommands old_value
curr_value = EchoMenuCommands []
~~~

`include "filename"`

### 添加命令

~~~bash
  MENU PREPEND "Main:Compute"
    "Water Accessible Surface" exec "run '$MOE/sample/asurf.svl'"
        accel 'ctrl+alt+a'
        active atoms 
  ENDMENU
~~~

- MENU - ENDMENU 定义声明
- PREPEND,APPEND代表添加位置,最前还是最后
- "Main:Compute" 菜单子菜单名字 注意用字符串,选项前是:
	- 第一行声明了添加操作所在菜单或工具栏
	- 第二行起是添加内容,第三四行是内容的属性.
	- exec是执行命令, 前跟命令名字,后跟字符串.
	- accel 是快捷键, token
	- active 是激活所需条件,atoms是体系中有原子

更多条件等请[参考](http://platinhom.github.io/ManualHom/MOE/moe2010/html/moe/fcnref/menufile.htm)

`&`是连接符
表达中 `&&`逻辑与 `|` 逻辑或 `!`逻辑非

### 添加子菜单

~~~bash
    MENU APPEND "Main"
 "MyMenu" submenu "Work on Selection"
    ENDMENU

    MENU "Work on Selection"
 "Keys" exec 'Atoms[] | aSelected Atoms[]'
        active sel_atom
 "Total" exec 'length (Atoms[] | aSelected Atoms[])'
        active sel_atom
    ENDMENU
~~~

添加子菜单使用`submenu`关键词来添加,前跟显示名字后跟子菜单真实定义名字,再使用MENU 方法定义子菜单. 注意不跟APPEND,PREPEND.

另外一种子菜单方法:

~~~bash
MENU "Main:File"
    "New"
 MENU "Main:File:New"
     "Database..." exec "run'dbvnew.svl'"
     "Pharmacophore Query..." exec "run'ph4_edit.svl'"
     "Text Editor..." exec 'ted_Open[]'
     "MOEvie..." exec "run'moevie.svl'"
 ENDMENU
SEPARATOR
~~~

### 右键窗口
支持:

- MOE Window: MainPopup
- Sequence Editor: SEPopupMenu, SEChainPopupMenu, SEColumnPopupMenu, SEResiduePopupMenu
- Database Viewer: dbvMolCellPopupMenu, dbvFieldPopupMenu, dbvEntryPopupMenu, dbvCellPopupMenu, dbvPlotPopupMenu, dbvYAxisPopupMenu
- SVL Text Editor: SVLTextEditorPopup

实例:

~~~bash
MENU APPEND "SEPopupMenu"
    "num" exec 'add rSelected Residues[]'
ENDMENU
~~~

### buttonbar
支持RightButtonBar, LeftButtonBar, SERightButtonBar, SELeftButtonBar, dbvRightButtonBar, dbvLeftButtonBar.
实例

~~~bash
  MENU PAGER "LeftButtonBar"
    "Select" submenu "SELECT"
    "Render"    submenu "RENDER"
  ENDMENU
~~~

PAGER是多个合在一起

menu-item	| : SEPARATOR
	|	: string submenu string
	|	: string MENU string { menu-item }* ENDMENU
	|	: string { command }*

Certain menu names have special meaning in MOE: 

Name	|	Meaning	|	Standard Definition
----|-----|-----
dbvMenuBar	|	The Database Viewer menu bar.	|	$MOE/lib/menu-dbv
dbvCellPopupMenu	|The Database Viewer non-molecule field popup menu.	|	$MOE/lib/menu-dbv
dbvEntryPopupMenu	|The Database Viewer entry number popup menu.	|	$MOE/lib/menu-dbv
dbvFieldPopupMenu	|The Database Viewer field title popup menu.	|	$MOE/lib/menu-dbv
dbvMolCellPopupMenu	|The Database Viewer molecule field popup menu.	|	$MOE/lib/menu-dbv
dbvPlotPopupMenu	|The Database Viewer plot area popup menu.	|	$MOE/lib/menu-dbv
dbvYAxisPopupMenu	|The Database Viewer plot area y-axis popup menu.	|	$MOE/lib/menu-dbv
Main	|	The MOE main window menu bar.	|	$MOE/lib/moe-menus
MainPopup	|	The MOE main window popup menu.	|	$MOE/lib/moe-menus
SEChainPopupMenu	|	The Sequence Editor chain box popup menu.	|	$MOE/lib/menu-se
SEColumnPopupMenu	|	The Sequence Editor residue column popup menu.	|	$MOE/lib/menu-se
SEMenuBar	|	The Sequence Editor menu bar.	|	$MOE/lib/menu-se
SEPopupMenu	|	The Sequence Editor popup menu.	|	$MOE/lib/menu-se
SEResiduePopupMenu	|	The Sequence Editor residue box popup menu.	|	$MOE/lib/menu-se
SVLTextEditor	|	The Text Editor menu bar.	|	$MOE/lib/menu-ted
SVLTextEditorPopup	|	The Text Editor popup menu.	|	$MOE/lib/menu-ted

The predefined state tags in MOE are

Tag	| Definition
-----|-----
data	|	There is molecular data (atoms, residues or chains)
data_modified	|	Molecular data is modified, but not saved
data_filename	|	A save filename exists
atoms	|	Atom objects exist
residues	|	Residue objects exist
chains	|	Chain objects exist
sel_atom	|	At least one atom is selected
sel_residue	|	At least one residue is selected
sel_chain	|	At least one chain is selected
sel\_atom_1	|	Exactly one atom is selected
sel\_atom_2	|	Exactly two atoms have been selected
sel\_atom_3	|	Exactly three atoms have been selected
sel\_residue_1	|	Exactly one residue is selected
sel\_residue_2	|	Exactly two residues have been selected
sel\_residue_3	|	Exactly three residues have been selected
mol_ribbon	|	Ribbon is displayed
mol_trace	|	Alpha trace is displayed
mol_axes	|	Axes are displayed
mol_box	|	Periodic box is displayed
mol_constraints	|	Constraint meters are displayed
mol_meters	|	Meters are displayed
mol_hbonds	|	Hydrogen bonds are displayed
mol_bondorder	|	Multiple bonds are displayed
mol_stereo	|	Stereo mode is on
mol_antialias	|	Anti-aliasing is on
mol_polyatoms	|	Polyhedral atom rendering is on
mol_polybonds	|	Polyhedral bond rendering is on
db_fields	|	Database contains at least one field
db_entries	|	Database contains at least one entry
db\_sel_fields	|	Database has at least one field selected
db\_sel_entries	|	Database has at least one entry selected
dbv_exists	|	A database viewer is up
dbv\_read_only	|	Database viewer is read-only
dbv\_mol_present	|	Database has a molecule data field
ted_exists	|	At least one SVL text editor is up
ted_highlight	|	Editor has highlighted text
ted_filename	|	Editor has a filename defined
ted_canundo	|	Editor can undo the command
ted_canredo	|	Editor can redo the command

---------

## GUI编程

$MOE/sample/windemo.svl 内含各种组件对象,属性等.

- `YesNo`, `NoYes`, `OKCancel`, `Warning`  and `YesNoCancel` 
弹对话框, 语法 YesNo 'Prompt' 可返回值,用变量接收. 注意此时MOE被block掉,可按Return代替
- const/local PANEL [title:'abc',Label:[text: 'hi']]   
创建一个常量/变量的窗口描述符,用于WindowCreate等指令创建窗口. 内容是tagged vector, 记录了各种组件和属性. PANEL名字可任改,常量推荐大写
- wkey = `WindowCreate` PANEL  
创建一个窗口,不可见.返回窗口key
- `WindowDestroy` wkey  
删除一个窗口.
- key = `WindowShow` [ window, show ]  
window可以是window key,可以是windowName. show项非0时则显示,反之隐藏.不存在window返回0.
- names = `WindowName` keys  
返回windowName 属性设置的名字, 不存在返回null
- keys = `WindowKey` keys\_or_names   
返回window的key, 不存在返回0
- names = `WindowNameList` []  
返回所有窗口的windowName到names向量
- keys = `WindowKeyList` []  
返回WindowCreate创建的窗口的key
- obj\_name\_value\_pairs = `WindowPrompt` [window\_descriptor, default\_values]  
创建一个含OK,Cancel两按钮的窗口,自动显示关闭,但不锁死, 缺省值不设为[].按Cancel将跳过后面的事件,OK继续执行.一种特殊的交互. **返回值**是组件name:value的tagged vector, 例如一个text组件叫data, 可以设定起始值[data:'hello']. 返回值可用window\_key.widget\_name来获取. 若widget没有name,则其不返回值,重复的name的只返回第一个name对应的widget的值. Trigger return后退出.
- [widget\_name\_value_pairs, triggername] = `WindowWait` wkey  
等待窗口发生trigger事件,一般嵌套在loop之内. 第一项是所有widget\_name:value, 第二项是激发trigger的widget name. 在嵌套时,为退出,可用if trigger=='panel' 来destroywindow, 并return终止任务.
- `WindowTrigger` [wkey, widget\_name\_value_pair]  
模拟引发trigger事件,window和widget必须是存在的
- `WindowSetAttr` [ wkey, attribute\_value_pairs ]  
设定某窗口中某些widget的属性. [wkey, [text:[len:20,onTrigger:'returen'],button:[columns:3,...]] 
- name\_value\_pairs = `WindowGetData` [ win, widget_names ]   
获取widget的值
- `WindowSetData` [ win, widget\_name\_value\_pairs ]
设定widget的值,需要用widget_name: value的形式设定.
- name\_value\_pairs = `WindowValues` wkey  
获取所有widget\_name:value的值,tagged vector
- filename = `FilePrompt` [       # 返回的是绝对路径  
	title :	'title',  
	mode  :	'mode',   # open(验证), saveAs 文件名. 会出现覆盖提示, file/dir 选择指定类型, none 不加任何验证  
 	path  :	'directory',            # 不指名为空token'',即用当前位置  
	filter:	'pattern',                     # '\*.svl' 过滤  
	name  :	'filename',           # 打开时预设的文件名  
	multi :	flag,         # 是否允许多选.0为不许,1为有附加file list来多选,2为可选是否显示这个附件file list  
	list  :	['file','file', ...],                # 显示在file list中的内容  
	recentDirs: ['dir','dir', ...],     # 指明右键弹出的最近路径  
	allowEmptyList : flag,           # 是否允许空文件list返回  
	allowDuplicates: flag ]           # 是否允许相同名字出现    
 如 FilePrompt [], FilePrompt [multi:1, filter:'\*.mdb']
 
 
### Widget:

- name是组件名,建议唯一;
- title是显示的内容; 
- titleFont 显示内容字体; 
- shadow是边框样式; 
- bubbleHelp是停留显示的帮助,
- vector时要和每个元素对应; 
- sensitive是可用否的状态; 
- titleTop是title在组件上方; 
- onTrigger 激发响应,默认ignore,常用return和validate(多了个数值检查,可在如text中加min/max属性)和exit; 
- uniformRows/uniformCols 调整每行每列的大小和最大的对齐; font 字体大小; minWidth 最小宽度; 
- Panel: 主窗口:返回key,
	- name, title,onTrigger
	- text:['a','b'] 底部紧凑创建按钮
- 容器: Vbox, Hbox, Mbox, and Pager 如一般的Frame
	- Vbox, Hbox (V是垂直,H是横向容器.) 
		- name, title, titletop, bubbleHelp, sensitive,shadow(常用etched-in)
		- spacingV和spacingH 间隙,small none medium large
	- Mbox 行列式容器
		- name, title, titletop, bubbleHelp, sensitive,shadow(常用etched-in)
		- columns 多少列
		- columnMajor :1, 排列顺序按竖排; 0, 排列顺序按横排(默认)
		- spacingV和spacingH 间隙,small none medium large 
	- Pager 分页容器 返回容器内widget的的所有值.
		- name, title, titletop, bubbleHelp, sensitive,shadow(常用etched-in) 
		- page: 最重要, int型,一般要配合Radio(返回int)来实现改变page来切换页面. page内容的分隔通过在里面放容器Vbox,Hbox等按顺序自动定义.
- 关于Prompter: 这个是直接替代掉command line的区域而嵌入在主窗口中,无关键词. 嵌入主窗口包括: 'MOE', 'SequenceEditor', 'DatabaseViewer', 'SVLTextEditor'等. 作为一种嵌入子窗口,属于首层. 必须定义location(上面几种). 可以用widget,也可以用'pickAtom', 'pickResidue/Chain', 'pickCell,pickEntry/Field' 等来操作,返回将是选中的atom/res/chain/entry等的key.cell返回[entry key, field name],field 返回field name
- Separator 分离线    
	- name, title, titletop, bubbleHelp, sensitive,shadow(常用etched-in)    
	- vertical : 1:垂直, 0:水平(默认)    
	- extendH,extendV 对于延长分离线很有必要,常设为1.    
- Text :  返回值:填入的内容  
	- name, title, titleTop, bubbleHelp, sensitive, onTrigger  
	- type是返回类型, len是框长度;allowBlank是运行留空否; password是密码*形式显示;emptyText是没有值时的显示; emptyForeground是没有值显示时颜色,默认gray;   
- Label : 标签, 无返回无trigger  
一般属性外,主要是text, minWidth,font, graphic, background等属性  
- Edit : 文本编辑框: 返回内容  
一般属性外,还有len,width,foreground, background  
- Button : 按钮: 返回一系列button中最后按的一个的token或从1起的索引号,与text和type设置有关  
一般属性外,还有columns(几列), type, onTrigger, text, minWidth, 字体前背景对齐图片等,  
- Checkbox : 返回值:0/1  
	- name, title, titleTop,bubbleHelp, sensitive, onTrigger  
	- text是选框后面的内容,title是前面的内容  
- Radio: 单选项 : 返回1~n的选项值或token  
	- text: 显示的选项值,vector  
	- name, title, titleTop, bubbleHelp, sensitive, onTrigger  
	- type: 选中返回值类型; columns: 分成几列; extendH: 延长宽度至合适  
- Option : 下拉选择框 : 返回选中的token或index  
一般属性外,还有columns(分成几列列出), text(内容), type, onTrigger, 字体,前后景,图形等.  
- Listbox : 列表框 : 返回值 [[select\_items],number\_of_click]  
	- text: 内容!vector!!    
	- name, title, titleTop, bubbleHelp, sensitive, onTrigger  
	- len/width 长宽值; type 数据类型; header:token, 第一行的抬头,下有分割线; multiSelect, 可以多选; multiColumn, 列成多列; grid, 在列成多列时,显示分割线;  
	- font,foreground,background  
通过返回值可知选中的项和双击还是单击.  
- Scale : 数值范围,带text框: 返回位置对应的值  
一般属性外,主要有range :[min,max,multiplier], len(决定text框长度), width(决定拖动条长度), vertical, onTrigger.  
- Slider : 拖动条, 不带text框: 返回浮点数的位置值  
一般属性外,主要有range :[min,max,multiplier], width, vertical, onTrigger.   
- Spin: 步进器, 带text框: 返回text中的值  
一般属性外,主要有range :[min,max,multiplier], len(决定text框长度), vertical, onTrigger.   
- FSB : 文件选择框: 返回值:选择的文件的vector  
常利用WindowPrompt来定义,再利用key.fsb来获取. 也可以利用其default来预定义'*.svl'去锁定后缀名显示.  
	- mode: none, read, saveas; read的时候不能键入不存在的文件; len,width: 长宽  
	- recentDirs : `['$HOME','$MOE/sample/mol']` 这样可设定最近文件夹位置, 右键地址输入框可弹出最近的文件夹.  
- FSBText :单行文件输入框,可以验证存在否. 有如mode,len, onTrigger的属性  
- Data 数据框,不可见. :用来连接数据到窗口.  
- Material, Trackball, Wheel, Color, Plot , CLI 都是比较花巧高级的东东   

------

MOE2010  
Prepared Function  
弹框  
Builder []   
MOE_Electrostatics []  
MinimizeEnergy []  

#### menu-bbar

~~~bash
#moe:menu
# menu-bbar button bars in main window
MENU "RightButtonBar"
    "System" bgcolor 'Blue' fgcolor 'white'
 exec "_LIGX_SystemPanel [['MOE','_LIGX_System',93]]"
 name '_LIGX_System'
    SEPARATOR

    "Open" exec "run'open.svl'"
    "LigX" exec "_LIGX_Prepare[]"
    "Constrain"
 MENU "LigX:Constrain"
     "Tether" exec "_LIGX_Constrain'tethered'" active atoms
     "Fix" exec "_LIGX_Constrain'fixed'"  active atoms
     "Unfix" exec "_LIGX_Constrain'unfixed'"  active atoms
     "Free" exec "_LIGX_Constrain'free'"  active atoms
     SEPARATOR
     "Render" exec "_LIGX_ConstrainRender[]"  active atoms
 ENDMENU

    "Close" exec "Close[]" fgcolor 'red'

    SEPARATOR
    "Center" exec 'View (Atoms[]|aSelected Atoms[])'
 bgcolor 'Blue' fgcolor 'white'
    "SiteView "
 exec "_RenderIsolate []"

    SEPARATOR

    "Hydrogens" exec "_RenderShow 'cycleH'"
    "Hide" submenu "Render:Hide" active atoms
 exec "_RenderHide[]"
    "Show" submenu "Render:Show" active atoms
 exec "_RenderShow[]"

    SEPARATOR

    "Ligand"
 MENU "RightButtonBar:Properties"
     "Ligand Interactions..." exec "run 'prolig2d.svl'"
 active atoms
     "2D Molecules..." exec "run ['view2d.svl', []]"
 active atoms
     SEPARATOR
     "Choose Ligand" exec "_LIGX_SelectLigand[]"
 active sel_atom
     SEPARATOR
     "Ligand Properties" exec "_LIGX_LigandProperties'toggle'"
     "Ligand R-Vectors" exec "_LIGX_RVectors'toggle'"
     SEPARATOR
     "Duplicate" exec "_LIGX_Duplicate[]" active atoms
     "Minimize (Vac)" exec "_LIGX_MinimizeV[]" active atoms
 ENDMENU

    "Surface" submenu "RightButtonBar:Surface"
    "Measure" submenu "Main:Edit:Measure"

    SEPARATOR

    "Builder" exec "run'builder.svl'"
 bgcolor 'Blue' fgcolor 'white'

    "Minimize" exec "_LIGX_Minimize[]"
    SEPARATOR
    "Select" submenu "RightButtonBar:Select"
    "Extend" submenu "Select:Extend"

    SEPARATOR

    "Delete" exec "EditDelete[]"
 fgcolor 'red'

ENDMENU

MENU "RightButtonBar:Select"
    "Invert" exec 'aSetSelected [Atoms[], not aSelected Atoms[]]'
 active atoms
    "Clear" exec 'aSetSelected [Atoms[],0]'
 active sel_atom
    "All" exec 'aSetSelected [Atoms[],1]' active atoms
    SEPARATOR
    "Ligand" exec "_SelectA ['', '$$ligand']" active atoms
    "Pocket" exec "_SelectA ['', '$$pocket']" active atoms
    "Receptor" exec "_SelectA ['', '$$receptor']" active atoms
    "Solvent" exec "_SelectA ['', '$$solvent']" active atoms
    "Dummy" exec "_SelectA ['Du', '']" active atoms
    SEPARATOR
    "Atom Selector..." exec "run'aselect.svl'"
ENDMENU

MENU "RightButtonBar:Surface"
    "Receptor"
 exec "run ['surfmap.svl','rec','QuickSurface']"
 active atoms
    "Ligand"
 exec "run ['surfmap.svl','lig','QuickSurface']"
 active atoms
    "Interaction (VDW)"
 exec "run ['surfmap.svl','int','QuickSurface']"
 active atoms
    "Clear"
 exec "run ['surfmap.svl','clear','QuickSurface']"
 active atoms
    SEPARATOR
    "Surfaces and Maps..."
 exec "run 'surfmap.svl'"
ENDMENU
~~~

#### moe-menus

~~~bash
#moe:menu
# moe-menus MOE default menus
#

include "$MOE/lib/menu-se"
include "$MOE/lib/menu-dbv"
include "$MOE/lib/menu-ted"
include "$MOE/lib/menu-bbar"

MENU "Main"
    "File" submenu "Main:File"
    "Edit" submenu "Main:Edit"
    "Selection" submenu "Main:Select"
    "Render" submenu "Main:Render"
    "Compute" submenu "Main:Compute"

    "GizMOE"
 MENU "GizMOE"
     "Rock and Roll" exec "GizMOE_RockAndRoll[]"
     "Energy" exec 'GizMOE_Energy[]'
     "Minimizer" exec 'GizMOE_Minimizer[]'
     "Color Force" exec 'GizMOE_ColorForce[]'
 ENDMENU

    "Window"
 MENU "Main:Window"
     "MOE" exec "WindowShow 'MOE'"
 accel 'Ctrl+m'
     "Database Viewers" SUBMENU "DatabaseViewers"
 active dbv_exists
     "Sequence Editor..." exec "SequenceEditor[]"
 accel 'Ctrl+q'
     "Atom Manager..." exec "AtomManager[]"
 accel 'Ctrl+a'
     "Alignment Constraints..."  exec "AlignmentConstraintsManager[]"
     "Graphics Object..." exec "GraphicObjectManager[]"
 accel 'Ctrl+g'
     "Crystal Parameters..." exec "run'cell.svl'"
     "Potential Setup..." exec "run'potsetup.svl'"
     SEPARATOR
     "Commands..." exec "WindowShow 'SVLCommands'"
 accel 'Ctrl+c'
     "Modules & Tasks..." exec "WindowShow 'SVLModulesTasks'"
     "Crash History..." exec "WindowShow 'SVLCrashHistory'"
     "Text Editors" SUBMENU "SVLTextEditors"
 active editor_exists
     SEPARATOR
     "Options..." exec 'OptionsWindow[]'
 ENDMENU

    "Help" submenu "Help"
ENDMENU

MENU "Main:File"
    "New"
 MENU "Main:File:New"
     "Database..." exec "run'dbvnew.svl'"
     "Pharmacophore Query..." exec "run'ph4_edit.svl'"
     "Text Editor..." exec 'ted_Open[]'
     "MOEvie..." exec "run'moevie.svl'"
 ENDMENU

    "Open..." exec "run'open.svl'"
 accel 'Ctrl+o'

    "Save..." exec "run'save.svl'"
 accel 'Ctrl+s'

    "Close" exec "Close[]"
 active data

    SEPARATOR
    "Print..." exec "run'printmoe.svl'"
 active atoms
    SEPARATOR
    "Protein Database..." exec "run'pdbbrowse.svl'"
    "PSILO/RCSB..." exec "run'rcsb.svl'"
    SEPARATOR
    "Suspend..." exec "LicenseSuspend[]"
    "Quit" exec "WindowQuit[]"
ENDMENU

MENU "Main:Edit"
    "Copy As" submenu "Main:Edit:CopyAs"
    "Paste" exec "EditPaste[]" 
    "Delete..." exec "EditDelete[]" active atoms
    SEPARATOR
    "Hydrogens" submenu "Main:Edit:Hydrogens"
    "Build" submenu "Main:Edit:Build"

    "Automatic" submenu "Main:Edit:Automatic"
    "Chirality" submenu "Main:Edit:Chirality"
    "Potential" submenu "Main:Edit:Potential"

    SEPARATOR

    "Measure" submenu "Main:Edit:Measure"
    "Superpose..." exec "Isuper[]" active atoms
ENDMENU

MENU "Main:Edit:Measure"
    "Distances" exec "run ['mkmeter.svl','create_distance']"
 active atoms
    "Angles" exec "run ['mkmeter.svl','create_angle']"
 active atoms
    "Dihedrals" exec "run ['mkmeter.svl','create_dihedral']"
 active atoms
    SEPARATOR
    "Remove All" exec "run ['mkmeter.svl','delete_all']"
 active atoms
    SEPARATOR
    "Remove Distances" exec "run ['mkmeter.svl','delete_distance']"
 active atoms
    "Remove Angles" exec "run ['mkmeter.svl','delete_angle']"
 active atoms
    "Remove Dihedrals" exec "run ['mkmeter.svl','delete_dihedral']"
 active atoms
ENDMENU

MENU "Main:Edit:CopyAs"
    "MOE" active atoms exec "run ['save.svl','MOE',   'CopyMainWindow']"
    "PDB" active atoms exec "run ['save.svl','PDB',   'CopyMainWindow']"
    "MOL (3D)" active atoms exec "run ['save.svl','MOL3D', 'CopyMainWindow']"
    "MOL (2D)" active atoms exec "run ['save.svl','MOL2D', 'CopyMainWindow']"
    "SMILES" active atoms exec "run ['save.svl','SMILES','CopyMainWindow']"
    "MOL2" active atoms exec "run ['save.svl','MOL2',  'CopyMainWindow']"
    "MMD" active atoms exec "run ['save.svl','MMD',   'CopyMainWindow']"
    "MAE" active atoms exec "run ['save.svl','MAE',   'CopyMainWindow']"
    "XTL" active atoms exec "run ['save.svl','XTL',   'CopyMainWindow']"
    "Picture" active atoms exec "run ['save.svl','BMP',   'CopyMainWindow']"
ENDMENU

MENU "Main:Edit:Automatic"
    "Connect and Type" exec "EditAutoConnectType[]" active atoms
    "Connect Only" exec "EditAutoConnect[]" active atoms
    "Reconnect Only" exec "EditAutoReconnect[]" active atoms
    "Type Only" exec "EditAutoType[]" active atoms
ENDMENU

MENU "Main:Edit:Hydrogens"
    "Add Hydrogens" exec "_EditH 'addH'" active atoms
    "Add Polar Hydrogens" exec "_EditH 'addHpolar'" active atoms
    "Add Hydrogens and LPs" exec "_EditH 'addHLP'" active sel_atom
    "Delete Hydrogens" exec "_EditH 'delH'" active atoms
    "Delete Nonpolar Hydrogens" exec "_EditH 'delHnonpolar'" active atoms
    "Delete Lone Pairs" exec "_EditH 'delLP'" active atoms
ENDMENU

MENU "Main:Edit:Chirality"
    "R / Z"      exec "_EditChirality'R'" active sel_atom
    "S / E"      exec "_EditChirality'S'" active sel_atom
    "Geometry" exec "_EditChirality'geom'" active sel_atom
    "Clear" exec "_EditChirality'clear'" active sel_atom
ENDMENU

MENU "Main:Edit:Potential"
    "Fix" exec "_EditPot['aFixed',1]" active sel_atom
    "Unfix" exec "_EditPot['aFixed',0]" active sel_atom
    "Inert" exec "_EditPot['aInert',1]" active sel_atom
    "Active" exec "_EditPot['aInert',0]" active sel_atom
    "Wall" exec "_EditPot['aWall' ,1]" active sel_atom
    "Unwall" exec "_EditPot['aWall' ,0]" active sel_atom
    "State"
 MENU "Main:Edit:State"
     "0" exec "_EditPot['aState',0]" active sel_atom
     "1" exec "_EditPot['aState',1]" active sel_atom
     "2" exec "_EditPot['aState',2]" active sel_atom
     "3" exec "_EditPot['aState',3]" active sel_atom
     "Molecule" exec "_EditPot['aState','mol']" active sel_atom
     "Tag" exec "_EditPot['aState','tag']" active sel_atom
 ENDMENU
    SEPARATOR
    "Restrain..." exec "run'restrain.svl'" active atoms
ENDMENU

MENU "Main:Edit:Build"
    "Molecule..." exec "run'builder.svl'"
    "Carbohydrate..." exec "CarboBuilder[]"
    SEPARATOR
    "Repeat Unit..." exec "RepeatUnitPrompt[]"
    "Polymer..." exec "PolymerBuilderPanel[]"
    SEPARATOR
    "Protein..." exec "pro_Builder[]"
    "Sequence..." exec "SE_CreateSequence[]"
    "Rotamer Explorer..." exec "run'rotexpl.svl'"
    SEPARATOR
    "Solvate..." exec "run'solvate.svl'"
ENDMENU

MENU "Main:Compute"
    "Potential Energy" exec 'MeasurePotential[]' 
 active atoms
    "Protonate 3D..." exec "run'protonate3d_ui.svl'"
 active atoms
    "Partial Charges..." exec 'PartialChargePanel[]'
 active atoms
    "Energy Minimize..." exec "run'emin.svl'"
 active atoms
    SEPARATOR

    "Site Finder..." exec "run'sitefind.svl'"
 active atoms
    "Surfaces and Maps..." exec "run'surfmap.svl'"
    "Ligand Interactions..." exec "run'prolig2d.svl'"
 active atoms
    "Protomers..." exec "run'protoview.svl'"
 active atoms
    "2D Molecules..." exec "run ['view2d.svl', []]"

    SEPARATOR
    "Pharmacophore"
 MENU "Main:Compute:Pharmacophore"
     "Query Editor..." exec "run'ph4_edit.svl'"
     "Elucidation..." exec "ph4_Elucidate[]"
     "Search..."  exec "run'ph4_search.svl'"
 ENDMENU

    "Fragments"
 MENU "Main:Compute:Fragments"
     "Scaffold Replacement..."
 exec "run['fragments_ui.svl','ScaffRepl']"
     "Link Multiple Fragments..."
 exec "run['fragments_ui.svl','LinkFrag']"
     "Add Group to Ligand..."
 exec "run['fragments_ui.svl','AddGroup']"
     "MedChem Transformations..."
 exec "run['fragments_ui.svl','MedChemTrns']"
     "BREED..."
 exec "run['fragments_ui.svl','BREED']"
     "RECAP Analysis..."
 exec "run['recap_ui.svl','analysis']"
     "RECAP Synthesis..."
 exec "run['recap_ui.svl','synthesis']"
     "MultiFragment Search..."
 exec "run'mfss.svl'"
 active atoms
 ENDMENU

    "Conformations"
 MENU "Main:Compute:Conformations"
     "Conformational Search..." exec "run 'confsrch.svl'"
     "Conformation Import..." exec "run'conf_ui.svl'"
     "Dihedral Energy Plot..." exec 'DihedralEnergyPlot[]'
 active atoms
     "Dihedral Contour Plot..." exec 'DihedralEnergyContour[]'
 active atoms
 ENDMENU

    "Biopolymer" MENU "Main:Compute:Biopolymer"
 "PDB Search..." exec "run'searchpdb.svl'"
 "Kinase Search..." exec "run'kinsearch.svl'"
 "Align..." exec "run'proalign_ui.svl'"
 "Superpose..." exec 'pro_Superpose[]'
 "Consensus..." exec 'pro_Consensus[]'
 SEPARATOR
 "Homology Model..." exec "run'promodel_ui.svl'"
 "Antibody Modeler..." exec "run'fabmodel.svl'"
 "Rotamer Explorer..." exec "run'rotexpl.svl'"
 SEPARATOR
 "Residue pKa..." exec "run'propka.svl'"
 "Protein Contacts..." exec 'pro_Contacts[]'
 "Protein Geometry..." exec "run'progeom.svl'"
    ENDMENU

    "QuaSAR" MENU "QuaSAR"
 "Model-Composer..." exec "run'model.svl'"
 "Model-Evaluate..." exec "model_Evaluate[]"
 "Calculate Descriptors..." exec "run'qdesc.svl'"
 "QuaSAR-Model..." exec "QuaSAR_Model[]"
 "QuaSAR-Classify..." exec "run'qbct.svl'"
 "QuaSAR-Cluster..." exec "QuaSAR_Cluster[]"
 "QuaSAR-Reagent..." exec "QuaSAR_Reagent[]"
 "QuaSAR-CombiGen..." exec "QuaSAR_CombiGen[]"
 "QuaSAR-CombiDesign..." exec "QuaSAR_CombiDesign[]"
 "QuaSAR-HoleFiller..." exec "QuaSAR_HoleFiller[]"
    ENDMENU

    "Simulations" MENU "Main:Compute:Simulations"
 "Dock..." exec "run'dock_ui.svl'"
 active atoms
 "Flexible Alignment..." exec "FlexAlignPanel[]"
 active atoms
 "SAReport..."
     exec "run ['sareport.svl', [], 'SAReportUI']"
 "SCF Calculation..." exec "run'scfpanel.svl'"
 active atoms

 "Dynamics..." exec "run'md_ui.svl'"
 "Diffraction..." exec "run'diffr.svl'"
 active atoms
 "Polymer Properties..." exec 'PolymerPropertiesPanel[]'
 active atoms
    ENDMENU

    SEPARATOR

    "Priority" MENU "Main:Compute:Priority"
 "Highest" exec "exe_setpriority[0,1]"
 value is_prio_highest
 active use_prio_highest
 "Above Normal" exec "exe_setpriority[0,0.5]"
 value is_prio_above
 active use_prio_above
 "Normal" exec "exe_setpriority[0,0]"
 value is_prio_normal
 active use_prio_normal
 "Below Normal" exec "exe_setpriority[0,-0.5]"
 value is_prio_below
 active use_prio_below
 "Lowest" exec "exe_setpriority[0,-1]"
 value is_prio_lowest
 active use_prio_lowest
    ENDMENU

ENDMENU

MENU "Help"
    "Contents..." exec "LaunchDocument'$MOE/html/index.htm'"
    "Panel Index..." exec "LaunchDocument'$MOE/html/panelindex.html'"
    "Function Index..." exec "LaunchDocument'$MOE/html/fcnindex.html'"
    SEPARATOR
    "Mouse..." exec "run'mouseref.svl'"
    "Tutorials" MENU "Help:Tutorial"
 "Getting Started..."
     exec "LaunchDocument'$MOE/html/tutorials/moetour.html'"
 "Visualization and Making Pictures..."
     exec "LaunchDocument'$MOE/html/tutorials/graphics_tut.htm'"
 "Building Molecules..."
     exec "LaunchDocument'$MOE/html/tutorials/builder_tut.htm'"
 SEPARATOR
 "Building Carbohydrates..."
     exec "LaunchDocument'$MOE/html/tutorials/carbo_tut.htm'"
 "Docking Tutorial..."
     exec "LaunchDocument'$MOE/html/tutorials/dock_tut.htm'"
 "Flexible Alignment of Molecules..."
     exec "LaunchDocument'$MOE/html/tutorials/flex_tut.htm'"
 "LowModeMD..."
     exec "LaunchDocument'$MOE/html/tutorials/lmmd_tut.htm'"
 "MedChem Transformations In-Cleft..."
     exec "LaunchDocument'$MOE/html/tutorials/medchemtrns_tut.htm'"
 "Homology Modeling of Proteins..."
     exec "LaunchDocument'$MOE/html/tutorials/hom_tut.htm'"
 "Protein Alignment..."
     exec "LaunchDocument'$MOE/html/tutorials/protalign_tut.htm'"
 "LigX Tutorial..."
     exec "LaunchDocument'$MOE/html/tutorials/ligx_tut.htm'"
 "Pharmacophore Searching..."
     exec "LaunchDocument'$MOE/html/tutorials/ph4_tut.htm'"
 "PLIF Tutorial..."
     exec "LaunchDocument'$MOE/html/tutorials/plif_tut.htm'"
 "QSAR..."
     exec "LaunchDocument'$MOE/html/tutorials/quasar_tut.htm'"
 "Scaffold Replacement..."
     exec "LaunchDocument'$MOE/html/tutorials/scaff_tut.htm'"
 "SD Tools..."
     exec "LaunchDocument'$MOE/html/tutorials/sdfrag_tut.html'"
 SEPARATOR
 "Prepare a Small Molecule..."
     exec "LaunchDocument'$MOE/html/moe/mol_prep.htm'"
 "Prepare a Protein or Protein-Ligand Complex..."
     exec "LaunchDocument'$MOE/html/proteins/proprep.htm'"
 "Prepare a Small Molecule Dataset..."
     exec "LaunchDocument'$MOE/html/moe/moldb_prep.htm'"
 "Prepare a Conformation Database..."
     exec "LaunchDocument'$MOE/html/moe/prep3ddb.htm'"
 SEPARATOR
 "SVL Basics..."
     exec "LaunchDocument'$MOE/html/tutorials/svltour.html'"
 "MOE Programming..."
     exec "LaunchDocument'$MOE/html/tutorials/mpgtut.html'"
 "Window Toolkit..."
     exec "LaunchDocument'$MOE/html/tutorials/wintour.html'"
    ENDMENU
    SEPARATOR
    "Release Notes..." exec "LaunchDocument'$MOE/html/rnotes.htm'"
    "License Info..." exec "run'licinfo.svl'"
    "OpenGL Info..." exec "run'oglinfo.svl'"
ENDMENU

# ================================= RENDER ===================================

MENU "MOE:Trackball"
    "View" title
    "Reset" exec "ViewReset[]; View (Atoms[] | aSelected Atoms[])"
    "Load"
 MENU "Main:Trackball:Load"
     columns 2
     "  1  " exec 'ViewLoad 1' active view_save_1
     "  2  " exec 'ViewLoad 2' active view_save_2
     "  3  " exec 'ViewLoad 3' active view_save_3
     "  4  " exec 'ViewLoad 4' active view_save_4
     "  5  " exec 'ViewLoad 5' active view_save_5
     "  6  " exec 'ViewLoad 6' active view_save_6
     "  7  " exec 'ViewLoad 7' active view_save_7
     "  8  " exec 'ViewLoad 8' active view_save_8
 ENDMENU
    "Save"
 MENU "Main:Trackball:Save"
     columns 2
     "  1  " exec 'ViewSave 1'
     "  2  " exec 'ViewSave 2'
     "  3  " exec 'ViewSave 3'
     "  4  " exec 'ViewSave 4'
     "  5  " exec 'ViewSave 5'
     "  6  " exec 'ViewSave 6'
     "  7  " exec 'ViewSave 7'
     "  8  " exec 'ViewSave 8'
 ENDMENU
ENDMENU

MENU "Main:Render"
    "Center" exec "View (Atoms[] | aSelected Atoms[])"
    "Hide" submenu "Render:Hide" exec "_RenderHide[]"
    "Show" submenu "Render:Show" exec "_RenderShow[]"
    "Atoms" submenu "MOE:AtomStyle" active atoms
    "Ribbon" submenu "MOE:RibbonStyle" active atoms
    "Contacts" submenu "MOE:Contacts" active atoms
    SEPARATOR
    "Draw" submenu "Render:Draw"
    "Stereo" submenu "Render:Stereo"
    "Full Screen (F12)" exec "FullScreen not FullScreen []"
    "Setup..." exec "run'vsetup.svl'"
ENDMENU

MENU "MOE:Popup"
    "Center" exec "View (Atoms[] | aSelected Atoms[])"
    "Hide" submenu "Render:Hide" exec "_RenderHide[]"
    "Show" submenu "Render:Show" exec "_RenderShow[]"
    "Atoms" submenu "MOE:AtomStyle" active atoms
    "Ribbon" submenu "MOE:RibbonStyle" active atoms
    "Contacts" submenu "MOE:Contacts"
    SEPARATOR
    "Select" submenu "Main:Select"
    SEPARATOR
    "Draw" submenu "Render:Draw"
    "Stereo" submenu "Render:Stereo"
    "Full Screen" exec "FullScreen not FullScreen []"
ENDMENU

MENU "Render:Draw"
    "Coordinate Axes" exec 'DrawAxes not DrawAxes[]'
 value mol_axes
    "High Quality Rotation"
     exec 'HighQualityRotation not HighQualityRotation[]'
 value mol_highqualityrotation
    "High Quality Anti-Alias" exec '_HighQualityAntiAlias (AntiAlias[] < 2)'
 value mol_antialias
    SEPARATOR
    "Small Font" value mol_fontsmall exec "FontSize'small'"
    "Medium Font" value mol_fontmedium exec "FontSize'medium'"
    "Large Font" value mol_fontlarge exec "FontSize'large'"
    "Bold Font" value mol_fontbold exec "FontBold not FontBold[]"
    "Fixed Width Font" value mol_fontfixed exec "FontFixed not FontFixed[]"
    SEPARATOR
    "Save As Default..." exec 'RenderSaveDrawDefaults[]'
ENDMENU

# Render:Stereo handles the stereoscopic rendering modes

MENU "Render:Stereo"
    "Perspective" exec "Stereo 'none'" value mol_perspective
    "Parallel" exec "Stereo 'parallel'" value mol_parallel
    "Quad Buffer" exec "Stereo 'quad-buffer'" value mol_stereo
    "ISL Autostereo" exec "Stereo 'isl'" value mol_isl
    "Over-Under" exec "Stereo 'over-under'" value mol_overunder
    "Interlace" exec "Stereo 'interlace'" value mol_interlace
    "Left-Right" exec "Stereo 'left-right'" value mol_splitpair
    "Green-Magenta" exec "Stereo 'anaglyph'" value mol_anaglyph
    SEPARATOR
    "Settings..." exec "run'stereo.svl'"
ENDMENU

MENU "Render:Hide"
    "All Atoms" name "allAtoms" active atoms
    "Selected" name "selectedAtoms" active atoms
    "Unselected" name "unselectedAtoms" active atoms
    SEPARATOR
    "Hydrogens" name "allH" active atoms
    "Polar Hydrogens" name "polarH" active atoms
    "Nonpolar Hydrogens" name "nonpolarH" active atoms
    SEPARATOR
    "Ligand" name "$$ligand" active atoms
    "Pocket" name "$$pocket" active atoms
    "Receptor" name "$$receptor" active atoms
    "Solvent" name "$$solvent" active atoms
    "Dummy" name "dummy" active atoms
    SEPARATOR
    "Backbone" name "$$backbone" active atoms
    "Sidechain" name "$$sidechain" active atoms
ENDMENU

MENU "Render:Show"
    "All Atoms" name "allAtoms" active atoms
    "Selected" name "selectedAtoms" active atoms
    "Unselected" name "unselectedAtoms" active atoms
    "More (4.5A)" name "prox:4.5" active atoms
    SEPARATOR
    "Hydrogens" name "allH" active atoms
    "Polar Hydrogens" name "polarH" active atoms
    "Nonpolar Hydrogens" name "nonpolarH" active atoms
    SEPARATOR
    "Ligand" name "$$ligand" active atoms
    "Pocket" name "$$pocket" active atoms
    "Receptor" name "$$receptor" active atoms
    "Solvent" name "$$solvent" active atoms
    "Dummy" name "dummy" active atoms
    SEPARATOR
    "Backbone" name "$$backbone" active atoms
    "Sidechain" name "$$sidechain" active atoms
ENDMENU

# ================================= SELECT ===================================

MENU "Main:Select"
    "Invert" exec 'aSetSelected [Atoms[], not aSelected Atoms[]]'
 active atoms
    "Clear" exec 'aSetSelected [Atoms[],0]' active sel_atom
    "All" exec 'aSetSelected [Atoms[],1]' active atoms

    "Extend" submenu "Select:Extend"

    SEPARATOR
    "Ligand" exec "_SelectA ['','$$ligand']" active atoms
    "Pocket" exec "_SelectA ['','$$pocket']" active atoms
    "Receptor" exec "_SelectA ['','$$receptor']" active atoms
    "Solvent" exec "_SelectA ['','$$solvent']" active atoms
    "Dummy" exec "_SelectA ['Du','']" active atoms
    SEPARATOR
    "Attachment" submenu "Select:Attachment"
    "Element" submenu "Select:Element"
    "Geometry" submenu "Select:Geometry"
    "Potential" submenu "Select:Potential"
    "Protein" submenu "Select:Protein"

    "Atom Selector..." exec "run'aselect.svl'" active atoms

    SEPARATOR
    "Save" exec 'SaveSelection[]' active atoms
    "Restore" exec 'RestoreSelection[]' active atoms
    SEPARATOR
    "Synchronize" value syncselect
 exec "SyncSelection not SyncSelection[]"
ENDMENU

# Select:Accessibility selects atoms based upon buriedness

MENU "Select:Accessibility"
    "Buried" exec "_SelectA 'aBuried'" active atoms
    "Buried Hydrophilic" exec "_SelectA 'aBuriedLPA'" active atoms
    "Exposed" exec "_SelectA 'aExposed'" active atoms
    "Exposed Grease" exec "_SelectA 'aExposedHYD'" active atoms
ENDMENU

# Select:Attachment selects A0, A1, ... named atoms

MENU "Select:Attachment"
    "Any" exec "_SelectA 'A*'" active atoms
    "A0" exec "_SelectA 'A0'" active atoms
    "A1" exec "_SelectA 'A1'" active atoms
    "A2" exec "_SelectA 'A2'" active atoms
    "A3" exec "_SelectA 'A3'" active atoms
    "A4" exec "_SelectA 'A4'" active atoms
    "A5" exec "_SelectA 'A5'" active atoms
    "A6" exec "_SelectA 'A6'" active atoms
    "A7" exec "_SelectA 'A7'" active atoms
    "A8" exec "_SelectA 'A8'" active atoms
    "A9" exec "_SelectA 'A9'" active atoms
ENDMENU

# Select:Element handles the element-specific selections

MENU "Select:Element"
    "Heavy Atom" exec "_SelectA 'Q'" active atoms
    "Hydrogen" exec "_SelectA 'H'" active atoms
    "Polar Hydrogen" exec "_SelectA 'PolarH'" active atoms
    "Non-polar Hydrogen" exec "_SelectA 'NonpolarH'" active atoms
    "Lone Pair" exec "_SelectA 'LP'" active atoms
    "Dummy" exec "_SelectA 'Du'" active atoms
    SEPARATOR
    "Non-Metal" exec "_SelectA 'Non-Metal'" active atoms
    "Semi-Metal" exec "_SelectA 'Semi-Metal'" active atoms
    "Metal" exec "_SelectA 'Metal'" active atoms
    "Transition Metal" exec "_SelectA 'TM'" active atoms
ENDMENU

# Select:Extend handles the extension of the selection set

MENU "Select:Extend"
    "Bonded To" exec 'SelectionExtendBonded[]'
 active sel_atom
    "H and LP" exec 'SelectionExtendHLP[]'
 active sel_atom
    "Molecule" exec 'SelectionExtendMolecule[]'
 active sel_atom
    "Near (4.5A)" exec 'SelectionExtendProximity 4.5'
 active sel_atom
    "Near Residues" exec 'SelectionExtendResidueProximity 4.5'
 active sel_atom
    "Residue" exec 'SelectionExtendResidue[]'
 active sel_atom
    "Chain" exec 'SelectionExtendChain[]'
 active sel_atom
    "Chain Tag" exec 'SelectionExtendChainTag[]'
 active sel_atom
ENDMENU

# Select:Geometry handles geometry-specific selections

MENU "Select:Geometry"
    "Linear" exec "_SelectA 'aLinear'" active atoms
    "Planar" exec "_SelectA 'aPlanar'" active atoms
    "Tetrahedral" exec "_SelectA 'aTetrahedral'" active atoms
    "Pi Bonded" exec "_SelectA 'aPiBonded'" active atoms
    "Aromatic" exec "_SelectA 'aInHRing'" active atoms
    "d-Hybridized" exec "_SelectA 'aDHybridized'" active atoms
    "Chiral" exec "_SelectA 'aChiral'" active atoms
    "Chiral R" exec "_SelectA 'aChiralR'" active atoms
    "Chiral S" exec "_SelectA 'aChiralS'" active atoms
    "StereoBond Z / E" exec "_SelectA 'aStereoZE'" active atoms
    "StereoBond Z" exec "_SelectA 'aStereoZ'" active atoms
    "StereoBond E" exec "_SelectA 'aStereoE'" active atoms
ENDMENU

# Select:Pharmacophore handles selection of pharmacophore types

MENU "Select:Pharmacophore"
    "Acceptor" exec "_SelectA 'aAcceptor'" active atoms
    "Acid" exec "_SelectA 'aAcid'" active atoms
    "Anion" exec "_SelectA 'aAnion'" active atoms
    "Aromatic" exec "_SelectA 'aInHRing'" active atoms
    "Base" exec "_SelectA 'aBase'" active atoms
    "Donor" exec "_SelectA 'aDonor'" active atoms
    "Cation" exec "_SelectA 'aCation'" active atoms
    "Grease" exec "_SelectA 'aGrease'" active atoms
    "Hydrophobe" exec "_SelectA 'aHydrophobe'" active atoms
ENDMENU

# Select:Potential handles the potential/forcefield specific selections

MENU "Select:Potential"
    "Fixed" exec "_SelectA 'aFixed'" active atoms
    "Forced Chirality"
 MENU "Select:Potential:Chiral"
     "R" exec "_SelectA 'aForceR'" active atoms
     "S" exec "_SelectA 'aForceS'" active atoms
     "R or S" exec "_SelectA 'aForceRS'" active atoms
 ENDMENU
    "Forced StereoBond"
 MENU "Select:Potential:StereoBond"
     "Z" exec "_SelectA 'aForceZ'" active atoms
     "E" exec "_SelectA 'aForceE'" active atoms
     "Z or E" exec "_SelectA 'aForceZE'" active atoms
 ENDMENU
    "Inert" exec "_SelectA 'aInert'" active atoms
    "Tethered" exec "_SelectA 'aTether'" active atoms
    "Restrained" exec "_SelectA 'aRestrained'" active atoms
    "Walled" exec "_SelectA 'aWall'" active atoms
    "Untyped" exec "_SelectA 'aMMType??'" active atoms
ENDMENU

# Select:Protein handles protein-specific selections

MENU "Select:Protein"
    "Alpha Carbons" exec "_SelectA ['','$$alphaC']" active atoms
    "Beta Carbons" exec "_SelectA ['','$$betaC']" active atoms
    "Backbone Atoms" exec "_SelectA ['','$$backbone']" active atoms
    "Sidechain Atoms" exec "_SelectA ['','$$sidechain']" active atoms
ENDMENU

# Selectd:Ring handles ring-specific selections

MENU "Select:Ring"
    "Any" exec "_SelectA 'aInRing'" active atoms
    "Aromatic" exec "_SelectA 'aInHRing'" active atoms
    "Large" exec "_SelectA 'aInLargeRing'" active atoms
    "Small" exec "_SelectA 'aInSmallRing'" active atoms
    "Spiro Center" exec "_SelectA 'aSpiro'" active atoms
    "Fused Center" exec "_SelectA 'aFused'" active atoms
    "3-Ring" exec "_SelectA 'aIn3Ring'" active atoms
    "4-Ring" exec "_SelectA 'aIn4Ring'" active atoms
    "5-Ring" exec "_SelectA 'aIn5Ring'" active atoms
    "6-Ring" exec "_SelectA 'aIn6Ring'" active atoms
    "7-Ring" exec "_SelectA 'aIn7Ring'" active atoms
    "8-Ring" exec "_SelectA 'aIn8Ring'" active atoms
ENDMENU
~~~

------
