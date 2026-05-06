# ingredient.py

class Ingredient:
    
    def __init__(self, name, protein, fats, carbs, cals):
        self.id = self.generate_id()
        self.name = name
        self.protein_per_100g = protein
        self.fat_per_100g = fats
        self.carbs_per_100g = carbs
        self.calories_per_100g = cals

        def generate_id(self):
            pass