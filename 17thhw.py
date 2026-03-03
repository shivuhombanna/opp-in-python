class phone:
    def __init__(self,call_cont,tack_pic):
        self.call_cont=call_cont
        self.tack_pic=tack_pic
        
    def calling(self):
        print(f"calling is {self.call_cont}")

    def tackpic(self):
        print(f"tacking pic {self.tack_pic}")

call=phone("7568767278","vivo.img")
call.calling()
call.tackpic()

class vechile():
    def __init__(self,bick_name):
        self.bick_name=bick_name

    def raid_vei(self):
        print(f"vechile name {self.bick_name}")

class bick(vechile):
    def raid(self):
        print("bick is raid is start ")

raid=bick("Splendar")
raid.raid_vei()
raid.raid()

class Shape():
    def send(self):
        pass
class circl(Shape):
    def send(self):
        print("this is circl")

class rectangal(Shape):
    def send(self):
        print("rectangal")



notificatin = [circl(),rectangal()]
for notifi in notificatin:
    notifi.send()



    
        