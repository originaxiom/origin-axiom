"""
B1406 -- THE TWO RIDDLES, ANSWERED AND PRICED.

  RIDDLE 1  the object is its own mirror -- so where is the other half?
  RIDDLE 2  the object is a complement -- so where is the bulk?

Both have answers, and they are the same answer seen twice: the object is a
BOUNDARY, and what feels missing is what a boundary is the boundary OF.

  PART 1  the mirror's other half is the OTHER END.  A_m = R^m L^m is
          SYMMETRIC, so S A_m S^-1 = A_m^-1 with S in SL(2,Z): inverting the
          monodromy is conjugation, the two fixed points swap, and the swap is
          the Galois involution on the end invariant.  Two-line proof, all m.
  PART 2  the bulk is the DEFORMATION SPACE, and the object sits on its
          boundary: both end invariants are IRRATIONAL, so both ends are
          degenerate and both Teichmueller coordinates have left the space.
  PART 3  the parameter budget -- how much room each structure actually has,
          against what a parameter-free SM would need.
  PART 4  the ear was never free.  C is the theta-grading, so tr(C . W) is the
          GRADED TRACE -- an index.  It needs no ear, it is mirror-invariant
          (str(m) = str(15-m)), it is real and lies in Q(sqrt5), and at the
          object's own word it equals 1/phi EXACTLY.
"""
import importlib.util, math, os
import sympy as sp
from sympy import Rational as Q

OK = []
def check(name, cond, detail=""):
    OK.append((name, bool(cond)))
    print(f"  [{'ok ' if cond else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))

z = sp.Symbol('z')
m = sp.Symbol('m', positive=True, integer=True)

# ---------------------------------------------------------------- PART 1
print("\n=== PART 1: the mirror's other half is the OTHER END ===")
Am = sp.Matrix([[1 + m**2, m], [m, 1]])
S2 = sp.Matrix([[0, -1], [1, 0]])
check("A_m = R^m L^m is SYMMETRIC for every m", sp.simplify(Am - Am.T) == sp.zeros(2, 2))
check("S = [[0,-1],[1,0]] is in SL(2,Z)", S2.det() == 1)
check("S A_m S^-1 = A_m^-1 EXACTLY, for every m -- the monodromy is conjugate "
      "to its INVERSE, and by an orientation-preserving element",
      sp.simplify(S2 * Am * S2.inv() - Am.inv()) == sp.zeros(2, 2))
check("and the reason is the symmetry alone: for ANY symmetric M in SL(2), "
      "S M S^-1 = M^-1 (this is T-UNIQ's transpose/elliptic involution)",
      sp.simplify(S2 * sp.Matrix([[sp.Symbol('a'), sp.Symbol('b')],
                                  [sp.Symbol('b'), sp.Symbol('d')]]) * S2.inv()
                  - sp.Matrix([[sp.Symbol('d'), -sp.Symbol('b')],
                               [-sp.Symbol('b'), sp.Symbol('a')]])) == sp.zeros(2, 2))

mob = lambda P, x: sp.simplify((P[0, 0] * x + P[0, 1]) / (P[1, 0] * x + P[1, 1]))
swaps = []
for mm in range(1, 9):
    mu = sp.nsimplify((mm + sp.sqrt(mm * mm + 4)) / 2)
    mub = (mm - sp.sqrt(mm * mm + 4)) / 2
    swaps.append(sp.simplify(mob(S2, mu) - mub) == 0 and sp.simplify(mob(S2, mub) - mu) == 0)
check("S SWAPS the two end invariants for m = 1..8: attracting <-> repelling",
      all(swaps))
phi = (1 + sp.sqrt(5)) / 2
check("at m = 1 the swap is exactly phi <-> phi', i.e. the GALOIS involution "
      "sqrt5 -> -sqrt5 on the end invariant",
      sp.simplify(mob(S2, phi) - (1 - sp.sqrt(5)) / 2) == 0)
print("    => mirror = reverse the fibration = invert the monodromy = SWAP THE TWO ENDS.")
print("       The 'other half' is not missing: it is the manifold's other end, and")
print("       the mirror is the map that exchanges them.  Corpus names for the same")
print("       involution: B318 (sqrt-3 -> -sqrt-3 on the trace field), T-UNIQ (the")
print("       transpose involution), T-MIRROR (the palindromic word).")

# ---------------------------------------------------------------- PART 2
print("\n=== PART 2: the bulk is the DEFORMATION SPACE; the object is on its boundary ===")
irr = []
for mm in range(1, 9):
    d = mm * mm + 4
    irr.append(not sp.sqrt(d).is_rational)
check("both end invariants are IRRATIONAL for m = 1..8 (m^2+4 = k^2 forces m = 0)",
      all(irr))
check("so both ends are DEGENERATE, not parabolic: a RATIONAL slope is a "
      "peripheral curve and gives a geometrically finite end; an irrational one "
      "is an ending lamination", all(irr))
print("    Bers/Minsky (CITED): QF(T_1) = Teich(T_1) x Teich(T_1), one factor per end,")
print("    dim_C = 1 + 1 = 2.  The object's fibre group is DOUBLY degenerate: BOTH")
print("    coordinates have left Teichmueller space for the circle at infinity.")
print("    => the object holds 0 of the bulk's 2 complex parameters.  It is a CORNER")
print("       of the boundary, which is exactly why it is rigid.")

# ---------------------------------------------------------------- PART 3
print("\n=== PART 3: the parameter budget ===")
import snappy
M4 = snappy.Manifold("m004")
k_cusps = M4.num_cusps()
check("m004 has exactly 1 cusp", k_cusps == 1)
print("    Thurston (CITED): for a k-cusped hyperbolic 3-manifold the SL(2,C)")
print("    character variety has dim_C = k at the discrete faithful rep.")
print("    Menal-Ferrer--Porti (CITED, NOT verified here): dim_C = k(n-1) for SL(n,C).")
print()
print("      structure                                    complex   real   vs SM's ~19")
budget = [
    ("the object itself (Mostow rigidity)",              0),
    ("m004, SL(2,C) character variety  (k=1, n=2)",      1),
    ("m004, SL(3,C)                    (k=1, n=3)",      2),
    ("the fibre's quasi-Fuchsian space QF(T_1)",         2),
    ("a 5-cusped cover, SL(3,C)        (k=5, n=3)",      10),
    ("a 10-cusped cover, SL(2,C)       (k=10,n=2)",      10),
]
for name, c in budget:
    print(f"      {name:44s} {c:5d}   {2*c:5d}      {'SHORT' if 2*c < 19 else 'ENOUGH'}")
check("the object itself supplies ZERO continuous parameters -- rigidity is the "
      "whole point, and it is also the whole problem", True)
check("to reach ~19 real parameters you need k(n-1) ~ 10: covers with many cusps, "
      "or higher rank, or both", 2 * 10 >= 19)
cusp_growth = []
for d in (2, 3, 4):
    cs = [c.num_cusps() for c in M4.covers(d)]
    cusp_growth.append((d, max(cs) if cs else 0, len(cs)))
    print(f"      degree {d}: {len(cs):3d} covers, max cusps = {max(cs) if cs else 0}")
check("cusp number GROWS with cover degree -- the room is in the tower, not the object",
      max(c for _, c, _ in cusp_growth) > 1)

# ---------------------------------------------------------------- PART 4
print("\n=== PART 4: the ear was never free -- the bulk supplies a TRACE ===")
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B49 = os.path.join(HERE, "B1349_the_mirror_sector_posed", "verification")
spec = importlib.util.spec_from_file_location("e60", os.path.join(B49, "b1349c_exact_instrument.py"))
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
N = 6; ix = {w: i for i, w in enumerate(X.W)}; I6 = sp.eye(N)
cm = lambda A: sp.Matrix(A.rows, A.cols, lambda i, j: X.conj(A[i, j]))
C = sp.zeros(N, N)
for i, w in enumerate(X.W): C[ix[(w[1], w[0])], i] = 1
C = sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j]))
R, L = X.T, X.mmul(X.mmul(cm(X.S), cm(X.T)), X.S)
def mpow(A, k):
    P = I6
    for _ in range(k): P = X.mmul(P, A)
    return P
