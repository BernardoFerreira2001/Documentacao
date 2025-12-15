#database.py
from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set in .env file")

#criar engine
engine = create_engine(DATABASE_URL, echo=False, connect_args={"charset":"utf8mb4"})

def create_db_and_tables():
    from models import Device, SensorReading, ActuatorState, Setting, ErrorLog
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
