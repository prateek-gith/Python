a="Prateek_Is_a_Good_Boy"

print(a)

# It Is Use For The Find And Pring Indexing Value 
# Like We Give 0:7 It Mean index 0 to 6 in This Index Print Character 
# First 0 is including OR 7 Is Excluding 
print(a[0:7])


# It Is Use For Give Gap In Fetch String 
# Last Value Is Denoded The Gap B/W Character 
# Like 2 it denodet in Gap B/W Two Character
print(a[0:7:2])

#matlb Last Vale Column Me Jo Bhi Value Di Gyi h Usme Se Ek Kam karke Yani 4-->4-1=3 Charcater Skip Kar do
print(a[0:7:3])
print(a[0::4])

# It Take string Inreverse Formt 
# Lat Index Is -1,-2,-3,-4-------etc.
print(a[-8:-2])

# Fist - in last Colon It Meat It Reverse All String Like Prateek TO keetarp 
# The Skip Which Value We Give For Skip
print(a[::-1])

print("\nFunction Of Sting\n")

# It Give only True And False Value Because It Work On Boolean Function
# endwith("Char/String")  Mean End Of String Char. Is "charcter/String"
print(a.endswith("Boy"))

# This Function Use For Count The Given Character How Many time It Char Is Use 
# It Is Use The Check The Frequency Of Given Character
print(a.count("o"))

# This Function Is Use FOr Caplize First String Charater 
print(a.capitalize())

# This Function Is Use For Fide The Character In Strin 
# It Give Index Value Where Character Is Started 
# If Character or String not Found Then It Retur The Value -1
print(a.find("Is"))

# This Function To Use Convert The whole String In Lower Form
print(a.lower())

# This Function Is Use To Conver Whole String In Upper Case 
print(a.upper())

# This Function Is Use To Replace The Caracter in New Charcte 
print(a.replace("Is","Are"))