import time
import threading

def sing():
    """唱歌五秒钟"""
    for i in range(5):
        print("正在唱歌中。。。1")
        time.sleep(1)

    # 如果创建 Thread 时执行的函数运行结束，那么就意味着这个子线程结束了

def dance():
    """跳舞五秒钟"""
    for i in range(5):
        print("正在跳舞中。。。0")
        time.sleep(1)


def main():
    threading.Thread(target=sing).start()  # 函数名() 这是调用函数
    threading.Thread(target=dance).start()  # 函数名 相当于找到程序函数的地址

    while True:
        print("当前线程运行的线程数为：%d" % len(threading.enumerate()))
        if len(threading.enumerate()) <= 1:
            break

        time.sleep(1)


if __name__ == '__main__':
    main()