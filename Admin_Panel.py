import json
import random
class Admin_Panel:

    def __init__(self):
        self.flowerdetails={}

    def login(self):

        self.username=input("Enter Your Username :")
        self.password=input("Enter Your Password :")

        if self.username=="admin" and self.password=="admin":
            print("Login Successfully....")
        else:
            print("Enter Correct Username and Password")

    def addFlowers(self):
        id=random.randint(1,100)
        name=input("Enter Flower Name :")
        quantity=input("Enter Quantity :")
        price=input("Enter Flower Price :")

        flowerdata={"Name":name,"Quantity":quantity,"Price":price}

        self.flowerdetails[id]=flowerdata

        #store data in json
        with open("addFlowers.json","w")as f:
            json.dump(self.flowerdetails,f,indent=4)
        print("Data Added Successfully....")

    def removeFlowers(self):

        #load data from json
        with open("addFlowers.json","r")as f:
            content1=json.load(f)
        print(content1)

        for k,v in content1.items():
            print(f"Module ID:{k}    Data:{v}")
        
        module_key=input("Enter Flower Id Which you Want to Delete :")
        del content1[module_key]

        #update in json also
        with open("addFlowers.json","w") as f:
            json.dump(content1,f,indent=4)
        print("Data Updated Successfully......")

    def update_data(self):

        with open("addFlowers.json","r")as f:
            content1=json.load(f)
        print(content1)

        for k,v in content1.items():
            print(f"Module ID:{k}               Data:{v}")
        
        updated_id=input("Enter Id Which You Want To Update :")
        updated_field=input("Enter Field Which You Want To Update :")
        updated_value=input("Enter New Value :")

        content1[updated_id][updated_field]=updated_value

        #need to store updated data into json
        with open("addFlowers.json","w")as f:
            json.dump(content1,f,indent=4)
        print("Data Updated Successfully........")
    



#ad=Admin_Panel()
#ad.login()
#ad.addFlowers()
#ad.removeFlowers()
#ad.update_data()