def find_mul(numbers):
        num=[i for i in numbers.split(" ")]
        numb=list(map(int,num))
        result = 1
        for nums in numb:
            result = result * nums
        return result
    
print(find_mul("1 2 3 4 5"))