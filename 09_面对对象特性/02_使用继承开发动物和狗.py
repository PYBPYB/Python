class Animal:

    def eat(self):
        print("吃。。。")

    def drink(self):
        print("喝。。。")

    def run(self):
        print("跑。。。")

    def sleep(self):
        print("睡。。。")


class Dog(Animal):

    def bark(self):  b
        print("汪汪叫。。")

    def sleep(self):
        print("好困。。")


class XiaoTianChuan(Dog):
    def fly(self):
        print("我会飞。。")

    def bark(self):

        # 1、针对子类的需求，编写代码
        print("像神一样的叫唤")

        # 2、使用 super（），调用原本在父类中封装的方法
        super().bark()
        super().sleep()

        # 3、增加其他子代码
        print("sdfjoeiggrfeijg。。。")


xiaobai = Dog()
xiaobai.eat()
xiaobai.run()
d

xiaotianquan = XiaoTianChuan()
xiaotianquan.bark()