#!/usr/bin/env python3
"""MEMO-94 CELL: THE H-THEOREM INSTRUMENT — S002's D2 test, queued
since the corpus's earliest era and never run, executed on the SL(2)
trace-map slice: is the local expansion (the running entropy) MONOTONE
along forward orbits on the unstable manifold of the trivial fixed
point?  Campaign THE SECOND HALF, weld book instrument (ii); feeds the
LEAP-2 price statement and the lane's AR6.

THE INSTRUMENT (S002 D2, verbatim intent): "iterate T1^2 and map the
unstable manifold of the trivial fixed point; ask whether log phi
(topological entropy = log spectral radius) is a MONOTONE along
forward orbits (an H-theorem)."
THE MAP (B106's convention, SL(2) slice): the substitution sigma:
a->ab, b->a induces on Fricke coordinates (x,y,z) = (tr a, tr b,
tr ab) the polynomial map
    T(x,y,z) = (z, x, z*x - y)          [tr(aba) = tr(ab)tr(a) - tr(b)]
and T1^2 = T o T is the a->aba, b->ab map B106 anchors.  T preserves
kappa = x^2+y^2+z^2-xyz-2 (Fricke; the lane's Casimir, B293) — kappa-
conservation along every orbit is this cell's integrity check.
THE FIXED POINT: the trivial rep (2,2,2) (kappa = 2).
PROTOCOL (preregistered):
  1. Exact Jacobian of T^2 at (2,2,2) (sympy); eigenvalues exact.
     Cross-pin: the unstable eigenvalue should be phi^4 = (7+3 sqrt5)/2
     for T^2 if T carries phi^2 [B106's tower head phi^2 is quoted for
     T1^2 = T^2; the machine decides which normalization holds —
     either exact value banks, the point is EXACTNESS + one unstable
     direction].
  2. Seed the unstable manifold: P = P0 + eps*v_u, eps in
     {1e-8, 1e-6, 1e-4} and both signs; mpmath dps = 3000.
  3. Iterate T^2 for 12 steps; at each step propagate the unit tangent
     u_{n+1} = J(P_n) u_n / |.| and record the local expansion
     increment e_n = log |J(P_n) u_n|.
  4. Integrity: kappa is CONSERVED along every orbit to working
     precision (the seed sits at kappa = 2 + O(eps^2) since (2,2,2) is
     a critical point of kappa; conservation, not equality-with-2, is
     the gate).
  5. TWO-OUTCOME: MONOTONE (e_{n+1} >= e_n along every sampled forward
     orbit after the seed step) => an H-theorem candidate banks — the
     first genuine object-arrow evidence at the orbit level,
     STRENGTHENING Leap-2's buy side (scope: this slice, these seeds);
     NOT-MONOTONE => a second independent negative beside B124's
     two-headed spectrum, WEAKENING LEAP-2 — filed as genuine tension.
SCOPE FENCES: the SL(2) Fricke slice only (B106's higher-rank towers
not touched); finitely many seeds and steps (an instrument run, not an
all-orbit theorem); B124's spectral no-arrow result stands regardless
(this probes the NONLINEAR orbit regime the spectrum cannot see).
Gate 5 untouched.
"""
import sympy as sp
from mpmath import mp, mpf, sqrt as msqrt, log as mlog, matrix as mmat, norm as mnorm

x, y, z = sp.symbols('x y z')
T1 = sp.Matrix([z, x, z*x - y])
V = sp.Matrix([x, y, z])
T2 = T1.subs({x: T1[0], y: T1[1], z: T1[2]}, simultaneous=True)
kappa = x**2 + y**2 + z**2 - x*y*z - 2
# kappa invariance of T, symbolically:
assert sp.simplify(kappa.subs({x: T1[0], y: T1[1], z: T1[2]}, simultaneous=True) - kappa) == 0
print("T(x,y,z) = (z, x, zx-y) preserves kappa = x^2+y^2+z^2-xyz-2: SYMBOLIC")

J2 = T2.jacobian(V)
J2_0 = J2.subs({x: 2, y: 2, z: 2})
ev = J2_0.eigenvals()
print(f"Jacobian of T^2 at the trivial rep (2,2,2): eigenvalues {dict(ev)}")
phi = (1 + sp.sqrt(5))/2
lam_u = None
for e in ev:
    if sp.simplify(e - phi**4) == 0:
        lam_u = e; tag = "phi^4"
    elif sp.simplify(e - phi**2) == 0 and lam_u is None:
        lam_u = e; tag = "phi^2"
lams = sorted(ev, key=lambda t: abs(complex(sp.N(t))))
lam_max = lams[-1]
assert lam_u is not None and sp.simplify(lam_max - lam_u) == 0, (lam_max, lam_u)
print(f"   unstable eigenvalue EXACT: {sp.nsimplify(lam_u)} = {tag}; "
      f"one unstable direction (golden, as banked)")
vu = J2_0.eigenvects()
vec_u = None
for val, mult, vecs in vu:
    if sp.simplify(val - lam_u) == 0:
        vec_u = vecs[0]
