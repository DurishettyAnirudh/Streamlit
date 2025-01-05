import streamlit as st
import time as ts
from datetime import time

def timetosec(time):
    m,s,mm = time.split(":")
    print(m)
    print(s)
    print(mm)
    seconds = int(m)*60 + int(s) + int(mm)/1000
    return seconds


st.title("Progress bar")
timer_value = st.time_input("Timer", value=time(0,0,0))

if str(timer_value) == "00:00:00":
    st.write("Please set the timer")
else:
    bar = st.progress(0)
    sec = timetosec(str(timer_value))
    per = sec/100
    progress_status = st.empty()
    for i in range(100):
        bar.progress((i + 1))
        progress_status.write(str(i+1)+ " %")
        ts.sleep(per)
