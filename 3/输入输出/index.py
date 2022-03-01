'''
Author: wangzhongjie
Date: 2022-03-01 13:45:17
LastEditors: wangzhongjie
LastEditTime: 2022-03-01 14:02:37
Description: 
Email: UvDream@163.com
'''
# 文件操作
f = open('./index.txt', 'w+')
f.write('迷们好')
f.close()
f = open('./index.txt', 'r')

# c = f.read()
print("-----read")
# print(c)
print("----readlines")
l = f.readline()
print(l)
l1 = f.readlines()
print(l1)
f.close()
