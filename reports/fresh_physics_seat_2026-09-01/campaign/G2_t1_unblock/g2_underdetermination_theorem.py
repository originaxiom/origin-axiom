"""G2 step 2 -- UNDERDETERMINED, PROVED. Two theorems, exact over K = Q(zeta_12):

THEOREM A (two-model independence). There exist tensors T_ann, T_obs on the physical
(A_7,B_6,B_2) slice, BOTH satisfying every committed constraint on the down block
(C12 selection rho+sigma=8 mod 12; antisymmetry of the two B legs; hence the committed
SKEW (4,4) ZERO; character-support bookkeeping), such that T_ann annihilates the
connecting subspace C (spread 0, the P^3 invisible) and T_obs does not (spread != 0).
Therefore the committed record proves NEITHER branch of B1232's fork: the annihilation
question is formally INDEPENDENT of the committed constraints. (Model-existence is the
standard independence method; both models are exhibited and machine-checked.)

THEOREM B (the freedom group). Even GIVEN codex's frame data up to the identifications
the committed record fixes (the character decomposition, the conn-sub/tail-quotient
filtrations, and nothing else), the 36 block values are determined only up to
    G = ( GL(A_7) x P(B_6) x P(B_2) x K^x_trace ) / (redundant scalar torus),
P(-) the parabolic preserving conn (B_6: 2-dim conn in 3; B_2: 3-dim conn in 4).
Computed below: dim Lie(G)_effective = 27 = generic orbit dimension in the 36-dim block
(stabilizer of a generic block is 3 redundant-scalar directions of the 30-dim raw Lie
algebra). The 27 connecting VALUES are not G-invariant (exhibited); the vanishing of all
27 IS G-invariant (proved structurally + checked exactly); and the boundary is sharp: a
frame change violating the filtration destroys the invariance (bite).

Conventions (E23): as T1/s1 -- raw chi_r = zeta_12^r on [M1]'s marked generator; physical
= raw twisted by chi_{-2} once; connecting quotient = SUB, Serre-dual tail = QUOTIENT of
B; splittings s_t(1) = bhat + sum t_k c_k. Entries live in K, arithmetic mod z^4-z^2+1.
"""
import sympy as sp
import random, json, os

random.seed(20260901)
CELL = os.path.dirname(os.path.abspath(__file__))
z = sp.Symbol("z")                              # zeta_12
MIN = sp.Poly(z**4 - z**2 + 1, z)
def red(e): return sp.rem(sp.Poly(sp.expand(e), z), MIN).as_expr()
def rq(): return sp.Rational(random.randint(-9, 9), random.randint(1, 5))
def rk(): return red(sum(rq() * z**i for i in range(4)))   # random element of K

# ---------------------------------------------------------------------------
# The committed slot model of B (from [M1], verbatim ledger):
#   conn multiplicities by raw label 0..11, tails at labels (0,2,4,6,8)
# ---------------------------------------------------------------------------
CONN_MULT = (2, 4, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3)
TAILS = (0, 2, 4, 6, 8)
SLOTS = [("c", r, i) for r in range(12) for i in range(CONN_MULT[r])] + [("t", r, 0) for r in TAILS]
assert len(SLOTS) == 38, "dim B must be 38 (33 conn + 5 tail)"
def label(s): return s[1]

# ---------------------------------------------------------------------------
# CHK -- the committed-constraint checker (MB12: failable, and its failures bite)
# T is a dict {(i, s1, s2): value in K} over i in 0..2 (A_7 family), s1,s2 in SLOTS.
# ---------------------------------------------------------------------------
def CHK(T, name):
    fails = []
    for (i, s1, s2), v in T.items():
        if red(v) != 0 and (label(s1) + label(s2)) % 12 != 8:
            fails.append(f"K1 selection: entry (i={i},{s1},{s2}) nonzero in a rho+sigma={label(s1)+label(s2)}%12 channel")
    for (i, s1, s2), v in T.items():
        w = T.get((i, s2, s1), 0)
        if red(v + w) != 0:
            fails.append(f"K2 antisymmetry: T[{i},{s1},{s2}] + T[{i},{s2},{s1}] != 0")
    for i in range(3):                            # K3 = the committed SKEW ZERO, derived
        v = T.get((i, ("t", 4, 0), ("t", 4, 0)), 0)
        if red(v) != 0:
            fails.append(f"K3 skew(4,4) zero: repeated tail-4 diagonal nonzero at i={i}")
    print(f"  CHK({name}): {'PASS' if not fails else 'FAIL'}" + (f" -- {fails[0]}" if fails else ""))
    return not fails

