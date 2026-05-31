import asyncio

import aiohttp

'''
async def add_async(a, b):
    return a + b

result = asyncio.run(add_async(1, 2))
print(result)  # 3'''

'''
#await 挂起等待 顺序执行
async def say_after(delay, what):
    await asyncio.sleep(delay)  # 异步等待，不阻塞
    print(what)

async def main():
    print("开始")
    await say_after(1, "你好")
    await say_after(2, "世界")
    print("结束")

asyncio.run(main())'''

'''
#create_task 并发执行

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    start_time = time.time()  # 开始计时
    task1 = asyncio.create_task(say_after(3, "你好"))
    task2 = asyncio.create_task(say_after(2, "世界"))

    print("任务已创建，开始并发等待...")
    await task1
    await task2
    print("结束")
    end_time = time.time()  # 结束计时
    print(f'总耗时: {end_time - start_time:.2f} 秒')

asyncio.run(main())

'''

'''
#asyncio.gather() 并发执行多个任务
async def say_after(delay, what):
    await asyncio.sleep(delay)
    return what

async def main():
    start_time = time.time()  # 开始计时
    results = await asyncio.gather(
        say_after(1, "你好"),
        say_after(2, "世界"),
        say_after(0.5, "！")
    )
    print(results)   # ['你好', '世界', '！']（顺序固定）
    end_time = time.time()  # 结束计时
    print(f'总耗时: {end_time - start_time:.2f} 秒')

asyncio.run(main())

'''



'''
#aiohttp(异步中代替request，在协程中使用)
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    html = await fetch('https://www.baidu.com/')
    print(html)

asyncio.run(main())

'''

'''
#aiohttp中可以直接获得的与需要await的
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"状态码（立即可得）: {response.status}")      # 不需要 await
            print(f"Content-Type（立即可得）: {response.headers.get('Content-Type')}")
            # 现在尝试读取响应体，需要 await
            body = await response.text()
            print(f"响应体长度: {len(body)}")

asyncio.run(fetch('https://www.baidu.com/'))

'''

'''
#自定义请求头和并发请求批量抓取
async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    urls = [
        "https://www.baidu.com/s?ie=UTF-8&wd=test",
        "https://www.baidu.com/s?wd=test&pn=50",
        "https://www.baidu.com/s?wd=test&pn=60"
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 ...",
        "Accept": "text/html"
    }
    params = {"key1": "value1", "key2": "value2"}
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for url, html in zip(urls, results):
            print(f"{url} 返回长度: {len(html)}")

asyncio.run(main())
'''

'''
#POST 请求与发送数据
async def post_example():
    data = {"name": "张三", "age": 20}
    async with aiohttp.ClientSession() as session:
        # 发送 form 数据（application/x-www-form-urlencoded）
        async with session.post("https://httpbin.org/post", data=data) as resp:
            result = await resp.json()
            print(result["form"])

        # 发送 JSON 数据
        async with session.post("https://httpbin.org/post", json=data) as resp:
            result = await resp.json()
            print(result["json"])
asyncio.run(post_example())

'''

'''
#异常处理
async def safe_fetch(session, url):
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            response.raise_for_status()  # 如果状态码非 2xx，抛出异常
            return await response.text()
    except asyncio.TimeoutError:
        print(f"请求超时: {url}")
    except aiohttp.ClientError as e:
        print(f"请求错误: {url}, {e}")
    except Exception as e:
        print(f"未知错误: {url}, {e}")
    return None  # 失败返回 None
asyncio.run(safe_fetch())
'''


HEADERS = {"User-Agent": "Mozilla/5.0"}
CONCURRENCY = 5
TIMEOUT = aiohttp.ClientTimeout(total=150)

async def fetch(sem, session, url):
    async with sem:
        try:
            async with session.get(url, headers=HEADERS, timeout=TIMEOUT) as resp:
                resp.raise_for_status()
                html = await resp.text()
                print(f"✓ {url}")
                return html
        except Exception as e:
            print(f"✗ {url}: {e}")
            return None

async def main():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://example.com",
    ]
    sem = asyncio.Semaphore(CONCURRENCY)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(sem, session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        # 后续解析 results 中非 None 的数据
        for url, html in zip(urls, results):
            if html:
                print(f"{url} 抓取成功，长度 {len(html)}")

if __name__ == "__main__":
    asyncio.run(main())








