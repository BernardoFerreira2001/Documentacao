import pandas as pd
from sqlalchemy import create_engine, text
from config import get_settings

def load_sensor_data():
    s = get_settings()
    engine = create_engine(s.DATABASE_URL, pool_pre_ping=True)

    q = text("""
        SELECT device_id, temperature, humidity_air, humidity_soil, timestamp
        FROM sensor_readings
        WHERE device_id = :device_id
        ORDER BY timestamp DESC
        LIMIT 10
    """)
    return pd.read_sql(q, engine, params={"device_id": s.DEVICE_ID})

def load_actuator_data():
    s = get_settings()
    engine = create_engine(s.DATABASE_URL, pool_pre_ping=True)

    q = text("""
        SELECT device_id, fan_state, mist_state, led_state, pump_state, mode, source, timestamp
        FROM actuator_states
        WHERE device_id = :device_id
        ORDER BY timestamp DESC
        LIMIT 10
    """)
    return pd.read_sql(q, engine, params={"device_id": s.DEVICE_ID})

if __name__ == "__main__":
    sensors = load_sensor_data()
    actuators = load_actuator_data()

    print("=== ÚLTIMOS 10 SENSORES ===")
    print(sensors)

    print("\n=== ÚLTIMOS 10 ATUADORES ===")
    print(actuators)
