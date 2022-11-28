class Cars:

    # instance variable of car
    def __init__(self, model, brand, year, color):
        self.model = model
        self.brand = brand
        self.year = year
        self.color = color

    def print_car(self):
        print(
            f"The {self.color} car is a {self.model} and was manufactured by {self.brand} on {self.year}")

# Child class of Cars


class Driver(Cars):
    def __init__(self, model, brand, year, color, driver):
        Cars.__init__(self, model, brand, year, color)
        self.driver = driver

    def print_car(self):
        print(f"The Driver of {self.model} is {self.driver}")


Jess = Driver("kekenapep", "Mercedes", "2045", "brown", "Jessica")

Jess.print_car()
