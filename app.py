from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import uvicorn

# =========================
# CONFIGURACIÓN INDUSTRIAL
# =========================
DATABASE_URL = "sqlite:///./aih_hse_vault.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(title="AIHumanity HSE Master API", version="5.0.0")

# Habilitar comunicación con la UI (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# MODELOS DE PERSISTENCIA (DB)
# =========================
class SensorData(Base):
    __tablename__ = "telemetry_logs"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(String, index=True)
    location = Column(String)
    pm25 = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    helmet_status = Column(String)
    risk_index = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# =========================
# SCHEMAS DE VALIDACIÓN (PYDANTIC)
# =========================
class SensorInput(BaseModel):
    worker_id: str = Field(..., example="W-70K-001")
    location: str = Field(..., example="Sector_Chancado_Norte")
    pm25: float = Field(..., gt=0)
    humidity: float = Field(..., ge=0, le=100)
    wind_speed: float = Field(..., ge=0)
    helmet_status: str = Field(..., pattern="^(ON|OFF)$")

# Dependencia para manejo de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# MOTOR DE RIESGO PREVENTIVO (ICR)
# =========================
def calculate_risk_index(data: SensorInput) -> float:
    # Lógica de pesos proporcionales HSE
    score = (data.pm25 * 0.4) + (data.humidity * 0.1) + (data.wind_speed * 0.2)
    if data.helmet_status == "OFF":
        score += 30.0  # Penalización crítica por EPP
    return round(min(score, 100.0), 2)

# =========================
# ENDPOINTS (INGESTIÓN & CONTROL)
# =========================

@app.post("/ingest", status_code=201)
def post_telemetry(data: SensorInput, db: Session = Depends(get_db)):
    try:
        calculated_icr = calculate_risk_index(data)
        
        new_record = SensorData(
            **data.model_dump(),
            risk_index=calculated_icr
        )
        
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return {"status": "SUCCESS", "record_id": new_record.id, "icr": calculated_icr}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database Sync Error: {str(e)}")

@app.get("/dashboard/summary")
def get_global_status(db: Session = Depends(get_db)):
    records = db.query(SensorData).all()
    if not records:
        return {"status": "NO_DATA", "avg_risk": 0}

    avg_risk = sum(r.risk_index for r in records) / len(records)
    
    # Lógica de semáforo HSE
    state = "SAFE (GREEN)"
    if avg_risk > 75: state = "CRITICAL (RED) - STOP WORK"
    elif avg_risk > 45: state = "WARNING (YELLOW)"

    return {
        "active_nodes": len(records),
        "global_icr": round(avg_risk, 2),
        "alert_level": state,
        "last_update": datetime.utcnow()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
