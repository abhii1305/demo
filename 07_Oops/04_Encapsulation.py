class Car:
    def __init__(self, brand , model):
        self.__brand=brand
        self.model=model


    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

        
my_Tesla=ElectricCar("Tesla","Model S", "85kWh")
# print(my_Tesla.__brand)
print(my_Tesla.get_brand())
# my_car = Car("Tata","Safari")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())