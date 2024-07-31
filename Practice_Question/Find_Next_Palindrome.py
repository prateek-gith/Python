def is_palindrome(num):
    if num[::-1]==num:
        return True
    else:
        return False

#it take Input As A String
def find_next_palindrome(num):
    #Typecast Into String
    number=int(num)
    
    # Add 1 For Serching Next Number 
    number=number+1
    
    #Again Convert Into String Becase Using String Slicing We can Easly Find The Reverse String And Check
    number=str(number)
    if is_palindrome(number)==True:
        print(f"Next Number {number} is palindrome")
    else:
        # recursion 
        find_next_palindrome(number)
        



a=input("Enter The Number or String : ")
if a.isalpha()==True:
    if a[::-1]==a:
        print("String Is palindrome")
elif a.isnumeric()==True:
    find_next_palindrome(a)
else:
    print("String Is Wrong")
