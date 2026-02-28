# class movie:
#     def __init__(self,titel,rating):
#         self.titel=titel
#         self.rating=rating

#     def movies_title(self):
#         print(f"movie name{self.titel} and that's {self.rating}")
    
# y=movie("kanthara","9.7")
# y.movies_title()

class employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary

    def movies_title(self):
        print(f"name={self.name}  design={self.designation} sal={self.salary}")
    
y=employee("shivaraj","architec")
z=employee("shivaraj","architec","5000")
x=employee("shivaraj","architec","8000")
m=employee("shivaraj","architec")
n=employee("shivaraj","architec")
y.movies_title()
z.movies_title()
x.movies_title()
m.movies_title()
n.movies_title()