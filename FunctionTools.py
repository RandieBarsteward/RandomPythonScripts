import functools

def mydecorator(func):
    #@functools.wraps(func)
    def wrapper(*args, **kwargs):
        '''Description from Wrapper function'''
        print("We could do anything here (before)")
        return func(y=42, *args, **kwargs)
    return wrapper

@mydecorator
def myfunc (x, y=37, z=127):
    '''Description for function'''
    print(x, y, z)

myfunc(x=3, z=4)
print(myfunc.__name__)
print(myfunc.__doc__)