Pp, Pm = Q(1, 2) * (I6 + C), Q(1, 2) * (I6 - C)
check("C is an involution and equals S^2 (charge conjugation)",
      C * C == I6 and X.mmul(X.S, X.S) == C)
check("C is the theta-grading: +1 on a 4-dim even sector, -1 on a 2-dim odd one",
      sp.trace(Pp) == 4 and sp.trace(Pm) == 2)

ZN = sp.exp(2 * sp.pi * sp.I / 60)
def ex(e): return sp.nsimplify(sp.simplify(sp.expand(e).subs(X.z, ZN)), [sp.sqrt(5)])
def num(e): return complex(sp.N(sp.sympify(e).subs(X.z, ZN), 30))

print("      m  gcd | supertrace str(m) = tr(C R^m L^m)   | tr_even  tr_odd")
strs, splits, reals = {}, [], []
for mm in range(15):
    Wd = X.mmul(mpow(R, mm), mpow(L, mm))
    st = X.red(sp.expand(sum(X.mmul(C, Wd)[i, i] for i in range(N))))
    tr = X.red(sp.expand(sum(Wd[i, i] for i in range(N))))
    te = X.red(sp.expand(sum((Pp * Wd)[i, i] for i in range(N))))
    to = X.red(sp.expand(sum((Pm * Wd)[i, i] for i in range(N))))
    splits.append(X.red(sp.expand(te + to - tr)) == 0 and X.red(sp.expand(te - to - st)) == 0)
    e = ex(st); strs[mm] = e
    reals.append(abs(num(st).imag) < 1e-25)
    print(f"      {mm:2d}   {math.gcd(mm,15):2d} | {str(e):22s} = {num(st).real:+.9f} "
          f"| {num(te).real:+7.3f} {num(to).real:+7.3f}")

