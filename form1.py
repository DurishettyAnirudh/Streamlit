import streamlit as st


# method 1
st.markdown("<h1>Form 1</h1>", unsafe_allow_html=True)
form = st.form("Registration form ")
form.text_input("First Name")
form.form_submit_button("Submit")


# method 2 using "with" keyword
st.markdown("<h1>Form 2</h1>", unsafe_allow_html=True)
with(st.form("form2", clear_on_submit=True)):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("year")
    st.markdown("""
                <style>
                .st-emotion-cache-15hul6a.button{
                    display: flex;
                    justify-content: flex-end;
                    }
                </style>
                    """,unsafe_allow_html=True)
    s_state = st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please fill all the columns")
        else:
            st.success("Form Submitted successfully")

    

