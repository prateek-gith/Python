class father:
    def __init__(self,sid,sname) -> None:
        self.id=sid
        self.name=sname

    # def Super_1(self):
    #     print(f"Id Is : {self.id}")

    @staticmethod
    def print_1():
        print("i am method of father class")





class child (father):

    # def __init__(self,sname) -> None:
    #     self.name=sname

    def Sub_1(self):
        return f"Name Is : {self.name} Id Is : {self.id}"
    
    @staticmethod
    def print_2():
        print("i am method of Child class")


S1=child(1001,"Prateek")
# S2=child("Prateek")


S1.print_1()
S1.print_2()

# S1.Super_1()
print(S1.Sub_1())


