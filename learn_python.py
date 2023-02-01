# 将 78 赋值给变量 n
n = 78
print(n)
print(type(n))
# 给x赋值一个很大的整数
x = 8888888888888888888888
print(x)
print(type(x))
# 给y赋值一个很小的整数
y = -7777777777777777777777
print(y)
print(type(y))
s2 = 'It took me six months to write this Python tutorial. \
    Please give me more support. \
    I will keep it updated.'
print(s2)
num = 20 + 3 / 4 + \
      2 * 3
print(num)

longstr = '''It took me 6 months to write this Python tutorial.
Please give me a to 'thumb' to keep it updated.
The Python tutorial is available at http://c.biancheng.net/python/.'''
print(longstr)

longstr = '''
    It took me 6 months to write this Python tutorial.
    Please give me a to 'thumb' to keep it updated.
    The Python tutorial is available at http://c.biancheng.net/python/.
'''
print(longstr)

'''
a = input("Enter a number: ")
b = input("Enter another number: ")
a = float(a)
b = float(b)
print("aType: ", type(a))
print("bType: ", type(b))
result = a + b
print("resultValue: ", result)
print("resultType: ", type(result))
'''

user_name = 'Charlie'
user_age = 8
# 同时输出多个变量和字符串
print("读者名：", user_name, "年龄：", user_age)

# 同时输出多个变量和字符串，指定分隔符
print("读者名：", user_name, "年龄：", user_age, sep='|')

f = open("demo.txt", "w")  # 打开文件以便写入
print('沧海月明珠有泪', file=f)
print('蓝田日暖玉生烟', file=f)
f.close()

'''
在 print() 函数中，由引号包围的是格式化字符串，它相当于一个字符串模板，可以放置一些转换说明符（占位符）。
本例的格式化字符串中包含一个%d说明符，它最终会被后面的 age 变量的值所替代。
中间的%是一个分隔符，它前面是格式化字符串，后面是要输出的表达式。
当然，格式化字符串中也可以包含多个转换说明符，这个时候也得提供多个表达式，用以替换对应的转换说明符；多个表达式必须使用小括号( )包围起来。
'''
name = "C语言中文网"
age = 8
url = "http://c.biancheng.net/"
print("%s已经%d岁了，它的网址是%s。" % (name, age, url))
print(type(age))

n = 1234567
print("n(10):%10d." % n)
print("n(4):%5d." % n)
url = "http://c.biancheng.net/python/"
print("url(35):%35s." % url)
print("url(20):%20s." % url)

'''
- 	指定左对齐
+ 	表示输出的数字总要带着符号；正数带+，负数带-。
0 	表示宽度不足时补充 0，而不是补充空格。
'''
f = 3.141592653
# 最小宽度为8，小数点后保留3位
print("%8.3f" % f)
# 最小宽度为8，小数点后保留3位，左边补0
print("%08.3f" % f)
# 最小宽度为8，小数点后保留3位，左边补0，带符号
print("%+08.3f" % f)

'''
转义字符 	说明
\n 	换行符，将光标位置移到下一行开头。
\r 	回车符，将光标位置移到本行开头。
\t 	水平制表符，也即 Tab 键，一般相当于四个空格。
\a 	蜂鸣器响铃。注意不是喇叭发声，现在的计算机很多都不带蜂鸣器了，所以响铃不一定有效。
\b 	退格（Backspace），将光标位置移到前一列。
\\ 	反斜线
\' 	单引号
\" 	双引号
\ 	在字符串行尾的续行符，即一行未完，转到下一行继续写。
'''
# 使用\t排版
str1 = '网站\t\t域名\t\t\t年龄\t\t价值'
str2 = 'C语言中文网\tc.biancheng.net\t\t8\t\t500W'
str3 = '百度\t\twww.baidu.com\t\t20\t\t500000W'
print(str1)
print(str2)
print(str3)
print("--------------------")
# \n在输出时换行，\在书写字符串时换行
info = "Python教程：http://c.biancheng.net/python/\n\
C++教程：http://c.biancheng.net/cplus/\n\
Linux教程：http://c.biancheng.net/linux_tutorial/"
print(info)

