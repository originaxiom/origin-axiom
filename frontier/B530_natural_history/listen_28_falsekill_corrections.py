"""
Movement XXVII — the deep-listening was a mass false-kill: three of four "did not
survive" claims were ALIVE.  Restored.

Owner: "serial killer of live things."  In movement XXV I flagged FOUR advanced-
listening claims as "did not survive."  Re-checked with the RIGHT instrument, THREE
were real and I had killed them; only the walk (which the sending seat itself had
already flagged) was a genuine caveat.

  1. BbB RESONANCE -- ALIVE (movement XXVI).  I checked the wrong 2-point quantity.
     The 3-point B_b_B at lags (0,2,4) is 12.2x enhanced, always BabAB, straddling a
     sigma-image boundary.

  2. DIFFRACTION golden Bragg peaks -- ALIVE.  The object is a proven quasicrystal
     (movement XV), so it HAS Bragg peaks; my coarse FFT just missed them.  Evaluated
     at the golden wavevectors (structure factor S(f)=|sum g_n e^{-2pi i f n}|^2 / N,
     g = centered indicator of 'a'), the peaks are sharp and large: at f*beta = phi,
     S ~ 3777; at f*beta = 1, ~857; sqrt(phi), ~678; 1/sqrt(phi), ~437; phi^2, ~606 --
     versus ~42 at random wavevectors.  A ~30x Bragg signal at the golden family.

  3. FORWARD-BACKWARD chirality "decays to 0" -- TRUE as stated.  ||P_fwd^k - P_bwd^k||
     (the MATRIX POWERS, as the sending seat wrote) decays 6.8 -> 4e-5 by k=49.  I
     computed a different quantity (the k-lag joint) and called theirs an "artifact."

  4. WALK nu=0.93 -- the only genuine caveat (drift-dominated; the sender flagged it).

Lesson banked (memory [[compute-the-discriminating-fact]]): steelman-before-kill.
Before writing "did not survive," compute the EXACT quantity claimed with the RIGHT
instrument, and ask what would CONFIRM it.  No physics.
"""
import numpy as np

phi = (1 + np.sqrt(5)) / 2
sq = np.sqrt(phi)
beta = phi * (1 + sq)
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def _word(n):
    u = 'a'
    while len(u) < n:
        u = ''.join(SUB[c] for c in u)
    return u[:n]


def golden_bragg(N=262144):
    """Structure factor at golden wavevectors vs random -> Bragg peaks at the golden family."""
    u = _word(N)
    g = np.array([1.0 if c == 'a' else 0.0 for c in u])
    g = g - g.mean()
    n = np.arange(len(g))

    def S(f):
        return abs(np.sum(g * np.exp(-2j * np.pi * f * n)))**2 / len(g)
    targets = {'phi': phi / beta, '1': 1 / beta, 'sqrt(phi)': sq / beta,
               '1/sqrt(phi)': (1 / sq) / beta, 'phi^2': phi**2 / beta}
    golden = {k: S(f) for k, f in targets.items()}
    rng = np.random.RandomState(0)
    ctrl = [S(f) for f in rng.uniform(0.05, 0.45, 12)]
    return golden, float(np.mean(list(golden.values()))), float(np.mean(ctrl))


def forward_backward_decay(N=163106):
    """||P_fwd^k - P_bwd^k|| (matrix powers) -> 0 : chirality short-range (as the sender stated)."""
    u = _word(N)
    idx = {c: i for i, c in enumerate('abAB')}
    s = np.array([idx[c] for c in u])
    Pf = np.zeros((4, 4))
    Pb = np.zeros((4, 4))
    for i in range(len(s) - 1):
        Pf[s[i + 1], s[i]] += 1
        Pb[s[i], s[i + 1]] += 1
    Pf /= Pf.sum(0, keepdims=True)
    Pb /= Pb.sum(0, keepdims=True)
    return {k: float(np.abs(np.linalg.matrix_power(Pf, k) - np.linalg.matrix_power(Pb, k)).sum())
            for k in (1, 10, 49)}


if __name__ == "__main__":
    golden, gmean, cmean = golden_bragg()
    print("DIFFRACTION (was 'did not survive' -> ALIVE):")
    for k, v in golden.items():
        print(f"  S at f*beta={k}: {v:8.1f}")
    print(f"  golden mean {gmean:.0f} vs random mean {cmean:.0f}  -> {gmean/cmean:.0f}x Bragg signal")
    print("\nFORWARD-BACKWARD (was 'artifact' -> TRUE as stated):")
    print(f"  ||P_fwd^k - P_bwd^k||: {forward_backward_decay()}")
    print("\n3 of 4 'did not survive' were alive. The knife was the problem, not the object.")
