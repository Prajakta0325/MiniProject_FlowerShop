import json
class Customer:
    def __init__(self):
        self.ordered_flowers_dic={}

    def orderFlower(self):
        with open("addFlowers.json","r")as f:
            content1=json.load(f)
        print(content1)

        order_id=input("Enter Flower Id Which You Want to Order :")
        self.ordered_flowers_dic[order_id]=content1

        #store in json
        with open("orderedFlowers.json","w")as f:
            json.dump(content1,f,indent=4)
        print("Ordered Added Successfully......")

    def order_history(self):
        with open("orderedFlowers.json","r")as f:
            content1=json.load(f)
        print(content1)

        for k,v in content1.items():
            print(f"Module Id:{k}       Data:{v}")

    def update_order(self):

        with open("orderedFlowers.json","r")as f:
            content1=json.load(f)
        print(content1)

        #update order

        ordered_id=input("Enter Flower Id Which You Want To Update :")
        ordered_field=input("Enter Field Which You Want To Update :")

        updated_value=input("Enter Updated Value:")

        content1[ordered_id][ordered_field]=updated_value

        #update value in json
        with open("orderedFlowers.json","w")as f:
            json.dump(content1,f,indent=4)
        print("Data Updated Successfully........")

    def remove_order(self):

        with open("orderedFlowers.json","r")as f:
            content1=json.load(f)
        print(content1)
        for k,v in content1.items():
            print(f"ID:{k}         Data:{v}")

        delete_id=input("Enter Flower ID Which You Want To Remove From Ordered :")
        del content1[delete_id]

        #store in json
        with open("orderedFlowers.json","w")as f:
            json.dump(content1,f,indent=4)
        print("Data Remove Successfully....")




#c=Customer()
#c.orderFlower()
#c.order_history()
#c.update_order()
#c.remove_order()