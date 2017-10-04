class MathDojo(object):
    def __init__(self):
        self.output = 0

    def add(self, *args):
        for thing in args:
            if type(thing) == tuple or type(thing) == list:
                self.output += sum(thing)
            else:
                self.output += thing
        return self

    def subtract(self, *args):
        for thing in args:
            if type(thing) == tuple or type(thing) == list:
                self.output -= sum(thing)
            else:
                self.output -= thing
        return self

    def display_output(self):
        print self.output

md = MathDojo()

md.add(2).add(2,[5, 2.08, 2, 6]).subtract(3,(2,8,10,2)).add([3,3.5,3,3,3]).display_output()

