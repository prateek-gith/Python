class Class_A:
    Class_A_Var=10
    def __init__(self,Name,Sub_1) -> None:
        self.name=Name
        self.sub_1=Sub_1
    
    def Print_A_Detail(self) :
        return f"{self.name}, {self.sub_1}, {self.Class_A_Var}"

class Class_B:
    CLass_B_Var=20
    def __init__(self,Number) -> None:
        self.Number=Number

    def Print_B_Detail(self) :
        return f"{self.Number}, {self.CLass_B_Var}"


class Class_C(Class_B,Class_A):
    Class_C_Var=30
    def Print_C_Detail(self) :
        return f"{self.Class_C_Var}"
    # def __init__(self, Name, Sub_1) -> None:
    #     super().__init__(Name, Sub_1)

S1=Class_C("Math")
print(S1.Print_B_Detail())

