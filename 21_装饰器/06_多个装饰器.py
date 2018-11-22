def set_func1(func):
    print('-----装饰器1启动了-----')
    def call_func(*args, **kwargs):
        print("-----权限验证1-----")
        return func(*args, **kwargs)  # 拆包
    return call_func

def set_func2(func):
    print('-----装饰器2启动了-----')
    def call_func(*args, **kwargs):
        print("-----权限验证2-----")
        return func(*args, **kwargs)  # 拆包
    return call_func

def set_func3(func):
    print('-----装饰器3启动了-----')
    def call_func(*args, **kwargs):
        print("-----权限验证3-----")
        return func(*args, **kwargs)# 拆包
    return call_func

@set_func1  # test1 = set_func(test1)
@set_func2
@set_func3
def test1(num, *args, **kwargs):
    print("-----test1-----", num)
    print("-----test1-----", args)
    print("-----test1-----", kwargs)
    return 'ok', '你好啊'

ret = test1(100)
print(ret)