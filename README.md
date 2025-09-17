# Loan-Dash X: Loan Approval Predictor

**Loan-Dash X** is a machine learning-powered web application that predicts the likelihood of loan approval based on a user's financial and personal information. Built with Python and Flask, it leverages a robust ML pipeline to provide fast and reliable predictions, making it a valuable tool for both users and financial institutions.

## Demo

Experience Loan-Dash X in action with the live demo playback below. The video will start automatically for a quick preview right on this page.  
To watch in full screen or open on YouTube, simply click anywhere on the video area.

<div style="position:relative; width:560px; max-width:100%;">
  <a href="https://www.youtube.com/watch?v=IkQV3ysOAuc" target="_blank" style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:2;display:block;text-decoration:none;">
    <span style="display:none;">Watch on YouTube</span>
  </a>
  <iframe width="560" height="315"
    src="https://www.youtube.com/embed/IkQV3ysOAuc?autoplay=1"
    title="Loan-Dash X Demo"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen
    style="position:relative;z-index:1;">
  </iframe>
</div>

> Feel free to explore the screenshots below for hands-on experience.


## Table of Contents

- [Key Features](#key-features)
- [Demo](#demo)
- [Technology Stack](#technology-stack)
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

## Key Features

- **Instant Loan Approval Prediction:**  
  Receive immediate feedback on loan approval chances after submitting personal and financial details.

- **Intuitive, Responsive UI:**  
  Modern design and clear guidance for a seamless user experience on any device.

- **Robust Input Validation:**  
  Comprehensive checks on both the frontend and backend for realistic and secure data entry.

- **Modular & Customizable ML Model:**  
  Easily update or retrain the underlying model to suit different datasets and business requirements.

- **Scalable Architecture:**  
  Built with Flask for straightforward deployment and future expansion.

---

## Technology Stack

- **Frontend:** HTML, CSS (custom styles, Google Fonts)
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn (`loan_approval_pipeline.joblib`)
- **Deployment:** Joblib for model serialization, Flask app server
- **Additional Libraries:** Pandas, Jinja2 templating

---

## How It Works

1. **User Input:**  
   Users provide:
   - Income (in thousands, up to ₹10 crore)
   - Credit Score (300–900)
   - Number of ongoing loans (0–20)
   - Age (18–75)
   - Gender

2. **Validation:**  
   HTML constraints and Python backend checks ensure valid, meaningful data.

3. **Prediction:**  
   The Flask server loads a pre-trained ML pipeline to predict loan approval probability.

4. **Result Display:**  
   Users receive their approval chance as a percentage, along with actionable feedback.

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BhattAyush17/Loan-Dash-X.git
   cd Loan-Dash-X
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **(Optional) Train your own model:**
   - Prepare your dataset.
   - Train using your preferred classifier (e.g., Logistic Regression, Random Forest).
   - Export as `loan_approval_pipeline.joblib` to the `models/` directory.
4. **Run the application:**
   ```bash
   python app/app.py
   ```
5. **Access the app:**
   - Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Usage

1. Fill out the form with your details.
2. Click **Predict Approval**.
3. View your approval probability and personalized suggestions.

---

## Project Structure

```
Loan-Dash-X/
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

- **Type:** Binary Classification (Approval / Not Approval)
- **Algorithms:** Logistic Regression, Random Forest, XGBoost (configurable)
- **Features:** Income, Credit Score, Ongoing Loans, Age, Gender
- **Preprocessing:** Scaling, Encoding, Feature Engineering (scikit-learn pipeline)
- **Evaluation Metrics:** Accuracy, ROC-AUC, F1-score (see training notebook for details)

---

## Screenshots

<img width="974" height="977" alt="App Screenshot 1" src="https://github.com/user-attachments/assets/bc434e93-4ccc-4e98-885e-c59229da0f12" />
<img width="1066" height="688" alt="App Screenshot 2" src="https://github.com/user-attachments/assets/6ef4d4eb-4fae-4095-92b4-7f9dcd5bb3f4" />

---

## Contributing

We welcome your contributions!  
- **Fork** the repository
- **Create** your feature branch
- **Commit** your changes
- **Open** a pull request

For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

- **Author:** [Ayush Bhatt](https://github.com/BhattAyush17)


---

*Empowering smarter lending decisions with data and AI.*

---

**Tags:**  
_Machine Learning • Loan Approval • FinTech • Python • Flask • AI • Data Science • Web App • Credit Score • ML Model • Finance • Predictive Analytics • Open Source • Smart Banking • Innovation • Tech For Good_
