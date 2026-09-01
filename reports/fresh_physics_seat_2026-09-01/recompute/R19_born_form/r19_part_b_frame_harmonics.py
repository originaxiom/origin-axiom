"""R19 blind recomputation, part (b): the Gleason harmonic core on S^2.

Claim (banked, B725 probe 3): expand a smooth frame function on S^2 in spherical
harmonics; the frame constraint  f(e1)+f(e2)+f(e3) = W  for EVERY orthonormal frame
kills every degree except l in {0, 2} (dims 1 + 5 = 6 = dim of symmetric 3x3 forms);
the frame-sum is non-constant at l = 1,3,4,5,6.  Plus dim-2 non-vacuity: h(n) = n_z^3
is a valid frame function for dim-2 frames (antipodal pairs on the Bloch sphere) that
is NOT of Born (quadratic/affine) form.

Written BLIND (before opening B725's probe scripts).  Method:
  * harmonic subspaces H_l built exactly as ker(Laplacian) on homogeneous degree-l
    polynomials (sympy, rational);
  * frame-sum F_H(R) = sum_i H(R e_i) evaluated at EXACT rational rotation matrices
    (built from rational quaternions), so "non-constant" is an exact proof;
  * constancy at l=2 proved symbolically for a general quaternion rotation;
  * key linear-algebra fact: H -> F_H is SO(3)-equivariant and H_l is irreducible,
    so constancy of F_H for one generic H decides all of H_l; we nevertheless test
    a full basis of each H_l.
  * planted-positive control: (x^2+y^2+z^2)^2 (degree-4, NOT harmonic) is constant
    on frames -- the detector must report it as a survivor, proving the l=4 kill is
    the harmonicity + frame constraint doing work, not a broken detector.
"""
import itertools
from fractions import Fraction

import sympy as sp

x, y, z = sp.symbols("x y z")
VARS = (x, y, z)
report = []


def check(name, ok, detail=""):
    report.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")


# ---------- harmonic basis of degree l, exact ----------
def monomials(l):
    return [x**a * y**b * z**(l - a - b) for a in range(l + 1) for b in range(l + 1 - a)]


def harmonic_basis(l):
    mons = monomials(l)
    if l < 2:
        return mons  # all homogeneous polys of degree 0,1 are harmonic
    lower = monomials(l - 2)
    rows = []
    for m in mons:
        lap = sp.expand(sum(sp.diff(m, v, 2) for v in VARS))
        pl = sp.Poly(lap, *VARS)
        rows.append([sp.Rational(pl.coeff_monomial(mm)) for mm in lower])
    M = sp.Matrix(rows).T  # maps coeff vectors of degree-l polys -> degree-(l-2) polys
    basis = []
    for vec in M.nullspace():
        basis.append(sp.expand(sum(c * m for c, m in zip(vec, mons))))
    return basis


# dimension check: dim H_l = 2l+1
for l in range(7):
    b = harmonic_basis(l)
    check(f"dim H_{l} = {2*l+1}", len(b) == 2 * l + 1, f"got {len(b)}")

# ---------- exact rational rotations from rational quaternions ----------
def quat_rot(q):
    w, xx, yy, zz = [sp.Rational(c) for c in q]
    n = w**2 + xx**2 + yy**2 + zz**2
    R = sp.Matrix([
        [w**2 + xx**2 - yy**2 - zz**2, 2 * (xx * yy - w * zz), 2 * (xx * zz + w * yy)],
        [2 * (xx * yy + w * zz), w**2 - xx**2 + yy**2 - zz**2, 2 * (yy * zz - w * xx)],
        [2 * (xx * zz - w * yy), 2 * (yy * zz + w * xx), w**2 - xx**2 - yy**2 + zz**2],
    ]) / n
    assert sp.simplify(R.T * R - sp.eye(3)) == sp.zeros(3, 3)
    return R

QUATS = [
    (1, 0, 0, 0),
    (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1),
    (1, 1, 1, 0), (1, 2, 0, 3), (2, 1, 3, 1),
    (1, 1, 1, 1), (3, 1, 4, 1), (2, 7, 1, 8),
    (1, -2, 3, 5), (5, 3, -2, 1),
]
ROTS = [quat_rot(q) for q in QUATS]


def frame_sum(H, R):
    """sum over the frame (columns of R) of H, exact rational."""
    tot = 0
    for i in range(3):
        col = R[:, i]
        tot += H.subs({x: col[0], y: col[1], z: col[2]}, simultaneous=True)
    return sp.cancel(sp.expand(tot))


