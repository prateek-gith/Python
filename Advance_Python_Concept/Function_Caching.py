import time 
from functools import lru_cache

# we give maxsize that is understand store the function valure from last maxsize
@lru_cache(maxsize=2)
def some_work(n):
    #Some Work Is Happen In This Line/ Me be Fie Read Or Many Work/ which is taking some time 
    time.sleep(n)
    return (n)
    # print(n)

if __name__=='__main__':
    print("Now Running........ Some Work")
    some_work(3)
    print("First Work Done")
    
    some_work(4)
    print("Second Work Is Done")
    
    some_work(3)
    print("Third Work Done")
    
    some_work(5)
    print("Fourth Work Is Done")
    
    some_work(4)
    print("Fift Work Is Done")
    
    some_work(3)
    print("Six Work Is Done")
    
# in first Ittresion some_work() Store The some_work(3), second ittresion store some_work(3) And some_work(4), in third ittretion store some_work(4) And some_work(3), fourth ittresion store some_work(3) and some_work(5), In fift ittresion store some_work(5) And some_work(4), in six Ittresion store some_work(4) And some_work(3)
    
