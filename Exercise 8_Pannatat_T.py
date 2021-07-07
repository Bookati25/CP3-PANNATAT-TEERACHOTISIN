print("Program start")
ID = input("ID:")
PW = input("Password:")
if ID == "User" and PW == "1234":
    print("Welcome")
    print("Do you want to but something?")
    Answer1 = input("Yes or No :")
    if Answer1 == "Yes":
        print("Fruit")
        print("1.Apple : 2g")
        print("2.Banana : 3g")
        print("3.Orange : 4g")
        print("4.Not but anything")
        print("What would you like to buy?")
        Buy1 = input("Item:")
        if Buy1 == "1" or Buy1 == "2" or Buy1 == "3":
            Qty1 = int(input("Quantity:"))
            if Buy1 == "1":
                print("Total",2*Qty1,"g")
            elif Buy1 == "2":
                print("Total",3 * Qty1,"g")
            elif Buy2 == "3":
                print("Total",4 * Qty1,"g")
        elif Buy1 == "4":
            print("Thank you, Goodbye")
        else:
            print("Program Error")
    elif Answer1 == "No":
        print("Thank you, Goodbye")
    else:
        print("Program Error")
else:
    print("Cannot Login")
