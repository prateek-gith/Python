print("Hello World\n")

a="My_Name_Is_Prateek_Yadav"
b="MY_NAME_IS_VISHAL_YADAV"
c="my_name_is_vaishali_yadav"
d="P\tR\tA\tT\tE\tE\tK"
e="For only {price:.2f} Rupees"
f="1234"
g="\u00b3"
h="    "

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
print(a.index("P"))         #   It Give The Index Value Where (" ") Charcter Is Start Or Store
print(a.isalnum())          #   It Return True Or False Only If Either Alpha Or Numeric value in The String It Return True Otherwise if  symbole (@) or Space ( )are use in string then return False
print(a.isalpha())          #   It Return True If All String Is Only base on Alphabet it Not Allow Any Symbol if any symbol or number are use then it return False
print(a.isdecimal())        #   It Return Trure If All String is Only Base On Numeric(0-9) otherwise false
print(g.isdigit())
print(a.isnumeric())        
print(a.isascii())          #   It Return True if all the characters are ascii characters (a-z).
print(a.isidentifier())     #   It Return True If String Like Identifire Oterwise false, Like String Start With numners(0-9) and We use Space ( ) in String Thet It Return False It Mean This Istring Is Not Like A Identifire
print(c.islower())          #   It Return Trure If All String Written In lowerCase
print(b.lower())            #   It Convert String In Lower Case
print(a.isprintable())      #   It Return True If String Is Printable Otherwise Is Return false Like We Use \t,\n and Print the Value Of d (In This Program "(d.isprintable())" ) then It return False
print(h.isspace())          #   It Return True If String Store Only space (" ")  
k="\u265E"
print(k.encode("utf-8"))

