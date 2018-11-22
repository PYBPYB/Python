import socket
import threading
import time


def recv_msg(udp_socket):
    """接收数据并显示"""

    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    """发送数据"""

    while True:
        send_data = input("请输入要发送的数据：")
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))

def main():
    """完成udp聊天器的整体控制"""

    # 1、创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2、绑定本地信息
    udp_socket.bind(("", 7891))

    # 3、获取对方ip
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入对方的端口号"))

    # 4、创建两个线程，去执行相应的功能
    threading.Thread(target=recv_msg, args=(udp_socket,)).start()
    threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port)).start()


if __name__ == '__main__':
    main()