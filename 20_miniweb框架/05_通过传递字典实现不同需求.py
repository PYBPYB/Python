import socket
import re
import multiprocessing
from ftame import mini_frame


class WSGIServer(object):

    def __init__(self):
        # 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定端口
        self.tcp_server_socket.bind(("", 6789))
        # 变为监听套接字
        self.tcp_server_socket.listen(128)

    def service_client(self, new_socket):
        """为这个客户端返回数据"""
        # 接送浏览器发送过来的请求
        # GET / HTTP/1.1
        # ......
        request = new_socket.recv(1024).decode("utf-8")
        # print(request)

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
        # 如果请求的资源不是以.py结尾，则认为是静态资源请求
        if not file_name.endswith(".py"):
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
        else:


            env = dict()
            env['PATH_INFO'] = file_name
            body = mini_frame.application(env, self.set_response_header)  # 传方法的引用，而不是方法

            header = "HTTP/1.1 %s\r\n" % self.status

            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])

            header += "\r\n"

            response = header + body
            # 发送
            new_socket.send(response.encode("utf8"))


        # 关闭套接字
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [('server', 'mini_web v1.0')]
        self.headers += headers

    def run_forever(self):
        while True:
            # 等待新客户的接入
            new_socket, client_addr = self.tcp_server_socket.accept()

            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()

            new_socket.close()  # 主进程才能关闭文件

        # 关闭监听套接字
        self.tcp_server_socket.close()



def main():
    """
    控制整体，创建一个web 服务器对象
    然后调用这个对象的 run_forever方法运行
    """
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()

if __name__ == '__main__':
    main()