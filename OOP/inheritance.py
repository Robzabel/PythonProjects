class dog():                       
    def __init__(self, name, age):           
        self.name = name
        self.age = age
    def speak(self):
        print('Hi I am', self.name, 'I am', self.age)
    def talk(self):
        print('bark')

class cat(dog):                                         # By putting Dog as the argument for cat, cat will inherit the dog class
    def __init__(self, name, age, colour):              # Here we list the arguments needed to create an object of cat
        super().__init__(name, age)                     # The super keyword tells the new class to use the constructor from the parent class
        self.colour = colour                            # This is the only attribute of the new class
    def talk(self):                                     # You can oveload the class methods
        print('Meow')
    def speak(self):
        print('Hi I am', self.name, 'I am', self.age, 'I am', self.colour)


Rex = dog('Rex', 3)                                     # Create an object of dog
Rex.speak()                                             # Call methods on dog object
Rex.talk()

Fenty = cat('Fenty', 5, 'black/brown')                  # Create an object of cat
Fenty.speak()                                           # Call methods on cat object
Fenty.talk()

