class Bicycle(object):
    def __init__(self, model, price):
        self.model = model
        self.price = price
    
        
class Customer(object):
    def __init__(self, name, budget, garage =[]):
        self.name = name
        self.budget = budget
        self.garage = garage
        
    def show_my_status(self, bike_shop):
        for bike in bike_shop.inventory:
            if self.budget >= bike.price:
                print("You can afford " + "{}, {}".format(bike.model, bike.price))
                
    def purchase(self, bike):
        self.garage.append(bike)
        print("Have bought: " + bike.model)
        
        
class Shop(object):
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.margin = margin
        
    def sell(self, bike_model, customer): 
        # bike_model is a string
        for bike in self.inventory:
            if bike_model == bike.model:
                self.inventory.remove(bike) # self.inventory.remove("Axiom")
                customer.purchase(bike)
    
        
        
    
    