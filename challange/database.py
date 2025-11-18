from models import Patient, PatientCreate

# Database e përkohshme në kujtesë
patients_db = {}
current_id = 1


def create_patient(patient: PatientCreate) -> int:
    global current_id
    patients_db[current_id] = Patient(id=current_id, **patient.dict())
    current_id += 1
    return current_id - 1


def read_patient(patient_id: int):
    return patients_db.get(patient_id)


def read_all_patients():
    return list(patients_db.values())


def update_patient(patient_id: int, patient: PatientCreate) -> bool:
    if patient_id not in patients_db:
        return False
    patients_db[patient_id] = Patient(id=patient_id, **patient.dict())
    return True


def delete_patient(patient_id: int) -> bool:
    if patient_id not in patients_db:
        return False
    del patients_db[patient_id]
    return True
