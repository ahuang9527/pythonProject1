from urllib import request,parse
'''
将testspider1的内容使用函数重写
包含3部分
1.拼接url地址
2.发送请求保存至本地
3.程序主入口
'''

#拼接url地址
def get_url(word):
    url = 'https://www.baidu.com/s?wd={}'
    params = parse.quote(word)
    full_url = url.format(params)
    return full_url


#发送请求，保存本地文件
def request_url(full_url,filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    # 创建请求对象
    req = request.Request(url=full_url, headers=headers)
    # 获取响应对象
    res = request.urlopen(req)
    # 解码获取响应内容
    html = res.read().decode("utf-8")

    # 保存为本地文件
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

#主程序入口，调用get_url函数生成要查询的拼接url地址
#将该地址与要保存的文件名传入请求函数request_url，获取对应内容
if __name__ == '__main__':
    # 想要搜索的内容
    word = input('请输入搜索内容：')
    url = get_url(word)
    print(url)
    filename = word + '.html'
    request_url(url,filename)
