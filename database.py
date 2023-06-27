from config import DATABASE_URI

class FoodComparison:
    def __init__(self, *foods, goal=None):
        self.foods = foods
        self.goal = goal

    def get_food_data(self, food_name):
        pass

    def compare_foods(self):
        pass

    def weight_loss(self):
        '''
        Comparison order
        1. Lower Calories
        2. Lower Fat (saturated)
        3. Lower Carbs (sugar)
        4. Higher Fibre
        5. Higher Protein
        '''
        pass

    def hypertrophy(self):
        '''
        1. Higher Protein
        '''
        pass
