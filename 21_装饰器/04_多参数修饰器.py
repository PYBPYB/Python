def set_func(func):
    print('-----装饰器启动了-----')
    def call_func(*args, **kwargs):
        print("-----权限验证-----")
        func(*args, **kwargs)  # 拆包
    return call_func

@set_func  # test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("-----test1-----", num)
    print("-----test1-----", args)
    print("-----test1-----", kwargs)


test1(100)
test1(100, 200)
test1(100, 200, 300, mm='你好啊')
