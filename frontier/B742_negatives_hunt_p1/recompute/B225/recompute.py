"""B739 Stage-B recompute -- target B225 (dead-probe, kill_form=base-rate, fact_basis=proxy).

BANKED KILL (B225/FINDINGS.md): the "2 = octahedral parent" half of chat1's conductor
decomposition (40 = 2^3*5 = (octahedral parent 2) x (golden filling 5)) is refuted because
prime 2 appears in the bad-prime set of the SL(2,C) character variety of EVERY 2-bridge knot
computed -- twist (Whitehead fillings: 4_1,5_2,6_1,7_2) AND non-twist (6_2,6_3,7_6,8_3,8_8,9_4)
-- so 2 does not discriminate the octahedral parent.

THE DISCRIMINATING FACT to recompute (E19, both directions):
  "2 is in the bad-prime extraction (disc of the z-branch locus of the Riley trace-coordinate
   character variety) for all 10 knots, in particular for the 6 NON-twist knots."
Direction 1: re-derive that fact from the arc's own declared conventions (independent
implementation + a numerical SL(2,C)-representation verification the arc never ran).
Direction 2: test whether the fact is DISCRIMINATING -- i.e. whether the extraction could ever
have reported "2 absent" for any knot at all.

ARC'S DECLARED CONVENTIONS (B225/conductor_test.py, followed exactly):
  A = [[s,1],[0,1/s]], B = [[s,0],[-u,1/s]]; relator  A.w = w.B ;
  w = b^{e1} a^{e2} b^{e3} ... (alternating, starting with b, length p-1), e_i = (-1)^floor(iq/p);
  rep-condition polynomial = numerator of (A.w - w.B)[0,1], palindromic in s, rewritten via
  s^j + s^-j -> p_j(x)  (x = s + 1/s);  z = tr(AB) = (x^2-2) - u;
  branch locus = content-stripped disc_z(Phi);  bad primes = primes of disc_x + primes of LC;
  fallback over the mirror-closed class [q, q^-1 mod p, p-q, p-(q^-1 mod p)].

E1 DECLARATIONS (conventions the arc left implicit, chosen here and declared):
  (D1) (p,q) inputs: arc-committed rows kept verbatim: 4_1=(5,2), 5_2=(7,3), 6_2=(11,3),
       6_3=(13,5), 7_6=(19,7), 8_3=(17,4). The four FINDINGS-only knots use standard Schubert
       fractions: 6_1=(9,2), 7_2=(11,2) (twist form p/2, matching the arc's 4_1=(5,2) style),
       8_8=(25,9), 9_4=(21,5). Only the mirror-closed class matters (arc's own fallback).
  (D2) twist-knot test (Whitehead-filling criterion, the arc's operationalization): the
       mirror-closed class of q contains 2 or p-2  <=>  fraction ~ p/2  <=>  twist knot.
  (D3) determinant sanity: p must equal the standard determinant of the named knot
       (4_1:5, 5_2:7, 6_1:9, 6_2:11, 6_3:13, 7_2:11, 7_6:19, 8_3:17, 8_8:25, 9_4:21).
  (D4) factorization bound: the arc full-factorints disc; huge cofactors make that
       non-terminating in general, so bad primes are reported as {v_2, all primes <= 10^4
       dividing lc*disc, cofactor digit count}. The kill's boolean (2 in bad) is exactly v_2>0
       or 2|lc, unaffected by the bound.
  (D5) squarefree repair: where the branch locus is NOT squarefree (found: 6_3, 8_3) the arc's
       disc is 0 (its factorint(0) contributes a literal '0' to the bad set and 2 enters only
       via LC); both the arc-exact behavior and the repaired convention (squarefree part first)
       are computed and reported.
  (D6) numerical verification slice: x0 = 7/3 exactly, mpmath dps = 60, all z-roots of
       Phi(7/3,z); representation residual = max entry of |A.W - W.B|; threshold 1e-40.
  (D7) controls: Weierstrass minimal models 11a3: y^2+y = x^3-x^2 ([0,-1,1,0,0]) and
       37a1: y^2+y = x^3-x ([0,0,1,-1,0]); good reduction at 2 is PROVED in-script via the
       standard b-invariant discriminant formula (Delta = -11, 37: odd), no external data.

Deterministic: no wall-clock, no randomness, no network. Needs sympy + mpmath only.
Gate 5: pure arithmetic geometry of character varieties; no SM quantities.
"""
import sympy as sp
import mpmath as mp

