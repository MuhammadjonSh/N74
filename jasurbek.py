class Car:
    def __init__(self, name, price, year, car_type):
        self.name = name 
        self.price = price
        self.year = year
        self.car_type = car_type
    
    def get_info(self):
        print(f"{self.name} - {self.price} - {self.year} - {self.car_type}")

cars = []
years = []

for i in range(2):
    name = input("Enter car name: ")
    price = input("Enter car price: ")
    year = input("Enter car year: ")
    car_type = input("Enter car type: ")
    
    car_instance = Car(name, price, year, car_type)
    cars.append(car_instance)
    years.append(int(year))
    
years = sorted(set(years))

for year in years:
    print(f"Cars from year {year}:")
    for car in cars:
        if int(car.year) == year:
            car.get_info()
