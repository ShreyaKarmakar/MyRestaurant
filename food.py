class Food:

    def __init__(self, name, time, cost):
        self.name = name
        self.time = time
        self.cost = cost

    def __str__(self):
        return f'{self.name} Cost:{self.cost}'
