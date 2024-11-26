class Automobile:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_description(self):
        print(f'Марка автомобиля: {self.brand}. Моделль автомобиля: {self.model}. Год выпуска: {self.year}')

    def start_engine(self):
        print('Двигатель запущен')

    def change_year(self, new_year):
        self.year = new_year

class ElectricCar(Automobile):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print('Электродвигатель запущен')

    def get_battery_info(self):
        print(f'Емкость батареи: {self.battery_capacity} кВтч')

class Truck(Automobile):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def get_load_info(self):
        print(f'Грузоподъемность грузовика: {self.load_capacity} т')


automobile_data = Automobile('Nissan', 'Juke', 2011)
automobile_data.get_description()
automobile_data.start_engine()

electric_car_data = ElectricCar('Tesla', 'Model 3', 2017, 75)
electric_car_data.get_description()
electric_car_data.start_engine()
electric_car_data.get_battery_info()

truck_data = Truck('Hyundai', 'HD78', 2012, 4.4)
truck_data.get_load_info()