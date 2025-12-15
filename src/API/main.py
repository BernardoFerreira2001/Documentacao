from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# --------------------------------------------------
# CARREGAR .ENV
# --------------------------------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI(title="GrowLab API")

# --------------------------------------------------
# MODELOS (Pydantic)
# --------------------------------------------------

class SensorData(BaseModel):
    temperature: float
    humidity: float

class ActuatorData(BaseModel):
    fan_state: int
    mist_state: int
    led_state: int
    mode: str      # "auto" ou "manual"
    source: str    # "esp32", "blynk", etc.


# --------------------------------------------------
# ENDPOINT: SENSOR READING
# --------------------------------------------------
@app.post("/devices/{device_id}/sensor")
def add_sensor_reading(device_id: int, data: SensorData):
    try:
        db = SessionLocal()

        query = text("""
            INSERT INTO sensor_readings (device_id, temperature, humidity)
            VALUES (:device_id, :temperature, :humidity)
        """)

        db.execute(query, {
            "device_id": device_id,
            "temperature": data.temperature,
            "humidity": data.humidity
        })

        db.commit()
        db.close()

        return {"status": "OK", "device": device_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --------------------------------------------------
# ENDPOINT: ACTUATORS
# --------------------------------------------------
@app.post("/devices/{device_id}/actuators")
def add_actuator_state(device_id: int, data: ActuatorData):
    try:
        db = SessionLocal()

        query = text("""
            INSERT INTO actuator_states
            (device_id, fan_state, mist_state, led_state, mode, source)
            VALUES
            (:device_id, :fan_state, :mist_state, :led_state, :mode, :source)
        """)

        db.execute(query, {
            "device_id": device_id,
            "fan_state": data.fan_state,
            "mist_state": data.mist_state,
            "led_state": data.led_state,
            "mode": data.mode,
            "source": data.source
        })

        db.commit()
        db.close()

        return {"status": "OK", "device": device_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
