import re

file = open("C:/Users/26797/Desktop/职位要求.txt", encoding="gbk")

while True:
    text = file.readline()
    if text:
        ret = re.sub(r"(<.>|<..>|<...>|<....>)", "", text)
        print(ret, end="")
    else:
        break

file.close()