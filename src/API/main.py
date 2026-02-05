from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# --------------------------------------------------
# ENV
# --------------------------------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI(title="GrowLab API")

# --------------------------------------------------
# Pydantic Schemas
# --------------------------------------------------

class SensorData(BaseModel):
    temperature: float
    humidity_air: float
    humidity_soil: float

class ActuatorData(BaseModel):
    fan_state: int
    mist_state: int
    led_state: int
    pump_state: int
    mode: str      # auto | manual
    source: str    # esp32 | blynk

# --------------------------------------------------
# SENSOR ENDPOINT
# --------------------------------------------------
@app.post("/devices/{device_id}/sensor")
def add_sensor_reading(device_id: int, data: SensorData):
    try:
        db = SessionLocal()

        query = text("""
            INSERT INTO sensor_readings
            (device_id, temperature, humidity_air, humidity_soil)
            VALUES
            (:device_id, :temperature, :humidity_air, :humidity_soil)
        """)

        db.execute(query, {
            "device_id": device_id,
            "temperature": data.temperature,
            "humidity_air": data.humidity_air,
            "humidity_soil": data.humidity_soil
        })

        db.commit()
        db.close()

        return {"status": "OK"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --------------------------------------------------
# ACTUATORS ENDPOINT
# --------------------------------------------------
@app.post("/devices/{device_id}/actuators")
def add_actuator_state(device_id: int, data: ActuatorData):
    try:
        db = SessionLocal()

        query = text("""
            INSERT INTO actuator_states
            (device_id, fan_state, mist_state, led_state, pump_state, mode, source)
            VALUES
            (:device_id, :fan_state, :mist_state, :led_state, :pump_state, :mode, :source)
        """)

        db.execute(query, {
            "device_id": device_id,
            "fan_state": data.fan_state,
            "mist_state": data.mist_state,
            "led_state": data.led_state,
            "pump_state": data.pump_state,
            "mode": data.mode,
            "source": data.source
        })

        db.commit()
        db.close()

        return {"status": "OK"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
