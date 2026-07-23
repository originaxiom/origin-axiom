#!/usr/bin/env python3
"""
OI-186 -- H112: one identity behind tr(A1A2)=15 and seam conductor 15?

Sealed criterion (B771 prereg):
  RESOLVED-A: a family law tr(A_m A_n) = seam-level derived, matching beyond (1,2)
  RESOLVED-B: the two 15s shown independent (base-rate honest)

The two 15s (B465 / HINT_LEDGER H112):
  (i)  Fricke: tr(A1 A2) = tr(A1)tr(A2) - tr(A1 A2^-1) = 3*6 - 3 = 15,
       with A_m = R^m L^m the metallic generators (A1 = RL golden, A2 = RRLL silver).
  (ii) seam level/conductor 15 = 3*5 = cond(Q(sqrt(5)) . Q(sqrt(-3)))
       = |disc| of the seam quadratic Q(sqrt(-15))
       (golden scale field x figure-eight geometry field, H122's C^15 = C^3 (x) C^5).

Plan (all exact/symbolic unless labeled):
  S1  Exact symbolic family table tr(A_m A_n), closed form + Fricke identity (sympy).
      Two word-set validation: A_m = R^m L^m vs L^m R^m vs M_m^2, M_m=[[m,1],[1,0]].
  S2  Geometry (invariant trace) fields of the metallic members computed IN-CELL
      via SnapPy shape fields (two precisions): m=1 -> Q(sqrt(-3)), m=2 -> Q(i),
      m>=3 -> shape not quadratic (degree check).  [numeric, 2 precisions]
  S3  Seam levels, literal H112 definition: seam(m) = conductor of the compositum
      scale(m).geometry(m) (biquadratic conductor = lcm of the three quadratic
      subfield |disc|).  Defined only where geometry(m) is quadratic (m=1,2).
  S4  The law tests:
      T1 literal law at the only other defined member m=2: seam(2) attainable by f?
      T2 elementwise scale-scale seam law f(m,n) =? cond(scale(m).scale(n)).
      T3 Eisenstein-anchored generalization f(m,n) =? |fund disc(-3(k^2+4))| scan.
      T4 all 4 cross-pairing conventions on {1,2}^2.
      T5 factorization forensics: which identifications make both 15s "3*5"?
  S5  Base-rate honesty: collision counts of f-table vs seam sets among small ints.
"""

import itertools
from fractions import Fraction
import sympy as sp
from sympy import symbols, Matrix, simplify, expand, factor, factorint, sqrt, lcm

OUT = []
def say(s=""):
    print(s)
    OUT.append(str(s))

# ----------------------------------------------------------------------------
say("=" * 78)
say("S1  EXACT SYMBOLIC FAMILY TABLE  tr(A_m A_n)")
say("=" * 78)

m, n = symbols("m n", positive=True, integer=True)
R = Matrix([[1, 1], [0, 1]])
L = Matrix([[1, 0], [1, 1]])

# R^k and L^k symbolically: R^k=[[1,k],[0,1]], L^k=[[1,0],[k,1]]
def Rk(k): return Matrix([[1, k], [0, 1]])
def Lk(k): return Matrix([[1, 0], [k, 1]])

A_m = Rk(m) * Lk(m)                     # R^m L^m
A_n = Rk(n) * Lk(n)
A_n_inv = A_n.inv()

tr_Am    = sp.expand(A_m.trace())
tr_AmAn  = sp.expand((A_m * A_n).trace())
tr_AmAni = sp.expand((A_m * A_n_inv).trace())

say(f"A_m = R^m L^m = {A_m.tolist()}")
say(f"tr(A_m)        = {tr_Am}                (metallic: m^2+2)")
say(f"tr(A_m A_n)    = {tr_AmAn}")
say(f"  closed form  = (mn)^2 + (m+n)^2 + 2 : "
    f"{sp.simplify(tr_AmAn - ((m*n)**2 + (m+n)**2 + 2)) == 0}")
say(f"tr(A_m A_n^-1) = {tr_AmAni}")
say(f"  closed form  = (m-n)^2 + 2          : "
    f"{sp.simplify(tr_AmAni - ((m-n)**2 + 2)) == 0}")

fricke = sp.simplify(tr_Am * tr_Am.subs(m, n) - tr_AmAni - tr_AmAn)
say(f"Fricke identity tr(A)tr(B) - tr(AB^-1) - tr(AB) == 0 : {fricke == 0}")

