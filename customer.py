from order import Order


class Customer:

    def __init__(self, name):
        self.name = name
        self.bill = 0

    def order(self, food_items):
        l=[]
        for item in food_items:
            self.bill += item.cost
            l.append(Order(self, food_items))
        return l

