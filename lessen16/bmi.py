import streamlit as st
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"


st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("BMI Calculator ")

with st.form("bmi_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=120, value=25)
    weight = st.number_input("Enter your weight (kg)", min_value=0.0, step=0.1)
    height = st.number_input("Enter your height (m)", min_value=0.0, step=0.01)
    submit = st.form_submit_button("Calculate BMI")


if submit:
    try:
        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)

        bmi = person.calculate_bmi()
        category = person.get_bmi_category()

        st.success(f"✅ Results for {person.name}:")
        st.write(f"**Age:** {person.age} years")
        st.write(f"**Weight:** {person.weight} kg")
        st.write(f"**Height:** {person.height} m")
        st.write(f"**BMI:** {bmi:.2f}")
        st.write(f"**Category:** {category}")

    except ValueError as e:
        st.error(f"❌ {e}")
