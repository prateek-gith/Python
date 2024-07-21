a=int(input('Enter The Age : '))
# b=int(input('Enter The Value Of B : '))


if a<18:
    print("You Can't Drive")
elif a==18:
    print("Please Go To RTO And Take Your Licence And Then Drive")
elif a>18:
    if a<70:
        print("You can drive")
    else:
        print("invalid")
else:
    b=input("You Have Dl : ")
    if b=='yes':
        print("You Can Drive")
    else:
        print("You Can't Drive")
print("\nThanqu")