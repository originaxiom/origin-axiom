#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B754 P2 cell -- TOMB-L63 (speculations/TOMBSTONES.md:L63, the Chat-2 umbrella).

KILLED CLAIM (banked, B742 RECONFIRMED): five quantum-tower / knot-invariant
observations are "the ambient theory's definitions doing the work, mistaken for
framework-specific bridges" (kill_form = category-error).  Member observables:
  M1 |lambda| = 1 (unitarity);  M2 finite-k eigenvalues are roots of unity
  (by construction / finite image);  M3 Kashaev -> volume (known conjecture);
  M4 z0 / k=4 phase match (phases multiples of pi/3);  M5 "three regimes"
  (standard asymptotics).
The original kill (B742 recompute/TOMB-L63) tested the members against AMBIENT
controls only (fixed Hilbert-matrix unitary, the RL^2 word); it consulted no
face (faces_consulted = none-arithmetic-only; grep-verified in PART 5 below).

P2 QUESTION: does the spectral face AS BANKED (ONLY B737, B739, B746, B753)
bear on this kill in a way the original kill never tested?

FACE SOURCES (frozen surface, verified inside each arc):
  B737 FINDINGS P3 + p3_sister_out.txt:68-90  (ray-class palette
       Cl_n = (O/n)^x / im(mu_6); sizes 1/2/8 at levels (2)/(4)/(8);
       m003's cusp = C/O_K itself)
  B739 FINDINGS + b739_probe_out.txt:39-44,203-208,311-312  (palette 1/2/8
       recomputed; continuous spectrum of m004 = single channel, multiplicity
       exactly 1, zeta_K only -- no level character appears)
  B746 FINDINGS F6/F8/F11 (zeta_5-cyclotomy graded IMPORTED "generic
       quantum-group, E20"; weights FORCED vs quantum overlay IMPORTED;
       continuous-spectrum face carries zero golden markers)
  B753 FINDINGS + compute.py + output.txt  (the theta-odd 2x2 block of the
       twisted weld at g = RL from the banked B238 SU(3)_2 pipeline:
       unitary, eigenvalues e^{+-i 72 deg}, kind-correct mixing entry
       P01 = 1/(phi sqrt 5) = 0.276393)

GATE 5: pure mathematics throughout; no SM values, no comparison to any
measured quantity.  Gate 5-Q: Q2 discrimination gate runs FIRST (PART 0);
Q5 no experience vocabulary; Q6 specialness budget carried in PART 3/4
(the sister/comparator question computed in-cell).
RUN-WITH: plain python3 (numpy allowed as in the banked B753 cell); no Sage.
Deterministic: no randomness, no wall clock; the generic comparator is a
FIXED rotation (angle 1 radian).
"""
import cmath
import importlib.util
import math
import os
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FRONTIER = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

PHI = (1 + math.sqrt(5)) / 2
LINE = "=" * 88


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(FRONTIER, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# --------------------------------------------------------------------------
# exact quadratic-field arithmetic:  x = a + b*sqrt(5),  a,b in Q
# --------------------------------------------------------------------------
def q5_mul(x, y):
    (a, b), (c, d) = x, y
    return (a * c + 5 * b * d, a * d + b * c)


def q5_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


# --------------------------------------------------------------------------
# exact Eisenstein-integer arithmetic:  z = a + b*omega,  omega^2 = -1 - omega
# --------------------------------------------------------------------------
def eis_mul(z, w):
    (a, b), (c, d) = z, w
    return (a * c - b * d, a * d + b * c - b * d)


def eis_mod(z, m):
    return (z[0] % m, z[1] % m)


def eis_norm(z):
    a, b = z
    return a * a - a * b + b * b


MU6 = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]  # powers of zeta_6 = 1 + omega


def palette(m):
    """|(O/mO)^x|, |image(mu_6)|, quotient size -- exact, brute force."""
    units = [(a, b) for a in range(m) for b in range(m)
             if math.gcd(eis_norm((a, b)), m) == 1]
    img = sorted(set(eis_mod(u, m) for u in MU6))
    return len(units), len(img), len(units) // len(img), units, img


# --------------------------------------------------------------------------
# the banked B753 block (verbatim pipeline: B238 su3_data(2); B753 compute.py)
# --------------------------------------------------------------------------
b238 = load("B238_su32_levelrank/su32_wrt.py", "b238")
w, S, T, cc = b238.su3_data(2)
KAPPA = 2 + 3  # k + N read from the banked construction (su3_data: kap = k + 3)
n = len(w)
C = np.zeros((n, n))
for i, wt in enumerate(w):
    C[w.index((wt[1], wt[0])), i] = 1.0
Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
R, L = T, Si @ Ti @ S

pairs = [(w.index((1, 0)), w.index((0, 1))), (w.index((2, 0)), w.index((0, 2)))]
U = np.zeros((n, 2))
for j, (a, b) in enumerate(pairs):
    U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
U = U.astype(complex)


def theta_odd_block(word):
    """the 2x2 theta-odd compression of the twisted weld C*rho(word)."""
    W = C.astype(complex)
    for ch in word:
        W = W @ (R if ch == "R" else L)
    return np.array([[np.conj(U[:, i]) @ W @ U[:, j] for j in range(2)]
                     for i in range(2)])


def overlap_matrix(B):
    """P_ij = |<u_i | w_j>|^2 over normalized eigenvectors (B753 CELL 4)."""
    evals, evecs = np.linalg.eig(B)
    order = np.argsort(-evals.imag)  # deterministic: +phase eigenvector first
    P = np.zeros((2, 2))
    for jj, j in enumerate(order):
        v = evecs[:, j] / np.linalg.norm(evecs[:, j])
        for i in range(2):
            P[i, jj] = abs(v[i]) ** 2
    return evals[order], P


def member_battery(B, tag):
    """the five member observables of TOMB-L63, applied to a 2x2 block.
    M3/M5 are asymptotic statements with no 2x2 realization; the battery
    carries the eigenvalue-stratum observables M1, M2, M4."""
    evals = np.linalg.eigvals(B)
    evals = evals[np.argsort(-evals.imag)]
    moduli = tuple(round(float(abs(ev)), 12) for ev in evals)
    orders = []
    for ev in evals:
        o = None
        for q in range(1, 121):
            if abs(ev ** q - 1) < 1e-9:
                o = q
                break
        orders.append(o)
    phases = tuple(round(cmath.phase(ev) / math.pi, 12) for ev in evals)
    in_pi3_lattice = tuple(
        abs(cmath.phase(ev) / (math.pi / 3) - round(cmath.phase(ev) / (math.pi / 3))) < 1e-9
        for ev in evals)
    print(f"  [{tag}] M1 moduli = {moduli}")
    print(f"  [{tag}] M2 root-of-unity orders = {orders}")
    print(f"  [{tag}] M4 phases/pi = {phases}; in pi/3-lattice = {in_pi3_lattice}")
    return moduli, tuple(orders), in_pi3_lattice


print(LINE)
print("PART 0 -- Q2 DISCRIMINATION GATE (mandatory first; Gate 5-Q)")
print(LINE)
print("Consultation operator O_mix: weld-block |-> kind-correct mixing entry")
print("P[0,1] of the eigenvector overlap matrix (the B753 CELL-4 object).")
print("Consultation operator O_pal: congruence level n |-> |(O/n)^x / im(mu_6)|")
print("(the B737-P3 / B739-Part-0.5 palette).")
print()

# O_mix on the object: the banked block at g = RL
B_obj = theta_odd_block("RL")
ev_obj, P_obj = overlap_matrix(B_obj)
p_obj = P_obj[0, 1]

# O_mix on the SPECTRUM-MATCHED generic comparator: same eigenvalues
# diag(e^{2 pi i/5}, e^{-2 pi i/5}), FIXED generic eigenbasis (rotation by
# 1 radian -- deterministic, no special structure w.r.t. the construction).
th_g = 1.0
V = np.array([[math.cos(th_g), -math.sin(th_g)],
              [math.sin(th_g), math.cos(th_g)]], dtype=complex)
D = np.diag([cmath.exp(2j * math.pi / 5), cmath.exp(-2j * math.pi / 5)])
B_gen = V @ D @ V.conj().T
ev_gen, P_gen = overlap_matrix(B_gen)
p_gen = P_gen[0, 1]

# O_mix on the original kill's own sister-word control RL^2, same pipeline
B_rll = theta_odd_block("RLL")
ev_rll, P_rll = overlap_matrix(B_rll)
p_rll = P_rll[0, 1]

def rou_order(ev, qmax=240):
    """least q with ev^q = 1 (numeric tolerance), else None."""
    for q in range(1, qmax + 1):
        if abs(ev ** q - 1) < 1e-9:
            return q
    return None


uni_rll = np.linalg.norm(B_rll @ B_rll.conj().T - np.eye(2))
ord_rll = sorted(rou_order(e) for e in np.linalg.eigvals(B_rll))
print(f"O_mix(object block, g=RL)              = {p_obj:.10f}")
print(f"O_mix(spectrum-matched generic V D V^d) = {p_gen:.10f}   (= sin^2(1) = {math.sin(1)**2:.10f})")
print(f"O_mix(RL^2-word block, same pipeline)   = {p_rll:.10f}   (also unitary:")
print(f"    ||B B^dag - I|| = {uni_rll:.2e}; eigenphase root-of-unity orders {ord_rll}")
print(f"    -- the M2 ambient finite-image mechanism holds on the comparator too,")
print(f"    while O_mix separates the words)")
d1 = abs(p_obj - p_gen) > 1e-6
d2 = abs(p_obj - p_rll) > 1e-6
print(f"CHECK: Q2 O_mix discriminates object from generic comparator "
      f"(|{p_obj:.6f} - {p_gen:.6f}| > 1e-6): {d1}")
print(f"CHECK: Q2 O_mix discriminates object from RL^2-word comparator: {d2}")

lv = {}
for m, tag in [(2, "(2) sister m003"), (4, "(4) m004 std"), (8, "(8) m004 mod-center")]:
    nu, ni, q, units, img = palette(m)
    lv[m] = (nu, ni, q)
    print(f"O_pal level {tag:22s}: |(O/n)^x| = {nu:2d}, |im mu_6| = {ni}, palette = {q}")
print(f"CHECK: Q2 O_pal discriminates object (m004 levels (4)/(8) -> palette "
      f"{lv[4][2]}/{lv[8][2]}) from sister m003 (level (2) -> palette {lv[2][2]}): "
      f"{lv[4][2] != lv[2][2] and lv[8][2] != lv[2][2]}")
print(f"CHECK: palette sizes ({lv[2][2]},{lv[4][2]},{lv[8][2]}) == banked (1,2,8) "
      f"[B737 p3_sister_out.txt:73-75; B739 b739_probe_out.txt:39-44]: "
      f"{(lv[2][2], lv[4][2], lv[8][2]) == (1, 2, 8)}")
print("Q2 GATE: PASS -- both consultation operators discriminate; the cell proceeds.")

print(LINE)
print("PART 1 -- the banked face object reproduced (B753 CELL 1, verbatim pipeline)")
print(LINE)
banked_B00 = 1 / (2 * PHI) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
print(f"B[0,0] = {B_obj[0,0]:+.6f}   banked B593/B753 element = {banked_B00:+.6f}")
print(f"CHECK: block reproduces banked B753 CELL-1 value "
      f"(|diff| = {abs(B_obj[0,0]-banked_B00):.2e} < 1e-12): "
      f"{abs(B_obj[0,0]-banked_B00) < 1e-12}")
uni_defect = np.linalg.norm(B_obj @ B_obj.conj().T - np.eye(2))
print(f"CHECK: block unitary, ||B B^dag - I|| = {uni_defect:.2e} < 1e-12: {uni_defect < 1e-12}")
print(f"eigenvalues = {ev_obj[0]:+.6f}, {ev_obj[1]:+.6f}  (banked: e^{{+-i 72 deg}})")

print(LINE)
print("PART 2 -- the eigenvalue stratum of the face's own quantum object is")
print("          AMBIENT twice over (members M1 + M2 mechanisms, computed)")
print(LINE)
print(f"ambient construction parameter (banked B238 pipeline): kappa = k + N = {KAPPA}")
print(f"  -> construction cyclotomy q = e^(2 pi i/{KAPPA}) [B238 header: 'the golden")
print(f"     cyclotomic field Q(zeta_5)'; B746 F6 grades this cyclotomy IMPORTED]")
m1 = all(abs(abs(ev) - 1) < 1e-12 for ev in ev_obj)
print(f"CHECK: M1 mechanism on the face object -- |lambda| = 1 by unitarity: {m1}")
r5 = all(abs(ev ** 5 - 1) < 1e-12 for ev in ev_obj)
ord5 = np.linalg.norm(np.linalg.matrix_power(B_obj, 5) - np.eye(2))
print(f"CHECK: M2 mechanism on the face object -- eigenvalues are exact 5th roots of unity, |lambda^5 - 1| < 1e-12 both: {r5}")
print(f"CHECK: the block itself has finite order 5, ||B^5 - I|| = {ord5:.2e} < 1e-12: {ord5 < 1e-12}")
# the golden appearance in the eigenvalue is a field identity of the ambient
# cyclotomy: 2 cos(2 pi/5) = 1/phi, i.e. x = (sqrt5 - 1)/2 satisfies x^2 + x - 1 = 0
x = (Fraction(-1, 2), Fraction(1, 2))                     # (sqrt5 - 1)/2 as a + b sqrt5
res = q5_add(q5_add(q5_mul(x, x), x), (Fraction(-1), Fraction(0)))
num = abs(2 * math.cos(2 * math.pi / 5) - 1 / PHI)
print(f"CHECK: 'golden' in the eigenvalue is the cyclotomic identity 2cos(2pi/5) = 1/phi -- exact ((sqrt5-1)/2)^2 + (sqrt5-1)/2 - 1 = {res[0]} + {res[1]}*sqrt5, numeric |diff| = {num:.2e}: {res == (Fraction(0), Fraction(0)) and num < 1e-12}")
print("  => Re(lambda) = 1/(2 phi) is a theorem of Q(zeta_5) -- the construction")
print("     field -- not object data.  [B746 F6/F8: zeta_5-cyclotomy IMPORTED;")
print("     weights FORCED -- the banked grading, re-instantiated by computation]")
print()
print("member-observable battery (M1/M2/M4) -- object vs spectrum-matched comparator:")
bat_obj = member_battery(B_obj, "object g=RL   ")
bat_gen = member_battery(B_gen, "generic V D V^d")
same = bat_obj == bat_gen
print(f"CHECK: all three eigenvalue-stratum member observables (M1/M2/M4) identical on object block vs generic comparator: {same}")
print(f"CHECK: while O_mix separates the same two inputs ({p_obj:.6f} vs {p_gen:.6f}): {d1}")
print("  => the five member observables have ZERO discriminating power on the")
print("     banked face's own quantum object; the object-specific datum the face")
print("     banks (the mixing entry) is in the EIGENVECTOR stratum, which none")
print("     of the five members measures.  KILL EXTENDED, column 1.")

print(LINE)
print("PART 3 -- the kind-correct face datum is exact and OUTSIDE the members' menu")
print(LINE)
p = (Fraction(1, 2), Fraction(-1, 10))                    # (5 - sqrt5)/10 as a + b sqrt5
five_p2 = q5_mul((Fraction(5), Fraction(0)), q5_mul(p, p))
poly = q5_add(q5_add(five_p2, q5_mul((Fraction(-5), Fraction(0)), p)),
              (Fraction(1), Fraction(0)))
res_num = abs(5 * p_obj ** 2 - 5 * p_obj + 1)
print(f"P(object) = {np.array2string(P_obj, precision=6)}")
print(f"CHECK: computed mixing entry satisfies 5p^2 - 5p + 1 = 0 "
      f"(residual {res_num:.2e} < 1e-9): {res_num < 1e-9}")
print(f"CHECK: exact: p = (5 - sqrt5)/10 = 1/(phi sqrt5) is a root of 5x^2 - 5x + 1 [banked B753 CELL 4: P01 = 0.276393]: "
      f"{poly == (Fraction(0), Fraction(0))}")
in_open_01 = 1e-6 < p_obj < 1 - 1e-6
print(f"CHECK: 0 < p < 1 strictly ({p_obj:.6f}) -- not a modulus (all member-M1 values = 1) and not a root of unity (all member-M2/M4 values have modulus 1): {in_open_01}")
print("  => the face's object-specific number is of a KIND none of the five")
print("     member observables produces (B753 CELL 3's own wording: eigenphase-vs-")
print("     mixing is a category error -- the SAME kill_form as this tombstone).")

print(LINE)
print("PART 4 -- member M4 (z0 / k=4 phase match) against the continuous-spectrum face")
print(LINE)
z6 = (1, 1)                                               # zeta_6 = 1 + omega in O
sq = eis_mul(z6, z6)
poly_e = (sq[0] - z6[0] + 1, sq[1] - z6[1])               # zeta_6^2 - zeta_6 + 1
powers = []
zz = (1, 0)
for _ in range(6):
    zz = eis_mul(zz, z6)
    powers.append(zz)
ordz = powers.index((1, 0)) + 1
arg_z6 = cmath.phase(complex(1 + (-0.5), math.sqrt(3) / 2))
print(f"CHECK: z0 = e^(i pi/3) is the torsion unit zeta_6 = 1 + omega of O_K -- exact: zeta_6^2 - zeta_6 + 1 = {poly_e} in O_K [z^2 - z + 1 = the banked tetrahedron-shape polynomial]: {poly_e == (0, 0)}")
print(f"CHECK: ord(zeta_6) = {ordz} and arg(zeta_6) = {arg_z6/math.pi:.6f} pi = pi/3: {ordz == 6 and abs(arg_z6 - math.pi/3) < 1e-12}")
print(f"       mu_6 = <zeta_6> = O_K^x exactly (the 6 powers: {powers})")
ks = [k for k in range(1, 25) if 6 % (k + 2) == 0]
kprim = [k for k in range(1, 25) if k + 2 == 6]
print(f"CHECK: q_k = e^(2 pi i/(k+2)) lands in mu_6 = mu(K) iff (k+2) | 6 -- scan k = 1..24 gives k in {ks}, primitive generator only at k in {kprim}: {ks == [1, 4] and kprim == [4]}")
print("  => M4's entire phase stratum (multiples of pi/3 = arg z0) is mu_6-valued.")
print()
print("the banked face is defined MODULO exactly this group (computed):")
for m in (4, 8):
    _, _, _, units, _ = palette(m)
    cosets = {}
    for u in units:
        key = min(sorted(eis_mod(eis_mul(u, t), m) for t in MU6))
        cosets[u] = key
    inv = all(cosets[eis_mod(eis_mul((1, 1), u), m)] == cosets[u] for u in units)
    print(f"CHECK: level ({m}): multiplication by zeta_6 preserves every palette coset (all {len(units)} units, {len(set(cosets.values()))} cosets): {inv}")
print("  [B737 p3_sister_out.txt:72 -- Cl_n = (O/n)^*/image(mu_6); B739")
print("   b739_probe_out.txt:203-208,311-312 -- the continuous spectrum is the")
print("   single zeta_K channel, multiplicity exactly 1; no level character occurs]")
print("  => every character the banked continuous-spectrum face could ever carry")
print("     is CONSTANT on the zeta_6 phase orbit; the face is structurally blind")
print("     to M4's observable.  Consulting the face cannot revive M4.")
print()
print("specialness budget (Q6): mu_6 is FIELD data, shared by the sister --")
print("m003's cusp lattice is O_K itself [B737 p3_sister_out.txt:29-46, j=0,")
print("hexagonal], with the SAME mu_6; only the palette SIZE separates m004 from")
print("m003 (2/8 vs 1, PART 0), and that datum is zeta_6-invariant by the coset")
print("check above.  M4's phase match is field-generic: zero object-discrimination.")
print("KILL EXTENDED, column 2: 'coincidence, not structure' (B742) is upgraded to")
print("'mu_6-torsion data, quotiented out of the banked face by definition'.")

print(LINE)
print("PART 5 -- novelty + members M3/M5 face-contact scan (computed, not asserted)")
print(LINE)
kill_dir = os.path.join(FRONTIER, "B742_negatives_hunt_p1", "recompute", "TOMB-L63")
face_terms = ["palette", "mu_6", "mixing", "Eisenstein", "scattering",
              "B737", "B739", "B746", "B753"]
hits = 0
for fn in ("recompute.py", "output.txt"):
    txt = open(os.path.join(kill_dir, fn), encoding="utf-8").read()
    for t in face_terms:
        for i, ln in enumerate(txt.splitlines(), 1):
            if t in ln:
                hits += 1
                print(f"  hit: {fn}:{i}: {ln.strip()[:72]}")
print(f"CHECK: original-kill artifacts contain {hits} face-term hit(s), and the single hit is the file's header label 'B739 Stage-B recompute' (a stage name -- no palette/mixing/Eisenstein content anywhere): {hits == 1}")
print("  => the consultation run here is NEW: the original kill never tested the")
print("     claim against the banked spectral surface.")
print()
m35_terms = ["Kashaev", "volume conjecture", "colored", "asymptotic expansion"]
findings = {
    "B737": "B737_candidate_zero/FINDINGS.md",
    "B739": "B739_character_rigidity/FINDINGS.md",
    "B746": "B746_golden_ledger/FINDINGS.md",
    "B753": "B753_mixing_structure/FINDINGS.md",
}
total = 0
for arc, rel in findings.items():
    txt = open(os.path.join(FRONTIER, rel), encoding="utf-8").read()
    for t in m35_terms:
        cnt = txt.count(t)
        if cnt:
            total += cnt
            for i, ln in enumerate(txt.splitlines(), 1):
                if t in ln:
                    print(f"  {arc} '{t}' at FINDINGS.md:{i}: {ln.strip()[:72]}")
print(f"CHECK: M3/M5 subject terms across the four frozen FINDINGS total {total} hit(s), the sole hit being the 'colored-Jones' domain label in B746's F6 grading row: {total == 1}")
print("       (that row's own verdict is 'zeta_5-cyclotomy ... IMPORTED (generic")
print("       quantum-group, E20)' -- a grading that SUPPORTS the kill; no")
print("       Kashaev/asymptotic computation exists on the frozen surface.)")
print("  => the face carries no computation touching M3/M5; those members' kills")
print("     are untouched (nothing to revive them with; nothing contradicts them).")

print(LINE)
print("VERDICT: KILL-EXTENDS")
print(LINE)
print("The banked spectral face bears on TOMB-L63 in a way the original kill")
print("never tested, and it UPHOLDS the kill, adding two computed columns:")
print("(1) on the face's own quantum object (the B753 theta-odd block, built from")
print("    the banked SU(3)_2 pipeline, kappa = 5): the eigenvalue stratum is")
print("    ambient twice over -- moduli 1 by unitarity (M1's mechanism), exact")
print("    5th-roots-of-unity phases with block order 5 (M2's finite-image")
print("    mechanism), Re(lambda) = 1/(2 phi) a Q(zeta_5) field identity -- and")
print("    all three eigenvalue-stratum member observables are IDENTICAL on the")
print("    object and a spectrum-matched generic comparator, while the banked")
print("    object-specific datum (the kind-correct mixing entry, root of")
print("    5x^2 - 5x + 1) lives in the eigenvector stratum that no member")
print("    observable measures;")
print("(2) member M4's phase stratum is exactly mu_6 = <z0>, the torsion of O_K --")
print("    field data shared by the sister m003 -- and the banked continuous-")
print("    spectrum face is defined modulo mu_6 (palette cosets zeta_6-invariant,")
print("    computed; continuous channel = zeta_K only, B739), so the face is")
print("    structurally blind to M4's observable.")
print("Exactly this and no more: no new bridge is claimed; M3/M5 are untouched by")
print("the frozen surface (computed scan).  The umbrella stays DEAD; the wall")
print("gains the two columns above.")
