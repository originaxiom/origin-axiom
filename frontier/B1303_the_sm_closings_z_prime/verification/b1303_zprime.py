"""B1303 Q1 / Q1' -- sm:B1283's Z' re-derived with main's own code (DESIGN sealed 9f44f4c3 before this was written).
Inputs from the record: the 27's (psi, chi) charges, the SM quantum numbers and state counts of its eleven multiplets, a basis
of the family torus u(1)^2, and the 14 singlet monomials of the one-coupling cubic AS THE SEAT STATES THEM (their U(1)^4
invariance is checked here; their derivation from d_abc is not repeated). Everything else -- the F-flat rule, exact D-flatness,
the surviving U(1), the per-generation charge table, the mu-matrix ranks, chat1's flavon sets, the Z'-neutrality of the VEV'd
fields, the five anomaly coefficients -- is computed here from scratch. PASS/FAIL against DESIGN Q1 (a)-(e), Q1' (f)-(h)."""
import itertools, json, sys
from fractions import Fraction as Fr
import sympy as sp

fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)

# ---------- the 27: multiplet -> (states, SU(3) rep, SU(2) dim, Y, psi, chi) ----------
# psi: 16 -> 1, 10 -> -2, 1 -> 4 ; chi: (10 of 16) -> -1, (5bar of 16) -> 3, (1 of 16) -> -5, (5 of 10) -> 2, (5bar of 10) -> -2, (1) -> 0
M = {  # name: (states, colour dim (3 / -3 for 3bar / 1), su2 dim, Y, psi, chi)
 'Q':    (6,  3, 2, Fr(1, 6),  1, -1), 'u^c': (3, -3, 1, Fr(-2, 3), 1, -1), 'e^c': (1, 1, 1, Fr(1), 1, -1),
 'd^c':  (3, -3, 1, Fr(1, 3),  1,  3), 'L':   (2,  1, 2, Fr(-1, 2), 1,  3), 'nu^c': (1, 1, 1, Fr(0), 1, -5),
 'H_u':  (2,  1, 2, Fr(1, 2), -2,  2), 'D':   (3,  3, 1, Fr(-1, 3), -2, 2),
 'H_d':  (2,  1, 2, Fr(-1, 2), -2, -2), 'Dbar': (3, -3, 1, Fr(1, 3), -2, -2),
 'N':    (1,  1, 1, Fr(0),     4,  0)}
assert sum(v[0] for v in M.values()) == 27
def beta(m):  return Fr(M[m][4] + M[m][5], 4)
def gamma(m): return Fr(-5 * M[m][4], 12) + Fr(M[m][5], 4)
print("=== (a) the two extra Cartan directions beta = (psi+chi)/4, gamma = -5psi/12 + chi/4 on the eleven multiplets ===")
seat_table = {'Q': (0, Fr(-2, 3)), 'u^c': (0, Fr(-2, 3)), 'e^c': (0, Fr(-2, 3)), 'd^c': (1, Fr(1, 3)), 'L': (1, Fr(1, 3)),
              'nu^c': (-1, Fr(-5, 3)), 'N': (1, Fr(-5, 3)), 'H_u': (0, Fr(4, 3)), 'D': (0, Fr(4, 3)), 'H_d': (-1, Fr(1, 3)), 'Dbar': (-1, Fr(1, 3))}
mine = {m: (beta(m), gamma(m)) for m in M}
print("  ", {m: (str(b), str(g)) for m, (b, g) in mine.items()})
check("(a) the (beta, gamma) table reproduces sm:B1283 on all eleven multiplets", all(mine[m] == (Fr(seat_table[m][0]), seat_table[m][1]) for m in M))
# tracelessness of beta, gamma, psi, chi on the 27 (sanity)
for nm, f in (("psi", lambda m: M[m][4]), ("chi", lambda m: M[m][5]), ("beta", beta), ("gamma", gamma)):
    assert sum(M[m][0] * f(m) for m in M) == 0, nm

