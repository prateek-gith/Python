a=10

try :
    f=open("c:/VS_CODE/Python/Advance_Python/prateek.txt","r")
except Exception as e:
    print(e)
else:
    print("File Is Successfull Open")
    a=f.read()
    print(a)
finally:
    print("ittretionn is done")
    f.close()