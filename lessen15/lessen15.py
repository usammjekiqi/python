import streamlit as st


 #   st.title("hello world")

#def Main():

#if st.button("click me"):
    #st.write("button clicked")

#if st.checkbox("check me to showe some mor text"):
    #st.write("check clicked")


#if __name__ == "__main__":
    #button()


user_input=st.text_input("enter your name","sample text")

st.write("yue entered:",user_input)

age=st.number_input("enter your age",min_value=0,max_value=100)
st.write("your age is:",age)

def calculate_bmi(weight,height):
    bmi=weight/(height*height)
    return bmi