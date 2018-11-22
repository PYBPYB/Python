import threading
import time


g_num = 100


def test1():
    global g_num
    g_num += 1
    print("g_lobal 在 test1 里面的值是 %d" % g_num)


def test2():
    print("g_lobal 在 test2 里面的值是 %d" % g_num)


def main():
    threading.Thread(target=test1).start()
    threading.Thread(target=test2).start()


if __name__ == '__main__':
    main()