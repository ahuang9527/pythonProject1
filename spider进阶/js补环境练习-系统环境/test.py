import execjs

#query = input("请输入要翻译的中文:")
# 读取js文件
with open('test.js', 'r', encoding='utf-8') as f:
    reader = f.read()
# 将读取的内容编译
loader = execjs.compile(reader)
# call执行编译的内容
result = loader.call('ps')
print(result)