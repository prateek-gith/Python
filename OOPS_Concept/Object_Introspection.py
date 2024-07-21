class A:
    def __init__(self,F_Name,L_Name):
        self.F_Name=F_Name
        self.L_Name=L_Name
        # self.E_Mail=f"{self.F_Name}_{self.L_Name}@Gmail.com"
    
    def Print_Detail(self):
        return f"The Name Is {self.F_Name}_{self.L_Name}"
    
    @property
    def E_Mail(self):
        if self.L_Name==None or self.F_Name==None :
            return "Email Is Not Found"
        return f"{self.F_Name}_{self.L_Name}@Gmail.com"
    
    @E_Mail.setter
    def E_Mail(self,Str):
        Split_String=Str.split("@")[0]
        Name=Split_String.split("_")
        self.F_Name=Name[0]
        self.L_Name=Name[1]

    @E_Mail.deleter
    def E_Mail(self):
        self.F_Name=None
        self.L_Name=None

import inspect

if __name__=='__main__':
    Obj_1=A("Prateek","Yadav")

    # type() --> retrun the Class Of Object 
    print("\t\t\t\t\tReurn Class Of Object\n")
    print(type(Obj_1))
    print(type("This Is String"))
    print(Obj_1.E_Mail)

    print("\n\t\t\t\t\tReurn Directory Class Of Object\n")
    print(dir(Obj_1))

    print("\n\t\t\t\t\tReurn unique Id Of Object OR Attribute\n")
    print(id(Obj_1))

    print("\n\t\t\t\t\tInspect (Member) Class Of Object\n")
    print(inspect.getmembers(Obj_1))