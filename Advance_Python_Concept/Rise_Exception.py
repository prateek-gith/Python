# Python raise Keyword is used to raise exceptions or errors. The raise keyword raises an error and stops the control flow of the program. It is used to bring up the current exception in an exception handler so that it can be handled further up the call stack.

# Custom Exception Which Is Written By Coder/Programer
# a = 5

# if a % 2 != 0:
# 	raise Exception("The number shouldn't be an odd integer")
    # print("The number shouldn't be an odd integer")
    
# print("When We Use Only Print Then Further Next Code/ittresion Is Run, But When We Rise Exception Then Programe Give A Error And Stop Further Next ittretion")


# We Use Custome Error In TRY Exception 
s = 'apple'

try:
	num = int(s)
except ValueError:
    print("String can't be changed into integer")
	# raise ValueError("String can't be changed into integer")

print("When We Use Only Print Then Further Next Code/ittresion Is Run, But When We Rise Exception Then Programe Give A Error And Stop Further Next ittretion")