name = "C语言中文网"
url = "http://c.biancheng.net/"
age = 8
info = name + "的网址是" + url + "，它已经" + str(age) + "岁了。"
print(info)

#*除了可以用作乘法运算，还可以用来重复字符串，也即将 n 个同样的字符串连接起来
str1 = "hello "
print(str1 * 4)

'''
运算符 	说 明 	用法举例 	等价形式
= 	最基本的赋值运算 	x = y 	x = y
+= 	加赋值 	x += y 	x = x + y
-= 	减赋值 	x -= y 	x = x - y
*= 	乘赋值 	x *= y 	x = x * y
/= 	除赋值 	x /= y 	x = x / y
%= 	取余数赋值 	x %= y 	x = x % y
**= 	幂赋值 	x **= y 	x = x ** y
//= 	取整数赋值 	x //= y 	x = x // y
&= 	按位与赋值 	x &= y 	x = x & y
|= 	按位或赋值 	x |= y 	x = x | y
^= 	按位异或赋值 	x ^= y 	x = x ^ y
<<= 	左移赋值 	x <<= y 	x = x << y，这里的 y 指的是左移的位数
>>= 	右移赋值 	x >>= y 	x = x >> y，这里的 y 指的是右移的位数
'''
n1 = 100
f1 = 25.5
n1 -= 80  # 等价于 n1=n1-80
f1 *= n1 - 10  # 等价于 f1=f1*( n1 - 10 )
print("n1=%d" % n1)
print("f1=%.2f" % f1)

print("89是否大于100：", 89 > 100)
print("24*5是否大于等于76：", 24 * 5 >= 76)
print("86.5是否等于86.5：", 86.5 == 86.5)
print("34是否等于34.0：", 34 == 34.0)
print("False是否小于True：", False < True)
print("True是否等于True：", True == True)

#== 用来比较两个变量的值是否相等，而 is 则用来比对两个变量引用的是否是同一个对象
import time  # 引入time模块

t1 = time.gmtime()  # gmtime()用来获取当前时间
t2 = time.gmtime()
print(t1 == t2)  # 输出True
print(t1 is t2)  # 输出False
print(t1,t2)

'''
age = int(input("请输入年龄："))
height = int(input("请输入身高："))
if age >= 18 and age <= 30 and height >= 170 and height <= 185:
    print("恭喜，你符合报考飞行员的条件")
else:
    print("抱歉，你不符合报考飞行员的条件")
'''

'''
对于 and 运算符，两边的值都为真时最终结果才为真，但是只要其中有一个值为假，那么最终结果就是假，
所以 Python 按照下面的规则执行 and 运算：

    如果左边表达式的值为假，那么就不用计算右边表达式的值了，因为不管右边表达式的值是什么，都不会影响最终结果，最终结果都是假，
    此时 and 会把左边表达式的值作为最终结果。
    如果左边表达式的值为真，那么最终值是不能确定的，and 会继续计算右边表达式的值，并将右边表达式的值作为最终结果。


对于 or 运算符，情况是类似的，两边的值都为假时最终结果才为假，只要其中有一个值为真，那么最终结果就是真，
所以 Python 按照下面的规则执行 or 运算：

    如果左边表达式的值为真，那么就不用计算右边表达式的值了，因为不管右边表达式的值是什么，都不会影响最终结果，最终结果都是真，
    此时 or 会把左边表达式的值作为最终结果。
    如果左边表达式的值为假，那么最终值是不能确定的，or 会继续计算右边表达式的值，并将右边表达式的值作为最终结果。
'''

url = "http://c.biancheng.net/cplus/"
print("----False and xxx-----")
print(False and print(url))
print("----True and xxx-----")
print(True and print(url))
print("----False or xxx-----")
print(False or print(url))
print("----True or xxx-----")
print(True or print(url))

