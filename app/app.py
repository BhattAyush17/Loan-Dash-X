from flask import Flask, render_template, request, flash
import joblib
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'loan_approval_pipeline.joblib')

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Model loading failed: {e}")

def preprocess_input(income, credit_score, loans_ongoing, age, gender):
    try:
        income = float(income)
        credit_score = float(credit_score)
        loans_ongoing = int(loans_ongoing)
        age = int(age)
        gender = gender
    except Exception:
        return None
    return pd.DataFrame({
        "income": [income],
        "credit_score": [credit_score],
        "loans_ongoing": [loans_ongoing],
        "age": [age],
        "gender": [gender]
    })

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        flash("Model not loaded. Please contact admin.")
        return render_template("result.html", prediction_text="Error")
    income = request.form.get('income')
    credit_score = request.form.get('credit_score')
    loans_ongoing = request.form.get('loans_ongoing')
    age = request.form.get('age')
    gender = request.form.get('gender')
    new_data = preprocess_input(income, credit_score, loans_ongoing, age, gender)
    if new_data is None:
        flash("Invalid input.")
        return render_template("result.html", prediction_text="0%")
    try:
        pred_proba = model.predict_proba(new_data)[0][1]
        return render_template("result.html", prediction_text=f"{pred_proba:.0%}")
    except Exception as e:
        flash(f"Prediction failed: {e}")
        return render_template("result.html", prediction_text="Error")
