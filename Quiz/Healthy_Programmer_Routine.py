from datetime import datetime
from time import time,sleep
from pygame import mixer

def Music_On_Loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    
    # While True Is Use For, Music Play Till Stop, When We Clik On The Stop Then It stop
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
        
def Log_data(MSG):
    with open("Mylog.txt",'a') as f:
        f.write(f"{MSG} : {datetime.now()} \n")
        
if __name__=='__main__':
    init_Water=time()
    init_Eyes=time()
    init_Exercise=time()
    Water_Second=2
    Eye_Second=20
    Exercise_Second=30
    while True:
        if time() - init_Water > Water_Second :
            print("Water Drink Time Enter 'ok' To Stop Alarm....")
            Music_On_Loop("c:/VS_CODE/Python/Quiz/Music.mp3","ok")
            init_Water=time()
            Log_data("Drank Water at")
            sleep(18)
            
        if time() - init_Eyes > Eye_Second :
            print("Eye Rest Time,  Enter 'ok' To Stop Alarm....")
            Music_On_Loop("c:/VS_CODE/Python/Quiz/Music.mp3","ok")
            init_Eyes=time()
            Log_data("Eye Rest at")
            sleep(10)
            
        if time() - init_Exercise > Exercise_Second :
            print("Water Exercise Time, Enter 'ok' To Stop Alarm....")
            Music_On_Loop("c:/VS_CODE/Python/Quiz/Music.mp3","ok")
            init_Exercise=time()
            Log_data("Exercise Start at")
            b=input("If you want to Quit Then Press 'Q' Otherwie Press Any Key : ")
            if b=="q" or b=="Q":
                break
            else:
                continue
            
        
            