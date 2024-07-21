print("This Function Is Use To Short The List With Specific Value There are three Type")
print("1. Sort the list alphabetically When We Use only sort()")
print("2. We Can Use Short Method By Using (reverse=true) It Mean First reverse alfabetically The Sting If It Is posible")
print("3. We Can Use The function for sort the list, which value function returns")
# 3. mtlb ki function ke hisab se list ko sort akreg jise thisd Type me hmne lenth ko function me return kiya hai to list length ke according sort hogi

print("First Type")

cars1 = ['Ford', 'BMW', 'Volvo']
print("\nThe List Is : ",cars1)

cars1.sort()
print("After Using sort() Function ",cars1)


print("\n2. Second Type")
cars2 = ['Ford', 'BMW', 'Volvo']
print("\nThe List Is : ",cars2)

cars2.sort(reverse=True)
print("After Using sort(reverse=True) function",cars2)


print("\n3. Third Method")

print("\n3.1 Method")
print("A function that returns the length of the value & This List Short according To The length")
def myFunc1(e):
  return len(e)

cars3 = ['Ford', 'Mitsubishi', 'BMW', 'VW']
print("The List Is : ",cars3)
cars3.sort(key=myFunc1)

print("After Using function sort with length ''usning function''",cars3)

print("\n3.2 Method")
print("A function that returns the year & This List according To year ")
def myFunc2(e1):
  return e1['year']

cars4 = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

print("The List Is : ",cars4)
cars4.sort(key=myFunc2)

print("After Using function sort With year ''using function'' ",cars4)
