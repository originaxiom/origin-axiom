"""B713 PROBE 1 (the DECISIVE probe) — independent verification (cc seat).

QUESTION: Is the B299 trinification triality (theta,phi) a symmetry of the OBJECT
(the figure-eight geometric holonomy / its H^1(M;27)=3 matter cohomology), which
would let it author generation/chiral structure -- OUTCOME A; or is it ONLY a
symmetry of the abstract E6 REPRESENTATION (permutes SU(3)^3 gauge blocks on the
27), acting not-at-all on the object -- OUTCOME B (GAUGE-ONLY)?

This script INDEPENDENTLY reproduces the two-seat result:
  (a) SnapPy: Isom(4_1) = D4, order 8 -> no order-3 element -> no Z/3 can act on
      the manifold or its character variety at all.
  (b) Four exact non-commutation checks that (theta,phi) do NOT normalize the
      geometric holonomy rho(pi_1) that H^1(M;27)=3 is built on:
        (i)   h_pr (principal grading vector) is not fixed;
        (ii)  the 6 simple roots are not mapped to signed simple roots;
        (iii) the 27x27 support pattern of e_pr,f_pr,h_pr,A27,B27 is scrambled;
        (iv)  v0 (the H^0=1 invariant line) has its support sent to a DISJOINT set.

All 27-dim work is exact over Q(sqrt(-3)) (the repo's own K class, executed
read-only from B575). The transport of (theta,phi) into Bourbaki coordinates and
every check below is my own code (independent of cc2's scratch scripts).

Run: python3 frontier/B713_chirality/b713_probe1.py   (writes _out.txt via tee)
"""
import sys, time, itertools
import sympy as sp

T0 = time.time()
LINES = []
def out(msg=""):
    print(msg, flush=True)
    LINES.append(str(msg))

out("=" * 72)
out("B713 PROBE 1 — is the triality a symmetry of the OBJECT or GAUGE-ONLY?")
out("=" * 72)

# ======================================================================= (a)
out("\n--- (a) SnapPy: no order-3 symmetry of the figure-eight manifold ---")
import snappy
M = snappy.Manifold('4_1')
G = M.symmetry_group()
order = G.order()
out(f"  snappy.Manifold('4_1').symmetry_group() = {G}, order = {order}")
out(f"  order %% 3 = {order % 3}  ->  Lagrange: order-3 element exists = {order % 3 == 0}")
NO_Z3_ON_MANIFOLD = (str(G) == "D4" and order == 8 and order % 3 != 0)
out(f"  => NO Z/3 acts on the manifold / character variety: {NO_Z3_ON_MANIFOLD}")

# ======================================================================= data
# B299 trinification triality (theta,phi) on the E6 Cartan (its OWN simple-root
# ordering, det-3 E6 Cartan).  Re-embedded verbatim from
# frontier/B299_trinification_triality/trinification_triality.py.
THETA = sp.Matrix([[0,-1,1,0,0,0],[1,-1,1,0,0,0],[0,0,1,0,0,0],
                   [0,0,1,0,-1,0],[0,0,0,1,-1,0],[0,0,0,0,0,1]])
PHI = sp.Matrix([[1,0,0,0,0,-1],[0,1,0,0,0,-2],[0,0,1,0,0,-3],
                 [0,0,1,-1,1,-2],[0,0,1,-1,0,-1],[0,0,1,0,0,-2]])
E6_CARTAN = sp.Matrix([[2,-1,0,0,0,0],[-1,2,-1,0,0,0],[0,-1,2,-1,0,-1],
                       [0,0,-1,2,-1,0],[0,0,0,-1,2,0],[0,0,-1,0,0,2]])

# sanity on the triality itself (independent re-check)
I6 = sp.eye(6)
assert THETA**3 == I6 and PHI**3 == I6 and THETA*PHI == PHI*THETA
assert THETA.det() == 1 and PHI.det() == 1
assert THETA.T*E6_CARTAN*THETA == E6_CARTAN and PHI.T*E6_CARTAN*PHI == E6_CARTAN
assert E6_CARTAN.det() == 3
out("\n  [triality self-check] theta,phi: order 3, commute, det 1, preserve E6_CARTAN(det 3): OK")

# ======================================================================= build the OBJECT
# Execute B575 stages 0-3 (read-only) to obtain the geometric holonomy exactly.
out("\n--- building the geometric holonomy (B575 stages 0-3, exact over Q(sqrt-3)) ---")
B575 = "frontier/B575_bridge_obstruction/l51_obstruction.py"
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
tb = time.time()
exec(compile(src[:cut], B575, "exec"), ns)
out(f"  holonomy built in {time.time()-tb:.1f}s")

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
W27 = ns["W27"]
C6 = ns["C6"]                       # Bourbaki E6 Cartan (list of lists, ints)
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
A27, B27 = ns["A27"], ns["B27"]
kvals = ns["kvals"]                 # C6 * k = 2*ones  (K entries)
nullspace = ns["nullspace"]
apply_op = lambda Mm, v: [sum((Mm[i][j]*v[j] for j in range(27) if not v[j].is_zero()), K0) for i in range(27)]

