def test(num):

    print("%s 在函数内部对应的内存地址是 %d" % (num, id(num)))

    # 定义一个字符串变量
    result = "hello"

    print("函数内部：%s 数据的内存地址是 %d" % (result, id(result)))

    # 将字符串变量返回
    return result

# 1、定义一个 数字变量
a = 10

# 数据的地址本质上就是一个数字
print("%d 在函数外部对应的内存地址是 %d" % (a, id(a)))

# 2、 调用 test 函数，本质上传递的是实参保存数据的引用，而不是实参本身
r = test(a)

# 函数返回的也是 实参保存数据的引用，而不是实参本身
print("函数外部：%s 对应的内存地址是 %s" % (r, id(r)))