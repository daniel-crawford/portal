import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
from PIL import Image


from utils.plot import generate_dummy_data, plot_usage, plot_cost

from dotenv import load_dotenv
import os


load_dotenv()  # Automatically loads from .env in the current directory

USERNAME = st.secrets["USERNAME"]
PASSWORD = st.secrets["PASSWORD"]



# ============================================
# Constants and Config
# ============================================
st.set_page_config(
    page_title="Utility Monitoring Dashboard",
    page_icon="📈",
    layout="wide"
)

COLOR_SCHEMES = {
    "Gas": "#FFA07A",       # Light Salmon
    "Electric": "#FFD700",  # Gold
    "Water": "#87CEFA"       # Light Sky Blue
}

ICONS = {
    "Gas": "⛽",       # Fuel Pump
    "Electric": "⚡",  # Lightning Bolt
    "Water": "💧"   # Droplet
}

# ============================================
# Authentication (Simple Password)
# ============================================
def authenticate():
    with st.sidebar:
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == USERNAME and password == PASSWORD :
                st.session_state.authenticated = True
            else:
                st.error("Invalid credentials")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    authenticate()
    st.stop()



# ============================================
# Main App Layout
# ============================================

# Logo / Main Page
st.title("Utility Monitoring Dashboard")
st.markdown("---")
col1, col2 = st.columns([1, 8])
with col1:
    st.image("logo.png", width=160)  # Replace with your logo if needed
with col2:
    st.markdown("### Welcome, Kenny! Hope you like the dashboard demo :) - Daniel")

# Tabs
tab_labels = tab_labels = [f"{ICONS[utility]} {utility}" for utility in ["Gas", "Electric", "Water"]]

tabs = st.tabs(tab_labels)

with tabs[0]:
    st.write('Gas' + ' gas'*0)
with tabs[1]:
    st.write('Electric' + ' electric'*0)
with tabs[2]:
    st.write('Water' + ' water'*0)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:2rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)


for tab, utility in zip(tabs, ["Gas", "Electric", "Water"]):
    with tab:
        st.markdown(f"<h2 style='color:{COLOR_SCHEMES[utility]}'>{ICONS[utility]} {utility} Dashboard</h2>", unsafe_allow_html=True)
        df = generate_dummy_data()

        st.plotly_chart(plot_usage(df, utility), use_container_width=True)
        st.plotly_chart(plot_cost(df, utility), use_container_width=True)

        st.info(f"This is a demo for the {utility} utility. Data shown is synthetic.")
