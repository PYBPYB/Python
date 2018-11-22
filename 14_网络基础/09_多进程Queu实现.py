import multiprocessing

def dowload_from_web(q):
    # 模拟从网上下载数据
    data = [11, 22, 33, 44, 55]

    # 像队列中写入数据
    for temp in data:
        q.put(temp)

def analysis_data(q):

    waitting_analysis_data = list()

    # 从队列中获取数据
    while True:
        data = q.get()
        waitting_analysis_data.append(data)
        if q.empty():
            break

    print(waitting_analysis_data)



def main():

    # 1、创建一个队列
    q = multiprocessing.Queue()

    # 2、创建多个进程，将队列的引用当作实参进行传递到里面
    multiprocessing.Process(target=dowload_from_web, args=(q,)).start()
    multiprocessing.Process(target=analysis_data, args=(q,)).start()


if __name__ == '__main__':
    main()