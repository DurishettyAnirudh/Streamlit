import streamlit as st
import time

st.set_page_config(layout = "wide")

if "photo" not in st.session_state:
    boolean = True
    st.session_state["photo"] = "not done"
def change_session_state():
    st.session_state["photo"] = "done"
    st.boolean = not st.boolean


col1, col2, col3 = st.columns([1,2,1])

col1.markdown("# This is first COl")
photo = col2.file_uploader("Upload a photo", on_change=change_session_state)
camera = col2.camera_input("Take a photo", on_change=change_session_state)


#this is progress bar


if st.session_state["photo"] == "done" and st.boolean:   
    progress_bar = col2.progress(0)

    for progress in range(100):
        time.sleep(0.05)
        progress_bar.progress(progress+1)
    col2.success("photo Uploaded sucessfully!")


    # task in progress example and expandbar
    with st.expander("Read more here"):
        st.write("More details Here")

        if photo is None:
            st.image(camera)
        else:
            st.image(photo)