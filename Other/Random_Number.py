# it is use for generate number for anythink

import random
n = random.random()
print(n)


# it is use for, when we want to generate random number B/W The Number like : 1 to 100 
import random
n = random.randint(1,100)
print(n)

import random
#Generate List of 5 random numbers between 10 and 30
randomlist = random.sample(range(10, 30), 5)
print(randomlist)


# when We want to make own list and then want to choise random in The List then we use Choice Function Wich is build under the random function
list=["Prateek","Vishal","vaishali","Kuldeep","Sunita"]
ch=random.choice(list)
print(ch)