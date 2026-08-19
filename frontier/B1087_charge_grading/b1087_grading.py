"""B1087 — THE CHARGE GRADING of the twisted double's surviving classes.

DESIGN (pre-registered before execution; the outcome grammar covers every branch):
  The dial slot hv8 (and hv16 as cross-slot control) is completed to an sl2-triple
  (X, H, Y) by Jacobson-Morozov (exact linear algebra in e6 over Q). H is the
  candidate AW-U(1) charge generator. Then, in order:
  O1. If the JM solve fails structurally -> typed obstruction, banks as the finding.
  O2. rho27(H): the charge operator on the 27 (eigenvalues + multiplicities).
  O3. Cusp equivariance: does rho27(H) commute with BOTH cusp matrices (Amu, Alam)?
      NO -> the seam grading is not H-defined; banks as typed obstruction.
  O4. The fiber no-go, stated: the theta-odd twisted amalgam's closure is ALL of e6
      (B1086's sweep), so only scalars commute with the twisted image and NO
      nontrivial charge operator acts on H^1(D_t;27) as a fixed fiber. The
      computable gradings are (a) the SEAM h^1(T^2;27) if O3 holds, and (b) the
      FAMILY: [H, X] = 2X means the dial parameter t itself carries H-weight 2
      (exp(sH) maps the t-fiber to the e^{2s}t-fiber).
  O5. If O3 holds: the H-grading of the seam space -- Z^1(T^2)/B^1(T^2) decomposed
      by H-weight; SYMMETRIC (weights come in +-q pairs / zero) vs ASYMMETRIC is
      the verdict. The 27-bar side must negate the weights (PD cross-check).
  Verdict grammar: GRADED-SYMMETRIC / GRADED-ASYMMETRIC / OBSTRUCTED-(O1|O3),
  each with the fiber no-go and family-weight statement carried alongside.

Provenance: builds on the outside bench's twisted_double.py machinery, verified
end-to-end on this bench (B1086) before any new use. All new computation exact.
"""
import importlib.util, sys, os
from fractions import Fraction as F
import sympy as sp

CERT = os.environ.get("B1087_CERT_PATH", "(scratchpad)/cloud_handoff/certificates/twisted_double.py")

G = {}
src = open(CERT).read()
# stop the cert after stage 6's cusp objects exist; stages 7-8 sweeps not needed here
cut = src.find('print(" IDENTITY double')
if cut < 0: cut = src.find("# ---------------- stage 7")
exec(src[:cut] if cut > 0 else src, G)
print("\n=== B1087: cert machinery loaded (stages 0-6) ===")

br, add_, smul_, is_zero = G['br'], G['add_'], G['smul_'], G['is_zero']
DIM, N = G['DIM'], G['N']
X8, X16 = G['X8'], G['X16']
rho27_Q = G['rho27_Q']
toF, mmul, msub, eye27 = G['toF'], G['mmul'], G['msub'], G['eye']
Amu, Alam = G['Amu'], G['Alam']

def basis_vec(i):
    v = [F(0)]*DIM; v[i] = F(1); return v

def ad_matrix(X):
    cols = []
    for i in range(DIM):
        img = br(X, basis_vec(i))
        cols.append([sp.Rational(c.numerator, c.denominator) for c in img])
    return sp.Matrix(cols).T  # column j = ad_X(e_j)

def to_sp(vec):
    return sp.Matrix([sp.Rational(c.numerator, c.denominator) for c in vec])

def to_frac(spvec):
    return [F(sp.Rational(x).p, sp.Rational(x).q) for x in spvec]

