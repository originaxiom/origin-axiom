#!/usr/bin/env python3
# B749 — fork F7 (sealed campaign, seal v2): the Sturmian strata control.
#
# Executes MEASUREMENTS.md F7 exactly as sealed (v2, hash dbf7e40c...40d81e5d):
#   F7a — non-quadratic slope: no self-similar generator (Lagrange), verified on a
#         concrete transcendental-slope witness (alpha = e-2) via CF non-periodicity.
#   F7b — the quadratic NON-metallic stratum (the v1-miss): the sqrt(3)-1 word's
#         composite substitution (CF period (1,2)), its carrier mapping torus,
#         hyperbolicity, volume, trace field, faces vs the banked V4 anatomy.
#   F7c — metallic stratum: covered by F3, cross-reference only.
#
# Anatomy yardstick (MEASUREMENTS.md header): being = trace field Q(sqrt(-3));
# hearing = the golden / Q(sqrt(5)) side; the cusp/interface; arithmeticity;
# knot-ness (H1 = Z) where applicable.
#
# Deterministic: no wall-clock, no unseeded randomness, no network.
# Tools: python 3.12.1, snappy 3.3.2 (+ its bundled pari), sympy 1.14.0, mpmath 1.3.0.
# Instrument rules honored: exact field claims = numeric relation + exact factornf;
# snappy identifications = two independent invariants (volume + isometry, plus H1);
# algdep with coefficient-size-aware thresholds and residual guards (cc2's lindep
# lesson); every verdict-bearing fact printed as a CHECK: line.

import warnings
warnings.filterwarnings("ignore")  # suppress the benign plink/tkinter GUI warning

import snappy
from snappy import pari
import sympy as sp
import mpmath as mp
from sympy.ntheory.continued_fraction import continued_fraction_periodic
from sympy.matrices.normalforms import smith_normal_form

checks = []


def CHECK(fact, value, ok=True):
    line = f"CHECK: {fact} = {value}"
    print(line)
    checks.append(line)
    if not ok:
        raise AssertionError("CHECK FAILED: " + line)


def pnum(x):
    """snappy HP Number -> pari t_COMPLEX/t_REAL at current pari precision."""
    return pari(str(x))


PREC = 64  # decimal digits carried by snappy's ManifoldHP quad-double numbers
pari.set_real_precision(PREC)

# Coefficient-size-aware algdep acceptance (cc2's lindep lesson, binding):
# accept candidate p only if it is small (height <= HMAX) AND the certified
# distance to the nearest root, |p(t)|/|p'(t)|, is below 10^-(PREC-12).
HMAX = 10**6
RESID = pari(f"1.0e-{PREC - 12}")


def algdep_guarded(t, maxdeg, label):
    """Return (poly, degree) for the minimal accepted degree; print the audit trail."""
    accepted = None
    for d in range(1, maxdeg + 1):
        try:
            p = pari.algdep(t, d)
        except Exception:
            continue  # pari refuses degree bounds below the input's complexity
        if p.poldegree() < 1:
            continue
        height = max(abs(int(c)) for c in p.Vec())
        res = pari.subst(p, pari("x"), t).abs()
        dres = pari.subst(p.deriv(), pari("x"), t).abs()
        cert = res / dres if dres != 0 else res
        ok = (height <= HMAX) and (cert < RESID) and p.polisirreducible()
        print(f"  algdep[{label}] deg<={d}: {p}  height={height:.3g}  "
              f"|p(t)|={float(res):.3e}  |p(t)|/|p'(t)|={float(cert):.3e}  "
              f"{'ACCEPT' if ok else 'reject'}")
        if ok:
            accepted = (p, p.poldegree())
            break
    if accepted is None:
        raise AssertionError(f"algdep found no admissible minimal polynomial for {label}")
    return accepted


def sqfree(n):
    """squarefree part (core) of a nonzero integer, sign preserved."""
    n = int(n)
    s = -1 if n < 0 else 1
    out = s
    for p_, e_ in sp.factorint(abs(n)).items():
        if e_ % 2 == 1:
            out *= p_
    return out


def splits_over(field_poly_t, target_poly_x):
    """number of irreducible factors of target (in x) over Q[t]/(field_poly_t)."""
    fx = pari(f"factornf({target_poly_x}, {field_poly_t})")
    return int(pari(f"matsize(factornf({target_poly_x}, {field_poly_t}))")[0]), fx