str = "C语言中文网"
print(str[0], "==", str[-6])
print(str[5], "==", str[-1])
#取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
print(str[:2])
#隔 1 个字符取一个字符，区间是整个字符串
print(str[::2])
#取整个字符串，此时 [] 中只需一个冒号即可
print(str[:])
'''
切片操作是访问序列中元素的另一种方法，它可以访问一定范围内的元素，通过切片操作，可以生成一个新的序列。

序列实现切片操作的语法格式如下：

sname[start : end : step]
其中，各个参数的含义分别是：

    sname：表示序列的名称；
    start：表示切片的开始索引位置（包括该位置），此参数也可以不指定，会默认为 0，也就是从序列的开头进行切片；
    end：表示切片的结束索引位置（不包括该位置），如果不指定，则默认为序列的长度；
    step：表示在切片过程中，隔几个存储位置（包含当前位置）取一次元素，也就是说，如果 step 的值大于 1，则在进行切片去序列元素时，会“跳跃式”的取元素。如果省略设置 step 的值，则最后一个冒号就可以省略。

'''

str = "c.biancheng.net"
print('c' in str)

str = "c.biancheng.net"
print('c' not in str)

# 将字符串转换成列表
list1 = list("hello")
print(list1)
# 将元组转换成列表
tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
list2 = list(tuple1)
print(list2)
# 将字典转换成列表
dict1 = {'a': 100, 'b': 42, 'c': 9}
list3 = list(dict1)
print(list3)
# 将区间转换成列表
range1 = range(1, 6)
list4 = list(range1)
print(list4)
# 创建空列表
print(list())

url = list("http://c.biancheng.net/shell/")
# 使用索引访问列表中的某个元素
print(url[3])  # 使用正数索引
print(url[-4])  # 使用负数索引
# 使用切片访问列表中的一组元素
print(url[9: 18])  # 使用正数切片
print(url[9: 18: 3])  # 指定步长
print(url[-6: -1])  # 使用负数切片

'''
append() 方法用于在列表的末尾追加元素，该方法的语法格式如下：

listname.append(obj)
其中，listname 表示要添加元素的列表；obj 表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等。
append() 方法传递列表或者元组时，此方法会将它们视为一个整体，作为一个元素添加到列表中，从而形成包含列表和元组的新列表。
'''
l = ['Python', 'C++', 'Java']
# 追加元素
l.append('PHP')
print(l)
# 追加元组，整个元组被当成一个元素
t = ('JavaScript', 'C#', 'Go')
l.append(t)
print(l)
# 追加列表，整个列表也被当成一个元素
l.append(['Ruby', 'SQL'])
print(l)

'''
extend() 和 append() 的不同之处在于：extend() 不会把列表或者元祖视为一个整体，而是把它们包含的元素逐个添加到列表中。

extend() 方法的语法格式如下：

listname.extend(obj)
其中，listname 指的是要添加元素的列表；obj 表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等，但不能是单个的数字。
'''
l = ['Python', 'C++', 'Java']
# 追加元素
l.extend('C')
print(l)
# 追加元组，元祖被拆分成多个元素
t = ('JavaScript', 'C#', 'Go')
l.extend(t)
print(l)
# 追加列表，列表也被拆分成多个元素
l.extend(['Ruby', 'SQL'])
print(l)

'''
append() 和 extend() 方法只能在列表末尾插入元素，如果希望在列表中间某个位置插入元素，那么可以使用 insert() 方法。

insert() 的语法格式如下：

listname.insert(index , obj)
其中，index 表示指定位置的索引值。insert() 会将 obj 插入到 listname 列表第 index 个元素的位置。

当插入列表或者元祖时，insert() 也会将它们视为一个整体，作为一个元素插入到列表中，这一点和 append() 是一样的。
'''
l = ['Python', 'C++', 'Java']
# 插入元素
l.insert(1, 'C')
print(l)
# 插入元组，整个元祖被当成一个元素
t = ('C#', 'Go')
l.insert(2, t)
print(l)
# 插入列表，整个列表被当成一个元素
l.insert(3, ['Ruby', 'SQL'])
print(l)
# 插入字符串，整个字符串被当成一个元素
l.insert(0, "http://c.biancheng.net")
print(l)

lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
del lang[1: 4]
print(lang)
lang.extend(["SQL", "C#", "Go"])
print(lang)
del lang[-5: -2]
print(lang)

'''
除了 del 关键字，Python 还提供了remove() 方法，该方法会根据元素本身的值来进行删除操作。

需要注意的是，remove() 方法只会删除第一个和指定值相同的元素，而且必须保证该元素是存在的，否则会引发 ValueError 错误。
'''
nums = [40, 36, 89, 2, 36, 100, 7]
# 第一次删除36
nums.remove(36)
print(nums)
# 第二次删除36
nums.remove(36)
print(nums)

#Python clear() 用来删除列表的所有元素，也即清空列表
url = list("http://c.biancheng.net/python/")
url.clear()
print(url)

nums = [40, 36, 89, 2, 36, 100, 7]
nums[2] = -26  # 使用正数索引
nums[-3] = -66.2  # 使用负数索引
print(nums)

nums = [40, 36, 89, 2, 36, 100, 7]
# 修改第 1~4 个元素的值（不包括第4个元素）
nums[1: 4] = [45.25, -77, -52.5]
print(nums)
nums = [40, 36, 89, 2, 36, 100, 7]
# 在4个位置插入元素
nums[4: 4] = [-77, -52.5, 999]
print(nums)

'''
使用切片语法赋值时，Python 不支持单个值
如果使用字符串赋值，Python 会自动把字符串转换成序列，其中的每个字符都是一个元素
'''
s = list("Hello")
s[2:4] = "XYZ"
print(s)

#使用切片语法时也可以指定步长（step 参数），但这个时候就要求所赋值的新元素的个数与原有元素的个数相同
nums = [40, 36, 89, 2, 36, 100, 7]
# 步长为2，为第1、3、5个元素赋值
nums[1: 6: 2] = [0.025, -99, 20.5]
print(nums)

'''
index() 的语法格式为：

listname.index(obj, start, end)
其中，listname 表示列表名称，obj 表示要查找的元素，start 表示起始位置，end 表示结束位置。

start 和 end 参数用来指定检索范围：

    start 和 end 可以都不写，此时会检索整个列表；
    如果只写 start 不写 end，那么表示检索从 start 到末尾的元素；
    如果 start 和 end 都写，那么表示检索 start 和 end 之间的元素。


index() 方法会返回元素所在列表中的索引值。
'''
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
# 检索列表中的所有元素
print(nums.index(2))
# 检索3~7之间的元素
print(nums.index(100, 3, 7))
# 检索4之后的元素
print(nums.index(7, 4))
# 检索一个不存在的元素
#print(nums.index(55))

'''
count() 方法用来统计某个元素在列表中出现的次数，基本语法格式为：

listname.count(obj)
其中，listname 代表列表名，obj 表示要统计的元素。

如果 count() 返回 0，就表示列表中不存在该元素，所以 count() 也可以用来判断列表中的某个元素是否存在。
'''
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, 36]
# 统计元素出现的次数
print("36出现了%d次" % nums.count(36))
# 判断一个元素是否存在
if nums.count(100):
    print("列表中存在100这个元素")
else:
    print("列表中不存在100这个元素")

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号,，否则 Python 解释器会将它视为字符串。
# 最后加上逗号
a = ("http://c.biancheng.net/cplus/",)
print(type(a))
print(a)
# 最后不加逗号
b = ("http://c.biancheng.net/socket/")
print(type(b))
print(b)

