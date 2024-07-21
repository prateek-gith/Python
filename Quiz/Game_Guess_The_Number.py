print ('Hello World\n')
i=0
while(i<10):
    a=int(input("Enter The Number : "))
    i=i+1
    if a!=10:
        print("SORRY, Wrong Number, You Have",10-i,"Chanses")
        if i==10:
            print("You Loose The Game! \nGame Over!")
        elif a<10:
            print("Hint : Increase Your Number\n")
        else:
            print("Hint : Decrese Your Number\n")
        continue
    if a==10:
        print("Congratulation!!!\nYou WIN!!\nYou Enter Right Number!")
        break