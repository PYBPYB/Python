def measure():
    """测量温度和湿度"""

    print("测量开始。。。")

    temp = 39
    wetness = 50
    print("测量结束。。。")

    # 元组 - 可以包含多个数据
    # 如果函数返回的是元组，小括号可以省略
    return temp, wetness

# 元组
result = measure()

print(result[0])
print(result[1])

# 如果函数返回值是元组，同时希望单独处理元组中的元素
# 可以使用多个变量，一次接受函数的返回结果
# 注意：使用多个变量接收结果时，变量个数=返回的元组里的元素个数
gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)