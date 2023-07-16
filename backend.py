global LIMIT_SEATS
LIMIT_SEATS = 5
hourly_rate = 50
sale_hourly_rate = 30

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
            current_hour = self.cars[car_number]
            cost = hours // 24 * 1020
            hours %= 24
            for i in range(hours):
                if current_hour >= 7 and current_hour < 22:
                    cost += hourly_rate
                else:
                    cost += sale_hourly_rate
                current_hour += 1
                current_hour %= 24
            del self.cars[car_number]
            return(f"Машина с номером {car_number} уехала! стоимость парковки: {cost}")
