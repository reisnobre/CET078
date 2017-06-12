class Pizza:
    ingredients = {}
    def __init__(self):
        self.__ingredients = {}
        
    def addIngredient(self, ingredient):
        if (ingredient in self.ingredients):
            self.ingredients[ingredient] += 1    
        else:
            self.ingredients[ingredient] = 1
        self.__ingredients[ingredient] = 1    