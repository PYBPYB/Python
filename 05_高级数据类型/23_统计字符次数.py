
def main():
    dict_num = dict()
    srt = input("请输入字符：")
    for s in srt:
        if s in dict_num:
            dict_num[s] = dict_num[s] + 1
        else:
            dict_num[s] = 1

    for key, value in dict_num.items():
        print("%s ---> %d 次" % (key, value))

if __name__ == '__main__':
    main()