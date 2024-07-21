print("continue statement we can stop the current iteration of the loop, and continue with the next")
print("Do not print banana")
fruits = ["apple", "banana", "cherry"]
for key in fruits:
  if key == "banana":
    continue
  print(key) 
