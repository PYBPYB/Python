
# a = 0
# b = 1
#
# for num in range(10):
#     a, b = b, a+b
# print(a, b)


class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        eit = self.a
        if self.current_num < self.all_num:

            self.a, self.b = self.b, self.a+self.b
            self.current_num += 1
        else:
            raise StopIteration
        return eit


fibo = Fibonacci(10)

for name in fibo:
    print(name, end=" ")
print("")
