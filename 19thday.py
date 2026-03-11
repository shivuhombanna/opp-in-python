def add(a,b):
    return a+b
def sup(a,b):
    return a-b
def mul(a,b):
    return a*b
while(True):
    print("simpal calculater ")
    print("1.add\n2.sup\n3.mul\n4.exit")

    caluclate =int(input(" enter your choice "))
    if caluclate=={1,2,3}:
        a=int(input("enter the first num "))
        b=int(input("enter the second num "))

    if caluclate==1:
        print("result ",add(a,b))
    elif caluclate==2:
        print("result ",sup(a,b))
    elif caluclate==3:
        print("result ",mul(a,b))
    elif caluclate==4:
        print("exit..... ")
        break
    else:
        print("invalid choice")