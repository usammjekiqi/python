import streamlit as st
from dotenv import load_dotenv ,set_key
import requests

# Base URL of the FastAPI backend
BASE_URL = "http://127.0.0.1:8000"

st.title("Hospital Management System")

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Add/Edit Patient", "View Patients"])

if menu == "Add/Edit Patient":
    st.header("Add or Edit Patient")

    # Form to add or edit a patient
    with st.form("patient_form"):
        patient_id = st.text_input("Patient ID (leave blank to add new)")
        name = st.text_input("Name")
        surname = st.text_input("Surname")
        contact = st.text_input("Contact")
        date_of_admission = st.date_input("Date of Admission")
        submit = st.form_submit_button("Submit")

    if submit:
        patient_data = {
            "name": name,
            "surname": surname,
            "contact": contact,
            "date_of_admission": str(date_of_admission),
        }

        if patient_id:
            # Update existing patient
            response = requests.put(f"{BASE_URL}/patients/{patient_id}", json=patient_data)
            if response.status_code == 200:
                st.success("Patient updated successfully!")
            else:
                st.error("Failed to update patient. Check the ID.")
        else:
            # Add new patient
            response = requests.post(f"{BASE_URL}/patients/", json=patient_data)
            if response.status_code == 200:
                st.success("Patient added successfully!")
            else:
                st.error("Failed to add patient.")

    # Form to delete a patient
    st.subheader("Delete Patient")
    delete_id = st.text_input("Patient ID to delete")
    delete_button = st.button("Delete Patient")

    if delete_button:
        response = requests.delete(f"{BASE_URL}/patients/{delete_id}")
        if response.status_code == 200:
            st.success("Patient deleted successfully!")
        else:
            st.error("Failed to delete patient. Check the ID.")

elif menu == "View Patients":
    st.header("View Patients")

    # Fetch and display all patients
    response = requests.get(f"{BASE_URL}/patients/")
    if response.status_code == 200:
        patients = response.json()
        if patients:
            for patient in patients: 
                st.write(f"ID: {patient['id']}")
                st.write(f"Name: {patient['name']} {patient['surname']}")
                st.write(f"Contact: {patient['contact']}")
                st.write(f"Date of Admission: {patient['date_of_admission']}")
                st.write("---")
        else:
            st.info("No patients found.")
    else:
        st.error("Failed to fetch patients.")