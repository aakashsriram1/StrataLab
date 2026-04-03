import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score

from ingestion.fred import get_cpi

df = get_cpi().dropna()

df["target"] = (df["mom_change"].shift(-1) > 0.9).astype(int)

for i in range(1, 7):
    df[f"lag_{i}"] = df["mom_change"].shift(i)

df = df.dropna()

print(f"Class distribution:\n{df['target'].value_counts()}\n")

feature_cols = [f"lag_{i}" for i in range(1, 7)]
X = df[feature_cols]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=29
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print(f"Accuracy:  {round(accuracy_score(y_test, y_pred), 2)}")
print(f"Precision: {round(precision_score(y_test, y_pred, zero_division=0), 2)}")
print(f"Recall:    {round(recall_score(y_test, y_pred, zero_division=0), 2)}")
print(f"F1 Score:  {round(f1_score(y_test, y_pred, zero_division=0), 2)}")
print(f"AUC:       {round(roc_auc_score(y_test, y_prob), 2)}")

print(f"\nModel probability that March CPI > 0.9%: {model.predict_proba(scaler.transform(X.tail(1)))[0][1]:.1%}")

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.figure()
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc_score(y_test, y_prob):.2f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("CPI > 0.9% Prediction — ROC Curve")
plt.legend()
plt.show()