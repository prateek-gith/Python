a=int(input('Enter The First Number : '))
b=int(input('Enter The Second Number : '))
c=input("Select Your Operator (*,%,/,+) : ")
if c=='*':
    print("A*B = ",a+b)
elif c=='+':
    print("A+B = ",a*b)
elif c=='/':
    print("A/B = ",a-b)
elif c=='%':
    print("A%B = ",a%b)
else :
    print("You Enter Wrong Operator")
print("\n ThankYou For Using Calculator")