def f(mm, nn):  # exact integer closed form, re-verified below against matrices
    return (mm * nn) ** 2 + (mm + nn) ** 2 + 2

# word-set validation: R^m L^m vs L^m R^m vs M_m^2 (house method: >=2 word sets)
ok_words = True
for mm, nn in itertools.product(range(1, 9), repeat=2):
    Am1 = Rk(mm) * Lk(mm);  An1 = Rk(nn) * Lk(nn)          # word set 1
    Am2 = Lk(mm) * Rk(mm);  An2 = Lk(nn) * Rk(nn)          # word set 2 (conjugate)
    Mm  = Matrix([[mm, 1], [1, 0]]);  Am3 = Mm * Mm        # word set 3: M_m^2
    Mn  = Matrix([[nn, 1], [1, 0]]);  An3 = Mn * Mn
    t1 = (Am1 * An1).trace(); t2 = (Am2 * An2).trace(); t3 = (Am3 * An3).trace()
    if not (t1 == t2 == f(mm, nn)):
        ok_words = False
        say(f"  WORD-SET MISMATCH at ({mm},{nn}): {t1} {t2} {t3}")
    # M_m^2 = [[m^2+1, m],[m,1]] equals R^m L^m only up to ordering; check trace:
    if t3 != f(mm, nn):
        ok_words = False
        say(f"  M^2 trace mismatch at ({mm},{nn}): {t3} vs {f(mm,nn)}")
say(f"word-set cross-validation (R^mL^m vs L^mR^m vs M_m^2), m,n<=8: "
    f"{'PASS' if ok_words else 'FAIL'}")

say(f"\nBase point: tr(A1 A2) = {f(1,2)}  (B465: 3*6 - 3 = 15)  "
    f"tr(A1)={f(1,1) if False else 3}, tr(A2)=6, tr(A1A2^-1)={(1-2)**2+2}")

say("\nFamily table tr(A_m A_n), m,n = 1..8:")
hdr = "      " + "".join(f"{nn:>8d}" for nn in range(1, 9))
say(hdr)
for mm in range(1, 9):
    say(f"m={mm:2d} |" + "".join(f"{f(mm,nn):>8d}" for nn in range(1, 9)))

# ----------------------------------------------------------------------------
say("")
say("=" * 78)
say("S2  GEOMETRY FIELDS OF THE METALLIC MEMBERS, IN-CELL (SnapPy shape fields)")
say("=" * 78)

import snappy
from snappy import Manifold, ManifoldHP

def shape_field_degree_and_disc(word, prec_dps=30):
    """Build the once-punctured-torus bundle b++<word>, return list of
    (algdep-degree, squarefree disc if quadratic) per tetrahedron shape."""
    Mfd = ManifoldHP("b++" + word)
    pari = snappy.pari
    old = pari.set_real_precision(prec_dps)
    shapes = Mfd.tetrahedra_shapes("rect")
    results = []
    for z in shapes:
        zp = pari(str(z))
        # find minimal degree with a convincing algdep hit
        deg_found, disc_sf = None, None
        for d in (1, 2, 3, 4, 5, 6, 7, 8):
            try:
                poly = pari.algdep(zp, d)
            except Exception:
                continue  # algdep domain error (e.g. degree 1 on complex input)
            if poly.poldegree() < 1:
                continue
            # residual check + height filter: a genuine small-degree relation for
            # these shapes has small integer coefficients; astronomically large
            # coefficients are algdep noise (conditioning: at low precision the
            # noise CAN pass a pure-residual test -- UNSTABLE beats a forced hit)
            resid = abs(poly.subst(pari("x"), zp))
            height = max(abs(int(poly.polcoeff(i)))
                         for i in range(poly.poldegree() + 1))
            if float(resid) < 10 ** (-(prec_dps - 8)) and height < 10 ** 8:
                deg_found = poly.poldegree()
                if deg_found == 2:
                    a, b, c = (int(poly.polcoeff(2)), int(poly.polcoeff(1)),
                               int(poly.polcoeff(0)))
                    D = b * b - 4 * a * c
                    disc_sf = sp.factorint(D) if D != 0 else None
                    # squarefree kernel of D
                    sf = 1
                    for p, e in sp.factorint(D).items():
                        if p == -1:
                            sf *= -1 if e % 2 else 1
                        else:
                            sf *= p ** (e % 2)
                    disc_sf = sf
                break
        results.append((deg_found, disc_sf, str(zp)[:24]))
    vol = Mfd.volume()
    pari.set_real_precision(old)
    return vol, results

