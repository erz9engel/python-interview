# --------------------------------
# 1. Context Manager
# --------------------------------

import sqlite3

class DataConn:
    """Manager for connecting to a database"""
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        """Open a database connection"""
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the connection"""
        self.conn.close()
        if exc_val:
            """Handle closing error"""
            raise

if __name__ == '__main__':
    db = 'test.db'

    with DataConn(db) as conn:
        cursor = conn.cursor()


# --------------------------------
# 2. Singleton
# --------------------------------

# Main idea:
# 1. Ensures that a class has only one instance.
# 2. Provides a global access point.

class Singleton(object):

    def __new__(cls):
        # Override object creation
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print(id(s))
print(s)

b = Singleton()
print(id(b))
print(b)

print(s is b)

# Output:
# 140425907838864
# <__main__.Singleton object at 0x7fb7745a9f90>
# 140425907838864
# <__main__.Singleton object at 0x7fb7745a9f90>
# True


# --------------------------------
# 3. Iterator
# --------------------------------

class SimpleIterator:
    def __iter__(self):
        # Return the iterator to use in a for loop
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


# --------------------------------
# 4. Generator
# --------------------------------

# A function that contains `yield` returns a generator object
# instead of executing immediately.
# It runs each time the `__next__()` method is called.
# In a `for` loop, this happens automatically.
# The function preserves variable values between calls.


def gen(n):
    for i in range(n):
        yield i + 1


g = gen(5)
next(g)

# or

for n in gen(5):
    print(n)


# --------------------------------
# 5. Decorator
# --------------------------------

# Decorators are “wrappers” that allow changing
# a function’s behavior without modifying its code.

def decorator(func):

    def wrapper_func():
        print('hello')
        func()
    return wrapper_func


def func1():
    print('world')

# or

@decorator
def func2():
    print('world')


decorator(func1)()
# or
func2()

# >> hello
# >> world

# --------------------------------
# 6. Decorator with parameters
# --------------------------------

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
