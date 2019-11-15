--------------------------------
1. Context Manager
--------------------------------

import sqlite3

class DataConn:
    """Менеджера для подключения к базе"""
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        """Открываем подключение с базой данных"""
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрываем подключение"""
        self.conn.close()
        if exc_val:
            """Обрабатываем ошибку закрытия"""
            raise

if __name__ == '__main__':
    db = 'test.db'

    with DataConn(db) as conn:
        cursor = conn.cursor()


--------------------------------
2. Singleton
--------------------------------

Основная мысль:
1. Гарантирует, что у класса есть только один экземпляр!
2. Предоставляет глобальную точку доступа

class Singleton(object):

    def __new__(cls):
        # Перекрываем создание объекта класса
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print id(a)
print s

b = Singleton()
print id(b)
print b

print (s is b)

# Вывод:
# 140425907838864
# <__main__.Singleton object at 0x7fb7745a9f90>
# 140425907838864
# <__main__.Singleton object at 0x7fb7745a9f90>
# True


--------------------------------
3. Iterator
--------------------------------

class SimpleIterator:
    def __iter__(self):
        # возвращаем итератор чтобы использовать в цикле for
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

iter = SimpleIterator(5)
for i in iter:
    print(i)


--------------------------------
4. Generator
--------------------------------

Функция, содержащая yield, возвращает объект-генератор,
а не выполняет свой код сразу.
исполняется при каждом вызове метода __next__().
В цикле for это делается автоматически.
функция сохраняет значения переменных от предыдущего вызова.


def gen(n):
    for i in range(n):
        yield i + 1


g = gen(5)
next(g)

# или

for n in gen(5):
    print(n)


--------------------------------
5. Decorator
--------------------------------

Декораторы — "обёртки", которые дают возможность
изменить поведение функции, не изменяя её код.


def decorator(func):

    def wrapper_func():
        print('hello')
        func()
    return wrapper_func


def func1():
    print('world')

# или

@decorator
def func2():
    print('world')


decorator(func1)()
# или
func2()

# >> hello
# >> world


--------------------------------
6. Decorator с параметрами
--------------------------------

def param_decorator(word):
    def decorator(func):
        def wrapper_func():
            print('hello')
            func()
        return wrapper_func
    return decorator


@param_decorator('hello')
def func3():
    print('world')


func3()

# >> hello
# >> world
