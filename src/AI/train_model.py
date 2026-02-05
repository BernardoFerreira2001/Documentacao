import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
import joblib
from config import get_settings

FEATURES = [
    "temperature",
    "humidity_air",
    "humidity_soil",
    "out_temp",
    "out_humidity",
    "out_precip",
    "out_cloudcover",
    "hour",
    "day_of_week",
    "is_night",
    "temp_avg_30min",
    "humidity_air_avg_30min",
    "active_actuators",
    "fan_state",
    "mist_state",
    "led_state",
    "pump_state",
]

TARGET = "energy_consumption"

def main():
    s = get_settings()

    df = pd.read_csv("dataset_latest.csv")
    if df.empty:
        raise RuntimeError("dataset_latest.csv está vazio. Corre primeiro prepare_dataset.py")

    # Garantir que as colunas existem
    missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
    if missing:
        raise RuntimeError(f"Faltam colunas no dataset: {missing}")

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=s.TEST_SPLIT_RATIO, random_state=s.RANDOM_STATE
    )

    baseline_pred = np.repeat(y_train.mean(), len(y_test))
    baseline_mae = mean_absolute_error(y_test, baseline_pred)

    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("rf", RandomForestRegressor(
            n_estimators=200,
            random_state=s.RANDOM_STATE,
            n_jobs=-1
        ))
    ])

    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, pred)
    rmse = mean_squared_error(y_test, pred) ** 0.5

    print("=== AVALIAÇÃO DO MODELO ===")
    print(f"Baseline MAE : {baseline_mae:.2f} W")
    print(f"Modelo MAE   : {mae:.2f} W")
    print(f"Modelo RMSE  : {rmse:.2f} W")

    joblib.dump(model, "energy_model.pkl")
    print("\n Modelo guardado em energy_model.pkl")

if __name__ == "__main__":
    main()
