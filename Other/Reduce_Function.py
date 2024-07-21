from functools import reduce

def sum_1(x,y) :
    return x+y

list=[1,2,3,4,5,6,7,8,9]

num=reduce(sum_1,list)
print(num)