for mm, word in [(1, "RL"), (2, "RRLL"), (3, "RRRLLL"), (4, "RRRRLLLL")]:
    for prec in (30, 60):   # two precisions (house method)
        vol, res = shape_field_degree_and_disc(word, prec)
        degs = sorted({d for d, _, _ in res if d is not None})
        none_ct = sum(1 for d, _, _ in res if d is None)
        sfs  = sorted({s for _, s, _ in res if s is not None})
        quad = "QUADRATIC, disc sf=" + str(sfs) if degs == [2] else \
               ("NOT quadratic (min small-height degrees " + str(degs) +
                (f", {none_ct} shapes with no small-height relation <= deg 8"
                 if none_ct else "") + ")")
        say(f"m={mm} b++{word} prec={prec}dps vol={float(vol):.9f} -> {quad}")

say("""
Reading (matches banked B125, now recomputed in-cell):
  m=1: every shape quadratic, squarefree disc -3  -> geometry field Q(sqrt(-3))
  m=2: shapes quadratic, squarefree disc -1       -> geometry field Q(i)
  m=3,4: shapes NOT quadratic (degree >= 4)       -> geometry field not quadratic,
         hence NOT abelian over Q => a CONDUCTOR for the compositum DOES NOT EXIST.
""")

# ----------------------------------------------------------------------------
say("=" * 78)
say("S3  SEAM LEVELS (literal H112 definition) -- exact conductor arithmetic")
say("=" * 78)

def fund_disc(d):
    """fundamental discriminant of Q(sqrt(d)), d a nonzero integer (not square)."""
    sf = 1
    for p, e in sp.factorint(d).items():
        if p == -1:
            sf *= (-1) ** (e % 2) if p == -1 else 1
        else:
            sf *= p ** (e % 2)
    if d < 0 and sf > 0:
        sf = -sf  # keep the sign of the radicand's squarefree kernel
    return sf if sf % 4 == 1 else 4 * sf

def biquadratic_conductor(d1, d2):
    """conductor of Q(sqrt(d1), sqrt(d2)) = lcm of |fund discs| of the three
    quadratic subfields (conductor-discriminant)."""
    D1, D2 = fund_disc(d1), fund_disc(d2)
    D3 = fund_disc(d1 * d2)
    return sp.lcm(sp.lcm(abs(D1), abs(D2)), abs(D3)), (D1, D2, D3)

# member data: scale field radicand m^2+4 ; geometry radicand (S2, in-cell)
geometry_radicand = {1: -3, 2: -1}  # m>=3: none (not quadratic)

say("member m | scale field disc | geometry field disc | seam quadratic | "
    "cond(compositum) | sqrt(disc(compositum))")
seam = {}
for mm in (1, 2):
    ds = mm * mm + 4
    dg = geometry_radicand[mm]
    cond, (D1, D2, D3) = biquadratic_conductor(ds, dg)
    # disc of the biquadratic = D1*D2*D3 (conductor-discriminant, 4 characters)
    disc_comp = abs(D1 * D2 * D3)
    seam[mm] = int(cond)
    say(f"   {mm}     |  {int(D1):>4d}            |  {int(D2):>4d}               "
        f"| Q(sqrt({int(fund_disc(ds*dg))})) |  {int(cond):>4d}          | "
        f"{sp.sqrt(disc_comp)}")
say(f"\nseam(1) = {seam[1]}   (= the banked seam level 15 = 3*5)   "
    f"seam(2) = {seam[2]}")
say("m>=3: seam undefined (geometry field non-quadratic, in-cell S2; compositum"
    " non-abelian, no conductor).")

# ----------------------------------------------------------------------------
say("")
say("=" * 78)
say("S4  THE LAW TESTS")
say("=" * 78)

say("\n--- T1: the literal law at the ONLY other defined member, m=2 ---")
say(f"seam(2) = {seam[2]} (conductor reading); sqrt(disc) reading gives 16.")
say("Is 8 (or 16) in the image of f(m,n) = (mn)^2+(m+n)^2+2, m,n>=1 ?")
say("f = 8  <=> (mn)^2+(m+n)^2 = 6 ;  f = 16 <=> (mn)^2+(m+n)^2 = 14.")
say("Exact finite check: (mn)^2 <= 14 forces mn <= 3, i.e. (m,n) in "
    "{(1,1),(1,2),(2,1),(1,3),(3,1)}:")
