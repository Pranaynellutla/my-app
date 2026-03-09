# ZEVO: Zero Emission Vehicle Operator 🌿
**ZEVO** is a sustainable ride-hailing platform designed to empower drivers and promote green mobility. By focusing on EVs, LPG, and CNG vehicles, we aim to reduce the carbon footprint of urban transportation.

## 🚀 The ZEVO Difference
Unlike traditional ride-sharing apps like Uber or Rapido that take high commissions, ZEVO operates on a **Flat-Fee Subscription Model**:
* **Driver Independence:** Drivers pay a flat **₹50/day fee** and keep 100% of their earnings.
* **Green Fleet:** Our platform exclusively matches passengers with Zero Emission or Low Emission vehicles.
* **Range-Aware Routing:** Advanced backend logic ensures EV drivers are only assigned trips within their current battery range.

## 🛠 Tech Stack
This repository contains the core ZEVO Backend, featuring:
* **FastAPI (Python):** High-performance API for ride-matching and status management.
* **PostgreSQL + PostGIS:** Geospatial database for tracking vehicles in real-time.
* **WebSockets:** Live GPS telemetry for a seamless passenger experience.

## 🚦 Getting Started
To run the ZEVO backend locally:
1. Ensure you have Python installed.
2. Run the one-click startup file: `run_zevo.bat`.
3. Visit `http://127.0.0.1:8000/docs` to interact with the API.
