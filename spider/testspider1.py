from urllib import request,parse

#定义URL变量，拼接url地址
url = 'https://www.baidu.com/s?wd={}'
#想要搜索的内容
word = input('请输入搜索内容：')
params = parse.quote(word)
#拼接url与要搜索的内容
full_url = url.format(params)
'''


 向URL发送请求
发送请求主要分为以下几个步骤：

    创建请求对象-Request
    获取响应对象-urlopen
    获取响应内容-read
'''
#重构请求头，可使用U-A代理池或fake_useragent的UserAgent方法自动生成
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
#创建请求对象
req = request.Request(url=full_url,headers=headers)
#获取响应对象
res = request.urlopen(req)
#解码获取响应内容
html = res.read().decode("utf-8")


#保存为本地文件
filename = word + '.html'
with open(filename,"w",encoding="utf-8") as f:
    f.write(html)
