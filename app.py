from flask import Flask, render_template, request, flash
import joblib
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Use relative path for the model (works on Render and locally)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'loan_approval_pipeline.joblib')

# Try to load the model, handle version compatibility issues
try:
    model = joblib.load(MODEL_PATH)
    MODEL_LOADED = True
    print("Model loaded successfully!")
except Exception as e:
    print(f"Warning: Could not load model due to version compatibility: {e}")
    model = None
    MODEL_LOADED = False

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
    income = request.form.get('income')
    credit_score = request.form.get('credit_score')
    loans_ongoing = request.form.get('loans_ongoing')
    age = request.form.get('age')
    gender = request.form.get('gender')
    
    new_data = preprocess_input(income, credit_score, loans_ongoing, age, gender)
    if new_data is None:
        flash("Invalid input.")
        return render_template("result.html", prediction_text="0%")
    
    # If model couldn't load due to version compatibility, provide fallback
    if not MODEL_LOADED:
        # Simple heuristic-based prediction as fallback
        income_val = float(income)
        credit_score_val = float(credit_score)
        loans_ongoing_val = int(loans_ongoing)
        age_val = int(age)
        
        # Simple scoring algorithm
        score = 0
        if income_val > 50: score += 30
        elif income_val > 30: score += 20
        else: score += 10
        
        if credit_score_val > 750: score += 40
        elif credit_score_val > 650: score += 30
        elif credit_score_val > 550: score += 20
        else: score += 10
        
        if loans_ongoing_val == 0: score += 20
        elif loans_ongoing_val <= 2: score += 10
        
        if 25 <= age_val <= 45: score += 10
        
        pred_proba = min(score / 100, 1.0)
        flash("Note: Using fallback prediction algorithm due to model compatibility issues.")
        return render_template("result.html", prediction_text=f"{pred_proba:.0%}")
    
    # Use actual model prediction
    pred_proba = model.predict_proba(new_data)[0][1]
    return render_template("result.html", prediction_text=f"{pred_proba:.0%}")

if __name__ == "__main__":
    app.run(debug=True)