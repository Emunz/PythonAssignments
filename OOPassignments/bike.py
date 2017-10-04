class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def display_info(self):
        print self.price, self.max_speed, self.miles
        return self

    def ride(self):
        self.miles += 10
        print "Riding: now at", self.miles, "miles"
        return self
    
    def reverse(self):
        self.miles -= 5
        print "Reversing: now at", self.miles, "miles"
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(500, "30mph")
bike3 = Bike(300, "25mph")

bike1.ride().ride().ride().reverse().display_info()

bike2.ride().ride().reverse().reverse().display_info()

bike3.reverse().reverse().reverse().display_info()