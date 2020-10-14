class smartphone:

    def __init__(self,name, r_size, processer, d_size, price):
        self.name = name
        self.r_size = r_size
        self.processer = processer
        self.d_size = d_size
        self.price = price
        self.discount = 40
    
    def discription(self):
        return"The Smartphone Name is {} it has {} ram, {} processer, with {}inch Display and its price is only {} Rupees.".format(self.name, self.r_size, self.processer, self.d_size, self.price)
        
    def buy(self, name, address):
        print("Hello {} We got your details we have {}% Discount to our VIP custommers. So are You Our VIP custommer or not".format(name, self.discount))
        user = input("Please Type (YES) or (NO): ")

        if user in ("YES", "Y", "yes", "y"):
            username = input("Please Enter Your VIP Username: ")
            passd = input("Please Enter Your Password: ")

            if username == username and passd == passd:
                t_d = self.price * self.discount / 100
                price_to_be_paid = self.price - t_d
                return "Congrates you got {}% Discount You have to pay only {}Rupees!!! ".format(self.discount, price_to_be_paid)
            
            else:
                return "You have to pay {} for Your Smartphone".format(self.price)




smartphone1 = smartphone("Samsung", 8, "Snapdragon1000", 1.5, 15000)
print(smartphone1.discription())

userask = input("Do You Want To Buy This Smartphone: ")

if userask in ("yes", "YES", "Y", "y"):
    name = input("Please Enter Your Name: ")
    address = input("Please Enter Your Address: ")
    print(smartphone1.buy(name, address))
else:
    print("Thanku To Vist The Store!!")