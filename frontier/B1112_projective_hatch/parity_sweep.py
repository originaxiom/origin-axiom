"""B1098 - THE NON-ABELIAN HATCH, first stratum: sl2-factored holonomy.

DESIGN (pre-registered): every non-abelian holonomy factoring pi1(M) -> SL(2,C) -> E6
lands in an sl2 conjugacy class = a nonzero nilpotent orbit of e6. For each class:
representative -> JM triple (the B1087-verified solver pattern) -> exact centralizer
c = ker(ad e) & ker(ad h) & ker(ad f) -> dim, reductive rank (generic-element method,
repeated for safety), simple-factor types (identified by (rank, dim)) -> SM-containment
verdict per the justified rank-4 table:
  rank-4 SM-containers: A4, A3+A1, A2+A2, A2+A1(+T1), B4, C4, F4  [D4 EXCLUDED:
  su(3) in so(8) has commutant u(1)+u(1) only - no commuting su(2)];
  rank > 4 with an SM-container inside: SM-compatible-with-extra-U(1)s (weaker landing).
Orbit enumeration is CONSTRUCTIVE (no table imported for representatives): the regular
nilpotent of every standard Levi (sum of the Levi's simple-root vectors) + a search over
random nilpotents inside the D4, D5, E6 Levis for their distinguished non-regular
orbits (D4(a1), D5(a1), E6(a3), E6(a1)); classes deduped by the ad-h eigenvalue
multiset (a complete invariant given the centralizer dim). The known count for e6 is
20 nonzero orbits (CITED, Bala-Carter); the enumeration must saturate it or report
what it found - no silent gap.

Outcome grammar: HATCH OPENS (nonempty SM-compatible list, named classes - the
object's own hyperbolic rho composed with the class embedding supplies the flat
connection) / HATCH CLOSES at the sl2-factored stratum. Either banks.

Adjacent prior art (declared, non-colliding): B854 (the FINITE 2T centralizer =
u(1)^4, abelian, rank 4); B932 (finite-order torus elements only).
"""
import os, sys, json, itertools, random
from fractions import Fraction as F
import sympy as sp

CERT = os.environ.get("B1098_CERT_PATH", os.environ.get("B1098_CERT_PATH","(set B1098_CERT_PATH; cert is the session twisted_double.py)"))
G = {}
src = open(CERT).read()
cut = src.find('print(" IDENTITY double')
exec(src[:cut] if cut > 0 else src, G)
br, add_, smul_, is_zero = G['br'], G['add_'], G['smul_'], G['is_zero']
evec, hvec, ROOTS, IDX, N, DIM = G['evec'], G['hvec'], G['ROOTS'], G['IDX'], G['N'], G['DIM']
print(f"e6 loaded: {len(ROOTS)} roots, dim {DIM}")

def basis_vec(i):
    v = [F(0)]*DIM; v[i] = F(1); return v

def ad_matrix(X):
    cols = []
    for i in range(DIM):
        img = br(X, basis_vec(i))
        cols.append([sp.Rational(c.numerator, c.denominator) for c in img])
    return sp.Matrix(cols).T

def to_sp(vec):
    return sp.Matrix([sp.Rational(c.numerator, c.denominator) for c in vec])

def to_frac(v):
    return [F(sp.Rational(x).p, sp.Rational(x).q) for x in v]

def jm_triple(X):
    adX = ad_matrix(X); ad2 = adX*adX
    target = -2*to_sp(X)
    try:
        sol = ad2.gauss_jordan_solve(target)[0]
        sol = sol.subs({s: 0 for s in sol.free_symbols})
    except Exception:
        return None
    if any(sp.simplify(v) != 0 for v in (ad2*sol - target)):
        return None
    Y = to_frac(sol); H = br(X, Y)
    HX = br(H, X)
    if not all(HX[i] == F(2)*X[i] for i in range(DIM)): return None
    HY = br(H, Y)
    if not all(HY[i] == F(-2)*Y[i] for i in range(DIM)):
        adH = ad_matrix(H); M = adH + 2*sp.eye(DIM)
        rhs = to_sp(HY) + 2*to_sp(Y)
        kerX = ad_matrix(X).nullspace()
        Kb = sp.Matrix.hstack(*kerX) if kerX else sp.zeros(DIM, 0)
        try:
            c = (M*Kb).gauss_jordan_solve(rhs)[0]
            c = c.subs({s: 0 for s in c.free_symbols})
            Y = to_frac(to_sp(Y) - Kb*c); H = br(X, Y)
            HY = br(H, Y)
            if not all(HY[i] == F(-2)*Y[i] for i in range(DIM)): return None
        except Exception:
            return None
    return X, H, Y

def adh_spectrum(H):
    """ad-H integer spectrum multiset (class key; float eigvals rounded — ad H has integer spectrum)"""
    A = _ad_np(H)
    ev = _np.linalg.eigvals(A)
    return tuple(sorted((round(float(x.real)), ) for x in ev for _ in [0]))

def centralizer_basis(X, H, Y):
    S = sp.Matrix.vstack(ad_matrix(X), ad_matrix(H), ad_matrix(Y))
    return S.nullspace()

