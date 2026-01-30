
import streamlit as st

def render_aim():
    st.markdown('<div class="main-title">Aim</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-text">
        The aim of this experiment is to estimate the Direction of Arrival (DOA)
        of an underwater acoustic signal using a two-hydrophone array and a
        Time Difference of Arrival (TDOA) based method.
        </div>
        """,
        unsafe_allow_html=True,
    )
