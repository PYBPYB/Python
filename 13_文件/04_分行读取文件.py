file = open("README", encoding='UTF-8')

while True:
    text = file.readline()

    print(text, end='')
    # 判断是否读取到内容
    if not text:
        break


file.close()