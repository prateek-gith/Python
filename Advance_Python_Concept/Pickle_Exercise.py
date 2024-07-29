# import requests
import pickle

f=open("iris.data",'r')
data=f.read()
data2=data.split("\n")

# print(data2)
print(type(data2))

# with open ("Pickle_Exercise","wb") as write_file:
#     pickle.dump(data2,write_file)
    
# with open ("Pickle_Exercise","rb") as Read_File:
#     print(pickle.load(Read_File))
    
f.close()


# this is one line code of list append whis done in four line thas call comprihension
list=[item.split(",") for item in data2 if len(item)!=0]

print(list)