class A:
    Public_A=1001
    _Procectet_A=1002
    __Private_A=1002

class B(A):
    Public_B=2001
    _Procectet_B=2002
    __Private_B=2002

    # @staticmethod
    def print_1(self):
        return self.__Private_A


Obj_B=B()

print(Obj_B._B__Private_B)
print(Obj_B._Procectet_A)
print(Obj_B.print_1())