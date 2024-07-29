# == : value equality -- two object have same value
# is : refrence equality -- two refrence hsve same value

a=[1,2,3,4,5,6,1,2]
b=a  # b point to a object/refrence -- it mena when we change a then b is also change and when we change b then a also change

a[6]=7
b[7]=8
print("A Is : ", a, "  B Is : ",b)
c=[1,2,3,4,5,6,7,8]

print(b == a)
print(b is a)

print(c==a)
print(c is a)

d=a[:] # create copy of a and store in d -- it mena when we change the a then d did not change
d[1]=0 
print("A Is : ",a, " D Is : ",d)
print(c is a)