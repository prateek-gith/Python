# import Main_FunCtion_in_PyThon as mf

# mf.Add_Two_Num(10,20)

    
# for i in range (5) :
#     print(lambda x:x(i))
# y=lambda x:x*x
# print(y(10))

# import Lambda
# print(Lambda.sum(10,20))

list_1=[]
a=int(input('How Many Value You Want To Enter : '))
for i in range(a):
    a=int(input(f"{i} Enter The Value : "))
    list_1.append(a)

# print(list_1)

b=int(input('Which Type Of Comprehensions You Want\n1.For List Comprehension\n2.For Dict_Comprehensions'))
if b==1:
    List_Com=[value for value in list_1]
    print(List_Com)
elif b==2:
    Dict_1={Value:f"Item_{Value}" for Value in list_1}
    print(Dict_1)
    c=int(input("If You Want Print Return In Reverse Order Then Press 1 : "))
    if c==1:
        Dict_Res={Value:Key for Key,Value in Dict_1.items()}
        print(Dict_Res)
    else:
        exit()
else :
    exit()