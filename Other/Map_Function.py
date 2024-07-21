num=["1","2","3","4","5"]
print(num)

# map(int,num) --> Return The Object Type And We convert, Object To List Use list() "Function"
print(map(int,num))

#  Object To List Use list() "Function"
Map_Num=list(map(int,num))
print(Map_Num)

# create function for power The Number 
def pow(x) :
    return x*x

def cube(x):
    return x*x*x

pow_List=list(map(pow,Map_Num))
print(pow_List)

# We can Us lambda Function Because First Argument In the Map() Is Function And Lambda Is A function
Cube_List=list(map(lambda x : x*x*x,Map_Num))
print(Cube_List)

def num_1(x):
    return x

list_fun=[num_1,pow,cube]

# def fun_1(x) :
#     return x(i)

for i in range(5) :
    list_3=list(map(lambda x:x(i),list_fun))
    print(list_3)

# for n in range(5) :
#     list_4=list(map(fun_1,list_fun))
#     print(list_4)