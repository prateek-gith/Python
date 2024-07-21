print("Split a string into a list where each word is a list item")
# Mtlb Jitni Bhi Value/String/Word Hai is Poori String me Use Vo Ek List Ke Roop Me Bna dega 
print("First Type")
a = "welcome to the jungle"
print("\n",a)
print(a.split())

print("second Type")
b = "hello, my name is Peter, I am 26 years old"
# iska mtlb hai ki split yani list/devide kar do jaha jaha (,) laga hua hai 
print("\n",b)
print(b.split(","))

print("Third Type")
c = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
# iska mtlb hai ki string me pahle dhoondo # kaha kaha hai fir next value di gyi h 1 yani pahle jaha mil jaye bs utne ke pahle ek list value uske bad ek bs
print("\n",c)
print(c.split("#",1))
