'''
Author: wangzhongjie
Date: 2022-02-25 14:59:16
LastEditors: wangzhongjie
LastEditTime: 2022-02-25 17:53:57
Description: 函数
Email: UvDream@163.com
'''


def max(a, b):
    if a > b:
        return a
    else:
        return b


c = max(4, 5)
print(c)
# 默认参数


def printInfo(name, age=18):
    print("name:", name)
    print("age:", age)

# 不定长参数


def functionName(arg1, *vartuple):
    print("first:", arg1)
    for var in vartuple:
        print(var)
    return


functionName(10)
functionName(10, 2)


def print_info(arg1, **vartuple):
    print("first:", arg1)
    for var in vartuple:
        print(var)
    return


print_info(1, a=1, b=3)
# 匿名函数
a = 1
def x(a): return a+10


print(x)
