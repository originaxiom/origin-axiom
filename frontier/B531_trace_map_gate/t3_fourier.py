"""
T3 — Internal-space Fourier analysis of the binary potential.

The binary potential V_n = 1_{A,B}(n) is a function on the substitution sequence.
In Bellissard's formalism, the gap-opening rates at IDS = α are determined by the
Fourier coefficients of V projected onto the internal (contracting) eigenspace at
wavevectors corresponding to α.

This connects the numerical slopes (T1) to the substitution's algebraic structure.
"""
import numpy as np

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
ALPH = 'abAB'
M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)

PHI = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI)
S = PHI + 1 + PHI * SQ + SQ
FREQ = np.array([PHI / S, 1 / S, PHI * SQ / S, SQ / S])
TARGET_IDS = [FREQ[0], FREQ[0] + FREQ[1], 1 - FREQ[3]]


def _fixed_point(n):
    u = 'a'
    while len(u) < n:
        u = ''.join(SUB[c] for c in u)
    return u[:n]


def _eigenspaces():
    """Compute the eigenspace decomposition of the substitution matrix."""
    vals, V = np.linalg.eig(M)
    W = np.linalg.inv(V)
    i_perr = int(np.argmax(vals.real))
    i_real = [i for i in range(4) if abs(vals[i].imag) < 1e-9 and i != i_perr][0]
    i_cplx = [i for i in range(4) if vals[i].imag > 1e-9][0]
    return {
        'perron': (vals[i_perr].real, W[i_perr]),
        'real': (vals[i_real].real, W[i_real]),
        'complex': (vals[i_cplx], W[i_cplx]),
        'eigenvalues': vals,
    }


def binary_potential_projection(n=500000):
    """Project the binary potential V_n = 1_{A,B}(n) onto the contracting eigenspaces.

    Returns the projection coordinates (physical space n, internal space coordinates)
    and the potential values.
    """
    u = _fixed_point(n)
    idx = {c: i for i, c in enumerate(ALPH)}
    V_n = np.array([1.0 if c in 'AB' else 0.0 for c in u])

    steps = np.zeros((len(u), 4))
    for k, c in enumerate(u):
        steps[k, idx[c]] = 1
    P = np.cumsum(steps, axis=0)

    es = _eigenspaces()
    proj_perron = (es['perron'][1] @ P.T).real
    proj_real = (es['real'][1] @ P.T).real
    proj_cplx = (es['complex'][1] @ P.T)

    return {
        'V': V_n,
        'perron': proj_perron,
        'real': proj_real,
        'complex_re': proj_cplx.real,
        'complex_im': proj_cplx.imag,
        'internal': np.vstack([proj_real, proj_cplx.real, proj_cplx.imag]).T,
        'eigenspaces': es,
    }


