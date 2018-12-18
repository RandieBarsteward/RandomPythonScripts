import functools

def myfunc(x, y=37, z=123):
    """test function"""
    print(x, y, z)

mydefault = functools.partial(myfunc, y=42)
mydefault(x=3, z=4)

functools.update_wrapper(mydefault, myfunc)
print(mydefault.__name__)
print(mydefault.__doc__)