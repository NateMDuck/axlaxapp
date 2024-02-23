from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Your lists
list_side = ['right', 'left']
list_moves = ['shift', 'double shift', 'triple shift', 'roll dodge', 'question mark dodge', 'face dodge', 'split dodge', 'bull dodge']
list_shots = ['high', 'side', 'low']
list_goal = ['right upper ninety', 'left upper ninety', 'right lower ninety', 'left lower ninety', 'nutmeg']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_moves = request.form.getlist('moves')
        selected_shots = request.form.getlist('shots')
        selected_goals = request.form.getlist('goals')
        sleep_time = request.form['sleep_time']  # Assuming this is how you'd like to handle it

        # Generate drills based on selections
        drills = []
        num_rounds = int(request.form['num_rounds'])  # User specifies number of rounds
        for _ in range(num_rounds):
            move = f"{random.choice(list_side)} {random.choice(selected_moves)}"
            shot = f"{random.choice(list_side)} {random.choice(selected_shots)} {random.choice(selected_goals)}"
            drills.append({'move': move, 'shot': shot})

        return render_template('result.html', drills=drills, sleep_time=sleep_time)
    else:
        # Pass all moves, shots, and goals to the template
        return render_template('index.html', moves=list_moves, shots=list_shots, goals=list_goal)

if __name__ == '__main__':
    app.run(debug=True)
