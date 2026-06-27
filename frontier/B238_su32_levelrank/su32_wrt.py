"""B238 / L49 remainder -- the SU(3)_2 WRT of the figure-eight + the level-rank duality SU(2)_3 <-> SU(3)_2.
The last computable item of the chat1 handoff. Pure numpy (no SnapPy); fully reproducible. Nothing to CLAIMS.md.

Builds the SU(3)_2 modular data (S,T) from Kac-Peterson, GATE-verifies the modular relations, computes the
closed figure-eight-bundle WRT Z = tr(rho(RL)) (the B204 object, the Sol mapping torus), and compares to
SU(2)_3 across many monodromy words.

HEADLINE (verify-don't-trust, both gates pass):
  Z(4_1=RL closed bundle; SU(2)_3) = Z(4_1; SU(3)_2) = -1/phi  (= -0.618034), EXACTLY.
  -- the figure-eight WRT COINCIDES across the level-rank pair.
But this is NOT a general level-rank equality: it FAILS for silver (RRLL: 0 vs 1), bronze (RRRLLL: 1 vs 3),
and generic words -- the 4-dim (SU(2)_3) and 6-dim (SU(3)_2) modular reps have different traces in general.
THE REASON (the honest 'why'): level-rank SU(2)_3 <-> SU(3)_2 shares kappa = k+N = 5 (3+2 = 2+3), the golden
cyclotomic field Q(zeta_5); the figure-eight (the minimal/golden monodromy) lands on -1/phi for both, while
the non-golden metallic bundles do not coincide. (And c(SU(2)_3)+c(SU(3)_2)=9/5+16/5=5=c(SU(6)_1): the
level-rank conformal embedding SU(2)_3 x SU(3)_2 ⊂ SU(6)_1.) One more instance of 'golden is special'.

Run: python su32_wrt.py (pyenv).
"""
import cmath
import itertools

import numpy as np

PHI = (1 + 5 ** 0.5) / 2


def su3_data(k):
    """SU(3)_k modular (S,T) via Kac-Peterson. Casimir C2=<l,l+2rho>=(2/3)(a^2+ab+b^2)+2(a+b)."""
    N, kap = 3, k + 3
    weights = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    Lvec = lambda w: np.array([w[0] + w[1] + 2.0, w[1] + 1.0, 0.0])     # lambda+rho in eps-coords
    ip = lambda u, v: float(np.dot(u, v) - u.sum() * v.sum() / 3.0)      # su(3) trace-zero inner product
    perms = list(itertools.permutations(range(3)))
    sgn = lambda p: (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    n = len(weights)
    S = np.zeros((n, n), dtype=complex)
    for i, wl in enumerate(weights):
        Ll = Lvec(wl)
        for j, wm in enumerate(weights):
            Lm = Lvec(wm)
            S[i, j] = sum(sgn(p) * cmath.exp(-2j * np.pi * ip(Ll[list(p)], Lm) / kap) for p in perms)
    S = S / np.sqrt((np.abs(S) ** 2).sum(axis=0)[0])                      # normalize to unitary
    c = k * 8 / (k + 3)
    T = np.diag([cmath.exp(2j * np.pi * (((2.0 / 3) * (a * a + a * b + b * b) + 2 * (a + b)) / (2 * kap) - c / 24.0))
                 for (a, b) in weights])
    return weights, S, T, c


def su2_data(k):
    """SU(2)_k modular (S,T); h_j=j(j+1)/(k+2), j=a/2."""
    n, kap = k + 1, k + 2
    S = np.array([[np.sqrt(2.0 / kap) * np.sin(np.pi * (a + 1) * (b + 1) / kap) for b in range(n)]
                  for a in range(n)], dtype=complex)
    c = k * 3 / (k + 2)
    T = np.diag([cmath.exp(2j * np.pi * ((a / 2.0) * (a / 2.0 + 1) / kap - c / 24.0)) for a in range(n)])
    return S, T, c


def modular_gate(S, T):
    """the correctness gate: S unitary & symmetric, S^2 a permutation (charge conj C), (ST)^3 proportional to S^2."""
    n = S.shape[0]
    uni = np.allclose(S @ S.conj().T, np.eye(n), atol=1e-9)
    sym = np.allclose(S, S.T, atol=1e-9)
    S2 = S @ S
    perm = np.allclose(np.abs(S2) @ np.abs(S2), np.eye(n), atol=1e-9)     # S^2=C permutation => |S2| is a perm
    ST3 = np.linalg.matrix_power(S @ T, 3)
    idx = np.unravel_index(np.argmax(np.abs(S2)), S2.shape)
    prop = np.allclose(ST3, (ST3[idx] / S2[idx]) * S2, atol=1e-7)
    return uni and sym and perm and prop


def wrt_trace(S, T, word):
    """Z = tr(rho(word)) with R=T, L=S^{-1}T^{-1}S; the closed-bundle WRT (the c/24 framing cancels in any word
    with equal R,L count, e.g. R^aL^a)."""
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    Rr, Lr = T, Si @ Ti @ S
    M = np.eye(S.shape[0], dtype=complex)
    for ch in word:
        M = M @ (Rr if ch == 'R' else Lr)
    return np.trace(M)


if __name__ == "__main__":
    S2, T2, c2 = su2_data(3)
    w3, S3, T3, c3 = su3_data(2)
    print("=== correctness gates (modular relations) ===")
    g2, g3 = modular_gate(S2, T2), modular_gate(S3, T3)
    print(f"  SU(2)_3 (4 primaries) gate: {g2}   c={c2}")
    print(f"  SU(3)_2 (6 primaries {w3}) gate: {g3}   c={c3}")
    assert g2 and g3

    print("\n=== the figure-eight (RL) WRT coincides across the level-rank pair ===")
    z2, z3 = wrt_trace(S2, T2, 'RL'), wrt_trace(S3, T3, 'RL')
    print(f"  Z(4_1; SU(2)_3) = {z2:+.6f}   Z(4_1; SU(3)_2) = {z3:+.6f}   (-1/phi = {-1/PHI:+.6f})")
    assert abs(z2 - (-1 / PHI)) < 1e-9 and abs(z3 - (-1 / PHI)) < 1e-9
    print("  => BOTH = -1/phi exactly (reproduces B204 for SU(2)_3).")

    print("\n=== but NOT a general level-rank equality (verify-don't-trust) ===")
    for w in ['RL', 'RRLL', 'RRRLLL', 'RRL', 'RLL']:
        a, b = wrt_trace(S2, T2, w), wrt_trace(S3, T3, w)
        print(f"  {w:>7}: SU(2)_3={a:+.4f}  SU(3)_2={b:+.4f}  equal:{abs(a-b)<1e-9}")
    assert abs(wrt_trace(S2, T2, 'RRLL') - wrt_trace(S3, T3, 'RRLL')) > 1e-6   # silver differs

    print("\n=== the 'why' + level-rank signatures ===")
    print(f"  shared kappa = k+N: SU(2)_3 -> 3+2=5 ; SU(3)_2 -> 2+3=5  (same golden cyclotomic Q(zeta_5))")
    print(f"  c(SU(2)_3)+c(SU(3)_2) = {c2}+{c3} = {c2+c3} = c(SU(6)_1)=35/7={35/7}  (conformal embedding)")
    assert abs((c2 + c3) - 35 / 7) < 1e-12
    print("  => figure-eight (golden/minimal) WRT coincides at -1/phi via the shared kappa=5; non-golden differ.")
    print("\nALL CHECKS PASS")
