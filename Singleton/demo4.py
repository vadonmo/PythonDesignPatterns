'''
单例和元类
使用 metaclass 指定元类
'''


class MyInt(type):
    def __call__(self, *args, **kwargs):
        print("**** Here's My int ***", args)
        print("Now do whatever you want with these objects...")
        return super().__call__(*args, **kwargs)
    pass


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


if __name__ == "__main__":
    i = int(4, 5)
    '''
    **** Here's My int *** (4, 5)
    Now do whatever you want with these objects...
    '''
    logger1 = Logger()
    logger2 = Logger()
    print(logger1, logger2)
    '''
    {<class '__main__.Logger'>: <__main__.Logger object at 0x0000022DCC9D0978>} {<class '__main__.Logger'>: <__main__.Logger object at 0x0000022DCC9D0978>}
    '''
