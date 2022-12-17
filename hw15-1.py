#HW15-1, 12/16/2022
#Chaning 24 hour to 12 hour time.
#***************************************
class Time:
    def __init__(self, hour, minu, sec):
        self.hour = hour
        self.minu = minu
        self.sec = sec
    #**********************************
    def changeTime(self):
        if self.hour>12:
            h=str(self.hour-12)
            print(h.zfill(2), ":",end="")
        else:
            h=str(self.hour)
            print(h.zfill(2),":",end="")
            
        m=str(self.minu)
        print(m.zfill(2),':',end="")
        
        s=str(self.sec)
        print(s.zfill(2),end="")
        
        if self.hour>12:
            print(" pm")
        else:
            print(" am")
#*******************************************    
time=Time(9,5,5)
time.changeTime()