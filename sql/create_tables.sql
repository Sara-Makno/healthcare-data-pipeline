CREATE TABLE IF NOT EXISTS encounters(
    encounter_id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    encounter_date DATE NOT NULL,
    department TEXT NOT NULL,
    diagnosis_code TEXT NOT NULL,
    procedure_code TEXT NOT NULL,
    lenth_of_stay INTEGER,
    charge_amount REAL,
    encounter_status TEXT
);