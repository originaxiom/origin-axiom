"""B1303 Q3 -- sm:B1300 re-derived with main's own code (DESIGN sealed 9f44f4c3).
(a) the weights of the 27 modulo the Standard-Model roots, derived from the LATTICE (the trinification frame of main's exact E6:
    the 27 = (3,3bar,1)+(3bar,1,3)+(1,3,3bar), Y and psi read off the frame, the 8 SM roots, P/Q_SM computed with an exact
    unimodularity check) -- a route independent of the seat's (the eleven cubic couplings); the seat's coupling route is also
    re-solved here as a consistency check;
(b) the line census of Y_9 from B1278's support theorem alone (h^1 = 1 exactly on ((C_1 u C_2) x V_4) minus 1 in (Z/76)^2), with
    an own enumerator over the 145^3 lines; (c) the triplet's protection. PASS/FAIL against DESIGN Q3."""
import itertools, json, sys
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
import sympy as sp
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)

# ---------------- (a) the frame ----------------
def eps(i):
    v = [Fr(0)] * 3; v[i] = Fr(1); return [x - Fr(1, 3) for x in v]
Z = [Fr(0)] * 3
def cat(*p): return tuple(x for q in p for x in q)
def neg(v): return [-x for x in v]
# the 27's weights and their SM names (trinification: colour = block 0, SU(2)_L on block-1 indices {0,1}, SU(2)_R on block-2 indices {0,1})
w27 = []   # (name, weight)
for i in range(3):
    for j in range(3): w27.append(('Q' if j < 2 else 'D', cat(eps(i), neg(eps(j)), Z)))            # (3, 3bar, 1): quarks
for i in range(3):
    for k in range(3): w27.append((['u^c', 'd^c', 'Dbar'][k], cat(neg(eps(i)), Z, eps(k))))        # (3bar, 1, 3): antiquarks
for j in range(3):
    for k in range(3):
        nm = (['H_u', 'H_d', 'L'][k] if j < 2 else ['e^c', 'nu^c', 'N'][k])
        w27.append((nm, cat(Z, eps(j), neg(eps(k)))))                                                # (1, 3, 3bar): leptons
assert len(w27) == 27
def Y(w):   return Fr(1, 2) * w[5] - Fr(2, 3) * w[6] + Fr(1, 3) * w[7] + Fr(1, 3) * w[8]
def PSI(w): return 3 * w[5] - 3 * w[8]
Ytab = {'Q': Fr(1, 6), 'u^c': Fr(-2, 3), 'e^c': Fr(1), 'd^c': Fr(1, 3), 'L': Fr(-1, 2), 'nu^c': Fr(0), 'N': Fr(0), 'H_u': Fr(1, 2), 'D': Fr(-1, 3), 'H_d': Fr(-1, 2), 'Dbar': Fr(1, 3)}
PSItab = {'Q': 1, 'u^c': 1, 'e^c': 1, 'd^c': 1, 'L': 1, 'nu^c': 1, 'N': 4, 'H_u': -2, 'D': -2, 'H_d': -2, 'Dbar': -2}
print("=== (a) the trinification frame: Y and psi on the 27 ===")
check("(a) the functional Y = w1[2]/2 - 2w2[0]/3 + w2[1]/3 + w2[2]/3 gives the SM hypercharges of all 27 states", all(Y(w) == Ytab[n] for n, w in w27))
check("(a) the functional psi = 3(w1[2] - w2[2]) gives the SO(10) grading 16 -> 1, 10 -> -2, 1 -> 4 of all 27 states (the SO(10) assignment is right)", all(PSI(w) == PSItab[n] for n, w in w27))
cnt = Counter(n for n, w in w27); check("(a) state counts Q 6, u^c 3, d^c 3, L 2, e^c 1, nu^c 1, N 1, H_u 2, H_d 2, D 3, Dbar 3", cnt == {'Q': 6, 'u^c': 3, 'd^c': 3, 'L': 2, 'e^c': 1, 'nu^c': 1, 'N': 1, 'H_u': 2, 'H_d': 2, 'D': 3, 'Dbar': 3})
# the 72 roots
A2 = [tuple(a - b for a, b in zip(eps(i), eps(j))) for i in range(3) for j in range(3) if i != j]
roots = set()
for f in range(3):
    for r in A2:
        parts = [Z, Z, Z]; parts[f] = list(r); roots.add(cat(*parts))
