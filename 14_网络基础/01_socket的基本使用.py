import socket

def main():

    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地的相关信息，如果一个网络程序绑定，则系统会随机分配
    # local_addr = ('', 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    # udp_socket.bind(local_addr)

    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")

        if len(send_data) <= 0:
            break

        # 可以使用套接字收发数据
        # udp_socket.sendto("hahaa",对方的ip以及port)
        # udp_socket.sendto("hahaa", ("192.168.85.130",8080))
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.85.130", 7788))

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()