print("=" * 78)
print("[1] CHK instrument bites (MANDATORY planted cases -- each constraint failable):")
print("=" * 78)
B6c = [("c", 6, i) for i in range(2)]; B6t = ("t", 6, 0)
B2c = [("c", 2, i) for i in range(3)]; B2t = ("t", 2, 0)
def antisym_close(T):
    out = dict(T)
    for (i, s1, s2), v in list(T.items()):
        out[(i, s2, s1)] = red(-v)
    return out
ok = CHK(antisym_close({(0, B6c[0], B2c[0]): z}), "conforming single entry")
assert ok
bad1 = CHK(antisym_close({(0, ("c", 1, 0), ("c", 4, 0)): 1}), "PLANT selection violation (1+4=5)")
bad2 = CHK({(0, B6c[0], B2c[0]): 1, (0, B2c[0], B6c[0]): 1}, "PLANT symmetric pair")
bad3 = CHK({(1, ("t", 4, 0), ("t", 4, 0)): z**2}, "PLANT nonzero skew-(4,4) diagonal")
assert not bad1 and not bad2 and not bad3
print("  -> the checker DECIDES: conforming passes, each planted violation is caught by name.")
print("  -> and the committed SKEW ZERO is a THEOREM of the checker (K2 => K3 in char 0),")
print("     reproduced as the planted known case: the one committed exact entry-level zero.")

print()
print("=" * 78)
print("[2] THEOREM A -- two models, both committed-legal, opposite fork branches:")
print("=" * 78)
# The selected physical block: i in A_7(3), j in B_6 (2 conn + 1 tail), k in B_2 (3 conn + 1 tail).
B6S = B6c + [B6t]; B2S = B2c + [B2t]
def block_to_T(block):                            # block[(i,j,k)] over the 3x3x4 selected slice
    return antisym_close({(i, B6S[j], B2S[k]): v for (i, j, k), v in block.items() if red(v) != 0})

tailvals = [[rk() for _ in range(3)] for _ in range(3)]
T_ann_blk = {(i, j, 3): tailvals[i][j] for i in range(3) for j in range(3)}       # conn entries ABSENT (=0)
T_obs_blk = dict(T_ann_blk); T_obs_blk[(1, 2, 0)] = z                              # ONE conn entry = zeta_12
ok_ann = CHK(block_to_T(T_ann_blk), "T_ann (27 conn entries = 0, generic K tails)")
ok_obs = CHK(block_to_T(T_obs_blk), "T_obs (single conn entry = zeta_12)")
assert ok_ann and ok_obs, "both models must satisfy every committed constraint"

def spread_exact(blk, npts=12):
    """max over exact splittings t of |Y[i,j](t)-Y[i,j](0)| != 0 as an exact K statement."""
    t_pts = [(sp.Rational(a, 3), sp.Rational(-b, 2), sp.Rational(a * b, 5)) for a in (1, 2, 3) for b in (1, 2)]
    devs = []
    for i in range(3):
        for j in range(3):
            for tp in t_pts[:npts]:
                Y0 = blk.get((i, j, 3), 0)
                Yt = Y0 + sum(tp[m] * blk.get((i, j, m), 0) for m in range(3))
                devs.append(red(Yt - Y0))
    return [d for d in devs if d != 0]
dev_ann, dev_obs = spread_exact(T_ann_blk), spread_exact(T_obs_blk)
print(f"  spread(T_ann): {len(dev_ann)} nonzero deviations over 54 exact (i,j,t) probes -> P^3 INVISIBLE")
print(f"  spread(T_obs): {len(dev_obs)} nonzero deviations (e.g. {dev_obs[0]}) -> P^3 VISIBLE")
assert not dev_ann and dev_obs
print("  => THEOREM A: the committed constraints admit BOTH an annihilating and an obstructing")
print("     model; B1232's fork is formally INDEPENDENT of the committed record. In particular")
print("     no committed constraint forces a nonzero connecting entry (T_ann is a witness), and")
print("     none forces annihilation (T_obs is a witness).")

