# 1、打开文件
file = open("README", 'r', encoding='UTF-8')
# 2、读取文件内容
print(file.read())

print("-" * 50)

# 注意：read 方法运行完以后会将标记指针移动到文件末尾
#      第二次运行就读取不到文件了
print(file.read())

# 3、关闭文件
file.close()