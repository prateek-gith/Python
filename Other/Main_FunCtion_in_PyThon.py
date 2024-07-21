def Add_Two_Num(a,b):
    c=int(a)+int(b)
    print(f"The Sum Of {a},{b}",c)

def Mul_Two_Num(a,b):
    c=int(a)*int(b)
    print(f"Multiplication Of {a}, {b}",c)

# it return the the name of file
# if return main it mean code run in through current file function
# otherwise return file name where function is run
print("The Name Is Where Code Run : ",__name__)



# if __name__=='__main__': Work Like A Main Function As "int Main()" Work In c And C++
# if We import this File To Another File And Use The Funtion of import's File Then only Function Is Run 
# it Mean No Run Unnessry code, which is only current File Code, And Another File We dont't Want To Excute Other(unnessery) Code
if __name__=='__main__':
    # and it Mean if name==main then execute the program which is written under the "__name__=='__main__':"
    Add_Two_Num(20,30)
    print("My Name Is Prateek Yadav")