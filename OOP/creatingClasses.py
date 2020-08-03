                                             # Start with the class key word
class dog():                                 # Then then name of the class, you could also write object as the argument to the class definition i.e. class dog(object):
    def __init__(self):                      # This is the class constructor
        pass                                 # To bypass the constructor, use the pass keyword
    def speak(self):
        pass

class dog():                                 # In this second version of the class, the object needs to be called with an argument for the name which is used by the constructor to create the name attribute
    def __init__(self, name):                # This means that if you create a dog object with a name argument it will use this calss not the first
        self.name = name                     # This creates an attribute called name which is initialised with the name passed as an argument at the objects creation
    def speak(self):                         # Here we are creating a function for the dog object to speak   
        print('Hi I am', self.name)          # Notice how there are not concatination + symbols here and it prints correctly.

class dog2():                       
    def __init__(self, name, age):           # In this new class for dog2 we are takling the age as well
        self.name = name
        self.age = age
    def speak(self):
        print('Hi I am', self.name, 'I am', self.age)
    def add_weight(self, weight):            # In this method we try initialising the weight attribute but we are not passing this as an argument when we create the object
        self.weight = weight                 # To get the weight value, we need to define it in the programme


Rex = dog('Rex')                             # Creating objects and calling methods here
Rex.speak()
Dogbert = dog2('dogbert', 44)
Dogbert.speak()
Dogbert.add_weight(70)                       # This is how you can add the weight attribute to the object even though you did not initialise it when you created it 
print(Dogbert.age)                           # You can access the objects attributes from the main programme as well
