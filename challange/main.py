from fastapi import FastAPI, HTTPException
from typing import List
import models
import database
from models import PatientCreate, Patient

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Hospital Management System"}


@app.post("/patients/", response_model=Patient, status_code=201)
def create_patient(patient: PatientCreate):
    """Create a new patient"""
    patient_id = database.create_patient(patient)
    return Patient(id=patient_id, **patient.dict())


@app.get("/patients/{patient_id}", response_model=Patient)
def read_patient(patient_id: int):
    """Read a single patient"""
    patient = database.read_patient(patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@app.get("/patients/", response_model=List[Patient])
def read_all_patients():
    """Read all patients"""
    return database.read_all_patients()


@app.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, patient: PatientCreate):
    """Update a patient's info"""
    updated = database.update_patient(patient_id, patient)
    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")
    return Patient(id=patient_id, **patient.dict())


@app.delete("/patients/{patient_id}", response_model=dict)
def delete_patient(patient_id: int):
    """Delete a patient"""
    deleted = database.delete_patient(patient_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted successfully"}
