# models.py
from sqlmodel import SQLModel, Field, Column
from typing import Optional
from datetime import datetime
from sqlalchemy import TIMESTAMP

class Device(SQLModel, table=True):
    __tablename__ = "devices"
    device_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    location: Optional[str] = None
    created_at: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    )

class SensorReading(SQLModel, table=True):
    __tablename__ = "sensor_readings"
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: int = Field(foreign_key="devices.device_id")

    temperature: float
    humidity_air: float
    humidity_soil: float

    timestamp: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    )

class ActuatorState(SQLModel, table=True):
    __tablename__ = "actuator_states"
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: int = Field(foreign_key="devices.device_id")

    fan_state: bool
    mist_state: bool
    led_state: bool
    pump_state: bool

    mode: str              # auto | manual
    source: Optional[str]  # esp32 | blynk | api

    timestamp: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    )

class Setting(SQLModel, table=True):
    __tablename__ = "settings"
    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: int = Field(foreign_key="devices.device_id")

    min_temp: float = 20.0
    max_temp: float = 28.0
    min_humidity: float = 40.0
    max_humidity: float = 75.0

    light_on_time: Optional[str] = "08:00:00"
    light_off_time: Optional[str] = "20:00:00"

    updated_at: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(
            TIMESTAMP,
            server_default="CURRENT_TIMESTAMP",
            onupdate="CURRENT_TIMESTAMP"
        )
    )

class ErrorLog(SQLModel, table=True):
    __tablename__ = "error_logs"
    id: Optional[int] = Field(default=None, primary_key=True)
    level: str = Field(default="INFO")
    message: str
    created_at: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    )

