#!/bin/python
class Plant:
    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown", 0, 0)

    def __init__(self, name, height=0, age=0) -> None:
        self.name = name
        self._height = 0
        self._days_old = 0
        self.stat = self.Statistics()
        if height >= 0:
            self._height = height
        else:
            print("height can't be negative")
        if age >= 0:
            self._days_old = age
        else:
            print("Error, age can't be negative")

    def show(self) -> str:
        self.stat.increment_show()
        return (f"{self.name}:    {round(self._height, 2)}cm, \
{self._days_old} days old")

    def grow(self, amount=0.8) -> None:
        self._height += amount
        self.stat.increment_grow()

    def age(self) -> None:
        self._days_old = self._days_old + 1
        self.stat.increment_age()
        self.grow()

    def set_height(self, n_height) -> None:
        if n_height >= 0:
            self._height = n_height
            print(f"Height updated: {self._height}cm")
        else:
            print(self.name, "Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, n_age) -> None:
        if n_age >= 0:
            self._days_old = n_age
            print(f"Age updated: {self._days_old} days")
        else:
            print(self.name, "Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_old

    @staticmethod
    def is_older_than_year(age) -> bool:
        return age > 365

    class Statistics():
        def __init__(self, grow_count=0, age_count=0, show_count=0) -> None:
            self.__grow_count = grow_count
            self.__age_count = age_count
            self.__show_count = show_count

        def increment_grow(self) -> None:
            self.__grow_count += 1

        def increment_age(self) -> None:
            self.__age_count += 1

        def increment_show(self) -> None:
            self.__show_count += 1

        def display(self) -> str:
            return f"\nStats:{self.__grow_count} grow, \
{self.__age_count} age, {self.__show_count} show"


class Vegetable(Plant):
    def __init__(self, name, height=0, age=0, h_season="", n_value=0) -> None:
        super().__init__(name, height, age)
        self.harvest_season = h_season
        self.nutritional_value = n_value

    def show(self) -> str:
        res = super().show() + f"\nharvest season: {self.harvest_season}"
        res = res + f"\nnutritional value: {self.nutritional_value}"
        return res

    def grow(self, amount=2.1) -> None:
        self.nutritional_value += 1
        return super().grow(amount)

    def age(self) -> None:
        return super().age()


class Flower(Plant):
    def __init__(self, name, height=0, age=0, color="") -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloomed = False

    def bloom(self) -> None:
        self.is_bloomed = True
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> str:
        res = super().show()
        res += f"\ncolor: {self.color}"
        if self.is_bloomed is False:
            res += f"\n{self.name} has not bloomed yet\n"
        return res


class Tree(Plant):
    def __init__(self, name, height=0, age=0, trunk_diameter=0) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shadow_count = 0

    def produce_shade(self) -> None:
        self.shadow_count += 1
        print(f"Tree {self.name} now produces a shade of \
{round(self.get_height(), 2)} long and {self.trunk_diameter}cm wide")

    def show(self) -> str:
        res = super().show()
        res += f"\nTrunk diameter: {self.trunk_diameter}cm"
        return res


class Seed(Flower):
    def __init__(self, name, height, age, color, seeds_count) -> None:
        super().__init__(name, height, age, color)
        self.seeds_count = seeds_count

    def show(self) -> str:
        res = super().show()
        res += f"\nSeeds: {self.seeds_count}"
        return res

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42


def Statistic(plant) -> None:
    print(plant.stat.display())
    if isinstance(plant, Tree):
        print(plant.shadow_count, " shade.")


t1 = Tree("tree1", 11, 300)
t1.grow()
t1.grow()
t1.age()
t1.show()
t1.show()
t1.show()
t1.produce_shade()
t1.produce_shade()
t1.produce_shade()
t1.produce_shade()
Statistic(t1)
