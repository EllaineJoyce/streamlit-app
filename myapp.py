import streamlit as st
from PIL import Image


st.title("My Autobiography and Portfolio")


st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Autobiography", "Portfolio"])

# Home Section
if options == "Home":
    st.header("Welcome to My Personal Portfolio")
    st.write("Explore my journey, skills, and projects!")

# Autobiography Section
if options == "Autobiography":
    st.header("Autobiography")
    st.write("""
    My name is Ellaine, a BSIT Student in Cebu Institute of Technology.
    Over the years, I've worked on several projects that highlight my skills and expertise in design and software developing.
    """)

    # Add an image
    image = Image.open('me.jpg')
    st.image(image, caption='This is me!', width=200)  # Adjust the width as needed


# Portfolio Section
if options == "Portfolio":
    st.header("Portfolio")
    st.write("In my LinkedIn Account, you can see some of my project portfolio.")
    st.write("""
    [Link to Profile](https://www.linkedin.com/in/ellaine-joyce-c-58a195207/)
    """)

   

st.sidebar.text("Thank you for visiting!")
