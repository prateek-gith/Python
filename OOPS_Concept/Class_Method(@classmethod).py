class Student:
    Class_Name="MCA"

    def __init__(self,cid,cname,csub) -> None:
        self.id=cid
        self.name=cname
    
    @classmethod
    def class_method_1(cls,str):
        cls.Class_Name=str
    


S1=Student(1001,"Ishika","Python_Coding")

S1.class_method_1("MMCA")

print(Student.Class_Name)


