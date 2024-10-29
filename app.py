from flask import Flask, render_template, redirect, url_for
from flask import request
from routes.binary_search_solver import solver

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for sessions

app.register_blueprint(solver, url_prefix='/solver')


@app.route('/', methods=('GET', 'POST'))
def hello_world():  # put application's code here
    if request.method == 'POST':
        cap = request.form['Capacitors']
        boosters = request.form['Boosters']

        result = cap + boosters
        return render_template('index.html', result=result)


    return render_template('index.html')


@app.route('/solverjs', methods=('GET', 'POST'))
def solverjs():
    return render_template('solverjs.html')


@app.route('/ShieldData', methods=('GET', 'POST'))
def shield_data():
    if request.method == 'GET':
        # return the yaml data
        return


if __name__ == '__main__':
    app.run(debug=True)








