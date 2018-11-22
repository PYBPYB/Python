info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

print(info_tuple[0])

print(info_tuple.index("zhangsan"))

print(info_tuple.count("zhangsan"))


# 循环遍历元组
for my_tuple in info_tuple:

    print(my_tuple, end=" ")
print()

"""
元组 中保存的变量类型 通常是不同的

"""
num_list = [1, 2, 3, 4, 5]
print(type(num_list))

num_tuple = tuple(num_list)
print(type(num_tuple))
