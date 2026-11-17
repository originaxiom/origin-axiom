#!/usr/bin/env python3
"""W-A3's checks (card relays/cards/CHAT1_W-A3_the_cover_the_class_and_the_up_sector.md, d1e36f8f4). Data-free.

    python3 -I -u wa3_checks.py

A  dihedral representations of pi_1(m004) = <a, b, t | t a t^-1 = aba, t b t^-1 = ab>, primes 3..31; plant a -> ababa.
B  the cover at p = 5: the fibre's character, the meridian, the cusp degrees, deck groups over m004 and over M2, the
   clocks as twists, irreducibility of <X, Z>, t on the (shift, clock) plane, the cover's t against rho_a(LR).
C  H_1 of covers by Fox calculus and the Smith normal form: m004, M2, the 5-sheeted and the 10-sheeted dihedral covers.
D  the level-5 classes: the knot's discriminant form, B1951's rho(T), the flux-5 modes, frame C's theta numerators
   (this seat's W-F22 transcription of thc), and the shear of the act's unipotent part.
E  part 2: the up pair's phase order; model M1 checked; closure of three-body couplings under M1 and M2.
F  level 25 in the object: roots mod 25, invariant cyclic subgroups of order 25, D_25.
"""
import itertools
import json
import os

import numpy as np
from fractions import Fraction as Fr
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {}


def say(*a):
    print(*a, flush=True)


def e(x):
    return np.exp(2j * np.pi * x)


# ---------------------------------------------------------------- words
def W(s):
    return [(c.lower(), 1 if c.islower() else -1) for c in s]


def inv(w):
    return [(g, -s) for g, s in reversed(w)]


def red(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]:
            out.pop()
        else:
            out.append(x)
    return out


PHI = {"a": W("aba"), "b": W("ab")}
PLANT = {"a": W("ababa"), "b": W("ab")}


def apply(phi, w):
    out = []
    for g, s in w:
        out += phi[g] if s == 1 else inv(phi[g])
    return red(out)


def abel(w):
    return (sum(s for g, s in w if g == "a"), sum(s for g, s in w if g == "b"))


def mono(phi):
    ca, cb = abel(phi["a"]), abel(phi["b"])
    return np.array([[ca[0], cb[0]], [ca[1], cb[1]]])


def relators(phi):
    return [W("t") + [(x, 1)] + W("T") + inv(phi[x]) for x in ("a", "b")]


LR = mono(PHI)
say("monodromy on H1 of the fibre (columns = images of a, b):", LR.tolist(), " plant:", mono(PLANT).tolist())
OUT["LR"] = LR.tolist()


# ---------------------------------------------------------------- dihedral groups, right action i.g = g(i)
def dmul(g, h, n):  # i.(gh) = h(g(i)); g = (sign, shift): i -> sign*i + shift
    return (g[0] * h[0], (h[0] * g[1] + h[1]) % n)


def deval(word, img, n):
    g = (1, 0)
    for x, s in word:
        y = img[x]
        if s == -1:
            y = (y[0], (-y[0] * y[1]) % n)
        g = dmul(g, y, n)
    return g


def primes(lo, hi):
    return [p for p in range(lo, hi + 1) if p > 1 and all(p % q for q in range(2, int(p ** 0.5) + 1))]


def dihedral(phi, n):
    sols = []
    for x, y in itertools.product(range(n), repeat=2):
        if x == 0 and y == 0:
            continue
        img = {"a": (1, x), "b": (1, y), "t": (-1, 0)}
        if all(deval(r, img, n) == (1, 0) for r in relators(phi)):
            sols.append((x, y))
    return sols


A = {p: dihedral(PHI, p) for p in primes(3, 31)}
Ap = {p: dihedral(PLANT, p) for p in primes(3, 31)}
OUT["A_primes"] = [p for p in A if A[p]]
OUT["A_plant_primes"] = [p for p in Ap if Ap[p]]
say("A: primes 3..31 with a dihedral representation (t to a reflection):", OUT["A_primes"], " solutions at 5:", A.get(5))
say("A: the plant (a -> ababa, monodromy [[3,1],[2,1]]):", OUT["A_plant_primes"])

