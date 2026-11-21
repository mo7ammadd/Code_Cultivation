#!/bin/python
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.days_old = age

    def show(self) -> None:
        print(f"{self.name}:    {round(self.height, 2)}cm,\
{self.days_old} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days_old = self.days_old + 1
        self.grow()


rose = Plant("Rose", 25, 30)
initial_height = rose.height
print("=== Garden Plant Growth ===")
rose.show()
for i in range(7):
    rose.age()
    print(f"=== Day {i+1} ===")
    rose.show()
print("Growth this week: ", round(rose.height - initial_height, 2), "cm")
