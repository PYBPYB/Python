def test2(a, b, *areg, **kwarge):

    print(a)
    print(b)
    print(areg)
    print(kwarge)


def test1(a, b, *areg, **kwarge):   # 代表分组。。
    print("------1------")
    print(a)
    print(b)
    print(areg)
    print(kwarge)
    print("------2------")
    test2(a, b, areg, kwarge)
    print("------3------")
    test2(a, b, *areg, kwarge)
    print("------4------")
    test2(a, b, *areg, **kwarge)  # ’*‘代表拆包！！

if __name__ == '__main__':
    test1(1, 2, 3, 4, 5, 6, name="小明", age = "18")