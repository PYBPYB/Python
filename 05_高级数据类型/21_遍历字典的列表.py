students = [{"name": "张三"},
            {"name": "李四"},
            {"name": "小美"}]

find_name = "张"

for stu_dict in students:
    print(stu_dict)

    if stu_dict["name"] == find_name:

        print("找到了 %s"%stu_dict["name"])
        break
else:
    print("抱歉，没有找到 %s"%find_name)

print("查找过程结束了")