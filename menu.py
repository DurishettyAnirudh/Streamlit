import streamlit as st

# Create sidebar menu
menu = st.sidebar.selectbox(
    "Select an option",
    ["Home", "About", "Contact"]
)

# Display content based on menu selection
if menu == "Home":
    st.title("Welcome to the Home Page!")
    st.write("This is the home page content.")
elif menu == "About":
    st.title("About Us")
    st.write("This is the about page content.")
elif menu == "Contact":
    st.title("Contact Us")
    st.write("This is the contact page content.")
