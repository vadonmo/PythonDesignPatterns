'''
Monostate单例模式
'''


class Brog:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


class Brog2(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Brog2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


if __name__ == "__main__":
    # b = Brog()
    # b1 = Brog()
    # b.x = 4
    b = Brog2()
    b1 = Brog2()
    b.x = 4

    print("Brog Object 'b':", b)
    print("Brog Object 'b1':", b1)
    print("Object State'b':", b.__dict__)
    print("Object State 'b1':", b1.__dict__)
'''
Brog Object 'b': <__main__.Brog object at 0x00000142B2DF0278>
Brog Object 'b1': <__main__.Brog object at 0x00000142B2DF02B0>
Object  State'b': {'1': '2', 'x': 4}
Object State 'b1': {'1': '2', 'x': 4}
'''

'''
Brog Object 'b': <__main__.Brog2 object at 0x0000017EE2C8F2E8>
Brog Object 'b1': <__main__.Brog2 object at 0x0000017EE2C8FC88>
Object State'b': {'x': 4}
Object State 'b1': {'x': 4}
'''
