from queue import Queue
import threading
import requests
from concurrent.futures import ThreadPoolExecutor


def worker(queue, results):
    while True:
        url = queue.get()
        if url is None:  # 结束信号
            break
        try:
            resp = requests.get(url, timeout=5)
            results.append((url, resp.status_code))
        except Exception as e:
            results.append((url, f'Error: {e}'))
        finally:
            queue.task_done()

# 任务队列
q = Queue()
results = []

# 启动 3 个工作线程
num_workers = 3
threads = []
for _ in range(num_workers):
    t = threading.Thread(target=worker, args=(q, results))
    t.start()
    threads.append(t)

# 添加任务
urls = ['http://books.toscrape.com'] * 6
for url in urls:
    q.put(url)

# 等待所有任务完成
q.join()

# 发送结束信号
for _ in range(num_workers):
    q.put(None)
for t in threads:
    t.join()

print(f'完成 {len(results)} 个请求')