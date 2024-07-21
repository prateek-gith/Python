# 1. List Comprehensions

"""
# create a list Which Is Divisible For 2 With Simple Loop 
List_1=[]
for i in range(10):
    if i%2==0:
        List_1.append(i)

print(List_1) 

"""

# create a list Which Is Divisible For 2 With List "Comprehensions Method"
list_2=[i for i in range(10) if i%2==0]
print(list_2)


# Dictionery Comprehensions
"""
DIct_1={}

for i in range(10):
    DIct_1.update({i:f"Item_{i}"})

print(DIct_1)

"""
Dict_2={i:f"Item_{i}" for i in range(10)}
print(Dict_2)

# when We Reverse the Dictiobery Like First Value And Second Key
Dict_Rev={Value:Key for Key,Value in Dict_2.items()}
print(Dict_Rev)

# Generator Comprehensions
"""
def Gen(n):
    for i in range(n):
        if i %2==0:
            yield i

Gen_1=Gen(10)
print(next(Gen_1))

for value in Gen(10):
    print(value)

"""

Gen_Com=(i for i in range(10) if i%2==0)

for value in Gen_Com:
    print(value)