# ---------- the 18 SM singlets and their charges under (beta, gamma, F1, F2) ----------
E = {1: (Fr(1), Fr(1)), 2: (Fr(-1), Fr(1)), 3: (Fr(0), Fr(-2))}   # a basis of the family torus: the weights of a 3 of SU(3)_F
fields = {}
for i in (1, 2, 3):
    for X in ('N', 'nu^c'):
        fields[f"{X}_{i}"]    = (beta(X),  gamma(X),  E[i][0],  E[i][1])
        fields[f"{X}bar_{i}"] = (-beta(X), -gamma(X), -E[i][0], -E[i][1])
    for j in (1, 2, 3):
        if i != j:
            fields[f"S_{i}{j}"] = (Fr(0), Fr(0), E[i][0] - E[j][0], E[i][1] - E[j][1])
names = sorted(fields); assert len(names) == 18
def conj(x):
    if x.startswith('S_'): return f"S_{x[-1]}{x[-2]}"
    return x.replace('bar_', '_') if 'bar' in x else x.replace('_', 'bar_')
# the 14 monomials (the seat's statement of B1276's one-coupling cubic restricted to the singlets)
mons = []
for i in (1, 2, 3):
    for j in (1, 2, 3):
        if i != j:
            for X in ('N', 'nu^c'):
                mons.append((f"S_{i}{j}", f"{X}_{j}", f"{X}bar_{i}"))
mons += [("S_12", "S_23", "S_31"), ("S_21", "S_32", "S_13")]
check("(a') the 14 singlet monomials are each U(1)^4-invariant with these charges", len(mons) == 14 and
      all(all(sum(fields[f][k] for f in mon) == 0 for k in range(4)) for mon in mons))

# ---------- (b) the squarefree F-flat rule: maximal coordinate subspaces on which no monomial has two switched-on fields ----------
adj = {n: set() for n in names}
for mon in mons:
    for a, b in itertools.combinations(mon, 2):
        adj[a].add(b); adj[b].add(a)
def bron_kerbosch(R, P, X, out):      # maximal independent sets = maximal cliques of the complement graph
    if not P and not X: out.append(frozenset(R)); return
    for v in list(P):
        nb = set(n for n in names if n != v and n not in adj[v])   # non-neighbours = complement-graph neighbours
        bron_kerbosch(R | {v}, P & nb, X & nb, out); P = P - {v}; X = X | {v}
maxF = []; bron_kerbosch(set(), set(names), set(), maxF)
print(f"=== (b) maximal F-flat coordinate subspaces: {len(maxF)} ===")
check("(b) 85 maximal F-flat sets", len(maxF) == 85)

# ---------- (c) exact D-flatness: a set S is D-flat iff some strictly positive combination of its charge vectors vanishes ----------
def d_flat(S):
    """EXACT decision of {Q x = 0, x >= 1} (D-flat with every field of S strictly on): scipy finds a vertex of the primal
    (feasible) or of Gordan's dual {Q^T y >= 0, sum(Q^T y) = 1} (infeasible); the float vertex is rounded to rationals and the
    certificate is verified exactly, so no verdict rests on a float."""
    import numpy as np
    from scipy.optimize import linprog as lp
    S = list(S)
    if not S: return True
    Q = [[fields[a][k] for a in S] for k in range(4)]
    Qf = np.array([[float(x) for x in row] for row in Q])
    n = len(S)
    # primal: min 0 s.t. Q x = 0, x >= 1
    r = lp(np.zeros(n), A_eq=Qf, b_eq=np.zeros(4), bounds=[(1, None)] * n, method="highs")
    if r.status == 0:
        x = [Fr(float(v)).limit_denominator(10 ** 6) for v in r.x]
        if all(xi >= 1 for xi in x) and all(sum(Q[k][a] * x[a] for a in range(n)) == 0 for k in range(4)):
            return True
    # dual (Gordan): find y with Q^T y >= 0 componentwise and sum(Q^T y) = 1  -> certificate of infeasibility
    r2 = lp(np.zeros(4), A_ub=-Qf.T, b_ub=np.zeros(n), A_eq=np.ones((1, n)) @ Qf.T, b_eq=np.ones(1), bounds=[(None, None)] * 4, method="highs")
    if r2.status == 0:
        y = [Fr(float(v)).limit_denominator(10 ** 6) for v in r2.x]
        w = [sum(y[k] * Q[k][a] for k in range(4)) for a in range(n)]
        if all(wa >= 0 for wa in w) and any(wa > 0 for wa in w):
            return False
    raise RuntimeError(f"no exact certificate for {S}: primal {r.status}, dual {r2.status}")
