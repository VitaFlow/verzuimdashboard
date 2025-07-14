
# 📊 Verzuimdashboard

Een Streamlit-dashboard waarmee HR-teams het risico op toekomstig verzuim onder medewerkers kunnen voorspellen en visualiseren. Gebouwd met een Random Forest Classifier op basis van HR-data.

## ⚙️ Functionaliteiten

- Upload je eigen Excelbestand met HR-kenmerken
- Voorspel verzuimrisico met behulp van AI
- Filter op afdeling en risicoklasse
- Visualiseer risicoverspreiding en risico per afdeling
- Download resultaten als CSV

## 🧠 Gebruikte Features

- Leeftijd, Geslacht, Afdeling, Dienstjaren
- Verzuimdagen laatste 12 maanden
- Scores: Ziekteverzuim, Mentale en Fysieke belasting, Werktevredenheid

## 🗂️ Structuur

```
verzuimdashboard/
│
├── app.py                # Streamlit frontend
├── model.py              # Model training + predictie
├── model.pkl             # Getraind model
├── requirements.txt      # Dependencies
└── synthetische_verzuimdata.xlsx  # Voorbeeldbestand
```

## ▶️ Installatie & Gebruik

1. Clone de repository:
```bash
git clone https://github.com/<VitaFlow>/verzuimdashboard.git
cd verzuimdashboard
```

2. Installeer vereisten:
```bash
pip install -r requirements.txt
```

3. Start de applicatie:
```bash
streamlit run app.py
```

4. Upload een Excelbestand met de volgende kolommen:
```
['Werknemer_ID', 'Leeftijd', 'Geslacht', 'Afdeling', 'Dienstjaren', 
 'Verzuimdagen_12mnd', 'ZiekteverzuimScore', 'MentaleBelastingScore',
 'FysiekeBelastingScore', 'WerktevredenheidScore', 'VerzuimKomtWaarschijnlijk']
```

Een voorbeeldbestand `synthetische_verzuimdata.xlsx` is meegeleverd.

## 📦 Export

Download in de app eenvoudig een CSV met risicoscores per medewerker.

---

🧠 Gemaakt met scikit-learn, pandas, Streamlit & Plotly.  
🔒 Alleen bedoeld voor educatieve/demo-doeleinden.
