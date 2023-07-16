from flask import Flask, request, render_template
import backend

app = Flask(__name__)

endpoint = backend.Endpoint()


@app.route('/')
def home():
    return render_template('index.html')


def park():
    car_number = str(request.form['car_number'])
    hours = int(request.form['hours'])
    if car_number.lower().replace(" ", "") != '':
        return endpoint.park(car_number, hours)
    return 'Неккоректный номер машины'


def park_cargo():
    car_number = request.form['car_number']
    hours = int(request.form['hours'])
    if car_number.lower().replace(" ", "") != '':
        return endpoint.park_cargo(car_number, hours)
    return 'Неккоректный номер машины'


@app.route('/unpark', methods=['POST'])
def unpark():
    car_number = str(request.form['car_number'].lower().replace(" ", ""))
    hours = int(request.form['hours'])
    cost = endpoint.unpark(car_number, hours)
    return cost


@app.route('/park', methods=['POST'])
def select_park():
    chosen_car = request.form['vehicle_type']
    if chosen_car == 'Легковая':
        return park()
    elif chosen_car == 'Грузовая':
        return park_cargo()
    else:
        return 'Invalid function selection'


if __name__ == '__main__':

    app.run(debug=True)