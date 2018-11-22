import socket
import re
import threading

def service_client(new_socket, request):
    """为这个客户端返回数据"""
    # 接送浏览器发送过来的请求
    # GET / HTTP/1.1
    # ......

    request_lines = request.splitlines()
    print("")
    print(">>" * 50)
    print(request_lines)

    # /index.html HTTP/1.1
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*" * 60, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 返回http格式的数据给浏览器
    try:
        f = open("./html/" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NO FOUND\r\n"
        response += "\r\n"
        response += "--------file not found--------"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    tcp_server_socket.bind(("", 6788))

    # 变为监听套接字
    tcp_server_socket.listen(128)

    tcp_server_socket.setblocking(False)  # 设置套接字为非堵塞方式
    client_socket_list = list()

    while True:
        # time.sleep(1)
        try:
            new_socket, new_addr = tcp_server_socket.accept()
        except Exception as ret:
            # print("---没有新的客户端到来---")
            pass
        else:
            # print("---只要没有产生异常，那么也就意味者，来了一个新客户---")
            new_socket.setblocking(False)  # 设置套接字为非堵塞方式
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                # print(ret)
                # print("---这个客户端没有发送过来数据---")
                pass
            else:
                if recv_data:
                    # print("---客户端发送过来了数据---")
                    service_client(client_socket, recv_data)
                else:
                    # 对方调用了close 导致了 recv 返回
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()