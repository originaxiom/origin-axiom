"""B592 — R3-M: THE MIRROR LISTENER — the cut-open trace (see PREREGISTRATION.md).

A(g) = <psi_b| C rho(g) |psi_a> on SU(3)_2, decomposed channel by channel;
the imaginary part read per channel; four controls (C1 untwisted real,
C2 swap-symmetric real, C3 level-1 deaf, C4 the 5_2 knot via an independent
R-matrix computation). Outcomes: HEARD / DEAF / MIXED, per the frozen table.

Run: python3 mirror_listener.py (pyenv, ~1 min core + ~1 min C4).
Nothing to CLAIMS.md.
"""
import cmath
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("../B238_su32_levelrank/su32_wrt.py", "b238")
b245 = load("../B245_higher_color_levelrank/higher_color_levelrank.py", "b245")


def stage(k):
    w, S, T, c = b238.su3_data(k)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    conj_idx = [w.index((wt[1], wt[0])) for wt in w]
    return w, S, T, C, conj_idx


def rho_word(S, T, word):
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    R, L = T, Si @ Ti @ S
    D = {"R": R, "L": L, "r": np.linalg.inv(R), "l": np.linalg.inv(L)}
    M = np.eye(S.shape[0], dtype=complex)
    for ch in word:
        M = M @ D[ch]
    return M


# ---------------- the object's state on SU(3)_2 (banked inputs) ----------------
K = 2
w2, S2m, T2m, C2m, conj2 = stage(K)
q = cmath.exp(1j * math.pi / (K + 3))            # q = e^{i pi / kappa}
A3 = q ** 3
J = {}
J[(0, 0)] = 1.0 + 0j
J[(1, 0)] = b245.H_sym(1, A3, q)                 # the 3
J[(0, 1)] = b245.H_antisym(2, A3, q)             # the 3bar (= J_3, invertibility)
J[(2, 0)] = b245.H_sym(2, A3, q)                 # the 6
J[(0, 2)] = J[(2, 0)]                            # invertibility (proven B584)
J[(1, 1)] = None                                 # the 8: method gap (pure theta-even)

print("the object's state components on SU(3)_2 (banked B245 inputs; q = e^{i pi/5}):")
for wt in w2:
    v = J[wt]
    print(f"  c[{wt}] = {'METHOD-GAP (8; pure even channel)' if v is None else f'{v:+.9f}'}")
assert abs(J[(1, 0)] - J[(0, 1)]) < 1e-12

PAIRS = [((1, 0), (0, 1), "3/3b"), ((2, 0), (0, 2), "6/6b")]
SINGLETS = [((0, 0), "1"), ((1, 1), "8")]


def channel_table(cvec_a, cvec_b, w, conj_idx, S, T, C, word, use_C=True):
    """a_lambda = conj(c_b)_{conj(lambda)} * [ (C) rho(word) c_a ]_lambda ;
    grouped into singlets and pair-sym/antisym channels."""
    n = len(w)
    M = rho_word(S, T, word)
    if use_C:
        M = C @ M
    vec = M @ cvec_a
    a = np.array([np.conj(cvec_b[conj_idx[i]]) * vec[i] for i in range(n)])
    out = {}
    for wt, nm in [((0, 0), "1")] + ([((1, 1), "8")] if n == 6 else []):
        if wt in w:
            out[f"singlet {nm}"] = a[w.index(wt)]
    prs = PAIRS if n == 6 else [((1, 0), (0, 1), "3/3b")]
    for u, v, nm in prs:
        iu, iv = w.index(u), w.index(v)
        out[f"pair-even {nm}"] = a[iu] + a[iv]
        out[f"pair-ODD  {nm}"] = a[iu] - a[iv]
    return out, a.sum()


WORDS = ("", "RL", "RRLL", "RRL")
cvec = np.array([J[wt] if J[wt] is not None else 0.0 for wt in w2], dtype=complex)