s, u, x, z, X = sp.symbols('s u x z X')

A  = sp.Matrix([[s, 1], [0, 1/s]])
B  = sp.Matrix([[s, 0], [-u, 1/s]])
Ai = A.inv()
Bi = B.inv()

KNOTS = [
    # name,  p,  q,  provenance of (p,q)
    ("4_1", 5, 2, "arc-committed"),
    ("5_2", 7, 3, "arc-committed"),
    ("6_1", 9, 2, "E1-declared (twist p/2)"),
    ("7_2", 11, 2, "E1-declared (twist p/2)"),
    ("6_2", 11, 3, "arc-committed"),
    ("6_3", 13, 5, "arc-committed"),
    ("7_6", 19, 7, "arc-committed"),
    ("8_3", 17, 4, "arc-committed"),
    ("8_8", 25, 9, "E1-declared (Schubert 25/9)"),
    ("9_4", 21, 5, "E1-declared (Schubert 21/5)"),
]
STANDARD_DET = {"4_1": 5, "5_2": 7, "6_1": 9, "6_2": 11, "6_3": 13,
                "7_2": 11, "7_6": 19, "8_3": 17, "8_8": 25, "9_4": 21}


def v2(n):
    n = abs(int(n))
    if n == 0:
        return None  # v2(0) undefined/infinite
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def mirror_class(p, q):
    qi = pow(q, -1, p)
    return sorted({q % p, qi, (p - q) % p, (p - qi) % p})


def is_twist(p, q):
    cl = mirror_class(p, q)
    return (2 in cl) or ((p - 2) % p in cl)


def eps(i, p, q):
    return (-1) ** ((i * q) // p)


def word_letters(p, q):
    return [('b' if i % 2 == 1 else 'a', eps(i, p, q)) for i in range(1, p)]


def word(p, q):
    W = sp.eye(2)
    for g, e in word_letters(p, q):
        M = (B if e == 1 else Bi) if g == 'b' else (A if e == 1 else Ai)
        W = (W * M).applyfunc(sp.expand)
    return W


def cheb_pj(j):
    """p_j(x) with s^j + s^-j = p_j(s + 1/s)."""
    a, b = sp.Integer(2), x
    if j == 0:
        return a
    for _ in range(2, j + 1):
        a, b = b, sp.expand(x * b - a)
    return b


def phi_try(p, q):
    """Riley trace-coordinate nonabelian character-variety polynomial Phi(x,z), arc convention."""
    W = word(p, q)
    n01 = sp.fraction(sp.together((A * W - W * B)[0, 1]))[0]
    P = sp.Poly(sp.expand(n01), s)
    co = P.all_coeffs()[::-1]           # ascending in s
    nz = [i for i, c in enumerate(co) if c != 0]
    if not nz:
        return None
    body = co[nz[0]:nz[-1] + 1]
    d = len(body) - 1
    if d % 2:
        return None
    h = d // 2
    if not all(sp.expand(body[k] - body[d - k]) == 0 for k in range(h + 1)):
        return None                     # not palindromic -> wrong class representative
    rx = body[h] + sum(body[h + j] * cheb_pj(j) for j in range(1, h + 1))
    F = sp.expand(sp.expand(rx).subs(u, x**2 - 2 - z))
    if sp.Poly(F, z).degree() < 1 or sp.Poly(F, x).degree() < 1:
        return None
    return F


def char_variety(p, q):
    for qq in [q, pow(q, -1, p), p - q, (p - pow(q, -1, p)) % p]:
        if 0 < qq < p:
            F = phi_try(p, qq)
            if F is not None:
                return F, qq
    return None, None


def numeric_rep_check(F, p, qq):
    """Independent verification the arc never ran: every root z0 of Phi(x0,z0)=0 really gives
    an SL(2,C) representation of the 2-bridge group (residual |A.W - W.B| ~ 0)."""
    mp.mp.dps = 60
    x0 = mp.mpf(7) / mp.mpf(3)
    Pz = sp.Poly(F.subs(x, sp.Rational(7, 3)), z)
    coeffs = [mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q) for c in Pz.all_coeffs()]
    roots = mp.polyroots(coeffs, maxsteps=200, extraprec=120)
    s0 = (x0 + mp.sqrt(x0 * x0 - 4)) / 2
    worst = mp.mpf(0)
    for z0 in roots:
        u0 = x0 * x0 - 2 - z0
        An = mp.matrix([[s0, 1], [0, 1 / s0]])
        Bn = mp.matrix([[s0, 0], [-u0, 1 / s0]])
        Ain = mp.matrix([[1 / s0, -1], [0, s0]])
        Bin = mp.matrix([[1 / s0, 0], [u0, s0]])
        Wn = mp.eye(2)
        for g, e in word_letters(p, qq):
            M = (Bn if e == 1 else Bin) if g == 'b' else (An if e == 1 else Ain)
            Wn = Wn * M
        R = An * Wn - Wn * Bn
        worst = max(worst, max(abs(R[i, j]) for i in range(2) for j in range(2)))
    return len(roots), worst


