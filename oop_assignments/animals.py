class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print 'Name:', self.name
        print 'Health:', self.health

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print "Name:", self.name
        print "Health:", self.health
        print "I am a dragon!"


animal1 = Animal('Chauncey', 150)
animal1.walk().walk().walk().run().run().display_health()

dog1 = Dog('Lottie')
dog1.walk().walk().walk().run().run().pet().display_health()

dragon1 = Dragon('Drogon')
dragon1.run().fly().display_health()

dog3 = Dog('Wisdom')
dog3.pet().pet().display_health()