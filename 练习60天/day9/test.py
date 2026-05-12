import random

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

from trio import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 访问无限滚动页面
    page.goto('https://www.taobao.com/')

    # 等待初始内容加载
    page.wait_for_selector('.layer')
    time.sleep(2)


    # 记录已有的数量
    previous_count = 0
    target_count = 90  # 我们想要抓取的总数

    while True:
        # 获取当前页面上所有
        quote_elements = page.locator('//span[contains(@class, "info-wrapper-title-text")]')
        current_count = quote_elements.count()
        print(f'当前可见商品：{current_count} 条')

        # 满足退出条件：达到目标数量或连续两次滚动数量不再增加
        if current_count >= target_count:
            print(f'已达到目标数量 ({target_count})，停止滚动。')
            break
        if current_count == previous_count:
            print('滚动后未加载新商品，可能已到底，停止滚动。')
            break
        previous_count = current_count

        # 【核心改进】模拟更真实的滚动行为
        # A. 优先对搜索结果容器内的最后一个元素使用 scroll_into_view_if_needed() 方法[reference:1]
        last_quote_elements = quote_elements.last
        last_quote_elements.scroll_into_view_if_needed()

        # B. 组合使用随机的鼠标滚轮滚动 (mouse.wheel)
        page.mouse.wheel(delta_x=0, delta_y=random.randint(200, 500))

        # C. 随机等待，模拟阅读时间
        page.wait_for_timeout(random.randint(1000, 3000))

        time.sleep(0.5)  # 尊重服务器

    # 获取最终的完整 HTML，交给 BeautifulSoup 解析
    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')

    data = []
    for quote in soup.select('div.tb-pick-content-item.new-hover'):
        title_elem = quote.select_one('span.info-wrapper-title-text')
        price_elem = quote.select_one('span.price-value')

        if title_elem and price_elem:
            text = title_elem.get_text(strip=True)
            money = price_elem.get_text(strip=True)
            data.append({'text': text, 'money': money})
        else:
            # 可选：打印出有问题的 div 的前200字符，帮助定位
            # print('发现结构异常的商品卡片，已跳过')
            pass

    print(f'一共成功抓取 {len(data)} 条')



    for item in data:
        print(item['text'], '价格：', item['money'])


    time.sleep(20)
    browser.close()
