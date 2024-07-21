a=[["prateek",6],["vishal",7],["vaishali",8],["kuldeep",9],["sinita",10]]

# The Loop Execute Again And Again till Key/Item Are Not End
for key,value in a:
    print("The Key Is : ",key,", And its Value Is : ",value)


b=[["prateek",6],["vishal",7],["vaishali",8],["kuldeep",9],["sinita",10]]
dic=dict(b)

for key,value in dic.items():
    print("The Key Of Dictionry IS : ",key,",And Value Of Dictionry Item Is : ",value)

# For Dictionery "["prateek",6]" it Whole Is Item 
print(dic.items())

#for Only Items print We Can Use 
for item in dic:
    print(item)