

import streamlit as st

from sections.aim import render_aim
from sections.theory import render_theory
from sections.procedure import render_procedure
from sections.simulation import render_simulation


st.markdown(
    """
    <style>
    .main-title {
        font-size: 40px;
        font-weight: 600;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .section-text {
        font-size: 18px;
        line-height: 1.7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        border-radius: 6px;
        padding: 10px 0px;
        margin-bottom: 8px;
        font-size: 16px;
        font-weight: 500;
    }

    div.stButton > button:hover {
        background-color: #145a86;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Underwater DOA Virtual Lab",
    layout="wide",
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Virtual Lab")
section = st.sidebar.radio(
    "Navigate",
    [
        "Aim",
        "Theory",
        "Procedure",
        "Simulation"
    ],
)

# ---------------- MAIN CONTENT ----------------
if section == "Aim":
    render_aim()

elif section == "Theory":
    render_theory()

elif section == "Procedure":
    render_procedure()

elif section == "Simulation":
    render_simulation()

