from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# =========================
# CONFIGURACIÓN BASE
# =========================

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

app = FastAPI(title="AIHumanity HSE Control Center")

# =========================
# MODELOS BASE DATOS
# =========================

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(String)
    location = Column(String)
    pm25 = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    helmet_status = Column(String)
    risk_index = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# =========================
# MODELO DE INGESTIÓN
# =========================

class SensorInput(BaseModel):
    worker_id: str
    location: str
    pm25: float
    humidity: float
    wind_speed: float
    helmet_status: str  # "ON" or "OFF"

# =========================
# MOTOR RIESGO PROGRESIVO
# =========================

def calculate_risk(pm25, humidity, wind_speed, helmet_status):
    risk = 0

    risk += pm25 * 0.3
    risk += humidity * 0.1
    risk += wind_speed * 0.2

    if helmet_status == "OFF":
        risk += 30

    return min(risk, 100)

# =========================
# ENDPOINT INGESTIÓN
# =========================

@app.post("/ingest")
def ingest_data(data: SensorInput):
    db = SessionLocal()

    risk_index = calculate_risk(
        data.pm25,
        data.humidity,
        data.wind_speed,
        data.helmet_status
    )

    record = SensorData(
        worker_id=data.worker_id,
        location=data.location,
        pm25=data.pm25,
        humidity=data.humidity,
        wind_speed=data.wind_speed,
        helmet_status=data.helmet_status,
        risk_index=risk_index
    )

    db.add(record)
    db.commit()
    db.close()

    return {
        "status": "Data received",
        "risk_index": risk_index
    }

# =========================
# DASHBOARD GLOBAL
# =========================

@app.get("/dashboard")
def get_dashboard():
    db = SessionLocal()
    records = db.query(SensorData).all()

    total = len(records)
    avg_risk = sum(r.risk_index for r in records) / total if total else 0

    db.close()

    return {
        "total_events": total,
        "average_risk": round(avg_risk, 2),
        "global_status": "STOP_WORK" if avg_risk > 80 else "WARNING" if avg_risk > 50 else "SAFE"
    }