# 将字符串转换成元组
tup1 = tuple("hello")
print(tup1)
# 将列表转换成元组
list1 = ['Python', 'Java', 'C++', 'JavaScript']
tup2 = tuple(list1)
print(tup2)
# 将字典转换成元组
dict1 = {'a': 100, 'b': 42, 'c': 9}
tup3 = tuple(dict1)
print(tup3)
# 将区间转换成元组
range1 = range(1, 6)
tup4 = tuple(range1)
print(tup4)
# 创建空元组
print(tuple())

'''
通过键而不是通过索引来读取元素 	字典类型有时也称为关联数组或者散列表（hash）。
它是通过键将一系列的值联系起来的，这样就可以通过键从字典中获取指定项，但不能通过索引来获取。
字典是任意数据类型的无序集合 	和列表、元组不同，通常会将索引值 0 对应的元素称为第一个元素，而字典中的元素是无序的。
字典是可变的，并且可以任意嵌套 	字典可以在原处增长或者缩短（无需生成一个副本），
并且它支持任意深度的嵌套，即字典存储的值也可以是列表或其它的字典。
字典中的键必须唯一 	字典中，不支持同一个键出现多次，否则只会保留最后一个键值对。
字典中的键必须不可变 	字典中每个键值对的键是不可变的，只能使用数字、字符串或者元组，不能使用列表。
'''

'''
由于字典中每个元素都包含两部分，分别是键（key）和值（value），因此在创建字典时，键和值之间使用冒号:分隔，
相邻元素之间使用逗号,分隔，所有元素放在大括号{ }中。

使用{ }创建字典的语法格式如下：

dictname = {'key':'value1', 'key2':'value2', ..., 'keyn':valuen}
其中 dictname 表示字典变量名，keyn : valuen 表示各个元素的键值对。需要注意的是，同一字典中的各个键必须唯一，不能重复。
'''
# 使用字符串作为key
scores = {'数学': 95, '英语': 92, '语文': 84}
print(scores)
# 使用元组和数字作为key
dict1 = {(20, 30): 'great', 30: [1, 2, 3]}
print(dict1)
# 创建空元组
dict2 = {}
print(dict2)

'''
Python 中，还可以使用 dict 字典类型提供的 fromkeys() 方法创建带有默认值的字典，具体格式为：

dictname = dict.fromkeys(list，value=None)
其中，list 参数表示字典中所有键的列表（list）；value 参数表示默认值，如果不写，则为空值 None。
knowledge 列表中的元素全部作为了 scores 字典的键，而各个键对应的值都是 60。这种创建方式通常用于初始化字典，设置 value 的默认值。
'''
knowledge = ['语文', '数学', '英语']
scores = dict.fromkeys(knowledge, 60)
print(scores)
print(scores['语文'])

'''
get() 方法的语法格式为：
dictname.get(key[,default])
其中，dictname 表示字典变量的名字；key 表示指定的键；default 用于指定要查询的键不存在时，此方法返回的默认值，如果不手动指定，会返回 None。
'''
a = dict(two=0.65, one=88, three=100, four=-59)
print(a)
print(a.get('one', '该键不存在'))
print(a.get('five', '该键不存在'))

a = {'数学': 95}
print(a)
# 添加新键值对
a['语文'] = 89
print(a)
# 再次添加新键值对
a['英语'] = 90
print(a)

a = {'数学': 95, '语文': 89, '英语': 90}
b = list(a.keys())
print(b)
c = list(a.values())
print(c)

set1 = set("c.biancheng.net")
set2 = set([1, 2, 3, 4, 5])
set3 = set((1, 2, 3, 4, 5))
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)

str = "I LIKE C"
print(str.lower())

str = "网站名称：{:>9s}\t网址：{:s}"
print(str.format("C语言中文网", "c.biancheng.net"))

add = "http://c.biancheng.net/python/"
# for循环，遍历 add 字符串
for ch in add:
    print(ch, end="")

