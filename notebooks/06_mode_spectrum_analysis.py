"""
File: notebooks/06_mode_spectrum_analysis.py
Purpose: Analyse the 1D mode spectrum data produced by
  src/run_mode_spectrum_with_constraint.py. Compares the dominant oscillation
  frequency omega(k) with and without the non-cancelling constraint.
Axiom link: Tests whether imposing a small non-cancelling bound on the global
  mean field significantly distorts the dispersion relation of a lattice
  scalar mode.
Inputs:
  - data/processed/mode_spectrum_1d.npz
Outputs:
  - data/processed/mode_spectrum_timeseries.png
  - data/processed/mode_spectrum_power.png
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    data_path = "data/processed/mode_spectrum_1d.npz"
    print(f"Loading mode spectrum data from {data_path}")
    d = np.load(data_path, allow_pickle=True)

    t = d["t"]
    mode_free = d["mode_free"]
    mode_constrained = d["mode_constrained"]
    params = d["params"].item() if isinstance(d["params"], np.ndarray) else d["params"]

    N = params["N"]
    dt = params["dt"]
    steps = params["steps"]
    m0 = params["m0"]
    k_index = params["k_index"]
    epsilon = params["epsilon"]

    print("Run parameters:")
    for k, v in params.items():
        print(f"  {k}: {v}")

    # Time-series plot (first part of the evolution for visibility)
    out_ts = "data/processed/mode_spectrum_timeseries.png"
    max_points = min(1000, steps)
    fig, ax = plt.subplots()
    ax.plot(t[:max_points], mode_free[:max_points], label="free")
    ax.plot(t[:max_points], mode_constrained[:max_points], label="constrained")
    ax.set_xlabel("t")
    ax.set_ylabel("mode amplitude")
    ax.set_title(f"Mode time series (k_index = {k_index})")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_ts)
    plt.close(fig)
    print(f"Saved time-series plot: {out_ts}")

    # Frequency analysis via FFT
    # Use rfft (real FFT) and convert to angular frequencies omega = 2*pi*f
    nt = t.size
    freqs = np.fft.rfftfreq(nt, d=dt)
    omega = 2.0 * np.pi * freqs

    fft_free = np.fft.rfft(mode_free)
    fft_con = np.fft.rfft(mode_constrained)

    power_free = np.abs(fft_free) ** 2
    power_con = np.abs(fft_con) ** 2

    # Ignore the zero-frequency component when searching for the peak
    # to avoid picking up any offset.
    start_idx = 1
    idx_free = start_idx + np.argmax(power_free[start_idx:])
    idx_con = start_idx + np.argmax(power_con[start_idx:])

    omega_free = omega[idx_free]
    omega_con = omega[idx_con]

    # Theoretical lattice dispersion (for small amplitude, linear Klein-Gordon)
    k_phys = 2.0 * np.pi * k_index / float(N)  # lattice spacing a = 1
    omega_theory = np.sqrt(m0 ** 2 + 4.0 * (np.sin(k_phys / 2.0) ** 2))

    print("\nExtracted dominant frequencies:")
    print(f"  omega_free       ~ {omega_free:.6f}")
    print(f"  omega_constrained~ {omega_con:.6f}")
    print(f"  omega_theory     ~ {omega_theory:.6f}")

    # Power spectrum plot
    out_power = "data/processed/mode_spectrum_power.png"
    fig, ax = plt.subplots()
    ax.plot(omega, power_free, label="free")
    ax.plot(omega, power_con, label="constrained")
    ax.set_xlabel("omega")
    ax.set_ylabel("power")
    ax.set_title(f"Mode power spectrum (k_index = {k_index})")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_power)
    plt.close(fig)
    print(f"Saved power spectrum plot: {out_power}")


if __name__ == "__main__":
    main()
