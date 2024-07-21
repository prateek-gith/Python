print("This List Function Is Use To Add/Catenate Two List or tuple List")

fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

print("The First List Is : ",fruits)
print("The Second or Tuple List Is : ",points)

fruits.extend(points)
print(fruits)