import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from pathlib import Path

BASE_URL = "https://pl.wikipedia.org"
CATEGORY_URL = f"{BASE_URL}/wiki/Kategoria:Bitwy_w_historii_Polski"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}

# =========================
# POMOCNICZE
# =========================

def extract_year(text):
    match = re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", text)
    return int(match.group(0)) if match else None


def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()


def get_infobox_value(infobox, field_names):
    """
    field_names: lista możliwych nazw pól (PL)
    """
    for row in infobox.select("tr"):
        header = row.find("th")
        value = row.find("td")

        if not header or not value:
            continue

        header_text = header.get_text(strip=True).lower()

        for field in field_names:
            if field in header_text:
                return clean_text(value.get_text(" ", strip=True))

    return None


# =========================
# LINKI DO BITEW
# =========================

def get_battle_links(limit=100):
    resp = requests.get(CATEGORY_URL, headers=HEADERS)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    links = []
    for a in soup.select(".mw-category-group a"):
        title = a.text.strip()
        href = a.get("href")

        if href and title:
            links.append((title, BASE_URL + href))

        if len(links) >= limit:
            break

    return links


# =========================
# SCRAPER
# =========================

def scrape_battles(limit=100):
    battles = get_battle_links(limit)
    rows = []

    for name, url in battles:
        try:
            r = requests.get(url, headers=HEADERS)
            r.raise_for_status()

            soup = BeautifulSoup(r.text, "html.parser")

            # --- rok ---
            content = soup.get_text(" ", strip=True)
            year = extract_year(content)

            # --- infobox ---
            infobox = soup.find("table", class_="infobox")

            winner = None
            forces = None

            if infobox:
                winner = get_infobox_value(
                    infobox,
                    ["zwycięzca", "wynik", "rezultat"]
                )

                forces = get_infobox_value(
                    infobox,
                    ["siły", "liczebność", "wojska", "armia"]
                )

            rows.append({
                "Bitwa": name,
                "Rok": year,
                "Zwycięzca": winner,
                "Liczebność": forces
            })

            time.sleep(1)

        except Exception as e:
            print(f"⚠️ Pominięto {name}: {e}")

    df = pd.DataFrame(rows)
    df = df.dropna(subset=["Rok"])

    return df


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    df = scrape_battles(limit=50)

    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    DATA_DIR.mkdir(exist_ok=True)

    csv_path = DATA_DIR / "bitwy.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8")

    print(f"✅ Zapisano {len(df)} bitew do {csv_path}")
