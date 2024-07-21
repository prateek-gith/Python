import time

# here no parameter is passed
print(time.strftime("%H:%M:%S"))

print(time.time())
print(time.localtime(time.time()))
loc_tm=time.asctime(time.localtime(time.time()))
print(loc_tm)


# time.time() --> calculate the time as a number 
# time.localtime(time.time())--> convert to locals time which is retur from "Time.time()" 
# time.asctime(time.localtime(time.time())) --> it covert to the readable format which is return from "time.localtime(time.time())"
