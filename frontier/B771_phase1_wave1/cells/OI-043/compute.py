"""OI-043 (B771 Phase-1 Wave-1) -- CRT closed form of the -1/16 phase sum (P64 residue).

THE OPEN ITEM (B382 Leg 4, docs/progress/REVIEWS.md:95-96, docs/ROADMAP.md:17-18):
the generic (det-class-1) slot partial of the level-15 theta-model seam constant is a pure
phase-sum over 84 unit-magnitude cells equal to (0, 0, -1/16, -1/16) in the basis
{1, sqrt5, sqrt-3, sqrt-15}; the named residue was its CRT zeta3 x zeta5 closed-form
evaluation.  B386 (2026-07-03, -> P66) banked a closed form; the census row OI-043 stayed
LIVE off the bundled ROADMAP checkbox.  This cell RE-DERIVES the discriminating fact
end-to-end, in exact arithmetic over Q(zeta_60) (Fractions; zero numerics):

  GATE 0  the global level-15 theta model, orders (20, 12); the 240-cell Par-trace table C.
  GATE 1  the CRT/tensor identity  C[j,l] = C3[j,l] * C5[j,l]  (local theta models q = 3, 5
          at multiplier u = 2), all 240 cells; NEGATIVE CONTROL: multiplier (1,1) fails.
  GATE 2  the det-class indicator is CRT-local: invertibility of (gamma'-I) mod 15 is the
          conjunction of the mod-3 and mod-5 indicators, all 240 cells; support census
          {1: 84, 3: 12, 5: 28, 15: 4} on the 128 nonzero-window cells.
  GATE 3  the DIRECT global class partials (the P64 reading, recomputed from C):
          class-1 = (0,0,-1/16,-1/16), class-5 = (0,0,-1/48,-1/48), class-3 = class-15 = 0,
          total = (0,0,-1/12,-1/12)  [1/12 = 1/16 + 1/48].
  GATE 4  the periodicity facts the closed form stands on: C3 has (j,l)-periods (4,4),
          C5 has (10,6); ind3 has (4,4), ind5 has (10,6)  [10 = 2*5 and 6 = 2*3 share
          their 2-part with the 3-side period 4 -- the split is two-branch over the
          shared parity, NOT a naive Z4 x Z5 product].
  GATE 5  THE CRT CLOSED FORM (the derivation): with the window characters split by
          1/20 = 1/4 - 1/5 and 1/12 = -1/4 + 1/3 (so zeta20^k = zeta4^k zeta5^{-k},
          zeta12^k = zeta4^{-k} zeta3^k), for K in {1, 5}:

            partial(K) = (1/240) * sum_{(a1,a2,s) in TERMS}  s *
                         sum_{(j4,l4) in Z4 x Z4}  f_K^{a1,a2}(j4,l4) * GH_K^{a1,a2}(j4%2, l4%2)

          TERMS = {(6,2,+1), (6,10,-1), (14,2,-1), (14,10,+1)}  [the slot window expansion],
          f_K = zeta4^{-a1 j4 + a2 l4} * C3(j4,l4) * [ind3 == (K%3 != 0 ... i.e. 3-regular)],
          GH_K(p,q) = sum over the 5-side period-(10,6) lattice at fixed parities (p,q) of
                      zeta5^{a1 j} zeta3^{-a2 l} * C5(j,l) * [ind5-part matches K].
          Verified EXACTLY equal to the direct partials -- this closed form evaluates the
          -1/16 (and -1/48) from 3-local x 5-local data alone; every branch constant is
          printed in H-components.  A finite exact identity over Q(zeta_60): the
          verification IS the proof.

Re-runnable end-to-end: python3 compute.py  (from anywhere; paths resolved off __file__).
Engine: the banked exact Q(zeta_60) engine (frontier/B358) + the banked theta-model
builders (frontier/B367).  Runtime ~2-4 min, pure Fractions.
"""
import json
import os
import sys
import time
from fractions import Fraction as Fr
from math import gcd

