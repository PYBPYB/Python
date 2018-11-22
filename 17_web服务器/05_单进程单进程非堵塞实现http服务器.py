import socket
import time

# 创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定端口
tcp_server_socket.bind(("", 6789))

# 变为监听套接字
tcp_server_socket.listen(128)

tcp_server_socket.setblocking(False)  # 设置套接字为非堵塞方式
client_socket_list = list()

while True:
    # time.sleep(1)
    try:
        new_socket, new_addr = tcp_server_socket.accept()
    except Exception as ret:
        print("---没有新的客户端到来---")
    else:
        print("---只要没有产生异常，那么也就意味者，来了一个新客户---")
        new_socket.setblocking(False)  # 设置套接字为非堵塞方式
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024).decode("utf-8")
        except Exception as ret:
            # print(ret)
            print("---这个客户端没有发送过来数据---")
        else:
            if recv_data:
                print("---客户端发送过来了数据---", recv_data)
            else:
                # 对方调用了close 导致了 recv 返回
                client_socket_list.remove(client_socket)
                client_socket.close()

