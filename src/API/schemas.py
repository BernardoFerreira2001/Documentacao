#schemas.py
from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime

class SensorCreate(SQLModel):
    device_id: int
    temperature: float
    humidity: float
    timestamp: Optional[datetime] = None

class SensorRead(SQLModel):
    id: int
    device_id: int
    temperature: float
    humidity: float
    timestamp: datetime

class ActuatorCreate(SQLModel):
    device_id: int
    fan_state: bool
    mist_state: bool
    led_state: bool
    mode: str = "auto"
    source: Optional[str] = None

class ActuatorRead(SQLModel):
    id: int
    device_id: int
    fan_state: bool
    mist_state: bool
    led_state: bool
    mode: str
    source: Optional[str]
    timestamp: datetime

class SettingCreate(SQLModel):
    device_id: int
    min_temp: Optional[float] = None
    max_temp: Optional[float] = None
    min_humidity: Optional[float] = None
    max_humidity: Optional[float] = None
    light_on_time: Optional[str] = None
    light_off_time: Optional[str] = None
