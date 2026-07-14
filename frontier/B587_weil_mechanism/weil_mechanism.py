"""B587 — the tone mechanism: the Weyl-twisted Weil factorization (L82 / L24(c)).

(D) Z(W; SU(3)_k) = (1/6) sum_w sign(w) tr(rho_Weil(W) . P_w) on C[P/kQ],
verified exactly against banked B238 values for balanced words; the C-twist
expands over the coset -W. (M) each term's conductor = det(A x (+-w) - I_4).
Framework KNOWN (Jeffrey 1992; banked B204 PROOF): this computes the open
SU(3) reach (L24(c)) and the B585 tone menu (L82).

Run: python3 weil_mechanism.py (pyenv, ~10 min). Nothing to CLAIMS.md.
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

PHI = (1 + 5 ** 0.5) / 2

# the Weyl group of A2 on weight coordinates (a,b), plus -1 (= S^2 on the stage)
S1 = np.array([[-1, 0], [1, 1]])          # s1: (a,b) -> (-a, a+b)
S2 = np.array([[1, 1], [0, -1]])          # s2: (a,b) -> (a+b, -b)
WEYL = []                                 # (matrix, sign)
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = np.eye(2, dtype=int)
    for g in word:
        M = (S1 if g == 0 else S2) @ M
    WEYL.append((M, (-1) ** len(word)))

# SL(2,Z) monodromies (R=[[1,1],[0,1]], L=[[1,0],[1,1]])
R2 = np.array([[1, 1], [0, 1]])
L2 = np.array([[1, 0], [1, 1]])
def mono(word):
    M = np.eye(2, dtype=int)
    for ch in word:
        M = M @ (R2 if ch == 'R' else L2)
    return M


def ip_weight(u, v):
    """A2 weight-space inner product: (u,v) = (2/3)(a1 a2 + b1 b2) + (1/3)(a1 b2 + a2 b1)."""
    return (2.0 * (u[..., 0] * v[..., 0] + u[..., 1] * v[..., 1])
            + (u[..., 0] * v[..., 1] + u[..., 1] * v[..., 0])) / 3.0


def build_G(kap):
    """G = P/kQ as weight-coordinate representatives + index map via SNF coords.
    kQ has basis k*(2,-1), k*(-1,2); U = [[1,0],[1,1]]-style SNF: G ~ Z_k x Z_3k
    via u = (a mod k? ...) -- implemented directly: canonical coords
    c1 = a mod k is wrong in general; use U from SNF of K=[[2,-1],[-1,2]]:
    U K V = diag(1,3) with U = [[0,1],[1,2]]? -- computed below numerically."""
    # SNF of K: find U unimodular s.t. rows reduce. K = [[2,-1],[-1,2]].
    # U = [[0,-1],[1,2]]: U@K = [[1,-2],[0,3]]; then V clears the -2: canonical
    # coords c = U @ mu with c1 mod k, c2 mod 3k AFTER the V-mix; simpler:
    # c = U @ mu; class invariant: (c1 mod k, (c2 + 2*c1? ) ...). Robust route:
    # brute-force canonical rep by reduction search over the two generators.
    U = np.array([[0, -1], [1, 2]])
    KQ1 = kap * np.array([2, -1])
    KQ2 = kap * np.array([-1, 2])

    def canon(mu):
        c = U @ mu
        # after U, the lattice U*kQ has basis k*(1,-2)->? U@KQ1 = (k*1, k*0)?
        # U@KQ1 = [0*2k -1*(-k), 1*2k + 2*(-k)] = (k, 0); U@KQ2 = (-2k, 3k)...
        # basis: (k,0) and (-2k,3k): reduce c1 mod k, then c2 mod 3k (using
        # (-2k,3k) after clearing c1 leaves c2 mod 3k up to the -2k shift tied
        # to c1 reductions; since (k,0) is there, shifts of c1 are free, and
        # c2 changes only via the second generator: c2 mod 3k, c1 mod k with a
        # correction: adding (-2k,3k): c1 -> c1-2k == c1 mod k. So classes are
        # exactly (c1 mod k, c2 mod 3k).
        return (int(c[0]) % kap, int(c[1]) % (3 * kap))

    reps, index = [], {}
    # enumerate representatives: invert canon on the grid
    Uinv = np.array([[2, 1], [-1, 0]])     # inverse of U (det U = 1)
    for c1 in range(kap):
        for c2 in range(3 * kap):
            mu = Uinv @ np.array([c1, c2])
            index[(c1, c2)] = len(reps)
            reps.append(mu)
    reps = np.array(reps)
    return reps, index, canon


def weil_ops(kap):
    reps, index, canon = build_G(kap)
    n = len(reps)
    q = ip_weight(reps, reps)                          # |mu|^2
    T = np.exp(1j * np.pi * q / kap)                   # diag phases e^{pi i |mu|^2 / kap}
    pair = ip_weight(reps[:, None, :], reps[None, :, :])
    S = np.exp(-2j * np.pi * pair / kap) / np.sqrt(n)
    # NO anomaly calibration: S = the bare finite Fourier transform (S^2 = parity
    # exactly); the framing anomaly lives in per-letter offsets (-i per R, +i per
    # L relative to the SU(3) T = T_bare * e^{-2pi i/3}) which CANCEL for balanced
    # words -- the only words used in (D).
    # gates
    assert np.allclose(S @ S.conj().T, np.eye(n), atol=1e-8)
    perms = {}
    for pm in (1, -1):
        for wi, (Wm, sg) in enumerate(WEYL):
            P = np.zeros((n, n))
            for i, mu in enumerate(reps):
                P[index[canon(pm * (Wm @ mu))], i] = 1.0
            perms[(pm, wi)] = (P, sg)
    # -1 must equal S^2 up to nothing (gate)
    Pm1 = perms[(-1, 0)][0]
    assert np.allclose(S @ S, Pm1, atol=1e-7), f"S^2 != parity at kap={kap}"
    return T, S, perms, n


def rho_weil(word, T, S):
    n = S.shape[0]
    Sinv = S.conj().T
    Rop = np.diag(T)
    Lop = Sinv @ np.diag(T).conj() @ S
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ (Rop if ch == 'R' else Lop)
    return M


def conductor_menu(A):
    """det(A x (pm w) - I4) via eigenvalue products, exact integer."""
    out = {}
    for pm in (1, -1):
        for wi, (Wm, sg) in enumerate(WEYL):
            B = pm * Wm
            K = np.kron(A, B) - np.eye(4)
            out[(pm, wi)] = int(round(np.linalg.det(K)))
    return out


WORDS = {"RL": "golden", "RRLL": "silver", "RRRLLL": "bronze"}

print("registered conductor menus det(A x (pm w) - I4):")
for wd in WORDS:
    A = mono(wd)
    menu = conductor_menu(A)
    print(f"  {wd:>7} (tr {np.trace(A)}): " +
          "  ".join(f"{'+' if pm>0 else '-'}w{wi}:{d}" for (pm, wi), d in sorted(menu.items())))

print("\nW1 — the decomposition identity (D) vs banked B238 values:")
KAPS = list(range(4, 21))
per_term = {wd: {} for wd in WORDS}
for kap in KAPS:
    k = kap - 3
    w3, S3, T3, c3 = b238.su3_data(k)
    T, S, perms, n = weil_ops(kap)
    for wd in WORDS:
        M = rho_weil(wd, T, S)
        terms = {}
        for key, (P, sg) in perms.items():
            terms[key] = np.trace(M @ P)
        per_term[wd][kap] = terms
        zW = sum(perms[(1, wi)][1] * terms[(1, wi)] for wi in range(6)) / 6.0
        zB = b238.wrt_trace(S3, T3, wd)
        ok = abs(zW - zB) < 1e-6
        if not ok:
            print(f"  kap={kap} {wd}: Weil {zW:+.6f} vs banked {zB:+.6f}  MISMATCH")
        assert ok, f"(D) FAILS at kap={kap}, {wd}"
    print(f"  kap={kap:2d}: (D) exact for RL, RRLL, RRRLLL  PASS")

print("\nW2 — per-term firing table (golden RL; values rounded):")
print("  term(+-w, conductor): values over kap=4..20")
Ag = mono("RL")
menu_g = conductor_menu(Ag)
for key in sorted(menu_g):
    vals = [per_term["RL"][kap][key] for kap in KAPS]
    line = "  ".join(f"{v.real:+.2f}{v.imag:+.2f}j" if abs(v.imag) > 1e-6 else f"{v.real:+.3f}"
                     for v in vals)
    print(f"  ({'+' if key[0]>0 else '-'}w{key[1]}, d={menu_g[key]:>3}): {line}")

print("\nW3 — the assembled STAGE channels (convention: inserting stage-C = sign(w0) x")
print("the (-W)-coset, and sign(w0) = -1 for A2; so tr_odd = (Z + Zcoset)/2):")
print("verifying LAW-O (B585) and the banked even values, kap=4..20:")
for kap in KAPS:
    t = per_term["RL"][kap]
    Z = sum(WEYL[wi][1] * t[(1, wi)] for wi in range(6)) / 6.0
    Zco = sum(WEYL[wi][1] * t[(-1, wi)] for wi in range(6)) / 6.0
    odd, even = (Z + Zco) / 2, (Z - Zco) / 2
    law_o = (1.0 if kap % 4 == 0 else 0.0) - (1 / PHI if kap % 5 == 0 else 0.0)
    assert abs(odd - law_o) < 1e-7, f"LAW-O fails at kap={kap}: {odd} vs {law_o}"
    print(f"  kap={kap:2d}: odd={odd.real:+.6f} = LAW-O  even={even.real:+.6f}")
print("  LAW-O RE-DERIVED from the twelve Gauss terms at every kap  PASS")

print("\nthe closed-form assembly at 5|kap (the golden voice):")
print("  odd = (1/12)[(1 + 5) - 6*sqrt(5) + 2*(1 + (-1))] = (1 - sqrt5)/2 = -1/phi")
print("  (identity 1, the d=25 term 5, six reflection Gauss sums sqrt5, rotations cancel)")

print("\nsilver per-term table (the 7-tone = the d=49 rotation terms):")
menu_s = conductor_menu(mono("RRLL"))
for key in sorted(menu_s):
    vals = [per_term["RRLL"][kap][key] for kap in KAPS]
    line = "  ".join(f"{v.real:+.2f}" if abs(v.imag) < 1e-6 else f"{v:+.2f}" for v in vals)
    print(f"  ({'+' if key[0]>0 else '-'}w{key[1]}, d={menu_s[key]:>3}): {line}")

print("\nbronze kap=10 SILENCE exhibited (stage convention):")
t = per_term["RRRLLL"][10]
tot = 0
for wi in range(6):
    tot += WEYL[wi][1] * (t[(1, wi)] + t[(-1, wi)])
print("  (1/12) sum sign(w) (t_+w + t_-w) = (1/12)[(3+1) - 3*(3+1) + 2*(-6+10)]"
      f" = {tot.real/12:+.8f}")
assert abs(tot / 12) < 1e-7
print("  => the observed silence is an EXACT arithmetic cancellation: 4 - 12 + 8 = 0")

print("\nALL GATES PASS")