print("=" * 78)
print("B749 FORK F7 — THE STURMIAN STRATA CONTROL (seal v2)")
print("=" * 78)

# ============================================================================
# PART 0 — INSTRUMENT CONTROL: run the exact-field pipeline on the banked m004
# (validates that the being-face detector fires where it must fire).
# ============================================================================
print("\n--- PART 0: instrument control on the banked carrier m004 ---")
m004 = snappy.ManifoldHP("m004")
assert m004.solution_type() == "all tetrahedra positively oriented"
z004 = m004.tetrahedra_shapes("rect")[0]
p004, d004 = algdep_guarded(pnum(z004), 4, "m004 shape")
CHECK("control m004 shape minpoly", str(p004), str(p004) == "x^2 - x + 1")
CHECK("control m004 shape-field disc (squarefree part)", sqfree(1 - 4),
      sqfree(1 - 4) == -3)
n3, _ = splits_over("t^2 - t + 1", "x^2 + 3")
CHECK("control factornf(x^2+3) over Q[t]/(t^2-t+1) #factors", n3, n3 == 2)
CHECK("control m004 volume", str(snappy.Manifold('m004').volume()),
      abs(float(snappy.Manifold('m004').volume()) - 2.029883212819) < 1e-9)
CHECK("control m004 H1", str(m004.homology()), str(m004.homology()) == "Z")
# m004's hearing face: monodromy RL, dilatation = golden^2
R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])
A004 = R * L
lam004 = max((A004).eigenvals().keys(), key=lambda e: sp.N(e))
x = sp.Symbol("x")
CHECK("control m004 monodromy RL trace/det", f"tr={A004.trace()},det={A004.det()}",
      A004.trace() == 3 and A004.det() == 1)
CHECK("control m004 dilatation minpoly", sp.minimal_polynomial(lam004, x),
      sp.minimal_polynomial(lam004, x) == x**2 - 3 * x + 1)  # phi^2, field Q(sqrt5)

# ============================================================================
# PART A — F7a: the non-quadratic (transcendental) slope stratum.
# Witness: alpha = e - 2 in (0,1). e is transcendental (Hermite 1873 — classical);
# the sealed measurement is CF non-periodicity, computed here.
# Theorem chain used (stated, elementary direction only):
#   (i) If a Sturmian word of irrational slope alpha is fixed by a nontrivial
#       substitution with primitive abelianization M in GL2(Z), the letter-frequency
#       vector (1-alpha, alpha) is a Perron eigenvector of M, so alpha is a fixed
#       point of an integer Mobius map that is not the identity => alpha satisfies
#       an integer quadratic (M scalar is excluded: scalar matrices are imprimitive).
#   (ii) Lagrange: alpha quadratic <=> CF(alpha) eventually periodic.
# Hence: CF not eventually periodic => alpha not quadratic => NO self-similar
# generator exists. The self-similarity locus is exactly the QUADRATIC class.
# ============================================================================
print("\n--- PART A: F7a — non-quadratic slope witness alpha = e - 2 ---")
mp.mp.dps = 300
alpha = mp.e - 2
NDIG = 40
digs = []
y = 1 / alpha
for _ in range(NDIG):
    d = int(mp.floor(y))
    digs.append(d)
    y = 1 / (y - d)
print("CF(e-2) =", "[0;" + ",".join(map(str, digs)) + ",...]")

# (A1) digits match Euler's proven pattern for e-2: blocks (1, 2k, 1), k>=1
euler = []
k = 1
while len(euler) < NDIG:
    euler += [1, 2 * k, 1]
    k += 1
euler = euler[:NDIG]
CHECK("F7a CF(e-2) first 40 digits == Euler pattern (1,2k,1 blocks)", digs == euler,
      digs == euler)

# (A2) convergent certificate: reconstruct p/q = [0; d1..d40] by backward
# recurrence and verify the continued-fraction quality bound |alpha - p/q| < 1/q^2
num, den = 0, 1
for d in reversed(digs):
    num, den = den, d * den + num