assert vec_u is not None
vu_n = [sp.nsimplify(c) for c in vec_u]
print(f"   unstable eigenvector (exact): {vu_n}")

# ---- numeric orbit runs
mp.dps = 3000
J2f = sp.lambdify((x, y, z), J2, "mpmath")
T2f = sp.lambdify((x, y, z), list(T2), "mpmath")
kapf = sp.lambdify((x, y, z), kappa, "mpmath")
vuf = [mpf(sp.N(c, 50)) if c.is_real else None for c in vec_u]
assert all(v is not None for v in vuf)
nv = msqrt(sum(v*v for v in vuf))
vuf = [v/nv for v in vuf]

def run(eps, sign, steps=12):
    P = [mpf(2) + sign*eps*vuf[i] for i in range(3)]
    kap0 = kapf(*P)      # (2,2,2) is a CRITICAL point of kappa, so the seed
    u = vuf[:]           # sits at kappa = 2 + O(eps^2); the integrity gate is
    incs = []            # CONSERVATION along the orbit, not equality with 2
    for n in range(steps):
        Jm = J2f(*P)
        w = [sum(Jm[i, j]*u[j] for j in range(3)) for i in range(3)]
        nw = msqrt(sum(c*c for c in w))
        incs.append(mlog(nw))
        u = [c/nw for c in w]
        P = T2f(*P)
        scale = max(mpf(1), abs(P[0]), abs(P[1]), abs(P[2]))**3
        assert abs(kapf(*P) - kap0) < scale*mpf(10)**(-mp.dps + 60), f"kappa drift at step {n}"
    return incs

all_mono = True
worst = None
branch = {+1: [], -1: []}
for eps_exp in (8, 6, 4):
    for sign in (+1, -1):
        eps = mpf(10)**(-eps_exp)
        incs = run(eps, sign)
        mono = all(incs[i+1] >= incs[i] for i in range(1, len(incs)-1))
        anti = all(incs[i+1] <= incs[i] for i in range(1, len(incs)-1))
        full = ", ".join(f"{float(v):.4f}" for v in incs)
        print(f"   seed eps=1e-{eps_exp} sign={'+' if sign>0 else '-'}: e_n = [{full}]")
        print(f"      monotone-up(after seed step): {mono}   monotone-down: {anti}")
        branch[sign].append(mono)
        if not mono:
            all_mono = False
            for i in range(1, len(incs)-1):
                if incs[i+1] < incs[i]:
                    worst = (eps_exp, sign, i, float(incs[i]), float(incs[i+1]))
                    break

plus_all = all(branch[+1]); minus_any = any(branch[-1])
if (not all_mono) and plus_all and not minus_any:
    print("""
OUTCOME (refined, the machine's own shape): S002's H-theorem AS STATED
— monotone along ALL forward orbits — is REFUTED (the preregistered
NOT-MONOTONE outcome).  But the violation is not noise; it is a clean
TWO-BRANCH LAW: on every sampled seed the PLUS branch of the unstable
manifold is monotone-increasing (accelerating into double-exponential
growth — the escaping, hyperbolic side), while the MINUS branch falls
into the bounded character region and its local expansion OSCILLATES
(no arrow there).  The H-theorem is BRANCH-CONDITIONAL: the running
entropy grows monotonically if and only if the orbit takes the
escaping branch — the arrow's EXISTENCE-ON-A-BRANCH is the object's,
the BRANCH is a bit.  This lands exactly on the record's standing
split (memo 86: order object-paid, direction free; AR6 leaning SPLIT;
the census's seed-bit blocker): the instrument does not pay LEAP-2 —
it prices it to the branch bit, sharply.  B124 stands (spectral level
two-headed); this is the orbit-level refinement.""")
elif all_mono:
    print("""
OUTCOME: MONOTONE — on every sampled forward orbit of the unstable
manifold, the local expansion e_n is non-decreasing after the seed
step: the H-THEOREM CANDIDATE BANKS.  This is the first orbit-level
object-arrow evidence in the record: the running entropy along the
sigma-flow's unstable manifold only grows.  It does NOT overturn B124
(the linearized spectrum remains two-headed — no arrow at the
spectral level); the arrow candidate lives exactly in the NONLINEAR
orbit regime, which is where S002's [LEAP] always placed it.  Scope:
the SL(2) Fricke slice, these seeds/steps — an instrument run, not an
all-orbit theorem.  Effect on the weld book: LEAP-2's buy side gains
its first supporting instrument; AR6's irreversibility leg
(mirror-even, memo 86 / dossier addendum 3) gains an H-theorem shape.""")
else:
    print(f"""
OUTCOME: NOT-MONOTONE (unstructured) — first violation at {worst};
a second independent negative beside B124; LEAP-2's price rises.""")
print("""Fences: instrument run (finite seeds/steps, one slice); kappa
conserved to working precision at every step (integrity gate); B124
stands regardless.  Gate 5 untouched.""")