# maximal D&F-flat subsets: for every maximal F-flat set, every subset (smallest 4-sets to the whole), keep the D-flat ones, then maximal by inclusion
cands = set()
for Fset in maxF:
    Fl = sorted(Fset)
    for r in range(1, len(Fl) + 1):
        for sub in itertools.combinations(Fl, r):
            if d_flat(sub): cands.add(frozenset(sub))
branches = [c for c in cands if not any(c < d for d in cands)]
branches.sort(key=lambda c: (-len(c), sorted(c)))
print(f"=== (c) maximal D&F-flat branches (all 18 fields are SM singlets, so every branch preserves the SM): {len(branches)} ===")
def surviving_rank(S):
    Q = sp.Matrix([[fields[a][k] for k in range(4)] for a in S])
    return 4 - Q.rank()
rows = []
for b in branches:
    paired = all(conj(x) in b for x in b)
    rk = surviving_rank(b)
    rows.append((len(b), rk, paired, sorted(b)))
    print(f"   {len(b)} fields, surviving extra u(1)s: {rk}, conjugate-paired: {paired}: {sorted(b)}")
check("(c) nine branches", len(branches) == 9)
check("(c) all conjugate-paired", all(r[2] for r in rows))
check("(c) three 6-field branches of rank 1 and six 4-field branches of rank 2", sorted((r[0], r[1]) for r in rows) == [(4, 2)] * 6 + [(6, 1)] * 3)
check("(c) minimal surviving abelian rank is 1 (no branch breaks all four)", min(r[1] for r in rows) == 1)
# no unpaired D-flat direction at all (the seat's stronger statement): every D-flat subset found is conjugate-paired
check("(c') every D-flat subset of every F-flat set is conjugate-paired (no unpaired direction)", all(all(conj(x) in c for x in c) for c in cands))

# ---------- (d) the surviving U(1) on each maximal branch, its E6 part and the per-generation charge table ----------
print("=== (d) the surviving direction on each maximal branch ===")
# psi, chi in terms of beta, gamma:  beta = (psi+chi)/4, gamma = -5psi/12 + chi/4  ->  solve
p_, c_ = sp.symbols('psi chi')
sol = sp.solve([sp.Eq((p_ + c_) / 4, sp.Symbol('b')), sp.Eq(-sp.Rational(5, 12) * p_ + c_ / 4, sp.Symbol('g'))], [p_, c_])
tables = {}
for b in [r for r in rows if r[0] == 6]:
    S = b[3]
    Q = sp.Matrix([[fields[a][k] for k in range(4)] for a in S])
    ker = Q.nullspace(); assert len(ker) == 1
    v = ker[0]; v = v / sp.gcd_list([x for x in v if x != 0]) if any(x != 0 for x in v) else v
    cb, cg, c1, c2 = v
    g = next(i for i in (1, 2, 3) if f"N_{i}" in S)
    # charge of multiplet m in generation i:  cb*beta + cg*gamma + (c1, c2).E[i]
    def q(m, i): return cb * beta(m) + cg * gamma(m) + c1 * E[i][0] + c2 * E[i][1]
    # normalise: the heavy generations' N charge = 15 (the seat's table), sign included
    h = next(i for i in (1, 2, 3) if i != g)
    scale = sp.Rational(15) / q('N', h)
    tab = {i: {m: sp.nsimplify(q(m, i) * scale) for m in M} for i in (1, 2, 3)}
    e6_part = {m: sp.nsimplify((cb * beta(m) + cg * gamma(m)) * scale) for m in M}
    tables[g] = (tab, e6_part, (cb * scale, cg * scale))
    print(f"   branch g={g} {S}: direction (beta, gamma, F1, F2) = {list(v)}; beta-coefficient {cb} (0 <=> E6 part is pure gamma)")
    print(f"     E6 part (normalised): {e6_part}")
    for i in (1, 2, 3): print(f"     generation {i}: {tab[i]}")
