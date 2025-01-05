import streamlit as st
import pandas as pd

st.title("St.Title")
st.header("Streamlit")
st.subheader("Streamlit sub header")
st.latex("c = \\pm\\sqrt{a^2 + b^2}")
st.code("This code box code example", language='python')




json = {'a': [1,2,3], 'b' : "This is a string"}
st.json(json)

st.markdown("[google](https://www.google.com) This is markdown example the below line is too")
st.markdown("---")
st.write("## h2 This is our swiss army knife example i.e. st.write() fun")
st.write("You can play with it. Refer official streamlit documantation")


st.metric(label='Wind Speed', value="120ms\^-1", delta="1.4ms",)


table = pd.DataFrame({'Column 1': [1,2,3, 9,4], 'Column 2':[3, 4,1,2,6]})
st.table(table)
st.dataframe(table)
st.image("photo.jpg", caption = "This is an image", width = 720)
st.audio("Audio.m4a")
st.video("Video.mp4")

def checkfun():
    print(st.session_state.first_checker)
check = st.checkbox(label='Wind Speed', value = True, on_change = checkfun, key="first_checker")
if check:
    st.write("The checkbox is checked😘")
def radiostatus():
    print(st.session_state.radiosession)
radio = st.radio("Which country do you live?", options = ("US", "UK", "India😘"), key = "radiosession", on_change = radiostatus)

def buttonclick():
    print("button clicked")
btn = st.button("Click Me", on_click =buttonclick)



def selected():
    print(selection)
selection = st.selectbox("what is your favourite car?", options = ("BMW", "Ferrari","Lamborgini"), on_change = selected)



def multiselected():
    print(multiselection)
multiselection = st.multiselect("select few items", options=("cars", "planes", "Trains", "Machines"), on_change=multiselected)
st.write(multiselection)