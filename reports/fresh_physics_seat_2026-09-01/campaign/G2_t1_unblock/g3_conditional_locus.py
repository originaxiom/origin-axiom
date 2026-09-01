"""G2 step 3 -- THE CONDITIONAL ANALYSIS, computable NOW: the 27 values as unknowns over
K = Q(zeta_12); the annihilation locus inside the space the committed constraints allow.

Outputs:
  [1] the allowed space IS the full block K^36 -- every committed constraint is support/
      symmetry bookkeeping already saturated by the block's position in the census;
  [2] codim(annihilates) = 27 in the allowed space (instrument validated on planted cases);
  [3] the FORCING CENSUS: no committed constraint forces any of the 27 entries nonzero
      (each candidate enumerated with source and defeated by an explicit witness) -- so
      B1232's fork is NOT resolvable to OBSTRUCTED by constraints alone; and none forces
      annihilation either;
  [4] the CONDITIONAL layer: importing the E8-fence rank-2 family law (fenced non-importable
      by B1185 INV-3 -- run as a conditional, labeled) cuts the allowed space to the
      identically-singular-pencil variety (local dim 26 at its common-kernel points, codim 10)
      and STILL leaves both fork branches open; inside it, annihilation has codim 18. The
      strong form (rank exactly 2) forces the surviving OBSERVABLE nonzero -- not the 27.

Conventions (E23): as T1/s1 and g2. Family matrix Y(t)[i][j] = M0 + t1 M1 + t2 M2 + t3 M3
with M0[i][j] = T[i,j,tail2] and Mk[i][j] = T[i,j,conn_k] -- the (3,4,1) splitting chart.
"""
import sympy as sp
import random, json, os

random.seed(20260901)
CELL = os.path.dirname(os.path.abspath(__file__))

print("=" * 78)
print("[1] the allowed space = K^36, shown structurally (not just sampled):")
print("=" * 78)
# The block's channels: (B6 slot, B2 slot) with raw labels (6,2) or (6-tail, 2) etc.
B6S = [("c", 6, 0), ("c", 6, 1), ("t", 6, 0)]
B2S = [("c", 2, 0), ("c", 2, 1), ("c", 2, 2), ("t", 2, 0)]
for s1 in B6S:
    for s2 in B2S:
        assert (s1[1] + s2[1]) % 12 == 8            # K1 selection: SATURATED by every channel
assert not any(s1 == s2 for s1 in B6S for s2 in B2S)  # K2 never relates an entry to itself
assert set((s1, s2) for s1 in B6S for s2 in B2S).isdisjoint(
       set((s2, s1) for s1 in B6S for s2 in B2S))     # K2 relates block <-> MIRROR block only
assert ("t", 4, 0) not in B6S + B2S                   # K3 skew-(4,4) zero lives OUTSIDE the block
print("  K1 (selection rho+sigma=8): every one of the 12 (j,k) channels has 6+2=8 -- 0 equations;")
print("  K2 (antisymmetry): pairs an entry with its MIRROR (B2,B6)-block image, never with another")
print("     block entry (label 6 != 2, and no slot pair occurs in both orders) -- 0 equations;")
print("  K3 (skew (4,4) zero): the repeated tail-4 channel is not in this block -- 0 equations.")
print("  => the committed constraints impose ZERO polynomial relations among the 36 entries:")
print("     the allowed space is the full affine K^36. (Constraint support disjoint from block.)")

print()
print("=" * 78)
print("[2] codim(annihilates) inside the allowed space -- instrument with planted controls:")
print("=" * 78)
# 36 coordinates: Ms[m][i][j], m=0 tail matrix, m=1..3 the conn matrices.
M = [[[sp.Symbol(f"M{m}_{i}{j}") for j in range(3)] for i in range(3)] for m in range(4)]
flat = [M[m][i][j] for m in range(4) for i in range(3) for j in range(3)]
def jac_rank_at(eqs, point):
    J = sp.Matrix([[sp.diff(e, v) for v in flat] for e in eqs])
    return J.subs(point).rank()
def rand_point(cond=None):
    while True:
        p = {v: sp.Rational(random.randint(-9, 9), random.randint(1, 4)) for v in flat}
        if cond is None or cond(p): return p