# ---------------------------------------------------------------- B. the cover at p = 5
p = 5
x0, y0 = A[5][0]
IMG = {"a": (1, x0), "b": (1, y0), "t": (-1, 0)}
v = None
for vv in itertools.product(range(5), repeat=2):
    if vv != (0, 0) and all(((LR @ np.array(vv)) + np.array(vv)) % 5 == 0):
        v = vv
        break
omega_v = ((-v[1]) % 5, v[0] % 5)  # omega(v, (m, n)) = v0 n - v1 m  -> covector (-v1, v0)
prop = [c for c in range(1, 5) if ((c * omega_v[0] - x0) % 5, (c * omega_v[1] - y0) % 5) == (0, 0)]
OUT["B_u"] = [x0, y0]; OUT["B_v"] = list(v); OUT["B_u_is_multiple_of_omega_v"] = bool(prop)
say("B: fibre character u = (u(a), u(b)) =", (x0, y0), "; the act's fixed line v (LR v = -v mod 5) =", v,
    "; omega(v, .) =", omega_v, "; u = c * omega(v, .) with c =", prop)
uLR = ((x0 * LR[0, 0] + y0 * LR[1, 0]) % 5, (x0 * LR[0, 1] + y0 * LR[1, 1]) % 5)
say("B: u o LR =", uLR, " -u =", ((-x0) % 5, (-y0) % 5))

lam = W("abAB")
plam = apply(PHI, lam)
core, g = list(plam), []
while len(core) > 1 and core[0][0] == core[-1][0] and core[0][1] == -core[-1][1]:
    g.append(core[0]); core = core[1:-1]
conj = None
for tgt in (lam, inv(lam)):
    for j in range(len(tgt)):
        if core == tgt[j:] + tgt[:j]:
            conj = red(g + inv(tgt[:j])); break
    if conj is not None:
        break
assert red(conj + lam + inv(conj)) == plam or red(conj + inv(lam) + inv(conj)) == plam
mu = inv(conj) + W("t")
mu_img = deval(mu, IMG, 5)
lam_img = deval(lam, IMG, 5)


def perm_of(gimg, n=5):
    return [(gimg[0] * i + gimg[1]) % n for i in range(n)]


fix_mu = sum(1 for i in range(5) if perm_of(mu_img)[i] == i)
# orbits of the peripheral image
orb, seen = [], set()
for i in range(5):
    if i in seen:
        continue
    o, frontier = {i}, [i]
    while frontier:
        k = frontier.pop()
        for gg in (mu_img, lam_img):
            j = perm_of(gg)[k]
            if j not in o:
                o.add(j); frontier.append(j)
    seen |= o; orb.append(len(o))
OUT["B_phi_lambda_conjugator"] = "".join(x if s == 1 else x.upper() for x, s in conj)
OUT["B_meridian_image"] = list(mu_img); OUT["B_meridian_fixed_points"] = fix_mu; OUT["B_longitude_image"] = list(lam_img)
OUT["B_cusp_degrees"] = sorted(orb)
say("B: phi([a,b]) = g [a,b]^(+-1) g^-1 with g =", OUT["B_phi_lambda_conjugator"], "; meridian g^-1 t ->", mu_img,
    "(fixed points", fix_mu, "); longitude ->", lam_img, "; cusp degrees", sorted(orb))


def centraliser(gens):
    out = []
    for s in itertools.permutations(range(5)):
        if all(all(s[pg[i]] == pg[s[i]] for i in range(5)) for pg in gens):
            out.append(s)
    return out


gens_M = [perm_of(IMG[k]) for k in ("a", "b", "t")]
G2_words = [W("a"), W("b"), W("tt"), W("taT"), W("tbT")]
gens_M2 = [perm_of(deval(w, IMG, 5)) for w in G2_words]
cM, cM2 = centraliser(gens_M), centraliser(gens_M2)
rot = all(all(s[i] == (i + s[0]) % 5 for i in range(5)) for s in cM2)
OUT["B_deck_over_m004"] = len(cM); OUT["B_deck_over_M2"] = len(cM2); OUT["B_deck_over_M2_are_shifts"] = rot
say("B: deck group of the 5-sheeted cover over m004: order", len(cM), "; over M2: order", len(cM2), "shifts:", rot)


