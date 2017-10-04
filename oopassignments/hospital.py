class Patients(object):
    ID = 1000
    bed_number = 50
    def __init__(self, name, allergies):
        self.id = Patients.ID
        Patients.ID += 1
        self.name = name
        self.allergies = allergies
        Patients.bed_number += 1
        self.bed_number = Patients.bed_number

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def admit(self, name, allergies = None):
        if len(self.patients) >= self.capacity:
            print 'I\'m sorry, ' + name + ', but the hospital is full'
        else:
            self.patients.append(Patients(name, allergies))
            print name + ', your admission process has been completed'
        return self

    def discharge(self, full_name):
        for people in self.patients:
            if people.name == full_name:
                self.patients.remove(people)
                print people.name + ', you have been discharged and can go home'

    def display_info(self):
        for people in self.patients:
            print 'ID:', people.id
            print 'Name:', people.name
            print 'Allergies:', people.allergies
            print 'Bed Number:', people.bed_number
            print '--------------------'

hosp = Hospital('Sacred Heart', 10)

hosp.admit('Kevin Abstract', 'Penecillin')
hosp.admit('Keenan Kel')
hosp.admit('S.A Squatch', 'Gluten')
hosp.admit('Charlie Bliss', 'Lactose Intolerant')
hosp.discharge('Keenan Kel')
hosp.admit('Steve Bannon')
hosp.admit('Carly Simon', 'not melodies, lol')
hosp.admit('Jimmy Stewart')
hosp.admit('Stephen A. Smith', 'logical thought')
hosp.admit('Marshall Matters')
hosp.admit('Ellen Emayoh', 'advil')
hosp.admit('Elle Ohell')
hosp.admit('Cordell Blackmon', 'penicillin')
hosp.admit('James James')
hosp.admit('Donnie Blumpet')
hosp.admit('Chance T. Wrapper')
hosp.discharge('Elle Ohell')

hosp.display_info()
