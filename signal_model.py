import numpy as np

C = 1500 # speed of sound (m/s)


def generate_time_axis(Fs, T):
    return np.arange(0, T, 1 / Fs)


def generate_signals(t, f, theta_deg, d, noise_sigma):
    """
    Generate two sensor signals with DOA-based delay and noise
    """
    theta = np.deg2rad(theta_deg)
    tau = (d * np.sin(theta)) / C

    x1 = np.sin(2 * np.pi * f * t)
    x2 = np.sin(2 * np.pi * f * (t - tau))

    # Add noise
    x1 += np.random.normal(0, noise_sigma, size=len(t))
    x2 += np.random.normal(0, noise_sigma, size=len(t))

    return x1, x2, tau