def fourier_amplitudes(n=500000):
    """Compute the Fourier amplitudes of V_n at the gap-labeling frequencies.

    For a substitution quasicrystal, the gap at IDS = α opens at rate proportional
    to |V̂(α)|, where V̂(α) = (1/N) Σ V_n e^{-2πi α n}. This is a DIRECT Fourier
    coefficient, not from the FFT (which has discrete freq resolution 1/N).

    We compute V̂(α) exactly at the three gap frequencies α = TARGET_IDS[g].
    """
    u = _fixed_point(n)
    V = np.array([1.0 if c in 'AB' else 0.0 for c in u])
    N = len(V)

    print("=" * 70)
    print("T3 — FOURIER ANALYSIS OF BINARY POTENTIAL")
    print("=" * 70)
    print(f"  N = {N}, V mean = {V.mean():.6f}")
    print(f"  Target IDS: {[f'{t:.6f}' for t in TARGET_IDS]}")

    ns = np.arange(N)
    amplitudes = []
    for g, alpha in enumerate(TARGET_IDS):
        Vhat = np.sum(V * np.exp(-2j * np.pi * alpha * ns)) / N
        amplitudes.append(abs(Vhat))

    print(f"\n  Fourier amplitudes |V̂(α)| at gap frequencies:")
    for g, a in enumerate(amplitudes):
        print(f"    Gap {g+1}: α = {TARGET_IDS[g]:.6f}, |V̂(α)| = {a:.8f}")

    if amplitudes[1] > 0:
        ratio = amplitudes[0] / amplitudes[1]
        print(f"\n  Amplitude ratio |V̂₁|/|V̂₂| = {ratio:.6f} "
              f"(slope ratio s1/s2 = 1.2565)")

    fft_V = np.fft.fft(V - V.mean())
    power = np.abs(fft_V[:N // 2]) ** 2 / N
    freqs = np.arange(N // 2) / N

    top20_idx = np.argsort(power)[-20:][::-1]
    print(f"\n  Top 10 FFT peaks (all frequencies):")
    for i, idx in enumerate(top20_idx[:10]):
        label = ""
        for g, t in enumerate(TARGET_IDS):
            if abs(freqs[idx] - t) < 0.001:
                label = f"  ← gap {g+1}"
        print(f"    freq = {freqs[idx]:.6f}, |V̂|² = {power[idx]:.6f}{label}")

    return {
        'amplitudes': amplitudes,
        'freqs': freqs,
        'power': power,
    }


def internal_space_diffraction(n=500000):
    """Compute the diffraction pattern of V in the internal (contracting) space.

    This is the autocorrelation of V projected onto the contracting eigenspace,
    which should show Bragg peaks at the gap-labeling wavevectors.
    """
    proj = binary_potential_projection(n)
    V = proj['V']
    internal = proj['internal']
    N = len(V)

    dev_V = V - V.mean()

    print("\n" + "=" * 70)
    print("INTERNAL-SPACE DIFFRACTION")
    print("=" * 70)

    corr = np.correlate(dev_V[:10000], dev_V[:10000], mode='full')
    corr = corr / corr.max()

    lags = np.arange(-9999, 10000)
    fft_corr = np.fft.fft(corr)
    power_corr = np.abs(fft_corr[:len(corr) // 2]) ** 2
    freqs_corr = np.arange(len(corr) // 2) / len(corr)

    top_idx = np.argsort(power_corr)[-20:][::-1]
    print("  Top 20 diffraction peaks (frequency, power):")
    for i, idx in enumerate(top_idx):
        print(f"    {i+1}. freq = {freqs_corr[idx]:.6f}, power = {power_corr[idx]:.4f}")

    return freqs_corr, power_corr


def wavevector_analysis(n=500000):
    """Analyze the wavevectors at which the potential has power, and compare
    with the gap-labeling frequencies.

    The gap-label module is (1/S)·Z[phi, sqrt(phi)], rank 4. Each gap
    corresponds to a specific wavevector k in the dual module. The Fourier
    coefficient |V̂(k)|² determines the gap-opening rate.
    """
    proj = binary_potential_projection(n)
    V = proj['V']
    N = len(V)

    dev_V = V - V.mean()
    fft_V = np.fft.fft(dev_V)
    amp = np.abs(fft_V[:N // 2]) / np.sqrt(N)
    freqs = np.arange(N // 2) / N

    print("\n" + "=" * 70)
    print("WAVEVECTOR ANALYSIS")
    print("=" * 70)

    for g, t in enumerate(TARGET_IDS):
        window = 200
        idx = int(round(t * N))
        lo = max(0, idx - window)
        hi = min(N // 2, idx + window)
        if lo >= hi:
            print(f"\n  Gap {g+1} (IDS = {t:.6f}): beyond Nyquist, use direct V̂(α) above")
            continue
        local_amp = amp[lo:hi]
        local_freq = freqs[lo:hi]

        peak_local = np.argmax(local_amp)
        peak_freq = local_freq[peak_local]
        peak_amp = local_amp[peak_local]

        sorted_amp = np.sort(local_amp)[::-1]
        top5 = sorted_amp[:5]

        print(f"\n  Gap {g+1} (IDS = {t:.6f}):")
        print(f"    Peak: freq = {peak_freq:.8f}, amplitude = {peak_amp:.6f}")
        print(f"    Top 5 amplitudes in window: {[f'{a:.4f}' for a in top5]}")
        print(f"    Background (median): {np.median(local_amp):.6f}")
        print(f"    Peak / background: {peak_amp / np.median(local_amp):.1f}")


if __name__ == "__main__":
    fourier_amplitudes()
    wavevector_analysis()
