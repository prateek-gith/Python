print("The range() function returns a sequence of numbers, starting from 0 by default")
print("and increments by 1 (by default), and ends at a specified number")
# range function same as condition a is By Defalt 0 Value And By Using range() function
# python increments of value by defalt 1 after Every Excution 
# and (6) It Mean loop excutute till a<6
print("\n\t same as -->> for(int a=0;a<6;a++)")
for a in range(6):
  print(a) 

print("\n \n")

print("\n\t same as -->> for(int a=1;a<20;a++)")
for b in range(1,20):
  print(b)

print("\n \n")

print("\n\t same as -->> for(int a=2;a<20;a=a+2) '  mean increment of a is 2 after every exicution")
for b in range(2,20,2):
  print(b)