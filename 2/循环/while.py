'''
Author: wangzhongjie
Date: 2022-02-25 11:25:19
LastEditors: wangzhongjie
LastEditTime: 2022-02-25 13:53:06
Description: 循环语句
Email: UvDream@163.com
'''
# while
count = 0
while count < 7:
    print(count)
    count += 1
else:
    print("循环结束")

# for
langs = ['js', 'go', 'py']
for lang in langs:
    print(lang)
else:
    print("无数据循环")
# range
for i in range(5):
    print(i)

# while 中使用break
a = 1
while a < 10:
    a += 1
    if a == 5:
        break
    else:
        print("打断", a)

# for 循环使用break
for i in range(5):
    if i == 3:
        break
    print("断线了", i)
# pass
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
