print ('Hello World\n')

i=0;
print("Welcome To The My Code, Enter The Code For Start The Window, You Have Only Five Chance")
while(i<5):
    a=int(input("Enter The Cood : "))
    i=i+1
    if a!=10:
        print("You Have",5-i,"Chance")
        if i==5:
            print("Sorry You Are Fail To Start The Window, It Mean You Are Not Prateek")
        continue
    if a==10:
        print("Hello MR. Prateek Yadav Ji, How Are You ")
        break