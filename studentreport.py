class Student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
        self.__marks={}
    def get_marks(self):
        return self.__marks
    
    def add_marks(self,subject,marks):
        self.__marks[subject]=marks

    def caluclate_average(self):
        total=0
        for mark in self.__marks.values():
            total +=mark
        average=total/len(self.__marks)
        return average
    def is_passed(self):
        has_passed=all(mark>35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name}has passed")
        else:
            print(f"{self.name}has failed")

    def caluclate_grade(self):
        print("grade",end="")
        persentage=self.caluclate_average()
        if persentage>=90:
            print(" A")
        elif persentage>=85:
            print(" B")
        else:
            print(" c")
class ReportCard:
    @staticmethod
    def generte(student:Student):
        student_marks=student.get_marks()
        print(f"name {student.name} \t roll no {student.roll_no}")
        print("-------marks-------")
        for subject,marks in student_marks.items():
            print(f"{subject} {marks}")
        print("==================")
        print(f"avarage {student.caluclate_average ()}")
        student.is_passed()
        student.caluclate_grade()

a=Student(1,"shivaraj")
a.add_marks("science =",98)
a.add_marks("social =",11)

ReportCard.generte(a)