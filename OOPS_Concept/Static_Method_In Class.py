class Student:
    @staticmethod
    def static_method(string):
        print(f"{string} Is A Good Boy/Girl")

    @staticmethod
    def Sum(a,b):
        return a+b


S1=Student()

# We can Call The class static Method using class Object
S1.static_method("Prateek")

# We can Call The class static Method using class name 
Student.static_method("Ishika")

# We can Also Create A Static Method  like A Function But It is fetch/Call Only By the Class Or Class Object 
a=S1.Sum(10,20)
print(a)