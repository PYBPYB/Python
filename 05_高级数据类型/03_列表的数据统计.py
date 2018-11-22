name_list = ["张三", "李四", "王五", "张三", "李四", "王五"]
num_list = [1,2,3,42,3,2,3,1,34,2,34,4]

# len(length 长度) 函数可以统计列表中元素的总数
print(len(name_list))

# count 方法可以统计列表中某一个数据出现的次数
print("张三 出现了 %d 次"%name_list.count("张三"))

# 从列表中删除第一次出现的数据，如果数据不存在，程序会报错
name_list.remove("张三")

print(name_list)

print(num_list)

num_list.sort()
print(num_list)
print()

num_list.sort(reverse=True)
print(num_list)

num_list.reverse()
print(num_list)