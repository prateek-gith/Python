print("Hello World\n")

a="My_Name_Is_Prateek_Yadav"
b="MY_NAME_IS_VISHAL_YADAV"
c="my_name_is_vaishali_yadav"
d="P\tR\tA\tT\tE\tE\tK"
e="For only {price:.2f} Rupees"

print(c.capitalize())       #   capitalize Fist Char of String
print(b.casefold())         #   Convert In Lower Case 
print(a.center(50))         #   Give The Distance/Move From Left Side
print(a.count("a"))         #   Count The Frequency of Given Char
print(a.encode())           #   Encoding The Ant Diff Char. Otherthan English Language
print(a.endswith("av"))     #   If String end WIth Given Char (" ") Then It return True Otharwise False
print(d.expandtabs(3))      #   if We Use In String \t, Then It Give Tab b/w Char where we use \t and (3) it mean give two Char. Tab 
print(d)                    #   If we Use the \t, than give tab b/w char where we use 
print(a.find("P"))          #   This Is use For Find The given Char. In Given String, It Return Index Value, Where (" ") Chr. Is store
print(a.find("p"))          #   if It Not Found The (" ") Char. Then It Return -1 or Garbage Value
print(e.format(price = 49)) #   it Give The Value OR Replace The value which is use in string in {name : } and same use in farmat(name=value) it replace in string name ki jagah value likh dega 

print(a.lower())
