# 📜 Historia w Danych – Ilościowa Analiza Przeszłości

## 📌 Opis projektu
**Historia w Danych** to interdyscyplinarny projekt analityczny, który rzuca nowe światło na wydarzenia historyczne poprzez pryzmat nowoczesnych metod Data Science. Projekt udowadnia, że historia nie jest tylko zbiorem dat i opisów, ale potężnym zbiorem danych, który można modelować, wizualizować i analizować statystycznie.

Projekt łączy w sobie:
* 📊 **Exploratory Data Analysis (EDA):** Wydobywanie trendów z nieoczywistych źródeł.
* 🗺️ **Geospatial Analysis:** Wizualizacja konfliktów i zmian granic na mapach.
* ✍️ **Data Storytelling:** Przekształcanie suchych liczb w angażującą narrację historyczną.
* 🕸️ **Network Analysis:** Badanie powiązań dynastycznych i dyplomatycznych.

---

## 🎯 Cele projektu
* **Kwantyfikacja historii:** Przekształcenie opisowych źródeł historycznych w ustrukturyzowane zestawy danych (CSV/JSON).
* **Analiza trendów:** Identyfikacja cykli stabilności i kryzysów na przestrzeni wieków.
* **Wizualizacja złożoności:** Tworzenie interaktywnych dashboardów ułatwiających zrozumienie procesów dziejowych.
* **Portfolio Building:** Prezentacja warsztatu pracy Data Scientista na unikalnym, autorskim zbiorze danych.

---

## 🧠 Zakres analiz

### ⚔️ Analiza konfliktów zbrojnych
* Statystyka bitew w poszczególnych epokach.
* Analiza skuteczności armii (zależność: liczebność vs. wynik).
* Korelacja między postępem technologicznym a skalą strat.

### 🗺️ Analiza geoprzestrzenna
* Interaktywne mapy punktowe bitew i kluczowych wydarzeń.
* Heatmapy natężenia konfliktów w danych regionach.
* Dynamiczne osie czasu obrazujące ekspansję terytorialną państw.

### 👑 Władcy i Dynastie
* Analiza długości panowania (rozłady prawdopodobieństwa, średnie).
* Grafy relacji rodzinnych i wpływów dynastycznych.
* Badanie okresów bezkrólewia i ich wpływu na stabilność państwa.

---

## 🧰 Technologie
* **Język:** Python (Pandas, NumPy, Scipy)
* **Wizualizacja:** * `Plotly` (interaktywne wykresy i mapy)
    * `Matplotlib` / `Seaborn` (statyczna analiza EDA)
* **Środowisko:** Jupyter Notebook
* **Geodata:** Geopandas / Folium

---

## 🏗️ Struktura repozytorium
```text
historia-w-danych/
├── data/                   # Surowe i przetworzone zbiory danych (CSV, GeoJSON)
├── notebooks/              # Dokumentacja procesu analitycznego
│   ├── 01_eda_battles.ipynb
│   ├── 02_geospatial_viz.ipynb
│   └── 03_network_analysis.ipynb
├── visuals/                # Wygenerowane wykresy i dashboardy
├── scripts/                # Skrypty do scrapowania/czyszczenia danych
└── README.md