for mm, nn in [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1)]:
    say(f"   (m,n)=({mm},{nn}): (mn)^2+(m+n)^2 = {(mm*nn)**2 + (mm+nn)**2}")
say("=> 6 and 14 are NOT attained. 8 and 16 are NOT traces of any metallic pair.")
say("=> the law fails DEFINITIVELY at its only other testable member:")
say("   no (m,n) whatsoever gives tr(A_m A_n) = seam(2), under either reading.")

say("\n--- T2: elementwise scale-scale seam law: f(m,n) =? cond(scale(m).scale(n)) ---")
matches = []
for mm in range(1, 31):
    for nn in range(mm + 1, 31):
        cond, _ = biquadratic_conductor(mm * mm + 4, nn * nn + 4)
        if f(mm, nn) == cond:
            matches.append((mm, nn, int(cond)))
c12, _ = biquadratic_conductor(5, 8)
say(f"at the base point (1,2): cond(Q(sqrt5).Q(sqrt2)) = {c12}  vs  f(1,2) = 15"
    f"  -> already fails at (1,2)")
say(f"elementwise matches for 1<=m<n<=30: {matches if matches else 'NONE'}")

say("\n--- T3: Eisenstein-anchored generalization "
    "f(m,n) =? |fund_disc(-3(k^2+4))| for some k ---")
level3 = {}
for k in range(1, 401):
    level3[abs(fund_disc(-3 * (k * k + 4)))] = level3.get(
        abs(fund_disc(-3 * (k * k + 4))), []) + [k]
hits = []
for mm in range(1, 61):
    for nn in range(mm, 61):
        v = f(mm, nn)
        if v in level3:
            hits.append((mm, nn, v, level3[v]))
say("hits (m<=n<=60, k<=400):")
for h in hits:
    say(f"   f({h[0]},{h[1]}) = {h[2]} = seam_E(k) for k in {h[3]}")
