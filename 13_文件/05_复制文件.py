# 1、打开
file1 = open("README", 'r', encoding='UTF-8')
file2 = open("README[复件]", 'w', encoding='UTF-8')
# 2、读写
file2.write(file1.read())

# 3、关闭
file1.close()
file2.close()