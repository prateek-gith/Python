a=10 
# Global Variable & Scope Of Global Variable Is Till The Program Execute
# We can Use Global Variable Value Till The Program Run & Execute (Also use Inside The Any Block (Function))

def fun_1(n):
    a=20 
    # Local Value Of Function & Scope Of Local Value Is Till The Function Is Call Or When Function Call
    # We Can Use Local Variable Value Only Inside The Block (Function), We Can't Use Outside The Bloc (Function)
    print("The Value You Enterd Is : ",n)
    print("This Is Local Value Of Function Is : ",a)

b=int(input("Enter A Number : "))
fun_1(b)

print("This Is Global Balue Of A is : ",a)

# If In A program Local & global variable Name Is Same (Like A=10) 
# Then In The Block Or Function Give The Most Preority of Local Variable 