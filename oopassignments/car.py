class car(object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if(self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print 'Price:', self.price
        print 'Speed:', self.speed
        print 'Fuel:', self.fuel
        print 'Mileage:', self.mileage
        print 'Tax:', self.tax
        return self

car1 = car(21000, '80mph', 'Full', '33mpg')
car2 = car(14000, '75mph', 'Mostly Full', '24mpg')
car3 = car(6000, '60mph', 'Empty', '22mpg')
car4 = car(45000, '85mph', 'Full', '32mpg')
car5 = car(18000, '80mph', 'Kind of Full', '27mpg')
car6 = car(4999, '70mph', 'Almost Empty', '25mpg')
