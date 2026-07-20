"""
B724 PROBE 3 (Path 1) — GGM resurgence/3D-index integers vs banked object integers.
OBJECT-INTERNAL consistency check, base-rate-gated. Structural/arithmetic only; HINT-grade.
COMPUTE-NOT-CITE: we recompute GGM's fig-8 3D-index in-sandbox (from the paper's own
q-series defs, eq. 13a/13b/80 of arXiv:2007.10190) and recompute the banked torsions.

Two-outcome:
  A = a PRINCIPLED object-internal identity (a resurgence integer = a torsion/sum-rule
      integer, or a q-series identity) that BEATS the base rate (p < 0.01).
  B = no match / base-rate coincidences only.
"""
import json, os, math
from fractions import Fraction as Fr
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
q = sp.Symbol('q')
NT = 14  # q-series truncation order

out = []
def p(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

# ----------------------------------------------------------------------------
# 1. GGM fig-8 (4_1) DGG rotated 3D-index — RECOMPUTED from the paper's q-series.
#    eq (13a): G0_0(q) = sum_n (-1)^n q^{n(n+1)/2} / (q;q)_n^2
#    eq (13b): G1_0(q) = sum_n (-1)^n q^{n(n+1)/2}/(q;q)_n^2 * (E1(q) + 2 sum_{j=1}^n (1+q^j)/(1-q^j))
#    E1(q) = 1 - 4 sum_{n>=1} q^n/(1-q^n)
#    eq (80): Ind^rot_{4_1}(q) = G0_0(q) * G1_0(q) = 1 - 8q - 9q^2 + 18q^3 + 46q^4 + O(q^5)
# ----------------------------------------------------------------------------
# --- fast truncated power series over Q, as coefficient lists of length NT ---
from fractions import Fraction as F
def zero(): return [F(0)] * NT
def const(c): a = zero(); a[0] = F(c); return a
def add(a, b): return [a[i] + b[i] for i in range(NT)]
def scal(a, c): return [a[i] * F(c) for i in range(NT)]
def mul(a, b):
    r = zero()
    for i in range(NT):
        if a[i] == 0: continue
        for j in range(NT - i):
            if b[j] != 0:
                r[i + j] += a[i] * b[j]
    return r
def inv(a):  # 1/a, a[0]!=0
    r = zero(); r[0] = 1 / a[0]
    for k in range(1, NT):
        s = F(0)
        for j in range(1, k + 1):
            s += a[j] * r[k - j]
        r[k] = -s / a[0]
    return r
def qpow(e):  # q^e as series
    a = zero()
    if e < NT: a[e] = F(1)
    return a

# (q;q)_n^2  as a series (product of (1-q^j)^2)
def qpoch2(n):
    r = const(1)
    for j in range(1, n + 1):
        f = const(1)
        if j < NT: f[j] = F(-1)
        r = mul(mul(r, f), f)
    return r

# E1(q) = 1 - 4 sum_{n>=1} q^n/(1-q^n) = 1 - 4 sum_{n>=1} sum_{k>=1} q^{nk}
E1 = const(1)
for n in range(1, NT):
    k = 1
    while n * k < NT:
        E1[n * k] += F(-4)
        k += 1

# 2 sum_{j=1}^n (1+q^j)/(1-q^j)
def hn(n):
    r = zero()
    for j in range(1, n + 1):
        num = const(1); num = add(num, qpow(j))          # 1 + q^j
        den = const(1)
        if j < NT: den[j] += F(-1)                        # 1 - q^j
        r = add(r, scal(mul(num, inv(den)), 2))
    return r

G0 = zero(); G1 = zero()
for n in range(0, NT):
    tri = n * (n + 1) // 2
    if tri >= NT: break
    base = mul(scal(qpow(tri), (-1)**n), inv(qpoch2(n)))
    G0 = add(G0, base)
    inner = add(E1, hn(n))                                # E1 + 2 sum(...)  (m=0 so 2m=0)
    G1 = add(G1, mul(base, inner))

Ind = mul(G0, G1)
ind_coeffs = [int(Ind[k]) for k in range(0, min(11, NT))]
p("=== GGM fig-8 (4_1) DGG rotated 3D-index, RECOMPUTED from eq 13a/13b (arXiv:2007.10190) ===")
p("G0_0(q) coeffs [q^0..q^5] =", [int(G0[k]) for k in range(6)])
p("Ind^rot_{4_1}(q) coeffs [q^0..q^10] =", ind_coeffs)
GGM_eq80 = [1, -8, -9, 18, 46]
p("GGM paper eq (80) states     [q^0..q^4] =", GGM_eq80)
p("MATCH eq(80)?", ind_coeffs[:5] == GGM_eq80)

# chat-1's quoted series I_T(4mu+lambda) = q - q^4 - 2q^5 - 5q^6 - 8q^7 - 10q^8 - 11q^9 - 6q^10
chat1 = {1: 1, 4: -1, 5: -2, 6: -5, 7: -8, 8: -10, 9: -11, 10: -6}
p("\nchat-1 quoted I_T(4mu+lambda) coeffs =", chat1)
p("GGM actual rotated-index coeffs        =", {k: ind_coeffs[k] for k in range(1, 11)})
p("chat-1 series == GGM rotated 3D-index?  ->", all(ind_coeffs[k] == chat1.get(k, 0) for k in range(0, 11)))

# GGM Stokes constants for 4_1 (eq 79): off-diagonal +/-3
GGM_stokes_41 = [3]         # |entries| of S^+(0)=[[1,3],[0,1]]
# GGM 5_2 Stokes matrix (eq 101): entries 4, 3 ; rotated index (eq 102): 1,-12,3,74,90
GGM_stokes_52 = [4, 3]
GGM_ind_52 = [1, -12, 3, 74, 90]
# GGM 4_1 perturbative-series numerators over Q(sqrt-3) (eq 8): 1, 11, 697, 724351
GGM_pert_41 = [1, 11, 697, 724351]
p("\nGGM 4_1 Stokes constants           =", GGM_stokes_41)
p("GGM 4_1 perturbative numerators     =", GGM_pert_41, " (over Q(sqrt-3))")
p("GGM 5_2 Stokes constants           =", GGM_stokes_52)
p("GGM 5_2 rotated 3D-index coeffs     =", GGM_ind_52)

# ----------------------------------------------------------------------------
# 2. Banked OBJECT integers — RECOMPUTED (not cited).
# ----------------------------------------------------------------------------
DATA = os.path.join(ROOT, "B581_six_torsions", "six_torsions_results.json")
d = json.load(open(DATA))
t = sp.Symbol('t')
def poly(m):
    qd = d[m]['quotient']
    P = sum(sp.Rational(Fr(a)) * t**k for k, (a, b) in enumerate(qd))
    lead = sp.Poly(P, t).all_coeffs()[0]
    return sp.Poly(sp.expand(P / lead), t)
torsions = {}
for m in ['1', '4', '5', '7', '8', '11']:
    P = poly(m)
    red, rem = sp.div(P.as_expr(), t - 1)
    tau = int(sp.expand(red.subs(t, 1)))
    torsions[int(m)] = tau
p("\n=== Banked object integers (RECOMPUTED) ===")
p("B581 torsion spectrum tau_m =", torsions)
for m, tau in torsions.items():
    p("  m=%2d  tau=%-40d |tau|=%d  log10=%.3f" % (m, tau, abs(tau), math.log10(abs(tau))))
# sum-rule integers (B671/B684/G1)
sumrule = {"7983360": 7983360, "7983360/13": Fr(7983360, 13), "2661120/13": Fr(2661120, 13)}
p("Generation sum-rule integers =", sumrule)
p("7983360 factorization =", sp.factorint(7983360))

# ----------------------------------------------------------------------------
# 3. COMPARISON + BASE RATE.
# ----------------------------------------------------------------------------
p("\n=== COMPARISON ===")
ggm_all = set(abs(x) for x in GGM_stokes_41 + GGM_stokes_52 + GGM_pert_41 + ind_coeffs + GGM_ind_52)
ggm_all.discard(0)
banked_all = set(abs(x) for x in torsions.values()) | {7983360}
p("GGM integer bag |.|   =", sorted(ggm_all))
p("banked integer bag |.|=", sorted(banked_all))
common = ggm_all & banked_all
p("EXACT common integers =", sorted(common))

# The only overlap: 3 (GGM Stokes const for 4_1)  vs  |tau_1| = 3.
# Base rate for a single-small-integer coincidence.
p("\n--- BASE RATE for the '3 = 3' coincidence ---")
p("3 is the ramified prime of Q(sqrt-3) (disc = -3); the fig-8 trace field IS Q(sqrt-3),")
p("and the object's field IS Q(sqrt-3) (the object == fig-8 trace map, B67/B71).")
# base rate: probability a 'random' small arithmetic invariant of Q(sqrt-3) contains |3|
# among its low integers. We treat GGM's small-int bag (Stokes+index low coeffs) and ask:
# how many distinct small integers (|.| <= 50) does GGM produce, and what is the chance a
# given target small integer (like |tau_1|=3) lands in that bag by size alone?
ggm_small = sorted(x for x in ggm_all if x <= 50)
p("GGM small integers (|.|<=50) =", ggm_small, " count =", len(ggm_small))
# a target drawn uniformly from {1..50}: chance it hits the GGM small bag
p("crude base rate P(random target in {1..50} hits GGM small bag) = %d/50 = %.2f"
  % (len(ggm_small), len(ggm_small) / 50))
# but tau_1=3 is NOT random: 3 is FORCED in both by the shared field => P(3 present)~1
p("Because 3 is forced by the shared field, P(3 in both) ~ 1 (EXPECTED, not surprising).")

p("\n--- BASE RATE for a LARGE-integer identity ---")
p("The banked large integers (260736, 165110400, 3.26e15, 1.01e20, 6.9e36, 7983360) appear")
p("NOWHERE in GGM's 4_1 data. GGM's 4_1 integers are all tiny (<=724351, mostly <100).")
p("A genuine principled identity would need a specific LARGE integer to coincide; none does.")
p("large-overlap count =", len([x for x in common if x > 100]))

# q-series identity test: is the object's torsion spectrum a q-series with the GGM coeffs?
p("\n--- q-SERIES IDENTITY test ---")
p("Object torsions tau_m are single Reidemeister-torsion integers indexed by metallic level m")
p("(a SPECTRUM), not the coefficients of a q-series. GGM's 3D-index is a q-series in q.")
p("Different structural type => no q-series identity available to test. (STRUCTURAL mismatch.)")

# ----------------------------------------------------------------------------
# 4. VERDICT
# ----------------------------------------------------------------------------
p("\n=== VERDICT ===")
p("Discriminating facts computed in-sandbox:")
p(" (i)  GGM fig-8 rotated 3D-index recomputed = %s  == paper eq(80) %s -> %s"
  % (ind_coeffs[:5], GGM_eq80, ind_coeffs[:5] == GGM_eq80))
p(" (ii) chat-1's I_T(4mu+lambda) = q - q^4 - 2q^5 - ... does NOT equal GGM's actual 4_1")
p("      3D-index (1 - 8q - 9q^2 + 18q^3 + 46q^4). chat-1's quote is NOT the DGG rotated index.")
p(" (iii)The ONLY exact integer overlap is 3 (= |tau_1| = GGM 4_1 Stokes const): a single")
p("      small integer FORCED by the shared field Q(sqrt-3); base rate ~ 1, p NOT < 0.01.")
p(" (iv) No large banked integer (torsion 10^5..10^37, sum-rule 7983360) matches any GGM int.")
p(" (v)  No q-series identity (structural type mismatch: spectrum vs q-series).")
p("OUTCOME B: no principled object-internal identity beats the base rate. The shared field")
p("Q(sqrt-3) is REAL (the object IS the fig-8) but that is a necessary-not-sufficient")
p("structural fact, not a base-rate-beating numerical identity. HINT-grade at most.")

with open(os.path.join(HERE, "b724_probe3_out.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
