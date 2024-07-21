print("Remove The space/value, Three Type Of Strip Fuinction")
print("1. lsplit() --> it use to remove space/value From Left Side")
print("2. rsplit() --> it use to remove space/value From Right Side")
print("3. split() --> it use to remove space/value From Both Side\n")
print("Remove spaces/value to the left of the string:")

a= "     banana     "

#x = a.lstrip()

print("\n1. of all fruits", a.lstrip(), "is my favorite")
print("\n2. of all fruits", a.rstrip(), "is my favorite")
print("\n3. of all fruits", a.strip(), "is my favorite")

print("\nRemove the leading characters:")

b= ",,,,,ssaaww.....banana"

y = b.lstrip(",.saw")
print(y)