seat_e6 = {'Q': 4, 'u^c': 4, 'e^c': 4, 'd^c': -2, 'L': -2, 'nu^c': 10, 'N': 10, 'H_u': -8, 'D': -8, 'H_d': -2, 'Dbar': -2}
seat_gen_g = {'Q': -6, 'u^c': -6, 'e^c': -6, 'd^c': -12, 'L': -12, 'nu^c': 0, 'N': 0, 'H_u': -18, 'D': -18, 'H_d': -12, 'Dbar': -12}
seat_gen_h = {'Q': 9, 'u^c': 9, 'e^c': 9, 'd^c': 3, 'L': 3, 'nu^c': 15, 'N': 15, 'H_u': -3, 'D': -3, 'H_d': 3, 'Dbar': 3}
ok_e6 = all(tables[g][1] == seat_e6 for g in tables)
ok_tab = all(tables[g][0][g] == seat_gen_g and all(tables[g][0][i] == seat_gen_h for i in (1, 2, 3) if i != g) for g in tables)
check("(d) the E6 part of the surviving U(1) is (5psi - 3chi)/2: charges 4, -2, 10, -8, -2 on every maximal branch", ok_e6)
# (5 psi - 3 chi)/2 check explicitly on the multiplets
check("(d') (5psi - 3chi)/2 evaluates to the same eleven charges", all(Fr(5 * M[m][4] - 3 * M[m][5], 2) == seat_e6[m] for m in M))
check("(d) the per-generation table (VEV'd g: 0, -6, -12, -18, -12; the other two equal: 15, 9, 3, -3, 3) on every maximal branch", ok_tab)
check("(d) the VEV'd generation's N and nu^c are exactly neutral", all(tables[g][0][g]['N'] == 0 and tables[g][0][g]['nu^c'] == 0 for g in tables))

# ---------- (e) the mu-matrix mu_jk = lambda |eps_ijk| <N_i>: rank on each branch; the three-N control ----------
print("=== (e) mu-matrix ranks ===")
N1, N2, N3, lam = sp.symbols('N1 N2 N3 lambda')
def mu(Ns):
    return sp.Matrix(3, 3, lambda j, k: sum(lam * abs(sp.LeviCivita(i, j, k)) * Ns[i] for i in range(3)))
ranks = {}
for g in (1, 2, 3):
    Ns = [0, 0, 0]; Ns[g - 1] = [N1, N2, N3][g - 1]; ranks[g] = mu(Ns).rank()
three = mu([N1, N2, N3])
print(f"   one N per branch -> ranks {ranks}; three N's -> rank {three.rank()}, det = {sp.factor(three.det())}")
check("(e) rank 2 on every maximal branch (one light Higgs pair, one light D pair) and rank 3 with three N's (the control)", all(r == 2 for r in ranks.values()) and three.rank() == 3 and sp.simplify(three.det() - 2 * lam ** 3 * N1 * N2 * N3) == 0)

# ---------- Q1' (f) chat1's structural closure: the flavons forbidden by F-flatness once N_g, nu^c_g (and conjugates) are on ----------
print("=== Q1' (f) forbidden / allowed flavons on branch g (the record has SIX flavons S_ij, i != j) ===")
flav = [n for n in names if n.startswith('S_')]
ok_f = True
for g in (1, 2, 3):
    on = {f"N_{g}", f"Nbar_{g}", f"nu^c_{g}", f"nu^cbar_{g}"}
    forb = sorted(s for s in flav if any(s in mon and len(set(mon) & on) >= 1 for mon in mons))
    allow = sorted(s for s in flav if s not in forb)
    pred_forb = sorted(f"S_{i}{j}" for i in (1, 2, 3) for j in (1, 2, 3) if i != j and (i == g or j == g))
    pred_allow = sorted(f"S_{i}{j}" for i in (1, 2, 3) for j in (1, 2, 3) if i != j and i != g and j != g)
    print(f"   g={g}: forbidden {forb}; allowed {allow}")
    ok_f &= (forb == pred_forb and allow == pred_allow)
check("(f) forbidden = the four flavons S_gj, S_jg; allowed = the other pair's S_hk, S_kh (chat1's (i,i) labels are not fields of the record)", ok_f and len(flav) == 6)