def Rm(perm, n):
    R = np.zeros((n, n))
    for i in range(n):
        R[i, perm[i]] = 1
    return R


z = e(1 / 5)
X = Rm([(i + 1) % 5 for i in range(5)], 5)  # e_i -> e_(i+1) as row vectors
Zc = np.diag([z ** i for i in range(5)])
P = Rm(perm_of(IMG["t"]), 5)
rhoG2 = [Rm(pp, 5) for pp in gens_M2]
twist_ok = []
for w_, R in zip(G2_words, rhoG2):
    m = deval(w_, IMG, 5)
    assert m[0] == 1
    lhs = Zc @ R @ np.linalg.inv(Zc)
    twist_ok.append(min(np.abs(lhs - z ** (s * m[1]) * R).max() for s in (1, -1)))
tP = Zc @ P @ np.linalg.inv(Zc)
t_not_twist = min(np.abs(tP - c * P).max() for c in [z ** k for k in range(5)])
OUT["B_clock_intertwines_on_M2"] = max(twist_ok); OUT["B_clock_on_t_defect"] = t_not_twist
say("B: Z rho(g) Z^-1 = chi(g) rho(g) on M2's generators, worst defect %.1e; on t, best scalar defect %.2f (not a twist)"
    % (max(twist_ok), t_not_twist))
# clocks as twists: chi_b on the fibre is zeta^(b u)
say("B: the deck characters on the fibre: chi_b(a) = z^(b u(a)), chi_b(b) = z^(b u(b)), u =", (x0, y0))
# irreducibility of <X, Z>
K = np.vstack([np.kron(np.eye(5), M_) - np.kron(M_.T, np.eye(5)) for M_ in (X, Zc)])
sv = np.linalg.svd(K, compute_uv=False)
comm_dim = int(np.sum(sv < 1e-9))
OUT["B_commutant_dim_XZ"] = comm_dim
XZ = X @ Zc @ np.linalg.inv(X) @ np.linalg.inv(Zc)
OUT["B_commutator_scalar"] = complex(XZ[0, 0])
say("B: commutant of <X, Z> has dimension", comm_dim, "; X Z X^-1 Z^-1 =", np.round(XZ[0, 0], 6), "* I:",
    np.abs(XZ - XZ[0, 0] * np.eye(5)).max() < 1e-12)
PX = P @ X @ P.T; PZ = P @ Zc @ P.T
OUT["B_t_on_plane"] = [bool(np.abs(PX - np.linalg.inv(X)).max() < 1e-12), bool(np.abs(PZ - np.linalg.inv(Zc)).max() < 1e-12)]
say("B: t acts on the (shift, clock) plane as -I: P X P^-1 = X^-1:", OUT["B_t_on_plane"][0], "; P Z P^-1 = Z^-1:",
    OUT["B_t_on_plane"][1])


def weil(a):
    T_ = np.diag([e(a * x * x / 5) for x in range(5)])
    S0 = np.array([[e(-2 * a * x * y / 5) for y in range(5)] for x in range(5)]) / np.sqrt(5)
    lhs = np.linalg.matrix_power(S0 @ T_, 3); rhs = S0 @ S0
    k = np.argmax(np.abs(rhs))
    sigma = (rhs.flat[k] / lhs.flat[k])
    S_ = sigma * S0
    ok = (np.abs(np.linalg.matrix_power(S_ @ T_, 3) - S_ @ S_).max(), np.abs(np.linalg.matrix_power(S_, 4) - np.eye(5)).max())
    return T_, S_, ok


