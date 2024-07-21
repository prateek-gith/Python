def fun_1(x,y) :
    return x+y

# fun_2=fun_1         # We Can Create The Copy Of Function (Fun_1) to (fun_2)
# # del fun_1         # this Is Use For delete the Function       After The Delete We Are Unable To Use Def_1 
# a=fun_1(4,5)
# print(a)


# b=fun_2(4,5)
# print(b)


# def fun_11(x):
#     print(f"This Is : {x}")

# def new(func) :
#     func("prateek")

# new(print)


def deco(fun_12) :
    def deoce() :
        print("Start")
        fun_12()
        print("End")
    return deoce()



# @deco
def my_Dec() :
    print("My Name Is Prateek")


my_Dec=deco(my_Dec)
my_Dec