def jm_triple(X, name):
    adX = ad_matrix(X)
    ad2 = adX * adX
    target = -2 * to_sp(X)
    try:
        sol = ad2.gauss_jordan_solve(target)[0]
        sol = sol.subs({s: 0 for s in sol.free_symbols})
    except Exception as ex:
        print(f"O1 OBSTRUCTED ({name}): ad^2 Y = -2X has no solution: {ex}")
        return None
    if any(sp.simplify(v) != 0 for v in (ad2 * sol - target)):
        print(f"O1 OBSTRUCTED ({name}): no exact solution")
        return None
    Y = to_frac(sol)
    H = br(X, Y)
    # verify [H,X] = 2X
    HX = br(H, X)
    ok1 = all(HX[i] == F(2)*X[i] for i in range(DIM))
    # correct Y by kernel components to enforce [H,Y] = -2Y (standard JM step)
    HY = br(H, Y)
    ok2 = all(HY[i] == F(-2)*Y[i] for i in range(DIM))
    if ok1 and not ok2:
        # project: solve (ad_H + 2) dY = ([H,Y]+2Y) with dY in ker(ad_X)
        adH = ad_matrix(H)
        M = adH + 2*sp.eye(DIM)
        rhs = to_sp(HY) + 2*to_sp(Y)
        kerX = ad_matrix(X).nullspace()
        Kb = sp.Matrix.hstack(*kerX) if kerX else sp.zeros(DIM, 0)
        A = M * Kb
        try:
            c = A.gauss_jordan_solve(rhs)[0]
            c = c.subs({s: 0 for s in c.free_symbols})
            dY = Kb * c
            Y = to_frac(to_sp(Y) - dY)
            H = br(X, Y)
            HY = br(H, Y)
            ok2 = all(HY[i] == F(-2)*Y[i] for i in range(DIM))
            HX = br(H, X); ok1 = all(HX[i] == F(2)*X[i] for i in range(DIM))
        except Exception as ex:
            print(f"  ({name}) JM correction step failed: {ex}")
    print(f"JM({name}): [H,X]=2X: {ok1} | [H,Y]=-2Y: {ok2}")
    return (X, H, Y) if (ok1 and ok2) else None

