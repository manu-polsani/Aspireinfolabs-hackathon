# from flask import Blueprint

# views = Blueprint('views',__name__)

# @views.route('/')
# # 
# def home():
#     return "<h1>Test</h1>"
from .health import calc

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
#from .models import Note 
#import db
#import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    return render_template("home.html", user=current_user)

@views.route('/', methods=['GET', 'POST'])
@views.route('/n_news', methods=['GET', 'POST'])
@login_required
def n_news():
    return render_template("n_news.html", user=current_user)

@views.route('/MyHealth1', methods=['GET', 'POST'])
@login_required
def MyHealth1():
    return render_template("MyHealth1.html", user=current_user)

@views.route('/MyHealth1/DailyProgress', methods=['GET', 'POST'])
@login_required
def DailyProgress():
    return render_template("DailyProgress.html", user=current_user)

@views.route('/community')
@login_required
def community():
    return render_template('community.html')

@views.route('/performance_tracking')
@login_required
def Performance_tracking():
    return render_template('performance_tracking.html')

# @views.route('/predict', methods=['POST'])
# @login_required
# def predict():
#     Steps = float(request.form['Steps'])
#     Weight = float(request.form['Weight'])
#     SleepDuration = float(request.form['SleepDuration'])
#     CaloriesBurn = float(request.form['CaloriesBurn'])
#     WaterIntake = float(request.form['WaterIntake'])

#     # Call the calc function from health.py
#     output = calc(Steps, Weight, SleepDuration, CaloriesBurn, WaterIntake)

#     # Render a template with the output or return it as JSON, etc.
#     return render_template('result.html', output=output)

@views.route("/generate", methods=["GET", "POST"])
@login_required
def generate():
    Steps = float(request.form.get("Steps"))
    weight = float(request.form.get("weight"))
    sleep_duration = float(request.form.get("sleep_duration"))
    calories_burn = float(request.form.get("calories_burn"))
    Water_Intake = float(request.form.get("Water_Intake"))

    #healthStatus, strategy = check_health(Steps, weight, sleep_duration, calories_burn, Water_Intake)
    UnHealthy, Healthy = calc(Steps, weight, sleep_duration, calories_burn, Water_Intake)

    return render_template("result.html", UnHealthy=UnHealthy, Healthy=Healthy, Steps=int(Steps), weight=int(weight), sleep_duration=int(sleep_duration), calories_burn=int(calories_burn), Water_Intake=int(Water_Intake))

# @views.route('/delete-note', methods=['POST'])
# def delete_note():  
#     note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})