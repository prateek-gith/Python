# Dunder Method == Special Method
# In This Concept Name Is Mapping Operator To Function 

class A:
    def __init__(self,id,name,salary) -> None:
        self.id=id
        self.name=name
        self.salary=salary
    
    def printD(self):
        # print(self.id," And ",self.name," And ",self.salary)
        return f"Id Is {self.id} And Name Is {self.name} And Salary Is {self.salary}"
    
    # Dunder Or Special Method
    # It Is use When We Use + Operator (Add Two Object Of Same Class(A)) Then It Run
    # It Is Call Operator Overloading Which Is Work On Object 
    def __add__(self,other):
        return self.salary + other.salary
    

    # When We Print The Object Of The Class then Print A string 
    # For This use We Make A Special(Dunder Method) __repr__(self)
    def __repr__(self) :
        # 1.Type We Call The Any Class Method Which Is Return Type String
        # return self.printD()

        # 2. Simply We return Any instance Variable Or Calss variable
        # return self.name

        # 3. Simply return The Any String
        return f"Name Is {self.name} Id Is {self.id}"
    
    def __str__(self):
        return f"Detail Is : ('{self.name}',{self.id})"
    
if __name__=='__main__':

    Obj_1=A("1001","Prateek",100000)
    Obj_2=A("1002","Ishika",200000)

    # We Try To Add The Object Of same Class  then It run __add__ Method
    print(Obj_1 + Obj_2)
    # print(Obj_1.printD())

    # Cal The __repr__(self) Method
    print(Obj_1)
    print(repr(Obj_1))