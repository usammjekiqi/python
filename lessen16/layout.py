import streamlit as st

col1, col2, col3, col4,col5 = st.columns(5,gap="medium",vertical_alignment="center")

with col1:
    st.header("colon1")
    st.write(" this is column 1")

with col2:
    st.header("colon2")
    st.write(" this is column 2")

with col3:
    st.header("colon3")
    st.write(" this is column 3")

with col4:  
    st.header("colon4")
    st.write(" this is column 4")

with col5:
    st.header("colon5")
    st.write(" this is column 5")

with st.container():
    st.header("This is the container")
    st.subheader("You can put multiple elements here")
    st.write("This is inside the container")


tab1, tab2, tab3 = st.tabs([" news", " sports", " economy"])

with tab1:
    st.header("This is the news tab")
    st.write("This is the news tab content")

with tab2:  
    st.header("This is the sports tab")
    st.write("This is the sports tab content")

with tab3:
    st.header("This is the economy tab")
    st.write("This is the economy tab content")

