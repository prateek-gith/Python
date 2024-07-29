f=open(r"c:\VS_CODE\Python\File_Handling\prt.txt","w")
f.write("My Name Is Prateek yadav")
f.close()

c=open(r"c:\VS_CODE\Python\File_Handling\prt.txt")
a=c.read()
print(a)
f.close()