import numpy as np
import matplotlib.pyplot as plt

from signal_model import generate_time_axis, generate_signals
from doa_algorithm import bandpass_filter, estimate_tdoa_phase, tdoa_to_doa


# ---------------- PLOTTING FUNCTIONS ---------------- #

def plot_time_domain(t, x1, x2, title):
    plt.figure(figsize=(10, 4))
    plt.plot(t[:2000], x1[:2000], label="Sensor 1")
    plt.plot(t[:2000], x2[:2000], label="Sensor 2")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_frequency_domain(x1, x2, Fs, f_center, title):
    N = len(x1)
    freqs = np.fft.fftfreq(N, 1 / Fs)

    X1 = np.fft.fft(x1)
    X2 = np.fft.fft(x2)

    mag1_db = 20 * np.log10(np.abs(X1) + 1e-12)
    mag2_db = 20 * np.log10(np.abs(X2) + 1e-12)

    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:N // 2], mag1_db[:N // 2], label="Sensor 1")
    plt.plot(freqs[:N // 2], mag2_db[:N // 2], label="Sensor 2")

    plt.xlim(f_center - 5000, f_center + 5000)  # zoom around signal
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_doa_diagram(theta_true, theta_est, d):
    plt.figure(figsize=(5, 5))

    # Sensor positions
    plt.scatter([-d / 2, d / 2], [0, 0], color="black", s=80)
    plt.text(-d / 2, -0.03, "S1", ha="center")
    plt.text(d / 2, -0.03, "S2", ha="center")

    r = 0.1 # ray length (tight, readable)

    # True DOA
    plt.plot(
        [0, r * np.cos(np.deg2rad(theta_true))],
        [0, r * np.sin(np.deg2rad(theta_true))],
        "g--",
        linewidth=2,
        label="True DOA",
    )

    # Estimated DOA
    plt.plot(
        [0, r * np.cos(np.deg2rad(theta_est))],
        [0, r * np.sin(np.deg2rad(theta_est))],
        "r",
        linewidth=2,
        label="Estimated DOA",
    )

    plt.axhline(0, color="gray", linewidth=0.5)
    plt.axvline(0, color="gray", linewidth=0.5)

    plt.xlim(-0.7, 0.7)
    plt.ylim(-0.7, 0.7)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Direction of Arrival (Top View)")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


# ---------------- MAIN EXPERIMENT ---------------- #

def main():
    # PARAMETERS (underwater case)
    Fs = 100_000
    T = 0.2
    f = 30_000
    d = 0.02

    theta_true = float(input("Enter source angle (deg): "))
    noise_sigma = float(input("Enter noise level (e.g. 0.01): "))

    # Generate signals
    t = generate_time_axis(Fs, T)
    x1, x2, _ = generate_signals(t, f, theta_true, d, noise_sigma)

    # STEP 1: Time-domain noisy signals
    if input("Show time-domain noisy signals? (y/n): ").lower() == "y":
        plot_time_domain(t, x1, x2, "Time-Domain Signals (With Noise)")

    # STEP 2: Frequency-domain (raw)
    if input("Show frequency-domain signals? (y/n): ").lower() == "y":
        plot_frequency_domain(
            x1, x2, Fs, f, "Frequency-Domain (Before Filtering)"
        )

    # Filtering
    x1f = bandpass_filter(x1, Fs, f)
    x2f = bandpass_filter(x2, Fs, f)

    # STEP 3: Filtered time-domain
    if input("Show filtered time-domain signals? (y/n): ").lower() == "y":
        plot_time_domain(t, x1f, x2f, "Filtered Time-Domain Signals")

    # STEP 4: Filtered frequency-domain
    if input("Show filtered frequency-domain signals? (y/n): ").lower() == "y":
        plot_frequency_domain(
            x1f, x2f, Fs, f, "Frequency-Domain (After Band-Pass Filtering)"
        )

    # STEP 5: DOA estimation
    delta_t = estimate_tdoa_phase(x1f, x2f, Fs, f)
    theta_est = tdoa_to_doa(delta_t, d)

    print(f"\nTrue Angle      : {theta_true:.2f}°")
    print(f"Estimated Angle : {theta_est:.2f}°")

    if input("Show DOA diagram? (y/n): ").lower() == "y":
        plot_doa_diagram(theta_true, theta_est, d)


if __name__ == "__main__":
    main()
