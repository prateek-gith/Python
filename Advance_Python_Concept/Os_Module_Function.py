import os

# it return the attribute which is store in os mudule, {Kya Kya khilwad kr sakte h yah btayega}
# print(dir(os))

# It Mean getcwd ==> Get Current Working Directory {Mtlb Jaha Pr Hm Current me Work Kr Rahe H}
# print(os.getcwd())

# We can change the Current Working Directory,  CHDIR ==> Change Directory
# os.chdir("C:/")
# print(os.getcwd())

# it Return The List Of Current Directoy Or Files
# print(os.listdir())

# WE Can Give The Path Name For Know All Fills Or Folder In Given Path
# print(os.listdir("c:/VS_CODE"))

# Create A New Folder In Current Directory Where We Working Corrently, MKDIR ==> Make Directory
# os.mkdir("AAAAAAAAA")

# Create Directory(Folder) Inside The Folder(Dirctory)
# os.makedirs("AAAA/BBBB")

# For Rename The Directory Or File Name
# os.rename("Advance_Python","Advance_Python_Concept")


# print(os.environ.get('path'))


# Join The Two Path In Optimal Way {It mena remove The Unnessery / Or Something...... }
# print(os.path.join("C:","Prateek.txt"))

# Know That Directotry(Folder) are Exist Or Not If Exist Return TRUE Otherwise FALSE
# print(os.path.exists("c:/"))

# It Return True When File Is Exist For Given Name , OtherWise False
# print(os.path.isfile("Mylog.txt"))

# It Return True When Folder Is Exist For Given Name , OtherWise False
# print(os.path.isdir("File_Handling"))

print(os.path.splitext("Mylog.txt"))
