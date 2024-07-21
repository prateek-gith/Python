class Student:
        
    # this is method of class
    def printdetail(self):
        # self ==> it is a work like a object
        # when we call the this method through the class object then self is the object which object  called this method
        # jis object ke through hm is method ko call kr rahe h self vah object bn jata h
        # kyuki yah kisi perticual ek object ke liye method nhi h koi bhi object jo ki is class ke dwara bna hua h call kr sakta h 
        return f"Name Is {self.name} And Id Is {self.id}"
    
S1=Student()
S2=Student()

S1.name="Ishika"
S1.id=1001

S2.name="Prateek"
S2.id=1002

print(S1.printdetail())
print(S2.printdetail())