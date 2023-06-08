from Admin_Panel import*
from Customer import*
import sys

admin=Admin_Panel()
cus=Customer()

while True:
    print("----------- Welcome To Flowers Shop -----------")
    print("1.Admin\n2.Customer\n3.Exit")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        admin.login()
        print("*************Welcom To Admin Panel*************")
        print("Press 1--For Add Flowers")
        print("Press 2--For Remove Flowers")
        print("Press 3--For Update Flowers")
        print("Press 4--For Exit Menu")

        opt=int(input("Enter Your Choice :"))
        if opt==1:
            admin.addFlowers()
        elif opt==2:
            admin.removeFlowers()
        elif opt==3:
            admin.update_data()
        elif opt==4:
            sys.exit()
        else:
            print("Enter Correct Choice")

    elif choice==2:
        print("***********Welcom To Customer Panel**************")
        print("Press 1--For Add Order")
        print("Press 2--For Update Order")
        print("Press 3--For Delete Order")
        print("Press 4--For Exit Menu")

        option=int(input("Enter Your Choice :"))
        if option==1:
            cus.orderFlower()
        elif option==2:
            cus.update_order()
        elif option==3:
            cus.remove_order()
        elif option==4:
            sys.exit()
        else:
            print("Enter Correct Choice")
    elif choice==3:
        print("Thank You For Visiting")
        sys.exit()
    else:
        break
    
