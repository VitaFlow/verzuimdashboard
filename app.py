# app.py

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="VerzuimDashboard", layout="wide")

st.title("📊 VerzuimDashboard – Signaleer & Voorkom")

# Upload data
uploaded_file = st.file_uploader("📤 Upload medewerkersdata (.csv)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Ingevoerde Data")
    st.dataframe(df.head())

    if "verzuim" not in df.columns:
        st.warning("⚠️ Voeg een 'verzuim' kolom toe (1 = ziek, 0 = niet ziek) om voorspellingen te trainen.")
    else:
        # Laat statistieken zien
        st.subheader("📈 Algemene Statistieken")
        st.write(df.describe())

        # Visualisaties
        st.subheader("📊 Verzuim per afdeling")
        if 'afdeling' in df.columns:
            fig1, ax1 = plt.subplots()
            sns.countplot(data=df, x='afdeling', hue='verzuim', ax=ax1)
            st.pyplot(fig1)

        # Voorbeeldmodel bouwen
        st.subheader("🤖 Verzuimrisico Voorspellen met AI")
        feature_cols = [col for col in df.columns if col not in ['verzuim', 'naam', 'id']]
        X = df[feature_cols]
        y = df['verzuim']

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X, y)

        df['voorspelling'] = model.predict(X)
        df['risico (%)'] = model.predict_proba(X)[:, 1] * 100

        st.success("✅ AI-model getraind! Hieronder zie je de risico-inzichten.")
        st.dataframe(df[['naam'] + feature_cols + ['risico (%)']].sort_values(by='risico (%)', ascending=False))

        # Opslaan van model (optioneel)
        if st.button("💾 Sla AI-model op"):
            joblib.dump(model, "verzuim_model.pkl")
            st.success("Model opgeslagen als verzuim_model.pkl")

else:
    st.info("⬆️ Upload eerst een .csv-bestand met medewerkersdata om te starten.")
