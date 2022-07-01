class Menu:

    def __init__(self, db):
        self.food_items = []
        self.db = db

    def add_food(self, food):
        self.food_items.extend(food)
        self.add_to_db(food)

    def display(self):
        for id, food in enumerate(self.food_items):
            print(f'ID:{id} Name:{food}')

    def add_to_db(self, food_list):
        menu_col = self.db.get_collection('menu')  # db = get the collection...
        for food in food_list:
            self.db.add_to_collection(menu_col, food)
