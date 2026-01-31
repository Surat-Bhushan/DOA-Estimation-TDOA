import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from signal_model import generate_time_axis, generate_signals
from doa_algorithm import bandpass_filter, estimate_tdoa_phase, tdoa_to_doa


def obs_box(text):
    st.markdown(
        f"""
        <div style="
            background-color:#e8f2fb;
            padding:10px;
            border-left:4px solid #1f77b4;
            margin-bottom:20px;
            font-size:15px;">
        <b>Observation:</b> {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_simulation():
    st.markdown('<div class="main-title">Simulation</div>', unsafe_allow_html=True)

    # ---------------- STEP 1 ----------------
    st.subheader("Parameter Selection")

    st.markdown(
        """
        <div class="section-text">
        Noise represents additive environmental and sensor disturbances.
        Higher noise directly corrupts phase estimation and therefore affects
        time-delay and DOA estimation. Larger source angles are more sensitive
        to noise.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.table({
        "Angle Range (deg)": ["0–15", "15–40", "40–90"],
        "Recommended Noise σ": ["≤ 0.05", "≤ 0.02", "≤ 0.01"]
    })

    theta = st.slider("Source Angle (deg)", -90, 90, 20)
    noise_sigma = st.slider(
    "Noise Level (σ)",
    min_value=0.0,
    max_value=0.5,
    value=0.01,
    step=0.005,
)


    # ---------------- STEP 2 ----------------
    with st.expander("Advanced Settings"):
        d = st.number_input("Sensor spacing d (m)", value=0.02)
        T = st.number_input("Signal duration T (s)", value=0.2)

        st.latex(r"\Delta t = \frac{d \sin(\theta)}{c}")

        st.markdown(
                """
                <div class="section-text">
                <ul>
                    <li><b>d</b> must be smaller than half the wavelength to avoid angle ambiguity.</li>
                    <li>Large <b>d</b> causes different angles to produce the same phase difference.</li>
                    <li><b>T</b> should be long enough for accurate phase estimation.</li>
                    <li>Very large <b>T</b> increases noise effects and reduces real-time response.</li>
                </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )


    # ---------------- STEP 3 ----------------
    st.subheader("Run Simulation")
    if st.button("Run Simulation"):
        Fs = 100_000
        f = 30_000

        t = generate_time_axis(Fs, T)
        x1, x2, _ = generate_signals(t, f, theta, d, noise_sigma)

        x1f = bandpass_filter(x1, Fs, f)
        x2f = bandpass_filter(x2, Fs, f)

        delta_t = estimate_tdoa_phase(x1f, x2f, Fs, f)
        theta_est = tdoa_to_doa(delta_t, d)

        # -------- TIME DOMAIN --------
        fig1, ax1 = plt.subplots(figsize=(7, 3))
        ax1.plot(t[:1500], x1[:1500], label="Sensor 1")
        ax1.plot(t[:1500], x2[:1500], label="Sensor 2")
        ax1.set_title("Time-Domain Signals")
        ax1.legend()
        st.pyplot(fig1)
        obs_box("Time delay is extremely small and not visually apparent.")

        # -------- FREQ DOMAIN (RAW) --------
        freqs = np.fft.fftfreq(len(x1), 1/Fs)
        X1 = np.fft.fft(x1)
        X2 = np.fft.fft(x2)

        fig2, ax2 = plt.subplots(figsize=(7, 3))
        ax2.plot(freqs[:len(freqs)//2], 20*np.log10(np.abs(X1[:len(X1)//2])+1e-12), label="Sensor 1")
        ax2.plot(freqs[:len(freqs)//2], 20*np.log10(np.abs(X2[:len(X2)//2])+1e-12), label="Sensor 2")
        ax2.set_title("Frequency-Domain (Before Filtering)")
        ax2.legend()
        st.pyplot(fig2)
        obs_box("Signal appears as a narrowband peak; noise is broadband.")
        # -------- TIME DOMAIN (FILTERED) --------
        fig_td_filt, ax_td_filt = plt.subplots(figsize=(7, 3))
        ax_td_filt.plot(t[:1500], x1f[:1500], label="Sensor 1 (filtered)")
        ax_td_filt.plot(t[:1500], x2f[:1500], label="Sensor 2 (filtered)")
        ax_td_filt.set_title("Filtered Time-Domain Signals")
        ax_td_filt.legend()
        st.pyplot(fig_td_filt)

        obs_box(
            "After band-pass filtering, noise is reduced but the time delay is still "
            "too small to observe directly in the time domain."
        )
        # -------- FREQ DOMAIN (FILTERED) --------
        X1f = np.fft.fft(x1f)
        X2f = np.fft.fft(x2f)

        fig3, ax3 = plt.subplots(figsize=(7, 3))
        ax3.plot(freqs[:len(freqs)//2], 20*np.log10(np.abs(X1f[:len(X1f)//2])+1e-12), label="Sensor 1 (filtered)")
        ax3.plot(freqs[:len(freqs)//2], 20*np.log10(np.abs(X2f[:len(X2f)//2])+1e-12), label="Sensor 2 (filtered)")
        ax3.set_title("Frequency-Domain (After Filtering)")
        ax3.legend()
        st.pyplot(fig3)
        obs_box("Filtering suppresses broadband noise outside the signal band.")

        st.subheader("Estimated Direction of Arrival")

        st.markdown(
            f"""
            <div style="
                background-color:#f7f7f7;
                padding:15px;
                border-left:5px solid #1f77b4;
                font-size:18px;">
            <b>Given Source Angle:</b> {theta:.2f}° <br>
            <b>Estimated DOA:</b> {theta_est:.2f}°
            </div>
            """,
            unsafe_allow_html=True,
        )
