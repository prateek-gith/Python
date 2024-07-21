print("Search for the last occurrence of the word 'bananas', and return a tuple with three elements:")
# Search ki gyi string ya charcter ho main string me search karta hai
# fir last vali value jo match ho rahi hai use dhoondkar vahi se teen bhago me devide kar deta hai
# jaise jaha par last value mili uske pahle ek partition or fur dosra partion jo search kiya hai fir 3 partion usko search karne ke bad
print("1 - everything before the 'match'")
print("2 - the 'match'")
print("3 - everything after the 'match'\n")

a = "I could eat bananas all day, bananas are my favorite fruit"
print(a)

x = a.rpartition("bananas")

print(x)