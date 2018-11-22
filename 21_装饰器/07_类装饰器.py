class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("这里是装饰器里添加的新功能")
        self.func()

@Test
def get_str():
    return "haha"

print(get_str())