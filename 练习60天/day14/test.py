import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(f'{url} 状态: {resp.status}')
            return await resp.text()

async def main():
    urls = ['http://httpbin.org/delay/1'] * 5
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(f'完成 {len(results)} 个请求')

asyncio.run(main())