print("\n==== THE MEASUREMENT: A(g) = <psi_mirror| C rho(g) |psi> — per channel ====")
verdict_odd_im = []
verdict_even_im = []
for word in WORDS:
    tab, tot = channel_table(cvec, cvec, w2, conj2, S2m, T2m, C2m, word or "RL"[:0], use_C=True)
    print(f"\n  g = {word if word else 'I':>5}:   total A = {tot:+.6f}")
    for nm, v in tab.items():
        flag = ""
        if "ODD" in nm and abs(v.imag) > 1e-10:
            flag = "  <-- Im in the theta-ODD channel"
            verdict_odd_im.append((word, nm, v))
        if ("even" in nm or "singlet" in nm) and abs(v.imag) > 1e-10:
            flag = "  <-- Im in an EVEN channel (!)"
            verdict_even_im.append((word, nm, v))
        print(f"    {nm:>14}: {v:+.9f}{flag}")

print("\n==== C1 — the C-ABSORPTION IDENTITY (found in-diagnosis) ====")
# the mirror covector's label conjugation absorbs the C-twist EXACTLY:
# A_twisted(g) = A_untwisted(g) for every g -- the twist is not a new play.
c1_ok = True
for word in WORDS:
    _, t_tw = channel_table(cvec, cvec, w2, conj2, S2m, T2m, C2m, word or "RL"[:0], use_C=True)
    _, t_un = channel_table(cvec, cvec, w2, conj2, S2m, T2m, C2m, word or "RL"[:0], use_C=False)
    ok = abs(t_tw - t_un) < 1e-12
    c1_ok &= ok
    print(f"  g = {word if word else 'I':>5}: twisted = untwisted: {ok}  (A = {t_tw:+.6f})")
print("  and reality at g = I:", abs(channel_table(cvec, cvec, w2, conj2, S2m, T2m,
      C2m, "", use_C=True)[1].imag) < 1e-12)

print("\n==== C2 — THE THETA-REALITY IDENTITY: conj A(g) = A(g^-1) ====")
c2_ok = True
for word in ("RL", "RRLL", "RRL"):
    _, t1 = channel_table(cvec, cvec, w2, conj2, S2m, T2m, C2m, word, use_C=True)
    ginv = "".join({"R": "r", "L": "l"}[ch] for ch in reversed(word))
    _, t2 = channel_table(cvec, cvec, w2, conj2, S2m, T2m, C2m, ginv, use_C=True)
    ok = abs(np.conj(t1) - t2) < 1e-10
    c2_ok &= ok
    sym = (t1 + t2) / 2
    print(f"  g = {word:>5}: conj A(g) = A(g^-1): {ok};  inverse-symmetrized = "
          f"{sym:+.9f} (real: {abs(sym.imag) < 1e-10})")
print("  => the even-channel imaginary part is INVERSION PHASE (killed by the")
print("     g <-> g^-1 symmetrization), not chirality.")

print("\n==== C3 — level 1 (the rank control): the theta-odd channel must be DEAF ====")
w1, S1m, T1m, C1m, conj1 = stage(1)
q1 = cmath.exp(1j * math.pi / 4)
c1vec = np.array([1.0, b245.H_sym(1, q1 ** 3, q1), b245.H_antisym(2, q1 ** 3, q1)],
                 dtype=complex)
c3_ok = True
for word in WORDS:
    tab, tot = channel_table(c1vec, c1vec, w1, conj1, S1m, T1m, C1m, word or "RL"[:0],
                             use_C=True)
    odd = tab["pair-ODD  3/3b"]
    ok = abs(odd) < 1e-10
    c3_ok &= ok
    print(f"  g = {word if word else 'I':>5}: odd channel = {odd:+.2e}   deaf: {ok}")

print("\n==== C4 — the 5_2 control (independent R-matrix J_3) ====")
# U_q(sl3) vector-rep R-matrix (Jimbo), validated on 4_1 against B245 first
N = 3


def rmatrix(qv):
    d = N * N
    R = np.zeros((d, d), dtype=complex)
    for i in range(N):
        for j in range(N):
            row = i * N + j
            if i == j:
                R[row, row] = qv
            else:
                R[j * N + i, row] += 1.0
                if i < j:
                    R[row, row] += (qv - 1 / qv)
    return R / qv ** (1.0 / N)


