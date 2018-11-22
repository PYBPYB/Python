import re

names = ["name1", "_name", "2_name", "__name__", "___", "---#", "jafn!!"]

for name in names:
    ret = re.match(r"^[a-zA-Z_]+[\w]*$", name)

    if ret:
        print("变量名 %s 符合要求！" % ret.group())
    else:
        print("变量名 %s 不符合标准！" % name)