for i, j, k in itertools.product(range(3), repeat=3):
    w = cat(eps(i), eps(j), eps(k)); roots.add(w); roots.add(tuple(-x for x in w))
roots = sorted(roots); assert len(roots) == 72
sm_roots = [r for r in roots if (all(x == 0 for x in r[3:]) ) or (all(x == 0 for x in r[:3]) and all(x == 0 for x in r[6:]) and r[5] == 0)]
check("(a) 8 Standard-Model roots in the frame: 6 colour + 2 of SU(2)_L", len(sm_roots) == 8)
# ---- P / Q_SM : integer lattices (x3 to clear thirds) ----
def I(v): return [int(3 * x) for x in v]
def row_basis(rows):
    """Z-basis of the row lattice of integer vectors (echelon by Euclid)"""
    M = [list(r) for r in rows if any(r)]; basis = []; col = 0; ncol = len(rows[0])
    while M and col < ncol:
        piv = [r for r in M if r[col] != 0]
        if not piv: col += 1; continue
        while len(piv) > 1:
            piv.sort(key=lambda r: abs(r[col])); p = piv[0]
            new = [p]
            for r in piv[1:]:
                q = r[col] // p[col]; rr = [a - q * b for a, b in zip(r, p)]
                if rr[col] != 0: new.append(rr)
                elif any(rr): M.append(rr)
            piv = new
            M = [r for r in M if r[col] == 0 and any(r)]
        basis.append(piv[0]); M = [r for r in M if r[col] == 0 and any(r)]; col += 1
    return basis
P_basis = row_basis([I(w) for n, w in w27])
Q_basis = row_basis([I(r) for r in sm_roots])
check("(a) P (the Z-span of the 27's weights) has rank 6 and Q_SM rank 3", len(P_basis) == 6 and len(Q_basis) == 3)
Pm = sp.Matrix(P_basis)
def coords_in_P(v):
    x = sp.Matrix(P_basis).T.solve_least_squares(sp.Matrix(I(v)))  # exact rational
    assert (sp.Matrix(P_basis).T * x - sp.Matrix(I(v))) == sp.zeros(9, 1)
    assert all(xi.q == 1 for xi in x), ("not in P", v)
    return [int(xi) for xi in x]
wQ = next(w for n, w in w27 if n == 'Q'); wU = next(w for n, w in w27 if n == 'u^c'); wL = next(w for n, w in w27 if n == 'L')
Bmat = sp.Matrix([coords_in_P([Fr(x, 3) for x in q]) for q in Q_basis] + [coords_in_P(wQ), coords_in_P(wU), coords_in_P(wL)])
det = Bmat.det()
print(f"   det[ Q_SM basis ; w_Q, w_u^c, w_L ] in P's coordinates = {det}")
check("(a) {Q_SM basis} u {w_Q, w_u^c, w_L} is a Z-basis of P (determinant +-1): P/Q_SM is FREE of rank 3 with basis (w_Q, w_u^c, w_L)", abs(det) == 1)
Binv = Bmat.T.inv()
def qul(w):
    c = Binv * sp.Matrix(coords_in_P(w)); return tuple(int(x) for x in c[3:6])
table = {}
for n, w in w27:
    q = qul(w); assert table.setdefault(n, q) == q, (n, "two states of one multiplet differ mod Q_SM")
pred = {'Q': (1, 0, 0), 'u^c': (0, 1, 0), 'L': (0, 0, 1), 'D': (-2, 0, 0), 'e^c': (2, -1, 0), 'H_u': (-1, -1, 0), 'd^c': (1, -1, 1),
        'H_d': (-2, 1, -1), 'Dbar': (-1, 0, -1), 'N': (3, 0, 1), 'nu^c': (1, 1, -1)}
print(f"   weights mod Q_SM in the basis (w_Q, w_u^c, w_L): {table}")
check("(a) w_D = -2 w_Q, and the whole table as pre-registered (lattice route)", table == pred)
# the coupling route (the seat's): solve the eleven zero-sum triples
names = list(pred); trip = [('Q', 'u^c', 'H_u'), ('Q', 'd^c', 'H_d'), ('L', 'e^c', 'H_d'), ('L', 'nu^c', 'H_u'), ('N', 'H_u', 'H_d'), ('Q', 'Q', 'D'),
                            ('u^c', 'e^c', 'D'), ('u^c', 'd^c', 'Dbar'), ('Q', 'L', 'Dbar'), ('d^c', 'nu^c', 'D'), ('N', 'D', 'Dbar')]
