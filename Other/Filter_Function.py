list_1=[1,2,3,4,5,6,7,8,9,10,11,12]
lambda x:x>5

def Is_Greaterthen_5(n) :
    return n>5

# for i in range(10) :
#     print(Is_Greaterthen_5(i))

Filter_1=list(filter(Is_Greaterthen_5,list_1))
print(Filter_1)