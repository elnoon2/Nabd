# Data dictionary
| Dataset | Column | Type | Description |
|---|---|---|---|
| wait_logs | hospital_id, day, hour, specialty, severity, patients_present, wait_minutes, is_peak, blood_stock_level | mixed | ~15,000 simulated rows |
| donors | donor_id, blood_type, age, weight_kg, area_node, days_since_donation, available, response_prob | mixed | ~2,000 simulated donors |
| blood_requests | request_id, hospital_id, blood_type, hour, units, urgency | mixed | ~1,500 simulated requests |
| hospitals | hospital_id, name, lat, lon, node_id | mixed | From OpenStreetMap (ODbL) |
