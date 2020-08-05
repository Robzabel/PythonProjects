class Point():
    def __init__(self, x=0, y=0):
        self.x = x                                                      # Define a simple class for the point objects
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x ,y):                                               # Give the Class a method to move coordinates on a graph
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)                        # Overload the built in functions so that when they are called on objects of this class, the
                                                                        # action is different than what it would be for other class types
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return Point(self.x * p.x + self.y * p.y)

    def __div__(self, p):
        return Point(self.x / p.x, self.y / p.y)

    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) +')'               # The built in string function is used whenever you call the print method or use str() on an object

    

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

print(p5, p6, p7)
