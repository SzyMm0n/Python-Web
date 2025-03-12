# A simple calculator app, with usage of forms and method POST.
# CSS added afterward
from flask import  Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] )
def index():
    result = None
    if request.method == 'POST':
        try:
            number_1 = float(request.form.get('number_1',0))
            number_2 = float(request.form.get('number_2',0))
        except ValueError:
            number_1 = 0
            number_2 = 0


        operation = request.form.get('operation')

        if operation == 'add':
            result = number_1 + number_2
        elif operation == 'subtract':
            result = number_1 - number_2
        elif operation == 'multiply':
            result = number_1 * number_2
        elif operation == 'divide':
            if number_2 != 0:
                result = number_1 / number_2
            else:result = "You can't divide by zero"

    return render_template('index.html', result = result )


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )

