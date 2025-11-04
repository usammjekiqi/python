import sqlite3
from datetime import datetime

class Patient:
    def __init__(self, name: str, surname: str, contact: str, date_of_admission: str):
        self.name = name
        self.surname = surname
        self.contact = contact
        self.date_of_admission = date_of_admission

def create_connection():
    """Create a database connection to the SQLite database."""
    connection = sqlite3.connect('hospital.db')
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    """Create the patients table in the database."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        contact TEXT NOT NULL,
        date_of_admission TEXT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

create_table()

def add_patient(patient: Patient) -> int:
    """Add a new patient to the database."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO patients (name, surname, contact, date_of_admission)
    VALUES (?, ?, ?, ?)
    ''', (patient.name, patient.surname, patient.contact, patient.date_of_admission))
    connection.commit()
    patient_id = cursor.lastrowid
    connection.close()
    return patient_id

def get_patient(patient_id: int):
    """Retrieve a patient by their ID."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return Patient(name=row["name"], surname=row["surname"], contact=row["contact"], date_of_admission=row["date_of_admission"])

def get_all_patients():
    """Retrieve all patients from the database."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    connection.close()
    return [Patient(name=row["name"], surname=row["surname"], contact=row["contact"], date_of_admission=row["date_of_admission"]) for row in rows]

def update_patient(patient_id: int, patient: Patient) -> bool:
    """Update a patient's information."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    UPDATE patients
    SET name = ?, surname = ?, contact = ?, date_of_admission = ?
    WHERE id = ?
    ''', (patient.name, patient.surname, patient.contact, patient.date_of_admission, patient_id))
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    return updated > 0

def delete_patient(patient_id: int) -> bool:
    """Delete a patient from the database."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0

# Example usage:
if __name__ == "__main__":
    # Add a new patient
    new_patient = Patient(name="John", surname="Doe", contact="1234567890", date_of_admission=datetime.now().strftime("%Y-%m-%d"))
    patient_id = add_patient(new_patient)
    print(f"Added patient with ID: {patient_id}")

    # Retrieve all patients
    patients = get_all_patients()
    for patient in patients:
        print(f"{patient.name} {patient.surname}, Contact: {patient.contact}, Date of Admission: {patient.date_of_admission}")