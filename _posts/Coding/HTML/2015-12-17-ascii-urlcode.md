---
layout: post
title: ASCII值和网址特殊符号转换码对照
date: 2015-12-17 09:23:36
categories: Coding
tags: HTML Website Python
---

### Python转换编码

- `urllib.quote`(sring[,safe]) : 将字符串转为URL编码.safe是不会被转换的字符, 默认是`/`
- `urllib.unquote`(sring) : 将字符串从URL编码转回ASCII
- 类似地还有URL编码的: `urllib2.quote`(sring), `requests.utils.quote`(sring)
- 类似地还有URL反编码的: `urllib2.unquote`(sring), `requests.utils.unquote`(sring)
- `urllib.quote_plus`(sring[,safe]) : 将字符串转为URL编码, 其中的空格会被`+`取代. 原字符串的`+`会被转码,空格转新`+`. 反编码使用`urllib.unquote_plus`(sring)

> 使用编码转换时, 默认`/`,`.`,`_`,`-`是不会被转换的.其余包括空格,`&`都会被转换.可以通过控制safe参数改变一些规则.  
> 对于unicode如果有编码问题, 可以`urllib.quote(s.encode('utf-8'))`,反编码可以`urllib.unquote(s).decode('utf-8')`


### ASCII值和网址特殊符号转换码对照:

