import streamlit as st

def render_theory():
    st.markdown('<div class="main-title">Theory</div>', unsafe_allow_html=True)

    def section_start():
        st.markdown("<div style='margin-bottom:40px;'>", unsafe_allow_html=True)

    def section_end():
        st.markdown("</div>", unsafe_allow_html=True)

     def styled_image(url, caption):
        st.markdown(
            """
            <div style="
                border:.3px solid #cccccc;
                padding:2px;
                background-color:#fafafa;
                margin:20px 0;
                text-align:center;">
            """,
            unsafe_allow_html=True,
        )
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.image(url, use_container_width=True, caption=caption)

        st.markdown(
            """
            <div style="
                border:.3px solid #cccccc;
                padding:2px;
                background-color:#fafafa;
                margin:20px 0;
                text-align:center;">
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)



    # ---------------- DOA ----------------
    section_start()
    st.markdown(
        """
        <div class="section-text">
        <h3>Direction of Arrival (DOA) in Underwater Acoustics</h3>
        Direction of Arrival refers to the angle from which an acoustic wave reaches
        a sensor array. In this experiment, the medium is assumed to be water
        with approximately constant sound speed (≈1500 m/s). The source is assumed
        to be in the far-field, producing a plane wave that reaches spatially
        separated hydrophones at slightly different times.
        </div>
        """,
        unsafe_allow_html=True,
    )
    styled_image(
        "https://www.mdpi.com/sensors/sensors-24-05835/article_deploy/html/images/sensors-24-05835-g020-550.jpg",
        "Geometry of DOA estimation using a linear sensor array",
    )
    section_end()

    # ---------------- TDOA ----------------
    section_start()
    st.markdown(
        """
        <div class="section-text">
        <h3>Time Difference of Arrival (TDOA)</h3>
        Due to spatial separation between sensors, the acoustic wave reaches one
        hydrophone earlier than the other. This time difference depends on the
        source angle and the sensor spacing.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.latex(r"\Delta t = \frac{d \sin(\theta)}{c}")
    styled_image(
        "https://cdn.shopify.com/s/files/1/0594/9472/7851/files/time_difference_of_arrival_800x.png?v=1663832766",
        "Illustration of time difference of arrival between two sensors",
    )
    section_end()

    # ---------------- PHASE TDOA ----------------
    section_start()
    st.markdown(
        """
        <div class="section-text">
        <h3>Phase-Based TDOA Estimation</h3>
        For narrowband signals, estimating very small time delays directly in the
        time domain is difficult. Instead, the delay is estimated through phase
        differences in the frequency domain. Time delay is later recovered from this
        phase difference. In practice, phase estimates from multiple neighboring
        frequency bins are averaged to reduce noise-induced errors.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.latex(r"\Delta \phi = 2 \pi f \Delta t")
    
    styled_image(
        "https://europe1.discourse-cdn.com/arduino/original/4X/9/6/7/9673ae7df816bf89cdb00050119ed37c00c51924.jpeg",
        "Time-domain and frequency-domain representations of a signal",
    )
    section_end()

    

    # ---------------- NOISE + FILTER ----------------
    section_start()
    st.markdown(
        """
        <div class="section-text">
        <h3>Noise and Its Effect on DOA Estimation</h3>
        Noise is typically broadband and spreads across frequencies with relatively
        low amplitude. Noise disturbs phase estimation, which in turn affects time
        delay estimation and ultimately the DOA.

        <h3>Band-Pass Filtering</h3>
        Band-pass filtering isolates the signal band while suppressing broadband
        noise outside the frequency of interest.
        </div>
        """,
        unsafe_allow_html=True,
    )
    styled_image(
        "https://de.mathworks.com/help/examples/rf/win64/BandpassFilterResponseExample_05.png",
        "Frequency response of a band-pass filter",
    )
    section_end()

    # ---------------- LIMITATIONS ----------------
    section_start()
    st.markdown(
        """
        <div class="section-text">
        <h3>Error Sources and Limitations</h3>
        <ul>
            
            <li>Noise-induced errors in phase and TDOA estimation</li>
            <li>Phase ambiguity due to phase wrapping</li>
            <li>Sampling and FFT resolution limitations</li>
            <li>Limited angular resolution with a two-sensor array</li>
            <li>Assumes narrowband signal model</li>
            <li>Ideal free-field propagation assumption</li>
            <li>No multipath or reverberation effects</li>
            <li>Cannot resolve multiple or symmetric sources</li>
            <li>Large source angles are more sensitive to small delay errors.</li>
            <li>Simulation-only setup without hardware imperfections</li>

        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    section_end()
