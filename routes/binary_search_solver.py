
from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
import math
from markupsafe import escape

solver = Blueprint('solver', __name__)

@solver.route('/', methods=['GET', 'POST'])
def solverHome():

    print("SolverTest")
    if request.method == 'POST':
        # Initialize game settings based on user input
        low_value = int(request.form['low_value'])
        high_value = int(request.form['high_value'])

        session['low_value'] = low_value
        session['high_value'] = high_value
        print(escape(session['low_value']))
        session['correct'] = (low_value + high_value) // 2
        session['attempts'] = 0
        session['max_attempts'] = math.ceil(math.log2(high_value - low_value + 1))

        return redirect(url_for('solver.guess'))
    print("TEST")
    return render_template('solver.html')


@solver.route('/guess', methods=['GET', 'POST'])
def guess():
    print("GUESS")
    if 'low_value' not in session or 'high_value' not in session:
        print("NO VALS")
        return redirect(url_for('solver.solverHome'))  # Start game if session data is missing

    if request.method == 'POST':
        response = request.form['response']
        guess = (session['low_value'] + session['high_value']) // 2
        session['attempts'] += 1

        # Update range based on user's feedback
        if response == 'L':
            session['low_value'] = guess + 1
        elif response == 'H':
            session['high_value'] = guess - 1
        elif response == 'R':
            return redirect(url_for('solver.solverHome'))  # Restart game

        # Update correct guess
        session['correct'] = (session['low_value'] + session['high_value']) // 2

        # Render guess page again after processing the feedback
        return redirect(url_for('solver.guess'))

    return render_template(
        'guess.html',
        low=session['low_value'],
        high=session['high_value'],
        guess=session['correct'],
        attempts=session['attempts'],
        max_attempts=session['max_attempts']
    )



