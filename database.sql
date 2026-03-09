-- 1. Create a table for Drivers
CREATE TABLE drivers (
    driver_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    vehicle_type VARCHAR(20), -- e.g., 'EV', 'LPG', 'CNG'
    battery_level INT DEFAULT 100, -- Real-time status for ZEVO logic
    is_online BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Create a table for Subscriptions
CREATE TABLE driver_subscriptions (
    sub_id SERIAL PRIMARY KEY,
    driver_id INT REFERENCES drivers(driver_id),
    amount_paid DECIMAL(10, 2) DEFAULT 50.00,
    payment_date DATE DEFAULT CURRENT_DATE,
    expiry_time TIMESTAMP NOT NULL, -- Usually set to 23:59:59 of the payment day
    is_active BOOLEAN DEFAULT TRUE
);
