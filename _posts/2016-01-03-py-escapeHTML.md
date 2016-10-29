---
layout: post
title: Python:Escape和Unescape特殊字符
date: 2016-01-03 05:40:01
categories: Coding
tags: Python HTML
---

今晚(8号..)被HTML的特殊字符搞晕了..在endnote中输出的xml中使用的是HTML方式处理,将特殊符号escape掉成例如`&amp;` 这种..下面是特殊符号和名字实体对照表.


特殊符号	|	命名实体	|	十进制编码	|	特殊符号	|	命名实体	|	十进制编码	|	特殊符号	|	命名实体	|	十进制编码
Α	|	&amp;Alpha;	|	&amp;#913;	|	Β	|	&amp;Beta;	|	&amp;#914;	|	Γ	|	&amp;Gamma;	|	&amp;#915;
Δ	|	&amp;Delta;	|	&amp;#916;	|	Ε	|	&amp;Epsilon;	|	&amp;#917;	|	Ζ	|	&amp;Zeta;	|	&amp;#918;
Η	|	&amp;Eta;	|	&amp;#919;	|	Θ	|	&amp;Theta;	|	&amp;#920;	|	Ι	|	&amp;Iota;	|	&amp;#921;
Κ	|	&amp;Kappa;	|	&amp;#922;	|	Λ	|	&amp;Lambda;	|	&amp;#923;	|	Μ	|	&amp;Mu;	|	&amp;#924;
Ν	|	&amp;Nu;	|	&amp;#925;	|	Ξ	|	&amp;Xi;	|	&amp;#926;	|	Ο	|	&amp;Omicron;	|	&amp;#927;
Π	|	&amp;Pi;	|	&amp;#928;	|	Ρ	|	&amp;Rho;	|	&amp;#929;	|	Σ	|	&amp;Sigma;	|	&amp;#931;
Τ	|	&amp;Tau;	|	&amp;#932;	|	Υ	|	&amp;Upsilon;	|	&amp;#933;	|	Φ	|	&amp;Phi;	|	&amp;#934;
Χ	|	&amp;Chi;	|	&amp;#935;	|	Ψ	|	&amp;Psi;	|	&amp;#936;	|	Ω	|	&amp;Omega;	|	&amp;#937;
α	|	&amp;alpha;	|	&amp;#945;	|	β	|	&amp;beta;	|	&amp;#946;	|	γ	|	&amp;gamma;	|	&amp;#947;
δ	|	&amp;delta;	|	&amp;#948;	|	ε	|	&amp;epsilon;	|	&amp;#949;	|	ζ	|	&amp;zeta;	|	&amp;#950;
η	|	&amp;eta;	|	&amp;#951;	|	θ	|	&amp;theta;	|	&amp;#952;	|	ι	|	&amp;iota;	|	&amp;#953;
κ	|	&amp;kappa;	|	&amp;#954;	|	λ	|	&amp;lambda;	|	&amp;#955;	|	μ	|	&amp;mu;	|	&amp;#956;
ν	|	&amp;nu;	|	&amp;#957;	|	ξ	|	&amp;xi;	|	&amp;#958;	|	ο	|	&amp;omicron;	|	&amp;#959;
π	|	&amp;pi;	|	&amp;#960;	|	ρ	|	&amp;rho;	|	&amp;#961;	|	ς	|	&amp;sigmaf;	|	&amp;#962;
σ	|	&amp;sigma;	|	&amp;#963;	|	τ	|	&amp;tau;	|	&amp;#964;	|	υ	|	&amp;upsilon;	|	&amp;#965;
φ	|	&amp;phi;	|	&amp;#966;	|	χ	|	&amp;chi;	|	&amp;#967;	|	ψ	|	&amp;psi;	|	&amp;#968;
ω	|	&amp;omega;	|	&amp;#969;	|	ϑ	|	&amp;thetasym;	|	&amp;#977;	|	ϒ	|	&amp;upsih;	|	&amp;#978;
ϖ	|	&amp;piv;	|	&amp;#982;	|	•	|	&amp;bull;	|	&amp;#8226;	|	…	|	&amp;hellip;	|	&amp;#8230;
′	|	&amp;prime;	|	&amp;#8242;	|	″	|	&amp;Prime;	|	&amp;#8243;	|	‾	|	&amp;oline;	|	&amp;#8254;
⁄	|	&amp;frasl;	|	&amp;#8260;	|	℘	|	&amp;weierp;	|	&amp;#8472;	|	ℑ	|	&amp;image;	|	&amp;#8465;
ℜ	|	&amp;real;	|	&amp;#8476;	|	™	|	&amp;trade;	|	&amp;#8482;	|	ℵ	|	&amp;alefsym;	|	&amp;#8501;
←	|	&amp;larr;	|	&amp;#8592;	|	↑	|	&amp;uarr;	|	&amp;#8593;	|	→	|	&amp;rarr;	|	&amp;#8594;
↓	|	&amp;darr;	|	&amp;#8595;	|	↔	|	&amp;harr;	|	&amp;#8596;	|	↵	|	&amp;crarr;	|	&amp;#8629;
⇐	|	&amp;lArr;	|	&amp;#8656;	|	⇑	|	&amp;uArr;	|	&amp;#8657;	|	⇒	|	&amp;rArr;	|	&amp;#8658;
⇓	|	&amp;dArr;	|	&amp;#8659;	|	⇔	|	&amp;hArr;	|	&amp;#8660;	|	∀	|	&amp;forall;	|	&amp;#8704;
∂	|	&amp;part;	|	&amp;#8706;	|	∃	|	&amp;exist;	|	&amp;#8707;	|	∅	|	&amp;empty;	|	&amp;#8709;
∇	|	&amp;nabla;	|	&amp;#8711;	|	∈	|	&amp;isin;	|	&amp;#8712;	|	∉	|	&amp;notin;	|	&amp;#8713;
∋	|	&amp;ni;	|	&amp;#8715;	|	∏	|	&amp;prod;	|	&amp;#8719;	|	∑	|	&amp;sum;	|	&amp;#8722;
−	|	&amp;minus;	|	&amp;#8722;	|	∗	|	&amp;lowast;	|	&amp;#8727;	|	√	|	&amp;radic;	|	&amp;#8730;
∝	|	&amp;prop;	|	&amp;#8733;	|	∞	|	&amp;infin;	|	&amp;#8734;	|	∠	|	&amp;ang;	|	&amp;#8736;
∧	|	&amp;and;	|	&amp;#8869;	|	∨	|	&amp;or;	|	&amp;#8870;	|	∩	|	&amp;cap;	|	&amp;#8745;
∪	|	&amp;cup;	|	&amp;#8746;	|	∫	|	&amp;int;	|	&amp;#8747;	|	∴	|	&amp;there4;	|	&amp;#8756;
∼	|	&amp;sim;	|	&amp;#8764;	|	≅	|	&amp;cong;	|	&amp;#8773;	|	≈	|	&amp;asymp;	|	&amp;#8773;
≠	|	&amp;ne;	|	&amp;#8800;	|	≡	|	&amp;equiv;	|	&amp;#8801;	|	≤	|	&amp;le;	|	&amp;#8804;
≥	|	&amp;ge;	|	&amp;#8805;	|	⊂	|	&amp;sub;	|	&amp;#8834;	|	⊃	|	&amp;sup;	|	&amp;#8835;
⊄	|	&amp;nsub;	|	&amp;#8836;	|	⊆	|	&amp;sube;	|	&amp;#8838;	|	⊇	|	&amp;supe;	|	&amp;#8839;
⊕	|	&amp;oplus;	|	&amp;#8853;	|	⊗	|	&amp;otimes;|	&amp;#8855;	|	⊥	|	&amp;perp;	|	&amp;#8869;
⋅	|	&amp;sdot;	|	&amp;#8901;	|	⌈	|	&amp;lceil;	|	&amp;#8968;	|	⌉	|	&amp;rceil;	|	&amp;#8969;
⌊	|	&amp;lfloor;|	&amp;#8970;	|	⌋	|	&amp;rfloor;|	&amp;#8971;	|	◊	|	&amp;loz;	|	&amp;#9674;
♠	|	&amp;spades;|	&amp;#9824;	|	♣	|	&amp;clubs;	|	&amp;#9827;	|	♥	|	&amp;hearts;	|	&amp;#9829;
♦	|	&amp;diams;	|	&amp;#9830;	|	 	|	&amp;nbsp;	|	&amp;#160;	|	¡	|	&amp;iexcl;	|	&amp;#161;
¢	|	&amp;cent;	|	&amp;#162;	|	£	|	&amp;pound;	|	&amp;#163;	|	¤	|	&amp;curren;	|	&amp;#164;
¥	|	&amp;yen;	|	&amp;#165;	|	¦	|	&amp;brvbar;|	&amp;#166;	|	§	|	&amp;sect;	|	&amp;#167;
¨	|	&amp;uml;	|	&amp;#168;	|	©	|	&amp;copy;	|	&amp;#169;	|	ª	|	&amp;ordf;	|	&amp;#170;
«	|	&amp;laquo;	|	&amp;#171;	|	¬	|	&amp;not;	|	&amp;#172;	|		|	&amp;shy;	|	&amp;#173;
®	|	&amp;reg;	|	&amp;#174;	|	¯	|	&amp;macr;	|	&amp;#175;	|	°	|	&amp;deg;	|	&amp;#176;
±	|	&amp;plusmn;|	&amp;#177;	|	²	|	&amp;sup2;	|	&amp;#178;	|	³	|	&amp;sup3;	|	&amp;#179;
´	|	&amp;acute;	|	&amp;#180;	|	µ	|	&amp;micro;	|	&amp;#181;	|	"	|	&amp;quot;	|	&amp;#34;
<	|	&amp;lt;	|	&amp;#60;	|	>	|	&amp;gt;	|	&amp;#62;	|	'	|	&amp;apos;	|	&amp;#39;
&amp;	| 	&amp;amp;	|	&amp;#38;

