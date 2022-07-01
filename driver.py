from customer import Customer
from food import Food
from menu import Menu
from mon import dbase

menu1 = Menu(dbase())

orders = []
pizza = Food('pizza', 15, 100)
burger = Food('burger', 10, 50)

menu1.add_food([pizza, burger])

menu1.display()

cust1 = Customer('shreya')
cust2 = Customer('riya')

orders.extend(cust1.order([pizza]))
orders.extend(cust2.order([pizza, burger]))

print(cust1.bill)
print(cust2.bill)

