def calculate_age(number):
    if number<100 and number>1:
        less_age_from_100=100-number
        print(f"You Will Become 100 After {less_age_from_100} Year")
    else:
        print("Your age is not valid ")
    
def calculate_dob(number):
    if number<2024 and number>1924:
        current_age=2024-number
        print(f"Your Age Is {current_age}")
        calculate_age(current_age)
    else:
        print("Your DOB is not valid")

if __name__=='__main__':
    age=input("Enter Your Age Or Date Of Birth : ")
    
    lenghth_of_age=len(age)

    age=int(age)
    
    if lenghth_of_age<=2:
        calculate_age(age)
    elif lenghth_of_age>2:
        calculate_dob(age)
    else :
        print("something Went Wrong")
    