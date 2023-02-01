import re

import execjs
import requests


#请求参数无误，但是会报错访问异常1022
#百度翻译访问仍有异常，但是网上目前没有找到处理办法，先暂时搁置。等之后学习深入后解决该问题后，我写一篇针对该问题的博客
class Baidufanyispider():
    # 初始化
    def __init__(self):
        self.url='https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    # 获取get请求带params的页面
    def get_page(self, params):
        headers={
            "Cookie": 'BIDUPSID=045D9B0CF7102B192779C81EB524D918; PSTM=1672884109; BAIDUID=045D9B0CF7102B19951FB815B9FD4C7D:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=00ak0g2104840hak0h85al5u1hst1h31k; BAIDUID_BFESS=045D9B0CF7102B19951FB815B9FD4C7D:FG=1; ZFY=pJpYZncGsW6Xy68o77YOs6mHy6nr:A9lrZF7AEIwvLsc:C; BAIDU_WISE_UID=wapp_1674480200620_45; __bid_n=18581b965eaaf0e54a4207; arialoadData=false; FPTOKEN=pSnyGh+5Xc8kzgF2GfcJfzWbTsNgzNH49GXrmUEef3SnHNPHuSDy2zF+0wkiJJAMYTSaU/ioaghQWutmbnRZFArIMJfybaNU9UJ06LQaMXm+o+nta53QIo2zZfjGjAdlKeQKPMuKsezXxs9/heawUStDuSfGgIYCZsRS/NodTavxEyM3a9qbSpmZw6cY0qSFfPGxWnKvyMSDA+YS1XIp2a/ft44Cd4CXp7I99lNIoQqpy0uc7xoy8uFnCkzs33Q69ucSyBIOzaIkapu2nl1UBn1Nvn0xDOlZ7AKtIdAT2LS19UznlEagJ7+J7mvpJFq9V4GHe84+nwyWzi78LhcywHdxNJOYXh09IQNBAdFgjKTbpyxreWlD6K6KDP/0yLLWMxQmbuzLiCr4N1P291xSDQ==|eYJ+qdKTru/ju+I/6mU5+6QqiadF5cf+Y0z6f20ppf8=|10|d79c4cd5c67ae35d8010471ad7738430; RT="z=1&dm=baidu.com&si=f405506b-3039-45d2-b45e-47ae0d5adb3e&ss=ld8u9ysk&sl=6&tt=64c&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=7x1&ul=95j&hd=968"; delPer=0; PSINO=1; H_PS_PSSID=36544_37647_38055_36920_37990_37929_26350_37881; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1674182639,1674203218,1674475238,1674527775; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1674550135; ab_sr=1.0.1_YTk0MzE5NDkxMTIyZDM5MDYwN2Y1MWE5ZjA2OWEyZmQ5NjYwYzJiNmMxNDE3M2U1M2MxYjYwMDY2YzVkY2I1OGFkNWE0NDZjMDA0NzUzMWRhOGI5NDNiYTA5OTMzZDI0MTQwY2Y5OGYyNTA4NmE0OGVjZTE0OGEzZWQ4NTAzMzc3YWE1YTNkYjU1MGRiMjFjZDAzNThhNWQwOTFhYWYzYw==',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        # 将json格式的响应体进行反序列化为python字典
        #html = requests.post(url=self.url, headers={'user-agent': UserAgent().random}, params=params).json()
        html = requests.post(url=self.url, headers=headers, params=params).json()
        print(html)
        #self.parse_html(html)

    #请求网页获取token参数
    def get_token(self):
        url='https://fanyi.baidu.com/?aldtype=16047'
        headers = {
            "Cookie": 'BIDUPSID=045D9B0CF7102B192779C81EB524D918; PSTM=1672884109; BAIDUID=045D9B0CF7102B19951FB815B9FD4C7D:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=00ak0g2104840hak0h85al5u1hst1h31k; BAIDUID_BFESS=045D9B0CF7102B19951FB815B9FD4C7D:FG=1; ZFY=pJpYZncGsW6Xy68o77YOs6mHy6nr:A9lrZF7AEIwvLsc:C; BAIDU_WISE_UID=wapp_1674480200620_45; __bid_n=18581b965eaaf0e54a4207; arialoadData=false; FPTOKEN=pSnyGh+5Xc8kzgF2GfcJfzWbTsNgzNH49GXrmUEef3SnHNPHuSDy2zF+0wkiJJAMYTSaU/ioaghQWutmbnRZFArIMJfybaNU9UJ06LQaMXm+o+nta53QIo2zZfjGjAdlKeQKPMuKsezXxs9/heawUStDuSfGgIYCZsRS/NodTavxEyM3a9qbSpmZw6cY0qSFfPGxWnKvyMSDA+YS1XIp2a/ft44Cd4CXp7I99lNIoQqpy0uc7xoy8uFnCkzs33Q69ucSyBIOzaIkapu2nl1UBn1Nvn0xDOlZ7AKtIdAT2LS19UznlEagJ7+J7mvpJFq9V4GHe84+nwyWzi78LhcywHdxNJOYXh09IQNBAdFgjKTbpyxreWlD6K6KDP/0yLLWMxQmbuzLiCr4N1P291xSDQ==|eYJ+qdKTru/ju+I/6mU5+6QqiadF5cf+Y0z6f20ppf8=|10|d79c4cd5c67ae35d8010471ad7738430; RT="z=1&dm=baidu.com&si=f405506b-3039-45d2-b45e-47ae0d5adb3e&ss=ld8u9ysk&sl=6&tt=64c&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=7x1&ul=95j&hd=968"; delPer=0; PSINO=1; H_PS_PSSID=36544_37647_38055_36920_37990_37929_26350_37881; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1674182639,1674203218,1674475238,1674527775; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1674550135; ab_sr=1.0.1_YTk0MzE5NDkxMTIyZDM5MDYwN2Y1MWE5ZjA2OWEyZmQ5NjYwYzJiNmMxNDE3M2U1M2MxYjYwMDY2YzVkY2I1OGFkNWE0NDZjMDA0NzUzMWRhOGI5NDNiYTA5OTMzZDI0MTQwY2Y5OGYyNTA4NmE0OGVjZTE0OGEzZWQ4NTAzMzc3YWE1YTNkYjU1MGRiMjFjZDAzNThhNWQwOTFhYWYzYw==',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        html = requests.get(url=url, headers=headers).text
        #re.search(pattern,string,flags=0)参数说明：pattern：正则表达式string：目标字符串
        token=re.search(r"token: '(.*?)',",html).group(1)
        print(token)
        return token

    #定义入口函数
    def run(self):
        query=input("请输入要翻译的中文:")
        #使用execjs包中的方法执行分析页面提取的json文件，进而得到动态变化的params参数sign
        #读取js文件
        with open('sign.js','r',encoding='utf-8') as f:
            reader=f.read()
        #将读取的内容编译
        loader=execjs.compile(reader)
        sign=loader.call('e',query)
        token=self.get_token()
        #构建查询参数params
        params={
            'from':'zh',
            'to':'en',
            'query':query,
            #'transtype':'realtime',
            'simple_means_flag':'3',
            'sign':sign,
            'token':token,
            'domain':'common'
        }
        print(params)
        self.get_page(params)

#初始化对象并调用函数
if __name__=='__main__':
    spider=Baidufanyispider()
    spider.run()

