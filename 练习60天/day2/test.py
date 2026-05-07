import os

import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "PSTM": "1769092927",
    "BAIDUID": "ADDCA3633D94DE950A9AB74FC06792E9:FG=1",
    "BD_UPN": "12314753",
    "BIDUPSID": "045D9B0CF7102B192779C81EB524D918",
    "BDUSS": "NLdzRrdDVGSWY5a09aajJCYThnTS02b3c3YTN6QjJkc3dITmtiT1pVQno2N05wRVFBQUFBJCQAAAAAAAAAAAEAAAC9XaCy1ru~tMjwyve6uruv1-kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHNejGlzXoxpLW",
    "BDUSS_BFESS": "NLdzRrdDVGSWY5a09aajJCYThnTS02b3c3YTN6QjJkc3dITmtiT1pVQno2N05wRVFBQUFBJCQAAAAAAAAAAAEAAAC9XaCy1ru~tMjwyve6uruv1-kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHNejGlzXoxpLW",
    "MCITY": "-131%3A",
    "ZFY": "IahiGttpD6dx8hU3Q2:AGji:BiTAod5LohBoGINrSL5cA:C",
    "BAIDUID_BFESS": "ADDCA3633D94DE950A9AB74FC06792E9:FG=1",
    "H_PS_PSSID": "63148_67862_68165_68297_68738_69006_69160_69178_69227_69245_69239_69233_69234_69296_69251_69385_69398_69401_69402_69396_69420_69415_69412_69423_69446_69435_69450_69342_69338_69347_69344_69348_69350_69340_69496_69499_69515_69554_69555_69569_69591_69651_69668_69664_69658_69683",
    "delPer": "0",
    "BD_CK_SAM": "1",
    "PSINO": "5",
    "BA_HECTOR": "8l21ah2g8l252l0k0k048h210h2g871kviskm26",
    "BDORZ": "B490B5EBF6F3CD402E515D22BCDA1598",
    "H_WISE_SIDS": "63148_67862_68165_68297_68738_69006_69160_69178_69227_69245_69239_69233_69234_69296_69251_69385_69398_69401_69402_69396_69420_69415_69412_69423_69446_69435_69450_69342_69338_69347_69344_69348_69350_69340_69496_69499_69515_69554_69555_69569_69591_69651_69668_69664_69658_69683",
    "H_WISE_SIDS_BFESS": "63148_67862_68165_68297_68738_69006_69160_69178_69227_69245_69239_69233_69234_69296_69251_69385_69398_69401_69402_69396_69420_69415_69412_69423_69446_69435_69450_69342_69338_69347_69344_69348_69350_69340_69496_69499_69515_69554_69555_69569_69591_69651_69668_69664_69658_69683",
    "SMARTINPUT": "%5Bobject%20Object%5D"
}

#resp.apparent_encoding：根据网页内容自动猜出来的正确编码,避免乱码
response = requests.get('https://www.baidu.com/index.htm', cookies=cookies, headers=headers)
response.encoding = response.apparent_encoding

# 获取当前 py 文件所在目录
#__file__：代表当前脚本文件本身
#os.path.dirname()：获取文件所在的文件夹路径

current_dir = os.path.dirname(os.path.abspath(__file__))# 获取当前 py 文件所在目录
#__file__：代表当前脚本文件本身
#os.path.dirname()：获取文件所在的文件夹路径
save_path = os.path.join(current_dir, "index.html")
with open(save_path, "wb") as f:
    f.write(response.content)

print("保存成功：", save_path)