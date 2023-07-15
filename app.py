from flask import Flask, render_template, request
import backend


app = Flask(__name__)
cars = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        answer = check_answer(user_input)
        return render_template('index.html', answer=answer)
    return render_template('index.html')


def check_answer(user_input):
    endpoint = backend.Endpoint()
    if user_input.lower().replace(" ", "") != '':
        cars.append(user_input.lower())
        for i in cars:
            answer = endpoint.park(i)
        print(endpoint.cars)
    else:
        answer = 'Неккоректный номер машины'
    return answer


if __name__ == '__main__':
    app.run(debug=True)