from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import datetime
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TrafficData(BaseModel):
    attack_type: str = "normal"
    packets_per_second: int

@app.post("/predict")
async def predict_traffic(traffic: TrafficData):
    # Simulate Edge AI Processing delay
    await asyncio.sleep(0.0032)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Generate a completely dynamic, realistic attacker IP signature
    source_ip = f"{random.randint(11, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    if traffic.attack_type == "ddos":
        # 1. Defending Against "Smashing the Doorbell"
        return {
            "timestamp": timestamp,
            "sourceIp": source_ip,
            "protocol": "TCP/UDP",
            "prediction": "Volumetric DDoS",
            "confidence": "N/A (Rate Limited)",
            "action": "Dropped before AI (>1000 p/s)",
            "isThreat": True
        }
    elif traffic.attack_type == "adversarial":
        # 2. Defending Against "The AI Optical Illusion"
        return {
            "timestamp": timestamp,
            "sourceIp": source_ip,
            "protocol": "TCP",
            "prediction": "Adversarial Padding",
            "confidence": "98.7%",
            "action": "Blocked via Disguise Training",
            "isThreat": True
        }
    elif traffic.attack_type == "rounding_error":
        # 3. Defending Against "The Rounding Error"
        return {
            "timestamp": timestamp,
            "sourceIp": source_ip,
            "protocol": "ICMP",
            "prediction": "Low-Confidence Normal",
            "confidence": "51.2%",
            "action": "Blocked via Safety Net Threshold (<80%)",
            "isThreat": True
        }
    else:
        return {
            "timestamp": timestamp,
            "sourceIp": "192.168.1.45",
            "protocol": "TCP",
            "prediction": "Normal Traffic",
            "confidence": "99.8%",
            "action": "Allowed",
            "isThreat": False
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
