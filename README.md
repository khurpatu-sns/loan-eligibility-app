# 📘 Loan Eligibility Prediction Web App

A complete **Machine Learning + Flask** based web application that predicts whether a user is eligible for a loan based on their financial and personal details.

This project is perfect for:
- Machine Learning beginners to advance their skills  
- Students building portfolio projects  
- Developers learning Flask deployment  
- Resume-ready ML application  

---

## 📂 Project Structure
loan-eligibility-app/
│── app.py
│── requirements.txt
│── README.md
│── model/
│ └── loan_model.pkl
│── templates/
│ ├── index.html
│ └── result.html
│── static/
└── bootstrap.min.css


---

## 🚀 Features

- Clean and modern Bootstrap UI  
- Logistic Regression ML model  
- Real-time loan eligibility prediction  
- Flask backend API  
- 100% deployable on Render / Railway  
- Easy to clone and run locally  

---

# 🔧 1. How to Clone This Project

Open a terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/loan-eligibility-app.git
cd loan-eligibility-app

create virtual environment
python3 -m venv venv
source venv/bin/activate

Install Required Packages
pip install -r requirements.txt

python train_model.py


How to Use the Web App
Open your browser
Enter: http://127.0.0.1:5000
Fill the form details:
Gender
Marital status
Applicant Income
Coapplicant Income
Loan Amount
Dependents
Credit History
Employment Status
Click Predict Loan Eligibility
Result displayed:
✔ Loan Approved
❌ Loan Not Approved