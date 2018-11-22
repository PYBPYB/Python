import re
import time


def main():
    while True:
        emall = input("请输入你要匹配的邮箱：")
        if emall == "":
            print("程序结束。。。")
            break

        ret = re.match(r"^[0-9a-zA-Z_]{4,20}@(163|123)\.com$", emall)
        if ret:
            print("邮箱： %s 符合要求！" % emall)
        else:
            print("邮箱： %s 不符合标准！" % emall)



if __name__ == '__main__':
    main()