from config import DATABASE_URI

class FoodComparison:
    def __init__(self, *foods, goal=None):
        self.foods = foods
        self.goal = goal

    def get_food_data(self, food_name):
        pass

    def compare_foods(self):
        pass