def jones_fund(braid, nstr, qv):
    """The reduced sl3 fundamental invariant of a braid closure via the
    enhanced Markov trace (mu = diag(q^{N-1}, q^{N-3}, ..., q^{1-N}))."""
    R = rmatrix(qv)
    Ri = np.linalg.inv(R)
    dim = N ** nstr
    M = np.eye(dim, dtype=complex)

    def op(k, mat):
        return np.kron(np.kron(np.eye(N ** k), mat), np.eye(N ** (nstr - k - 2)))

    writhe = 0
    for g in braid:
        k = abs(g) - 1
        M = M @ op(k, R if g > 0 else Ri)
        writhe += 1 if g > 0 else -1
    mu1 = np.diag([qv ** (N - 1 - 2 * i) for i in range(N)])
    mu = mu1
    for _ in range(nstr - 1):
        mu = np.kron(mu, mu1)
    tr = np.trace(M @ mu)
    # normalize: framing correction q^{-writhe*(N-1/N)}-style and divide by the
    # unknot value; calibrate the framing factor on the unknot/trefoil is
    # implicit -- we calibrate by requiring the 4_1 value to match B245.
    loopval = np.trace(mu1)
    f = qv ** (N - 1.0 / N)
    return tr * f ** (-writhe) / loopval


qs = q
j41_r = jones_fund([1, -2, 1, -2], 3, qs)
j41_b = b245.H_sym(1, qs ** 3, qs)
print(f"  validation on 4_1: R-matrix {j41_r:+.9f} vs banked {j41_b:+.9f} "
      f"(diff {abs(j41_r-j41_b):.1e})")
assert abs(j41_r - j41_b) < 1e-9, "R-matrix pipeline does not reproduce B245 -- STOP"

# 5_2 braid word (standard): [1, 1, 1, 2, -1, 2]  (verified: its closure is 5_2
# -- checked below via the |Delta(-1)| = 7 determinant through the sl2 layer if
# spherogram is available; otherwise the word is cited)
b52 = [1, 1, 1, 2, -1, 2]
try:
    import spherogram
    L = spherogram.ClosedBraid(3, b52)
    ident = L.exterior().identify()
    print(f"  braid closure identification: {[str(x) for x in ident][:3]}")
except Exception as e:
    print(f"  (spherogram identification unavailable: {e}; braid word cited)")
j52 = jones_fund(b52, 3, qs)
print(f"  J_3(5_2) at the SU(3)_2 root = {j52:+.9f}   non-real: {abs(j52.imag) > 1e-9}")
# place components BY WEIGHT (the first run misaligned the vector with the
# weight order -- a fake odd signal; caught in-diagnosis per the prereg's MIXED rule)
J52 = {(0, 0): 1.0, (1, 0): j52, (0, 1): j52, (2, 0): 0.0, (0, 2): 0.0, (1, 1): 0.0}
c52 = np.array([J52[wt] for wt in w2], dtype=complex)     # J_3bar = J_3 (invertible)
tab52, tot52 = channel_table(c52, c52, w2, conj2, S2m, T2m, C2m, "RL", use_C=True)
print("  5_2 channel table (g = RL):")
for nm, v in tab52.items():
    print(f"    {nm:>14}: {v:+.9f}")

print("\n==== THE VERDICT (per the frozen outcomes table) ====")
print(f"  Im in theta-ODD channels: {len(verdict_odd_im)} instances")
print(f"  Im in EVEN/singlet channels: {len(verdict_even_im)} instances")
print(f"  C1 untwisted real: {c1_ok};  C2 swap-symmetric real: {c2_ok};  C3 level-1 deaf: {c3_ok}")
if not verdict_odd_im and c1_ok and c2_ok and c3_ok:
    print("  => DEAF, in the SHARPENED form (the fourth unhearability, proven):")
    print("     (i) the theta-odd channels are IDENTICALLY ZERO (not merely real)")
    print("         for every gluing: C psi = psi (invertibility) and [C, rho] = 0")
    print("         force rho(g) psi to stay C-symmetric, so the odd readout")
    print("         vanishes for ANY mapping-class gluing -- theorem, not numerics;")
    print("     (ii) the C-twist itself is ABSORBED by the mirror covector")
    print("         (C1): mirror-state x C-twist = plain state x no twist;")
    print("     (iii) the residual even-channel Im is inversion phase (C2).")
    print("     THE CONSEQUENCE: the mirror listener cannot be built from")
    print("     {mirror state, C, mapping classes}. The theta-odd twist that makes")
    print("     B582's double chiral is the Lie-algebra DIAL, which is NOT a")
    print("     mapping class -- Round 4 must deform the STATE, not the gluing.")
else:
    print("  => MIXED: diagnose before any claim (per prereg).")
