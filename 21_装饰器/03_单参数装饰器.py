def set_func(func):
    print('-----装饰器启动了-----')
    def call_func(a):
        print("-----权限验证-----")
        func(a)
    return call_func

@set_func  # test1 = set_func(test1)
def test1(num):
    print("-----test1-----%d" % num)

@set_func
def test2(num):
    print("-----test1-----%d" % num)


test1(100)
test2(200)