list_1=input("Enter The List : ")
list_1=[i for i in list_1.split(" ")]
list_1=list(map(int,list_1))
print("My List is : ", list_1)

# First Method
# Using Build in function

#First We Create a Copy Of List Because reverse function Update the Original List
list_2=list_1[:]
list_2.reverse()
print("Using Build In Function Of List : ", list_2)

# Second Method
# Using String Slicing
list_3=list_1[::-1]
print("Using String Slicing : ", list_3)


# Third Method Using Custome function

def swap(l):
    list_4=l[:]
    length=len(l)
    for i in range(length):
        var1=l[i]
        var2=l[(length-1)-i]
        list_4[i]=var2
        list_4[(length-1)-i]=var1
    print("Using Custom function : ",list_4)
        

swap(list_1)
