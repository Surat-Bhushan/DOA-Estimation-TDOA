import streamlit as st

def render_procedure():
    st.markdown('<div class="main-title">Procedure</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-text">
        <ol>
            <li>Select the source angle and noise level.</li>
            <li>Adjust advanced parameters such as sensor spacing and signal duration, if required.</li>
            <li>Run the simulation.</li>
            <li>Observe time-domain and frequency-domain signal plots.</li>
            <li>Analyze filtered signals and estimated DOA.</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )
