import socket  # socket 套接字是全双工的！！！

def main():

    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 获取对方的IP和port
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入对方的端口号："))

    while True:

        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")

        if len(send_data) <= 0:
            break

        # 可以使用套接字收发数据
        # udp_socket.sendto("hahaa",对方的ip以及port)
        # udp_socket.sendto("hahaa", ("192.168.85.130",8080))
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

        # 等待接受对方的数据
        recv_data = udp_socket.recvfrom(1024)
        # recv_data 这个变量里存储的是一个元组(b'123', ('192.168.85.1', 7788))
        recv_msg = recv_data[0]  # 存储接收到的数据
        recv_addr = recv_data[1]  # 存储接收到的对方的地址信息
        if recv_msg == 88:
            break
        # 打印接收到的数据
        # print(recv_data)
        print("%s:%s" % (str(recv_addr), recv_msg.decode("utf-8")))

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()