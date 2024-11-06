class Tech:
    def __init__(self, name, storage):
        self.name = name
        self.storage = storage
    
class Phone(Tech):
    
    def __init__(self, color,name,storage):
        self.color = color
        self.name = super().__init__(name)
        self.storage = super().__init__(storage)

    def __str__(self):
        return f"\nA {self.color} {self.name} with {self.storage}GB of storage"
    
    def __repr__(self):
        return f"\nPhone({self.color}, {self.name}, {self.storage})"

class Laptop(Tech):
    
    def __init__(self, size,name,storage):
        self.size = size
        self.name = super().__init__(name)
        self.storage = super().__init__(storage)

    def __str__(self):
        return f"\n{self.size}-inch {self.name} with {self.storage}GB of storage"
    
    def __repr__(self):
        return f"\nPhone({self.name}, {self.storage}, {self.size})"
