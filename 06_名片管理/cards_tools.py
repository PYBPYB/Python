# 记录所有的名片字典
card_list = []


def show_menu():
    print("*" * 50)
    print("名片管理系统1.0")
    print()
    print("1、新建名片")
    print("2、显示全部")
    print("3、查询名片")
    print()
    print("0、退出系统")

    print("*" * 50)

def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1、提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ:")
    emall_str = input("请输入邮箱：")

    # 2、使用用户输入的名片信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "emall": emall_str}

    # 3、将名片字典添加到列表中
    card_list.append(card_dict)

    print(card_list)

    # 4、提示用户添加成功
    print("-" * 50)
    print("添加 %s 用户，成功！" % name_str)

def show_all():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录
    if len(card_list) == 0:

        print("当前没有任何名片记录，请使用 新增名片 功能添加名片！")

        # 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    # 打印分割线
    print("-" * 50)
    # 1、遍历名片列表依次输出所有信息
    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["emall"]))


def search_card():

    print("-" * 50)
    print("搜索名片")

    # 1、提示用户输入要 搜索 的名字
    find_name = input("请输入要搜索的姓名：")

    # 2、遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了，%s 的信息如下：" % find_name)
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print("")
            # 打印分割线
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["emall"]))

            #  针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)

            break
    else:
        print("抱歉，没有找到 %s ..."%find_name)

def deal_card(find_dict):
    """
    处理查找到的文件
    :param find_dict:查找到的文件
    """
    # print(find_dict)
    action_str = input("请选择要执行的操作：、"
                       "【1】（修改）  "
                       "【2】（删除）  "
                       "【0】（返回上一级）")

    if action_str == "1":

        print("修改名片 *直接回车，则不修改！！！*")
        find_dict["name"] = input_card_info(find_dict["name"], "新的姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "新的电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "新的QQ：")
        find_dict["emall"] = input_card_info(find_dict["emall"], "新的邮箱：")
        print("修改 名片 成功！")

    elif action_str == "2":

        print("删除名片")
        card_list.remove(find_dict)
        print("删除 名片 成功！")


def input_card_info(dict_value, tip_massage):

    """
    输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_massage: 输入的提示文字
    :return: 如果用户输入了内容就返回内容，否则返回字典中原有的值
    """
    # 1、提示用户输入内容
    result_str = input(tip_massage)

    # 2、针对用户输入的内容进行判断，如果用户输入了内容没直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3、如果没有输入内容，返回‘字典中原有的值’
    else:
        return dict_value