results = {}
for name, X in (("hv8", X8), ("hv16", X16)):
    print(f"\n--- slot {name} ---")
    trip = jm_triple(X, name)
    if trip is None:
        results[name] = "OBSTRUCTED-O1"
        continue
    X_, H, Y_ = trip
    # O2: the charge operator on the 27
    H27q = rho27_Q(H)
    H27sp = sp.Matrix([[sp.Rational(v.numerator, v.denominator) for v in row] for row in H27q])
    eigs = H27sp.eigenvals()
    spec = sorted(((sp.nsimplify(k), int(m)) for k, m in eigs.items()), key=lambda t: t[0])
    print(f"O2 rho27(H) spectrum (charge, mult): {spec}")
    tr = sum(k*m for k, m in spec)
    print(f"   trace = {tr} (0 iff sl2-balanced on the 27)")
    # O3: cusp equivariance
    H27F = toF([[v for v in row] for row in H27q])
    commA = mmul(H27F, Amu) == mmul(Amu, H27F)
    commL = mmul(H27F, Alam) == mmul(Alam, H27F)
    print(f"O3 cusp equivariance: [H27, Amu]=0: {commA} | [H27, Alam]=0: {commL}")
    if not (commA and commL):
        results[name] = ("OBSTRUCTED-O3", spec)
        continue
    # O5: the seam grading — Z^1(T^2)/B^1 under H
    # T^2 cocycles for the commuting pair (Amu, Alam) with module the 27:
    # Z = {(u,v) in 27+27 : (Alam - 1)u = (Amu - 1)v} ; B = {((Amu-1)w, (Alam-1)w)}
    n = 27
    def spF(Mf):
        return sp.Matrix([[sp.Rational(a.numerator, a.denominator) +
                           sp.sqrt(-3)*sp.Rational(b.numerator, b.denominator)
                           for (a, b) in row] for row in Mf])
    AmuS, AlamS = spF(Amu), spF(Alam)
    I = sp.eye(n)
    Zmat = sp.Matrix.hstack(AlamS - I, -(AmuS - I))  # kernel = Z^1
    Zbasis = Zmat.nullspace()
    Bgen = sp.Matrix.vstack(AmuS - I, AlamS - I)     # columns' span = B^1
    print(f"O5 seam: dim Z^1 = {len(Zbasis)}, rank B^1 = {Bgen.rank()}, h^1(T^2) = {len(Zbasis)-Bgen.rank()}")
    H27S = spF(H27F)
    Hbig = sp.diag(H27S, H27S)
    # action on H^1(T^2): matrix of Hbig on Z-basis modulo B
    Zb = sp.Matrix.hstack(*Zbasis)
    full = sp.Matrix.hstack(Zb, Bgen)
    # coordinates of Hbig*Zb in the (Zb | Bgen) spanning set -> the Z-block is the induced action
    act = []
    for j in range(Zb.cols):
        w = Hbig * Zb[:, j]
        sol = full.gauss_jordan_solve(w)[0]
        sol = sol.subs({s: 0 for s in sol.free_symbols})
        act.append([sp.nsimplify(sol[i]) for i in range(Zb.cols)])
    ActZ = sp.Matrix(act).T
    # eigenvalues of the induced action on Z^1 include B-directions' artifacts;
    # do the honest quotient: eigenvalues of ActZ restricted to a complement of B in Z
    # via: charge spectrum on Z^1, then on B^1, quotient multiset = difference
    eZ = ActZ.eigenvals()
    # B^1 grading: Hbig maps B to B (equivariance); induced on the generating map w -> ((Amu-1)w,(Alam-1)w)
    # commutes with H27 on the source, so B-grading = H27 spectrum restricted to im(d0)-source modulo ker d0
    kerd0 = Zmat  # not needed; compute directly:
    d0 = Bgen
    src_act = H27S
    # ker d0 = invariants of the pair; charge on coker-of-ker source:
    kd = d0.nullspace()
    print(f"   dim ker d0 (T^2 invariants) = {len(kd)}")
    specZ = sorted(((sp.nsimplify(k), int(m)) for k, m in eZ.items()), key=lambda t: str(t[0]))
    print(f"   induced charge spectrum on Z^1(T^2): {specZ}")
    src_spec = sorted(((sp.nsimplify(k), int(m)) for k, m in src_act.eigenvals().items()), key=lambda t: str(t[0]))
    kd_charges = []
    if kd:
        Kb2 = sp.Matrix.hstack(*kd)
        acts = []
        for j in range(Kb2.cols):
            w = H27S * Kb2[:, j]
            sol = Kb2.gauss_jordan_solve(w)[0]
            sol = sol.subs({s: 0 for s in sol.free_symbols})
            acts.append([sp.nsimplify(sol[i]) for i in range(Kb2.cols)])
        Kact = sp.Matrix(acts).T
        kd_charges = sorted(((sp.nsimplify(k), int(m)) for k, m in Kact.eigenvals().items()), key=lambda t: str(t[0]))
    print(f"   charge on ker d0 (-> h^0(T^2)): {kd_charges}")
    # h^1 charges = (Z charges) minus (27 charges) plus (ker d0 charges)  [long exact / dimension bookkeeping]
    from collections import Counter
    cnt = Counter()
    for k, m in specZ: cnt[k] += m
    for k, m in src_spec: cnt[k] -= m
    for k, m in kd_charges: cnt[k] += m
    h1_charges = sorted(((k, m) for k, m in cnt.items() if m != 0), key=lambda t: str(t[0]))
    print(f"O5 RESULT — charge spectrum on h^1(T^2;27): {h1_charges}")
    sym = all(dict(h1_charges).get(-q, 0) == m for q, m in h1_charges)
    print(f"   symmetric under q -> -q: {sym}")
    results[name] = ("GRADED-SYMMETRIC" if sym else "GRADED-ASYMMETRIC", spec, h1_charges)

print("\n=== O4 (carried in every branch): the fiber no-go + the family weight ===")
print("The theta-odd twisted amalgam's closure is ALL of e6 (B1086's sweep), so only")
print("scalars commute with the twisted image: NO nontrivial charge operator acts on")
print("H^1(D_t;27) at fixed t. [H,X]=2X puts H-weight 2 on the dial parameter itself:")
print("exp(sH) maps the t-fiber to the exp(2s)t-fiber — the U(1) grades the FAMILY.")
print("\n=== SUMMARY ===")
for k, v in results.items():
    print(k, "->", v if isinstance(v, str) else v[0])
import json
def ser(o):
    if isinstance(o, tuple): return [ser(x) for x in o]
    if isinstance(o, list): return [ser(x) for x in o]
    try: return str(o)
    except Exception: return repr(o)
json.dump({k: ser(v) for k, v in results.items()},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "b1087_results.json"), "w"), indent=2)
print("results written")
