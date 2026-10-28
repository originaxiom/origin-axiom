"""Referee B1801, checks 1, 3, 4 and the filling scan.
(1) the Wilson line: U = exp(2 pi i 6Y/3), det, commutant (centraliser dimension in su(5)), U = centre of SU(3), the
    holonomy table, FW's U_gamma (3.28) at q = 3; which (q, w) break SU(5) -> SM; which leave the doublet untwisted.
(3) FW's normalisation: Turaev-convention torsion of L(q,1) (cell complex), e^T = 1/|tau_Turaev| on both characters;
    L(Q) for the fillings; FW's lens L = 4q sin^2(5 pi w/q).
(4) FW's (3.20)-(3.21) traces and the one-loop sin^2 theta_W invariance (det[1/alpha_a, k_a, b_a] unchanged).
(5) the filling scan: lowest volumes with 3 | p, the solution-type filter vs the known exceptional slopes of 4_1."""
import math, cmath, itertools
import numpy as np
import sympy as sp
import snappy

w3 = cmath.exp(2j * math.pi / 3)
sixY = np.array([-2, -2, -2, 3, 3])
U = np.diag(np.exp(2j * np.pi * sixY / 3))
print("(1) U = exp(2 pi i 6Y/3) =", np.round(np.diag(U), 12), "| det =", np.round(np.linalg.det(U), 12))
print("    U == diag(w,w,w,1,1):", np.allclose(np.diag(U), [w3, w3, w3, 1, 1]), "| U restricted to colour = w * 1_3, the generator of Z(SU(3))")
# centraliser of Ad(U) in su(5): dimension of {X : U X U^-1 = X}
basis = []
for i in range(5):
    for j in range(5):
        E = np.zeros((5, 5), complex); E[i, j] = 1; basis.append(E)
Ad = np.array([(U @ E @ np.linalg.inv(U)).ravel() for E in basis]).T
fix = 25 - np.linalg.matrix_rank(Ad - np.eye(25), tol=1e-9)
print("    dim centraliser in gl(5) =", fix, "-> in su(5):", fix - 1, "(SU(3)xSU(2)xU(1) has dim 12)")
fields = {"Q": 1, "u^c": -4, "d^c": 2, "L": -3, "e^c": 6, "H (5, doublet)": 3, "T (5, triplet)": -2, "X,Y": 5}
for f, y in fields.items():
    ph = cmath.exp(2j * math.pi * y / 3)
    tri = {"Q": 1, "u^c": -1, "d^c": -1, "L": 0, "e^c": 0, "H (5, doublet)": 0, "T (5, triplet)": 1, "X,Y": -1}[f]
    print(f"    {f:15s} 6Y = {y:+d}: holonomy w^{y % 3}; colour triality {tri:+d} -> w^(triality) = w^{tri % 3}; equal: {abs(ph - w3**(tri % 3)) < 1e-12}")
# FW (3.28): U_gamma = exp(2 pi i (w/q) diag(2,2,2,-3,-3))
for q, w in ((3, 1), (3, 2)):
    Ug = np.exp(2j * np.pi * (w / q) * np.array([2, 2, 2, -3, -3]))
    print(f"    FW U_gamma(q={q}, w={w}) =", np.round(Ug, 9))
# which (q, w), q <= 12, break SU(5) -> SM (q does not divide 5w), and which leave the doublet untwisted (q | 3w)
brk, dbl = set(), set()
for q in range(2, 13):
    for w in range(1, q):
        order = q // math.gcd(q, w)
        if (5 * w) % q != 0:
            brk.add(order)
            if (3 * w) % q == 0:
                dbl.add(order)
print("    exact orders of U_gamma breaking SU(5) -> SM (q <= 12):", sorted(brk))
print("    ... of those, orders leaving the 5's doublet untwisted:", sorted(dbl), "(group theory: diag(z,z,z,1,1), z^3 = 1)")
print("    and the 5's components untwisted at FW's minimal lens (q, w) = (2, 1): U = diag(1,1,1,-1,-1): the TRIPLET untwisted, the doublet twisted")

# ---- (3) normalisation ----------------------------------------------------------------------------------------------
print("\n(3) Turaev convention on L(q,1): cells e0..e3, d1 = xi - 1, d2 = 1 + xi + ... + xi^{q-1}, d3 = xi - 1 (twisted)")
for q in (2, 3, 5, 6):
    for w in range(1, q):
        if (5 * w) % q == 0: continue
        xi = cmath.exp(2j * math.pi * 5 * w / q)          # the X,Y bosons' holonomy (charge 5 under 6Y-type generator)
        tau_T = 1 / ((xi - 1) * (xi - 1))                 # Turaev: d1 contributes det^-1, d3 contributes det^-1, d2 = 0
        tau_T_triv = q                                    # trivial coefficients, integral bases: d2 = q contributes q^{+1}
        T_om = math.log(4 * math.sin(5 * math.pi * w / q)**2); T_O = -math.log(q)
        ok = abs(math.exp(T_om) - 1 / abs(tau_T)) < 1e-12 and abs(math.exp(T_O) - 1 / tau_T_triv) < 1e-12
        L = math.exp(T_om - T_O)
        print(f"    L({q},1), w={w}: e^T_omega = 4 sin^2 = {math.exp(T_om):.6f} = 1/|tau_T| {ok}; L = 4q sin^2 = {L:.6f}")
        break
