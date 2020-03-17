import sqlite3


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Database(metaclass=MetaSingleton):

    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


if __name__ == "__main__":
    db1 = Database().connect()
    db2 = Database().connect()

    print("Database Objects is DB1", db1)
    print("Database Objects is DB2", db2)
    '''
    Database Objects is DB1 <sqlite3.Cursor object at 0x000001D30715D260>
    Database Objects is DB2 <sqlite3.Cursor object at 0x000001D30715D260>
    '''