print()
print("=" * 78)
print("[3] THEOREM B -- the freedom group G: dimension, orbit, invariance, sharp boundary")
print("=" * 78)
# Raw Lie algebra: gl3(A) + p(B6) + p(B2) + scale.  p(B6) in gl3 preserves span(e0,e1);
# p(B2) in gl4 preserves span(e0,e1,e2).  Basis of each:
def gl_basis(n): return [(a, b) for a in range(n) for b in range(n)]
def par_basis(n, k):  # parabolic preserving first-k subspace: entries (a,b) with not(a>=k and b<k)... careful:
    # X preserves span(e_0..e_{k-1}) iff X[a][b]=0 for a>=k, b<k  (column b<k maps into first k rows)
    return [(a, b) for a in range(n) for b in range(n) if not (a >= k and b < k)]
BA, B6b, B2b = gl_basis(3), par_basis(3, 2), par_basis(4, 3)
dim_raw = len(BA) + len(B6b) + len(B2b) + 1
print(f"  raw Lie dims: gl3(A)={len(BA)}, p(B6)={len(B6b)}, p(B2)={len(B2b)}, scale=1 -> total {dim_raw}")
assert (len(BA), len(B6b), len(B2b)) == (9, 7, 13) and dim_raw == 30

# Infinitesimal action on the 36-entry block T[i][j][k] (trilinear form, lower indices):
# (X.T)[i,j,k] = sum_a X_A[a,i] T[a,j,k] + sum_b X_6[b,j] T[i,b,k] + sum_c X_2[c,k] T[i,j,c] + lam*T
Tgen = [[[sp.Rational(random.randint(-20, 20), random.randint(1, 7)) for _ in range(4)] for _ in range(3)] for _ in range(3)]
def act_rows(Tv):
    rows = []
    def flat(d): return [d[i][j][k] for i in range(3) for j in range(3) for k in range(4)]
    for (a, i0) in BA:
        d = [[[Tv[a][j][k] if i == i0 else 0 for k in range(4)] for j in range(3)] for i in range(3)]
        rows.append(flat(d))
    for (b, j0) in B6b:
        d = [[[Tv[i][b][k] if j == j0 else 0 for k in range(4)] for j in range(3)] for i in range(3)]
        rows.append(flat(d))
    for (c, k0) in B2b:
        d = [[[Tv[i][j][c] if k == k0 else 0 for k in range(4)] for j in range(3)] for i in range(3)]
        rows.append(flat(d))
    rows.append(flat(Tv))
    return rows
Mact = sp.Matrix(act_rows(Tgen))
rank_gen = Mact.rank()
print(f"  generic-block orbit dimension = rank of the 30x36 linearized action = {rank_gen}")
assert rank_gen == 27, "expected effective dim 27 = 30 - 3 redundant scalars"
# rows of Mact are the 36-vectors dT for each generator; stabilizer = combos of rows giving 0
print(f"  stabilizer of a generic block: dim {30 - rank_gen} (the redundant scalar torus:")
print("    mu_A*I_A + mu_6*I_6 + mu_2*I_2 + lam acts by (mu_A+mu_6+mu_2+lam); 3 relations)")
# confirm structurally: identity elements of the three gl's + scale with coefficients summing to 0
idxA = [BA.index((d, d)) for d in range(3)]
idx6 = [len(BA) + B6b.index((d, d)) for d in range(3)]
idx2 = [len(BA) + len(B6b) + B2b.index((d, d)) for d in range(4)]
for combo in ([(idxA, 1), (idx6, -1)], [(idxA, 1), (idx2, -1)], [(idx6, 1), (idx2, -1)]):
    vec = [0] * 30
    for idxs, sgn in combo:
        for ix in idxs: vec[ix] += sgn
    resid = (sp.Matrix([vec]) * Mact).norm()
    assert resid == 0, "scalar-difference direction must stabilize every block"
print("  confirmed exactly: the three scalar-difference directions annihilate EVERY block.")

# --- invariance of the vanishing property under the GROUP (not just the algebra), exact ---
def rand_parabolic(n, k):
    while True:
        g = sp.zeros(n, n)
        for a in range(n):
            for b in range(n):
                if not (a >= k and b < k): g[a, b] = rq()
        if g.det() != 0: return g
def rand_gl(n):
    while True:
        g = sp.Matrix(n, n, lambda a, b: rq())
        if g.det() != 0: return g
def group_act(Tv, gA, g6, g2, lam):
    return [[[red(lam * sum(gA[a, i] * g6[b, j] * g2[c, k] * Tv[a][b][c]
                            for a in range(3) for b in range(3) for c in range(4)))
              for k in range(4)] for j in range(3)] for i in range(3)]