def survives(H):
    """True iff frame-sum is the same exact rational at all sample rotations.
    Returns (constant?, set of distinct values)."""
    vals = {sp.Rational(frame_sum(H, R)) for R in ROTS}
    return len(vals) == 1, vals


# ---------- the per-degree scan ----------
surviving = {}
for l in range(7):
    basis = harmonic_basis(l)
    verdicts = []
    for H in basis:
        const, vals = survives(H)
        verdicts.append(const)
    if all(verdicts):
        surviving[l] = True
        detail = "ALL basis elements frame-constant"
    elif not any(verdicts):
        surviving[l] = False
        detail = "ALL basis elements frame-NON-constant (exact witness rotations)"
    else:
        surviving[l] = None
        detail = f"MIXED ({sum(verdicts)}/{len(verdicts)} constant) -- unexpected for irreducible H_l"
    print(f"  l={l}: survives={surviving[l]}  ({detail})")

check("only l in {0,2} survive the frame constraint",
      surviving == {0: True, 1: False, 2: True, 3: False, 4: False, 5: False, 6: False},
      f"surviving map = {surviving}")

check("surviving dimension count 1 + 5 = 6 = dim Sym(3x3)",
      len(harmonic_basis(0)) + len(harmonic_basis(2)) == 6 == 3 * 4 // 2)

# ---------- symbolic proof of the l=2 survival (general quaternion rotation) ----------
w_, a_, b_, c_ = sp.symbols("w a b c", real=True)
n_ = w_**2 + a_**2 + b_**2 + c_**2
Rq = sp.Matrix([
    [w_**2 + a_**2 - b_**2 - c_**2, 2 * (a_ * b_ - w_ * c_), 2 * (a_ * c_ + w_ * b_)],
    [2 * (a_ * b_ + w_ * c_), w_**2 - a_**2 + b_**2 - c_**2, 2 * (b_ * c_ - w_ * a_)],
    [2 * (a_ * c_ - w_ * b_), 2 * (b_ * c_ + w_ * a_), w_**2 - a_**2 - b_**2 + c_**2],
]) / n_
A = sp.Matrix(3, 3, sp.symbols("A0:3(0:3)"))
A = (A + A.T) / 2  # symmetric quadratic form
FA = sum((Rq[:, i].T * A * Rq[:, i])[0, 0] for i in range(3))
check("symbolic: frame-sum of ANY quadratic form = tr(A) for ALL rotations",
      sp.simplify(FA - sp.trace(A)) == 0)
# harmonic l=2 = trace-free quadratic forms -> frame-sum identically tr(A)=0: constant. QED l=2.

# ---------- planted-positive control ----------
plant = sp.expand((x**2 + y**2 + z**2) ** 2)  # constant (=1) on S^2, so frame-sum = 3 always
const, vals = survives(plant)
check("planted positive: (x^2+y^2+z^2)^2 detected as SURVIVOR with frame-sum 3",
      const and vals == {sp.Rational(3)}, f"values={vals}")
# and it is genuinely degree 4 but NOT harmonic:
check("plant is degree 4 and non-harmonic (so the l=4 kill is doing real work)",
      sp.total_degree(sp.Poly(plant, *VARS)) == 4
      and sp.expand(sum(sp.diff(plant, v, 2) for v in VARS)) != 0)

# a second control: a random *non*-constant combination must be flagged non-surviving
H4 = harmonic_basis(4)[0]
const, vals = survives(H4)
check("control: a generic l=4 harmonic is flagged NON-surviving (>=2 exact values)",
      (not const) and len(vals) >= 2, f"{len(vals)} distinct exact values")

# ---------- dim-2 counterexample (non-vacuity of dim>=3) ----------
# dim-2 Hilbert space: an orthonormal basis = antipodal pair {n, -n} on the Bloch sphere.
# frame constraint: h(n) + h(-n) = W.  h(n) = n_z^3 satisfies it with W = 0:
nz = sp.Symbol("n_z", real=True)
h = nz**3
check("dim-2: h(n)=n_z^3 satisfies h(n)+h(-n)=const (=0) -- valid frame function",
      sp.simplify(h + h.subs(nz, -nz)) == 0)
# but it is NOT of Born form: Born-form dim-2 frame functions are Tr(rho P) = (1 + r.n)/2,
# affine in n. n_z^3 is not affine in n (second derivative in n_z nonzero on the sphere):
check("dim-2: n_z^3 is not affine in n (not Tr(rho P)) -- Gleason genuinely needs dim>=3",
      sp.diff(h, nz, 2) != 0)

fails = [r for r in report if not r[1]]
print()
print("PART B RESULT:", "ALL PASS" if not fails else f"{len(fails)} FAILURES")
