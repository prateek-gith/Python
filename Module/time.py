import datetime
# import time
def gettimet():
    return datetime.datetime.now()

print(gettimet())


# print(datetime._Date())
# print(datetime.time())

def user():
    a=input('Enter The Clint Name : ')
    if a=='Aman':
        b=int(input("Enter What is Known Like Dyed, Food \n 1.for Dyed \n 2.For Health : "))
        if b==1:
            c=int(input(" 1.For All \n 2. For particular Day : "))
            if c==1:
                f=open("c:\VS_CODE\Python\prateek.txt",'r')
                d=f.read()
                gettimet()
                print(d)
                # for line in d:
                #     print(line)
            elif c==2:
                f=open("c:\VS_CODE\Python\prateek.txt",'r')
                d=f.read()
                f.seek(11)
                print(f.readline())



# user()