import numpy as np
from scipy.signal import butter, filtfilt

C = 1500


def bandpass_filter(x, Fs, f_center, bw=2000):
    b, a = butter(
        4,
        [f_center - bw / 2, f_center + bw / 2],
        btype="band",
        fs=Fs,
    )
    return filtfilt(b, a, x)

def estimate_tdoa_phase(x1, x2, Fs, f, n_bins=5):
    N = len(x1)

    X1 = np.fft.fft(x1)
    X2 = np.fft.fft(x2)

    freqs = np.fft.fftfreq(N, 1 / Fs)
    pos = np.where(freqs > 0)[0]
    k0 = pos[np.argmin(np.abs(freqs[pos] - f))]

    half = n_bins // 2
    k_start = max(k0 - half, 0)
    k_end   = min(k0 + half + 1, N)

    phasors = X1[k_start:k_end] * np.conj(X2[k_start:k_end])

    mean_phasor = np.mean(phasors)
    delta_phi = np.angle(mean_phasor)

    f_bin = freqs[k0]         
    delta_t = delta_phi / (2 * np.pi * f_bin)

    return delta_t



def tdoa_to_doa(delta_t, d):
    val = (delta_t * C) / d
    val = np.clip(val, -1.0, 1.0)
    return np.rad2deg(np.arcsin(val))
