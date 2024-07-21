class Student:
    def __init__(self,cid,cname,csub) -> None:
        self.id=cid
        self.name=cname
    
    @classmethod
    def class_method_1(cls,str):
        a=str.split("-")
        # split ==> It is String function that convert into a list after devide which is given into split parameter                  {   split("-")   }
        # for example if we print the a (after split) then output is ==> [1001,"prateek","MCA"]
        return cls(a[0],a[1],a[2])

    @classmethod
    def class_method_2(cls,arg):
        return cls(*arg.split("-"))
    
# S1=Student(1001,"Ishika")
# S2=Student(102,"Prateek")

S1=Student.class_method_1("1001-Prateek-MCA")
S2=Student.class_method_2("1002-Ishika-MCA")

print(S1.id)
print(S2.id)

