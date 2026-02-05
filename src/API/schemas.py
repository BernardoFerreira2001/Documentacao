#schemas.py
from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime

#---------- SENSOR ----------
class SensorCreate(SQLModel):
    temperature: float
    humidity_air: float
    humidity_soil: float

class SensorRead(SQLModel):
    id: int
    device_id: int
    temperature: float
    humidity_air: float
    humidity_soil: float
    timestamp: datetime

#---------- ACTUATORS ----------
class ActuatorCreate(SQLModel):
    fan_state: bool
    mist_state: bool
    led_state: bool
    pump_state: bool
    mode: str = "auto"
    source: Optional[str] = None

class ActuatorRead(SQLModel):
    id: int
    device_id: int
    fan_state: bool
    mist_state: bool
    led_state: bool
    pump_state: bool
    mode: str
    source: Optional[str]
    timestamp: datetime
