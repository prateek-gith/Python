class Student:
    
    # def __init__(self,Argument_1, Argument_2,Argument_3,Argument_4-------Argument_n) 
    # this is called constructor 
    # the work of constructor is it assign the value in class variable which is pass while creating object
    # constructor ka work hota h object cration ke time di gyi value ko class ke vaiable me value ko assign krna
    # self object ko leta h

    # type 1st
    def __init__(self,cid,cname) -> None:
        self.id=cid
        # yanni jis object ke through value pass kr rahe ho us object ki id me jo value pass kri h object bnate time vo value assign kr do
        self.name=cname

    # type 2nd
    # def __init__(self,cid,cname):
    #     self.id=cid
    #     self.name=cname
        
    # this is method of class
    def printdetail(self):
        return f"Name Is {self.name} And Id Is {self.id}"
    
S1=Student(1001,"Ishika")
S2=Student(102,"Prateek")

print(S1.printdetail())
print(S2.printdetail())