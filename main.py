# main.py
from api import get_food_data as get_food_data_from_api
from database import save_food_data, get_food_data, compare_foods

def main():
    # Get user input for the foods to compare
    # Check if the data is already in the database
    # If not, fetch it from the API and save it
    # Compare the foods and print the comparison
    pass

def weight_loss():
    # Gets called in main() if the user chooses the "Weight Loss" option. 
    # Priority of nutrients to be confirmed
    '''
    Priority ordering:
    1. Lower Calorie
    2. Lower Fat (saturated)
    3. Lower Carbs (sugar)
    4. Higher Fibre
    4. Higher Protein
    '''
    pass

def build_muscle():
    '''
    Priority ordering:
    1. Higher Protein
    '''
    pass



if __name__ == '__main__':
    main()
