#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.days_old = age
    def show(self):
        return(f"{self.name}:    {round(self.height, 2)}cm, {self.days_old} days old")
    
    def grow(self):
        self.height += 0.8
    def age(self):
        self.days_old = self.days_old + 1
        self.grow()

rose = Plant("Rose", 25.0, 30)
oak = Plant("Oak", 200.0, 365)
cactus = Plant("Cactus", 5.0, 90)
sunflower = Plant("Sunflower", 80.0, 45)
fern = Plant("Fern", 15.0, 120)
print("=== Plant Factory Output ===")
print(f"Created:    {rose.show()}")
print(f"Created:    {oak.show()}")
print(f"Created:    {cactus.show()}")
print(f"Created:    {sunflower.show()}")
print(f"Created:    {fern.show()}")
