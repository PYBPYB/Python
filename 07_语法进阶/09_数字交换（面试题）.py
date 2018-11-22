a = 6
b = 100

# 解法1：-使用其他变量
c = a
a = b
b = c
print("解法1：", a, b)



a = 6
b = 100
# 解法2：-不使用其他变量
a = a + b
b = a - b
a = a - b
print("解法2：", a, b)



a = 6
b = 100
# 解法3：-Python 专有
# a, b = (b, a)
# 等号右边是元组，只是省略了小括号
a, b = b, a
print("解法3：", a, b)
