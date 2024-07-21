list_1=["Prateek","Vishal","Vaishali","Kuldeep","Suita","Ishika"]

# print(list_1[::2])
# this is without enumerate function
# without enumerate we declear a index number (i=0) and need to increment (i=i+1)

# i=0
# for item in list_1:
#     if i%2==0:
#         print(f"The Item Is : {item}")
#     i+=1


# This Is enumerate function
# enumerate Automatic give index And item and auto incremnt
for index,item in enumerate(list_1) :
    if index%2==0:
        print(f"The Item Is : {item}")