syms = {n: sp.Matrix(sp.symbols(f"{n.replace('^', '').replace('_', '')}_0:3")) for n in names}
eqs = []
for t in trip: eqs += list(sum((syms[n] for n in t), sp.zeros(3, 1)))
eqs += list(syms['Q'] - sp.Matrix([1, 0, 0])) + list(syms['u^c'] - sp.Matrix([0, 1, 0])) + list(syms['L'] - sp.Matrix([0, 0, 1]))
sol = sp.solve(eqs, [s for n in names for s in syms[n]], dict=True); assert len(sol) == 1
ctab = {n: tuple(int(sol[0][s]) for s in syms[n]) for n in names}
check("(a) the coupling route (the eleven zero-sum triples with (w_Q, w_u^c, w_L) as basis) gives the same table", ctab == pred)
# the roots' coordinates
rq = Counter(qul(r) for r in roots)
print(f"   roots by (Q,u,L) coordinate: zero {rq[(0, 0, 0)]}, +-(1,-1,0) {rq[(1, -1, 0)] + rq[(-1, 1, 0)]}, others {72 - rq[(0, 0, 0)] - rq[(1, -1, 0)] - rq[(-1, 1, 0)]}")
check("(a) 8 roots trivial mod Q_SM (the SM's) and 12 at +-(w_Q - w_u^c) (SU(5)'s X, Y): SU(5) = 20 roots", rq[(0, 0, 0)] == 8 and rq[(1, -1, 0)] == 6 and rq[(-1, 1, 0)] == 6)
try:
    seat = json.load(open("inputs/e6_roots_qul.json"))
    seat_multiset = Counter(tuple(r['qul']) for r in seat['roots'])
    seat_tab = {('N' if k == 'S' else k): tuple(v) for k, v in seat['table27'].items()}
    check("(a) the seat's e6_roots_qul.json root multiset equals this frame's, and its table27 (S = the SO(10) singlet N) equals the lattice table (cross-check of two derivations)", seat_multiset == rq and seat_tab == pred)
except FileNotFoundError:
    print("   (seat root file not present; cross-check skipped)")
root_coords = sorted(rq.elements())

# ---------------- (b) the census of Y_9 from B1278's support theorem alone ----------------
print("=== (b) Y_9: the support model ((C_1 u C_2) x V_4) minus 1 in (Z/76)^2 and the 145^3 lines ===")
m = 76
supp = np.zeros((m, m), dtype=bool)
lines19 = [(x, 6 * x % 19) for x in range(19)] + [(x, 16 * x % 19) for x in range(19)]     # the two eigenlines of the deck (roots 6, 16 of Delta mod 19)
L19 = set(lines19)
for a in range(m):
    for b in range(m):
        if (a, b) == (0, 0): continue
        if a % 2 == 0 and b % 2 == 0 and (a % 19, b % 19) in L19: supp[a, b] = True
check("(b) the model support has 147 characters", int(supp.sum()) == 147)
chis = [(38, 0), (0, 38), (38, 38)]
def gencount(A, B):
    return sum(supp[(A + ca) % m, (B + cb) % m].astype(np.int8) for ca, cb in chis)
AA, BB = np.meshgrid(np.arange(m), np.arange(m), indexing='ij')
GC = gencount(AA, BB)
dist = Counter(GC.ravel().tolist()); print(f"   generation-count distribution over the 5776 characters: {dict(dist)}")
check("(b) {0: 5628, 2: 3, 3: 145} (B1278)", dist == {0: 5628, 2: 3, 3: 145})
K3 = list(zip(*np.where(GC == 3))); K2 = list(zip(*np.where(GC == 2)))
check("(b) K2 = the three family characters", sorted(K2) == sorted(chis))
K3a = np.array([k[0] for k in K3]); K3b = np.array([k[1] for k in K3]); n = len(K3)
iQ, iU, iL = np.meshgrid(np.arange(n), np.arange(n), np.arange(n), indexing='ij')
iQ, iU, iL = iQ.ravel(), iU.ravel(), iL.ravel()
psi = {'Q': (K3a[iQ], K3b[iQ]), 'u^c': (K3a[iU], K3b[iU]), 'L': (K3a[iL], K3b[iL])}
counts = {}
for nm, (cQ, cU, cL) in pred.items():
    A = (cQ * psi['Q'][0] + cU * psi['u^c'][0] + cL * psi['L'][0]) % m
    B = (cQ * psi['Q'][1] + cU * psi['u^c'][1] + cL * psi['L'][1]) % m
    counts[nm] = gencount(A, B)
