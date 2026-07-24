#!/usr/bin/env python3
"""
B775 Phase-2 Wave-3  Cell P2W3-N1  (OI-077)
e_n mod 5 / mod 7 exclusion via an eventual-periodicity lemma.

Object:  M_0 = F = [[1,1],[1,0]];  T(M) = [[M,M],[M^2,M]];  M_n = T^n(F).
Charge tower:  e_n = det(I - M_n).   |e_n| = 1,11,809,18845089,...   (B556/B552).

QUESTION (OI-077): prove e_n mod 5 and mod 7 are eventually periodic and give
the excluded residues, OR find a counterexample.  The sweep flagged that the
"Lucas analogy" (periodicity of a LINEAR recurrence mod p) does not apply
because the charge recursion is NON-linear.

WHAT THIS CELL ESTABLISHES (each reproduced >=2 ways):

 [A] GROUND TRUTH.  e_n mod p by two independent routes:
       (1) modular determinant of I - M_n (matrix definition), and
       (2) the golden-norm  e_n = N_{Q(sqrt5)/Q}(g_n(phi)),  g_1 = x^3-x^2+2x-1,
           g_{n+1} = Res_t(t^2-2y t + y^2-y^3, g_n(t))   (B556 FL2, re-verified).
     They agree.

 [B] EXCLUSION THEOREM mod 5 (PROVEN, no periodicity needed).
       5 RAMIFIES in Q(sqrt5):  (5) = (sqrt5)^2, residue field F_5, and the two
       archimedean conjugates coincide mod the ramified prime P.  Hence for
       alpha = g_n(phi) in Z[phi],
           e_n = N(alpha) = alpha * conj(alpha)  ==  (alpha mod P)^2   (mod 5),
       a SQUARE in F_5.  Squares mod 5 = {0,1,4}.
       => residues 2 and 3 are EXCLUDED mod 5 for every n.   (verified vs data.)

 [C] NON-exclusion mod 7 (PROVEN).
       7 is INERT in Q(sqrt5) (5 is a non-residue mod 7), so
           e_n = N_{F_49/F_7}(g_n(Phi)),  Phi in F_49 a golden root.
       The relative norm F_49^* -> F_7^* is SURJECTIVE, so NO nonzero residue is
       excluded mod 7; all of {1,..,6} occur (confirmed in data).  Only 0 (i.e.
       7 | e_n) can conceivably be excluded.

 [D] THE WALL on the remaining "0-exclusion" and on full periodicity.
       5 | e_n  <=>  e_n == 0  <=>  g_n(phi) == 0 mod P  <=>  the golden residue
       lies in the zero-set of g_n  <=>  the FORWARD doubling orbit of {phi,psi}
       reaches a root of g mod p.  The doubling map mu -> mu(1 +- sqrt mu) has
       a forward orbit whose splitting-field degree GROWS WITHOUT BOUND mod p
       (measured: 2,4,8,16,32,64,128,256,... over F_5).  There is therefore NO
       finite eigenvalue orbit and NO finite-state reduction: the periodicity /
       0-exclusion lemma does NOT follow from the (linear-only) Lucas analogy.
       Empirically 5,7 divide NO e_n in the computed range -> exclusion holds so
       far but is NOT proven; NO counterexample either.
"""
import json, time
import numpy as np
import sympy as sp
from sympy import Poly, symbols, resultant, sqrt

OUT = {}

# ----------------------------------------------------------------------
# [A1] modular determinant route
# ----------------------------------------------------------------------
def escalate(M, p):
    M2 = (M @ M) % p
    return np.vstack([np.hstack([M, M]), np.hstack([M2, M])]) % p

def det_mod(A, p):
    A = A.copy().astype(np.int64) % p
    n = A.shape[0]; det = 1
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r, col] % p), -1)
        if piv == -1:
            return 0
        if piv != col:
            A[[col, piv]] = A[[piv, col]]; det = (-det) % p
        inv = pow(int(A[col, col]), p - 2, p)
        det = (det * int(A[col, col])) % p
        if col + 1 < n:
            f = (A[col+1:, col] * inv) % p
            A[col+1:, col:] = (A[col+1:, col:] - np.outer(f, A[col, col:])) % p
    return det % p