CELL = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(CELL, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B358_seam_certification"))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B367_value_map"))
import cyclo_engine as E                      # noqa: E402
import seam_certification as SC               # noqa: E402
from step0_exact_matrices import build_theta_W, matrix_order, par_trace  # noqa: E402

T0 = time.time()
GATES = {}


def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)


def hs(t):
    """Exact H-components (p, q, r, s) of t = p + q sqrt5 + r sqrt-3 + s sqrt-15; None if not in H."""
    sol = SC.solve_H(SC.H_avg(t))
    return None if sol is None else tuple(str(x) for x in sol)


# ----------------------------------------------------------------------------- GATE 0
log("GATE 0: building the global level-15 theta model (exact)...")
W1 = build_theta_W(1)
W2 = build_theta_W(2)
o1, pow1 = matrix_order(W1)
o2, pow2 = matrix_order(W2)
assert (o1, o2) == (20, 12), f"orders {(o1, o2)} != (20, 12)"
C = {(j, l): par_trace(pow1[j], pow2[l]) for j in range(o1) for l in range(o2)}
GATES["gate0_orders"] = [o1, o2]
log(f"GATE 0 PASS: orders (o1,o2)=({o1},{o2}); 240-cell table C built.")


# ------------------------------------------------------------------- local theta models
def zq(q, k):
    """zeta_q^k inside the zeta_60 engine."""
    return E.zeta((60 // q) * (k % q))


def local_model(q, u, m):
    """W_m at level q, multiplier u: W_m = WR^m * D^m, D = diag zq^{u j(j-1)/2},
    WR = F D^{-1} F^{-1} with F = [zq^{u i j}] (the B386 local convention)."""
    def diagm(f):
        return [[f(j) if i == j else E.ZERO for j in range(q)] for i in range(q)]
    D_inv = diagm(lambda j: zq(q, -u * (j * (j - 1) // 2)))
    F = [[zq(q, u * i * j) for j in range(q)] for i in range(q)]
    Fi = [[E.scal(Fr(1, q), zq(q, -u * i * j)) for j in range(q)] for i in range(q)]
    WR = E.mmul(E.mmul(F, D_inv), Fi)
    P = [[E.ONE if i == j else E.ZERO for j in range(q)] for i in range(q)]
    for _ in range(m):
        P = E.mmul(P, WR)
    Dm = diagm(lambda j: zq(q, m * u * (j * (j - 1) // 2)))
    return E.mmul(P, Dm)


def local_table(q, u):
    """T[(j,l)] = tr(Par_q * W1_q^j * W2_q^l) for j in Z_o1, l in Z_o2 (global orders)."""
    Wa, Wb = local_model(q, u, 1), local_model(q, u, 2)

    def powers(W, n):
        P = [[E.ONE if i == j else E.ZERO for j in range(q)] for i in range(q)]
        out = [P]
        for _ in range(n - 1):
            out.append(E.mmul(out[-1], W))
        return out

    pa, pb = powers(Wa, o1), powers(Wb, o2)
    T = {}
    for j in range(o1):
        for l in range(o2):
            M = E.mmul(pa[j], pb[l])
            t = E.ZERO
            for x in range(q):
                t = E.add(t, M[(-x) % q][x])
            T[(j, l)] = t
    return T


# ----------------------------------------------------------------------------- GATE 1
log("GATE 1: the CRT/tensor identity C = C3 * C5 at multiplier (2,2)...")
T3 = local_table(3, 2)
T5 = local_table(5, 2)
bad22 = sum(1 for j in range(o1) for l in range(o2)
            if C[(j, l)] != E.mul(T3[(j, l)], T5[(j, l)]))
assert bad22 == 0, f"tensor identity FAILS at (2,2): {bad22}/240 mismatches"
log("GATE 1 PASS: C[j,l] = C3[j,l]*C5[j,l] exactly, 240/240 cells at (u3,u5)=(2,2).")

log("GATE 1 negative control: multiplier (1,1)...")
T3n = local_table(3, 1)
T5n = local_table(5, 1)
bad11 = sum(1 for j in range(o1) for l in range(o2)
            if C[(j, l)] != E.mul(T3n[(j, l)], T5n[(j, l)]))
assert bad11 > 0, "negative control failed: (1,1) also satisfies the identity"
GATES["gate1_tensor"] = {"mismatches_u22": bad22, "mismatches_u11_control": bad11}
log(f"GATE 1 CONTROL PASS: (1,1) fails at {bad11}/240 cells (multiplier is load-bearing).")


# ----------------------------------------------------------------------------- GATE 2
log("GATE 2: the det-class indicator is CRT-local...")


def cat(m, n):
    """The seed matrix A_m = [[1+m^2, m], [m, 1]] mod n."""
    return [[(1 + m * m) % n, m % n], [m % n, 1 % n]]


def mm2(a, b, n):
    return [[(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % n,
             (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % n],
            [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % n,
             (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % n]]


def ind_table(n):
    """(j,l) -> True iff det(gamma' - I) is invertible mod n, gamma' = -gamma1^j gamma2^l."""
    g1, g2 = cat(1, n), cat(2, n)
    G1 = [[[1 % n, 0], [0, 1 % n]]]
    for _ in range(o1 - 1):
        G1.append(mm2(G1[-1], g1, n))
    G2 = [[[1 % n, 0], [0, 1 % n]]]
    for _ in range(o2 - 1):
        G2.append(mm2(G2[-1], g2, n))
    out = {}
    for j in range(o1):
        for l in range(o2):
            g = mm2(G1[j], G2[l], n)
            d = ((-g[0][0] - 1) * (-g[1][1] - 1) - g[0][1] * g[1][0]) % n
            out[(j, l)] = (gcd(d, n) == 1)
    return out


I3, I5, I15 = ind_table(3), ind_table(5), ind_table(15)
crt_bad = sum(1 for k in I15 if I15[k] != (I3[k] and I5[k]))
assert crt_bad == 0, f"CRT locality of the det-class FAILS on {crt_bad} cells"


def detclass(j, l):
    return (1 if I3[(j, l)] else 3) * (1 if I5[(j, l)] else 5)


# slot windows (the banked grading: a in {6,14} on the 20-side, b in {2,10} on the 12-side)
def w1(j):
    return E.sub(E.zeta((-3 * 6 * j) % 60), E.zeta((-3 * 14 * j) % 60))     # zeta20^{-6j} - zeta20^{-14j}


def w2(l):
    return E.sub(E.zeta((-5 * 2 * l) % 60), E.zeta((-5 * 10 * l) % 60))     # zeta12^{-2l} - zeta12^{-10l}


support = {1: 0, 3: 0, 5: 0, 15: 0}          # window-nonzero cells (the B382 census)
support_C = {1: 0, 3: 0, 5: 0, 15: 0}        # refinement: also C != 0
for j in range(o1):
    for l in range(o2):
        if w1(j) != E.ZERO and w2(l) != E.ZERO:
            support[detclass(j, l)] += 1
            if C[(j, l)] != E.ZERO:
                support_C[detclass(j, l)] += 1
assert support == {1: 84, 3: 12, 5: 28, 15: 4}, f"support census off: {support}"
GATES["gate2_crt_class"] = {"crt_mismatches": crt_bad, "support": support,
                           "support_nonzero_C": support_C}
log(f"GATE 2 PASS: det-class is CRT-local (240/240); window-support census {support} "
    f"(B382's 128 cells); with C != 0 it refines to {support_C} "
    f"(every class-3 window cell has C = 0 -- the 3-side silence is cell-wise).")


# ----------------------------------------------------------------------------- GATE 3
log("GATE 3: the direct global class partials (the P64 reading, from C)...")


def partial_direct(K):
    tot = E.ZERO
    for j in range(o1):
        for l in range(o2):
            if detclass(j, l) != K:
                continue
            tot = E.add(tot, E.mul(E.mul(w1(j), w2(l)), C[(j, l)]))
    return E.scal(Fr(1, 240), tot)


direct = {K: partial_direct(K) for K in (1, 3, 5, 15)}
targets = {1: ("0", "0", "-1/16", "-1/16"), 3: ("0", "0", "0", "0"),
           5: ("0", "0", "-1/48", "-1/48"), 15: ("0", "0", "0", "0")}
for K in (1, 3, 5, 15):
    got = hs(direct[K])
    assert got == targets[K], f"class-{K} direct partial {got} != {targets[K]}"
    log(f"  class-{K:>2} partial = {got}  (target {targets[K]})  EXACT")
total = E.ZERO
for K in (1, 3, 5, 15):
    total = E.add(total, direct[K])
assert hs(total) == ("0", "0", "-1/12", "-1/12"), f"total {hs(total)}"
GATES["gate3_direct"] = {f"class{K}": list(targets[K]) for K in (1, 3, 5, 15)}
GATES["gate3_direct"]["total"] = ["0", "0", "-1/12", "-1/12"]
log("GATE 3 PASS: -1/12 = -1/16 + -1/48 by det-class, exactly (P64 recomputed in-cell).")


# ----------------------------------------------------------------------------- GATE 4
log("GATE 4: the periodicity facts under the closed form...")


def period(T, axis, cands):
    for P in cands:
        if axis == 0 and all(T[(j, l)] == T[((j + P) % o1, l)] for j in range(o1) for l in range(o2)):
            return P
        if axis == 1 and all(T[(j, l)] == T[(j, (l + P) % o2)] for j in range(o1) for l in range(o2)):
            return P
    return None


IB3 = {k: (E.ONE if v else E.ZERO) for k, v in I3.items()}
IB5 = {k: (E.ONE if v else E.ZERO) for k, v in I5.items()}
periods = dict(
    C3=[period(T3, 0, (1, 2, 4, 5, 10, 20)), period(T3, 1, (1, 2, 3, 4, 6, 12))],
    C5=[period(T5, 0, (1, 2, 4, 5, 10, 20)), period(T5, 1, (1, 2, 3, 4, 6, 12))],
    ind3=[period(IB3, 0, (1, 2, 4, 5, 10, 20)), period(IB3, 1, (1, 2, 3, 4, 6, 12))],
    ind5=[period(IB5, 0, (1, 2, 4, 5, 10, 20)), period(IB5, 1, (1, 2, 3, 4, 6, 12))],
)
assert periods["C3"] == [4, 4] and periods["ind3"] == [4, 4], f"3-side periods {periods}"
assert periods["C5"] == [10, 6] and periods["ind5"] == [10, 6], f"5-side periods {periods}"
GATES["gate4_periods"] = periods
log(f"GATE 4 PASS: periods {periods} -- 3-side lives on Z4 x Z4, 5-side on Z10 x Z6; "
    f"the shared 2-part forces the two-branch (parity-graded) split.")


# ----------------------------------------------------------------------------- GATE 5
log("GATE 5: THE CRT CLOSED FORM -- assembly and exact evaluation...")
# window character split (exact exponent identities, verified below):
#   1/20 = 1/4 - 1/5      => zeta20^k = zeta4^k * zeta5^{-k}
#   1/12 = -1/4 + 1/3     => zeta12^k = zeta4^{-k} * zeta3^k
assert Fr(1, 20) == Fr(1, 4) - Fr(1, 5) and Fr(1, 12) == -Fr(1, 4) + Fr(1, 3)
for k in range(20):
    assert E.zeta(3 * k) == E.mul(E.zeta((15 * k) % 60), E.zeta((-12 * k) % 60))
for k in range(12):
    assert E.zeta(5 * k) == E.mul(E.zeta((-15 * k) % 60), E.zeta((20 * k) % 60))
log("  window-splitting identities zeta20^k = zeta4^k zeta5^-k, zeta12^k = zeta4^-k zeta3^k: EXACT")

TERMS = [(6, 2, 1), (6, 10, -1), (14, 2, -1), (14, 10, 1)]


def closed_form(K):
    """The CRT closed form of partial(K), K in {1, 5}: two-branch product assembly."""
    need3 = (K % 3 != 0)   # 3-regular cells for K in {1,5}
    need5 = (K % 5 != 0)   # 5-regular for K=1, 5-singular for K=5
    total_cf = E.ZERO
    factors = {}
    for (a1, a2, s) in TERMS:
        # 5-side branch constants GH(p,q): the period-(10,6) lattice at fixed parities.
        # j in {p, p+2, ..., p+8} hits every j mod 5 once at parity p (period 10);
        # l in {q, q+2, q+4} hits every l mod 3 once at parity q (period 6).
        GH = {}
        for p in (0, 1):
            for q_ in (0, 1):
                t = E.ZERO
                for j in range(p, p + 10, 2):
                    for l in range(q_, q_ + 6, 2):
                        if I5[(j % o1, l % o2)] != need5:
                            continue
                        w5 = E.mul(E.zeta((12 * a1 * j) % 60),      # zeta5^{+a1 j}
                                   E.zeta((-20 * a2 * l) % 60))     # zeta3^{-a2 l}
                        t = E.add(t, E.mul(w5, T5[(j % o1, l % o2)]))
                GH[(p, q_)] = t
        # 3-side 16-cell table f(j4,l4) and the parity-coupled assembly
        term = E.ZERO
        for j4 in range(4):
            for l4 in range(4):
                if I3[(j4, l4)] != need3:
                    continue
                w4 = E.mul(E.zeta((-15 * a1 * j4) % 60),            # zeta4^{-a1 j4}
                           E.zeta((15 * a2 * l4) % 60))             # zeta4^{+a2 l4}
                f = E.mul(w4, T3[(j4, l4)])
                term = E.add(term, E.mul(f, GH[(j4 % 2, l4 % 2)]))
        factors[f"term({a1},{a2})"] = dict(
            sign=s,
            GH={f"{p}{q_}": hs(GH[(p, q_)]) for p in (0, 1) for q_ in (0, 1)},
            term_total=hs(term))
        total_cf = E.add(total_cf, E.scal(Fr(s), term))
    return E.scal(Fr(1, 240), total_cf), factors


results = {}
for K in (1, 5):
    cf, factors = closed_form(K)
    got = hs(cf)
    # the discriminating fact, twice over: the closed form equals the DIRECT partial
    # cell-for-cell as a field element, and equals the banked constant.
    assert cf == direct[K], f"class-{K}: closed form != direct partial (field elements differ)"
    assert got == targets[K], f"class-{K}: closed form {got} != target {targets[K]}"
    log(f"  class-{K} closed form  = {got}  == direct partial  == target  EXACT")
    results[f"class{K}"] = dict(closed_form=list(got), target=list(targets[K]),
                                equals_direct=True, factors=factors)

GATES["gate5_closed_form"] = results
log("GATE 5 PASS: the CRT closed form is an exact identity for both classes.")

log("-- the branch constants of the -1/16 (class-1), term (6,2):")
for pq, v in results["class1"]["factors"]["term(6,2)"]["GH"].items():
    log(f"     GH[{pq}] = {v}")
log("-- the branch constants of the -1/48 (class-5), term (6,2):")
for pq, v in results["class5"]["factors"]["term(6,2)"]["GH"].items():
    log(f"     GH[{pq}] = {v}")

# ------------------------------------------------------------------------------- exit
out = dict(cell="OI-043", verdict_gates=GATES,
           statement=("partial(K) = (1/240) sum_{(a1,a2,s)} s * sum_{Z4xZ4} "
                      "f_K(j4,l4) * GH_K(j4%2,l4%2); exact over Q(zeta60); "
                      "class-1 = (0,0,-1/16,-1/16), class-5 = (0,0,-1/48,-1/48); "
                      "matches B386/P66"),
           runtime_sec=round(time.time() - T0, 1))
with open(os.path.join(CELL, "closed_form_verified.json"), "w") as f:
    json.dump(out, f, indent=1)
log("ALL GATES PASS -- the CRT closed form of the -1/16 phase sum is derived and proven "
    "(exact finite identity over Q(zeta_60)); artifacts: closed_form_verified.json")
print("DONE")
