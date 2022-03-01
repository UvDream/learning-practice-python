'''
Author: wangzhongjie
Date: 2022-02-25 17:54:06
LastEditors: wangzhongjie
LastEditTime: 2022-03-01 14:02:21
Description: 模块
Email: UvDream@163.com
'''

import sys
import support
from fibo import fibo1

print("命令行参数如下:")
for i in sys.argv:
    print(i)
print("\n\nPython 路径为：", sys.path, "\n")
support.print_func('111')
fibo1()
str = input("请输入:")
print("你输入的内容是: ", str)
