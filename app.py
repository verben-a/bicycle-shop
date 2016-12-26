from bicycle_shop import Bicycle
from bicycle_shop import Customer
from bicycle_shop import Shop

b1 = Bicycle("Axiom", 700)
b2 = Bicycle("Evergreen", 550)
b3 = Bicycle("Redsky", 500)
b4 = Bicycle("Airheart", 250)
b5 = Bicycle("Expat", 200)
b6 = Bicycle("Sola", 180)
b7 = Bicycle("Sola", 180)

name = input("Please enter your name: ")
budget = int(input("Please enter your budget: "))

bike_shop = Shop("Awesome bicycles", [b1, b2, b3, b4, b5, b6], "20%")
bike_shop.inventory.append(b7)

c1 = Customer(name, budget)
c1.show_my_status(bike_shop)

decision = input("What bike do you want to buy?").capitalize()

bike_shop.sell(decision, c1)
print([bike.model for bike in bike_shop.inventory])
print([bike.model for bike in c1.garage])



