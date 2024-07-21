import math
a=input('Enter Your Name : ')
b=input('Enter Your Code Choice like Python,c,java, Etc : ')

# type 1 : This Is Called String Formating or format String
c="Hi Mr/Mrs. : %s Welcome To Prateek Code , \n You Are Also Intrested in, %s Wow I Like It"%(a,b)

print(c)

# type 2 : This Is Called String Formating or format String
d="Hi Mr/Mrs. : {} Welcome To Prateek Code , \n You Are Also Intrested in , {} Wow I Like It"
e=d.format(a,b)
print(e)

# type 3: 
# This Is Called "f String"  = fast String 

f=f"Hi Mr/Mrs. : {a} Welcome To Prateek Code , \n You Are Also Intrested in , {b} Wow I Like It"

print(f)

print(f"The power Of 2^6 is {math.pow(2,6)}")