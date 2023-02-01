'''
程序模拟多线程
def sing():
    for i in range(2):
        print('正在唱歌:%d'%i)
        time.sleep(1)


def dance():
    for i in range(2):
        print('正在跳舞:%d'%i)
        time.sleep(1)

if __name__=='__main__':
    sing()
    dance()
'''



'''
# 通过函数创建多线程
def demo():
    #线程的函数事件
    print('子线程！')

if __name__=='__main__':
    for i in range(8):
        #只是创建还没有启动
        t= threading.Thread(target=demo())
        # 启动(一个可以启动的状态)
        t.start()
'''


'''
#通过thread类重写run方法来创建多线程
class MyThread(threading.Thread):
    #重写run方法
    def run(self):
        for i in range(5):
            print('这是第%d个子进程'%i)

if __name__=='__main__':
    my=MyThread()
    my.start()

#线程中传入参数时，需要使用参数 args 注意传入的是一个元组；
t1 = threading.Thread(target=MyThread(), args=(100000,))
'''


'''
主线程与子线程的执行关系
（1）主线程会等待子线程结束之后结束；

（2）join（）等待子线程结束之后，主线程继续执行；

（3）setDaemon（）守护线程，不会等待子线程结束，即当主线程执行完，无论子线程有没有技术都会结束程序；


def text():
    for i in range(4):
        print('子线程')

if __name__=='__main__':
    t=threading.Thread(target=text())
    t.start()
    # 当主线程运行完，无论子线程玩没玩都会结束
    # t.setDaemon()
    # 不论子线程运行多久，一定是要等待子线程运行完成之后才运行主线程，有个timeout参数，可以设置等待时间
    #t.join()
    print("主线程")
    
'''

'''
查看线程数量
（1）enumerate() 方法在循环中使用时，会连同索引一起返回：
# enumerate()  连同索引一起返回
text_list = ['xxx', 'yyy', 'zzz']
for index, i in enumerate(text_list):
    # print(type(i), i)
    print(index, i)
    
（2）threading.enumerate() 查看线程数量的方法：

threading.enumerate()	查看当前线程的数量



# threading.enumerate()
def demo1():
    for i in range(8):
        time.sleep(1)
        print(f'demo1--{i}')


def demo2():
    for i in range(5):
        time.sleep(1)
        print(f'demo2--{i}')


if __name__ == '__main__':
    t1 = threading.Thread(target=demo1)
    # print(threading.enumerate())
    t2 = threading.Thread(target=demo2)
    t1.start()
    # 在start开始时子线程才会创建成功
    # print(threading.enumerate())
    t2.start()
    # print(threading.enumerate())
    while True:
        time.sleep(1)
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break

'''




'''
num = 100
# 线程锁，解决资源竞争问题
lock = threading.Lock()


# RLock 可以上多把锁,上多少解多少
# rlock = threading.RLock()

def demo1(num1):
    global num
    # 上锁
    lock.acquire()
    for i in range(num1):
        num += 1
    # 解锁
    lock.release()
    print(f'demo1--{num}')


def demo2(num1):
    global num
    lock.acquire()
    for i in range(num1):
        num += 1
    lock.release()
    print(f'demo2--{num}')


def main():
    # 使用 args 传参  当传入的参数很大时，资源竞争更加明显，CPU调度问题
    t1 = threading.Thread(target=demo1, args=(100000,))
    t2 = threading.Thread(target=demo2, args=(100000,))
    t1.start()
    t2.start()
    print(f'main--{num}')


if __name__ == '__main__':
    main()

'''

'''
#Condition版的生产者和消费者

gMoney = 0
# 定义一个变量 保存生产的次数 默认是0次
gTimes = 0
# 定义一把锁
# gLock = threading.Lock()
gCond = threading.Condition()


# 定义生产者
class Producer(threading.Thread):

    def run(self):
        global gMoney
        global gTimes

        while True:
            gCond.acquire()  # 上锁
            if gTimes >= 10:
                gCond.release()
                break
            money = random.randint(0, 100)
            gMoney += money
            gTimes += 1
            print("%s生产了%d元钱，剩余%d元钱" % (threading.current_thread().name, money, gMoney))
            gCond.notify_all()
            gCond.release()  # 解锁


# 定义消费者
class Consumer(threading.Thread):

    def run(self):
        global gMoney
        while True:
            gCond.acquire()  # 上锁
            money = random.randint(0, 100)

            while gMoney < money:
                if gTimes >= 10:
                    gCond.release()
                    return  # 这里如果用break只能退出外层循环，所以我们直接return
                print("%s想消费%d元钱，但是余额只有%d元钱了，并且生产者已经不再生产了！" % (threading.current_thread().name, money, gMoney))
                gCond.wait()
            # 开始消费
            gMoney -= money
            print("%s消费了%d元钱，剩余%d元钱" % (threading.current_thread().name, money, gMoney))
            gCond.release()


def main():
    # 开启5个生产者线程
    for x in range(5):
        th = Producer(name="生产者%d号" % x)
        th.start()
    # 开启5个消费者线程
    for x in range(5):
        th = Consumer(name="消费者%d号" % x)
        th.start()


if __name__ == '__main__':
    main()

'''



