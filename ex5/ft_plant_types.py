#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height = 0, age = 0):
        self.name = name
        self._height = 0
        self._days_old = 0
        if height >= 0:
            self._height = height
        else:
            print("height can't be negative")
        if age >= 0:
            self._days_old = age
        else:
            print("Error, age can't be negative")


    def show(self):
        return(f"{self.name}:    {round(self._height, 2)}cm, {self._days_old} days old")
    def grow(self, amount = 0.8):
        self._height += amount
    def age(self):
        self._days_old = self._days_old + 1
        self.grow()

    def set_height(self, n_height):
        if n_height >= 0:
            self._height = n_height
            print(f"Height updated: {self._height}cm")

        else:
             print(self.name ,"Error, height can't be negative")
             print("Height update rejected")
           
    def set_age(self, n_age):
        if n_age >= 0:
            self._days_old = n_age
            print(f"Age updated: {self._days_old} days")
        else:
            print(self.name,"Error, age can't be negative")
            print("Age update rejected")

    def get_height(self):
        return self._height
    def get_age(self):
        return self._days_old

class Vegetable(Plant):
    def __init__(self, name, height = 0, age = 0, h_season = "", n_value = 0):
        super().__init__(name, height, age)
        self.harvest_season = h_season
        self.nutritional_value = n_value
    def show(self):
        res = super().show() + f"\nharvest season: {self.harvest_season}"
        res = res + f"\nnutritional value: {self.nutritional_value}"
        return res
    def grow(self, amount = 2.1):
        self.nutritional_value += 1
        return super().grow(2.1)
    def age(self):
        return super().age()

class Flower(Plant):
    def __init__(self, name, height=0, age=0, color = ""):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")
    def show(self):
        res = super().show()
        res += f"\ncolor: {self.color}"
        return res

class Tree(Plant):
    def __init__(self, name, height=0, age=0, trunk_diameter =0):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.get_height()} long and {self.trunk_diameter}cm wide")
    def show(self):
        res = super().show()
        res += f"\nTrunk diameter: {self.trunk_diameter}cm"
        return res

print("=== Garden Plant Types ===")

print("=== Flower ===")
rose = Flower("Rose", 15, 10, "red")
print(rose.show())
print("[asking the rose to bloom]")
rose.bloom()

print("\n=== Tree ===")
oak = Tree("Oak", 200, 365, 5)
print(oak.show())
print("[asking the oak to produce shade]")
oak.produce_shade()

print("\n=== Vegetable ===")
tomato = Vegetable("Tomato", 5, 10, "April")
print(tomato.show())

print("[make tomato grow and age for 20 days]")
for i in range(20):
    tomato.age()

print(tomato.show())