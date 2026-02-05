import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATASET_PATH = os.getenv("DATASET_PATH", "dataset_latest.csv")
DAYS = int(os.getenv("DAYS", "7"))

# Intervalo entre registos em segundos (se não existir no dataset, vamos estimar)
DEFAULT_INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS", "30"))

def main():
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(
            f"Não encontrei o ficheiro '{DATASET_PATH}'. "
            "Corre primeiro: python prepare_dataset.py"
        )

    df = pd.read_csv(DATASET_PATH)

    if "timestamp" not in df.columns:
        raise RuntimeError("O dataset não tem a coluna 'timestamp'.")

    if "energy_consumption" not in df.columns:
        raise RuntimeError("O dataset não tem a coluna 'energy_consumption' (W).")

    # Garantir timestamp como datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    df = df.dropna(subset=["timestamp"])

    # Filtrar últimos  dias
    end_time = df["timestamp"].max()
    start_time = end_time - pd.Timedelta(days=DAYS)
    df_7 = df[df["timestamp"] >= start_time].copy()

    if df_7.empty:
        print(f"⚠️ Não há registos nos últimos {DAYS} dias.")
        return

    # Ordenar por tempo
    df_7 = df_7.sort_values("timestamp")

    # Calcular delta_t (segundos) entre registos
    df_7["delta_seconds"] = df_7["timestamp"].diff().dt.total_seconds()

    # Corrigir valores inválidos
    df_7["delta_seconds"] = df_7["delta_seconds"].fillna(DEFAULT_INTERVAL_SECONDS)

    # Evitar intervalos absurdos
    # Se o delta for maior que 5 minutos, assume o intervalo padrão
    df_7.loc[df_7["delta_seconds"] > 300, "delta_seconds"] = DEFAULT_INTERVAL_SECONDS
    df_7.loc[df_7["delta_seconds"] <= 0, "delta_seconds"] = DEFAULT_INTERVAL_SECONDS

    # Energia (Wh) por registo = W * (segundos / 3600)
    df_7["energy_Wh"] = df_7["energy_consumption"] * (df_7["delta_seconds"] / 3600.0)

    total_Wh = df_7["energy_Wh"].sum()
    total_kWh = total_Wh / 1000.0

  
    df_7["date"] = df_7["timestamp"].dt.date
    daily_Wh = df_7.groupby("date")["energy_Wh"].sum().reset_index()
    daily_Wh["energy_kWh"] = daily_Wh["energy_Wh"] / 1000.0

    print(f"\n=== CONSUMO ESTIMADO (últimos {DAYS} dias) ===")
    print(f"Período: {start_time}  →  {end_time}")
    print(f"Total: {total_Wh:.2f} Wh  |  {total_kWh:.4f} kWh")

    print("\n=== CONSUMO POR DIA ===")
    print(daily_Wh.to_string(index=False))

    # Guardar CSV 
    out_csv = f"consumption_last_{DAYS}_days.csv"
    daily_Wh.to_csv(out_csv, index=False)
    print(f"\n Ficheiro criado: {out_csv}\n")

if __name__ == "__main__":
    main()