# ---------- Q1' (g) every VEV'd field of every maximal branch is Z'-neutral ----------
print("=== Q1' (g) Z'-neutrality of the VEV'd fields ===")
ok_g = True
for r in rows:
    if r[0] != 6: continue
    S = r[3]; Q = sp.Matrix([[fields[a][k] for k in range(4)] for a in S]); v = Q.nullspace()[0]
    charges = {a: sum(v[k] * fields[a][k] for k in range(4)) for a in S}
    print(f"   {S}: Z' charges {charges}")
    ok_g &= all(c == 0 for c in charges.values())
check("(g) 6/6 VEV'd fields Z'-neutral on each of the three maximal branches (by construction of the surviving direction)", ok_g)

# ---------- Q1' (h) the anomaly coefficients of the Z' on the three 27s, on the three 27bars, and on the sum ----------
print("=== Q1' (h) anomalies (the per-generation integer table; state counts as multiplicities) ===")
def coeffs(tab, sign):
    cubic = grav = su3 = su2 = yy = yz = 0
    for i in (1, 2, 3):
        for m, (n, col, su2d, Y, _, _) in M.items():
            q = sign * tab[i][m]; Yq = sign * Y   # a 27bar has opposite Y and opposite Z'
            cubic += n * q ** 3; grav += n * q
            if abs(col) == 3: su3 += sp.Rational(su2d, 2) * q          # T(3) = 1/2 per su2 component
            if su2d == 2: su2 += sp.Rational(abs(col), 2) * q          # T(2) = 1/2 per colour component
            yy += n * Yq ** 2 * q; yz += n * Yq * q ** 2
    return dict(cubic=cubic, grav=grav, su3sq=su3, su2sq=su2, YYZ=yy, YZZ=yz)
tab = tables[1][0]
a27, a27b = coeffs(tab, +1), coeffs(tab, -1)
tot = {k: a27[k] + a27b[k] for k in a27}
print(f"   three 27s: {a27}\n   three 27bars: {a27b}\n   total: {tot}")
check("(h) cubic anomaly -20250 from the 27s and +20250 from the 27bars, total 0", a27['cubic'] == -20250 and a27b['cubic'] == 20250 and tot['cubic'] == 0)
check("(h) every coefficient vanishes on 27s + 27bars (vector-like); the 27s alone are non-zero on the cubic (positive control)",
      all(v == 0 for v in tot.values()) and a27['cubic'] != 0)
# what the numbers say beyond the prediction: on the 27s ALONE every MIXED coefficient already vanishes (E6 is a safe group and
# the family torus is traceless), so the -20250 is purely the family part's cubic: 27 * sum_i f_i^3 with f = (-10, 5, 5).
fam = {i: tab[i]['N'] - tables[1][1]['N'] for i in (1, 2, 3)}     # family part = total - E6 part, read off N
print(f"   family parts of the Z' by generation: {fam}; 27 * sum f^3 = {27 * sum(f ** 3 for f in fam.values())}")
check("(h') the mixed and gravitational coefficients vanish on the 27s alone (E6 safe + traceless family torus) and the cubic -20250 = 27 * sum f_i^3 is the family torus's alone",
      all(a27[k] == 0 for k in ('grav', 'su3sq', 'su2sq', 'YYZ', 'YZZ')) and a27['cubic'] == 27 * sum(f ** 3 for f in fam.values()))
# NOTE (recorded): the DESIGN's control sentence expected the 27s alone to be non-zero on EACH coefficient; that expectation was
# wrong for the mixed ones (a safe group) -- the test's substance (total 0, cubic control non-zero) is unaffected. E-class: none; a mis-stated control.
json.dump({"maxF": len(maxF), "branches": [(r[0], r[1], r[2], r[3]) for r in rows],
           "tables": {str(g): {str(i): {m: str(x) for m, x in tables[g][0][i].items()} for i in (1, 2, 3)} for g in tables},
           "e6_part": {m: str(x) for m, x in tables[1][1].items()}, "anomalies_27": {k: str(v) for k, v in a27.items()},
           "anomalies_27bar": {k: str(v) for k, v in a27b.items()}, "mu_ranks": ranks, "fails": fails}, open("b1303_zprime.json", "w"), indent=1)
print("Q1/Q1':", "PASS" if not fails else f"FAIL ({len(fails)})")
sys.exit(0 if not fails else 1)
