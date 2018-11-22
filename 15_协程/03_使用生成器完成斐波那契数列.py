
# 这不是函数，是生成器
def create_num(all_num):
    # a = 0
    # b = 1
    a, b = 0, 0.1
    current_num = 0
    while current_num < all_num:
        # print(a)
        ret = yield a  # 如果一个函数中有yield 语句，那么这个就不再是函数，而是生成器
        # print("ret-->", ret)
        a, b = b, a+b
        current_num += 1
    return "ok----"


# create_num(10)
obj = create_num(100)
for num in obj:
    print(num, end=" ")
    print()
# num = next(obj)
# print("ret-->", num)
#
# num = obj.send("你好啊")
# print("ret-->", num)