Sm = np.array([[0, -1], [1, 0]]); Tm = np.array([[1, 1], [0, 1]])
word_LR = Sm @ np.linalg.inv(Tm).round().astype(int) @ np.linalg.inv(Sm).round().astype(int) @ Tm
assert (word_LR == LR).all()
OUT["B_weil"] = {}
for a in (1, 2):
    T_, S_, ok = weil(a)
    R_LR = S_ @ np.linalg.inv(T_) @ np.linalg.inv(S_) @ T_
    best = min(np.abs(R_LR - c * P).max() for c in np.exp(2j * np.pi * np.arange(40) / 40))
    ratio = R_LR @ np.linalg.inv(P)
    nonscalar = np.abs(ratio - ratio[0, 0] * np.eye(5)).max()
    OUT["B_weil"][a] = {"relations_defect": [float(ok[0]), float(ok[1])], "rhoLR_minus_scalar_P": float(best),
                        "rhoLR_P_inverse_nonscalar": float(nonscalar), "rho_minusI_is_P": float(np.abs(S_ @ S_ - P).max())}
    say("B: Weil class a = %d: relations defect %.1e %.1e; rho(-I) = P: %.1e; min |rho(LR) - c P| over 40th roots c = %.3f;"
        " rho(LR) P^-1 off scalar by %.3f" % (a, ok[0], ok[1], np.abs(S_ @ S_ - P).max(), best, nonscalar))


# ---------------------------------------------------------------- C. homology of covers by Fox calculus
def fox(word, x):
    terms = []
    for j, (g, s) in enumerate(word):
        if g != x:
            continue
        if s == 1:
            terms.append((1, word[:j]))
        else:
            terms.append((-1, word[:j + 1]))
    return terms


def H1(phi, perms, n):
    gens = ["a", "b", "t"]
    Rg = {k: Rm(perms[k], n) for k in gens}

    def Rw(w):
        M_ = np.eye(n)
        for g_, s in w:
            M_ = M_ @ (Rg[g_] if s == 1 else Rg[g_].T)
        return M_

    rels = relators(phi)
    D2 = np.zeros((2 * n, 3 * n))
    for i, r in enumerate(rels):
        for j, x in enumerate(gens):
            blk = sum((s * Rw(pre) for s, pre in fox(r, x)), np.zeros((n, n)))
            D2[i * n:(i + 1) * n, j * n:(j + 1) * n] = blk
    D1 = np.vstack([Rg[x] - np.eye(n) for x in gens])
    zero = np.abs(D2 @ D1).max()
    snf = smith_normal_form(Matrix(D2.round().astype(int).tolist()), domain=ZZ)
    diag = [abs(int(snf[i, i])) for i in range(min(snf.shape))]
    r = sum(1 for d in diag if d != 0)
    tors = sorted(d for d in diag if d > 1)
    return {"rank": 3 * n - r - (n - 1), "torsion": tors, "d2d1": float(zero)}


def regular_D5():
    els = [(s, k) for s in (1, -1) for k in range(5)]
    idx = {g_: i for i, g_ in enumerate(els)}
    out = {}
    for name, gi in IMG.items():
        out[name] = [idx[dmul(h, gi, 5)] for h in els]
    return out, 10


covers = {
    "m004": ({"a": [0], "b": [0], "t": [0]}, 1),
    "M2": ({"a": [0, 1], "b": [0, 1], "t": [1, 0]}, 2),
    "dihedral5": ({k: perm_of(IMG[k]) for k in ("a", "b", "t")}, 5),
    "dihedral10_regular": regular_D5(),
}
OUT["C"] = {}
for name, (perms, n) in covers.items():
    h = H1(PHI, perms, n)
    OUT["C"][name] = h
    say("C: H1(%s) = Z^%d + torsion %s   (D2 D1 = 0: %.0e)" % (name, h["rank"], h["torsion"], h["d2d1"]))

# ---------------------------------------------------------------- D. the classes
RES, NONRES = {1, 4}, {2, 3}


def cls(c):
    c %= 5
    return "residue" if c in RES else ("non-residue" if c in NONRES else "zero")


