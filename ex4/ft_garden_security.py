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
    def grow(self):
        self._height += 0.8
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

rose = Plant("Rose", 15, 10)
rose.set_height(25)
rose.set_age(30)
rose.set_height(-5)
rose.set_age(-10)
print(rose.show())