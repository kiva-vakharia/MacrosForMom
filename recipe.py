# recipe.py

class Recipe:
    
    def __init__(self, name, total_yield_grams):
        self.id = self.generate_id()
        self.name = name
        self.total_yield_grams = total_yield_grams

        def generate_id(self):
            pass