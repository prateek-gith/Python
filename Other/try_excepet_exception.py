a=input('Enter The Number A : ')
b=input('Enter The Number B : ')

try:
    print("sum of number A+B : ",int(a)+int(b))
    # print("sum of number A+B : ",(a+b))
except Exception as a :
    print(a)

print("This Line print After Using try except exception")