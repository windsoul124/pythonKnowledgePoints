class Employee:
    """员工信息"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee {}'.format(Employee.empCount))

    def displayEmployee(self):
        print('Name:{}, Salary:{}'.format(self.name, self.salary))


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


# 创建 Employee 类的第一个对象
emp1 = Employee('Zara', 2000)
# 创建 Employee 类的第一个对象
emp2 = Employee('Manni', 5000)

#  显示员工信息
emp1.displayEmployee()
emp2.displayEmployee()
print('Total Employee : {}'.format(Employee.empCount))

#  操作属性
emp1.age = 2
emp1.age = 5
del emp1.age

# getattr(emp2, 'age')  # 获得对象的属性
# hasattr(emp2, 'age')  # 检测是否存在属性，存在返回True
# setattr(emp2, 'age', 8)  # 添加属性
# delattr(emp2, 'age')  # 删除属性

print('Employee.__doc__:{}'.format(Employee.__doc__))
print('Employee.__name__:{}'.format(Employee.__name__))
print('Employee.__module__:{}'.format(Employee.__module__))
print('Employee.__bases__:{}'.format(Employee.__bases__))
print('Employee.__dict__:{}'.format(Employee.__dict__))


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, '销毁')


pt1 = Point()
del pt1
