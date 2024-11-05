# composition is a type of class that exists in another class (class has a other class)

class Car:
    def __init__(self,make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
class Engine:
    def __init__(self, configuration, displaceent, horsepower, torque):
        self.configuration = configuration
        self.displacement = displaceent
        self.horsepower = horsepower
        self.torque = torque
    
    def ignite(self):
        print("broom broom im in me mums caaahr\nget out me caaahr")
    
myEngine = Engine("V8", 5.8, 3, 344)
myCar = Car("Mazda", "Maza 3", 2013, myEngine)

#to call a somposite class you must acces where it is saved withing the alss
print(myCar)

myCar.engine.ignite()