class delegate(object):
    def __init__(self, name, age,):
        self.__name = name
        self.__age = age
        self.__results = []

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        pass

    def get_age(self):
        return self.__age

    def set_results(self):
        pass

    def output_results(self):
        pass


#Create a new instance of delegate called newDelegate (object)
newDelegate = delegate("Frank",14)
print(newDelegate.get_name()) #takes name from get_name method
#print(newDelegate.__name) # throw error because name is private to the class
print(newDelegate.get_age()) #takes name from get_age method

newDelegate2 = delegate("Bobby",12)
print(newDelegate2.get_name()) #takes name from get_name method
#print(newDelegate2.__name) # throw error because name is private to the class
print(newDelegate2.get_age()) #takes name from get_age method

newDelegate.set_name("Franklin") #calls setname to change the value of name
print(newDelegate.get_name()) #takes name from get_name method
#print(newDelegate.__name) # throw error because name is private to the class
print(newDelegate.get_age()) #takes name from get_age method

#delegate.set_results()
#examtitle = input("Enter Exam Title: ")
examresult = input("Enter Exam Result: ")
#newDelegate.set_title(examtitle)
#newDelegate.set_results()
#print(newDelegate.output_results())