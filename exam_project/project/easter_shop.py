from exam_project.project.factory.egg_factory import EggFactory
from exam_project.project.factory.chocolate_factory import ChocolateFactory
from exam_project.project.factory.paint_factory import PaintFactory
from collections import defaultdict


class EasterShop:
    def __init__(self, name: str,
                 chocolate_factory: ChocolateFactory,
                 egg_factory: EggFactory,
                 paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = defaultdict(int)

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        self.store_product(recipe)

    def paint_egg(self, color: str, egg_type: str):
        can_paint = self.paint_factory.ingredients[color] >= 1
        has_egg = self.egg_factory.ingredients[egg_type] >= 1
        if not (can_paint and has_egg):
            raise ValueError("Invalid commands")
        else:
            painted_egg = f"{color} {egg_type}"
            self.store_product(painted_egg)
            self.paint_factory.remove_ingredient(color, 1)
            self.egg_factory.remove_ingredient(egg_type, 1)

    def store_product(self, product_name):
        self.storage[product_name] += 1

    def __repr__(self):
        repr_str = f"Shop name: {self.name}\n" \
                   f"Shop storage:\n"
        entries = []
        for item, quantity in self.storage.items():
            entries.append(f"{item}: {quantity}")
        repr_str += "\n".join(entries)
        return repr_str
