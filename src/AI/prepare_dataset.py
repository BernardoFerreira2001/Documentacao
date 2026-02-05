import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text
from config import get_settings
from weather import fetch_open_meteo

# Potências (W)
W_LED = 10.0
W_FAN = 2.0
W_MIST = 8.0
W_PUMP = 12.0

def main():
    s = get_settings()
    engine = create_engine(s.DATABASE_URL, pool_pre_ping=True)

    sensors = pd.read_sql(
        text("""
            SELECT device_id, temperature, humidity_air, humidity_soil, timestamp
            FROM sensor_readings
            WHERE device_id = :device_id
              AND timestamp >= NOW() - INTERVAL :days DAY
            ORDER BY timestamp ASC
        """),
        engine,
        params={"device_id": s.DEVICE_ID, "days": s.DAYS_BACK},
    )

    actuators = pd.read_sql(
        text("""
            SELECT device_id, fan_state, mist_state, led_state, pump_state, mode, timestamp
            FROM actuator_states
            WHERE device_id = :device_id
              AND timestamp >= NOW() - INTERVAL :days DAY
            ORDER BY timestamp ASC
        """),
        engine,
        params={"device_id": s.DEVICE_ID, "days": s.DAYS_BACK},
    )

    if sensors.empty:
        raise RuntimeError("Sem dados em sensor_readings no intervalo DAYS_BACK.")
    if actuators.empty:
        raise RuntimeError("Sem dados em actuator_states no intervalo DAYS_BACK.")

    sensors["timestamp"] = pd.to_datetime(sensors["timestamp"], utc=True, errors="coerce")
    actuators["timestamp"] = pd.to_datetime(actuators["timestamp"], utc=True, errors="coerce")

    sensors = sensors.dropna(subset=["timestamp"]).sort_values("timestamp")
    actuators = actuators.dropna(subset=["timestamp"]).sort_values("timestamp")

    merged = pd.merge_asof(
        sensors,
        actuators,
        on="timestamp",
        by="device_id",
        direction="backward",
        tolerance=pd.Timedelta(minutes=s.MERGE_TOLERANCE_MINUTES),
    )

    for c in ["fan_state", "mist_state", "led_state", "pump_state"]:
        merged[c] = merged[c].ffill().fillna(0).astype(int)

    # Fonte externa (Palmela via Open-Meteo)
    start_ts = merged["timestamp"].min()
    end_ts = merged["timestamp"].max()

    weather_df = fetch_open_meteo(s.LAT, s.LON, start_ts, end_ts)

    if not weather_df.empty:
        merged = pd.merge_asof(
            merged.sort_values("timestamp"),
            weather_df.sort_values("timestamp"),
            on="timestamp",
            direction="backward",
            tolerance=pd.Timedelta(hours=2),
        )
    else:
        merged["out_temp"] = np.nan
        merged["out_humidity"] = np.nan
        merged["out_precip"] = np.nan
        merged["out_cloudcover"] = np.nan

    # Features temporais
    merged["hour"] = merged["timestamp"].dt.hour
    merged["day_of_week"] = merged["timestamp"].dt.dayofweek
    merged["is_night"] = ((merged["hour"] < 8) | (merged["hour"] >= 20)).astype(int)

    merged = merged.set_index("timestamp")
    merged["temp_avg_30min"] = merged["temperature"].rolling("30min", min_periods=1).mean()
    merged["humidity_air_avg_30min"] = merged["humidity_air"].rolling("30min", min_periods=1).mean()
    merged = merged.reset_index()

    merged["active_actuators"] = (
        merged["fan_state"] + merged["mist_state"] + merged["led_state"] + merged["pump_state"]
    )

    # consumo estimado (W)
    merged["energy_consumption"] = (
        merged["led_state"] * W_LED
        + merged["fan_state"] * W_FAN
        + merged["mist_state"] * W_MIST
        + merged["pump_state"] * W_PUMP
    ).astype(float)

    merged.to_csv("dataset_latest.csv", index=False)
    print(merged.tail(10))
    print("\n dataset_latest.csv criado/atualizado.")

if __name__ == "__main__":
    main()