> 要是想在HTML输出&amp;lt; 实际是`&amp;lt;`.所以`&amp;`和`&lt;`,`&gt;`,`&nbsp;`都很重要!

Python当然有办法处理这些鬼东西.  

### HTML方法

可以参考: [Escaping HTML](https://wiki.python.org/moin/EscapingHtml)

- cgi.escape : 默认只支持`& < >`. 可以使用`quote=True`参数来支持引号. 而且该模块不支持unescape..
- HTMLParser的HTMLParser类有unescape方法, 但木有escape方法..两者配合吧..使用一般`htmlp=HTMLParser.HTMLParser(); htmlp.unescape(string)`, 即先创建类. 下面的示例显示直接使用类方法来转换而不是用实例的方法.

~~~python
import cgi
cgi.escape( """& < >""" )
# "&amp; &lt; &gt;"
cgi.escape(string_to_escape, quote=True)

from HTMLParser import HTMLParser
>>> HTMLParser.unescape.__func__(HTMLParser, 'ss&copy;')
u'ss\xa9'

#### Manual define method..
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

~~~

### xml.sax.saxutils 方法 

可以参考: [PythonWiki:EscapingXml](https://wiki.python.org/moin/EscapingXml)介绍其中使用xml.sax.saxutils方法. 

- [un]escape方法默认只能处理`<&>`符号..
- quoteattr针对xml的值属性是个字符串, 此时保留其原有的`''""`. 他会智能地帮你加引号并且适当转义一些引号.
- 三种方法都支持自定义的编码转换(可以是单字符, 甚至一个字符串), 使用一个字典作第二参数. 一般建议单字符仍然参考标准.

~~~python
from xml.sax.saxutils import escape, unescape, quoteattr

### Basical usage
escape("< & >")
# '&lt; &amp; &gt;'
unescape("&lt; &amp; &gt;")
# "< & >"
quoteattr('some value containing " a double-quote')
# '\'some value containing " a double-quote\''


### Can use a dictionary for replacement
escape("abc", {"b": "&#98;"})
#'a&#98;c'
escape("My product, PyThingaMaJiggie, is really cool.",
        {"PyThingaMaJiggie": "&productName;"})
# 'My product, &productName;, is really cool.'


### Default not for ' and "
unescape("&apos; &quot;", {"&apos;": "'", "&quot;": '"'})
# '\' "'

### Both escape() and unescape() takes care of &, < and >.
html_escape_table = {
    '"': "&quot;",
    "'": "&apos;"
}
html_unescape_table = {v:k for k, v in html_escape_table.items()}

def html_escape(text):
    return escape(text, html_escape_table)

def html_unescape(text):
    return unescape(text, html_unescape_table)

~~~

> 注意: 其中的方法`from xml.sax.saxutils import escape/unescape`并不能处理特殊的`&apos;` 和 `&quot;`, 因为xml不需要其处理.



------