def e_seq_matrix(p, Nmax):
    F = np.array([[1, 1], [1, 0]], dtype=np.int64) % p
    seq = []; M = F
    for n in range(Nmax + 1):
        N = M.shape[0]
        seq.append(int(det_mod((np.eye(N, dtype=np.int64) - M) % p, p)))
        if n < Nmax:
            M = escalate(M, p)
    return seq

# ----------------------------------------------------------------------
# [A2] golden-norm route (exact), + [B]/[C] residue checks
# ----------------------------------------------------------------------
def golden_norm_e(nmax):
    x, t, y = symbols('x t y')
    g = x**3 - x**2 + 2*x - 1
    def D(G):
        Gt = Poly(G.subs(x, t), t)
        ker = Poly(t**2 - 2*y*t + y**2 - y**3, t)
        return sp.expand(resultant(ker, Gt)).subs(y, x)
    gs = [None, g]; cur = g
    for n in range(2, nmax + 1):
        cur = sp.expand(D(cur)); gs.append(cur)
    phi = (1 + sqrt(5)) / 2; psi = (1 - sqrt(5)) / 2
    es = {}
    for n in range(1, nmax + 1):
        v = gs[n]
        es[n] = int(sp.nsimplify(sp.simplify(v.subs(x, phi) * v.subs(x, psi))))
    return es

# ----------------------------------------------------------------------
# [D] forward doubling-orbit field-degree growth (the obstruction)
# ----------------------------------------------------------------------
def orbit_degree_growth(p, levels):
    x, mu = symbols('x mu')
    def children(qc):  # qc = int coeffs high->low, monic; return child irreducibles
        qmu = Poly(sum(c*mu**i for i, c in enumerate(reversed(qc))), mu)
        ker = Poly(x**2 - 2*mu*x + mu**2 - mu**3, mu)
        Rp = Poly(resultant(qmu, ker), x, modulus=p)
        if Rp.is_zero:
            return []
        return [tuple(int(c) % p for c in f.monic().all_coeffs())
                for f, _ in Rp.factor_list()[1]]
    seed = Poly(x**2 - x - 1, x, modulus=p)
    frontier = [tuple(int(c) % p for c in f.monic().all_coeffs())
                for f, _ in seed.factor_list()[1]]
    known = set(frontier); maxdegs = []
    for _ in range(levels):
        nxt = []
        for q in frontier:
            for c in children([int(v) for v in q]):
                if c not in known:
                    known.add(c); nxt.append(c)
        maxdegs.append(max((len(k)-1 for k in known), default=0))
        if not nxt:
            break
        frontier = nxt
    return maxdegs

