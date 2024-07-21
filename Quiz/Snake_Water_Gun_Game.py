import random

li=["Snake","Water","Gun"]
a=0
e=0
d=0
print("Welcome To The Snake Water Gun Game")
print("The Game Run Five Time!!\n")
    
while a<10 :
    b=input('\nEnter Your Choice Snake, Water, Gun : ')
    b=b.capitalize()
    c=random.choice(li)
    print("Computer Choos : ",c)
    if c==b :
        print("Tai")
        a=a+1
        print(f"Current Score Your : {e}, Computer : {d} \n")
        print("Remaining Time",(10-a))
    elif c=="Snake" and b=="Water" :
        print("Computer Win")
        d=d+1
        a=a+1
        print(f"Current Score Your : {e}, Computer : {d} \n")
        print("Remaining Time",(10-a))
    elif c=="Water" and b=="Snake" :
        print("!!!You Win!!!")
        e=e+1
        a=a+1
        print(f"Current Score Your : {e}, Computer : {d} \n")
        print("Remaining Time",(10-a))
    elif c=="Snake" and b=="Gun" :
        print("!!!You Win!!!")
        e=e+1
        a=a+1
        print(f"Current Score Your : {e}, Computer : {d} \n")
        print("Remaining Time",(10-a))
    elif c=="Gun" and b=="Snake" :
        print("Computer Win")
        d=d+1
        a=a+1
        print(f"Current Score Your : {e}, Computer : {d} \n")
        print("Remaining Time",(10-a))
    elif c=="Water" and b=="Gun" :
        print("Computer Win")
        d=d+1
        a=a+1
        print(f"Current Score Your : {e}, Computer : {d} \n")
        print("Remaining Time",(10-a))
    elif b=="Water" and c=="Gun" :
        print("!!!You Win!!!")
        e=e+1
        a=a+1
        print(f"Current Score Your : {e}, Computer : {d} \n")
        print("Remaining Time",(10-a))
    else :
        print("Something Went Wrong!!")
        break

print(f"The Current Scoore Is : \n Computer Win {d} time \n You Win {e} Time!!")
if d==e :
    print("\nMatch Tai")
elif d>e :
    print("\nComputer Win!!")
else :
    ("\nYou Win")

print("\nThanqu For Playing The Game Viit Again")