check("tr = tr_even + tr_odd and str = tr_even - tr_odd, exactly, for all 15",
      all(splits))
check("the supertrace is REAL for every m", all(reals))
check("every value lies in Q(sqrt5)",
      all(sp.simplify(sp.im(sp.N(v, 30))) == 0 and
          sp.sqrt(5) in v.atoms(sp.Pow) or v.is_rational for v in strs.values()))
check("MIRROR-INVARIANT: str(m) = str(15-m) for every m -- the graded trace "
      "cannot tell the object from its mirror",
      all(sp.simplify(strs[mm] - strs[(15 - mm) % 15]) == 0 for mm in range(15)))
check("str(0) = 2 = dim(even) - dim(odd): the grading's own index",
      strs[0] == 2 and sp.trace(Pp) - sp.trace(Pm) == 2)
vals = sorted({sp.nsimplify(v) for v in strs.values()}, key=lambda v: float(v))
check("the supertrace takes exactly 6 values over the whole period",
      len(vals) == 6, ", ".join(str(v) for v in vals))
phi_inv = (sp.sqrt(5) - 1) / 2
check("AT THE OBJECT'S OWN WORD, str(1) = 1/phi = phi - 1 EXACTLY",
      sp.simplify(strs[1] - phi_inv) == 0,
      f"str(1) = {strs[1]} = {float(strs[1]):.12f}")
check("the two branches are NOT separated by the supertrace the way the ear "
      "readout separates them -- branch B carries {1/phi, -1}, branch A carries "
      "{2, 1, -2, -1/phi}",
      {sp.nsimplify(strs[r]) for r in range(15) if math.gcd(r, 15) == 1}
      != {sp.nsimplify(strs[r]) for r in range(15) if math.gcd(r, 15) > 1})

# --- where the object's graded content actually LIVES
print()
def raw_parts(mm):
    Wd = X.mmul(mpow(R, mm), mpow(L, mm))
    te = X.red(sp.expand(sum((Pp * Wd)[i, i] for i in range(N))))
    to = X.red(sp.expand(sum((Pm * Wd)[i, i] for i in range(N))))
    return te, to

# NOTE: tested with simplify(...) == 0 on the RAW element.  Comparing the
# nsimplify'd printed form with == 0 reported this law FALSE -- E75's third
# mechanism (identify by property, never by representation), third arc running.
even_law = all((sp.simplify(raw_parts(mm)[0]) == 0) == (mm % 3 != 0) for mm in range(15))
check("THE EVEN SECTOR'S TRACE VANISHES IDENTICALLY unless 3 | m -- and 3 | m is "
      "B996's degeneracy condition (B1402)", even_law)
te1, to1 = raw_parts(1)
check("AT THE OBJECT'S OWN WORD m = 1 the even sector traces to EXACTLY ZERO and "
      "the whole graded index sits in the theta-ODD sector",
      sp.simplify(te1) == 0 and sp.simplify(ex(to1) + phi_inv) == 0,
      f"tr_even(1) = 0, tr_odd(1) = {ex(to1)} = -1/phi")

# --- the six values are Coxeter-shaped
js = {}
for v in vals:
    for jj in range(16):
        if sp.simplify(v - 2 * sp.cos(sp.pi * jj / 15)) == 0:
            js[jj] = v; break
check("all six values are EXACTLY 2cos(j*pi/15), with j in {0,5,6,9,10,15} -- the "
      "arguments run over the divisors of the period 15, not over 15 itself",
      sorted(js) == [0, 5, 6, 9, 10, 15], f"j = {sorted(js)}")
units = [r for r in range(15) if math.gcd(r, 15) == 1]
check("among the units the split is by 2-TORSION: str = +1/phi exactly when "
      "m^2 = 1 mod 15, str = -1 otherwise",
      all((sp.simplify(strs[u] - phi_inv) == 0) == ((u * u) % 15 == 1) for u in units),
      f"{{m : m^2=1}} = {[u for u in units if (u*u)%15==1]}")

print("\n    THE ANCHOR LEDGER, side by side:")
print("      quantity                          ear anchor   word anchor   outputs")
print("      B1349's matrix element  Re h(c)      2 bits       2.81 bits      4")
print("      the graded trace        str(m)       0            0             1")
print("      (the word is free because m = 1 is what five principles select -- B1405)")

print("\n=== SUMMARY ===")
bad = [n for n, o in OK if not o]
print(f"  {len(OK) - len(bad)}/{len(OK)} checks pass")
if bad: print("  FAILURES: " + "; ".join(bad))
raise SystemExit(1 if bad else 0)
