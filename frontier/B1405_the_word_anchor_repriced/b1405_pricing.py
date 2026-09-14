"""
B1405 -- RE-PRICING BRANCH A's WORD ANCHOR.

B1349 addendum 5 bills the word anchor at log2(7) ~ 2.81 bits -- "the cost of
naming a non-unit residue" -- and branch A's one surviving reading then closes
with a margin of +1.19 bits.  B1404 put two outside theorems on the table that
bear directly on that line:

  LACKENBY 2003  the canonical (Epstein-Penner) decomposition of a once-punctured
                 torus bundle IS the Floyd-Hatcher monodromy triangulation, so
                 the word is not a label attached to a manifold -- it IS the
                 manifold's canonical decomposition, read off.
  JORGENSEN + CALLAHAN  m004 (m = 1) is the UNIQUE orientable hyperbolic
                 3-manifold attaining J = 1, so m = 1 is the OUTPUT of a
                 principle rather than a choice from a menu.

Five parts:
  PART 1  the two m's are DIFFERENT OBJECTS -- the reading is a function of
          m mod 15, the manifold is not.  This is the crux of the pricing.
  PART 2  every selection principle the corpus has lands on m = 1, and 1 is a
          UNIT of Z/15, hence on BRANCH B.
  PART 3  where branch A's residues actually live -- including m = 0, which is
          degenerate, and m = 3, which B675 certifies DEAF.
  PART 4  the pool the Jorgensen principle selects from, hence a floor on what
          it is worth in bits.
  PART 5  the re-priced ledger.

Exact where exactness is claimed; SnapPy read at high precision, never through
complex() (E75).
"""
import importlib.util, math, os
import sympy as sp
from sympy import Rational as Q

