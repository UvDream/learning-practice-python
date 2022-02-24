'''
Author: wangzhongjie
Date: 2022-02-24 17:41:52
LastEditors: wangzhongjie
LastEditTime: 2022-02-24 17:48:50
Description: 字典
Email: UvDream@163.com
'''
dict1 = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print(dict1)
# 查看字典数量
print(len(dict1))
# 查看类型
print(type(dict1))
# 访问值
print(dict1['name'])
# 修改字典
dict1['name'] = 'Google'

print(dict1)
# 清空字典
# dict1.clear()
print(dict1)

# 删除字典
# del dict1
print(dict1)
print('------')

str(dict1)
