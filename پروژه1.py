import random

class Car:
    def __init__(self, car_id, fuel, max_speed, color):
        self.car_id = car_id
        self.fuel = fuel
        self.max_speed = max_speed
        self.color = color
        self.distance_covered = 0
        self.active = True

    def drive(self):
        if self.fuel > 0 and self.active:
            self.distance_covered += self.max_speed
            self.fuel -= 1

    def refuel(self):
        if self.active:
            self.fuel += 3

    def refuel_at_station(self, station_name, next_station_distance):
        if self.active:
            refuel_choice = input(f"Car {self.car_id} ({self.color}) has {self.fuel} units of fuel left at {station_name}. Probability of reaching next station: {self.calculate_probability(next_station_distance)}. Do you want to refuel? (yes/no): ")
            if refuel_choice.lower() == 'yes':
                self.refuel()

    def calculate_probability(self, next_station_distance):
        distance_possible = self.fuel * self.max_speed
        probability = min(1, distance_possible / next_station_distance)
        return f"{probability * 100:.2f}%"

    def check_fuel(self):
        if self.fuel <= 0 and self.active:
            self.active = False
            print(f"Car {self.car_id} ({self.color}) is out of fuel and has left the race.")

    def __str__(self):
        return f"Car {self.car_id} ({self.color}): Distance covered = {self.distance_covered}, Fuel left = {self.fuel}"

def race(cars, fuel_stations, track_length):
    while any(car.active for car in cars):
        for station in fuel_stations:
            for car in cars:
                if car.active:
                    car.drive()
                    if car.distance_covered >= station:
                        station_name = f"Station {fuel_stations.index(station) + 1}"
                        next_station_distance = fuel_stations[fuel_stations.index(station) + 1] - station if fuel_stations.index(station) + 1 < len(fuel_stations) else track_length - station
                        car.refuel_at_station(station_name, next_station_distance)
                        for other_car in cars:
                            if other_car != car and other_car.active:
                                other_car.refuel_at_station(station_name, next_station_distance)
                car.check_fuel()

            for car in cars:
                if car.distance_covered >= track_length and car.active:
                    print(f"Car {car.car_id} finished the race!")
                    car.active = False

    print("Race finished. Here are the results:")
    for car in cars:
        print(car)

if __name__ == "__main__":
    num_cars = 10
    track_length = 1000
    fuel_stations = [200, 500, 800]

    colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Purple", "Orange", "Gray", "Pink"]

    cars = [
        Car(
            car_id,
            random.choice([30, 35, 40, 45, 50]),
            random.randint(250, 300),
            colors[car_id - 1]
        ) for car_id in range(1, num_cars + 1)
    ]
    
    race(cars, fuel_stations, track_length)

for car in cars:
    print(f"Car {car.car_id} ({car.color}): Fuel = {car.fuel} units, Max Speed = {car.max_speed} km/h")
