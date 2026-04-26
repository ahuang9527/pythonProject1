import json

import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "x-b3-traceid": "58410f35245c2882",
    "x-rap-param": "ByQBBQAAAAEAAAAUAAABZBcMZ+UAACfZAAAAHQAAAAAAAAAAYzJzdGMqkbljHE8f0KTgo75w+z5ZAAAAEHLdcXG6eRCjL+16lgSKVvYtHUf05vt302mMlh+sFA7H9eQl7IJwCAz0ZeRwArRCtc6AHYpG00hNxFzc3Gt06UE1oqYd4lJDJcwtt1xs3PNf9crbeTgQ7AY9OuJkHboQL+QRHFiewD9DZn3MqEEsC97T5D8hOcYMDBlEn6aByh37prD3cgroAZqAbvnQ3DJGrDFZwKgGVAQInv2ZafNxcNraLlQfqO+lItDnfPPyT6FO2GO4iIZBT/IAAKCVGJUe+GIir+ct26B/oxycBu6koEKJpSnCqfMzr/qigW8dg+E3DbvthRnHTrlyFmc+7H9AY8m/r3UxK88cHT5kAC9/5LCweW+cnHkkoO1NnQn74SJlWuACWXha9WEtyiDBy+BMoE8d9XHfkfQGa83mbjNGiIYp4DLxdWDWHJQ/m5LiQTnRkvphOPzfAL9WKnzSEkT3921tAOYYGRCsyUoETB1n+UMAAAFT",
    "x-s": "XYS_2UQhPsHCH0c1PUhMHjIj2erjwjQhyoPTqBPT49pjHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQTJdPIPAZlg94aGLTlLoq9+g+r/0rhqf+bqemk8eQmqF4dpB+awepnzsRx2bSocLDUyfEf+7iF8bpUpSQnyrF9yrRGLgSI+eSsnbkGcFRwaBqIankM4r8o8gmHaDpHPLrlL08Pp0p0LF8kpbP3zgQL2p8wGDRj4aTnGFzmPrkHaMY/PbSnzMq7PaT+c9EIqMQCLDkcpnbLP9IlLDT/Jfznnfl0yLLIaSQQyAmOarEaLSz+GDlHN7+MLBEcPauA2bHAJgYVG7k8zUHVHdWFH0ijJ9Qx8n+FHdF=",
    "x-s-common": "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",
    "x-t": "1777206983039",
    "x-xray-traceid": "cee4e53cb64b1a4ccd02037106b85b2e",
    "xy-direction": "93"
}
cookies = {
    "abRequestId": "f8803eb9-65ee-5bb5-b7a4-c167b7a290c2",
    "ets": "1777206890617",
    "webBuild": "6.7.4",
    "xsecappid": "xhs-pc-web",
    "a1": "19dc9c910e14lgyssy9vbep8vsnmimrcy72is2bn050000206061",
    "webId": "749254f29af80ad89eb04ddfabb133da",
    "acw_tc": "0a4ad06c17772068892883636e057fafbd353113ec0d98bf30cc1ddc636e8b",
    "websectiga": "29098a4cf41f76ee3f8db19051aaa60c0fc7c5e305572fec762da32d457d76ae",
    "sec_poison_id": "82b8c705-d54a-4d60-8c21-9513f36e9f30",
    "gid": "yjfSjSjyYdvJyjfSjSjy8WJDdy41kvMMvjhDJI8dUYhMI328636FSM888J8K8Ky8Kii0Wj08",
    "loadts": "1777206934593",
    "web_session": "040069b49bb92f46c358c94edb3b4b3f0df658",
    "id_token": "VjEAAPw2wno3i9yVE2IXQS7HOxy+fbLxWfoAziq/WPmIrC0FmXriaotJs2W7EsVhVdyKgrY3SZqES01ZM0jlZuaottQIdcnlRxbOf9S+KBnBGS3hA6N3e6PvC3b0c75kwL8lu6+o",
    "unread": "{%22ub%22:%2269edee41000000001a02fdfe%22%2C%22ue%22:%2269ed04920000000037035f3d%22%2C%22uc%22:31}"
}
url = "https://edith.xiaohongshu.com/api/sns/web/v1/homefeed"
data = {
    "cursor_score": "",
    "num": 18,
    "refresh_type": 1,
    "note_index": 39,
    "unread_begin_note_id": "",
    "unread_end_note_id": "",
    "unread_note_count": 0,
    "category": "homefeed.fashion_v3",
    "search_key": "",
    "need_num": 8,
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ],
    "need_filter_image": False
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)