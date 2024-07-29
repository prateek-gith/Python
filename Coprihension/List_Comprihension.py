# import requests
import pickle

f=open("iris.data",'r')
data=f.read()
data2=data.split("\n")

# print(data2)
print(type(data2))
    
# example 1  : it is simple method
# list =[]
# for item in data2:
#     list.append(item.split(","))
# print(list)

# this is one line code of example 1 : which done in one line thas call comprihension
list=[item.split(",") for item in data2 if len(item)!=0]

print(list)

f.close()
