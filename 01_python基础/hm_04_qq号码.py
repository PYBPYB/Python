# 1.定义一个变量存储qq号码
# qq_number = "1234567"
qq_number = input("请输入QQ号：")


# 2.定义一个变量存储qq密码
# qq_password = "123"
qq_password = input("请输入QQ密码：")


"""
# 查看类型
type(qq_number)
type(qq_password)

"""

# 如果希望通过解释器的方式，输出变量内容，需使用 print 函数
print("QQ号是：",qq_number)
print("QQ密码是：",qq_password)
print(int(qq_number) * int(qq_password))  # 转换类型函数1234