ASCII Value	|	URL-encode	|	ASCII Value	|	URL-encode	|	ASCII Value	|	URL-encode
æ	|	%00	|	0	|	%30	|	`	|	%60
 	|	%01	|	1	|	%31	|	a	|	%61
 	|	%02	|	2	|	%32	|	b	|	%62
 	|	%03	|	3	|	%33	|	c	|	%63
 	|	%04	|	4	|	%34	|	d	|	%64
 	|	%05	|	5	|	%35	|	e	|	%65
 	|	%06	|	6	|	%36	|	f	|	%66
 	|	%07	|	7	|	%37	|	g	|	%67
backspace	|	%08	|	8	|	%38	|	h	|	%68
tab	|	%09	|	9	|	%39	|	i	|	%69
linefeed	|	%0a	|	:	|	%3a	|	j	|	%6a
 	|	%0b	|	;	|	%3b	|	k	|	%6b
 	|	%0c	|	<	|	%3c	|	l	|	%6c
c return	|	%0d	|	=	|	%3d	|	m	|	%6d
 	|	%0e	|	>	|	%3e	|	n	|	%6e
 	|	%0f	|	?	|	%3f	|	o	|	%6f
 	|	%10	|	@	|	%40	|	p	|	%70
 	|	%11	|	A	|	%41	|	q	|	%71
 	|	%12	|	B	|	%42	|	r	|	%72
 	|	%13	|	C	|	%43	|	s	|	%73
 	|	%14	|	D	|	%44	|	t	|	%74
 	|	%15	|	E	|	%45	|	u	|	%75
 	|	%16	|	F	|	%46	|	v	|	%76
 	|	%17	|	G	|	%47	|	w	|	%77
 	|	%18	|	H	|	%48	|	x	|	%78
 	|	%19	|	I	|	%49	|	y	|	%79
 	|	%1a	|	J	|	%4a	|	z	|	%7a
 	|	%1b	|	K	|	%4b	|	{	|	%7b
 	|	%1c	|	L	|	%4c	|	\|	|	%7c
 	|	%1d	|	M	|	%4d	|	}	|	%7d
 	|	%1e	|	N	|	%4e	|	~	|	%7e
 	|	%1f	|	O	|	%4f	|	 	|	%7f
space	|	%20	|	P	|	%50	|	€	|	%80
!	|	%21	|	Q	|	%51	|	 	|	%81
"	|	%22	|	R	|	%52	|	‚	|	%82
\#	|	%23	|	S	|	%53	|	ƒ	|	%83
$	|	%24	|	T	|	%54	|	„	|	%84
%	|	%25	|	U	|	%55	|	…	|	%85
&	|	%26	|	V	|	%56	|	†	|	%86
'	|	%27	|	W	|	%57	|	‡	|	%87
(	|	%28	|	X	|	%58	|	ˆ	|	%88
)	|	%29	|	Y	|	%59	|	‰	|	%89
*	|	%2a	|	Z	|	%5a	|	Š	|	%8a
+	|	%2b	|	[	|	%5b	|	‹	|	%8b
,	|	%2c	|	\	|	%5c	|	Œ	|	%8c
-	|	%2d	|	]	|	%5d	|	 	|	%8d
.	|	%2e	|	^	|	%5e	|	Ž	|	%8e
/	|	%2f	|	_	|	%5f	|	 	|	%8f


ASCII Value	|	URL-encode	|	ASCII Value	|	URL-encode	|	ASCII Value	|	URL-encode
 	|	%90	|	À	|	%c0	|	ð	|	%f0
‘	|	%91	|	Á	|	%c1	|	ñ	|	%f1
’	|	%92	|	Â	|	%c2	|	ò	|	%f2
“	|	%93	|	Ã	|	%c3	|	ó	|	%f3
”	|	%94	|	Ä	|	%c4	|	ô	|	%f4
•	|	%95	|	Å	|	%c5	|	õ	|	%f5
–	|	%96	|	Æ	|	%c6	|	ö	|	%f6
—	|	%97	|	Ç	|	%c7	|	÷	|	%f7
˜	|	%98	|	È	|	%c8	|	ø	|	%f8
™	|	%99	|	É	|	%c9	|	ù	|	%f9
š	|	%9a	|	Ê	|	%ca	|	ú	|	%fa
›	|	%9b	|	Ë	|	%cb	|	û	|	%fb
œ	|	%9c	|	Ì	|	%cc	|	ü	|	%fc
 	|	%9d	|	Í	|	%cd	|	ý	|	%fd
ž	|	%9e	|	Î	|	%ce	|	þ	|	%fe
Ÿ	|	%9f	|	Ï	|	%cf	|	ÿ	|	%ff
 	|	%a0	|	Ð	|	%d0	|	 	|	 
¡	|	%a1	|	Ñ	|	%d1	|	 	|	 
¢	|	%a2	|	Ò	|	%d2	|	 	|	 
£	|	%a3	|	Ó	|	%d3	|	 	|	 
 	|	%a4	|	Ô	|	%d4	|	 	|	 
¥	|	%a5	|	Õ	|	%d5	|	 	|	 
`|`	|	%a6	|	Ö	|	%d6	|	 	|	 
§	|	%a7	|	 	|	%d7	|	 	|	 
¨	|	%a8	|	Ø	|	%d8	|	 	|	 
©	|	%a9	|	Ù	|	%d9	|	 	|	 
ª	|	%aa	|	Ú	|	%da	|	 	|	 
«	|	%ab	|	Û	|	%db	|	 	|	 
¬	|	%ac	|	Ü	|	%dc	|	 	|	 
¯	|	%ad	|	Ý	|	%dd	|	 	|	 
®	|	%ae	|	Þ	|	%de	|	 	|	 
¯	|	%af	|	ß	|	%df	|	 	|	 
°	|	%b0	|	à	|	%e0	|	 	|	 
±	|	%b1	|	á	|	%e1	|	 	|	 
²	|	%b2	|	â	|	%e2	|	 	|	 
³	|	%b3	|	ã	|	%e3	|	 	|	 
´	|	%b4	|	ä	|	%e4	|	 	|	 
µ	|	%b5	|	å	|	%e5	|	 	|	 
¶	|	%b6	|	æ	|	%e6	|	 	|	 
·	|	%b7	|	ç	|	%e7	|	 	|	 
¸	|	%b8	|	è	|	%e8	|	 	|	 
¹	|	%b9	|	é	|	%e9	|	 	|	 
º	|	%ba	|	ê	|	%ea	|	 	|	 
»	|	%bb	|	ë	|	%eb	|	 	|	 
¼	|	%bc	|	ì	|	%ec	|	 	|	 
½	|	%bd	|	í	|	%ed	|	 	|	 
¾	|	%be	|	î	|	%ee	|	 	|	 
¿	|	%bf	|	ï	|	%ef	|	 	|	 

参考: [Py3-urllib.parse](https://docs.python.org/3/library/urllib.parse.html)

------