# planted control 1: {M1 = 0} must come out codim 9
eqs_c1 = [M[1][i][j] for i in range(3) for j in range(3)]
r = jac_rank_at(eqs_c1, rand_point())
print(f"  planted control {{M1=0}}: Jacobian rank = {r} (expect 9)"); assert r == 9
# planted control 2: {det M0 = 0} must come out codim 1 at a smooth (rank-2) point
detM0 = sp.Matrix(3, 3, lambda i, j: M[0][i][j]).det()
pt = rand_point(); pt.update({M[0][2][j]: pt[M[0][0][j]] + pt[M[0][1][j]] for j in range(3)})  # row3=row1+row2
r = jac_rank_at([detM0], pt)
print(f"  planted control {{det M0=0}} at a rank-2 point: Jacobian rank = {r} (expect 1)"); assert r == 1
# the annihilation locus: the 27 conn entries
eqs_ann = [M[m][i][j] for m in (1, 2, 3) for i in range(3) for j in range(3)]
r = jac_rank_at(eqs_ann, rand_point())
print(f"  ANNIHILATION locus {{27 conn entries = 0}}: Jacobian rank = {r} -> codim 27, dim 9;")
assert r == 27
print("  the 9 remaining dims are exactly the surviving tail-family observable Ybar[i,j].")

print()
print("=" * 78)
print("[3] THE FORCING CENSUS -- does any committed constraint force a conn entry nonzero?")
print("=" * 78)
census = [
 ("selection rule rho+sigma=8 [M2]", "a PERMISSION (support), saturated by the block; T=0 satisfies it"),
 ("antisymmetry / skew (4,4) zero [M2,B1185]", "forces a zero OUTSIDE the block; T=0 satisfies it"),
 ("'C12 imposes no family texture zero' (B1161/B1167)", "permission again -- permits nonzero, forces nothing"),
 ("mu_u = 0 exact (R017/[M1])", "a fact about the OTHER map (Sym^2 A x C); shares no entry with mu_d"),
 ("C18->C21 rank 16 / 33+5 / 672x33 [M1]", "dimensions of B's presentation, not values of T"),
 ("Kodaira-Spencer rank 10 [M1]", "[M1] verbatim: 'not a proof that mu_d varies' -- moduli, not entries"),
 ("lambda-term row N1->2 nonzero (memo 80/B1206)", "a DIFFERENT coupling on a DIFFERENT arena (object channel); B1185 INV-1 forbids transport"),
 ("B1205 det cubic 'genuine failable cubic'", "computed over the tensor's SHAPE (B1206 fence) -- genericity, not a value claim"),
 ("Hoppe stability / local freeness gates [M1]", "existence gates for DEFINING mu_d; impose nothing on its values"),
 ("E8 rank-2 family law (memo 82/B1185)", "fenced NON-IMPORTABLE by B1185 INV-3 (family index not object-internal); conditional analysis in [4] -- and even imported it does not force a conn entry (witness W1 below)"),
]
for src, why in census:
    print(f"  - {src}:\n      {why}")
print("  WITNESS (g2 Theorem A): T_ann (all 27 = 0) satisfies every committed constraint -->")
print("  NO committed constraint forces a nonzero connecting entry. FORCED-NONZERO is NOT available;")
print("  B1232's fork cannot be resolved to OBSTRUCTED by the committed record alone.")
print("  (Symmetric check: T_obs shows it cannot be resolved to ANNIHILATES either.)")

print()
print("=" * 78)
print("[4] CONDITIONAL layer -- importing the E8 rank-2 family law (LABELED, fenced):")
print("=" * 78)
print("  Import fence: B1185 INV-3 proves the family index is not object-internal; this layer is")
print("  therefore CONDITIONAL bookkeeping, not a claim about the object. Weak form: det Y(t) == 0")
print("  identically in t (rank <= 2 everywhere). Strong form: rank EXACTLY 2 at the physical point.")
t1, t2, t3 = sp.symbols("t1 t2 t3")
Yt = sp.Matrix(3, 3, lambda i, j: M[0][i][j] + t1 * M[1][i][j] + t2 * M[2][i][j] + t3 * M[3][i][j])
detp = sp.Poly(sp.expand(Yt.det()), t1, t2, t3)
coeffs = detp.coeffs()
print(f"  det Y(t) as a polynomial in t: {len(coeffs)} coefficients, each cubic in the 36 entries")
assert len(coeffs) == 20
# the common-LEFT-kernel component: all four M_m share the left kernel e3^T (third rows zero):
ptV = rand_point()
for m in range(4):
    for j in range(3): ptV[M[m][2][j]] = sp.Integer(0)
