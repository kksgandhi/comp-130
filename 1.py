class Foods:

    def __init__(self, foods):
        self.food = foods

    def add(self, food):
        self.food.append(food)

snacks = ["goldfish", "ants"]
lunch = Foods(snacks)
lunch.add("crack")
dinner = Foods(snacks)
dinner.add("duckterken")
print(snacks)

print(dinner)
