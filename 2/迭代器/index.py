'''
Author: wangzhongjie
Date: 2022-02-25 14:00:30
LastEditors: wangzhongjie
LastEditTime: 2022-02-25 14:53:59
Description: 迭代器和生成器
Email: UvDream@163.com
'''

from cmath import exp
import sys
import re


list = [1, 2, 3, 4]
it = iter(list)
# 输出迭代器的下一个元素
print(next(it))
print("----")

print(next(it))
for x in it:
    print(x)
# 创建迭代器

print("创建迭代器")


class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            # StopIteration 异常用于表示迭代器的完成,防止出现无限循环的情况
            raise StopIteration


myClass = MyNumber()
myiter = iter(myClass)
for x in myiter:
    print(x)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# StopIteration
# 生成器


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
