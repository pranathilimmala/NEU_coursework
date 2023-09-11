#!/usr/bin/env bash

import math


"""Problem: 1
basic_classes.py"""

# To create two example instances of a class, and demonstrate
# the functionality of at least one of the methods.


class Circle:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def diameter(self):
        return 2 * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def isRed(self):
        return self.color == "red"

circle1 = Circle("red", 5)
circle2 = Circle("blue", 7)

print("Circle 1 Diameter:", circle1.diameter())
print("Circle 1 is red:", circle1.isRed())

class GraduateStudent:
    def __init__(self, first_name, last_name, year, major):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major

    def year_matriculated(self):
        return 2020 - self.year

student1 = GraduateStudent("jim", "Smith", 2, "Computer Science")
student2 = GraduateStudent("Jane", "Eyre", 3, "Biology")

print("Year Matriculated:", student1.year_matriculated())