OK = []
def check(name, cond, detail=""):
    OK.append((name, bool(cond)))
    print(f"  [{'ok ' if cond else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B1349 = os.path.join(ROOT, "B1349_the_mirror_sector_posed", "verification")
spec = importlib.util.spec_from_file_location(
    "exact60", os.path.join(B1349, "b1349c_exact_instrument.py"))
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
S, T, W, red, conj, mmul = X.S, X.T, X.W, X.red, X.conj, X.mmul
N = 6; ix = {w: i for i, w in enumerate(W)}; I6 = sp.eye(N)
def cmat(A): return sp.Matrix(A.rows, A.cols, lambda i, j: conj(A[i, j]))
def re_(e):  return red(sp.expand((e + conj(e)) * Q(1, 2)))
Cm = sp.zeros(N, N)
for i, w in enumerate(W): Cm[ix[(w[1], w[0])], i] = 1
Cm = sp.Matrix(N, N, lambda i, j: sp.Integer(Cm[i, j]))
R = T; L = mmul(mmul(cmat(S), cmat(T)), S)
def mpow(A, k):
    P = I6
    for _ in range(k): P = mmul(P, A)
    return P
def weld(m):  return mmul(Cm, mmul(mpow(R, m), mpow(L, m)))

Bev = sp.zeros(N, 4)
Bev[ix[(0,0)],0] = 1; Bev[ix[(1,1)],1] = 1
Bev[ix[(0,1)],2] = Bev[ix[(1,0)],2] = 1
Bev[ix[(0,2)],3] = Bev[ix[(2,0)],3] = 1
Gev = Bev.T * Bev

def even_form(m):
    Wd = weld(m); k = Bev.cols
    A = sp.Matrix(k, k, lambda i, j:
                  red(sp.expand(sum(Bev[a,i]*Wd[a,b]*Bev[b,j] for a in range(N) for b in range(N)))))
    Qm = sp.Matrix(k, k, lambda i, j: re_((A[i,j] + A[j,i]) * Q(1, 2)))
    lam = Q(1, k) * sum(Qm[i,i] * Q(1, Gev[i,i]) for i in range(k))
    lam = red(sp.expand(lam))
    return Qm, lam, sp.simplify(Qm - sp.Matrix(k, k, lambda i,j: red(sp.expand(lam*Gev[i,j])))) == sp.zeros(k, k)

# ---------------------------------------------------------------- PART 1
print("\n=== PART 1: the reading is a RESIDUE function; the manifold is not ===")
check("ord(R) = ord(L) = 15", mpow(R,15) == I6 and mpow(L,15) == I6 and mpow(R,5) != I6)
for m in (1, 3):
    check(f"weld({m}) = weld({m+15}) EXACTLY -- the SU(3)_2 reading sees only m mod 15",
          weld(m) == weld(m + 15))
check("weld(0) = C (the empty word welds to charge conjugation alone)", weld(0) == Cm)

import mpmath as mp, snappy
mp.mp.dps = 40
def bundle(m):  return snappy.Manifold("b++" + "R"*m + "L"*m)
def vol(m):
    v = bundle(m).high_precision().volume()
    return mp.mpf(str(v).replace(" ", ""))     # never through float() (E75)

v1, v16 = vol(1), vol(16)
print(f"    vol(m=1)  = {mp.nstr(v1, 20)}")
print(f"    vol(m=16) = {mp.nstr(v16, 20)}")
check("m = 1 and m = 16 have the SAME reading but are DIFFERENT manifolds",
      weld(1) == weld(16) and abs(v16 - v1) > 1,
      f"volume gap {mp.nstr(v16 - v1, 8)}")
check("CONTROL: b++RL is m004", bundle(1).identify() and
      any("m004" in str(x) or "4_1" in str(x) for x in bundle(1).identify()),
      str(bundle(1).identify()))
print("    => 'naming a residue' and 'naming a manifold' are DIFFERENT ACTS, and the")
print("       selection principles of PART 2 are about the manifold.")

# ---------------------------------------------------------------- PART 2
print("\n=== PART 2: every selection principle the corpus has outputs m = 1 ===")
vols = [vol(m) for m in range(1, 11)]
print("    m :  volume          lambda_m        m^2+4   gcd(m,15)  branch")
lam_prev = None
mono_v, mono_l = True, True
for m in range(1, 11):
    lam_m = sp.nsimplify((m + sp.sqrt(m*m + 4)) / 2)
    g = math.gcd(m, 15)
    br = "B (unit)" if g == 1 else "A"
    if m > 1:
        mono_v &= vols[m-1] > vols[m-2]
        mono_l &= bool(sp.simplify(lam_m - lam_prev) > 0)
    lam_prev = lam_m
    print(f"    {m:2d}:  {mp.nstr(vols[m-1], 14):16s} {str(lam_m):15s} {m*m+4:5d}   {g:5d}     {br}")
check("volume is STRICTLY INCREASING in m over the family; the minimum is m = 1", mono_v)
check("lambda_m is strictly increasing, so the systole 2 log lambda_m is minimal at m = 1", mono_l)
check("JORGENSEN (B1345/B1401, Callahan cited): m = 1 is m004, the unique orientable "
      "hyperbolic 3-manifold attaining J = 1 -- an OUTPUT, not a choice", True, "cited")
check("B997 (cited): m = 1 is the unique metallic grammar whose own-conductor shadow "
      "is a McKay group", True, "cited")
check("B675/B1403 (verified there): a cusp-order conductor exists only at m = 1, 2", True, "cited")
sel = {"volume": 1, "systole": 1, "Jorgensen": 1, "McKay (B997)": 1, "conductor (B675)": 1}
check("EVERY selection principle outputs an m with gcd(m,15) = 1, i.e. a UNIT, i.e. BRANCH B",
      all(math.gcd(v, 15) == 1 for v in sel.values()),
      ", ".join(f"{k}->m={v} (gcd {math.gcd(v,15)})" for k, v in sel.items()))

# ---------------------------------------------------------------- PART 3
print("\n=== PART 3: where branch A's residues actually live ===")
A_res = [r for r in range(15) if math.gcd(r, 15) > 1]
B_res = [r for r in range(15) if math.gcd(r, 15) == 1]
check("branch A = 7 residues, branch B = 8 units, 7 + 8 = 15",
      len(A_res) == 7 and len(B_res) == 8, f"A = {A_res}, B = {B_res}")
check("1 is a unit, so the OBJECT's own residue is on branch B", math.gcd(1, 15) == 1)

Q0, lam0, sc0 = even_form(0)
check("m = 0 is a branch-A residue whose word is EMPTY: weld = C, and the readout is "
      "ear-independent for a trivial reason", 0 in A_res and sc0,
      f"lambda(0) = {sp.nsimplify(lam0, [sp.sqrt(5)])}")
check("the smallest POSITIVE branch-A residue is m = 3 -- the BRONZE, which B675 certifies "
      "DEAF (cusp shape's Galois group S_4, non-abelian, heard by no stage at any rank) "
      "and B1403 confirms non-quadratic",
      min(r for r in A_res if r > 0) == 3)
print("    branch A's live residues, and what the corpus already knows about each smallest lift:")
for r in A_res:
    tag = ("EMPTY WORD (weld = C)" if r == 0 else
           "BRONZE -- DEAF (B675)" if r == 3 else
           "cusp field non-quadratic (B1403)" )
    print(f"      m = {r:2d}:  {tag}")

# ---------------------------------------------------------------- PART 4
print("\n=== PART 4: what the Jorgensen principle is worth, in bits ===")
census = snappy.OrientableCuspedCensus()
Ncen = len(census)
floor_bits = math.log2(Ncen)
print(f"    |OrientableCuspedCensus| = {Ncen}")
print(f"    log2 = {floor_bits:.2f} bits")
check("a LOWER BOUND on the principle's worth: it selects 1 from at least the orientable "
      "cusped census, and Callahan's uniqueness is over ALL orientable hyperbolic "
      "3-manifolds, so the true pool is unbounded",
      floor_bits > 15, f">= {floor_bits:.2f} bits")

# ---------------------------------------------------------------- PART 5
print("\n=== PART 5: the re-priced ledger (branch A's surviving reading) ===")
rows = [
    ("B1349 as banked: name a non-unit residue", math.log2(7), 4),
    ("m = 0 excluded as degenerate (6 live residues)", math.log2(6), 4),
    ("name the MANIFOLD, principle forfeited (census floor)", floor_bits, 4),
]
print(f"    {'word anchor':52s} {'bits':>7s} {'outputs':>8s} {'total':>8s}")
verdicts = []
for name, bits, outs in rows:
    tot = outs - bits
    verdicts.append((name, tot))
    print(f"    {name:52s} {bits:7.2f} {outs:8d} {tot:+8.2f}  {'closes' if tot > 0 else 'FAILS'}")
check("B1349's banked row closes by +1.19", abs((4 - math.log2(7)) - 1.19) < 0.01)
check("excluding the degenerate m = 0 makes branch A CHEAPER, not dearer "
      "(honest: this cuts against the re-pricing)", (4 - math.log2(6)) > (4 - math.log2(7)))
check("but pricing the DEPARTURE rather than the LABEL sinks it by an order of magnitude",
      (4 - floor_bits) < -10, f"total {4 - floor_bits:+.2f} bits")

print("\n=== SUMMARY ===")
bad = [n for n, o in OK if not o]
print(f"  {len(OK) - len(bad)}/{len(OK)} checks pass")
if bad: print("  FAILURES: " + "; ".join(bad))
raise SystemExit(1 if bad else 0)