C6m = sp.Matrix(C6)
assert C6m.det() == 3
kv = [int(v.a) for v in kvals]      # kvals as ints (a-parts; b-parts are 0)
assert all(v.b == 0 for v in kvals)
# independent re-solve of C6 k = 2*ones to confirm kvals
k_check = C6m.LUsolve(sp.Matrix([2]*6))
assert list(k_check) == kv, (list(k_check), kv)
out(f"  principal grading kvals (C6.k = 2.ones) = {kv}   [independently re-solved: OK]")

# ======================================================================= transport
# B299's E6_CARTAN and B575's C6 are the SAME abstract E6 Cartan in two different
# simple-root orderings. Find permutation matrices P with P^T C6 P = E6_CARTAN,
# then transport THETA_B = P THETA P^-1 into Bourbaki coordinates.
out("\n--- transporting (theta,phi) into the holonomy's Bourbaki basis ---")
def perm_matrix(sigma):
    # P e_i = e_{sigma[i]}  (column i has 1 in row sigma[i])
    P = sp.zeros(6, 6)
    for i in range(6):
        P[sigma[i], i] = 1
    return P

good = []
for sigma in itertools.permutations(range(6)):
    P = perm_matrix(sigma)
    if P.T * C6m * P == E6_CARTAN:
        good.append(sigma)
out(f"  # permutations sigma with P^T C6 P = E6_CARTAN : {len(good)}  (= the diagram's own symmetry)")
assert len(good) >= 1

def transport(sigma):
    P = perm_matrix(sigma)
    Pi = P.inv()
    TB = P * THETA * Pi
    FB = P * PHI * Pi
    # consistency: TB,FB must preserve C6 (proof-check of the transport)
    assert TB.T * C6m * TB == C6m and FB.T * C6m * FB == C6m
    assert TB**3 == I6 and FB**3 == I6 and TB*FB == FB*TB
    return TB, FB

# run every check for EVERY valid transport; record verdict per check
def run_checks(sigma, verbose=False):
    TB, FB = transport(sigma)
    kvec = sp.Matrix(kv)
    res = {}

    # ---- check (i): h_pr (grading vector kvals) fixed?  g(h_pr) coeffs = M*k ----
    res['i_theta_fix'] = (TB * kvec == kvec)
    res['i_phi_fix']   = (FB * kvec == kvec)
    res['i_theta_img'] = list(TB * kvec)
    res['i_phi_img']   = list(FB * kvec)

    # ---- check (ii): simple roots -> signed simple roots? (columns = images) ----
    def signed_simple_cols(Mm):
        n_ok = 0; bad = []
        for i in range(6):
            col = [Mm[r, i] for r in range(6)]
            nz = [(r, col[r]) for r in range(6) if col[r] != 0]
            if len(nz) == 1 and abs(nz[0][1]) == 1:
                n_ok += 1
            else:
                bad.append(i)
        return n_ok, bad
    res['ii_theta_ok'], res['ii_theta_bad'] = signed_simple_cols(TB)
    res['ii_phi_ok'],   res['ii_phi_bad']   = signed_simple_cols(FB)

    # ---- weight permutation on the 27 induced by g (Dynkin-label action C M C^-1) --
    C6inv = C6m.inv()
    def weight_perm(Mm):
        A = C6m * Mm * C6inv           # action on Dynkin labels
        A = sp.Matrix(6, 6, lambda i, j: int(A[i, j]))
        WI = {tuple(w): idx for idx, w in enumerate(W27)}
        perm = []
        for w in W27:
            wv = A * sp.Matrix(w)
            key = tuple(int(x) for x in wv)
            assert key in WI, "triality does not permute the 27!"  # closure gate
            perm.append(WI[key])
        assert sorted(perm) == list(range(27))                     # it IS a bijection
        return perm
    permT = weight_perm(TB)
    permF = weight_perm(FB)

    # ---- check (iii): 27x27 support scrambled?  X'[p[i]][p[j]] = X[i][j] ----------
    def support_mismatch(X, perm):
        pinv = [0]*27
        for i, p in enumerate(perm):
            pinv[p] = i
        mm = 0
        for r in range(27):
            for c in range(27):
                a = not X[r][c].is_zero()
                b = not X[pinv[r]][pinv[c]].is_zero()   # = X'[r][c]
                if a != b:
                    mm += 1
        return mm
    ops = {'e_pr': e_pr, 'f_pr': f_pr, 'h_pr': h_pr, 'A27': A27, 'B27': B27}
    res['iii_theta'] = {n: support_mismatch(X, permT) for n, X in ops.items()}
    res['iii_phi']   = {n: support_mismatch(X, permF) for n, X in ops.items()}

    # ---- check (iv): v0 support -> disjoint set? --------------------------------
    fix = nullspace([[A27[i][j] - (K1 if i == j else K0) for j in range(27)] for i in range(27)]
                    + [[B27[i][j] - (K1 if i == j else K0) for j in range(27)] for i in range(27)])
    assert len(fix) == 1, f"H^0 != 1 (got {len(fix)})"
    v0 = fix[0]
    for op in (e_pr, f_pr, h_pr):
        assert all(x.is_zero() for x in apply_op(op, v0))   # v0 is sl2-invariant
    S = tuple(i for i in range(27) if not v0[i].is_zero())
    res['iv_v0_support'] = S
    res['iv_theta_image'] = tuple(permT[i] for i in S)
    res['iv_phi_image']   = tuple(permF[i] for i in S)
    res['iv_theta_disjoint'] = set(res['iv_theta_image']).isdisjoint(S)
    res['iv_phi_disjoint']   = set(res['iv_phi_image']).isdisjoint(S)
    return res

