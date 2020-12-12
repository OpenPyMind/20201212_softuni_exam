from exam_project.project.factory.factory import Factory
from collections import defaultdict


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = defaultdict(dict)
        self.products = defaultdict(int)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        ingredient_types = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        else:
            if ingredient_type not in ingredient_types:
                raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
            else:
                self.ingredients[ingredient_type] += quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients:
            raise KeyError("No such product in the factory")
        else:
            if quantity > self.ingredients[ingredient_type]:
                raise ValueError("Ingredient quantity cannot be less than zero")
            else:
                self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes:
            raise TypeError("No such recipe")
        else:
            for ingredient_type, quantity in self.recipes[recipe_name].items():
                self.remove_ingredient(ingredient_type, quantity)

            self.products[recipe_name] += 1


