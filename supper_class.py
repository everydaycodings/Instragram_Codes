class Car:

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.reading = 0
    
    def description(self):
        return "This is a {} with model_number {} and its year is {}".format(self.name, self.model, self.year)
    
    def readingg(self):
        print("This car has ran {} miles".format(self.reading))
    
    def update_reading(self, miles):
        if miles >= self.reading:
            self.reading = miles
        else:
            pass

    def increment_reading(self, mmiles):
        self.reading += mmiles

class tesla(Car):

    def __init__(self, name, model, year):
        super().__init__(name, model, year)


my_tesla = tesla("Tesla", 65, 8888)
print(my_tesla.description())
        




"""
cARR = Car("Tesla", 9, 2020)
print(cARR.description())
cARR.update_reading(5000)
cARR.increment_reading(100)
cARR.readingg()"""