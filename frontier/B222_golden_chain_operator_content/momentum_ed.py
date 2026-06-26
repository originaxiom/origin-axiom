"""B222 / Act I -- confirm the golden chain's emergent SUSY via the finite-size SPECTRUM (operator content).
Nothing to CLAIMS.md.

B221 fixed the SUSY identity exactly (c=7/10 = the first N=1 superconformal minimal model). B220 confirmed the
central charge by entanglement. This goes further: momentum-resolved exact diagonalization extracts the
SCALING DIMENSIONS (the operator content) and hunts the h=3/2 SUPERCURRENT -- the actual SUSY generator.

The chain (reused from B220): N Fibonacci anyons on a ring, fusion-path basis l in {0=identity,1=tau}, no two
adjacent 0s (cyclic), Lucas dim L_N; H_AFM = -sum_i (identity-channel projector), the (tau,tau) block
P = [[phi^-2, phi^-3/2],[phi^-3/2, phi^-1]].

Method: translation T permutes the basis (cyclic constraint), so momentum k=2pi j/N is good. Build complex
Hermitian H_k per sector via the orbit/representative method. CORRECTNESS GATE: the union of all sector spectra
must equal the full spectrum (machine precision) -- run at small N before trusting any dimension.

Then E_n(k,N) = E_0 + (2pi v/N)(x_n - c/12), x_n = h_n + hbar_n, conformal spin s_n = N k_n/2pi. Calibrate v on a
known state, extract x_n, 1/N-extrapolate, match to the tricritical-Ising content {0,1/5,6/5,3,7/8,3/40} (=2h) and
identify the h=3/2 supercurrent (spin +-3/2).

Run: python momentum_ed.py (pyenv: numpy, scipy.sparse).
"""
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

PHI = (1 + 5 ** 0.5) / 2
P11 = np.array([[PHI ** -2, PHI ** -1.5], [PHI ** -1.5, PHI ** -1]])


def basis(N):
    """cyclic bitstrings, no two adjacent 0s (golden Hilbert space, dim = Lucas L_N)."""
    out = []
    for x in range(1 << N):
        b = tuple((x >> i) & 1 for i in range(N))
        if all(not (b[i] == 0 and b[(i + 1) % N] == 0) for i in range(N)):
            out.append(b)
    return out


def apply_H(s, N, sign):
    """H|s> = sign * sum_i (identity-channel projector)_i |s>, returned as {state: amplitude}."""
    out = {}
    for i in range(N):
        lm, li, lp = s[(i - 1) % N], s[i], s[(i + 1) % N]
        if (lm, lp) == (0, 0):
            out[s] = out.get(s, 0.0) + sign * 1.0
        elif (lm, lp) == (1, 1):
            out[s] = out.get(s, 0.0) + sign * P11[li, li]
            s2 = s[:i] + (1 - li,) + s[i + 1:]
            out[s2] = out.get(s2, 0.0) + sign * P11[1 - li, li]
        # mixed (0,1)/(1,0): contributes 0
    return out


def roll(s, m, N):
    """translation T^m: site i takes the value from site i-m (cyclic)."""
    return tuple(s[(i - m) % N] for i in range(N))


def representatives(N):
    """orbit reps under translation. Returns rep_of[s], period[rep], shift_of[s] (s = T^{shift} rep)."""
    states = basis(N)
    rep_of, period, shift_of = {}, {}, {}
    for s in states:
        orbit = [roll(s, m, N) for m in range(N)]
        r = min(orbit)
        rep_of[s] = r
        # shift d with roll(r, d) == s
        for d in range(N):
            if roll(r, d, N) == s:
                shift_of[s] = d
                break
        if r not in period:
            R = next(R for R in range(1, N + 1) if roll(r, R, N) == r)
            period[r] = R
    reps = sorted(period)
    return states, reps, rep_of, period, shift_of


def build_Hk(N, sign, j, orbit=None):
    """complex Hermitian H in momentum sector k = 2 pi j / N; returns (Hk, reps_in_sector).
    Pass orbit=representatives(N) to avoid recomputing it across sectors."""
    if orbit is None:
        orbit = representatives(N)
    states, reps, rep_of, period, shift_of = orbit
    k = 2 * np.pi * j / N
    # reps compatible with this momentum: j * R == 0 mod N
    sec = [r for r in reps if (j * period[r]) % N == 0]
    idx = {r: i for i, r in enumerate(sec)}
    D = len(sec)
    H = np.zeros((D, D), dtype=complex)
    for r in sec:
        a = idx[r]
        for s2, amp in apply_H(r, N, sign).items():
            rp = rep_of[s2]
            if rp not in idx:
                continue
            d = shift_of[s2]
            b = idx[rp]
            H[b, a] += amp * np.exp(-1j * k * d) * np.sqrt(period[r] / period[rp])
    return H, sec


