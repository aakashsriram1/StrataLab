import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"
API_KEY = os.getenv("FRED_API_KEY")
if API_KEY:
    print("API Key loaded successfully!")
else:
    print("Error: API Key not found.")

def get_cpi() -> pd.DataFrame:
    url = (
        f"{FRED_BASE}"
        f"?series_id=CPIAUCSL"
        f"&api_key={API_KEY}"
        f"&file_type=json"
        f"&observation_start=2020-01-01"
    )
    r = requests.get(url)
    r.raise_for_status()
    
    df = pd.DataFrame(r.json()["observations"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])
    df = df[["date", "value"]].dropna().reset_index(drop=True)
    df["mom_change"] = df["value"].pct_change() * 100
    
    return df

if __name__ == "__main__":
    df = get_cpi()
    print(df.tail(10))