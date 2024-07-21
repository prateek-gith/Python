f=open("c:\VS_CODE\Python\File_Handling\prateek.txt")
# We Can use ".tell()" function for knowing the file pointer position 
# it mean ".tell()" function tell that Where is file pointer and give the index Number where is file pointer
print(f.tell())

# ".readline()" function is use for the fetch the text in line 
# ".readline()" function print one line at a time 
print(f.readline())
print(f.tell())

print(f.readline())
print(f.tell())

# when we want to reset the file pointer position 
# and we want to jump file ponter position then we use the ".seek()" function
# and we set the position where jump our file pointer
f.seek(0)
print(f.tell())
print(f.readline())

f.seek(26)


# ".readlines()" function convert the file text into list format
print(f.readlines())

print(f.readline())
f.close()
