gl_list = [4, 6, 5, 7, 1, 3, 8, 2, 9, 0]

# 默认按照升序排序
gl_list.sort()
print(gl_list)
# reverse 就是缺省参数！！！
gl_list.sort(reverse=True)
print(gl_list)

def print_info(name, gender = True):
    """

    :param name: 班上同学的名字
    :param gender: Ture:男生  False:女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" %(name,gender_text))

# 假设班上的同学男生居多
# 缺省参数应该处于末尾位置
print_info("小明")
print_info("老王")
print_info("小美", gender=False)