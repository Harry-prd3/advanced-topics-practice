class App:
    def __init__(self, name, description, catagory):
        self.name = name
        self.description = description
        self.catagory = catagory
    
    def __str__(self):
        return f"{self.name} is a(n) {self.catagory} app that is {self.description}."