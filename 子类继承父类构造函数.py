#  子类需要父类构造函数
# class Father(object):
#     def __init__(self, name):
#         self.name = name
#         print('Name:{}'.format(self.name))
#
#     def getName(self):
#         return 'Father:{}'.format(self.name)
#
# class Son(Father):
#     def getName(self):
#         return 'Son:{}'.format(self.name)
#
# son = Son('Andy')
# print(son.getName())

#  子类不需要父类构造函数
# class Father(object):
#     def __init__(self, name):
#         self.name = name
#         print('Name:{}'.format(self.name))
#
#     def getName(self):
#         return 'Father:{}'.format(self.name)
#
# class Son(Father):
#     def __init__(self, name):
#         self.name = name
#         print("Hi, I'm {}".format(self.name))
#     def getName(self):
#         return 'Son:{}'.format(self.name)
#
# son = Son('Andy')
# print(son.getName())


#  子类既需要父类的构造函数，又需要重写`__init__`
class Father(object):
    def __init__(self, name):
        self.name = name
        print('Name:{}'.format(self.name))

    def getName(self):
        return 'Father:{}'.format(self.name)

class Son(Father):
    def __init__(self, name):
        self.name = name
        super(Son, self).__init__(name)
        print("Hi, I'm {}".format(self.name))
    def getName(self):
        return 'Son:{}'.format(self.name)

son = Son('Andy')
print(son.getName())