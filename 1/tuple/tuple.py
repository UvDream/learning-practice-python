'''
Author: wangzhongjie
Date: 2022-02-24 16:59:55
LastEditors: wangzhongjie
LastEditTime: 2022-02-24 17:34:09
Description: 元祖
Email: UvDream@163.com
'''
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = 1, 2, 3
print(tup1)

print(tup2)
# 访问元祖
print(tup1[0])
print(tup2[1:3])
# 修改元祖

tup3 = tup1+tup2
print(tup3)
# 删除元祖
# del tup1

print(tup1)
# 判断是否存在
print('Google' in tup3)
# len
print(len(tup3))
# 复制
tup4 = tup2*2
print(tup4)
# 内置函数
# 返回最大
max = max(tup2)
print(max)
# 最小
min = min(tup2)
# 将可迭代(循环)转换为元祖
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tup5 = tuple(list1)
print(tup5)
