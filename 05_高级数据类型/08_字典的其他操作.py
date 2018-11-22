xiaoming_ditc = {"name": "小明",
                 "age": 18}

# 1、统计键值对数量
print(len(xiaoming_ditc))

# 2、合并字典
temp_dict = {"name": "小小明",
             "height": 1.75,
             }

# 注意：如果合并的字典中包含已经存在的键值对，会覆盖原有的键值对
xiaoming_ditc.update(temp_dict)


print(xiaoming_ditc)

# 3、循环遍历
for my_dict in xiaoming_ditc:

    print("%s \t %s"%(my_dict,xiaoming_ditc[my_dict]))

# 4、清空字典
xiaoming_ditc.clear()

print(xiaoming_ditc)