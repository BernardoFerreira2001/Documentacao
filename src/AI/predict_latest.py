import pandas as pd
import joblib

FEATURES = [
    "temperature","humidity_air","humidity_soil",
    "out_temp","out_humidity","out_precip","out_cloudcover",
    "hour","day_of_week","is_night",
    "temp_avg_30min","humidity_air_avg_30min",
    "active_actuators","fan_state","mist_state","led_state","pump_state"
]

def main():
    model = joblib.load("energy_model.pkl")
    df = pd.read_csv("dataset_latest.csv")

    last = df.tail(1)
    x = last[FEATURES]
    pred = model.predict(x)[0]

    print("=== PREVISÃO (último registo) ===")
    print(last[["timestamp","energy_consumption"]])
    print(f"Previsto: {pred:.2f} W")

if __name__ == "__main__":
    main()
