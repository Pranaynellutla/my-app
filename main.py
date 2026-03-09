from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="ZEVO Backend")

# --- DATA MODELS ---
class StatusUpdate(BaseModel):
    driver_id: int
    wants_to_be_online: bool

# --- MOCK DATA (Simulating your SQL Database) ---
drivers_db = {1: {"name": "Arjun", "is_online": False, "vehicle": "EV"}}
subscriptions_db = {1: {"expiry": datetime(2026, 12, 31, 23, 59, 59)}}

# --- LOGIC: SUBSCRIPTION CHECK ---
@app.post("/driver/set-status")
async def set_driver_status(update: StatusUpdate):
    driver_id = update.driver_id
    sub = subscriptions_db.get(driver_id)
    
    # Check if the $50 daily subscription is valid
    if not sub or sub['expiry'] < datetime.now():
        return {"status": "error", "message": "Daily fee not paid. Cannot go online."}
    
    drivers_db[driver_id]["is_online"] = update.wants_to_be_online
    status_text = "Online" if update.wants_to_be_online else "Offline"
    return {"status": "success", "message": f"ZEVO Driver is now {status_text}"}

# --- LOGIC: REAL-TIME TRACKING (WebSockets) ---
@app.websocket("/ws/track/{driver_id}")
async def tracking_endpoint(websocket: WebSocket, driver_id: int):
    await websocket.accept()
    try:
        while True:
            # Receive GPS data from the driver's phone
            data = await websocket.receive_json() 
            print(f"ZEVO Driver {driver_id} position: {data}")
    except WebSocketDisconnect:
        print(f"Driver {driver_id} disconnected.")




# --- PASSENGER LOGIC: RIDE REQUESTING ---

class RideRequest(BaseModel):
    passenger_id: int
    pickup_location: str
    drop_location: str
    vehicle_preference: str # 'EV', 'CNG', or 'Any'

@app.post("/passenger/request-ride")
async def request_ride(request: RideRequest):
    # This filters our drivers to find those who are Online 
    # and match the 'Green' vehicle preference of ZEVO
    available_drivers = [
        d_id for d_id, info in drivers_db.items() 
        if info["is_online"] == True and 
        (request.vehicle_preference == "Any" or info["vehicle"] == request.vehicle_preference)
    ]
    
    if not available_drivers:
        raise HTTPException(status_code=404, detail="No ZEVO drivers nearby. Try again soon.")
    
    # Pick the first available driver (Simplified for your MVP)
    selected_id = available_drivers[0]
    driver_name = drivers_db[selected_id]["name"]
    
    return {
        "status": "success",
        "message": f"Driver {driver_name} has accepted your request!",
        "arrival_estimate": "5 minutes",
        "vehicle_type": drivers_db[selected_id]["vehicle"]
    }
