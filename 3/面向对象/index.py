# 类对象
class MyClass:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass(3, -4)
print(x)
print(x.i)
print(x.f())
