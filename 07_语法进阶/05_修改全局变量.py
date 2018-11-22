# global 关键字修改全局变量

gl_num = 10

def demo1():

    # global 关键字会告诉解释器 后面的变量是 全局变量
    # 在碰见赋值语句，就不会创建 局部变量了
    global gl_num

    # 函数内部 自己新建的变量 ，名字也叫 num
    gl_num = 99

    print("demo1 ==> %d ,num 的地址为 %d" % (gl_num, id(gl_num)))

def demo2():


    print("demo2 ==> %d ,num 的地址为 %d" % (gl_num, id(gl_num)))



demo1()
demo2()