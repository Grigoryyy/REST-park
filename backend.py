LIMIT_SEATS = 2
LIMIT_SEATS_CARGO = 2
hourly_rate = 50
sale_hourly_rate = 30


class Endpoint():

    def __init__(self):
        self.cars = {}
        self.cars_cargo = {}

    def park(self, car_number, hours):
        if len(self.cars) < LIMIT_SEATS:
            self.cars[car_number.lower().replace(" ", "")] = hours
            print(self.cars)
            return f"Легковая машина {car_number} припаркована на стоянке для легковых автомобилей, мест осталось: {LIMIT_SEATS - int(len(self.cars))}"
        elif len(self.cars_cargo) < LIMIT_SEATS_CARGO and len(self.cars) >= LIMIT_SEATS:
            self.cars_cargo[car_number.lower().replace(" ", "")] = hours
            return f"Легковая машина {car_number} припаркована на стоянке для грузовых автомобилей, мест осталось: {LIMIT_SEATS_CARGO - int(len(self.cars_cargo))}"
        else:
            return "Достигнуто максимальное количество машин. Парковки для грузовых и легковых автомобилей больше недоступны."

    def park_cargo(self, car_number, hours):
        if len(self.cars_cargo) < LIMIT_SEATS_CARGO:
            self.cars_cargo[car_number.lower().replace(" ", "")] = hours
            print(self.cars_cargo)
            return f"Грузовая машина {car_number} припаркована на стоянке для грузовых автомобилей, мест осталось: {LIMIT_SEATS_CARGO - int(len(self.cars_cargo))}"
        else:
            return "Достигнуто максимальное количество машин. Парковка для грузовых автомобилей больше недоступна."

    def unpark(self, car_number, hours):
        if car_number in self.cars:
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
            return f"Машина с номером {car_number} уехала! стоимость парковки: {cost}"
        elif car_number in self.cars_cargo:
            current_hour = self.cars_cargo[car_number]
            cost = hours // 24 * 1020
            hours %= 24
            for i in range(hours):
                if current_hour >= 7 and current_hour < 22:
                    cost += hourly_rate
                else:
                    cost += sale_hourly_rate
                current_hour += 1
                current_hour %= 24
            del self.cars_cargo[car_number]
            return f"Машина с номером {car_number} уехала! стоимость парковки: {cost}"
        else: return f"Машины с номером {car_number} нет на парковках!"