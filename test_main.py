from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_driver_status_with_paid_sub():
    # Test if a paid driver can go online
    response = client.post("/driver/set-status", json={"driver_id": 1, "wants_to_be_online": True})
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_ride_request_no_drivers():
    # Test behavior when no drivers are online
    response = client.post("/passenger/request-ride", json={
        "passenger_id": 101, 
        "pickup_location": "A", 
        "drop_location": "B", 
        "vehicle_preference": "EV"
    })
    # This should fail with 404 because no drivers are 'online' yet in our mock DB
    assert response.status_code == 404
