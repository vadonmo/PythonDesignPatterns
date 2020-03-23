#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo1.py
@Time    :   2020/03/22 18:01:47
@Author  :   Vadon Mo
@Version :   1.0
@Contact :   vadonmo@126.com
@License :   Code Project Open License (CPOL)
@Desc    :   简单工厂
'''

from abc import ABCMeta, abstractmethod
'''
@abstractmethod：抽象方法，
1. 含abstractmethod方法的类不能实例化，
2. 继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，
3. 未被装饰的可以不重写
'''


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print('Bhow Bhow!!')


class Cat(Animal):
    def do_say(self):
        print('Meow Meow!!')


class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == "__main__":
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
