class Dog():
    dogs = []                               # Class variables are declared outside of any member functions. 
                                            # This makes them private variables that are not available to be accessed by anything else
    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod                            # This is called the decorator, it is used to specify special types of method
    def num_dogs(cls):                      # The class method doesnt need an object instance to be called.
        return len(cls.dogs)                # Because it doesnt need an object, the methods are called on cls which stands for class rather than self

    @staticmethod
    def bark(n):                            # Static methods do not need to be passed the self or class arguments       
        # Barks n times                     # Because the method is not passed the self or cls peramaters, it cannot access the object or class variables
        for i in range(n):                  # This method needs to be called with Dog.bark() just so the interpreter knows where to look for the function definition
            print('Bark!')                  


dogbert = Dog('Dogbert')
Max = max('Max')

print(Dog.num_dogs())
print(Dog.bark(5))