V = [[Fr(-1), Fr(1)], [Fr(0), Fr(1)]]
Am = [[V[i][j] + V[j][i] for j in range(2)] for i in range(2)]
det = Am[0][0] * Am[1][1] - Am[0][1] * Am[1][0]
Ai = [[Am[1][1] / det, -Am[0][1] / det], [-Am[1][0] / det, Am[0][0] / det]]
alex = [V[0][0] * V[1][1] - V[0][1] * V[1][0]]  # placeholder; Alexander polynomial checked symbolically below
from sympy import symbols, expand, Matrix as SM
tt = symbols("t")
alexp = expand(SM([[V[i][j] - tt * V[j][i] for j in range(2)] for i in range(2)]).det())
qv, bv = set(), set()
for x1, x2 in itertools.product(range(-6, 7), repeat=2):
    val = Ai[0][0] * x1 * x1 + 2 * Ai[0][1] * x1 * x2 + Ai[1][1] * x2 * x2
    bv.add(int((val % 1) * 5) % 5)
    qv.add(int(((val / 2) % 1) * 5) % 5)
qc = [c for c in range(1, 5) if {(c * s) % 5 for s in (0, 1, 4)} == qv]
bc = [c for c in range(1, 5) if {(c * s) % 5 for s in (0, 1, 4)} == bv]
OUT["D_K"] = {"A": [[int(x) for x in r] for r in Am], "det": int(det), "alexander": str(alexp),
              "q_values_x5": sorted(qv), "q_coeff": qc, "q_class": cls(qc[0]), "b_values_x5": sorted(bv), "b_coeff": bc,
              "b_class": cls(bc[0])}
say("D(K): V + V^T =", OUT["D_K"]["A"], "det", int(det), "; Alexander", alexp, "; q = x^T A^-1 x / 2 takes 5q in",
    sorted(qv), "-> coefficient", qc, cls(qc[0]), "; b(x,x) takes", sorted(bv), "->", bc, cls(bc[0]))
OUT["D_B"] = {"T_coeff": 2, "class": cls(2), "T2_coeff": 4, "T2_class": cls(4)}
say("D(B): B1951's rho(T) = diag(e(2x^2/5)) (main's weil_centre.py): T-coefficient 2,", cls(2), "; T^2-coefficient 4,", cls(4))


def psi(j, tau, u, N=40):
    n = np.arange(-N, N + 1) + j / 5
    return np.sum(np.exp(1j * np.pi * 5 * tau * n * n + 2j * np.pi * 5 * u * n))


tau0, u0 = 0.21 + 0.93j, 0.13 + 0.07j
fl = []
for j in range(5):
    r = psi(j, tau0 + 2, u0) / psi(j, tau0, u0)
    fl.append(float((np.angle(r) / (2 * np.pi)) % 1))
f_c25 = [round(5 * f) % 5 for f in fl]
OUT["D_F"] = {"T2_phases": fl, "T2_coeff": 1, "T2_class": cls(1), "T_coeff": 3, "class": cls(3)}
say("D(F): flux-5 modes, phase of psi_j(tau+2)/psi_j(tau) / 2pi =", np.round(fl, 9).tolist(), "= j^2/5 ->",
    "T^2-coefficient 1 (", cls(1), "), T-coefficient 1/2 = 3 (", cls(3), ")")

NK = 40


def thc(a, b, u, T):
    n = np.arange(-NK, NK + 1) + a
    return np.sum(np.exp(1j * np.pi * T * n * n + 2j * np.pi * n * (u + b)))


def twist_of(w, t):
    a = w.imag / t.imag
    return (a, 2 * (w.real - a * t.real))


SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
OUT["D_C"] = {}
for sec, (lf, rf) in SECT.items():
    rows = []
    for k in range(1, 5):
        a_line, b_line = k / 5, (2 * k % 5) / 5
        w0 = a_line * tau0 + b_line
        vals = []
        for uu in (u0, 0.31 - 0.04j):
            num = den = 1
            for f in (lf, rf):
                wf = SIXY[f] * w0
                al, be = twist_of(wf, tau0)
                al2, be2 = twist_of(wf, tau0 + 1)
                num *= thc(al2, be2, uu, 2 * (tau0 + 1))
                den *= thc(al, be, uu, 2 * tau0)
            vals.append(num / den)
        ph = float((np.angle(vals[0]) / (2 * np.pi)) % 1)
        pred = float((-(SIXY[lf] ** 2 + SIXY[rf] ** 2) * k * k / 25) % 1)
        c25 = round(25 * ph) % 25
        rows.append({"k": k, "phase": ph, "pred": pred, "c25": c25, "u_indep": float(abs(vals[0] - vals[1])),
                     "modulus": float(abs(vals[0]))})
    lvl5 = all(r["c25"] % 5 == 0 for r in rows)
    coeffs = sorted({((r["c25"] // 5) * pow(r["k"] * r["k"], -1, 5)) % 5 for r in rows}) if lvl5 else None
    OUT["D_C"][sec] = {"rows": rows, "level5": lvl5, "T_coeff": coeffs,
                       "class": (cls(coeffs[0]) if coeffs and len(coeffs) == 1 else None)}
    say("D(C): frame C %s pair (%s, %s): T-phase x25 = %s (pred %s), |ratio| %s, u-independence %.1e; level 5: %s;"
        " T-coefficient %s %s" % (sec, lf, rf, [r["c25"] for r in rows], [round(25 * r["pred"]) % 25 for r in rows],
                                  sorted({round(r["modulus"], 9) for r in rows}), max(r["u_indep"] for r in rows), lvl5,
                                  coeffs, OUT["D_C"][sec]["class"]))

U = (-LR) % 5
vv = np.array(v); wv = None
for cand in itertools.product(range(5), repeat=2):
    if (vv[0] * cand[1] - vv[1] * cand[0]) % 5 == 1:
        wv = np.array(cand); break
Uw = (U @ wv) % 5
shear = [c for c in range(5) if all(((wv + c * vv) - Uw) % 5 == 0)][0]
U2 = (U @ U) % 5
U2w = (U2 @ wv) % 5
shear2 = [c for c in range(5) if all(((wv + c * vv) - U2w) % 5 == 0)][0]
OUT["D_shear"] = {"U": U.tolist(), "w": wv.tolist(), "shear_U": shear, "class_U": cls(shear), "shear_U2": shear2,
                  "class_U2": cls(shear2)}
say("D: LR = -U mod 5, U =", U.tolist(), "; in the symplectic basis (v, w), v =", list(v), "w =", wv.tolist(),
    ": U w = w + c v with c =", shear, cls(shear), "; U^2: c =", shear2, cls(shear2))

# ---------------------------------------------------------------- E. part 2
up = OUT["D_C"]["up"]["rows"]
orders = [25 // np.gcd(r["c25"], 25) for r in up]
OUT["E_up_orders"] = [int(o) for o in orders]
say("E: the up pair's T-phases have orders", OUT["E_up_orders"])
m1 = []
for d in (1, 2):
    for al in (0.2, 0.4, -0.8, 1.2):
        be = 0.37
        lhs = thc(al, be - 2 * d * al, u0, 2 * d * (tau0 + 1))
        rhs = e(-d * al * al) * thc(al, be, u0, 2 * d * tau0)
        m1.append(float(abs(lhs - rhs) / abs(rhs)))
OUT["E_M1_check"] = max(m1)
say("E: model M1 (a degree-d field's theta at modulus 2d tau has T-phase e(-d alpha^2)): worst relative defect %.1e" % max(m1))
YU = {"up": (1, -4, 3), "down": (1, 2, -3), "lep": (-3, 6, -3)}
OUT["E"] = {}
for sec, (q1, q2, qh_cons) in YU.items():
    res = {"M1": [], "M2": []}
    for qh in (3, -3, 0):
        for d in itertools.product((1, 2), repeat=3):
            s1 = (d[0] * q1 * q1 + d[1] * q2 * q2 + d[2] * qh * qh) % 5
            s2 = (d[0] ** 2 * q1 * q1 + d[1] ** 2 * q2 * q2 + d[2] ** 2 * qh * qh) % 5
            if s1 == 0:
                res["M1"].append({"degrees": list(d), "qH": qh, "conserving": qh == qh_cons})
            if s2 == 0:
                res["M2"].append({"degrees": list(d), "qH": qh, "conserving": qh == qh_cons})
    mains = {m: any(r["degrees"] == [2, 2, 1] for r in res[m]) for m in ("M1", "M2")}
    OUT["E"][sec] = {"closing": res, "mains_2_2_1_closes": mains}
    say("E: %s (q = %d, %d; Higgs 6Y conserving %d): closing in M1: %s" % (sec, q1, q2, qh_cons,
        [(r["degrees"], r["qH"]) for r in res["M1"]]))
    say("     closing in M2: %s ; main's (2, 2, 1) closes: %s" % ([(r["degrees"], r["qH"]) for r in res["M2"]], mains))

# ---------------------------------------------------------------- F. level 25
roots25 = [x for x in range(25) if (x * x - 3 * x + 1) % 25 == 0]
roots5 = [x for x in range(5) if (x * x - 3 * x + 1) % 5 == 0]
subs = set()
for vv25 in itertools.product(range(25), repeat=2):
    if vv25[0] % 5 == 0 and vv25[1] % 5 == 0:
        continue
    img = ((2 * vv25[0] + vv25[1]) % 25, (vv25[0] + vv25[1]) % 25)
    if any(((lam * vv25[0] - img[0]) % 25, (lam * vv25[1] - img[1]) % 25) == (0, 0) for lam in range(25)):
        subs.add(frozenset(((k * vv25[0]) % 25, (k * vv25[1]) % 25) for k in range(25)))
d25 = dihedral(PHI, 25)
d25_orders = sorted({25 // np.gcd(np.gcd(x, y), 25) for x, y in d25})
OUT["F"] = {"roots_mod_5": roots5, "roots_mod_25": roots25, "invariant_cyclic_25": len(subs), "D25_solution_orders": [int(o) for o in d25_orders]}
tors = {k: OUT["C"][k]["torsion"] for k in OUT["C"]}
OUT["F"]["covers_25_or_5rank2"] = {k: (any(t_ % 25 == 0 for t_ in tv) or sum(1 for t_ in tv if t_ % 5 == 0) >= 2) for k, tv in tors.items()}
say("F: roots of x^2 - 3x + 1 mod 5:", roots5, "; mod 25:", roots25, "; LR-invariant cyclic subgroups of order 25:", len(subs),
    "; D_25 representations: element orders", d25_orders, "; covers with Z/25 or 5-rank >= 2:", OUT["F"]["covers_25_or_5rank2"])

# ---------------------------------------------------------------- failure criteria
F = {}
F["F1"] = OUT["A_primes"] != [5]
F["F2"] = not (OUT["B_meridian_image"][0] == -1 and fix_mu == 1 and OUT["B_cusp_degrees"] == [1, 2, 2])
F["F3"] = not (OUT["B_deck_over_M2"] == 5 and rot)
F["F4"] = not OUT["B_u_is_multiple_of_omega_v"]
F["F5"] = comm_dim != 1
F["F6"] = not (OUT["D_C"]["down"]["level5"] and OUT["D_C"]["lep"]["level5"] and OUT["D_C"]["down"]["class"] is not None
               and OUT["D_C"]["down"]["class"] == OUT["D_C"]["lep"]["class"])
F["F7"] = any(OUT["E"]["up"]["mains_2_2_1_closes"].values())
F["F8"] = OUT["E_M1_check"] > 1e-10
F["harness"] = not (OUT["A_plant_primes"] != [5] and OUT["C"]["m004"]["rank"] == 1 and OUT["C"]["m004"]["torsion"] == []
                    and OUT["C"]["M2"]["rank"] == 1 and OUT["C"]["M2"]["torsion"] == [5])
OUT["failure"] = F
say("FAILURE CRITERIA (True = holds):", F)
with open(os.path.join(HERE, "wa3_checks_output.json"), "w") as fh:
    json.dump(OUT, fh, indent=1, default=str)
