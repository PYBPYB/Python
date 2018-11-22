
import time


def login():
    return "这是主页 time:%s" % time.ctime()

def register():
    return "---register---time:%s" % time.ctime()

def profile():
    return "---profile--- time:%s" % time.ctime()

def application(env, start_response):

    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    else:
        return "没有找到..."

