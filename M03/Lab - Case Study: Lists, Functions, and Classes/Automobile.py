from Vehicle import Vehicle

class Automobile(Vehicle):
    year: int
    make: str
    model: str
    doors: int
    roof: str

    def __init__(
        self, 
        year: int, 
        make: str, 
        model: str, 
        doors: int, 
        roof: str):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"Vehicle Type: {self.type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}"