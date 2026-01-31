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
