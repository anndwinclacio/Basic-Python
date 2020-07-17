# Challenge - Classes Exercise

# Add a method to the Car class called age that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

"""
class Car:

    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
"""


class Car:

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age (self, year):
        car_age = 2019 - self.year
        return car_age


# FOR PRINTING:
"""
car_info = Car(2010,"Hyundai", "i10")
print(car_info.age(car_info.year))
"""

    

    
