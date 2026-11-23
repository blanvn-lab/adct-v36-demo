from pathlib import Path
import streamlit as st
st.set_page_config(layout="wide")
st.iframe(Path(__file__).with_name("ADCT_V3_6.html"), height=1450)
