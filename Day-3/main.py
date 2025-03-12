from flask import  Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculations.db'
db = SQLAlchemy(app)

class CalculationHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_1 = db.Column(db.Float, nullable=False)
    number_2 = db.Column(db.Float, nullable=False)
    operation = db.Column(db.String(15), nullable=False)
    result = db.Column(db.Float, nullable=False)

@app.route('/', methods=['GET', 'POST'] )
def index():
    result = None
    if request.method == 'POST':
        try:
            number_1 = float(request.form.get('number1',0))
            number_2 = float(request.form.get('number2',0))
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
        new_calculation = CalculationHistory(
            number_1 = number_1,
            number_2 = number_2,
            operation = operation,
            result = result
        )
        db.session.add(new_calculation)
        db.session.commit()

    calculations = CalculationHistory.query.order_by(
        CalculationHistory.id.desc()
    ).limit(5).all()

    return render_template('index.html', result = result , calculations = calculations )


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()

    app.run(
        host='localhost',
        port=8080,
        debug=True
    )

