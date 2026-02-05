import pandas as pd
import requests

def fetch_open_meteo(lat: float, lon: float, start_ts: pd.Timestamp, end_ts: pd.Timestamp) -> pd.DataFrame:
    # garantir UTC
    if start_ts.tzinfo is None:
        start_ts = start_ts.tz_localize("UTC")
    else:
        start_ts = start_ts.tz_convert("UTC")

    if end_ts.tzinfo is None:
        end_ts = end_ts.tz_localize("UTC")
    else:
        end_ts = end_ts.tz_convert("UTC")

    start_date = start_ts.date().isoformat()
    end_date = end_ts.date().isoformat()

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relativehumidity_2m,precipitation,cloudcover",
        "timezone": "UTC",
        "start_date": start_date,
        "end_date": end_date,
    }

    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()
    data = r.json()

    hourly = data.get("hourly", {})
    times = hourly.get("time", [])
    if not times:
        return pd.DataFrame(columns=["timestamp", "out_temp", "out_humidity", "out_precip", "out_cloudcover"])

    df = pd.DataFrame({
        "timestamp": pd.to_datetime(times, utc=True),
        "out_temp": hourly.get("temperature_2m", [None] * len(times)),
        "out_humidity": hourly.get("relativehumidity_2m", [None] * len(times)),
        "out_precip": hourly.get("precipitation", [None] * len(times)),
        "out_cloudcover": hourly.get("cloudcover", [None] * len(times)),
    })

    # filtrar intervalo real
    df = df[(df["timestamp"] >= start_ts - pd.Timedelta(hours=1)) & (df["timestamp"] <= end_ts + pd.Timedelta(hours=1))]
    return df.sort_values("timestamp").reset_index(drop=True)