# ----------------------------------------------------------------------
# run
# ----------------------------------------------------------------------
if __name__ == "__main__":
    t0 = time.time()
    NMAT = 9
    seq5 = e_seq_matrix(5, NMAT)
    seq7 = e_seq_matrix(7, NMAT)
    OUT['e_n_mod5'] = seq5
    OUT['e_n_mod7'] = seq7

    # exact golden-norm cross-check + residues
    NEXACT = 5
    es = golden_norm_e(NEXACT)
    OUT['e_n_exact_small'] = {n: str(es[n]) for n in es}
    OUT['norm_route_mod5'] = [es[n] % 5 for n in range(1, NEXACT+1)]
    OUT['norm_route_mod7'] = [es[n] % 7 for n in range(1, NEXACT+1)]
    # cross-check routes agree (e_n are NEGATIVE integers; matrix gives e_n mod p)
    agree5 = all((es[n] % 5) == seq5[n] for n in range(1, NEXACT+1))
    agree7 = all((es[n] % 7) == seq7[n] for n in range(1, NEXACT+1))
    OUT['routes_agree'] = bool(agree5 and agree7)

    # [B] square-mod-5 theorem check
    sq5 = sorted({(i*i) % 5 for i in range(5)})           # {0,1,4}
    OUT['squares_mod5'] = sq5
    OUT['all_e_mod5_are_squares'] = all(v in sq5 for v in seq5)
    OUT['residues_hit_mod5'] = sorted(set(seq5))
    OUT['residues_excluded_mod5'] = sorted(set(range(5)) - set(seq5))
    # [C] mod-7: non-squares hit?
    sq7 = sorted({(i*i) % 7 for i in range(7)})           # {0,1,2,4}
    OUT['squares_mod7'] = sq7
    OUT['nonsquares_hit_mod7'] = sorted(set(seq7) - set(sq7))  # e.g. 3,5,6 -> 7 inert
    OUT['residues_hit_mod7'] = sorted(set(seq7))
    OUT['residues_excluded_mod7'] = sorted(set(range(7)) - set(seq7))
    # 0-exclusion (divisibility) status
    OUT['5_divides_any_e_in_range'] = (0 in seq5)
    OUT['7_divides_any_e_in_range'] = (0 in seq7)
    OUT['matrix_range_Nmax'] = NMAT

    # [D] obstruction: forward-orbit degree growth
    OUT['forward_orbit_maxdeg_mod5'] = orbit_degree_growth(5, 9)
    OUT['forward_orbit_maxdeg_mod7'] = orbit_degree_growth(7, 8)

    # ---------------- verdict logic ----------------
    proven_exclusion_mod5 = (OUT['all_e_mod5_are_squares']
                             and set(OUT['residues_excluded_mod5']) >= {2, 3})
    counterexample = OUT['5_divides_any_e_in_range'] or OUT['7_divides_any_e_in_range']
    # full OI-077 lemma = eventual periodicity + FULL 0-exclusion (5,7 never divide)
    orbit_infinite = (OUT['forward_orbit_maxdeg_mod5'][-1]
                      > OUT['forward_orbit_maxdeg_mod5'][0])
    full_lemma_proven = False   # 0-exclusion + periodicity are WALLED by infinite orbit

    if counterexample:
        verdict = "RESOLVED-B"
        terminal = "an excluded residue (0) is actually hit"
    elif full_lemma_proven:
        verdict = "RESOLVED-A"
        terminal = "full exclusion + eventual periodicity proven"
    else:
        # partial theorem proven (2,3 excluded mod 5) but full lemma obstructed
        verdict = "UNRESOLVED"
        terminal = ("WALLED: partial residue-exclusion PROVEN "
                    "(e_n mod5 in {0,1,4}, residues 2,3 excluded, via golden-norm "
                    "+ ramification); full 0-exclusion & eventual periodicity "
                    "obstructed by the unbounded forward doubling-orbit degree "
                    "(no finite-state / Lucas reduction). No counterexample.")

    OUT['verdict'] = verdict
    OUT['terminal_state'] = terminal
    OUT['proven_exclusion_mod5_residues_2_3'] = bool(proven_exclusion_mod5)
    OUT['orbit_field_degree_unbounded'] = bool(orbit_infinite)
    OUT['elapsed_sec'] = round(time.time() - t0, 1)

    with open("results.json", "w") as f:
        json.dump(OUT, f, indent=1)
    # compact console
    print("e_n mod 5 (n=0..%d):" % NMAT, seq5)
    print("e_n mod 7 (n=0..%d):" % NMAT, seq7)
    print("routes agree:", OUT['routes_agree'])
    print("e_n mod5 all squares:", OUT['all_e_mod5_are_squares'],
          " hit:", OUT['residues_hit_mod5'], " excluded:", OUT['residues_excluded_mod5'])
    print("mod7 non-squares hit (=> 7 inert, norm surjective):", OUT['nonsquares_hit_mod7'],
          " hit:", OUT['residues_hit_mod7'])
    print("5|e_n in range:", OUT['5_divides_any_e_in_range'],
          "  7|e_n in range:", OUT['7_divides_any_e_in_range'])
    print("forward-orbit maxdeg mod5:", OUT['forward_orbit_maxdeg_mod5'])
    print("forward-orbit maxdeg mod7:", OUT['forward_orbit_maxdeg_mod7'])
    print("VERDICT:", verdict)
    print("TERMINAL:", terminal)
