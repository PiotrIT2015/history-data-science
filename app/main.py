import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# katalog app/
APP_DIR = Path(__file__).resolve().parent

# katalog główny projektu
BASE_DIR = APP_DIR.parent

# katalog data/
DATA_DIR = BASE_DIR / "data"

csv_path = DATA_DIR / "bitwy.csv"

df = pd.read_csv(csv_path)





st.set_page_config(page_title="Historia w Danych", layout="wide")

st.title("📜 Historia w Danych")
st.sidebar.header("Nawigacja")

# =========================
# ŁADOWANIE DANYCH
# =========================
@st.cache_data
def load_data():
    return pd.read_csv(csv_path)

df = load_data()

# =========================
# ANALIZA
# =========================
st.header("Analiza Bitew")

# wykres tylko jeśli mamy liczebność
df_plot = df.dropna(subset=["Liczebność"])

if not df_plot.empty:
    fig = px.bar(
        df_plot,
        x="Bitwa",
        y="Liczebność",
        color="Rok",
        title="Liczebność wojsk w kluczowych bitwach"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Brak danych o liczebności – wykres chwilowo niedostępny.")

# =========================
# FILTROWANIE
# =========================
st.subheader("Surowe dane")

rok_filter = st.slider(
    "Wybierz zakres lat",
    int(df["Rok"].min()),
    int(df["Rok"].max()),
    (int(df["Rok"].min()), int(df["Rok"].max()))
)

filtered_df = df[
    (df["Rok"] >= rok_filter[0]) &
    (df["Rok"] <= rok_filter[1])
]

st.dataframe(filtered_df, use_container_width=True)
