# This Problem Create In Multiple Inheritance
# A-->B         B inherit The Property Of A
# A-->C         C inherit The Property Of A
# B,C--D        D inherit The Property Of B,C

class A:
    def PritntD(Self) :
        print("This Is The Method Of Class A")

class B(A):
    def PritntD(Self) :
        print("This Is The Method Of Class B Which IS Inherit The A Class Method")

class C(A):
    def PritntD(Self) :
        print("This Is The Method Of Class C Which IS Inherit The A Class Method")

class D(B,C):
    def PritntD(Self) :
        print("This Is The Method Of Class D Which IS Inherit The B,C Class Method")

if __name__=='__main__':
    Obj_d=D()

    Obj_d.PritntD()