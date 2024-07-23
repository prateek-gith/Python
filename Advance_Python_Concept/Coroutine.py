import time

def searcher():
    f=open("c:/VS_CODE/Python/Advance_Python/prateek.txt","r")
    a=f.read()
    time.sleep(4)
    
    while True:
        text=(yield)
        if text in a:
            print(f"{text} : is founded")
        else:
            print(f"{text} : is Not Founded")

search=searcher()

next(search)

search.send("Prateek")