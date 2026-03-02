# class User:
#     def __init__(self,username):
#         self.username=username

#     def login(self):
#         print(f"{self.username} login")

# class admin(User):
#     def deletuser(self):
#         print("deleted succes fully")

# u=admin("shivu")
# u.login()

class notification():
    def send(self):
        pass
class emailenoti(notification):
    def send(self):
        print("email notifi")

class smss(notification):
    def send(self):
        print("sms notificaton ")

notificatin = [emailenoti(),smss()]
for notifi in notificatin:
    notifi.send()