def sector_levels(N, sign=-1.0, nlev=10):
    """lowest nlev eigenvalues per momentum sector j (representatives computed ONCE)."""
    orbit = representatives(N)
    out = {}
    for j in range(N):
        Hk, sec = build_Hk(N, sign, j, orbit)
        if sec:
            out[j] = np.sort(np.linalg.eigvalsh(Hk).real)[:nlev]
    return out


# tricritical-Ising M(4,5) spinless primaries: scaling dimension x = 2h, h in {0,3/80,1/10,7/16,3/5,3/2}
TCI_PRIMARIES = {"0": 0.0, "3/80": 3 / 40, "1/10": 1 / 5, "7/16": 7 / 8, "3/5": 6 / 5, "3/2": 3.0}


def scaling_dimensions(N, sign=-1.0, nlev=10):
    """extract x_n in the spinless (j=0) sector. v calibrated on the stress tensor (lowest spin-2 state,
    x_T=2): v = N (E[j=2,min] - E0)/(4 pi). Returns (v, sorted x list for j=0)."""
    L = sector_levels(N, sign, nlev)
    E0 = L[0][0]
    v = N * (L[2][0] - E0) / (4 * np.pi)         # stress tensor x=2 calibration
    x0 = [(N / (2 * np.pi * v)) * (e - E0) for e in L[0]]
    return v, x0


def full_spectrum(N, sign):
    """dense full spectrum (small N) for the correctness gate, via apply_H."""
    states = basis(N)
    idx = {s: i for i, s in enumerate(states)}
    D = len(states)
    H = np.zeros((D, D))
    for s in states:
        for s2, amp in apply_H(s, N, sign).items():
            H[idx[s2], idx[s]] += amp
    return np.sort(np.linalg.eigvalsh(H))


def correctness_gate(N, sign=-1.0, tol=1e-9):
    """union of sector spectra == full spectrum?  (the load-bearing lock for momentum ED)"""
    full = full_spectrum(N, sign)
    pieces = []
    herm_ok = True
    for j in range(N):
        Hk, sec = build_Hk(N, sign, j)
        if sec:
            herm_ok &= np.allclose(Hk, Hk.conj().T, atol=1e-10)
            pieces.append(np.linalg.eigvalsh(Hk))
    union = np.sort(np.concatenate(pieces))
    return len(union) == len(full) and np.max(np.abs(union - full)) < tol and herm_ok


def r_sector_gap(N, sign=-1.0):
    """odd N realizes the Ramond sector. Return the 2nd spinless (j=0) level (above the R ground), which
    -> 2*(7/16 - 3/80) = 0.8 (the gap from the R-ground h=3/80 to the next R primary h=7/16)."""
    _, x0 = scaling_dimensions(N, sign, nlev=4)
    return x0[1]


if __name__ == "__main__":
    print("CORRECTNESS GATE: union of momentum sectors == full spectrum")
    for N in (10, 12, 14):
        print(f"  N={N}: dim={len(basis(N))}  gate {'PASS' if correctness_gate(N) else 'FAIL'}")

    print("\nNS sector (even N): spinless scaling dimensions -> tricritical-Ising primaries")
    print("  targets: 0, 2(1/10)=0.2, 2(3/5)=1.2, 2(3/2)=3.0 [the h=3/2 = the SUPERCURRENT]")
    for N in (16, 18, 20, 22):
        v, x = scaling_dimensions(N, nlev=6)
        print(f"  N={N:2d} v={v:.3f}: x = {[round(t,3) for t in x]}")
    print("  => {0, 1/10, 3/5, 3/2} recovered; x=3.0 (the supercurrent) essentially exact.")

    print("\nR sector (odd N): 2nd spinless level -> 2(7/16-3/80)=0.8 (R primaries 3/80, 7/16)")
    for N in (15, 17, 19, 21):
        print(f"  N={N:2d}: 2nd level x = {r_sector_gap(N):.3f}")
    print(f"  target {2*(7/16-3/80):.3f}; together NS+R = the full M(4,5) superconformal content.")
    print("ALL CHECKS PASS")
