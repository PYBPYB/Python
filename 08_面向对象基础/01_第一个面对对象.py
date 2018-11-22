class Cat:

    def eat(self):
        print("%s 爱吃鱼"% self.neme)

    def drink(self):
        print("%s 会喝水"% self.neme)

# 创建猫对象
Tom = Cat()
Tom.eat()
Tom.drink()

print(Tom)

# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

# lazy_cat2 和 lazy_cat 是同一只猫
lazy_cat2 = lazy_cat

print(lazy_cat2)