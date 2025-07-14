# model.py
# Voor training van een los AI-model voor verzuimvoorspelling

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Laad dataset
df = pd.read_csv("data/voorbeeld.csv")

# Features en target
X = df.drop(columns=["verzuim", "id", "naam"])
y = df["verzuim"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model trainen
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Opslaan model
joblib.dump(model, "verzuim_model.pkl")

print("✅ Model opgeslagen als 'verzuim_model.pkl'")
