# Assignment 1: Smartphone Class and Inheritance
class Smartphone:
    def __init__(self, brand, model, battery_life, storage):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
        self.storage = storage

    def display_info(self):
        return f"{self.brand} {self.model} with {self.battery_life} hours of battery life and {self.storage}GB storage."

    def charge(self):
        return f"{self.model} is charging... 🔋"

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, storage, gpu):
        super().__init__(brand, model, battery_life, storage)
        self.__gpu = gpu

    def display_info(self):
        return f"{self.brand} {self.model} (Gaming Edition) with {self.battery_life} hours battery life, {self.storage}GB storage, and GPU: {self.__gpu}."

    def play_game(self, game_name):
        return f"Playing {game_name} on {self.model} with {self.__gpu} graphics... 🎮"

# Test Assignment 1
phone = Smartphone("Apple", "iPhone 15", 24, 128)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 18, 256, "Adreno 740")

print(phone.display_info())
print(phone.charge())
print(gaming_phone.display_info())
print(gaming_phone.play_game("Call of Duty Mobile"))

# Activity 2: Polymorphism Challenge
class Mover:
    def move(self):
        pass

class Dog(Mover):
    def move(self):
        return "Running... 🐕"

class Car(Mover):
    def move(self):
        return "Driving... 🚗"

class Plane(Mover):
    def move(self):
        return "Flying... ✈️"

# Test Activity 2
movers = [Dog(), Car(), Plane()]
for mover in movers:
    print(mover.move())
