# Underwater Direction of Arrival (DOA) Virtual Lab
## Streamlit Deployed Link: 
https://doa-estimation-tdoa-hghl92f8hbskpmaqeyaxto.streamlit.app/

## Overview
This project is an interactive virtual laboratory for estimating the **Direction of Arrival (DOA)** of an underwater acoustic source using a **two-sensor linear array**.

The lab demonstrates how extremely small **time delays** between sensors can be estimated using **phase-based Time Difference of Arrival (TDOA)**, even in the presence of noise.

The project is implemented using:
- Python for signal processing
- Streamlit for interactive visualization
- NumPy, SciPy, and Matplotlib for numerical analysis and plotting

The focus of the lab is **conceptual clarity**, not black-box algorithms.

---

## Theory Background
For a far-field acoustic source and two sensors separated by distance `d`:

Δt = (d · sin(θ)) / c

where:
- θ = Direction of Arrival (DOA)
- c = speed of sound in water (≈ 1500 m/s)

For narrowband signals, very small time delays are estimated using **phase difference**:

Δφ = 2πfΔt

This project estimates phase difference around the signal frequency and converts it back to time delay and DOA.

---

## Project Structure

<img width="521" height="251" alt="Screenshot 2026-04-03 at 2 22 56 PM" src="https://github.com/user-attachments/assets/4c178466-8a6a-405e-a6d1-48414b1096b7" />

---

## Features
- Interactive control of source angle and noise level
- Time-domain and frequency-domain visualization
- Band-pass filtering to suppress broadband noise
- Phase-based TDOA estimation
- Robust DOA estimation under noise
- Educational observations at each step

---

## How to Run (Streamlit App)

### 1. Install dependencies
pip install -r requirements.txt


### 2. Run the app
streamlit run app.py


---

## How to Run (Standalone Experiment)
python main.py


This version allows step-by-step plotting and direct comparison between true and estimated DOA.

---

## Key Assumptions and Limitations
- Two-sensor linear array
- Narrowband signal model
- Far-field plane wave assumption
- No multipath or reverberation
- Simulation-only (no hardware imperfections)

---

## Educational Value
This project is intended for learning and teaching:
- Why time-domain delay is difficult to observe
- How phase information enables accurate delay estimation
- The effect of noise and sensor spacing on DOA accuracy

It is suitable for signal processing labs and introductory array processing studies.

---

## Author
Surat Bhushan  
2026
