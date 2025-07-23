# train_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Laad je eigen dataset
df = pd.read_excel("synthetische_verzuimdata.xlsx")

# Preprocessing
df_encoded = pd.get_dummies(df[['Geslacht', 'Afdeling']])
numerical = df[['Leeftijd', 'Dienstjaren', 'Verzuimdagen_12mnd',
                'ZiekteverzuimScore', 'MentaleBelastingScore',
                'FysiekeBelastingScore', 'WerktevredenheidScore']]
X = pd.concat([df_encoded, numerical], axis=1)
y = df['VerzuimKomtWaarschijnlijk']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Sla lokaal op met jouw sklearn-versie
joblib.dump(model, "model.pkl")
print("Model opgeslagen als model.pkl")
