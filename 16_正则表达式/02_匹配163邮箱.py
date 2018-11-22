import re


def main():
    while True:
        emall = input("请输入你要匹配的邮箱：")

        ret = re.match(r"^[0-9a-zA-Z_]{4,20}@163\.com$", emall)
        if ret:
            print("邮箱： %s 符合要求！" % ret.group())
        else:
            print("邮箱： %s 不符合标准！" % emall)



if __name__ == '__main__':
    main()