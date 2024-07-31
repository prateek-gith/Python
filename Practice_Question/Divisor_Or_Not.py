if __name__=='__main__':
    apple=int(input("Enter The Number Of Apple : "))
    minmum=int(input("Enter The Min Number Of Student : "))
    maxmum=int(input("Enter The Max Number Of Student : "))
    
    for i in range(minmum, maxmum+1):
        if minmum==maxmum:
            print("This Is Not A range")
        elif apple%i==0:
            print(f"{i} divisor of {apple}")
        else:
            print(f"{i} is not divisor of {apple}")
    