from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import sessionmaker, Session, declarative_base
import uvicorn

# =========================
# CONFIGURACIÓN DE NÚCLEO (FIXED)
# =========================
DATABASE_URL = "sqlite:///./aih_hse_vault.db"

# Fix para SQLite: check_same_thread=False es vital para FastAPI
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(title="AIHumanity HSE Master API")

# =========================
# MODELO DE BASE DE DATOS
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

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# =========================
# SCHEMAS DE ENTRADA (PYDANTIC V2 FIX)
# =========================
class SensorInput(BaseModel):
    # Usamos ConfigDict para compatibilidad total con Pydantic v2 de tu inventario
    model_config = ConfigDict(from_attributes=True)
    
    worker_id: str
    location: str
    pm25: float
    humidity: float
    wind_speed: float
    helmet_status: str  # "ON" or "OFF"

# Inyección de Dependencia de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# MOTOR DE RIESGO (ICR)
# =========================
def calculate_risk(pm25, humidity, wind_speed, helmet_status):
    risk = (pm25 * 0.3) + (humidity * 0.1) + (wind_speed * 0.2)
    if helmet_status.upper() == "OFF":
        risk += 30
    return round(min(risk, 100), 2)

# =========================
# ENDPOINTS LIMPIOS
# =========================

@app.post("/ingest")
def ingest_data(data: SensorInput, db: Session = Depends(get_db)):
    try:
        icr = calculate_risk(data.pm25, data.humidity, data.wind_speed, data.helmet_status)
        
        # Convertir Pydantic a SQLAlchemy Model
        db_record = SensorData(
            worker_id=data.worker_id,
            location=data.location,
            pm25=data.pm25,
            humidity=data.humidity,
            wind_speed=data.wind_speed,
            helmet_status=data.helmet_status,
            risk_index=icr
        )
        
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return {"status": "SUCCESS", "risk_index": icr}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/dashboard")
def get_dashboard(db: Session = Depends(get_db)):
    records = db.query(SensorData).all()
    if not records:
        return {"total_events": 0, "average_risk": 0, "global_status": "NO_DATA"}

    avg_risk = sum(r.risk_index for r in records) / len(records)
    
    return {
        "total_events": len(records),
        "average_risk": round(avg_risk, 2),
        "global_status": "STOP_WORK" if avg_risk > 80 else "WARNING" if avg_risk > 50 else "SAFE"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