def branch_locus(F):
    """content-stripped disc_z(Phi) (arc convention)."""
    D = sp.Poly(sp.expand(sp.discriminant(sp.Poly(sp.expand(F), z), z)), x)
    c = sp.gcd(D.all_coeffs())
    return sp.Poly(sp.expand(D.as_expr() / c), x)


def squarefree_part(P):
    g = sp.gcd(P, P.diff(x))
    return sp.quo(P, g) if g.degree() > 0 else P, (g.degree() == 0)


def small_primes_of(n, bound=10**4):
    n = abs(int(n))
    out = []
    if n == 0:
        return out, n
    for pr in sp.primerange(2, bound):
        if n % pr == 0:
            out.append(int(pr))
            while n % pr == 0:
                n //= pr
    return out, n  # n = unfactored cofactor


def mod2_square_data(P, var):
    """factor P mod 2; return (factor_list, all_exponents_even, sqrt-verified)."""
    P2 = sp.Poly(P.as_expr(), var, modulus=2)
    if P2.degree() < 0 or P2.is_zero:
        return None, None, None
    fl = sp.factor_list(P2.as_expr(), var, modulus=2)
    nontriv = [(f, e) for f, e in fl[1] if sp.Poly(f, var, modulus=2).degree() > 0]
    alleven = all(e % 2 == 0 for _, e in nontriv)
    if alleven:
        Vbar = sp.Integer(1)
        for f, e in nontriv:
            Vbar *= f ** (e // 2)
        ok = sp.Poly(sp.expand(Vbar**2) - P2.as_expr(), var, modulus=2).is_zero
    else:
        ok = False
    return fl[1], alleven, ok


def weierstrass_delta(a1, a2, a3, a4, a6):
    b2 = a1**2 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3**2 + 4 * a6
    b8 = (b2 * b6 - b4**2) // 4 if (b2 * b6 - b4**2) % 4 == 0 else sp.Rational(b2 * b6 - b4**2, 4)
    return -b2**2 * b8 - 8 * b4**3 - 27 * b6**2 + 9 * b2 * b4 * b6


print("=" * 100)
print("B739 Stage-B recompute of B225's discriminating fact (E19 compute-not-cite, both directions)")
print("=" * 100)

# ---------------------------------------------------------------- PART 1: pipeline re-derivation
print("\nPART 1 -- pipeline re-derived from the arc's declared conventions (independent implementation)")
results = {}
for nm, p, q, prov in KNOTS:
    assert p == STANDARD_DET[nm], f"determinant mismatch for {nm}"
    F, qq = char_variety(p, q)
    assert F is not None, f"no palindromic representative for {nm}"
    Pz = sp.Poly(F, z)
    degz = Pz.degree()
    monic = (sp.Poly(F, z, domain=sp.ZZ[x]).LC() == 1)
    even = (sp.expand(F.subs(x, -x) - F) == 0)
    proper = (sp.expand(F.subs(z, x**2 - 2)) != 0)  # not containing the abelian line z=x^2-2
    assert degz == (p - 1) // 2, f"deg_z != (p-1)/2 for {nm}"
    nroots, resid = numeric_rep_check(F, p, qq)
    assert resid < mp.mpf('1e-40'), f"numeric representation check FAILED for {nm}"
    results[nm] = dict(p=p, q=q, qq=qq, F=F, degz=degz, monic=monic, even=even,
                       twist=is_twist(p, qq), prov=prov)
    print(f"  {nm:4} b({p},{q})->class rep qq={qq:2}  [{prov}]  deg_z={degz:2} =(p-1)/2  "
          f"monic_z={monic}  even_in_x={even}  proper(nonabelian)={proper}  "
          f"rep-check: {nroots} roots, residual<1e-40: True")
    assert monic and even and proper

Phi41 = results["4_1"]["F"]
anchor = sp.expand(Phi41 - (z**2 - (x**2 + 1) * z + (2 * x**2 - 1)))
print(f"\n  ANCHOR (B211): Phi(4_1) == z^2-(x^2+1)z+(2x^2-1) exactly: {anchor == 0}")
assert anchor == 0

# ---------------------------------------------------------- PART 2: the banked table, recomputed
print("\nPART 2 -- Direction 1: the banked discriminating fact, recomputed per knot")
print(f"  {'knot':5} {'b(p,qq)':9} {'type':9} {'sqfree(D)':9} {'v2(disc Dsf)':12} {'v2(lc Dsf)':10} "
      f"{'2 in bad':8} {'small primes<=10^4 of lc*disc':30} cofactor")
table2 = {}
for nm, p, q, prov in KNOTS:
    r = results[nm]
    D = branch_locus(r["F"])
    Dsf, was_sf = squarefree_part(D)
    disc = int(sp.discriminant(Dsf, x))
    lc = int(Dsf.LC())
    vdisc = v2(disc)
    vlc = v2(lc) if abs(lc) > 1 else 0
    two_in_bad = (vdisc is not None and vdisc > 0) or (vlc > 0)
    sm, cof = small_primes_of(lc * disc)
    r.update(D=D, Dsf=Dsf, disc=disc, lc=lc, vdisc=vdisc, vlc=vlc, two=two_in_bad, was_sf=was_sf)
    typ = "twist" if r["twist"] else "NON-twist"
    cofs = "1" if cof == 1 else f"{len(str(cof))}digits"
    print(f"  {nm:5} b({p},{r['qq']:2})  {typ:9} {str(was_sf):9} {str(vdisc):12} {str(vlc):10} "
          f"{str(two_in_bad):8} {str(sm):30} {cofs}")
    table2[nm] = two_in_bad

n_twist = sum(1 for nm in table2 if results[nm]["twist"])
n_non = sum(1 for nm in table2 if not results[nm]["twist"])
print(f"\n  twist knots: {n_twist} (4_1,5_2,6_1,7_2)   NON-twist: {n_non} (6_2,6_3,7_6,8_3,8_8,9_4)")
print(f"  2 in bad-prime extraction for ALL 10/10 knots: {all(table2.values())}")

# arc-exact small cases + the non-squarefree wrinkle
D41 = results["4_1"]["D"]
bad41 = sorted(set(int(pp) for pp in sp.factorint(abs(int(sp.discriminant(D41, x)))))
               | set(int(pp) for pp in sp.factorint(abs(int(D41.LC()))) if int(D41.LC()) != 1))
D52 = results["5_2"]["D"]
bad52 = sorted(set(int(pp) for pp in sp.factorint(abs(int(sp.discriminant(D52, x)))))
               | set(int(pp) for pp in sp.factorint(abs(int(D52.LC()))) if abs(int(D52.LC())) != 1))
print(f"\n  arc-exact bad primes: 4_1 -> {bad41} (banked: [2,5] = conductor 40a1);  5_2 -> {bad52} (banked: [2,7])")
assert bad41 == [2, 5] and bad52 == [2, 7]
for nm in ("6_3", "8_3"):
    Dr = results[nm]["D"]
    d0 = int(sp.discriminant(Dr, x))
    print(f"  WRINKLE {nm}: branch locus NOT squarefree -> arc-exact disc(Dr) = {d0} "
          f"(arc's factorint(0)={{0:1}} put a literal 0 in its bad set; its '2' came from LC, "
          f"v2(LC)={v2(int(Dr.LC()))}); repaired (squarefree) convention above still gives 2 in bad.")

print(f"\n  (x^2-1) | branch locus (banked: only 4_1):")
for nm, p, q, prov in KNOTS:
    divides = sp.rem(results[nm]["D"], sp.Poly(x**2 - 1, x)).is_zero
    print(f"    {nm:5}: {divides}")
    assert divides == (nm == "4_1")
gold = sp.rem(D41, sp.Poly(x**2 - 5, x)).is_zero
print(f"  golden half (context, banked SOLID): (x^2-5) | D(4_1): {gold};  monodromy trace 3: t^2-4 = {3**2 - 4} = 5")
assert gold and 3**2 - 4 == 5

# ------------------------------------------- PART 3: Direction 2 -- is the fact DISCRIMINATING?
print("\nPART 3 -- Direction 2: specificity of the extraction at p=2")
print("""
  THEOREM (Vandermonde mod 2 / Stickelberger). For ANY f monic in z over Z[x]:
  disc_z(f) mod 2 = Vbar^2 is a SQUARE in F_2[x] (in char 2 the Vandermonde product
  V = prod_{i<j}(r_i - r_j) is fully symmetric, hence a polynomial in the coefficients).
  The branch locus D therefore reduces mod 2 to a square. Consequently, for Dsf =
  squarefree part of D with deg Dsf >= 1:
    (i)  if lc(Dsf) is even, 2 is in the bad set via the LC clause;
    (ii) if lc(Dsf) is odd, Dsf mod 2 keeps full (even) degree >= 2 and equals a square,
         hence is NOT squarefree mod 2, hence 2 | disc(Dsf) -- the disc clause.
  Either way the extraction reports 2. It reports 2 for EVERY monic-in-z input, i.e. its
  specificity at the prime 2 is ZERO: '2 in bad' cannot distinguish any knot from any other.
  (All ten Phi are monic in z -- asserted in Part 1.)
""")
print("  Empirical verification of the square structure, all 10 knots:")
print(f"  {'knot':5} {'Dsf mod 2 = square (x-level)':29} {'g mod 2 = square (X-level)':27} "
      f"{'v2(discX g)':11} {'v2(lc g)':8}")
for nm, p, q, prov in KNOTS:
    Dsf = results[nm]["Dsf"]
    fl, alleven, ok = mod2_square_data(Dsf, x)
    # X-level: Dsf is even in x (parity symmetry); write Dsf = gpoly(x^2)
    assert sp.expand(Dsf.as_expr().subs(x, -x) - Dsf.as_expr()) == 0
    Pg = sp.Poly(Dsf.as_expr(), x)
    assert all(m[0] % 2 == 0 for m in Pg.monoms())
    gexpr = sum(cf * X ** (m[0] // 2) for m, cf in zip(Pg.monoms(), Pg.coeffs()))
    gP = sp.Poly(sp.expand(gexpr), X)
    flX, allevenX, okX = mod2_square_data(gP, X)
    discX = int(sp.discriminant(gP, X))
    lcg = int(gP.LC())
    vX = v2(discX)
    vlcg = v2(lcg) if abs(lcg) > 1 else 0
    xlev = f"True(sqrt verified)" if ok else f"exps {[e for _, e in fl]}"
    Xlev = "True(sqrt verified)" if okX else (f"deg-drop; exps {[e for _, e in flX]}" if flX else "const")
    print(f"  {nm:5} {xlev:29} {Xlev:27} {str(vX):11} {str(vlcg):8}")
    assert alleven and ok
    assert (vX is not None and vX > 0) or vlcg > 0  # 2 fires at X-level too, and only via the square/LC mechanism

print("\n  CONTROLS -- same extraction on curves with PROVEN good reduction at 2:")
for label, (a1, a2, a3, a4, a6), Fc in [
        ("11a3: y^2+y=x^3-x^2", (0, -1, 1, 0, 0), z**2 + z - (x**3 - x**2)),
        ("37a1: y^2+y=x^3-x  ", (0, 0, 1, -1, 0), z**2 + z - (x**3 - x))]:
    Delta = int(weierstrass_delta(a1, a2, a3, a4, a6))
    assert Delta % 2 != 0
    Dc = branch_locus(Fc)
    Dcsf, _ = squarefree_part(Dc)
    dc = int(sp.discriminant(Dcsf, x))
    lcc = int(Dcsf.LC())
    smc, cofc = small_primes_of(lcc * dc)
    fired2 = (v2(dc) or 0) > 0 or (v2(lcc) or 0) > 0
    print(f"    {label}: Weierstrass Delta = {Delta} (ODD => good reduction at 2, computed in-script);")
    print(f"       extraction on Phi = {Fc}:  branch locus {Dcsf.as_expr()},  "
          f"bad-prime set {sorted(set(smc))} -> reports 2: {fired2}  <-- FALSE POSITIVE at 2")
    assert fired2

# ------------------------------------------------------------------------------- PART 4: verdict
print("\n" + "=" * 100)
print("PART 4 -- verdict assembly")
print("""
  Direction 1 (RECOMPUTED TRUE): the banked boolean table reproduces exactly under the arc's
  conventions -- 2 is in the bad-prime extraction for all 10 knots (4 twist + 6 non-twist),
  4_1 -> {2,5} = conductor of 40a1, 5_2 -> {2,7}, (x^2-1) | branch locus only for 4_1,
  and the golden half (x^2=5 branch = t^2-4 for trace 3) is SOLID.

  Direction 2 (NOT DISCRIMINATING): the recomputed fact is a TAUTOLOGY of the extraction, not a
  base-rate observation about 2-bridge knots. disc mod 2 of any monic-in-z polynomial is a
  square in F_2[x]; verified sqrt-exactly for all 10 branch loci at BOTH the SL (x) and PSL (X)
  levels; the extraction therefore fires '2 in bad' on EVERY possible input (specificity 0),
  and demonstrably fires on the 2-GOOD curves 11a3 (Delta=-11) and 37a1 (Delta=37).
  Likelihood ratio of the observation '2 present in non-twist knots' for the claim
  '2-part of the genuine conductor marks the octahedral parent' = 1. The kill's base-rate
  inference is vacuous at p=2. The only genuine conductor datum in the arc, 4_1 -> 40a1
  (N = 40, v2 = 3), is an octahedral (Whitehead-filling) child -- CONSISTENT with the claim
  the arc reported as refuted. The '2 = octahedral parent' half is REOPENED, undecided either
  way pending genuine (Jacobian-conductor) 2-parts of non-twist 2-bridge character varieties.

  VERDICT: REVIVED (prereg clause: recompute 'shows the banked fact was not discriminating
  (necessary-only, proxy, wrong object)'). No new positive structure is asserted (no E20 gate
  needed): the residue is the computed zero-specificity theorem + controls, not a claim that
  the decomposition holds.
""")
print("ALL CHECKS PASS")
