students=[]

while True:
    print("---student ditails---")
    print("1.add student detail\n 2.show the student details\n3.exit")

    choice=int(input("enter your choice"))

    if choice==1:
        name=input("enter your name")
        age=input("enter age ")
        corse=input("enter corce name")

        student={
            "name":name,
            "age":age,
            "corse":corse
        }

        students.append(student)
        print("student details succes fully updatte ")
    elif choice==2:
        print("---student details----")
        if not students:
            print("not record found ")
        else:
            for i, student in enumerate(students,1):
                print("student",i)
                print("name",student["name"])
                print("age",student["age"])
                print("corse",student["corse"])
    elif choice==3:
        print("thank you for visit!!!!!!!!!!!!!")
        break
    else:
        print("re tryyyy !!!!!!!")
