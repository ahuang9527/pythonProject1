class CLanguage:
    # 下面定义了2个类变量
    name1 = "C语言中文网"
    add1 = "http://c.biancheng.net"

    def __init__(self, name, add):
        # 下面定义 2 个实例变量
        self.name = name
        self.add = add
        print(name, "网址为：", add)

    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)


# 将该CLanguage对象赋给clanguage变量
clanguage = CLanguage("中文网", "http://c.biancheng.net")
clanguage2 = CLanguage("1", "2")
# 输出name和add实例变量的值
print(clanguage.name, clanguage.add)
print(CLanguage.name1)
# 修改实例变量的值
clanguage.name = "Python教程"
clanguage.add = "http://c.biancheng.net/python"
print(clanguage2.name)


# 调用clanguage的say()方法
clanguage.say("人生苦短，我用Python")
# 再次输出name和add的值
print(clanguage.name, clanguage.add)
# 为clanguage对象增加一个money实例变量
clanguage.money = 159.9
print(clanguage.money)

# 删除新添加的 money 实例变量
#del clanguage.money
# 再次尝试输出 money，此时会报错
#print(clanguage.money)




