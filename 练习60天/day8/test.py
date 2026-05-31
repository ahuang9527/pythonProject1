import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 请将这里的路径替换成你电脑上 chromedriver.exe 的实际位置
service = Service(r"D:\study-spider\driver\chromedriver-win64-147\chromedriver.exe")
driver = webdriver.Chrome(service=service)



driver.implicitly_wait(30)  # 全局隐式等待，最多等10秒

try:
    # 1. 访问登录页面
    driver.get('http://quotes.toscrape.com/login')

    # 2. 输入用户名密码
    driver.find_element(By.ID, 'username').send_keys('myuser')
    driver.find_element(By.ID, 'password').send_keys('mypassword')

    # 3. 点击登录按钮
    driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]').click()

    # 4. 等待登录成功后的特征元素出现（比如 Logout 按钮）
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Logout'))
    )
    print('登录成功！')

    # 5. 现在可以爬取登录后可见的数据
    #    比如首页的名人名言列表
    driver.get('http://quotes.toscrape.com/')

    # 使用 BeautifulSoup 解析
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    quotes = soup.select('div.quote')
    data = []
    for quote in quotes:
        text = quote.select_one('span.text').text
        author = quote.select_one('small.author').text
        data.append({'text': text, 'author': author})
    print(data)
    print(f'爬取到 {len(data)} 条名言')
    for item in data[:3]:
        print(item['text'][:30], '—', item['author'])

finally:
    time.sleep(20)
    driver.quit()

