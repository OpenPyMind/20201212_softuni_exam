from exam_project.project.factory.factory import Factory


class EggFactory(Factory):
    def add_ingredient(self, ingredient_type: str, quantity: int):
        ingredient_types = ["chicken egg", "quail egg"]
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        else:
            if ingredient_type not in ingredient_types:
                raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
            else:
                self.ingredients[ingredient_type] += quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients:
            raise KeyError("No such ingredient in the factory")
        else:
            if quantity > self.ingredients[ingredient_type]:
                raise ValueError("Ingredient quantity cannot be less than zero")
            else:
                self.ingredients[ingredient_type] -= quantity

    @property
    def products(self):
        return self.ingredients




