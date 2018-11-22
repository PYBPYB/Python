import gevent
import time
from gevent import monkey

monkey.patch_all()  # 将所有延时操作变为 gevent 能识别的延时

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.2)
        # gevent.sleep(0.1)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1.0)
        # gevent.sleep(1)

gevent.joinall([
    gevent.spawn(f1(5)),
    gevent.spawn(f2(5)),
    gevent.spawn(f3(5)),
])

# print("---1---")
# g1 = gevent.spawn(f1, 5)
# print("---2---")
# g2 = gevent.spawn(f2, 5)
# print("---3---")
# g3 = gevent.spawn(f3, 5)
# print("---4---")

# g1.join()
# g2.join()
# g3.join()
