-- 3NF schema
CREATE TABLE specialties (specialty_id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL);
CREATE TABLE blood_types (blood_type_id INTEGER PRIMARY KEY, label TEXT UNIQUE NOT NULL);
CREATE TABLE road_nodes (node_id INTEGER PRIMARY KEY, lat REAL NOT NULL, lon REAL NOT NULL);
CREATE TABLE road_edges (
  edge_id INTEGER PRIMARY KEY,
  from_node INTEGER NOT NULL REFERENCES road_nodes(node_id),
  to_node INTEGER NOT NULL REFERENCES road_nodes(node_id),
  length_m REAL NOT NULL, speed_kmh REAL NOT NULL);
CREATE TABLE hospitals (
  hospital_id INTEGER PRIMARY KEY, name TEXT NOT NULL,
  lat REAL NOT NULL, lon REAL NOT NULL,
  node_id INTEGER REFERENCES road_nodes(node_id));
CREATE TABLE hospital_specialties (
  hospital_id INTEGER REFERENCES hospitals(hospital_id),
  specialty_id INTEGER REFERENCES specialties(specialty_id),
  PRIMARY KEY (hospital_id, specialty_id));
CREATE TABLE wait_logs (
  log_id INTEGER PRIMARY KEY,
  hospital_id INTEGER NOT NULL REFERENCES hospitals(hospital_id),
  specialty_id INTEGER NOT NULL REFERENCES specialties(specialty_id),
  day INTEGER, hour INTEGER, severity INTEGER, patients_present INTEGER,
  wait_minutes REAL, is_peak INTEGER, blood_stock_level INTEGER);
CREATE TABLE donors (
  donor_id INTEGER PRIMARY KEY,
  blood_type_id INTEGER NOT NULL REFERENCES blood_types(blood_type_id),
  age INTEGER, weight_kg REAL, area_node INTEGER REFERENCES road_nodes(node_id),
  days_since_donation INTEGER, available INTEGER, response_prob REAL);
CREATE TABLE blood_requests (
  request_id INTEGER PRIMARY KEY,
  hospital_id INTEGER NOT NULL REFERENCES hospitals(hospital_id),
  blood_type_id INTEGER NOT NULL REFERENCES blood_types(blood_type_id),
  hour INTEGER, units INTEGER, urgency INTEGER);
CREATE TABLE recommendation_requests (
  rec_id INTEGER PRIMARY KEY,
  user_lat REAL, user_lon REAL,
  specialty_id INTEGER REFERENCES specialties(specialty_id),
  hour INTEGER,
  recommended_hospital_id INTEGER REFERENCES hospitals(hospital_id),
  baseline_hospital_id INTEGER REFERENCES hospitals(hospital_id),
  expected_minutes REAL, baseline_minutes REAL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP);
