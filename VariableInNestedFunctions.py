'''
result = 3
def myfunc():
    result = 12
    def scope_test():
        if result < 45:
            result += 1
            scope_test()
        scope_test()
'''


result = 3
def myfunc():
    result = 12
    def scope_test():
        nonlocal result
        if result < 45:
            print(result)
            result += 1
            scope_test()
    scope_test()
    print(result, "from myfunc")

myfunc()
print(result, "from main")