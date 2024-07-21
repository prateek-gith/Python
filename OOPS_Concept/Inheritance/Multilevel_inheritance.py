class Grand_Father:
    def __init__(self,Name) -> None:
        self.name=Name
    
    @staticmethod
    def GrandPrint():
        print("This Is Grand_Father Method")
    
    Ghr=4

class Father(Grand_Father):
    def __init__(self,Name,Address) -> None:
        self.name=Name
        self.Add=Address
    
    @staticmethod
    def FatherPrint():
        print("This Is Father Method")
    
    Home=3

class Son(Father):
    def __init__(self,Name,Address,Mob) -> None:
        self.name=Name
        self.Add=Address
        self.MoB=Mob

    @staticmethod
    def SonPrint():
        print("This Is Son Method")
    
    Home=1
    House=2


S1=Son("Prateek","Shuklagnj",9956)
# print(S1.name)
print(S1.Ghr)
print(S1.Home)
print(S1.House)
S1.SonPrint()