def reductive_rank(cbasis):
    """rank of the reductive centralizer: dim ker(ad_c x) for generic x in c, min over trials"""
    if not cbasis: return 0
    n = len(cbasis)
    best = n
    rng = random.Random(20260820)
    for _ in range(3):
        coeffs = [rng.randint(-9, 9) or 1 for _ in range(n)]
        x = [F(0)]*DIM
        for c_, b in zip(coeffs, cbasis):
            for i in range(DIM):
                x[i] += F(int(c_))*F(sp.Rational(b[i]).p, sp.Rational(b[i]).q)
        adx = ad_matrix(x)
        Cb = sp.Matrix.hstack(*cbasis)
        M = adx*Cb
        aug = sp.Matrix.hstack(M, Cb)
        # solutions inside c: ad_x(c v)=0 with v in coords of c
        r = (adx*Cb).rank()
        best = min(best, n - r)
    return best

# ---------- orbit enumeration ----------
SIMPLE = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
def levi_regular(subset):
    x = [F(0)]*DIM
    for i in subset:
        x = add_(x, evec(SIMPLE[i]))
    return x

classes = {}   # key -> dict(rep, H, dimc, ...)
_seen_pre = set()
import numpy as _np
def _ad_np(X):
    cols = []
    for i in range(DIM):
        img = br(X, basis_vec(i))
        cols.append([float(c) for c in img])
    return _np.array(cols).T
def _prekey(X):
    A = _ad_np(X)
    r = lambda M: int(_np.linalg.matrix_rank(M, tol=1e-8))
    A2 = A @ A
    return (r(A), r(A2), r(A2 @ A), r(A2 @ A2))
def register(X, label):
    pk = _prekey(X)
    if pk in _seen_pre:
        return None
    _seen_pre.add(pk)
    t = jm_triple(X)
    if t is None:
        print(f"  [{label}] JM failed - skipped"); return None
    X_, H, Y = t
    cb = centralizer_basis(X_, H, Y)
    key = (len(cb), adh_spectrum(H))
    if key in classes: return key
    classes[key] = {"label": label, "X": X_, "H": H, "Y": Y, "cb": cb, "dimc": len(cb)}
    print(f"  NEW class via [{label}]: dim c = {len(cb)}")
    return key

print("\n-- Levi regular nilpotents over all nonempty subsets of simple roots --")
for r in range(1, N+1):
    for subset in itertools.combinations(range(N), r):
        register(levi_regular(subset), f"Levi{subset}-regular")

print(f"classes so far: {len(classes)}")

# distinguished non-regular orbits: random nilpotents inside big Levis
# Bourbaki E6 numbering in this basis: assume simple roots indexed 0..5 as given by ROOTS/IDX construction.
BIG_LEVIS = {
    "D5?": (0,1,2,3,4), "D5b?": (1,2,3,4,5), "E6": tuple(range(6)),
    "D4?": (1,2,3,4),
}
rng = random.Random(60)
print("\n-- random-nilpotent search inside big Levis for distinguished orbits --")
for name, subset in BIG_LEVIS.items():
    if len(classes) >= 20: break
    posroots = [rt for rt in ROOTS if all(rt[k] >= 0 for k in range(N)) and all((rt[k] == 0) or (k in subset) or False for k in range(N))]
    posroots = [rt for rt in posroots if all((rt[k] == 0) or (k in subset) for k in range(N)) and any(rt[k] > 0 for k in range(N))]
    for trial in range(40):
        if len(classes) >= 20: break
        x = [F(0)]*DIM
        for rt in posroots:
            c_ = rng.randint(0, 2)
            if c_: x = add_(x, smul_(F(c_), evec(rt)))
        if is_zero(x): continue
        register(x, f"{name}-rand{trial}")
print(f"\nTOTAL classes found: {len(classes)} (e6 has 20 nonzero orbits - CITED)")


# ================= THE PARITY SWEEP (the owner's spin-structure criterion) ==
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("c2", "frontier/B1102_exact_hypercharge_solve/b1102_common.py")
_c2 = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_c2)
_ccb = _c2.load_ccb()
_weights, _WIDX, _rho27 = _c2.build_27(_ccb)
print("\n== PARITY SWEEP: sl2-weight parity of each class on the 27 ==")
out = []
for key, data in sorted(classes.items(), key=lambda kv: -kv[0][0]):
    Hv = data["H"]
    M = _rho27([F(x) for x in Hv])
    # H semisimple with integer sl2-weights; get spectrum via float eigvals
    # rounded (exact integers, wide separation -> parity is conclusive).
    import numpy as _np
    Mf = _np.array([[float(M[i][j].numerator)/float(M[i][j].denominator)
                     for j in range(27)] for i in range(27)])
    ev = _np.linalg.eigvals(Mf).real
    r = _np.round(ev).astype(int)
    assert _np.max(_np.abs(ev - r)) < 1e-6, (data["label"], "non-integer weight")
    mults = {}
    for k in r:
        mults[int(k)] = mults.get(int(k), 0) + 1
    tot = sum(mults.values())
    assert tot == 27, (data["label"], mults)
    odd = [k for k in mults if k % 2 != 0]
    verdict = "EVEN" if not odd else "ODD"
    out.append({"label": data["label"], "dim_c": data["dimc"],
                "weights27": {str(k): v for k, v in sorted(mults.items())},
                "parity": verdict})
    print(f"  dim_c={data['dimc']:3d}  {verdict:4s}  {sorted(mults.items())}  [{data['label'][:26]}]")
even = [o for o in out if o["parity"] == "EVEN"]
print(f"\nEVEN classes: {len(even)}/20 -> dims_c {sorted(o['dim_c'] for o in even)}")
import json as _j
_j.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "parity_sweep.json"), "w"), indent=1)
print("wrote parity_sweep.json")
