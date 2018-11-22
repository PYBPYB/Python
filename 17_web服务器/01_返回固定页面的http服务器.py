import socket
import re

def service_client(new_socket):
    """为这个客户端返回数据"""
    # 接送浏览器发送过来的请求
    # GET / HTTP/1.1
    # ......
    request = new_socket.recv(1024).decode("utf-8")

    # http://www.runoob.com/python/att-string-splitlines.html
    request_lines = request.splitlines()
    print("")
    print(">>" * 50)
    print(request_lines)


    # /index.html HTTP/1.1
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
        # header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # body
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)




    # 关闭套接字
    new_socket.close()


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    tcp_server_socket.bind(("", 6788))

    # 变为监听套接字
    tcp_server_socket.listen(128)

    while True:

        # 等待新客户的接入
        new_socket, client_addr = tcp_server_socket.accept()

        # 为这个客户服务
        service_client(new_socket)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()