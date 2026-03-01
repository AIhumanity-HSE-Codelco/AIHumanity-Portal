# aihumanity-master-hse/config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

FIREBASE_CREDS_PATH = os.getenv('FIREBASE_CREDS_PATH', 'path/to/firebase-creds.json')
DATABASE_URL = os.getenv('DATABASE_URL', 'https://your-db.firebaseio.com')
DARK_MODE = True  # Toggle for dark mode in UI
ICR_THRESHOLD = 70  # Below this, trigger alert
# aihumanity-master-hse/config/logging.py
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_alert(node_id, icr, data):
    logger.warning(f"Alert for node {node_id}: ICR={icr}, Data={data}")
    # Integrate with Firebase or external service if needed
# aihumanity-master-hse/core/__init__.py
# Empty init for package# aihumanity-master-hse/core/analytics/wave_analyzer.py
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class RiskPredictor:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.scaler = StandardScaler()
        self.trained = False

    def train(self, historical_df):
        if historical_df.empty:
            return False
        X = historical_df.drop('risk_label', axis=1, errors='ignore').values
        if len(X) < 2:  # Need at least some data
            return False
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled)
        self.trained = True
        return True

    def predict_risk(self, current_data):
        if not self.trained:
            return 50
        
        X_current = np.array([[current_data.get('temp', 0), current_data.get('dust', 0),
                               current_data.get('light', 0), current_data.get('epp', 0),
                               current_data.get('heart_rate', 0)]])
        X_scaled = self.scaler.transform(X_current)
        anomaly = self.model.predict(X_scaled)[0]
        decision = self.model.decision_function(X_scaled)[0]
        icr = 100 if anomaly == 1 else max(0, 100 + (decision * 100))  # Adjusted for 0-100 scale
        return icr# aihumanity-master-hse/core/models/schemas.py
from pydantic import BaseModel
from typing import Optional

class NodeData(BaseModel):
    temp: float
    dust: float
    light: float
    epp: bool
    heart_rate: Optional[float] = None
    timestamp: Optional[int] = None

class RiskIndex(BaseModel):
    icr: float
    node_id: str
    alert: bool = False# aihumanity-master-hse/core/repositories/firebase_repo.py
import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
from datetime import datetime, timedelta
from config.settings import FIREBASE_CREDS_PATH, DATABASE_URL

cred = credentials.Certificate(FIREBASE_CREDS_PATH)
firebase_admin.initialize_app(cred, {'databaseURL': DATABASE_URL})

def fetch_historical_data(node_id, days_back=30):
    ref = db.reference(f'nodes/{node_id}/history')
    data = ref.get()
    
    if not data:
        return pd.DataFrame()
    
    df = pd.DataFrame.from_dict(data, orient='index')
    df.index = pd.to_datetime(df.index, unit='s', errors='coerce')
    df = df.sort_index().last(pd.Timedelta(days=days_back))
    df['risk_label'] = df.get('accident', 0)
    features = ['temp', 'dust', 'light', 'epp', 'heart_rate', 'risk_label']
    df = df[[col for col in features if col in df.columns]]
    return df

def get_real_time_data(node_id):
    ref = db.reference(f'nodes/{node_id}/realtime')
    return ref.get() or {}  # Return dict of current data

def save_alert(node_id, icr, data):
    ref = db.reference(f'alerts/{node_id}/{int(datetime.now().timestamp())}')
    ref.set({'icr': icr, 'data': data, 'message': 'Tendencia peligrosa detectada'})# aihumanity-master-hse/utils/autonomy.py
import socket

def check_network_autonomy():
    try:
        socket.gethostbyname('google.com')
        return 'Online'
    except:
        # Fallback to local network (e.g., 192.168.4.1)
        return 'Offline - Using local network'# aihumanity-master-hse/utils/helpers.py
import asyncio

async def async_fetch_data(func, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, func, *args)# aihumanity-master-hse/app/__init__.py
# Empty init# aihumanity-master-hse/app/main.py
import streamlit as st
from app.pages import dashboard, alerts, nodes, reports

PAGES = {
    "Dashboard": dashboard,
    "Alerts": alerts,
    "Nodes Management": nodes,
    "Reports": reports
}

st.sidebar.title("AIHumanity HSE")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()# aihumanity-master-hse/app/pages/dashboard.py
import streamlit as st
import plotly.express as px
from core.services.risk_service import get_icr
from core.repositories.firebase_repo import get_real_time_data
from config.settings import DARK_MODE

def app():
    if DARK_MODE:
        st.markdown('<style>body {background-color: #121212; color: #fff;}</style>', unsafe_allow_html=True)
    
    st.title("Dashboard Principal")
    node_id = st.selectbox("Selecciona Nodo", ["node1", "node2"])  # Fetch dynamically in prod
    
    if st.button("Calcular ICR"):
        icr = get_icr(node_id, retrain=True)
        st.metric("Índice de Control de Riesgo (ICR)", f"{icr}/100")
        if icr < 70:
            st.error("¡Alerta! Tendencia peligrosa.")
    
    data = get_real_time_data(node_id)
    if data:
        df = pd.DataFrame([data])
        fig = px.line(df, title="Ondas de Datos en Tiempo Real")
        st.plotly_chart(fig)# aihumanity-master-hse/app/pages/alerts.py
import streamlit as st
from firebase_admin import db
from config.settings import DATABASE_URL

def app():
    st.title("Alertas")
    ref = db.reference('alerts')
    alerts = ref.get()
    if alerts:
        for node, alert_data in alerts.items():
            st.subheader(f"Nodo: {node}")
            for ts, data in alert_data.items():
                st.write(f"Timestamp: {ts}, ICR: {data['icr']}, Mensaje: {data['message']}")
    else:
        st.info("No hay alertas activas.")