three = np.all([counts[x] == 3 for x in ('Q', 'u^c', 'd^c', 'L', 'e^c')], axis=0)
su5b = ~((psi['Q'][0] == psi['u^c'][0]) & (psi['Q'][1] == psi['u^c'][1]))
avail = (counts['N'] >= 1) & (counts['nu^c'] >= 1) & (counts['H_u'] >= 1) & (counts['H_d'] >= 1)
sm = three & su5b & avail
full = sm & np.all([counts[x] == 3 for x in pred], axis=0)     # the seat's 'full' = SM lines keeping all 81 states
res = dict(three_gen=int(three.sum()), su5_broken=int((three & su5b).sum()), sm_vacua=int(sm.sum()), full=int(full.sum()))
print(f"   lines K3^3 = {n ** 3}: {res}")
check("(b) three-generation 758 593, SU(5) broken 737 568, SM vacua 706 464, full 568 656 (sm:B1278/B1300)", res == dict(three_gen=758593, su5_broken=737568, sm_vacua=706464, full=568656))
split = sm & (counts['D'] == 0) & (counts['Dbar'] == 0)
loses = {x: int((sm & (counts[x] < 3)).sum()) for x in pred}
print(f"   SM lines: doublet-triplet split lines {int(split.sum())}; loses-a-generation {loses}")
check("(b) split lines 0 and D loses a generation on 0 SM lines; D-bar on 29 376, H_u 30 240, H_d 29 376, N 28 512, nu^c 28 512", int(split.sum()) == 0 and loses['D'] == 0 and loses['Dbar'] == 29376 and loses['H_u'] == 30240 and loses['H_d'] == 29376 and loses['N'] == 28512 and loses['nu^c'] == 28512)
hist = Counter(zip(counts['H_u'][sm].tolist(), counts['H_d'][sm].tolist(), counts['D'][sm].tolist(), counts['Dbar'][sm].tolist()))
print(f"   (H_u, H_d, D, Dbar) on SM lines: {dict(sorted(hist.items()))}")
check("(b) the (H_u, H_d, D, Dbar) histogram of sm:B1300", dict(hist) == {(2, 2, 3, 3): 1296, (2, 3, 3, 2): 1296, (2, 3, 3, 3): 27648, (3, 2, 3, 2): 864, (3, 2, 3, 3): 27216, (3, 3, 3, 2): 27216, (3, 3, 3, 3): 620928})
# "projected iff its character IS a family character": on SM lines, for every multiplet x and generation g, x loses generation g iff chi_g psi_x in K2-shift... (the model's statement)
Dtot = Counter(counts['D'][sm].tolist()); print(f"   D total on SM lines: {dict(Dtot)}; on all lines: {dict(Counter(counts['D'].tolist()))}")
check("(b) D total is 3 on every one of the 3 048 625 candidate lines", set(counts['D'].tolist()) == {3})
# ---------------- (c) the protection theorem ----------------
sq_letters = [((2 * a) % m, (2 * b) % m) for a, b in K3]
K3set = set(K3)
check("(c) the square of every letter is a letter and no square is a family character (so psi_D = psi_Q^-2 is never projected)", all(s in K3set for s in sq_letters) and not any(s in set(chis) for s in sq_letters))
json.dump(dict(table=table, root_coords=[list(r) for r in root_coords], census=res, loses=loses, hist={str(k): v for k, v in hist.items()}, fails=fails), open("b1303_dt.json", "w"), indent=1)
print("Q3:", "PASS" if not fails else f"FAIL ({len(fails)})")
sys.exit(0 if not fails else 1)
