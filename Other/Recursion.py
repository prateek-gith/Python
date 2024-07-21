def fac(n):
    if n==1 :
        return 1
    else :
        return (n*fac(n-1))
    

def fab(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else : 
        return fab(n-1)+fab(n-2)



a=int(input("Enter A Number, For Factorial : "))

n=fac(a)

print("The Factorial of",a, " is ",n)

for a in range(0,a,1) :
    print(fab(a))

print("\n")
print(fab(a))



# when we only search the factoial then it return the factotial of number
# but in the series when search the factorial then it return the factioal of of number  which is currently preset in the index 
# like the the factoral of 6 is 8  then it return 8
# but in the series the in the sixth index is 5 then it return 5