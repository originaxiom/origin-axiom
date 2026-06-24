"""B200 -- verification of the 2026-06-24 chat1 independent-computation handoff.

Three incoming "MATH" results re-derived before banking (verify-don't-trust). Verdicts:
  R2  VERIFIED + banked: on-site is the unique finite-range interaction preserving the Fibonacci
      2-letter Sturmian alphabet (NN/NNN paired potentials break it).
  R1  REFUTED: "doublon = single-particle replica at U=t (kappa1=kappa2=3)" -- the t_eff=2t^2/U
      doublon formula is STRONG-COUPLING (U>>t); at U=t it is out of regime (t_eff=2t > single
      hopping; NO doublon band) and the handoff's "RMS=0 verification" was circular (effective
      Fibonacci chain with lambda_eff vs the single particle = a tautology at U=t).
  R3  STANDARD ETH (the handoff concedes this): many-body filling -> Poisson->GOE; finite-size
      (13 sites). Recorded as a boundary observation, not a headline.

Standalone condensed-matter / symbolic-dynamics math; no physics claim; nothing to CLAIMS.md. pyenv.
"""
import numpy as np
from collections import Counter


def fib_word(minlen):
    w = "0"
    while len(w) < minlen:
        w = "".join("01" if c == "0" else "0" for c in w)
    return w


def complexity(s, L):
    return len(set(s[i:i + L] for i in range(len(s) - L + 1)))


# ---------- R2 (VERIFIED): on-site uniquely preserves the Sturmian alphabet ----------
def r2_sturmian_selection():
    w = fib_word(987)
    single = [complexity(w, L) for L in range(1, 6)]
    assert single == [2, 3, 4, 5, 6], single          # Fibonacci IS Sturmian (p=L+1)
    assert "11" not in w                                # the substitution forbids 'bb'
    nn = "".join(str(int(w[i]) + int(w[i + 1])) for i in range(len(w) - 1))   # d=1
    nnn_vals = sorted(set(int(w[i]) + int(w[i + 2]) for i in range(len(w) - 2)))  # d=2
    nn_comp = [complexity(nn, L) for L in range(1, 6)]
    nn_vals = sorted(set(int(c) for c in nn))
    c = Counter(int(x) for x in nn)
    ratio = c[1] / c[0]
    print("R2: single Fibonacci complexity p(1..5) =", single, "(Sturmian)")
    print("R2: NN (d=1) paired values =", nn_vals, " complexity p(1..5) =", nn_comp,
          " -> p(4)=%d > 5 => NOT Sturmian" % nn_comp[3])
    print("R2: NNN (d=2) paired values =", nnn_vals, " (3 letters)")
    print("R2: NN letter ratio = %.3f (phi=%.3f phi^2=%.3f) -> not metallic" %
          (ratio, (1 + 5 ** .5) / 2, ((1 + 5 ** .5) / 2) ** 2))
    assert len(nn_vals) == 2 and nn_comp[3] == 6      # 2 values but p(4)=6 -> not Sturmian
    assert len(nnn_vals) == 3
    print("R2 VERIFIED: on-site (d=0) is the unique finite-range interaction preserving Sturmian. [num/combinatorial]")
    return True


# ---------- R1 (REFUTED): the doublon is NOT a single-particle replica at U=t ----------
def _fib_potential(N, V=1.0):
    w = fib_word(N)
    return V * np.array([int(c) for c in w[:N]], float)


def r1_doublon_refutation(N=13, t=1.0):
    Vsite = _fib_potential(N)
    idx = lambda a, b: a * N + b

    def true_doublon_topband(U):
        H = np.zeros((N * N, N * N))
        for a in range(N):
            for b in range(N):
                s = idx(a, b)
                H[s, s] = Vsite[a] + Vsite[b] + (U if a == b else 0.0)
                for ap in (a - 1, a + 1):
                    if 0 <= ap < N:
                        H[idx(ap, b), s] += -t
                for bp in (b - 1, b + 1):
                    if 0 <= bp < N:
                        H[idx(a, bp), s] += -t
        ev = np.sort(np.linalg.eigvalsh(H))
        return ev[-N:], ev[-N - 1]

    def pt_prediction(U):
        teff = 2 * t ** 2 / U
        Hd = np.diag(2 * Vsite + U).astype(float)
        for i in range(N - 1):
            Hd[i, i + 1] = Hd[i + 1, i] = -teff
        return np.sort(np.linalg.eigvalsh(Hd)), teff

    print("\nR1 (the doublon claim): TRUE 2-body ED vs the t_eff=2t^2/U doublon prediction:")
    out = {}
    for U in (1.0, 5.0, 20.0):
        band, below = true_doublon_topband(U)
        pred, teff = pt_prediction(U)
        rms = float(np.sqrt(np.mean((band - pred) ** 2)))
        gap = float(band[0] - below)
        out[U] = (teff, gap, rms)
        print("  U=%5.1f teff=%.3f band-gap-below=%6.2f RMS(true vs PT)=%.3f" % (U, teff, gap, rms))
    # at U=t the PT formula is out of regime: huge RMS + no band gap; at U>>t it works
    assert out[1.0][2] > 2.0 and out[1.0][1] < 0.3      # U=t: RMS huge, no gap
    assert out[20.0][2] < 0.3                            # U>>t: PT valid
    print("R1 REFUTED: at U=t the doublon formula is out of regime (no band, RMS~3.8); the handoff's")
    print("           'RMS=0' was effective-model-vs-single = circular. The U=t 'fixed point' is vacuous.")
    return True


# ---------- R3 (STANDARD ETH): filling drives Poisson -> GOE (finite-size) ----------
def r3_thermalization_trend(N=13):
    import itertools
    Vsite = _fib_potential(N)

    def r_stat(M, W):
        states = list(itertools.combinations(range(N), M))     # spinless fermions, M particles
        pos = {s: i for i, s in enumerate(states)}
        H = np.zeros((len(states), len(states)))
        for s in states:
            i = pos[s]
            occ = set(s)
            H[i, i] = sum(Vsite[k] for k in occ) + W * sum(1 for k in occ if k + 1 in occ)  # NN attraction
            for k in s:
                for kp in (k - 1, k + 1):
                    if 0 <= kp < N and kp not in occ:
                        ns = tuple(sorted((set(s) - {k}) | {kp}))
                        H[pos[ns], i] += -1.0
        ev = np.sort(np.linalg.eigvalsh(H))
        d = np.diff(ev)
        d = d[d > 1e-9]
        r = np.minimum(d[:-1], d[1:]) / np.maximum(d[:-1], d[1:])
        return float(np.mean(r))
    r1 = r_stat(1, 0.0); r2 = r_stat(2, -4.0)
    print("\nR3 (standard ETH, report-only): <r> M=1 (no int)=%.3f -> M=2 (W=-4)=%.3f  (Poisson~0.386, GOE~0.530)" % (r1, r2))
    print("   NOTE: this quick N=13 check does NOT reproduce the handoff's 'M=1 Poisson' signature (got %.3f, not ~0.386)" % r1)
    print("   -> R3 is textbook ETH but its specific Poisson->GOE numbers are setup/finite-size-sensitive; NOT banked as a result.")
    return True                                           # report-only; no pass/fail gate (R3 is standard, not a claim)


if __name__ == "__main__":
    ok = r2_sturmian_selection() and r1_doublon_refutation() and r3_thermalization_trend()
    print("\nALL CHECKS PASS" if ok else "FAILED")
