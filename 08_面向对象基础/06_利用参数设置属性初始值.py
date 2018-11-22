class Cat():
    """这是一个猫类"""

    def __init__(self, new_name):

        print("---这是一个初始化方式---")
        # self.属性名 = 属性的初始值
        # self.name = "Tom"

        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


Tom = Cat("Tom")
print(Tom.name)

Lazy_cat = Cat("lazy_cat")
Lazy_cat.eat()
