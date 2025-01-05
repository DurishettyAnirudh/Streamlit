import streamlit as st

st.title("Uploading files")
st.markdown("---")
image  = st.file_uploader("Upload an image", type=["png", "jpeg"])
if image is not None:
    st.image(image) 


images = st.file_uploader("Upload images", type=["png", "jpeg"], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)

slider1_value = st.slider("This is a slider")
print(slider1_value)

slider2_value = st.slider("This is a slider with different min max values and a predefined slider value", min_value= 235, max_value= 1400, value= 900)
print(slider2_value)

text_value = st.text_input("Enter your title ")
print(text_value)

max_text_value = st.text_input("text box with limit", max_chars= 100)
print(max_text_value)

text_area_value = st.text_area("Enter the description here")
print(text_area_value)


date_value = st.date_input("Enter your date")
print(date_value, type(date_value))

timer_value = st.time_input("Set the timer")
print(timer_value)