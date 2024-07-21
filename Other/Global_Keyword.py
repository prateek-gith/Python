a=10 

def fun_1(n):
    # When We Want to Change The Value Of Global Variabl Then We want Use The Keyword => "Global"
    # "global" keyword Give The permission to Block Or Function To Change The Value Of global variable
    # Without "global" We Can't Change The Value Of Global Variable Inside The Block 
    # Outside The Block We Can Easly Change The Value Of Golbal Variable Like A=10
    global a
    a=50
    print("The Value You Enterd Is : ",n)
    print("This Is Local Value Of Function Is : ",a)

b=int(input("Enter A Number : "))

fun_1(b)

print("This Is Global Value Of A is : ",a)



# when We don't Declear a Global variable & We Create A local variable in block (Function)
# and With in the function (fun_1) we create a new function (fun_2) and then use 'global x' for change the ----
# globle variable value then it search in the global if it doen't find the x varibale then it create the x value 
# which decleare inside the fun_2 it is called local variable global ,outside the block or function
x=10
def fun_2():
    x=20
    def fun_3():
        global x
        x=22
    # print("Before calling fun_3 x = ",x)
    fun_3()
    print("After calling fun_3 x = ",x)

fun_2()
print(x)