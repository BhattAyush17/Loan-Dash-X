# Loan-Dash X: Loan Approval Predictor

![Logo](static/logo.png)

Loan-Dash X is a machine learning-powered web application designed to predict the likelihood of loan approval for users based on their financial and personal information. Built using Python, Flask, and Scikit-learn, this project integrates a trained classification model to provide instant, data-driven feedback with a modern, user-friendly interface.

---

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Instant Loan Approval Prediction:**  
  Enter key details and get an immediate prediction of approval probability.

- **User-Friendly Interface:**  
  Modern, responsive design with clear guidance and validation.

- **Secure Input Validation:**  
  Both browser and backend checks for realistic financial ranges.

- **Customizable Model:**  
  Easily swap or retrain the underlying ML model for different datasets.

- **Scalable Architecture:**  
  Built with Flask for easy deployment and extension.

---

## Demo

*Add a link to a live demo or screenshots here.*

---

## Tech Stack

- **Frontend:** HTML, CSS (custom styles, Google Fonts)
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn (`loan_approval_pipeline.joblib`)
- **Deployment:** Joblib model serialization, Flask app
- **Other:** Pandas, Jinja2 templating

---

## How It Works

1. **User Input:**  
   Users fill out a form with:
   - Income (in thousands, up to ₹10 crore)
   - Credit Score (300-900)
   - Number of ongoing loans (0-20)
   - Age (18-75)
   - Gender

2. **Validation:**  
   Both browser (HTML min/max) and backend (Python) validation ensure meaningful input.

3. **Prediction:**  
   The Flask backend loads a pre-trained ML pipeline and predicts approval probability.

4. **Result Display:**  
   The user receives their loan approval chance as a percentage, along with any relevant feedback.

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BhattAyush17/Major-Project.git
   cd Major-Project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Train your own model:**
   - Prepare your dataset.
   - Train with a classification algorithm (e.g., Logistic Regression, Random Forest).
   - Export as `loan_approval_pipeline.joblib` to the `models/` directory.

4. **Run the application:**
   ```bash
   python app/app.py
   ```

5. **Access the app:**
   - Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## Usage

- Enter your details in the form.
- Click "Predict Approval".
- View your approval probability and suggestions.

---

## Project Structure

```
Major-Project/
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── logo.png
├── models/
│   └── loan_approval_pipeline.joblib
├── requirements.txt
└── README.md
```

---

## Model Details

- **Type:** Classification (binary: approval/not approval)
- **Algorithms used:** Logistic Regression, Random Forest, or XGBoost (configurable)
- **Features:** Income, credit score, loans ongoing, age, gender
- **Preprocessing:** Scaling, encoding, feature engineering (scikit-learn pipeline)
- **Evaluation:** Accuracy, ROC-AUC, F1-score (see training notebook for details)

---

## Screenshots

*Add screenshots here for the UI, including the logo and prediction form.*

---

## Contributing

Contributions are welcome!  
- Fork the repo
- Make your changes (feature, bugfix, documentation)
- Submit a pull request

---

## License

This project is licensed under the MIT License.

---

## Contact

- **Author:** [Ayush Bhatt](https://github.com/BhattAyush17)
- **Email:** *your-email@example.com*
- **LinkedIn:** [Ayush Bhatt](https://www.linkedin.com/in/ayushbhatt17/)

---

## Hashtags

```
#MachineLearning #LoanApproval #FinTech #Python #Flask #AI #DataScience #WebApp #CreditScore #MLModel #Finance #PredictiveAnalytics #MajorProject #OpenSource #SmartBanking #Innovation #TechForGood
```

---

*Empowering smarter lending decisions with data and AI!*
