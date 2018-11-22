# 字典 是一个无序的数据集合
# 输出 的顺序和定义的顺序可能不一致
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "heiget": 1.75,
            "weight": 75.5}

print(type(xiaoming))
print(xiaoming)

# 1、取值
print(xiaoming["name"])

# 2、增加/修改
xiaoming["like"] = "book"
xiaoming["name"] = "小小明"
# 3、删除
xiaoming.pop("name")

print(xiaoming)