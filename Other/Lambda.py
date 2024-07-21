print("Lambda function")

# lambda Function is Like A short Hand Function Or One Liner Function
#  It Is Also Called Ananymous Or Lambda Function

# It Same work As Simple function Work

def sum(x,y):
    return x+y

sum_l=lambda x,y : x+y

print("Sum Using Lamda Function : ",sum_l(20,25))
print("Sum Using Function : ",sum(10,20))