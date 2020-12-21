import re

from collections import defaultdict

from read_file.read_file import read_file


class Food:

    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens

    def __repr__(self):
        return f"{self.ingredients} - {self.allergens}"


if __name__ == '__main__':
    lines = read_file("input.txt")
    foods = []
    for line in lines:
        if not line:
            continue
        match = re.match("^(.*) \(contains (.*)\)$", line)
        ingredients = set(match.group(1).split(" "))
        allergens = set(match.group(2).split(", "))
        foods.append(Food(ingredients, allergens))

    all_ingredients = {ingredient for food in foods for ingredient in food.ingredients}
    can_be_in = defaultdict(lambda: set(all_ingredients))

    for food in foods:
        for found_allergen in food.allergens:
            can_be_in[found_allergen] &= food.ingredients

    ingredients_that_can_contain_allergen = {ingredient for ingredients in can_be_in.values() for ingredient in
                                             ingredients}

    count = sum(1 for food in foods for ingredient in food.ingredients if
                ingredient not in ingredients_that_can_contain_allergen)
    print(f"Part 1: {count}")

    can_be_in = dict(can_be_in)
    dangerous_ingredients_with_allergen = []
    while can_be_in:
        one_possible = [(list(ingredients)[0], allergen) for allergen, ingredients in can_be_in.items() if
                        len(ingredients) == 1]
        assert len(one_possible) > 0
        dangerous_ingredient, found_allergen = one_possible[0]
        dangerous_ingredients_with_allergen.append(one_possible[0])
        for allergen, ingredients in can_be_in.items():
            ingredients.discard(dangerous_ingredient)
        del can_be_in[found_allergen]

    dangerous_ingredients_with_allergen = list(sorted(dangerous_ingredients_with_allergen, key=lambda x: x[1]))
    dangerous_ingredients = ",".join(ingredient for ingredient, _ in dangerous_ingredients_with_allergen)

    print(f"Part 2: {dangerous_ingredients}")
