
def fanctiong(k, b):  # 这里面只可能会有一个 def 方法
    def run(x):
        print(k * x + b)
    return run


if __name__ == '__main__':
    text1 = fanctiong(2, 3)
    text1(3)