'''
Author: wangzhongjie
Date: 2022-02-24 16:51:41
LastEditors: wangzhongjie
LastEditTime: 2022-02-24 16:55:29
Description: 列表   
Email: UvDream@163.com
'''
list1 = ['Google', 'Runoob', 1997, 2000]
# 获取指定的元素
print("已经输出列表：", list1[0])
print(list1[1:3])
print(list1[-1])
# 更新列表
list1[0] = 'Runoob'
print(list1)
# 删除列表
del list1[2]
print(list1)
# 长度
print(len(list1))
