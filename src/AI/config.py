import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    DEVICE_ID: int
    DAYS_BACK: int

    LAT: float
    LON: float

    MERGE_TOLERANCE_MINUTES: int
    TEST_SPLIT_RATIO: float
    RANDOM_STATE: int

def get_settings() -> Settings:
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL não está definido no .env")

    return Settings(
        DATABASE_URL=db_url,
        DEVICE_ID=int(os.getenv("DEVICE_ID", "1")),
        DAYS_BACK=int(os.getenv("DAYS_BACK", "7")),
        LAT=float(os.getenv("LAT", "38.569")),
        LON=float(os.getenv("LON", "-8.901")),
        MERGE_TOLERANCE_MINUTES=int(os.getenv("MERGE_TOLERANCE_MINUTES", "5")),
        TEST_SPLIT_RATIO=float(os.getenv("TEST_SPLIT_RATIO", "0.2")),
        RANDOM_STATE=int(os.getenv("RANDOM_STATE", "42")),
    )
