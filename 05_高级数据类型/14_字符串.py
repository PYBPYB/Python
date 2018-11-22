str1 = "hello python"
str2 = '我的外号是“大西瓜”'

print("%s\n%s"%(str1,str2))

# 注意：使用 index 方法传递的子字符串不存在，程序运行会出错
print(str1.index("h"))
print(str1.index("ho"))
print()

# 2、统计某一个小（子）字符串出现的次数
print(str1.count("llo"))
print(str1.count("abc"))
