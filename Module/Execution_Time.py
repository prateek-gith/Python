import time
initial =time.time()
print(initial)

a=0
while(a<50):
    print("prateek")
    a=a+1

Second_Time=time.time()
Second_Time_ex=(time.time()-initial)
print(Second_Time_ex)

for i in range(0,50,1):
    print("Yadav")

third_time=(time.time()-Second_Time)
print(third_time)