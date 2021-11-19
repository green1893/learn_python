"""类定义学习"""
""" Python 3 Module of the Week: https://pymotw.com/3/index.html"""
from collections import OrderedDict

class Dog():
    """第一次模拟小狗🐶"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is sitting now.")
    
    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rolled over!")

my_dog = Dog("little yellow", 2)
my_dog.sit()
my_dog.roll_over()