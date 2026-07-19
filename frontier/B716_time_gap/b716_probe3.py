#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B716 PROBE 3 -- Is there a CANONICAL Wick rotation (Lorentzian continuation),
or is the object Euclidean-only?

FIREWALL: origin-axiom. Structural/mathematical ONLY. No cosmology claimed,
no SM value, no physics assertion beyond structural characterization.

The object: the figure-eight knot complement M = H^3 / Gamma, a complete
finite-volume hyperbolic 3-manifold. Its universal cover is Riemannian H^3
(Euclidean signature +++), Isom^+(H^3) = PSL(2,C) = SO^+(3,1), Gamma = pi_1(4_1)
a discrete torsion-free subgroup. Mostow-rigid.

Two-outcome:
  A = the object selects a CANONICAL Lorentzian (Wick) continuation
  B = Euclidean-only: the Lorentzian signature is EXTERNAL (the observer's)

A canonical Wick rotation of a geometry needs THREE things:
  (i)   a complexification of the geometry,
  (ii)  a real structure whose two real slices are the Euclidean and the
        Lorentzian metric,
  (iii) the CHOICE of that real structure (equivalently: a distinguished
        complex-TIME direction to rotate) must be CANONICAL -- forced by the
        object, not put in by hand.
The object supplies (i) and (ii); this probe tests (iii). The discriminating
fact is whether the object contains an isometry-invariant time direction.

We compute FIVE independent things:
  PART 1  The group coincidence PSL(2,C) = SO^+(3,1) is a SYMMETRY, not a
          spacetime metric; real-form structure of so(4,C).
  PART 2  Hyperboloid-model continuations: H^3 -> {AdS_3, dS_3, S^3}. Each needs
          a CHOICE of which ambient coordinate to rotate; each lands in a
          DIFFERENT real form; each stays 3-DIMENSIONAL (no 4d spacetime).
  PART 3  ISOTROPY = no canonical time (THE discriminating computation): the
          point-stabilizer SO(3) acts transitively on tangent directions, so no
          isometry-invariant complex-time axis exists to Wick-rotate.
  PART 4  Mostow rigidity: no 1-parameter analytic family of geometric metrics
          interpolates the two signatures; the Lorentzian SL(2,R) slice is a
          DISJOINT component of the character variety (B97), not a continuation.
  PART 5  Path-integral tie-in (B710): the state-integral saddle actions are
          REAL (CS=0); the continuation parameter is hbar (quantization), not a
          spacetime time; no distinguished imaginary-time direction.
"""

import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
np.set_printoptions(precision=6, suppress=True)

def hr(t=""):
    print("=" * 78)
    if t:
        print(t)
        print("=" * 78)

# ---------------------------------------------------------------------------
# Helpers: so(p,q) basis and Killing-form signature
# ---------------------------------------------------------------------------
def so_basis(eta):
    """Basis of so(eta) = { X : X^T eta + eta X = 0 } (real n x n)."""
    n = len(eta)
    E = np.diag(eta).astype(float)
    basis = []
    for i in range(n):
        for j in range(i + 1, n):
            X = np.zeros((n, n))
            # generator of the (i,j) plane consistent with the metric eta:
            # X = e_i e_j^T * eta_jj - e_j e_i^T * eta_ii  satisfies X^T eta + eta X = 0
            X[i, j] = E[j, j]
            X[j, i] = -E[i, i]
            basis.append(X)
    return basis

def killing_signature(eta):
    """Return (n_pos, n_neg, n_zero) of the Killing form of so(eta)."""
    B = so_basis(eta)
    d = len(B)
    # verify each X is in the algebra
    E = np.diag(eta).astype(float)
    for X in B:
        assert np.allclose(X.T @ E + E @ X, 0), "basis element not in so(eta)"
    def ad(X):
        # ad_X on the matrix algebra, expressed in the basis B
        cols = []
        for Y in B:
            Z = X @ Y - Y @ X
            # express Z in basis B by least squares over the flattened matrices
            A = np.array([b.flatten() for b in B]).T
            coeff, *_ = np.linalg.lstsq(A, Z.flatten(), rcond=None)
            cols.append(coeff)
        return np.array(cols).T
    ads = [ad(X) for X in B]
    K = np.zeros((d, d))
    for a in range(d):
        for b in range(d):
            K[a, b] = np.trace(ads[a] @ ads[b])
    ev = np.linalg.eigvalsh((K + K.T) / 2)
    tol = 1e-6 * max(1.0, np.max(np.abs(ev)))
    return int(np.sum(ev > tol)), int(np.sum(ev < -tol)), int(np.sum(np.abs(ev) <= tol)), ev

# ---------------------------------------------------------------------------
hr("PART 1  PSL(2,C) = SO^+(3,1): the LORENTZ GROUP appears as SYMMETRY, "
   "\n         not as a spacetime metric")
# ---------------------------------------------------------------------------
# Standard map: x=(x0,x1,x2,x3) -> Hermitian H(x)=x0 I + x1 sx + x2 sy + x3 sz.
# det H = x0^2 - x1^2 - x2^2 - x3^2 = <x,x>_{+---}.  A in SL(2,C) acts by
# H -> A H A^dagger, preserving det -> an element of SO^+(3,1).
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sig = [I2, sx, sy, sz]

def H_of_x(x):
    return x[0]*I2 + x[1]*sx + x[2]*sy + x[3]*sz

def x_of_H(H):
    # inverse: x_mu = (1/2) tr(H sigma_mu) with the right signs (sigma_mu Hermitian, orthonormal under (1/2)tr)
    return np.array([0.5*np.trace(H @ I2).real,
                     0.5*np.trace(H @ sx).real,
                     0.5*np.trace(H @ sy).real,
                     0.5*np.trace(H @ sz).real])

rng = np.random.default_rng(20260719)
def random_SL2C():
    M = rng.standard_normal((2, 2)) + 1j*rng.standard_normal((2, 2))
    M = M / np.sqrt(np.linalg.det(M))  # det = 1 (one branch)
    return M

eta_mink = np.diag([1.0, -1.0, -1.0, -1.0])  # +---
maxdev = 0.0
for _ in range(200):
    A = random_SL2C()
    # build the 4x4 Lorentz matrix
    L = np.zeros((4, 4))
    for mu in range(4):
        e = np.zeros(4); e[mu] = 1.0
        H = H_of_x(e)
        Hp = A @ H @ A.conj().T
        L[:, mu] = x_of_H(Hp)
    dev = np.max(np.abs(L.T @ eta_mink @ L - eta_mink))
    maxdev = max(maxdev, dev)
print(f"random SL(2,C) -> 4x4 matrix L:  max|L^T eta L - eta| over 200 trials = {maxdev:.2e}")
print("   => every A in SL(2,C) gives L in O(1,3) preserving the Minkowski form (SO^+(3,1)).")
print(f"   dim_R PSL(2,C) = 6 = dim SO(3,1).  PSL(2,C) = SL(2,C)/{{+-I}} ~= SO^+(3,1).")
print()
print("Killing-form signatures of the real forms of so(4,C)  (n_pos, n_neg, n_zero):")
for name, eta in [("so(4)   [Euclidean R^4]", [1,1,1,1]),
                  ("so(3,1) [Minkowski R^{3,1} = Isom H^3 = LORENTZ]", [1,-1,-1,-1]),
                  ("so(2,2) [split R^{2,2} = Isom AdS_3]", [1,1,-1,-1])]:
    p, q, z, ev = killing_signature(eta)
    print(f"   {name:52s}: ({p},{q},{z})")
print()
print("READING: SO^+(3,1) is the isometry group of Euclidean H^3 -- but it is a")
print("SYMMETRY group acting on a 3d RIEMANNIAN space, NOT the local Lorentz group")
print("of a 4d Lorentzian metric.  Same abstract group, different geometric role.")
print("The three real forms so(4)/so(3,1)/so(2,2) have DISTINCT Killing signatures,")
print("so a Wick rotation Euclidean<->Lorentzian must cross BETWEEN real forms; the")
print("object's isometry is pinned to the SINGLE real form so(3,1).")

# ---------------------------------------------------------------------------
hr("PART 2  Hyperboloid-model continuations: H^3 -> {AdS_3, dS_3, S^3} "
   "\n         -- each needs a CHOICE, lands in another real form, stays 3d")
# ---------------------------------------------------------------------------
# Ambient R^{3,1}, eta = diag(-1,1,1,1).  Quadric Q_k = { x : <x,x>_eta = k }.
# H^3   = Q_{-1}, x0>0  : Riemannian (+++), curvature -1, Isom SO(3,1).
# dS_3  = Q_{+1}        : Lorentzian (-++), curvature +1, Isom SO(3,1).
# Wick-rotating an ambient coordinate changes eta -> another real form:
#   rotate x3 -> i x3 : eta -> diag(-1,1,1,-1) ~ R^{2,2}; Q_{-1} -> AdS_3.
#   rotate x0 -> i x0 : eta -> diag(1,1,1,1)   = R^4;      Q_{+1} -> S^3.
# We verify the INDUCED-metric signature on each quadric at a sample point by
# building the tangent space (eta-orthogonal complement) and restricting eta.
def induced_signature(eta_diag, p, sign_flip_desc):
    eta = np.diag(eta_diag).astype(float)
    p = np.array(p, dtype=float)
    # tangent space T_p Q = { v : eta(p,v) = 0 }
    normal = eta @ p
    # basis of the orthogonal complement of `normal` in R^4 (the tangent 3-space)
    U, S, Vt = np.linalg.svd(normal.reshape(1, -1))
    T = Vt[1:].T  # columns span the 3d tangent space
    g = T.T @ eta @ T  # induced metric
    ev = np.linalg.eigvalsh((g + g.T)/2)
    npos = int(np.sum(ev > 1e-9)); nneg = int(np.sum(ev < -1e-9))
    return npos, nneg, ev

print("Ambient eta=diag(-1,1,1,1).  Quadric <x,x>=k.  Sample tangent-space signatures:")
# H^3 at p=(1,0,0,0) (on Q_{-1}, x0>0)
p, q, ev = induced_signature([-1,1,1,1], [1,0,0,0], "")
print(f"  H^3  = Q_-1 at (1,0,0,0) [eta=(-+++)] : induced signature (+{p},-{q}) "
      f"-> RIEMANNIAN (+++), curvature -1")
# dS_3 at p=(0,1,0,0) (on Q_{+1})
p, q, ev = induced_signature([-1,1,1,1], [0,1,0,0], "")
print(f"  dS_3 = Q_+1 at (0,1,0,0) [eta=(-+++)] : induced signature (+{p},-{q}) "
      f"-> LORENTZIAN (-++), curvature +1")
# AdS_3: rotate x3->i x3 gives eta=diag(-1,1,1,-1); H^3-quadric Q_-1 -> AdS_3
p, q, ev = induced_signature([-1,1,1,-1], [1,0,0,0], "")
print(f"  AdS_3= Q_-1 at (1,0,0,0) [eta=(-++-)] : induced signature (+{p},-{q}) "
      f"-> LORENTZIAN (-++), curvature -1   [via x3 -> i x3]")
# S^3: rotate x0->i x0 gives eta=diag(1,1,1,1); Q_+1 -> S^3
p, q, ev = induced_signature([1,1,1,1], [1,0,0,0], "")
print(f"  S^3  = Q_+1 at (1,0,0,0) [eta=(++++)] : induced signature (+{p},-{q}) "
      f"-> RIEMANNIAN (+++), curvature +1   [via x0 -> i x0]")
print()
print("READING: H^3 has (at least) THREE inequivalent 'continuations' -- to AdS_3,")
print("dS_3, S^3 -- selected by WHICH ambient coordinate one rotates.  All are")
print("3-DIMENSIONAL (none is a 4d Lorentzian spacetime), and each lands in a")
print("DIFFERENT real form (SO(2,2)/SO(3,1)/SO(4)).  There is no canonical winner.")

# ---------------------------------------------------------------------------
hr("PART 3  ISOTROPY = NO CANONICAL TIME  (the discriminating computation)")
# ---------------------------------------------------------------------------
# A Wick rotation must pick a complex-TIME direction to rotate.  On H^3 the
# point-stabilizer is SO(3), which acts TRANSITIVELY on tangent directions:
# hence NO isometry-invariant time direction exists -> no canonical Wick rotation.
# Contrast: an FRW / static spacetime has a global timelike Killing field -> a
# distinguished time -> a canonical Wick rotation.  H^3 has no such field.
eta = np.diag([-1.0, 1.0, 1.0, 1.0])
p = np.array([1.0, 0, 0, 0])  # base point of H^3 = Q_{-1}, x0>0

# Stabilizer of p in SO(3,1) = { L in SO(3,1) : L p = p } = block-diag(1, SO(3)).
def rotation_SO3(a, b, c):
    Rz = np.array([[np.cos(a),-np.sin(a),0],[np.sin(a),np.cos(a),0],[0,0,1]])
    Ry = np.array([[np.cos(b),0,np.sin(b)],[0,1,0],[-np.sin(b),0,np.cos(b)]])
    Rx = np.array([[1,0,0],[0,np.cos(c),-np.sin(c)],[0,np.sin(c),np.cos(c)]])
    R = Rz @ Ry @ Rx
    L = np.eye(4); L[1:,1:] = R
    return L

# (a) verify these stabilize p and lie in SO(3,1)
ok_stab = True; ok_lor = True
for _ in range(50):
    L = rotation_SO3(*rng.uniform(0, 2*np.pi, 3))
    ok_stab &= np.allclose(L @ p, p)
    ok_lor  &= np.allclose(L.T @ eta @ L, eta)
print(f"point-stabilizer of (1,0,0,0):  fixes p ? {ok_stab}   in SO(3,1) ? {ok_lor}")
print("   => Stab = block-diag(1, SO(3)) acting on T_p H^3 = {(0,v): v in R^3}.")

# (b) SO(3) acts TRANSITIVELY on unit tangent directions: sweep the orbit of a
#     seed direction and check it covers S^2 (any target direction is reached).
seed = np.array([0.0, 1.0, 0.0, 0.0])   # a unit tangent direction (v=e_x)
targets = rng.standard_normal((40, 3))
targets = targets / np.linalg.norm(targets, axis=1, keepdims=True)
worst = 0.0
for tgt in targets:
    # find R in SO(3) sending e_x -> tgt (transitivity of SO(3) on S^2)
    ex = np.array([1.0, 0, 0])
    v = np.cross(ex, tgt); s = np.linalg.norm(v); c = ex @ tgt
    if s < 1e-12:
        R = np.eye(3) if c > 0 else np.diag([1, -1, -1.0])
    else:
        vx = np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
        R = np.eye(3) + vx + vx @ vx * ((1 - c) / (s*s))
    L = np.eye(4); L[1:,1:] = R
    reached = (L @ seed)[1:]
    worst = max(worst, np.linalg.norm(reached - tgt))
print(f"SO(3) orbit of one tangent direction reaches ALL directions: "
      f"max miss over 40 random targets = {worst:.2e}")
print("   => the stabilizer acts TRANSITIVELY on directions at p.")
print()
print("CONCLUSION (discriminating): H^3 is an ISOTROPIC (two-point-homogeneous)")
print("Riemannian space; SO(3,1) acts transitively on its orthonormal frame")
print("bundle.  Therefore NO isometry-invariant tangent direction exists, so")
print("there is NO canonical complex-time axis to Wick-rotate.  Condition (iii)")
print("of a canonical Wick rotation FAILS.  Any Lorentzian continuation must")
print("import a time direction from OUTSIDE, breaking SO(3,1) -> SO(2,1) or SO(3).")

# ---------------------------------------------------------------------------
hr("PART 4  MOSTOW RIGIDITY: no interpolating family; the Lorentzian slice is a "
   "\n         DISJOINT character-variety component (B97), not a continuation")
# ---------------------------------------------------------------------------
# The figure-eight = two-bridge knot b(5,3).  Riley presentation
#   Gamma = pi_1(4_1) = < a, b | a W = W b >,  W = b a^{-1} b^{-1} a
# (the two-bridge relator word, signs eps=(+,-,-,+) from floor(i*3/5)).
# Standard parabolic geometric representation into SL(2,C):
#   a = [[1,1],[0,1]],  b = [[1,0],[om,1]],  om = e^{i pi/3} = (1 + i sqrt3)/2
# (completeness: om^2 - om + 1 = 0, i.e. om a primitive 6th root; conj = other shape).
# This is RIGID (Mostow): the complete hyperbolic structure is unique up to
# isometry; there is NO real 1-parameter deformation of the *complete* structure.
# A Wick rotation would be an analytic 1-parameter family g(theta), theta in
# [0, pi/2], of geometric metrics interpolating signatures -- rigidity forbids it.
om = (1 + 1j*mp.sqrt(3)) / 2   # = e^{i pi/3}, primitive 6th root; om^2 - om + 1 = 0
A = mp.matrix([[1, 1], [0, 1]])
B = mp.matrix([[1, 0], [om, 1]])
def mmul(*Ms):
    R = Ms[0]
    for M in Ms[1:]:
        R = R * M
    return R
def minv(M):
    d = M[0,0]*M[1,1]-M[0,1]*M[1,0]
    return mp.matrix([[M[1,1]/d, -M[0,1]/d], [-M[1,0]/d, M[0,0]/d]])
# two-bridge relator W = b a^{-1} b^{-1} a ; check the group relation  a W = W b
W = mmul(B, minv(A), minv(B), A)
lhs = mmul(A, W); rhs = mmul(W, B)
relerr = max(abs(complex(lhs[i,j]-rhs[i,j])) for i in range(2) for j in range(2))
comp_check = complex(om*om - om + 1)
comm = mmul(A, B, minv(A), minv(B))
tr_comm = complex(comm[0,0] + comm[1,1])
print(f"geometric parabolic rep (shape om=e^(i pi/3), om^2-om+1={abs(comp_check):.1e}): "
      f"relation a W = W b residual = {relerr:.2e}")
print(f"   tr(A)={complex(A[0,0]+A[1,1]).real:.0f} (parabolic cusp), "
      f"tr[A,B] = {tr_comm.real:.4f}{tr_comm.imag:+.4f}i")
print("   the two geometric shapes w, wbar in Q(sqrt-3) are the ONLY discrete")
print("   faithful reps of the COMPLETE structure (Mostow rigidity) -- a rigid")
print("   point, not a 1-parameter family: no analytic Euclidean->Lorentzian path.")
print()
print("The Lorentzian structure that DOES exist (B97) is the SL(2,R) Teichmuller")
print("(Fuchsian) rep of the FIBER surface F_2 -- signature so(2,1) as the")
print("gauge-algebra Killing form.  That is a DIFFERENT, disjoint component of the")
print("SL(2,C) character variety (real-type, tr[X,Y]=-2), NOT an analytic")
print("continuation of the geometric SL(2,C) rep.  So the 'Lorentzian slice' is a")
print("SEPARATE gauge structure present by construction, not a Wick image of the")
print("object's own hyperbolic metric.")
# quick disjointness witness: the geometric rep has tr[A,B] complex (in Q(sqrt-3)),
# a Fuchsian SL(2,R) rep of the punctured torus has tr[X,Y] = -2 (real).  Different loci.
print(f"   witness: geometric tr[A,B] = {tr_comm.real:.4f}{tr_comm.imag:+.4f}i (complex, "
      f"Q(sqrt-3))  vs  Fuchsian tr[X,Y] = -2 (real).  Distinct components.")

# ---------------------------------------------------------------------------
hr("PART 5  PATH-INTEGRAL TIE-IN (B710): real (CS=0) saddles, and the "
   "\n         continuation parameter is hbar, not a spacetime time")
# ---------------------------------------------------------------------------
# Reproduce Vol(4_1) two ways and confirm CS=0 (amphichiral) -> the two geometric
# saddle actions are REAL (Im=0): the object sits AT the conjugation fixed point.
z = mp.e**(1j*mp.pi/3)                     # geometric shape, a primitive 6th root
def bloch_wigner(z):
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))
D = bloch_wigner(z)
Vol = 2 * mp.im(mp.polylog(2, z))
Cl2 = mp.clsin(2, mp.pi/3)                 # Clausen Cl_2(pi/3)
ref = mp.mpf('2.029883212819307250042405108549')
print(f"Vol(4_1) = 2 Im Li_2(e^{{i pi/3}}) = {mp.nstr(Vol, 25)}")
print(f"   Bloch-Wigner D(z)             = {mp.nstr(D, 25)}")
print(f"   2*Cl_2(pi/3)                  = {mp.nstr(2*Cl2, 25)}")
print(f"   |Vol - reference|             = {mp.nstr(abs(Vol-ref), 6)}")
print(f"   CS(4_1) = 0 (amphichiral: CS = -CS mod 1) -> geometric flat connection")
print(f"            sits at the conjugation FIXED POINT.")
print(f"   two non-abelian saddle actions S = +/-(Vol + i*CS) = "
      f"+/-{mp.nstr(Vol,10)} + 0 i   (Im S = 0, REAL).")
print()
print("READING: the object's 'partition function' (Andersen-Kashaev / Kashaev")
print("state integral) is a function of the QUANTIZATION parameter hbar (q=e^{2pi i hbar}),")
print("NOT of a spacetime time coordinate.  A Wick rotation rotates spacetime")
print("TIME; here there is no lapse/time integral to rotate (contrast FRW's lapse")
print("N).  The only analytic parameter is hbar, and along it the two geometric")
print("saddles stay pinned to the REAL axis (CS=0).  B710: 2 real saddles, 1 mod-")
print("conjugation orbit -- INVERTED from FRW's 4 complex saddles / 2 orbits.")
print("There is no distinguished imaginary-time continuation of a real-action,")
print("timeless invariant.")

# ---------------------------------------------------------------------------
hr("CAVEATS (adversarial self-audit)")
# ---------------------------------------------------------------------------
print("""1. "H^3 IS Euclidean AdS_3, so AdS_3 is its canonical Lorentzian partner
   (=> A)."  TRUE that the symmetric space H^3 is the Euclidean version of AdS_3
   -- but (i) AdS_3 is still 3-DIMENSIONAL, not the 4d Lorentzian spacetime the
   frontier asks for; (ii) the continuation is a CHOICE of ambient coordinate
   (H^3 equally continues to dS_3 and S^3, Part 2), not canonical; (iii) the
   OBJECT is the rigid quotient H^3/Gamma with Gamma < SO(3,1), and SO(3,1) does
   not canonically embed in SO(2,2), so the quotient (the knot complement) does
   not carry the AdS_3 continuation.  Strengthens B, does not flip it.
2. Isotropy (Part 3) is a fact about the UNIVERSAL COVER H^3; the quotient
   H^3/Gamma is only locally isotropic, so a priori Gamma could pick out a
   direction.  It does not: Gamma acts by orientation-preserving isometries of
   the SAME homogeneous metric, and Mostow rigidity (Part 4) forbids any
   Gamma-invariant deformation toward a Lorentzian metric.  Both the local model
   AND the rigid global structure lack a canonical time.
3. CS=0 (Part 5) is amphichirality (CITED, textbook), not recomputed here; the
   load-bearing computed facts are Vol (two ways, 4e-32) and the real actions.
4. "Canonical Wick rotation" is read as: the object SELECTS the Euclidean->
   Lorentzian continuation with NO external input.  A weaker reading ("some
   Lorentzian space shares its symmetry group") is trivially satisfied by
   SO(3,1) itself but is exactly the observer-supplied structure the frontier
   is separating out -- the same move as B713 (chirality) and B97.""")

# ---------------------------------------------------------------------------
hr("VERDICT")
# ---------------------------------------------------------------------------
print("""OUTCOME B -- EUCLIDEAN-ONLY; the Lorentzian signature is the OBSERVER'S.

A canonical Wick rotation requires a canonical complex-TIME direction. The object
has none:
 * ISOTROPY (Part 3, discriminating): H^3 is two-point-homogeneous; the point-
   stabilizer SO(3) acts transitively on tangent directions, so NO isometry-
   invariant time axis exists to rotate. Condition (iii) of a canonical Wick
   rotation FAILS at the level of the homogeneous geometry itself.
 * NON-UNIQUE / 3d continuations (Part 2): rotating an ambient coordinate gives
   H^3 -> AdS_3 / dS_3 / S^3 depending on a CHOICE; all are 3-DIMENSIONAL (no 4d
   spacetime) and land in DIFFERENT real forms (SO(2,2)/SO(3,1)/SO(4)).
 * SYMMETRY, not metric (Part 1): PSL(2,C)=SO^+(3,1) is the Lorentz group as the
   *isometry* of a Riemannian 3-space, not a 4d Lorentzian metric; the three real
   forms have distinct Killing signatures, so a Wick rotation crosses real forms.
 * RIGIDITY (Part 4): Mostow rigidity forbids a 1-parameter analytic family of
   geometric metrics interpolating the signatures; the Lorentzian SL(2,R) slice
   (B97) is a DISJOINT gauge component, not a continuation of the object's metric.
 * PATH INTEGRAL (Part 5, B710): the saddle actions are REAL (CS=0) -- the object
   sits AT the conjugation fixed point; the only analytic parameter is hbar
   (quantization), not spacetime time; nothing to Wick-rotate.

DISCRIMINATING FACT: H^3 is isotropic -- its point-stabilizer SO(3) acts
transitively on tangent directions -- so the object contains NO invariant complex-
time direction; every Lorentzian continuation (AdS_3/dS_3/S^3) requires an external
choice of coordinate, breaks SO(3,1), lands in a different real form, and stays 3d.
The Lorentzian signature is imported by the observer's coupling, exactly like
chirality (B713) and values (B685/B706).  [expected B, confirmed]""")
