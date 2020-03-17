'''
懒汉单例模式
'''


class Singleton(object):
    __instance = None
    '''
    区别：
        对于”new”和”init”可以概括为：
        “new”方法在Python中是真正的构造方法（创建并返回实例），通过这个方法可以产生一个”cls”对应的实例对象，所以说”new”方法一定要有返回。
        对于”init”方法，是一个初始化的方法，”self”代表由类产生出来的实例对象，”init”将对这个对象进行相应的初始化操作。
    '''
    def __new__(cls):
        # print('__new__')
        return super().__new__(cls)

    def __init__(self):
        if not Singleton.__instance:
            print('__init__ method called...')
        else:
            print('Instance already created:', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


if __name__ == "__main__":
    s1 = Singleton()
    print('Object created', s1.getInstance())

    s2 = Singleton()
    print(s2.getInstance())

'''
__init__ method called
__init__ method called
Object created <__main__.Singleton object at 0x000002040B0C1A58>
Instance already created: <__main__.Singleton object at 0x000002040B0C1A58>
'''
