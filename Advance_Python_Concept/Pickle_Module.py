import pickle


obj=["Prateek","Yadav","Shuklaganj"]

# create/write a file in write binary form
# file=open("mypickle","wb")

# store in file into binary code
# pickle.dump(obj,file)

# close the file
# file.close()

# open file in read binary form
file_read=open("mypickle","rb")

# get/ read file in binary form and conert into object
myobjpkl=pickle.load(file_read)

# print object
print(myobjpkl)

# print type of object
print(type(myobjpkl))