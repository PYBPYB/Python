
import cards_tools

while True:

    cards_tools.show_menu()



    action_str = input("请输入希望进行的操作：")

    print(action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:


        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        else:
            cards_tools.search_card()
        # pass

    # 0 退出系统
    elif action_str == "0":

        print("-" * 50)
        print("欢迎再次使用【名片管理系统】！")

        break
        # 如果在开放程序时，不希望立刻编写分支内部的代码
        # 可以使用 pass 关键字， 表示一个占位符，能够保证程序的代码结构正确xm1
        # 程序运行时，pass 关键字不会执行任何的操作
        # pass
    # 其他内容输入错误，需要提示用户
    else:
        print("-" * 50)
        print("您输入的不正确，请重新选择。。。")