from flask import Flask, render_template, request, jsonify
import random
import subprocess
import time

app = Flask(__name__)

# Your lists
list_side = ['right', 'left']
list_moves = ['shift', 'double shift', 'triple shift', 'roll dodge', 'question mark dodge', 'face dodge', 'split dodge',
              'bull dodge']
list_shots = ['high', 'side', 'low']
list_goal = ['right upper ninety', 'left upper ninety', 'right lower ninety', 'left lower ninety', 'nutmeg']


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_moves = request.form.getlist('moves')
        selected_shots = request.form.getlist('shots')
        selected_goals = request.form.getlist('goals')
        sleep_time = int(request.form['sleep_time'])  # Convert sleep_time to int
        num_rounds = int(request.form['num_rounds'])  # User specifies number of rounds

        drills = []
        for _ in range(num_rounds):
            move = f"{random.choice(list_side)} {random.choice(selected_moves)}"
            shot = f"{random.choice(list_side)} {random.choice(selected_shots)} {random.choice(selected_goals)}"
            drills.append({'move': move, 'shot': shot})

            # Speak the text for the drill using the 'say' command-line utility
            subprocess.run(['say', f"{move}. {shot}"])

            time.sleep(sleep_time)  # Sleep for the specified time before the next drill

        # Return drills as JSON response
        return jsonify(drills), 200
    else:
        return render_template('index.html', moves=list_moves, shots=list_shots, goals=list_goal)


if __name__ == '__main__':
    app.run(debug=True)

