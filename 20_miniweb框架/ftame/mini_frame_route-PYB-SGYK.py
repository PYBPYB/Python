import re

"""
 URL_FUNC_DICI = {
 "/index.py":index
 "/center.py":center
 
 }
"""

URL_FUNC_DICI = dict()

def route(url):
    def set_func(func):
        # URL_FUNC_DICI['/index.py'] = index
        URL_FUNC_DICI[url] = func
        def call_fun(*args, **kwargs):
            return func(*args, **kwargs)
        return call_fun
    return set_func

@route("/index.html")
def index():
    with open("./templates/index.html") as f:
        content = f.read()

    my_stock_info = "哈哈哈哈，这是你的本月名称..."

    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content

@route("/center.html")
def center():
    with open("./templates/center.html") as f:
        content = f.read()

    my_stock_info = "这里是从mysql 查询出来的数据。。。"

    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    try:
        return URL_FUNC_DICI[file_name]()
    except Exception as ret:
        return "产生了异常：%s" % str(ret)