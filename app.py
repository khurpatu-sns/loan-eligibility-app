from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("model/loan_model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    income = float(request.form["income"])
    age = float(request.form["age"])
    loan_amount = float(request.form["loan_amount"])
    credit_score = float(request.form["credit_score"])

    features = np.array([[income, age, loan_amount, credit_score]])
    scaled = scaler.transform(features)

    prediction = model.predict(scaled)[0]

    return render_template("result.html", pred=prediction)

if __name__ == "__main__":
    app.run()