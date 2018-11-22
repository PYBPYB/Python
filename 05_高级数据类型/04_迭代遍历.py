name_list = ["张三", "李四", "王五", "张三", "李四", "王五"]
num_list = [1, 4, 3, 0, 3, 5, 3, 1, 9, 6, 8, 7]

"""

循序的从列表中依次获取数据
每一次循环过程中，数据都会保存在 name 这个变量中
在循环体内部可以访问到当前这一次获取到的数据

"""

for name in name_list:

    print(name, end=" ")

print()

for gl_num in num_list:

    print(gl_num, end=" ")