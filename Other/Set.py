print("It Is A set")
a=set({1,2,3,4,5,6,7,8,9})
b=set({3,4,5,6})
print(type(a))              # For Printing Type Of Set a
print(a)
a.add(9)                    # For Adding Any New Element In Set
print(a)
a.remove(9)                 #  For Removing Element In Any Set
print(a)
print(a.intersection(b))    #   For intersection (Common Element In Both Set)
print(a.union(b))           #   For Add Both Set
print(len(a))               #   For Print The Length Or Element Of Set