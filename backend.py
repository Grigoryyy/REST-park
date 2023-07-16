global LIMIT_SEATS
LIMIT_SEATS = 5
hourly_rate = 50


class Endpoint():

    def __init__(self):
        self.cars = {}

    def park(self, car_number, hours):
        if len(self.cars) < LIMIT_SEATS:
            self.cars[car_number.lower().replace(" ", "")] = hours
            print(self.cars)
            return (f"Машина {car_number} припаркована, мест осталось: {LIMIT_SEATS - int(len(self.cars))}")
        else:
            return "Достигнуто максимальное количество машин. Парковка больше недоступна."

    def unpark(self, car_number, hours):
        if car_number not in self.cars:
            return(f"Машины с номером {car_number} нет на парковке!")
        else:
            #cost = (hours - self.cars[car_number]) * hourly_rate
            cost = hours * hourly_rate
            del self.cars[car_number]
            return(f"Машина с номером {car_number} уехала! стоимость парковки: {cost}")
