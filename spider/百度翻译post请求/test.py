import execjs

#读取js文件
with open('sign.js','r',encoding='utf-8') as f:
    reader=f.read()

#加载编译读取内容
loader=execjs.compile(reader)
#调用执行js文件中的方法
r=loader.call('e','test')
print(r)


print(execjs.get())