class _Private:                                             # This class is noted as private through the use of the single underscore before the name
    def __init__(self, name):
        self.name = name


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(slef):                                     # This is a private method hence the underscore
        print("Hello")

    def display(self):                                      # This is a public method becasue there is no
        print("Hi")