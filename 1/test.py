#!/usr/bin/python3


# 列表推导式
from cmath import pi


names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

# 字典推导式
newdict = {name: len(name) for name in names}
print(newdict)

# 集合推导式
setnew = {i**2 for i in (1, 2, 3)}
print(setnew)

# 元祖推导式
a = (x for x in range(1, 10))
print(a)
tuple(a)
