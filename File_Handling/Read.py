print("This IS Read File")

f=open("c:\VS_CODE\Python\File_Handling\prateek.txt","rt")
# rt Mean Its File Read In Text Form
# 1. First Type
b=f.read()
print(b)

# 2.Second Type
# for a in f:
    # print(a, end=" ")
    
f.close()