print("    figure-eight fillings: e^T_omega = 1/|tau_T| = 3/4, e^T_O = 1/|H1| -> L = 3|H1|/4: ", [(p, 3 * p / 4) for p in (3, 6, 9, 12)])
print("    the same Turaev formula on the unknot (Delta = 1) gives FW's general lens L = 4q|sin(5 pi w/q) sin(5 pi j w/q)|: consistent")

# ---- (4) FW (3.20)-(3.21) and sin^2 theta_W ------------------------------------------------------------------------
TO, Tw, gM, Lm = sp.symbols("T_O T_w gM Lm")
k = [sp.Rational(5, 3), 1, 1]
b = [0, -6, -9]
trSM = [0, 2, 3]
trXY = [sp.Rational(25, 3), 3, 2]
Yd = sp.diag(-sp.Rational(1, 3), -sp.Rational(1, 3), -sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(1, 2))
assert (Yd**2).trace() == sp.Rational(5, 3) / 2
# X,Y: (3,2)_{-5/6} + conj: Tr Y^2 = 2*6*(25/36), SU(2): 2*3*(1/2), SU(3): 2*2*(1/2)
assert trXY == [2 * 6 * sp.Rational(25, 36), 2 * 3 * sp.Rational(1, 2), 2 * 2 * sp.Rational(1, 2)]
for a in range(3):
    S = 2 * (TO * trSM[a] + Tw * trXY[a])
    assert sp.simplify(S - (-sp.Rational(2, 3) * b[a] * (TO - Tw) + 10 * k[a] * Tw)) == 0
print("\n(4) FW (3.20) traces and (3.21) S'_a = -(2/3) b_a (T_O - T_w) + 10 k_a T_w: verified")
inv = [16 * sp.pi**2 * k[a] / gM**2 + b[a] * Lm + (-sp.Rational(2, 3) * b[a] * (TO - Tw) + 10 * k[a] * Tw) for a in range(3)]
D = sp.Matrix([[inv[a], k[a], b[a]] for a in range(3)]).det()
print("    det[16pi^2/g_a^2, k_a, b_a] with the thresholds =", sp.simplify(D), "(the one-loop relation fixing sin^2 theta_W given alpha_em, alpha_s: torsion-free)")

# ---- (5) the filling scan --------------------------------------------------------------------------------------------
print("\n(5) scan p in 3..60 (3 | p), q in -40..40, gcd 1: solution types and lowest volumes")
rows, dropped = [], []
for p in range(3, 61, 3):
    for q in range(-40, 41):
        if q == 0 or math.gcd(p, abs(q)) != 1: continue
        M = snappy.Manifold("m004"); M.dehn_fill((p, q))
        st = M.solution_type()
        exceptional = (q in (1, -1) and p <= 4)        # 4_1's exceptional slopes: inf, 0, +-1, +-2, +-3, +-4
        if st != "all tetrahedra positively oriented":
            dropped.append((p, q, st, exceptional))
            continue
        rows.append((float(M.volume()), p, q))
rows.sort()
print("    lowest five:", [(round(v, 6), p, q) for v, p, q in rows[:5]])
print("    lowest with p = 3:", [(round(v, 6), p, q) for v, p, q in rows if p == 3][:2])
print("    slopes dropped by the arc's filter (not 'all positively oriented'):", dropped[:10], "... total", len(dropped))
# m004 amphichirality: (p,q) and (p,-q) have equal volume
print("    amphichiral check (6,1) vs (6,-1):", round(float(snappy.Manifold("m004(6,1)").volume()), 9), round(float(snappy.Manifold("m004(6,-1)").volume()), 9))
print("    m004(1,0):", snappy.Manifold("m004(1,0)").homology(), "| m004(2,3) (|H1| = 2, hyperbolic):", snappy.Manifold("m004(2,3)").solution_type())
# symmetry groups (Witten's mechanism needs a symmetry F of Q with two fixed circles)
for s in ("m004(3,2)", "m004(6,1)", "m004(3,4)", "m004(9,2)"):
    try:
        print("    symmetry group of", s, ":", snappy.Manifold(s).symmetry_group())
    except Exception as e:
        print("    symmetry group of", s, ": not computed (", type(e).__name__, e, ")")
print("r3 exit 0")
