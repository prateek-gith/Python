def Fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Fac(n-1)

def fab(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
    
print(Fac(10))
print(fab(10))

list=[1,2,3,4,5,6,7,8]

for i in list:
    print(i)