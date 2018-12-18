#function that calls other function

#closure definition - note the nested function
def multiplyit(num):
    def multiplier(val):
        return num * val
    return multiplier

#Create a "trebler" (a function object)

treble = multiplyit(3)

#create a doubler

double = multiplyit(2)

#output 10
print(double(5))
#Output: 12'
print(treble(4))

#And these calls are nestable; outputs: 12
print(double(treble(2)))


