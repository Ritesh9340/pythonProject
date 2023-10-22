class car:
    def __init__(self , make, model,year,milage):
        self.make=make
        self.model=model
        self.year=year
        self.milage=milage
    def get_info(self):
        return f"Car:{self.make} {self.model}({(self.year)}) -milege:  {self.milage} "

car1=car("Toyota","x_sries",2022,"300 P/L")

INFO=car1.get_info()
print(INFO)