vals = [sp.expand(c).subs(ptV) for c in coeffs]
assert all(v == 0 for v in vals), "the common-left-kernel point must lie in the variety"
rV = jac_rank_at(coeffs, ptV)
print(f"  at a generic common-left-kernel point: all 20 coefficients vanish; Jacobian rank = {rV}")
print(f"  -> the variety is smooth of dim {36 - rV} there (component dim 26 = 4x6 + 2, codim 10).")
assert rV == 10
# WITNESS W1 (annihilating, in-variety, satisfies even the STRONG form):
#   M1=M2=M3=0, M0 = rank-2: Y(t) = M0 constant, rank exactly 2 for every t.
ptW1 = {v: sp.Integer(0) for v in flat}
for i in range(2):
    for j in range(3): ptW1[M[0][i][j]] = sp.Rational(random.randint(1, 9), random.randint(1, 3))
W1M0 = sp.Matrix(3, 3, lambda i, j: ptW1[M[0][i][j]])
assert all(sp.expand(c).subs(ptW1) == 0 for c in coeffs) and W1M0.rank() == 2
print("  W1 (ANNIHILATING branch): conn=0, tail matrix rank 2 -> in the variety, rank exactly 2")
print("     at EVERY splitting. The law does not exclude annihilation.")
# WITNESS W2 (obstructed, in-variety): common left kernel, conn entries generic nonzero:
W2conn_nonzero = any(ptV[M[m][i][j]] != 0 for m in (1, 2, 3) for i in range(2) for j in range(3))
W2rank_generic = sp.Matrix(3, 3, lambda i, j: (M[0][i][j] + t1 * M[1][i][j] + t2 * M[2][i][j]
                 + t3 * M[3][i][j]).subs(ptV)).subs({t1: 1, t2: sp.Rational(1, 2), t3: -2}).rank()
print(f"  W2 (OBSTRUCTED branch): common-left-kernel point, conn entries nonzero = {W2conn_nonzero},")
print(f"     rank Y(t*) = {W2rank_generic} at a sample splitting -> in the variety, generically rank 2.")
assert W2conn_nonzero and W2rank_generic == 2
print("  => EVEN THE IMPORTED LAW LEAVES BOTH FORK BRANCHES OPEN (W1, W2 both committed-legal +")
print("     law-compatible). It does NOT resolve the fork.")
# annihilation inside the conditional variety:
eqs_annV = eqs_ann + [detM0]
ptA = {v: sp.Integer(0) for v in flat}
for i in range(2):
    for j in range(3): ptA[M[0][i][j]] = sp.Rational(random.randint(1, 9), random.randint(1, 3))
rA = jac_rank_at(eqs_annV, ptA)
print(f"  annihilation INSIDE the variety = {{conn=0, det(tail)=0}}: Jacobian rank {rA} -> dim {36-rA};")
assert rA == 28
print(f"  codim inside the 26-dim component = {26 - (36 - rA)}.")
print("  DERIVED FALSIFIABLE CONSEQUENCE: rank-law + annihilation => det(tail observable) = 0.")
print("  If codex's values land ANNIHILATING with det(Ybar) != 0, the imported law is refuted for")
print("  this block -- a free forward-looking test, at no cost to the committed record.")
print("  STRONG form note: rank exactly 2 forces Ybar != 0 (the OBSERVABLE nonzero) -- it still")
print("  does not force any of the 27 conn entries nonzero (W1).")

print()
print("G3 VERDICT: allowed space = K^36 (0 committed equations on the block); annihilation locus")
print("codim 27 (dim 9 = the surviving observable); NO committed constraint forces a nonzero")
print("connecting entry (fork NOT resolvable to OBSTRUCTED without codex's values) and none forces")
print("annihilation; the conditional E8 layer cuts to a codim-10 variety, keeps both branches open,")
print("and adds one falsifiable cross-check (det Ybar = 0 under annihilation).")

json.dump({"allowed_space": "full K^36 -- zero committed equations on the block",
           "annihilation": {"codim": 27, "dim": 9, "surviving": "the 3x3 tail observable Ybar"},
           "forced_nonzero": False, "forced_annihilation": False,
           "conditional_E8_layer": {"import_fence": "B1185 INV-3 (non-importable; run as labeled conditional)",
                                    "variety_local_dim": 26, "codim": 10,
                                    "both_branches_survive": True,
                                    "annihilation_codim_inside": 18,
                                    "derived_test": "annihilation + law => det(Ybar) = 0"},
           "controls": ["{M1=0} codim 9 recovered", "{det M0=0} codim 1 recovered",
                        "common-left-kernel point lies in variety, smooth dim 26"]},
          open(os.path.join(CELL, "g3_locus.json"), "w"), indent=1)