# now [0; d1..d40] = num/den
err = abs(alpha - mp.mpf(num) / mp.mpf(den))
CHECK("F7a convergent p/q with |alpha - p/q| < 1/q^2",
      f"q={den}, err={mp.nstr(err, 5)}, 1/q^2={mp.nstr(1/mp.mpf(den)**2, 5)}",
      err < 1 / mp.mpf(den) ** 2)

# (A3) in-window periodicity exclusion: no (preperiod<=10, period<=10) fits
period_found = None
for pre in range(0, 11):
    for per in range(1, 11):
        if all(digs[i] == digs[i + per] for i in range(pre, NDIG - per)):
            period_found = (pre, per)
CHECK("F7a eventually-periodic fit with preperiod<=10, period<=10", period_found,
      period_found is None)
CHECK("F7a unbounded-digit evidence: strictly growing subsequence in window",
      f"{[d for d in digs if d % 2 == 0 and d > 1]}",
      [d for d in digs if d % 2 == 0 and d > 1] == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

# (A4) coefficient-size-aware quadraticity refutation in a box:
# min |A*alpha^2 + B*alpha + C| over |A|,|B|,|C| <= 50, (A,B,C) != 0
mp.mp.dps = 60
a60 = mp.e - 2
a2 = a60 * a60
best = None
for Acf in range(-50, 51):
    for Bcf in range(-50, 51):
        v = Acf * a2 + Bcf * a60
        Ccf = max(-50, min(50, int(mp.nint(-v))))
        if Acf == 0 and Bcf == 0:
            if Ccf == 0:
                continue
            val = abs(mp.mpf(1))  # min over C != 0 is 1
        else:
            val = abs(v + Ccf)
        if best is None or val < best[0]:
            best = (val, (Acf, Bcf, Ccf))
CHECK("F7a min |A a^2 + B a + C| over |A|,|B|,|C|<=50 (a = e-2)",
      f"{mp.nstr(best[0], 8)} at (A,B,C)={best[1]}", best[0] > mp.mpf("1e-12"))
print("F7a CONCLUSION: CF(e-2) is non-eventually-periodic (Euler pattern, verified in")
print("  window; no small periodic fit); no integer quadratic with |coeffs|<=50 comes")
print("  within 1e-12; e is transcendental (Hermite). By Lagrange + the Mobius-fixed-")
print("  point direction, NO nontrivial substitution fixes the slope-(e-2) Sturmian")
print("  word: the non-quadratic stratum carries NO self-similar generator at all —")
print("  there is no carrier to compare. F7a stratum verdict: ROBUST.")

# ============================================================================
# PART B — F7b: the quadratic NON-metallic stratum. Witness slope sqrt(3)-1,
# CF period (1,2). Construct the composite substitution, its carrier bundle,
# and measure hyperbolicity / volume / trace field / faces.
# ============================================================================
print("\n--- PART B: F7b — the sqrt(3)-1 stratum (CF period (1,2)) ---")

# (B1) exact slope facts
s3 = sp.sqrt(3)
xw = s3 - 1
CHECK("F7b CF(sqrt(3)-1) (sympy, exact)", continued_fraction_periodic(-1, 1, 3),
      continued_fraction_periodic(-1, 1, 3) == [0, [1, 2]])
CHECK("F7b minpoly(sqrt(3)-1)", sp.minimal_polynomial(xw, x),
      sp.minimal_polynomial(xw, x) == x**2 + 2 * x - 2)
# not metallic for ANY m: metallic [0;m,m,...] satisfies x^2+mx-1=0; subtracting
# the minpoly forces (m-2)x + 1 = 0, i.e. m = 2 - 1/x — irrational, so no integer m.
m_needed = sp.simplify(2 - 1 / xw)
CHECK("F7b unique m with sqrt(3)-1 = [0;m,m,...] would be", m_needed,
      m_needed == sp.Rational(3, 2) - s3 / 2 and not m_needed.is_integer)
CHECK("F7b metallic exclusion (m=1..50, exact)", "all nonzero",
      all(sp.simplify(xw**2 + m * xw - 1) != 0 for m in range(1, 51)))
# T4-extremality fails here: Lagrange number of the (1,2)-periodic word = 2*sqrt(3)
fwd2 = 1 + s3            # [2;1,2,1,...] : z = 2 + 1/(1 + 1/z) => z^2 = 2z + 2
bwd2 = s3 - 1            # [0;1,2,1,...]
fwd1 = (1 + s3) / 2      # [1;2,1,2,...]
bwd1 = 1 / (1 + s3)      # [0;2,1,2,...]
Lnum = sp.simplify(sp.Max(fwd2 + bwd2, fwd1 + bwd1))
CHECK("F7b Lagrange number of the (1,2)-word", Lnum,
      sp.simplify(Lnum - 2 * s3) == 0 and Lnum > sp.sqrt(5))
CHECK("F7b Lagrange number exceeds Hurwitz bottom sqrt(5) (T4 extremality fails)",
      f"2*sqrt(3) = {sp.N(Lnum, 10)} > sqrt(5) = {sp.N(sp.sqrt(5), 10)}", True)

# (B2) the composite substitution for CF period (1,2):
# standard Sturmian morphisms rho_k: a -> a^k b, b -> a; sigma = rho_1 o rho_2
def rho(kk):
    return {"a": "a" * kk + "b", "b": "a"}

def apply(sub, w):
    return "".join(sub[c] for c in w)

rho1, rho2 = rho(1), rho(2)
sigma = {"a": apply(rho1, rho2["a"]), "b": apply(rho1, rho2["b"])}
CHECK("F7b composite substitution sigma", f"a->{sigma['a']}, b->{sigma['b']}",
      sigma == {"a": "ababa", "b": "ab"})
Mab = sp.Matrix([[sigma["a"].count("a"), sigma["b"].count("a")],
                 [sigma["a"].count("b"), sigma["b"].count("b")]])
M1 = sp.Matrix([[1, 1], [1, 0]])
M2 = sp.Matrix([[2, 1], [1, 0]])
CHECK("F7b abelianization = [[1,1],[1,0]]*[[2,1],[1,0]]",
      f"{Mab.tolist()} tr={Mab.trace()} det={Mab.det()}",
      Mab == M1 * M2 and Mab == sp.Matrix([[3, 1], [2, 1]])
      and Mab.trace() == 4 and Mab.det() == 1)
CHECK("F7b monodromy class Anosov (|tr| = 4 > 2, det = +1)", "yes",
      abs(Mab.trace()) > 2 and Mab.det() == 1)
# primitivity: all entries of Mab positive
CHECK("F7b sigma primitive (all abelianization entries > 0)", "yes",
      all(e > 0 for e in Mab))

# dilatation and its field vs the golden/metallic side
lam = max(Mab.eigenvals().keys(), key=lambda e: sp.N(e))
plam = sp.minimal_polynomial(lam, x)
CHECK("F7b dilatation lambda", lam, sp.simplify(lam - (2 + s3)) == 0)
CHECK("F7b dilatation minpoly", plam, plam == x**2 - 4 * x + 1)
CHECK("F7b dilatation norm +1 (every metallic mean has norm -1)",
      f"const coeff {plam.coeff(x, 0)}", plam.coeff(x, 0) == 1)
CHECK("F7b dilatation field Q(sqrt(3)): sqfree disc", sqfree(16 - 4),
      sqfree(16 - 4) == 3)
# 3 | m^2+4 is impossible mod 3 => NO metallic mean lies in Q(sqrt(3)) at all
CHECK("F7b m^2+4 mod 3 takes values", sorted({(m * m + 4) % 3 for m in range(3)}),
      0 not in {(m * m + 4) % 3 for m in range(3)})
CHECK("F7b Q(sqrt(3)) contains NO metallic mean (3 never divides m^2+4)", "proved mod 3",
      True)
CHECK("F7b hearing face: nfisisom(x^2-4x+1, x^2-3x+1) [Q(sqrt3) vs golden Q(sqrt5)]",
      str(pari("nfisisom(x^2-4*x+1, x^2-3*x+1)")),
      str(pari("nfisisom(x^2-4*x+1, x^2-3*x+1)")) == "0")

# (B3) the fixed word is Sturmian of a slope PGL2(Z)-equivalent to sqrt(3)-1
w = "a"
while len(w) < 40000:
    w = apply(sigma, w)
CHECK("F7b fixed point: sigma(prefix) extends prefix", "yes",
      apply(sigma, w)[:len(w)] == w)
N = len(w)
pref = [0] * (N + 1)
for i, c in enumerate(w):
    pref[i + 1] = pref[i] + (1 if c == "b" else 0)
balanced = True
for n in range(1, 31):
    counts = [pref[i + n] - pref[i] for i in range(N - n + 1)]
    if max(counts) - min(counts) > 1:
        balanced = False
CHECK("F7b prefix (len %d) is 1-balanced for window lengths 1..30" % N, balanced,
      balanced)
complexity_ok = all(len({w[i:i + n] for i in range(N - n + 1)}) == n + 1
                    for n in range(1, 16))
CHECK("F7b factor complexity p(n) = n+1 for n = 1..15 (Sturmian signature)",
      complexity_ok, complexity_ok)
slope = sp.simplify((3 - s3) / 3)  # b-frequency from the Perron eigenvector
freq = pref[N] / N
CHECK("F7b letter-b frequency vs Perron slope (3-sqrt(3))/3",
      f"|{freq:.7f} - {float(slope):.7f}| = {abs(freq - float(slope)):.2e}",
      abs(freq - float(slope)) < 1e-3)
CHECK("F7b slope CF (sympy, exact)", sp.continued_fraction(slope),
      sp.continued_fraction(slope) == [0, 2, [2, 1]])
# exact PGL2(Z) tail-equivalence with sqrt(3)-1: slope = (x+2)/(2x+5), det 1
CHECK("F7b slope = (x+2)/(2x+5) at x = sqrt(3)-1, det[[1,2],[2,5]] = 1",
      f"{sp.simplify(slope - (xw + 2) / (2 * xw + 5)) == 0}, det = {1 * 5 - 2 * 2}",
      sp.simplify(slope - (xw + 2) / (2 * xw + 5)) == 0)

# (B4) the carrier bundle: mapping torus of the once-punctured torus, monodromy Mab
# RL-word: R*L*L = [[3,1],[2,1]] — hence snappy bundle string 'b++RLL'
CHECK("F7b R*L*L", (R * L * L).tolist(), R * L * L == Mab)
Nman = snappy.Manifold("b++RLL")
NHP = snappy.ManifoldHP("b++RLL")
CHECK("F7b carrier solution type", NHP.solution_type(),
      NHP.solution_type() == "all tetrahedra positively oriented")
CHECK("F7b carrier hyperbolic", "YES (geometric solution)", True)
CHECK("F7b carrier orientable / #cusps", f"{Nman.is_orientable()} / {Nman.num_cusps()}",
      Nman.is_orientable() and Nman.num_cusps() == 1)
volN = NHP.volume()
CHECK("F7b carrier volume", str(volN)[:32],
      abs(float(volN) - 2.66674478344905979) < 1e-12)

# identification by TWO independent invariants + homology (instrument rule)
m009 = snappy.Manifold("m009")
CHECK("F7b identify()", str(Nman.identify()), "m009" in str(Nman.identify()))
CHECK("F7b is_isometric_to(m009)", Nman.is_isometric_to(m009),
      Nman.is_isometric_to(m009))
CHECK("F7b volume match vs census m009",
      f"|{float(volN):.12f} - {float(m009.volume()):.12f}| = "
      f"{abs(float(volN) - float(m009.volume())):.2e}",
      abs(float(volN) - float(m009.volume())) < 1e-9)
CHECK("F7b homology match vs m009", f"{Nman.homology()} vs {m009.homology()}",
      str(Nman.homology()) == str(m009.homology()))
# conjugate-word consistency (construction fidelity)
CHECK("F7b cyclic words b++LLR, b++LRL isometric to carrier",
      "both True",
      snappy.Manifold("b++LLR").is_isometric_to(Nman)
      and snappy.Manifold("b++LRL").is_isometric_to(Nman))

# (B5) knot-ness face: H1 = Z + coker(A - I) (Wang sequence), exact SNF
snf = smith_normal_form(Mab - sp.eye(2))
CHECK("F7b SNF(A - I)", snf.tolist(), snf == sp.Matrix([[1, 0], [0, 2]]))
CHECK("F7b H1 = Z + Z/2 (Wang prediction == snappy)",
      str(Nman.homology()), str(Nman.homology()) == "Z/2 + Z")
CHECK("F7b knot-ness face (H1 = Z)", "ABSENT (H1 has Z/2 torsion)", True)

# (B6) trace field, exactly. Shapes at 64 digits, algdep-guarded, then the
# geometric solution is certified EXACTLY in Q(sqrt(-7)) via the gluing equations.
shapes = NHP.tetrahedra_shapes("rect")
shape_polys = []
for j, z in enumerate(shapes):
    pz, dz = algdep_guarded(pnum(z), 4, f"shape z{j}")
    shape_polys.append(pz)
CHECK("F7b shape minpolys", [str(p) for p in shape_polys],
      [str(p) for p in shape_polys] == ["x^2 - x + 2", "x^2 - x + 2", "x^2 + x + 2"])
CHECK("F7b shape-field disc (squarefree part) for all shapes",
      [sqfree(1 - 8), sqfree(1 - 8), sqfree(1 - 8)],
      sqfree(1 - 8) == -7)
# exact shapes (roots with positive imaginary part, matching the HP values)
i7 = sp.sqrt(7) * sp.I
zex = [(1 + i7) / 2, (1 + i7) / 2, (-1 + i7) / 2]
for j, (z, ze) in enumerate(zip(shapes, zex)):
    diff = (pnum(z) - pari(str(sp.N(ze, 70)))).abs()
    CHECK(f"F7b |HP shape z{j} - exact root| < 1e-55", f"{float(diff):.3e}",
          diff < pari("1.0e-55"))
# EXACT verification of every gluing equation (rect): prod z^A (1-z)^B = sign
glue_ok = True
for (Arow, Brow, sgn) in NHP.gluing_equations("rect"):
    expr = sp.Integer(1)
    for zj, aj, bj in zip(zex, Arow, Brow):
        expr *= zj**aj * (1 - zj)**bj
    if sp.simplify(expr - sgn) != 0:
        glue_ok = False
CHECK("F7b ALL rect gluing+cusp equations satisfied EXACTLY in Q(sqrt(-7))",
      glue_ok, glue_ok)
CHECK("F7b shape field (= invariant trace field, Neumann-Reid for cusped M)",
      "Q(sqrt(-7))", True)

# factornf exact confirmation of the field, and of the being-face verdict
n7, f7 = splits_over("t^2 - t + 2", "x^2 + 7")
CHECK("F7b factornf(x^2+7) over Q[t]/(t^2-t+2) #factors [sqrt(-7) IN field]",
      n7, n7 == 2)
n3b, _ = splits_over("t^2 - t + 2", "x^2 + 3")
CHECK("F7b factornf(x^2+3) over Q[t]/(t^2-t+2) #factors [sqrt(-3) NOT in field]",
      n3b, n3b == 1)
CHECK("F7b nfisisom(x^2-x+2, x^2+7)", str(pari("nfisisom(x^2-x+2, x^2+7)")),
      str(pari("nfisisom(x^2-x+2, x^2+7)")) != "0")
CHECK("F7b nfisisom(x^2-x+2, x^2+3) [being field]",
      str(pari("nfisisom(x^2-x+2, x^2+3)")),
      str(pari("nfisisom(x^2-x+2, x^2+3)")) == "0")
CHECK("F7b BEING face (trace field Q(sqrt(-3)))",
      "ABSENT — invariant trace field is Q(sqrt(-7))", True)

# (B7) independent trace-route cross-check + arithmeticity (verified, not cited)
G = NHP.fundamental_group()
CHECK("F7b pi_1 two-generator presentation", f"gens={G.num_generators()}, "
      f"relator={G.relators()[0]}", G.num_generators() == 2)
ga = G.SL2C("a")
gb = G.SL2C("b")
gab = ga * gb
tra = ga[0][0] + ga[1][1]
trb = gb[0][0] + gb[1][1]
trab = gab[0][0] + gab[1][1]
pa, da = algdep_guarded(pnum(tra), 6, "tr(a)")
pb, db = algdep_guarded(pnum(trb), 6, "tr(b)")
pc, dc = algdep_guarded(pnum(trab), 6, "tr(ab)")
CHECK("F7b minpoly tr(a)", str(pa), str(pa) == "x^4 - 5*x^2 + 8")
CHECK("F7b minpoly tr(b)", str(pb), str(pb) == "x^4 - 10*x^2 + 32")
CHECK("F7b minpoly tr(ab)", str(pc), str(pc) == "x + 2")
monic = all(int(p.Vec()[0]) == 1 for p in (pa, pb, pc))
CHECK("F7b tr(a), tr(b), tr(ab) all ALGEBRAIC INTEGERS (monic integral minpolys)",
      monic, monic)
print("  Fricke: for a 2-generator group every trace is an INTEGER polynomial in")
print("  (tr a, tr b, tr ab); all three are algebraic integers, hence ALL traces of")
print("  Gamma are algebraic integers.")
# parabolic certificate for non-cocompactness: tr(ab) = -2, ab != -I
offdiag = (pnum(gab[0][1])).abs()
CHECK("F7b ab parabolic: tr(ab) = -2 and |ab[0][1]| > 0.1 (ab != -I)",
      f"tr = -2, |offdiag| = {float(offdiag):.6f}", offdiag > pari("0.1"))
# invariant-trace-field cross-check from squares: tr(g^2) = tr(g)^2 - 2
pa2, _ = algdep_guarded(pnum(tra * tra - 2), 4, "tr(a^2)")
pb2, _ = algdep_guarded(pnum(trb * trb - 2), 4, "tr(b^2)")
CHECK("F7b minpoly tr(a^2)", str(pa2), str(pa2) == "x^2 - x + 2")
CHECK("F7b minpoly tr(b^2) (disc -28, same field Q(sqrt(-7)))", str(pb2),
      str(pb2) == "x^2 - 6*x + 16" and sqfree(36 - 64) == -7)
CHECK("F7b invariant trace field via traces AGREES with shape field", "Q(sqrt(-7))",
      True)
# Maclachlan-Reid identification (non-cocompact case): arithmetic <=>
# invariant trace field imaginary quadratic AND all traces algebraic integers.
CHECK("F7b ARITHMETICITY (Maclachlan-Reid, verified: kG = Q(sqrt(-7)) imaginary "
      "quadratic; all traces integral; cusped)", "YES — commensurable with PSL2(O_-7)",
      True)
# Humbert-volume consistency: vol / covol(PSL2(O_-7)) should be a small integer
mp.mp.dps = 50
chi = {1: 1, 2: 1, 3: -1, 4: 1, 5: -1, 6: -1}
Lchi = sum(chi[r] * mp.zeta(2, mp.mpf(r) / 7) for r in range(1, 7)) / 49
covol = mp.mpf(7) ** mp.mpf("1.5") * mp.zeta(2) * Lchi / (4 * mp.pi ** 2)
ratio = mp.mpf(str(volN)) / covol
CHECK("F7b vol / covol(PSL2(O_-7)) [Humbert]", mp.nstr(ratio, 12),
      abs(ratio - 3) < mp.mpf("1e-9"))
# commensurability with the banked carrier is EXCLUDED exactly:
CHECK("F7b commensurable with m004?", "NO — invariant trace fields differ "
      "(Q(sqrt(-7)) vs Q(sqrt(-3)); commensurable groups share kG)", True)

# (B8) cusp/interface face
cusp = NHP.cusp_info()[0]["shape"]
pcusp, _ = algdep_guarded(pnum(cusp), 4, "cusp shape")
CHECK("F7b cusp shape minpoly", str(pcusp), str(pcusp) == "8*x^2 + 2*x + 1")
CHECK("F7b cusp shape exact", "(-1 + i*sqrt(7))/8 — cusp field Q(sqrt(-7))",
      sqfree(4 - 32) == -7)
cdiff = (pnum(cusp) - pari(str(sp.N((-1 + i7) / 8, 70)))).abs()
CHECK("F7b |HP cusp shape - exact| < 1e-55", f"{float(cdiff):.3e}",
      cdiff < pari("1.0e-55"))
CHECK("F7b INTERFACE face (cusp)", "PRESENT (1 cusp) — but cusp field Q(sqrt(-7)), "
      "not the banked Q(sqrt(-3))", True)

# (B9) FRAGILE-reachability witness (MB12 / earned-ROBUST duty): the sibling
# punctured-torus-bundle carrier m003 DOES carry the being field Q(sqrt(-3)) —
# so absence of Q(sqrt(-3)) at the (1,2) stratum is informative, not automatic.
m003 = snappy.ManifoldHP("m003")
z003 = m003.tetrahedra_shapes("rect")[0]
p003, _ = algdep_guarded(pnum(z003), 4, "m003 shape")
CHECK("F7b vacuity witness: m003 (a fellow punctured-torus-bundle carrier) shape "
      "minpoly", str(p003), str(p003) == "x^2 - x + 1")
CHECK("F7b vacuity witness: m003 carries the being field Q(sqrt(-3)), vol",
      str(snappy.Manifold("m003").volume())[:12],
      abs(float(snappy.Manifold("m003").volume()) - 2.029883212819) < 1e-9)

# (B10) face table and stratum verdict
print("\nF7b FACE TABLE (carrier = b++RLL = m009, vs banked m004 anatomy):")
faces = [
    ("being (trace field Q(sqrt(-3)))", "ABSENT — field is Q(sqrt(-7)), factornf-certified"),
    ("hearing (golden / Q(sqrt(5)))", "ABSENT — dilatation 2+sqrt(3) in Q(sqrt(3)); "
     "no metallic mean lies in Q(sqrt(3)) (mod-3 proof); norm +1 vs metallic -1"),
    ("cusp/interface", "PRESENT structurally (1 cusp) — field Q(sqrt(-7)) differs"),
    ("arithmeticity", "PRESENT — over Q(sqrt(-7)): a DIFFERENT Bianchi class, "
     "provably incommensurable with the banked carrier"),
    ("knot-ness (H1 = Z)", "ABSENT — H1 = Z + Z/2"),
]
for f, v in faces:
    print(f"  {f}: {v}")
CHECK("F7b banked-specific anatomy markers failed "
      "{being field, golden hearing, knot-ness}", "3 of 3 (>= 2 required)", True)
print("F7b CONCLUSION: the quadratic-non-metallic carrier is a genuine cusped")
print("  hyperbolic (even arithmetic) manifold — hyperbolicity and arithmeticity per")
print("  se do NOT discriminate — but it carries NONE of the banked V4 anatomy:")
print("  wrong being field, hearing side field-disjoint from every metallic mean,")
print("  no knot-ness; and it is incommensurable with m004. The metallic (indeed")
print("  golden) selection is what pins the specific fields. T4's extremality is the")
print("  selector (Lagrange number 2*sqrt(3) > sqrt(5) here) and its price is now")
print("  measured: it buys the fields, not the existence of a hyperbolic carrier.")
print("  F7b stratum verdict: ROBUST.")

# ============================================================================
# PART C — F7c: the metallic stratum itself.
# ============================================================================
print("\n--- PART C: F7c — metallic stratum ---")
print("F7c: covered by fork F3 (the silver m=2 bundle); cross-reference only, no")
print("  duplicate measurement here, per the sealed design.")
CHECK("F7c cross-reference to F3", "as sealed (no computation in F7)", True)

# ============================================================================
# VERDICT
# ============================================================================
print("\n" + "=" * 78)
CHECK("F7 VERDICT (covers strata a AND b)", "ROBUST", True)
print("F7 = ROBUST — earned:")
print("  F7a: the non-quadratic stratum admits NO self-similar generator (CF non-")
print("       periodicity computed on the e-2 witness; Lagrange; Mobius-fixed-point")
print("       direction) — there is no sibling carrier at all outside the quadratic")
print("       class.")
print("  F7b: the quadratic-non-metallic carrier exists and is hyperbolic and")
print("       arithmetic (both verified) yet lacks every banked-specific anatomy")
print("       marker: being field Q(sqrt(-3)) ABSENT (field = Q(sqrt(-7)),")
print("       factornf-exact), golden hearing ABSENT (dilatation field Q(sqrt(3))")
print("       contains no metallic mean, mod-3 exact), knot-ness ABSENT (H1 =")
print("       Z + Z/2, Wang-exact). Absence is informative: the fellow bundle")
print("       carrier m003 DOES carry Q(sqrt(-3)) (computed), so the being face was")
print("       reachable in this family — FRAGILE was a live outcome.")
print("  Prior (F7 ROBUST) is CONFIRMED — no contra-prior skeptic triggered.")
print("Verdict is journal-only; nothing enters CLAIMS; Gate 5 absolute.")
print(f"\nTotal CHECK lines: {len(checks)}")
