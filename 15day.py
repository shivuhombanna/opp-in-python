#first program
class phone:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"brand{self.brand} model:{self.model}")

my_phone=phone("samsung","a32")
my_phone1=phone("samsung","s26 ultra")
my_phone.display_info()
my_phone1.display_info()

#2nd program

class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def display_info(self):
        print(f"student name{self.name} student mark:{self.mark}")
student_info=student("shivaraj",90)
student_info.display_info()
        