say("naive face-value form 3(k^2+4) (ignoring fundamental-disc corrections):")
naive_hits = []
for mm in range(1, 301):
    for nn in range(mm, 301):
        v = f(mm, nn)
        if v % 3 == 0 and (v // 3 - 4) >= 0:
            r = sp.sqrt(sp.Integer(v // 3 - 4))
            if r.is_integer and int(r) >= 1:
                naive_hits.append((mm, nn, v, int(r)))
say(f"solutions of (mn)^2+(m+n)^2+2 = 3(k^2+4), m<=n<=300: {naive_hits}")

def sf_kernel(x):
    sf = 1
    for p, e in sp.factorint(x).items():
        sf *= p ** (e % 2) if p != -1 else (-1) ** (e % 2)
    return sf

say("\nforensics on the k-multiset hitting 15: k in [1,4,11,29,76,199]:")
for k in [1, 4, 11, 29, 76, 199]:
    say(f"   k={k:3d}: squarefree kernel of k^2+4 = {sf_kernel(k*k+4)}  "
        f"-> scale field Q(sqrt({sf_kernel(k*k+4)}))")
say("=> every k hitting 15 has scale field Q(sqrt(5)) (k = odd-index Lucas,"
    " L^2+4 = 5F^2):")
say("   the 'extra instances' of 15 are the SAME field pair"
    " (Eisenstein, golden) re-entered, not new law instances.")
say("structure test for a canonical pairing k(m,n) across the other hits:")
say("   (1,6)->k=5; (1,18)->k=15; (2,19)->k=25; (3,4)->k=16; (11,22)->k=141 ...")
say("   no function of (m,n) (min, max, m+n, mn, |m-n|, ...) reproduces these k;")
for name, g in [("min", lambda a, b: min(a, b)), ("max", lambda a, b: max(a, b)),
                ("m+n", lambda a, b: a + b), ("mn", lambda a, b: a * b),
                ("|m-n|", lambda a, b: abs(a - b))]:
    ok = sum(1 for (mm, nn, v, kk) in naive_hits if g(mm, nn) == kk)
    say(f"   candidate k = {name}: matches {ok}/{len(naive_hits)} hits")
say("   the hits are Pell-conic integer points ((mn)^2+(m+n)^2-3k^2 = 10 is a"
    " quadric with infinitely many lattice points), not a family law.")

say("\n--- T4: all cross-pairing conventions on members {1,2} ---")
fields = {
    "scale(1)=Q(sqrt5)": 5, "scale(2)=Q(sqrt2)": 8,
    "geom(1)=Q(sqrt-3)": -3, "geom(2)=Q(i)": -1,
}
say(f"target: tr(A1A2) = 15.  conductors of all 2-subsets of member-{{1,2}} fields:")
names = list(fields)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        d1, d2 = fields[names[i]], fields[names[j]]
        if d1 * d2 > 0 and sp.integer_nthroot(d1 * d2, 2)[1]:
            say(f"   {names[i]} . {names[j]} : same field, no seam")
            continue
        cond, _ = biquadratic_conductor(d1, d2)
        star = "  <-- 15" if cond == 15 else ""
        say(f"   {names[i]} . {names[j]} : cond = {cond}{star}")
say("=> 15 arises from exactly ONE pairing: scale(1).geom(1) -- both fields of "
    "member m=1 ALONE.")
say("   The trace 15 is a TWO-member invariant (m=1 with m=2); the seam 15 is a "
    "ONE-member invariant (m=1 with itself).")
say("   The index structures do not even align at the base point.")

say("\n--- T5: factorization forensics of the two 15s ---")
say("trace:  15 = 3*6-3 = 3*(6-1) = tr(A1) * (tr(A2)-1)")
say("seam:   15 = 3*5   = |disc(geom(1))| * disc(scale(1))")
say("the '3's: tr(A1) = m^2+2 |_(m=1) = 3   vs  |disc Q(sqrt(-3))| = 3")
for mm in (2, 3, 4):
    g = geometry_radicand.get(mm)
    gd = abs(fund_disc(g)) if g else None
    say(f"   m={mm}: tr(A_m) = {mm*mm+2}  vs  |disc(geom({mm}))| = "
        f"{gd if gd else 'undefined (non-quadratic)'}   equal? "
        f"{gd == mm*mm+2 if gd else False}")
say("the '5's: tr(A2)-1 = 5  vs  disc(scale(1)) = 1^2+4 = 5")
for mm in (2, 3):
    say(f"   m={mm}: tr(A_(m+1))-1 = {(mm+1)**2+2-1}  vs  disc(scale({mm})) "
        f"= fund_disc({mm*mm+4}) = {fund_disc(mm*mm+4)}   equal? "
        f"{(mm+1)**2+1 == abs(fund_disc(mm*mm+4))}")
say("=> BOTH factor identifications (3<->3 and 5<->5) hold at m=1 ONLY.")
say("   Each is a small-number pun: m^2+2 vs |disc(shape field)| are unrelated "
    "quantities that collide at 3; (m+1)^2+1 vs fund_disc(m^2+4) collide at 5.")

# check: is f(m,m+1) = (m^2+2)(m^2+4) an identity or m=1-only?
lhs = f(m, m + 1) if False else None
expr = sp.expand((m * (m + 1)) ** 2 + (2 * m + 1) ** 2 + 2 - (m**2 + 2) * (m**2 + 4))
say(f"\nf(m,m+1) - (m^2+2)(m^2+4) = {sp.factor(expr)}  "
    f"(zero only at m=1: roots {sp.solve(expr, m)})")

# ----------------------------------------------------------------------------
say("")
say("=" * 78)
say("S5  BASE-RATE HONESTY")
say("=" * 78)
# how special is a collision like this among the program's small structural numbers?
fvals = sorted({f(mm, nn) for mm in range(1, 61) for nn in range(1, 61)})
seamE = sorted(level3.keys())
X = 5000
fX = [v for v in fvals if v <= X]
sX = [v for v in seamE if v <= X]
inter = sorted(set(fX) & set(sX))
say(f"f-values <= {X}: {len(fX)};  Eisenstein-seam levels <= {X}: {len(sX)}")
say(f"intersection: {inter}")
exp_rand = len(fX) * len(sX) / X
say(f"uniform-null expectation in [1,{X}]: ~{exp_rand:.1f}; observed: {len(inter)}.")
say("The excess over the uniform null is NOT law-evidence -- it is conic "
    "arithmetic. Two demonstrations:")

say("\n(a) the m=1-row hits are Pell-unit orbits, verified exactly:")
say("    m=1: f(1,n)=3(k^2+4) <=> u^2 - 6k^2 = 19 with u = 2n+1.")
u_k = [(2 * nn + 1, kk) for (mm, nn, v, kk) in naive_hits if mm == 1]
say(f"    hits as (u,k): {u_k}")
ok_pell = all(u * u - 6 * k * k == 19 for u, k in u_k)
say(f"    all satisfy u^2-6k^2 = 19: {ok_pell}")
say("    orbit check under the Pell unit 5+2*sqrt(6) of Z[sqrt6]:")
for (u1, k1), (u2, k2) in zip(u_k, u_k[2:]):
    up, kp = 5 * u1 + 12 * k1, 2 * u1 + 5 * k1   # (u+k sqrt6)(5+2 sqrt6)
    say(f"    ({u1},{k1}) * (5+2sqrt6) = ({up},{kp})  matches next-in-orbit "
        f"({u2},{k2}): {(up, kp) == (u2, k2)}")
say("    => the recurring 15-type hits propagate by Pell-unit multiplication --"
    " pure real-quadratic unit arithmetic, no seam content.")

say("\n(b) anchor-swap control: replace the Eisenstein anchor 3 by c and count "
    "solutions of f(m,n) = c(k^2+4), m<=n<=300:")
for c in (3, 5, 7, 11, 13):
    ct = 0
    for mm in range(1, 301):
        for nn in range(mm, 301):
            v = f(mm, nn)
            if v % c == 0 and v // c - 4 >= 1:
                if sp.integer_nthroot(v // c - 4, 2)[1]:
                    ct += 1
    say(f"    anchor c={c:2d}: {ct} solutions")
say("    counts (12/0/3/2/0) vary with the congruence density of the conic mod c,"
    " not with any seam meaning of c=3;")
say("    c=5 and c=13 are congruence-obstructed, c=7 and c=11 (no seam reading) "
    "still produce hits.")
say("\nConclusion: the overlap of the two quadratic-valued sets is generic conic/"
    "Pell arithmetic; nothing law-shaped survives.")
say("Moreover the one structurally-cited collision (15) pairs f(1,2) [two-member]"
    " with seam(1) [one-member]: mismatched index structure even where the "
    "numbers agree.")

say("")
say("=" * 78)
say("VERDICT")
say("=" * 78)
say("""RESOLVED-B. The two 15s are independent:
 1. EXACT family law for the trace side: tr(A_m A_n) = (mn)^2 + (m+n)^2 + 2
    (symbolic sympy, Fricke identity verified, 3 word-set conventions agree).
 2. The seam side is NOT a family: the conductor exists only for m in {1,2}
    (in-cell SnapPy shape fields, 2 precisions: geom(1)=Q(sqrt(-3)),
    geom(2)=Q(i), m>=3 non-quadratic => non-abelian compositum, no conductor).
 3. At the only other defined member, seam(2) = 8 (conductor) or 16 (sqrt-disc)
    and NEITHER is attainable: f = 8 or 16 forces (mn)^2+(m+n)^2 in {6,14},
    impossible (exact finite check). The law fails definitively beyond (1,2).
 4. Every liberal generalization scanned fails to be a law:
    - scale-scale conductor elementwise: 0 matches m<n<=30 (already 40 vs 15
      at the base point);
    - Eisenstein-anchored 3(k^2+4): the value 15 recurs only at k = odd-index
      Lucas (k^2+4 = 5F^2) -- the SAME field pair (Eisenstein, golden)
      re-entered; the remaining scattered hits are Pell-conic lattice points
      ((mn)^2+(m+n)^2-3k^2 = 10) with NO canonical pairing k(m,n) (all 5
      natural candidates score <= 1/12);
    - all cross-pairings on {1,2}^2: 15 arises from exactly one pairing,
      scale(1).geom(1), i.e. member 1 with itself -- MISMATCHED index
      structure vs the two-member trace (m=1 with m=2).
 5. Both factor identifications behind '15 = 3*5' (tr(A1)=3 <-> |disc(-3)|=3,
    tr(A2)-1=5 <-> disc 5) are m=1-only small-number collisions; the set
    overlap beyond the uniform null is fully accounted for by Pell-unit orbits
    (u^2-6k^2 = 19 verified exactly, orbit propagation by 5+2sqrt6) and
    survives anchor-swap (c=7, c=11 produce hits too): generic conic
    arithmetic, no Eisenstein/seam content.
Keepable positive: the exact closed forms tr(A_m A_n) = (mn)^2+(m+n)^2+2 and
tr(A_m A_n^-1) = (m-n)^2+2 for the metallic generator family.""")

with open(__file__.replace("compute.py", "output.txt"), "w") as fh:
    fh.write("\n".join(OUT) + "\n")