T_ann_arr = [[[T_ann_blk.get((i, j, k), 0) for k in range(4)] for j in range(3)] for i in range(3)]
prop_holds, values_moved = True, False
for trial in range(25):
    gA, g6, g2, lam = rand_gl(3), rand_parabolic(3, 2), rand_parabolic(4, 3), sp.Rational(random.randint(1, 5), random.randint(1, 3))
    Tp = group_act(T_ann_arr, gA, g6, g2, lam)
    conn = [red(Tp[i][j][k]) for i in range(3) for j in range(3) for k in range(3)]
    if any(v != 0 for v in conn): prop_holds = False
    if any(red(Tp[i][j][3] - T_ann_arr[i][j][3]) != 0 for i in range(3) for j in range(3)): values_moved = True
print(f"  25 random G-elements on T_ann: all 27 conn entries stay 0 = {prop_holds}; tail VALUES moved = {values_moved}")
assert prop_holds and values_moved
T_obs_arr = [[[T_obs_blk.get((i, j, k), 0) for k in range(4)] for j in range(3)] for i in range(3)]
gA, g6, g2 = rand_gl(3), rand_parabolic(3, 2), rand_parabolic(4, 3)
Tp = group_act(T_obs_arr, gA, g6, g2, sp.Integer(2))
moved = [(i, j, k) for i in range(3) for j in range(3) for k in range(3)
         if red(Tp[i][j][k] - T_obs_arr[i][j][k]) != 0]
print(f"  on T_obs one G-element changes {len(moved)} of the 27 conn VALUES (they are NOT invariant);")
print("  the PROPERTY 'all 27 vanish' is invariant (parabolic preserves conn; checked above).")
assert moved

# --- the sharp boundary (bite): a filtration-VIOLATING frame change kills the invariance ---
# The violating element must mix tail INTO a conn entry: T'[.,.,conn0] = sum_c g[c,0] T[.,.,c]
# picks up T[.,.,tail] iff g[3,0] != 0 -- exactly the entry the parabolic shape forbids (a>=3, b<3):
g2_bad = sp.eye(4); g2_bad[3, 0] = 1
Tbad = group_act(T_ann_arr, sp.eye(3), sp.eye(3), g2_bad, sp.Integer(1))
leaked = [red(Tbad[i][j][0]) for i in range(3) for j in range(3) if red(Tbad[i][j][0]) != 0]
print(f"  BITE: the non-parabolic element (g[3,0]=1, tail->conn leak) makes {len(leaked)} conn entries")
print("  of the transformed T_ann NONZERO -- outside G the 'annihilates' property is NOT stable, so")
print("  G is exactly the filtration-preserving group; the committed filtration is load-bearing.")
assert leaked

print()
print("=" * 78)
print("[4] Consequence for the committed tail-row strings (closing g1 route E):")
print("=" * 78)
print("  The spec's five committed coordinate strings describe the PRESENTATION of coker(D)^*")
print("  (the tail sector's basis data). Both models of THEOREM A leave that presentation data")
print("  untouched -- they assign block VALUES, not presentations -- so for any fixed strings both")
print("  models remain committed-legal. The strings constrain the 27 connecting values not at all.")

print()
print("G2 VERDICT: UNDERDETERMINED, PROVED at two layers.")
print("  ABSOLUTE layer (Thm A): the committed record is CONSISTENT WITH BOTH fork branches --")
print("    the 27 values are underdetermined not merely up to gauge but up to everything: the")
print("    admissible set is the full K^36 block (g3 verifies no constraint cuts it).")
print("  FRAME layer (Thm B): even granting codex's frames-up-to-committed-identifications, the")
print("    values are determined only up to the 27-dimensional group G (9+7+13+1-3); a generic")
print("    G-orbit in the 36-dim block is 27-dimensional, the 27 values are gauge-variant, and")
print("    the annihilation PROPERTY is the invariant -- so the fork QUESTION is well-posed and")
print("    its ANSWER requires exactly the normalization data listed in the commissioning spec.")

json.dump({"theorem_A": "two committed-legal models, opposite fork branches -- independence",
           "theorem_B": {"raw_lie_dim": 30, "redundant_scalars": 3, "effective_dim": 27,
                         "generic_orbit_dim": int(rank_gen),
                         "invariant": "vanishing of all 27 conn entries",
                         "not_invariant": "the 27 values themselves; the 9 tail values"},
           "bites": ["selection violation caught", "symmetric pair caught", "skew(4,4) plant caught",
                     "non-parabolic tail->conn leak breaks invariance (group boundary sharp)"]},
          open(os.path.join(CELL, "g2_theorems.json"), "w"), indent=1)
