import streamlit as st
import pandas as pd
import plotly.express as px
from model import load_model, predict

st.set_page_config(layout='wide')
st.title("HR Verzuimvoorspeller Dashboard")

model = load_model("model.pkl")

uploaded_file = st.file_uploader("Upload Excelbestand met medewerkergegevens", type=["xlsx"])
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        df_pred = predict(model, df)

        st.subheader("📊 Samenvatting Data")
        st.write(df_pred.describe())

        afdelingen = st.multiselect("Filter op Afdeling", options=df_pred['Afdeling'].unique(), default=df_pred['Afdeling'].unique())
        risico_filter = st.multiselect("Filter op Risicoklasse", options=['Laag', 'Midden', 'Hoog'], default=['Laag', 'Midden', 'Hoog'])

        df_filtered = df_pred[df_pred['Afdeling'].isin(afdelingen) & df_pred['Risicoklasse'].isin(risico_filter)]

        st.subheader("📈 Verzuim Risicoverdeling")
        fig = px.histogram(df_filtered, x="Risicoscore", nbins=20, title="Histogram Risicoscore")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🏢 Gemiddeld risico per Afdeling")
        avg_risico = df_filtered.groupby("Afdeling")["Risicoscore"].mean().sort_values(ascending=False).reset_index()
        fig2 = px.bar(avg_risico, x="Afdeling", y="Risicoscore", title="Gemiddeld Risico per Afdeling")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("📥 Download Resultaten")
        csv = df_pred.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV met Risicoscores", csv, "verzuimresultaten.csv", "text/csv")
    except Exception as e:
        st.error(f"Fout bij verwerken bestand: {e}")
else:
    st.info("Upload een bestand om te beginnen.")

