---
layout: post
title: Python:元类metaclass
date: 2015-10-23 05:17:21
categories: Coding
tags: Python
archive: true
---

元类就是类的类. 实际上,我们用`class` 关键词创建的类也是一个对象也就是我们常说的类其实也是通过一个底层的类来构建的,这个类就是元类(metaclass).

## 元类和类

先看一段代码:

~~~python
class C():pass
class CC(object):pass
c=C();
cc=CC();
type(C)
# <type 'classobj'>
type(CC)
# <type 'type'>
type(c)
# <type 'instance'>
type(cc)
# <class '__main__.CC'>

print C
# __main__.C
print CC
# <class '__main__.CC'>
print c
# <__main__.C instance at 0x1096f4320>
print cc
# <__main__.CC object at 0x1096ed950>

BB=CC
bb=BB();
print bb
# <__main__.CC object at 0x1096eda10>
~~~

以上是经典的查看经典类和新型类(继承自object)信息的代码. 经典类的类叫 **classobj**, 而新式类的类叫 **type**. 经典类对象的类是熟知的**instance**, 而新式类的对象的类则是创建该类的类对象`__main__.CC`. 打印出来的效果也是,新式类才是真的类,其对象也才是真的object对象.

新式类本事其实也是一个对象, 可以用变量接收, 可以作为函数参数传递甚至返回, 可以拷贝, 可以添加新属性, 可以创造对象(类的特性). 例如上述例子用BB接收类,用BB同样可以创造CC类的对象.

新式类的类叫`type`, 这个type就是元类. 可以用元类来创建我们所熟知的新式类. 

## type函数利用元类创建新式类

我们可以使用type函数来获取类型,同样也可以用该函数创造一个类,取决于参数. `type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)`, 例如:

~~~python
CCC=type('CCC',(),{});
ccc=CCC()
print CCC
# <type 'type'>
print ccc
# <__main__.CCC object at 0x1096ed990>
~~~

这里使用type创建一个新式类, (虽然不继承任何类,但实际继承了object, 用一个变量CCC接收, 这个变量实际就是类名, 类似于上面的CC和BB.而实际类对象类型取决于type第一个参数字符串. 如果不加后面的元组和字典, type一个字符串返回的是<type 'str'>. 

例如CCCC继承自CCC并且有个方法fun,属性attr:

~~~python
def fun():pass
CCCC=type('CCCC',(CCC,),{'attr':True,'fun':fun})

class CCCC(CCC):
	self.attr=True
	self.fun=fun
~~~

实际上我们使用class关键词创建新式类时是调用了type函数来实现的.

## `__metaclass__`类属性

`__metaclass__`属性用于指明该类创建时使用的元类. 如果没有该属性,则使用type来创建. 注意, 这个过程是逐层搜的, 首先搜索该类的定义, 再搜索继承的父类, 要是还找不到就在模块里面找, 模块级别都找不到该属性, 就用type来创建. 例如上述CCCC的class式定义中,首先搜索CCCC类的定义,其次是CCC父类,再是模组(main这里), 最后才是用type. 

决定了`__metaclass__`以后, 则用其来创建一个类对象. 那么, 这个元类怎么创建类对象呢...怎么定义自己的元类呢..

## 自定义元类

首先要明确, 你要修改元类干什么. 修改元类是在创建类对象前进行拦截从而改变其特性的,用于修改类, 并且可以返回类对象. 例如,要把所有属性/方法名变成大写.

### 使用新函数并将type函数作返回

使用一个新函数, 接受和type一样对应的三个参数. 当进行相应预处理后, 再将**type()函数**将修改内容生成类对象.

该方法简单易记, 缺点是不是oop的, 并且不能使用特殊方法来处理掉该预处理时的问题!

~~~python
# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
'''返回一个类对象，将属性名都转为大写形式'''
# 选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
# 将属性名转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
# 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)
 
__metaclass__ = upper_attr  
#  这会作用到这个模块中的所有类

class Foo(object):
# 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'
print hasattr(Foo, 'bar')
# 输出: False
print hasattr(Foo, 'BAR')
# 输出:True
f = Foo()
print f.BAR
# 输出:'bip'
~~~

### 使用类的方法

使用类的方法就是要使用**type作父类**, 再覆盖`__new__`方法并返回相应的type类的`__new__`方法结果.

~~~python
class UpperAttrMetaclass(type):
# 请记住，'type'实际上是一个类，就像'str'和'int'一样, 所以，可以从type继承
    def __new__(self_class, future_class_name, future_class_parents, future_class_attr):
# __new__ 是在__init__之前被调用的特殊方法, 用来创建对象并返回之的方法
# 而__init__只是用来将传入的参数初始化给对象
# __new__()方法接收到的参数依次是：当前准备创建的类的对象; 类的名字; 类继承的父类集合; 类的方法集合。
# 一般很少用到__new__，除非你希望能够控制对象的创建
# 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
# 如果你希望的话，你也可以在__init__中做些事情
# 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
# 复用type.__new__方法, 覆盖原type的创建的方式. 比较OOP
        return type.__new__(self_class, future_class_name, future_class_parents, uppercase_attr)
# 也可以直接用type函数返回..但就和上面的函数方法类似.
        #return type(future_class_name, future_class_parents, uppercase_attr)
# 也可以不作用于type.__new__, 而是使用super函数的结果
        #return super(UpperAttrMetaclass, self_class).__new__(self_class, name, bases, uppercase_attr)
# self_class这里就是一般类的实例的self, 这里是类实例(就是一个类)

class Foo(object):
    __metaclass__=UpperAttrMetaclass #指示使用UpperAttrMetaclass来创建类.
~~~

## 典型应用: 编写ORM框架

ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

~~~python
class Field(object):
    # 负责保存数据库表的字段名和字段类型
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
# 各种类型的field
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')        

# 定义出自定义元类, 用于创建不同表(不同类)
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 基类
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        # ORM设置
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        # 不要把实例属性和类属性使用相同的名字。
        # ModelMetaclass会删除掉User类的所有类属性，目的就是避免造成混淆。
        for k in mappings.iterkeys():
            attrs.pop(k)
        # 将属于列的属性先提到mapping,保存到__mappings__中,其余用于创建类.
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)

# 基类
class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        # __mappings__属性由元类创建,对应于列.
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name) #列名
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 调用接口,使用ORM框架,这里想定义一个User类来操作对应的数据库表User
# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由基类借助元类的处理自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
~~~

## Reference

1. [深刻理解Python中的元类(metaclass)](http://blog.jobbole.com/21351/)
2. [Python Types and Objects](http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html)

> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#more-metaclass)中, 不再更新.

------
