'''
单例模式
'''


class Singleton(object):
    def __new__(cls):
        print(dir(cls))
        if not hasattr(cls, 'instance'):  # 判断有没有 instance 属性
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    s1 = Singleton()
    print("Object created", s1)

    s2 = Singleton()
    print('Object created', s2)
'''
Object created <__main__.Singleton object at 0x000002512F7E1AC8>
Object created <__main__.Singleton object at 0x000002512F7E1AC8>

'''
'''
通过dir 更方便看到两者的区别
'''
