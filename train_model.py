import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.DataFrame({
    'income': [20000, 40000, 60000, 80000, 25000, 50000, 75000],
    'age':    [25, 35, 45, 30, 22, 40, 50],
    'loan_amount': [5000, 10000, 20000, 12000, 4000, 15000, 25000],
    'credit_score': [300, 600, 700, 650, 250, 680, 720],
    'eligible': [0, 1, 1, 1, 0, 1, 1]
})

X = data.drop("eligible", axis=1)
y = data["eligible"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model/loan_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("Model trained and saved!")