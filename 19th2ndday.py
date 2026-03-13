cart={}
prices={
    "apple":10,
    "bananna":30,
    "caret":70,
    "bread": 40,
    "eggs": 60
}

while (True):
    print("----grosari shop-----")
    print("1.Add items to their cart.\n 2.Remove items\n 3.View the total price\n 4.exit")


    choice=input("enter your choice : ")

    if choice==1:
        item=input("enter itam name  ").lower
        if item in prices:
            quntity=input("enter the quantity :  ")
            if item in cart:
                print("")