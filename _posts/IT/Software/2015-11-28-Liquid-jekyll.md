---
layout: post_toc
title: Liquid语言(jekyll所需)
date: 2015-11-28 09:37:35
categories: IT
tags: Software Git
---

<link rel="stylesheet" href="/jcss/css/pygments_monokai.css">

{% raw %}
Liquid语言是一种标记语言, 将模板转化为相应的代码从而进行相关的"编译". 被广泛用于多种工具中, 最为著名就是Github的Jekyll静态网页生成系统. Liquid使用Ruby编写而成.

Liquid语言有两大类标记: 一种是结果型(Output), 一种是语句型, 前者进行输出为text, 后者主要进行语句相关操作,如if, for等.  

Output型使用{{ output }} 进行, 而Tag型则采用 {% tag %}. 

## Output型

一种**直接输出**, 例如变量. {{ var }}  
一种是**过滤器**, 采用: {{ var | filter1 |filter2 }}形式, filter相当于一个处理函数, 对变量进行操作并返回新值. 新值用于下一个过滤器或者用于直接输出为结果. 过滤器可以见下面[介绍](#advanced-output-filters). jekyll有额外的过滤器参考[模板部分](http://jekyllrb.com/docs/templates/).

## Tag型 

说白了就是一般的语句, 包括If/Unless/Case判断, For/Loop循环等. 写完Tag后一般需要有后续的EndTagname. 如: {% if %} {% endif %}. 一些例子用法参考[后面的介绍](#tags).

先说一下, Liquid支持 `and`, `or`, `!=`, `==`, `contains` (包含), `true`, `false`.

### 常用tag包括:

- {% `assign` var=value %} 赋值语句. 没有end.
- {% `capture` var %} context {% endcapture %} 将中间的内容赋值给变量. 因此可以不是简单的值而是获取变量经操作后再赋值.更强大.
- {% `if` condition %}, {% `elsif` condition %}, {% `else` %}, {% `endif` %} 系列. 支持and, or, 不支持not. if not使用 {% `unless` condition %} .. {% `endunless` %}进行. 注意是 **elsif** 而不是elseif.
- {% `case` var %}, {% `when` value %}, {% `else` %}, {% `endcase` %} 系列, 多种条件选择.
- {% `for` var `in` array %}, {% `else` %}, {% `endfor` %} 循环, 后面可以跟一些修饰符 `parameter:value` 进一步控制. else可用于数组为空时的情况. 另外也支持 {% `break` %}和{% `continue` %}打断虚幻.
- {% `cycle` [groupname:] val1, val2, .. %} 循环逐个列出指定内容. 注意没有end. 每调用一次就会列出下个值. groupname是列的时候区分组的, 默认不加列名就是只有一个组.
- {% `comment` %} .. {% `endcomment` %} , Liquid注释(不是HTML注释), 不解释也不显示.
- {% `raw` %} ... {% `endraw` %}, 不作为Liquid解释, 会作为源码显示. 例如本文上边文字部分由该对tag包围. **很重要!**
- {% `include` filename %}, 将另一个文件作为模板片段插入.

新建tag可以使用Ruby进行, 参考最后for programmer的部分.

### 在Jekyll里还包括:

- {% `include_relative` filename %} 以当前文件所在目录来定位文件进行插入. {% include %}的包含则在`_includes`文件夹内.
- {% `highlight` lang linenos %} {% `endhighlight` %} Rouge或Pygments语法高亮. lang对应相应编程语言, 如vb.net(更多参考:[Rouge](http://rouge.jneen.net/)与[支持语言](https://github.com/jneen/rouge/wiki/List-of-supported-languages-and-lexers), [Pygments](http://pygments.org)与[支持语言](http://pygments.org/languages/))linenos是打开行号显示, 非必要.
- {% `post_url` /subdir/2010-07-21-name-of-post %} 可以将_posts里的blog文件名转化为相应url. 注意地址, 注意没有后缀.
- {% `gist` user/gistID filename %} 插入Gist内容. user和gistID对应在Gist的网址里.文件名可用于指定gist中某文件(非必要选项). 需要额外安装[jekyll-gist](https://github.com/jekyll/jekyll-gist)插件, 建议直接使用gist的embed功能.

{% endraw %}

----

if tab实例 (用的highlight的tag, 先包裹raw的tag去liquid解析, 再包含代码):

{% highlight Liquid linenos%}
{% raw s%}
{% if user.name == 'tobi' %}
  Hello tobi
{% elsif user.name == 'bob' %}
  Hello bob
{% endif %}
{% endraw %}
{% endhighlight %}

{% raw %}

--------

# Liquid Home

Liquid is a template engine which was crafted for very specific requirements

* It has to have simple markup and beautiful results. Template engines which
  don't produce good looking results are no fun to use.
* It needs to be non-evaling and secure. Liquid templates are made so that users
  can edit them. You don't want your server running code that your users
  wrote.
* It has to be stateless. The compile and render steps have to be separate, so
  that the expensive parsing and compiling can be done once;  later on, you can
  just render it by passing in a hash with local variables and objects.
* It needs to be able to style emails as well as HTML.

## Stuff to read, watch, etc.

* [Class reference](http://rubydoc.info/gems/liquid)
* [Liquid for Programmers](#file-liquid-programmer-md)
* [Liquid for Designers](#file-liquid-designer-md)
* [Liquid screencast](http://railscasts.com/episodes/118-liquid)
* Ports of Liquid to other environments:
  * [liquid.js](https://github.com/darthapo/liquid.js) (JavaScript)
  * [DotLiquid](http://dotliquidmarkup.org/) (C#)
  * [php-liquid](https://github.com/harrydeluxe/php-liquid) (PHP)
  * [Template::Liquid](https://metacpan.org/pod/Template::Liquid) (Perl)
  * [CFML-LIQUID](https://github.com/rip747/cfml-liquid) (CFML/ColdFusion)
  * [liquid.as](https://github.com/prevailhs/liquid.as) (ActionScript 3)
  * [Liqp](https://github.com/bkiers/Liqp) (Java)
  * [Liquid](https://github.com/karlseguin/liquid) (Go)
  * [Liquid.NET](https://github.com/mikebridge/Liquid.NET) (C#)

## Who uses Liquid?

* [Shopify](http://www.shopify.com)
* [eLocal](http://www.elocal.com)
* [Mephisto](http://mephistoblog.com/)
* [Harmony](http://get.harmonyapp.com)
* [Chameleon](http://chameleon.wikidot.com/)
* [Cashboard](http://www.getcashboard.com)
* [Adobe Business Catalyst](http://businesscatalyst.com/)
* [Voog](http://www.voog.com)
* [Zendesk](http://www.zendesk.com)
* [YikeSite (CMS)](http://api.yikesite.com/)
* [Simplicant (Applicant Tracking System)](http://www.simplicant.com/)
* [3scale (API Management System)](http://www.3scale.net/)
* [Chaptercore](http://www.chaptercore.com)
* [ScreenSteps Live](http://bluemangolearning.com/screenstepslive)
* [PokerAffiliateSolutions](http://www.pokeraffiliatesolutions.com/)
* [Desk.com](http://www.desk.com)
* [Ronin](http://www.roninapp.com)
* [AboutOne](http://www.aboutone.com)
* [RightScale](http://support.rightscale.com/15-References/Liquid_Markup_with_RightScale_Widgets)
* [Menumill](http://www.menumill.com)
* [Moxie Software](http://www.moxiesoft.com/)
* [Rusic](http://rusic.com/)
* [Development Seed](http://developmentseed.org/blog/2011/09/09/jekyll-github-pages/)
* [peerTransfer](http://peertransfer.com)
* [NationBuilder](http://nationbuilder.com/)
* [Pronto Avenue](http://www.prontoavenue.biz)
* [Device Magic](http://www.devicemagic.com)
* [Spiceworks](http://www.spiceworks.com)
* [PufferPages (CMS)](https://github.com/puffer/puffer_pages/)
* [Displet](http://displet.com)
* [Paspartout](http://paspartout.com)
* [TrackGrid](http://www.trackgrid.com)
* [Jekyll](http://jekyllrb.com/)
* [Octopress](http://octopress.org/)
* [Vnda](http://www.vnda.com.br/)
* [LeadFormance](http://www.leadformance.com/)
* [23 Video](http://www.23video.com/)
* [CrystalCommerce](http://www.crystalcommerce.com/)
* [Rackspace](http://www.rackspace.com/)
* [Talent Technology](http://www.talenttech.com)
* [WebKite](http://webkite.com/)
* [Adam Ralph](http://adamralph.com/)
* [Quaderno](http://getquaderno.com/)
* [LocomotiveCMS](http://locomotivecms.com/)
* [Customer.io](http://customer.io)
* [Mixture.io](http://mixture.io)
* [MakePlans](http://makeplans.net)
* [Planning Center Services](http://get.planningcenteronline.com)
* [Planning Center Resources](http://get.planningcenteronline.com/resources)
* [RoQua](http://www.roqua.nl)
* [Evrone](http://www.evrone.com)
* [Liquid.as](https://github.com/prevailhs/liquid.as)
* [Open Liquid](https://github.com/23/openliquid)
* [500px](http://portfolios.500px.com)
* [VTEX](http://www.vtex.com.br/)
* [Xorcode](http://www.xorcode.com/)
* [MobiCheckin (registration forms)](http://www.mobicheckin.com)
* [Educative-Games.org](http://educative-games.org)
* [GiftFold](http://giftfold.com)
* [Reamaze](http://www.reamaze.com)
* [Sitebox.io](http://www.sitebox.io)
* [Stunning](https://bestunning.net)
* [Vero (Email Marketing Software)](https://www.getvero.com)
* [GoDaddy](https://www.godaddy.com)
* [SendOwl](http://www.sendowl.com)
* [FOX21.at](http://blog.fox21.at)
* [Bright Sites](http://www.brightsites.com)
* [Mode Analytics](http://www.modeanalytics.com)
* [Helpjuice](https://www.helpjuice.com)
* [Freshdesk](http://freshdesk.com)
* [Continuity Control](http://www.continuity.net)
* [Mitingu](http://www.mitingu.com)
* [Festiment](http://www.festiment.com)
* [Unsound Music Festival](http://www.unsound.pl)
* [Expertory](http://www.expertory.com)
* [Appboy](https://www.appboy.com)
* [Disco](http://discolabs.com)
* [LavoWeb](http://lavoweb.net)
* [DediConcept](http://www.dediconcept.com)
* [Lucid](http://www.lucid.co.nz/)
* [Fedora](http://usefedora.com/)
* [Jumpseller](https://jumpseller.com/)
* [Openbay](https://www.openbay.com)
* [Sayan's Blog](http://sayan98.github.io/blog)
* [Industry Mailout](https://industrymailout.com/)
* [Near Me Marketplaces](https://near-me.com/)
* [Growing with the Web](http://www.growingwiththeweb.com/)
* [Mercury Flight](http://www.mercuryflight.com/)
* [Drip](https://www.getdrip.com/)
* [Sixty AS](http://www.sixty.no/)
* [Thinkific](http://www.thinkific.com/)
* [dotmailer](https://www.dotmailer.com/)
* [meowbox](https://meowbox.com/)
* [Embulk](http://embulk.org)
* ...Add yours :)

## Why should I use Liquid?

* You want to allow your users to edit the appearance of your application, but
  don't want them to run insecure code on your server.
* You want to render templates directly from the database.
* You like Smarty-style template engines.
* You need a template engine which does HTML just as well as emails.
* You don't like the markup language of your current template engine.

--------

# Liquid for designer {#file-liquid-designer-md}
There are two types of markup in Liquid: Output and Tag.

* Output markup (which may resolve to text) is surrounded by

{% endraw %}
{% highlight Liquid %}
{% raw %}
{{ matched pairs of curly brackets (ie, braces) }}
{% endraw %}
{% endhighlight %}
{% raw %}

* Tag markup (which cannot resolve to text) is surrounded by

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% matched pairs of curly brackets and percent signs %}
{% endraw %}
{% endhighlight %}
{% raw %}

## Output

Here is a simple example of Output:

{% endraw %}
{% highlight Liquid %}
{% raw %}
Hello {{name}}
Hello {{user.name}}
Hello {{ 'tobi' }}
{% endraw %}
{% endhighlight %}
{% raw %}

<a name="filters"></a>

### Advanced output: Filters

Output markup takes filters.  Filters are simple methods.  The first parameter
is always the output of the left side of the filter.  The return value of the
filter will be the new left value when the next filter is run.  When there are
no more filters, the template will receive the resulting string.

{% endraw %}
{% highlight Liquid %}
{% raw %}
Hello {{ 'tobi' | upcase }}
Hello tobi has {{ 'tobi' | size }} letters!
Hello {{ '*tobi*' | textilize | upcase }}
Hello {{ 'now' | date: "%Y %h" }}
{% endraw %}
{% endhighlight %}
{% raw %}

### Standard Filters

* `date` - reformat a date ([syntax reference](http://docs.shopify.com/themes/liquid-documentation/filters/additional-filters#date))
* `capitalize` - capitalize words in the input sentence
* `downcase` - convert an input string to lowercase
* `upcase` - convert an input string to uppercase
* `first` - get the first element of the passed in array
* `last` - get the last element of the passed in array
* `join` - join elements of the array with certain character between them
* `sort` - sort elements of the array
* `map` - map/collect an array on a given property
* `size` - return the size of an array or string
* `escape` - escape a string
* `escape_once` - returns an escaped version of html without affecting existing escaped entities
* `strip_html` - strip html from string
* `strip_newlines` - strip all newlines (\n) from string
* `newline_to_br` - replace each newline (\n) with html break
* `replace` - replace each occurrence *e.g.* `{{ 'foofoo' | replace:'foo','bar' }} #=> 'barbar'`
* `replace_first` - replace the first occurrence *e.g.* `{{ 'barbar' | replace_first:'bar','foo' }} #=> 'foobar'`
* `remove` - remove each occurrence *e.g.* `{{ 'foobarfoobar' | remove:'foo' }} #=> 'barbar'`
* `remove_first` - remove the first occurrence *e.g.* `{{ 'barbar' | remove_first:'bar' }} #=> 'bar'`
* `truncate` - truncate a string down to x characters. It also accepts a second parameter that will append to the string *e.g.* `{{ 'foobarfoobar' | truncate: 5, '.' }} #=> 'foob.'`
* `truncatewords` - truncate a string down to x words
* `prepend` - prepend a string *e.g.* `{{ 'bar' | prepend:'foo' }} #=> 'foobar'`
* `pluralize` - return the second word if the input is not `1`, otherwise return the first word *e.g.* `{{ 3 | pluralize: 'item', 'items' }} #=> 'items'`
* `append` - append a string *e.g.* `{{ 'foo' | append:'bar' }} #=> 'foobar'`
* `slice` - slice a string. Takes an offset and length, *e.g.* `{{ "hello" | slice: -3, 3 }} #=> llo`
* `minus` - subtraction *e.g.*  `{{ 4 | minus:2 }} #=> 2`
* `plus` - addition *e.g.*  `{{ '1' | plus:'1' }} #=> 2`, `{{ 1 | plus:1 }} #=> 2`
* `times` - multiplication  *e.g* `{{ 5 | times:4 }} #=> 20`
* `divided_by` - integer division *e.g.* `{{ 10 | divided_by:3 }} #=> 3`
* `round` - rounds input to the nearest integer or specified number of decimals
* `split` - split a string on a matching pattern *e.g.* `{{ "a~b" | split:"~" }} #=> ['a','b']`
* `modulo` - remainder, *e.g.* `{{ 3 | modulo:2 }} #=> 1`

## Tags

Tags are used for the logic in your template. New tags are very easy to code,
so I hope to get many contributions to the standard tag library after releasing
this code.

Here is a list of currently supported tags:

* **assign** - Assigns some value to a variable
* **capture** - Block tag that captures text into a variable
* **case** - Block tag, its the standard case...when block
* **comment** - Block tag, comments out the text in the block
* **cycle** - Cycle is usually used within a loop to alternate between values, like colors or DOM classes.
* **for** - For loop
* **break** - Exits a for loop
* **continue** Skips the remaining code in the current for loop and continues with the next loop
* **if** - Standard if/else block
* **include** - Includes another template; useful for partials
* **raw** - temporarily disable tag processing to avoid syntax conflicts.
* **unless** - Mirror of if statement

### Comments

Any content that you put between `{% comment %}` and `{% endcomment %}` tags is turned into a comment. 

{% endraw %}
{% highlight Liquid %}
{% raw %}
We made 1 million dollars {% comment %} in losses {% endcomment %} this year
{% endraw %}
{% endhighlight %}
{% raw %}

### Raw

Raw temporarily disables tag processing.
This is useful for generating content (eg, Mustache, Handlebars) which uses conflicting syntax.

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% raw %}
  In Handlebars, {{ this }} will be HTML-escaped, but {{{ that }}} will not.
\{\% endraw \%\}
{% endraw %}
{% endhighlight %}
{% raw %}

### If / Else

`if / else` should be well-known from any other programming language.
Liquid allows you to write simple expressions in the `if` or `unless` (and
optionally, `elsif` and `else`) clause:

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% if user %}
  Hello {{ user.name }}
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
# Same as above
{% if user != null %}
  Hello {{ user.name }}
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% if user.name == 'tobi' %}
  Hello tobi
{% elsif user.name == 'bob' %}
  Hello bob
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% if user.name == 'tobi' or user.name == 'bob' %}
  Hello tobi or bob
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% if user.name == 'bob' and user.age > 45 %}
  Hello old bob
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% if user.name != 'tobi' %}
  Hello non-tobi
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
# Same as above
{% unless user.name == 'tobi' %}
  Hello non-tobi
{% endunless %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
# Check for the size of an array
{% if user.payments == empty %}
   you never paid !
{% endif %}

{% if user.payments.size > 0  %}
   you paid !
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% if user.age > 18 %}
   Login here
{% else %}
   Sorry, you are too young
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
# array = 1,2,3
{% if array contains 2 %}
   array includes 2
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

{% endraw %}
{% highlight Liquid %}
{% raw %}
# string = 'hello world'
{% if string contains 'hello' %}
   string includes 'hello'
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

### Case Statement

If you need more conditions, you can use the `case` statement:

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% case condition %}
{% when 1 %}
hit 1
{% when 2 or 3 %}
hit 2 or 3
{% else %}
... else ...
{% endcase %}
{% endraw %}
{% endhighlight %}
{% raw %}

*Example:*

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% case template %}

{% when 'label' %}
     // {{ label.title }}
{% when 'product' %}
     // {{ product.vendor | link_to_vendor }} / {{ product.title }}
{% else %}
     // {{page_title}}
{% endcase %}
{% endraw %}
{% endhighlight %}
{% raw %}

### Cycle

Often you have to alternate between different colors or similar tasks.  Liquid
has built-in support for such operations, using the `cycle` tag.

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% cycle 'one', 'two', 'three' %}
{% cycle 'one', 'two', 'three' %}
{% cycle 'one', 'two', 'three' %}
{% cycle 'one', 'two', 'three' %}
{% endraw %}
{% endhighlight %}
{% raw %}

will result in

~~~
one
two
three
one
~~~

If no name is supplied for the cycle group, then it's assumed that multiple
calls with the same parameters are one group.

If you want to have total control over cycle groups, you can optionally specify
the name of the group.  This can even be a variable.

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% cycle 'group 1': 'one', 'two', 'three' %}
{% cycle 'group 1': 'one', 'two', 'three' %}
{% cycle 'group 2': 'one', 'two', 'three' %}
{% cycle 'group 2': 'one', 'two', 'three' %}
{% endraw %}
{% endhighlight %}
{% raw %}

will result in

~~~
one
two
one
two
~~~

### For loops

Liquid allows `for` loops over collections:

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% for item in array %}
  {{ item }}
{% endfor %}
{% endraw %}
{% endhighlight %}
{% raw %}

When iterating a hash, `item[0]` contains the key, and `item[1]` contains the value:

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% for item in hash %}
  {{ item[0] }}: {{ item[1] }}
{% endfor %}
{% endraw %}
{% endhighlight %}
{% raw %}

During every `for` loop, the following helper variables are available for extra
styling needs:

{% endraw %}
{% highlight Liquid %}
{% raw %}
forloop.length      # => length of the entire for loop
forloop.index       # => index of the current iteration
forloop.index0      # => index of the current iteration (zero based)
forloop.rindex      # => how many items are still left?
forloop.rindex0     # => how many items are still left? (zero based)
forloop.first       # => is this the first iteration?
forloop.last        # => is this the last iteration?
{% endraw %}
{% endhighlight %}
{% raw %}

There are several attributes you can use to influence which items you receive in
your loop

`limit:int` lets you restrict how many items you get.
`offset:int` lets you start the collection with the nth item.

{% endraw %}
{% highlight Liquid %}
{% raw %}
# array = [1,2,3,4,5,6]
{% for item in array limit:2 offset:2 %}
  {{ item }}
{% endfor %}
# results in 3,4
{% endraw %}
{% endhighlight %}
{% raw %}

Reversing the loop

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% for item in collection reversed %} {{item}} {% endfor %}
{% endraw %}
{% endhighlight %}
{% raw %}

Instead of looping over an existing collection, you can define a range of
numbers to loop through.  The range can be defined by both literal and variable
numbers:

{% endraw %}
{% highlight Liquid %}
{% raw %}
# if item.quantity is 4...
{% for i in (1..item.quantity) %}
  {{ i }}
{% endfor %}
# results in 1,2,3,4
{% endraw %}
{% endhighlight %}
{% raw %}

A for loop can take an optional `else` clause to display a block of text when there are no items in the collection:

{% endraw %}
{% highlight Liquid %}
{% raw %}
    # items => []
    {% for item in items %}
       {{ item.title }}
    {% else %}
       There are no items!
    {% endfor %}
{% endraw %}
{% endhighlight %}
{% raw %}

### Variable Assignment

You can store data in your own variables, to be used in output or other tags as
desired.  The simplest way to create a variable is with the `assign` tag, which
has a pretty straightforward syntax:

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% assign name = 'freestyle' %}

{% for t in collections.tags %}{% if t == name %}
  <p>Freestyle!</p>
{% endif %}{% endfor %}
{% endraw %}
{% endhighlight %}
{% raw %}

Another way of doing this would be to assign `true / false` values to the
variable:

{% endraw %}
{% highlight Liquid %}
{% raw %}
{% assign freestyle = false %}

{% for t in collections.tags %}{% if t == 'freestyle' %}
  {% assign freestyle = true %}
{% endif %}{% endfor %}

{% if freestyle %}
  <p>Freestyle!</p>
{% endif %}
{% endraw %}
{% endhighlight %}
{% raw %}

If you want to combine a number of strings into a single string and save it to
a variable, you can do that with the `capture` tag. This tag is a block which
"captures" whatever is rendered inside it, then assigns the captured value to
the given variable instead of rendering it to the screen.

{% endraw %}
{% highlight Liquid %}
{% raw %}
  {% capture attribute_name %}{{ item.title | handleize }}-{{ i }}-color{% endcapture %}

  <label for="{{ attribute_name }}">Color:</label>
  <select name="attributes[{{ attribute_name }}]" id="{{ attribute_name }}">
    <option value="red">Red</option>
    <option value="green">Green</option>
    <option value="blue">Blue</option>
  </select>
{% endraw %}
{% endhighlight %}
{% raw %}


# Liquid for programmer {#file-liquid-programmer-md}

## First steps

It's very simple to get started with Liquid.  A Liquid template is rendered in
two steps: Parse and Render.  For an overview of the Liquid syntax, please read
[Liquid for Designers](#file-liquid-designer-md).

~~~ruby
@template = Liquid::Template.parse("hi {{name}}")  # Parses and compiles the template
@template.render( 'name' => 'tobi' )               # Renders the output => "hi tobi"
~~~

The `parse` step creates a fully compiled template which can be re-used as often
as you like.  You can store it in memory or in a cache for faster rendering
later.

All parameters you want Liquid to work with have to be passed as parameters to
the `render` method.  Liquid does not know about your Ruby local, instance, and
global variables.

## Extending Liquid

Extending Liquid is very easy.  However, keep in mind that Liquid is a young
library and requires some outside help.  If you create useful filters and tags,
please consider making a [pull request](https://github.com/Shopify/liquid/pulls)
with them.

### Create your own filters

Creating filters is very easy.  Basically, they are just methods which take one
parameter and return a modified string.  You can use your own filters by passing
an array of modules to the render call like this: `@template.render(assigns,
[MyTextFilters, MyDateFilters])`.

~~~ruby
module TextFilter
  def textilize(input)
    RedCloth.new(input).to_html
  end
end
~~~

~~~ruby
@template = Liquid::Template.parse(" {{ '*hi*' | textilize }} ")
@template.render({}, :filters => [TextFilter])              # => "<strong>hi</strong>"
~~~

Alternatively, you can register your filters globally:

~~~ruby
module TextFilter
  def textilize(input)
    RedCloth.new(input).to_html
  end
end

Liquid::Template.register_filter(TextFilter)
~~~

Once the filter is globally registered, you can simply use it:

~~~ruby
@template = Liquid::Template.parse(" {{ '*hi*' | textilize }} ")
@template.render              # => "<b>hi</b>"
~~~

### Create your own tags

To create a new tag, simply inherit from `Liquid::Tag` and register your block
with `Liquid::Template`.

~~~ruby
class Random < Liquid::Tag
  def initialize(tag_name, max, tokens)
     super
     @max = max.to_i
  end

  def render(context)
    rand(@max).to_s
  end
end

Liquid::Template.register_tag('random', Random)
~~~

~~~ruby
@template = Liquid::Template.parse(" {% random 5 %}")
@template.render    # => "3"
~~~

### Create your own tag blocks

All tag blocks are parsed by Liquid.  To create a new block, you just have to
inherit from `Liquid::Block` and register your block with `Liquid::Template`.

~~~ruby
class Random < Liquid::Block
  def initialize(tag_name, markup, tokens)
     super
     @rand = markup.to_i
  end

  def render(context)
    value = rand(@rand)
    super.sub('^^^', value.to_s)  # calling `super` returns the content of the block
  end
end

Liquid::Template.register_tag('random', Random)
~~~

~~~ruby
text = " {% random 5 %} you have drawn number ^^^, lucky you! {% endrandom %} "
@template = Liquid::Template.parse(text)
@template.render  # will return "you have drawn number 1, lucky you!" in 20% of cases
~~~

## Caching of classes

If you get errors like `A copy of ... has been removed from the module tree but is still active!` it's probably because Liquid is caching your classes in development mode, the solution is to disable it in test and development modes:

~~~ruby
# in config/environments/development.rb and config/environments/test.rb
Liquid.cache_classes = false
~~~

{% endraw %}




# Reference

1. [Liquid-Github](https://github.com/Shopify/liquid), [Github-Liquid-wiki](https://github.com/Shopify/liquid/wiki)
2. [Jekyll-Template](http://jekyllrb.com/docs/templates/), [Jekyll-Plugins](http://jekyllrb.com/docs/plugins/)
3. [shopify中的Liquid介绍](https://docs.shopify.com/themes/liquid-documentation/basics)

------
