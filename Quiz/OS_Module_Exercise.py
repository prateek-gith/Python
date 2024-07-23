import os

# My solution
# def Detail(path,format):
#     os.chdir(path)
#     File_List=os.listdir()
#     n=1
#     for i in File_List:
#         if os.path.isfile(i)==True :
#             if i.split(".")[1]==format:
#                 os.rename(i,f"{n}.{format}")
#                 n=n+1
#             else:
#                 os.rename(i,i.capitalize())
#         else:
#             os.rename(i,i.capitalize())
        
    
    
# if __name__=='__main__':
#     Detail("C:/Users/hp/Desktop/Pythons","jpg")
    
    
    
# Correct Solution    
def Detail(path,file,format):
    os.chdir(path)
    File_List=os.listdir()
    n=1
    with open (file) as f:
        file_list=f.read().split("\n")
    
    # print(file_list)
    
    for i in File_List:
        # print(i)
        # os.rename(i,i.lower())
        if i not in file_list:
            # print(i)
            os.rename(i,i.capitalize())
        if os.path.splitext(i)[1]==format:
            os.rename(i,f"{n}{format}")
            n=n+1
    
    
if __name__=='__main__':
    Detail("C:/Users/hp/Desktop/Pythons","C:/Users/hp/Desktop/Pythons/files.txt",".jpg")

    