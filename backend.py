global LIMIT_SEATS
LIMIT_SEATS = 5


class Endpoint():

    def __init__(self):
        self.cars = []

    def park(self, car_number):
        if len(self.cars) < LIMIT_SEATS:
            self.cars.append(car_number)
            return (f"Машина {car_number} припаркована, мест осталось: {LIMIT_SEATS - int(len(self.cars))}")
        else:
            return "Достигнуто максимальное количество машин. Парковка больше недоступна."

    def unpark(self, car_number):
        if car_number not in self.cars:
            print(f"Машины с номером {car_number} нет на парковке!")
        else:
            print(f"Машина с номером {car_number} уехала!")
