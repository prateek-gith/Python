print("TYPE 1")
print ('Without Argument With Return Value\n')

def Sum():
    a=int(input('Enter A Number : '))
    b=int(input('Enter B Number : '))
    return a+b

v=Sum()
print("The Sum Is ",v)

print("TYPE 2")
print ('\n\nWithout Argument Without Return Value\n')

def Sum1():
    a=int(input('Enter A Number : '))
    b=int(input('Enter B Number : '))
    print("The Sum ",a+b)

Sum1()

print("TYPE 3")
print ('\n\nWith Argument Without Return Value\n')

def Sum2(a,b):
    print("The Value Of A is : ",a)
    print("The Value Of A is : ",b)
    print("The Sum ",a+b)

Sum2(4,5)


print("TYPE 4")
print ('\n\nWith Argument With Return Value\n')

def Sum3(a,b):
    """ This Function Calculate The Sum Of Two Number Which Is Given By User"""
    return a+b

c=int(input('Enter A : '))
d=int(input('Enter B : '))
p=Sum3(c,d)
print("The Sum Is : ",p)

# .__doc__ function is use for print the comment or docstring which is define inside the function
print("\n\n",Sum3.__doc__)