# ======================================================================= report
out("\n=== THE FOUR EXACT NON-COMMUTATION CHECKS (per valid transport) ===")
all_verdicts = []
for si, sigma in enumerate(good):
    r = run_checks(sigma)
    out(f"\n[transport sigma #{si+1} = {sigma}]")
    # (i)
    out(f"  (i)  h_pr fixed by theta: {r['i_theta_fix']}   (theta.kvals = {[int(x) for x in r['i_theta_img']]})")
    out(f"       h_pr fixed by phi:   {r['i_phi_fix']}   (phi.kvals   = {[int(x) for x in r['i_phi_img']]})")
    # (ii)
    out(f"  (ii) theta: {r['ii_theta_ok']}/6 simple roots -> signed simple; "
        f"NON-simple images at cols {r['ii_theta_bad']}")
    out(f"       phi:   {r['ii_phi_ok']}/6 simple roots -> signed simple; "
        f"NON-simple images at cols {r['ii_phi_bad']}")
    # (iii)
    out(f"  (iii) 27x27 support mismatches (of 729):")
    out(f"        theta: {r['iii_theta']}")
    out(f"        phi:   {r['iii_phi']}")
    # (iv)
    out(f"  (iv) v0 support {r['iv_v0_support']} ->")
    out(f"        theta image {r['iv_theta_image']}  disjoint={r['iv_theta_disjoint']}")
    out(f"        phi   image {r['iv_phi_image']}  disjoint={r['iv_phi_disjoint']}")

    v_i   = not (r['i_theta_fix'] or r['i_phi_fix'])
    v_ii  = (r['ii_theta_ok'] < 6) and (r['ii_phi_ok'] < 6)
    v_iii = any(v > 0 for v in r['iii_theta'].values()) and any(v > 0 for v in r['iii_phi'].values())
    v_iv  = r['iv_theta_disjoint'] and r['iv_phi_disjoint']
    all_verdicts.append((v_i, v_ii, v_iii, v_iv))

# ======================================================================= verdict
out("\n" + "=" * 72)
NC = all(all(v) for v in all_verdicts)   # all four checks say NON-commutation, every transport
out(f"ALL FOUR CHECKS => (theta,phi) do NOT normalize the holonomy: {NC}")
out(f"SnapPy: no order-3 symmetry of the manifold at all: {NO_Z3_ON_MANIFOLD}")
GAUGE_ONLY = NC and NO_Z3_ON_MANIFOLD
out("")
if GAUGE_ONLY:
    out("VERDICT: OUTCOME B — GAUGE-ONLY.")
    out("  The triality is a symmetry of the abstract E6 REPRESENTATION only")
    out("  (it permutes the SU(3)^3 gauge blocks on the 27: 9 free orbits of 3).")
    out("  It does NOT act on the OBJECT: it fails to normalize the geometric")
    out("  holonomy rho(pi_1), so it does not descend to H^1(M;27)=3 at all, and")
    out("  the manifold has no order-3 symmetry to carry any such action.")
    out("  => the triality CANNOT author generation/chiral structure in the object.")
else:
    out("VERDICT: OUTCOME A (or inconclusive) — RE-EXAMINE.")
out("=" * 72)

with open("frontier/B713_chirality/b713_probe1_out.txt", "w") as f:
    f.write("\n".join(LINES) + "\n")
out(f"\n[wrote frontier/B713_chirality/b713_probe1_out.txt; total {time.time()-T0:.1f}s]")
