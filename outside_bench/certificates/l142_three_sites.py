"""CERTIFICATE -- L142: three sites, one field.  One theorem or three facts?

SEAL  outside_bench/seals/L142_THREE_SITES_PREREG.md
      sha256 8226e745503a63b0115e612800c19ec14893e0d7adad4a9f1b3357f387d36d87
      sealed BEFORE this file was written.

THE CELL, registered 2026-08-08 from B969/solo section 5, NEVER RUN:
  "THREE SITES, ONE FIELD: one theorem or three facts?  K now appears at three constructions in two
   representations: mu's adjoint pencil, kappa's adjoint pencil, and the cubic form on the compact
   kernel in the 27.  Not adjudicable by opinion.  The discriminating test, named: EXHIBIT A
   MORPHISM CARRYING ONE PENCIL TO ANOTHER, OR SHOW THE AGREEMENT IS ONLY OF OUTPUTS."

THE TRAP, NAMED IN THE SEAL BEFORE THE RUN.  Over Q, PGL2 is 3-transitive on P^1 and the root-triple
of an irreducible binary cubic is Galois-stable, so ANY two irreducible binary cubics over Q with
isomorphic root fields are PGL2(Q)-equivalent up to scalar: a GL2(Q) test CANNOT FAIL (MB12).  And a
GL2(Z) test would measure the basis conventions the cubics are read in -- B866 records exactly such a
rescaling between two constructions of mu ("theirs(13t) = 2197*mine(t)").  Neither is used.  The
morphism question itself is asked instead, in two layers.

CELLS (two outcomes each, fixed in the seal before this file existed)
  CELL 1  Across representations: can any equivariant morphism exist?
          A: the reps are isomorphic / admit a nonzero e6-map
          B: inequivalent irreducibles, so Hom_e6(27,78) = 0 and NO equivariant morphism exists
  CELL 2  Within the 27: are the two pencils' generating pairs CONJUGATE in GL(27)?
          A: every conjugation invariant agrees   B: some invariant DIFFERS, so no such T exists
  CELL 3  Is the agreement real at output level -- does every site's cubic generate K?
          A: no   B: yes, with positive and bite controls

  VERDICT RULE, fixed: B/B/B answers L142 THREE FACTS -- THE AGREEMENT IS OF OUTPUTS.

CONTROLS
  C1  The field test is two-sided: mu must be found isomorphic to K, and an unrelated cubic of the
      same resolvent Q(sqrt77) must be found NOT K.
  C2  The conjugacy test must be able to say YES: a pair conjugated by a known random T must be
      reported conjugate.
  C3  And able to say NO on a genuinely non-conjugate pair.
  C4  Every 27-side cubic is RECOMPUTED here from the build; B866's mu is reproduced as a check and
      labelled as such.
  C5  Exact arithmetic throughout.

Gate 5 untouched.  No measured value is used as input anywhere.
"""
import contextlib
import io
import json
import os
import random
import sys

import sympy as sp

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FAIL = []
L = sp.Symbol("L")
x, lam = sp.symbols("x lambda")
NS = [8, 14, 16, 22]
EXPO = {8: 4, 14: 7, 16: 8, 22: 11}
MU = sp.Poly(500716339200 * L**3 - 2075673600 * L**2 - 4769856 * L + 2197, L)


def rule(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78, flush=True)


def check(n, ok, d=""):
    print(f"  [{'OK ' if ok else 'FAIL'}] {n}{('  ' + d) if d else ''}", flush=True)
    if not ok:
        FAIL.append(n)
    return ok


def sf(n):
    n = int(n)
    if n == 0:
        return 0
    s, n, o = (1 if n > 0 else -1), abs(n), 1
    for p, e in sp.factorint(n).items():
        if e % 2:
            o *= p
    return s * o


# ---------------------------------------------------------------- the build
REPJ = json.load(open(os.path.join(ROOT, "frontier/B883_the_27/rep27.json")))
REP = {int(k): v for k, v in REPJ["rep"].items()}
B854 = os.path.join(ROOT, "frontier/B854_centralizer_exact/e6_centralizer.py")
g6 = {"__file__": B854, "__name__": "b854"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(B854, encoding="utf-8").read(), B854, "exec"), g6)
INV, ADS = g6["INV"], g6["ADS"]


def rho(vec):
    M = sp.zeros(27, 27)
    for p in range(78):
        c = vec[p]
        if c == 0:
            continue
        q = sp.Rational(c.numerator, c.denominator)
        Rp = REP[p]
        for i in range(27):
            for j in range(27):
                if Rp[i][j]:
                    M[i, j] += q * Rp[i][j]
    return M


R27 = {n: rho(INV[n]) for n in NS}
AD = {n: sp.Matrix(ADS[n]) for n in NS}

# ================================================================== CELL 1
rule("CELL 1 -- across representations: can any e6-equivariant morphism exist?")
print("       mu's site  (B866): a pencil on the ADJOINT 78, det of a 48x48 minor of ad(x8 + t x16)")
print("       B969's site      : the cubic form on the compact kernel, in the MATTER 27")
print("       this bench's new site (memo 201): the (x14,x22) branch locus, in the MATTER 27")
print(f"\n       dim of the adjoint representation : {AD[8].rows}")
print(f"       dim of the matter representation  : {R27[8].rows}")
same_dim = AD[8].rows == R27[8].rows
print("       27 and 78 are irreducible e6-representations of DIFFERENT dimension, hence")
print("       INEQUIVALENT; by Schur's lemma Hom_e6(27, 78) = 0.")
CELL1 = "B" if not same_dim else "A"
print(f"\n  CELL 1 = {CELL1}  -- " +
      ("no e6-equivariant morphism carries the adjoint-side pencil to a matter-side pencil, or back."
       if CELL1 == "B" else "an equivariant map is possible and must be sought"))

# ================================================================== CELL 2
rule("CELL 2 -- within the 27: are the two pencils' generating pairs CONJUGATE in GL(27)?")


def invariants(M):
    return dict(kernel=len(M.nullspace()),
                charpoly=sp.factor_list(sp.Poly(M.charpoly(x).as_expr(), x).as_expr(), x))


def conjugate_possible(P, Q):
    """Necessary conditions for simultaneous conjugacy of ordered pairs, all exact."""
    out = {}
    for i, (A, B) in enumerate(zip(P, Q)):
        out[f"kernel_{i}"] = (len(A.nullspace()), len(B.nullspace()))
        out[f"charpoly_{i}"] = (sp.Poly(A.charpoly(x).as_expr(), x).as_expr()
                                == sp.Poly(B.charpoly(x).as_expr(), x).as_expr())
        out[f"trace_{i}"] = (sp.simplify(A.trace() - B.trace()) == 0)
    out["rank_product"] = ((P[0] * P[1]).rank(), (Q[0] * Q[1]).rank())
    return out


PAIR_M = [R27[8], R27[16]]       # the measured / dual-pair plane
PAIR_O = [R27[14], R27[22]]      # the orphan / compact plane
inv = conjugate_possible(PAIR_M, PAIR_O)
for k, v in inv.items():
    print(f"       {k:16s} measured-plane vs orphan-plane : {v}")
differs = (inv["kernel_0"][0] != inv["kernel_0"][1]) or (inv["kernel_1"][0] != inv["kernel_1"][1]) \
    or not inv["charpoly_0"] or not inv["charpoly_1"] \
    or inv["rank_product"][0] != inv["rank_product"][1]

# C2 -- the test must be able to say YES
random.seed(20260911)
# C2's T is a PERMUTATION matrix.  Conjugating by one genuinely changes the matrices while
# preserving every conjugation invariant -- exactly what a positive control needs -- and its entries
# CANNOT grow, so the conjugated charpolys stay the size of the originals.  Two earlier drafts used
# a dense random T, then a 40-step unimodular T; both produced entries whose exact charpolys did not
# terminate.  THE CONTROL WAS THE BOTTLENECK, NOT THE CELL -- twice.
_perm = list(range(27))
random.shuffle(_perm)
T = sp.zeros(27, 27)
for _r, _c in enumerate(_perm):
    T[_r, _c] = 1
Ti = T.T
assert T * Ti == sp.eye(27), "a permutation matrix's inverse is its transpose"
assert _perm != list(range(27)), "the control must actually move something"
CONJ = [T * PAIR_M[0] * Ti, T * PAIR_M[1] * Ti]
inv_pos = conjugate_possible(PAIR_M, CONJ)
pos_ok = (inv_pos["kernel_0"][0] == inv_pos["kernel_0"][1]
          and inv_pos["kernel_1"][0] == inv_pos["kernel_1"][1]
          and inv_pos["charpoly_0"] and inv_pos["charpoly_1"]
          and inv_pos["rank_product"][0] == inv_pos["rank_product"][1])
check("C2 -- the conjugacy test reports a genuinely conjugated pair as CONJUGATE", pos_ok)
# C3 -- and must be able to say NO
inv_neg = conjugate_possible(PAIR_M, [R27[8], R27[22]])
neg_fires = (inv_neg["kernel_1"][0] != inv_neg["kernel_1"][1]) or not inv_neg["charpoly_1"]
check("C3 -- and reports a genuinely non-conjugate pair as NOT conjugate", neg_fires)

CELL2 = "B" if differs else "A"
print(f"\n  CELL 2 = {CELL2}  -- " +
      ("a conjugation invariant DIFFERS, so NO T in GL(27) carries one pencil to the other. "
       "Proved, not searched for." if CELL2 == "B" else "all invariants agree; a morphism is not excluded"))

# ================================================================== CELL 3
rule("CELL 3 -- does every site's cubic generate K?  (C1: positive and bite controls)")
# C6 -- K is presented by its SMALLEST model, not by mu.  mu's coefficients are ~5e11 and
# factoring over Q(root of mu) is what stalled two runs of this certificate; x^3-12x-5 generates
# the SAME field -- verified immediately below, not assumed -- with coefficients small enough for
# the factorisation to terminate.
K_SMALL = sp.Poly(L**3 - 12*L - 5, L)
theta = sp.RootOf(K_SMALL.as_expr(), 0)
KF = sp.QQ.algebraic_field(theta)
_mu_deg = sorted(f.degree() for f, _ in sp.Poly(MU.as_expr(), L, domain=KF).factor_list()[1])
print(f"       C6 -- K presented as {sp.sstr(K_SMALL.as_expr())}; mu factors over it as {_mu_deg}")
print(f"              -> mu has a root there, so both models generate THE SAME field: "
      f"{1 in _mu_deg}")


def in_K(expr):
    return 1 in [f.degree() for f, _ in sp.Poly(expr, L, domain=KF).factor_list()[1]]


# C4 -- the 27-side cubics are RECOMPUTED here from the build
B = sp.Matrix.hstack(*R27[14].col_join(R27[22]).nullspace())
Bp = B.pinv()
sites = []
for n in (8, 16):
    Rest = sp.simplify(Bp * R27[n] * B)
    cp = sp.Poly(sp.nsimplify(sp.expand(Rest.charpoly(x).as_expr())), x)
    num = sp.expand(cp.as_expr() * sp.lcm([sp.denom(c) for c in cp.all_coeffs()]))
    sites.append((f"x{n} restricted to the compact kernel in the 27 (B969's site, recomputed)",
                  sp.Poly(num, x)))
# the (x14,x22) branch locus -- this bench's fourth site, memo 201
pts = [(sp.Rational(k), sp.Poly((R27[14] + sp.Rational(k) * R27[22]).charpoly(x).as_expr(), x).all_coeffs())
       for k in range(28)]
xs = [p[0] for p in pts]
co = [sp.expand(sp.interpolate(list(zip(xs, [p[1][ci] for p in pts])), lam)) for ci in range(28)]
P48 = sp.expand(sum(co[i] * x ** (27 - i) for i in range(28)))
seen = set()
for f, m in sp.factor_list(sp.Poly(P48, x, lam))[1]:
    fe = f.as_expr()
    if int(sp.degree(fe, x)) < 2:
        continue
    for g, _ in sp.factor_list(sp.Poly(sp.expand(sp.discriminant(sp.Poly(fe, x))), lam))[1]:
        ge = g.as_expr()
        if int(sp.degree(ge, lam)) != 3:
            continue
        key = sp.sstr(sp.Poly(ge, lam).monic().as_expr())
        if key in seen:
            continue
        seen.add(key)
        sites.append(("the (x14,x22) branch locus in the 27 (memo 201, new site)",
                      sp.Poly(ge.subs(lam, x), x)))
sites.append(("mu itself -- POSITIVE CONTROL, K by definition", sp.Poly(MU.as_expr().subs(L, x), x)))
sites.append(("B866's adjoint-pencil mu, reproduced as a check (C4)",
              sp.Poly(500716339200 * x**3 - 159667200 * x**2 - 28224 * x + 1, x)))
sites.append(("BITE CONTROL -- an unrelated cubic of resolvent Q(sqrt77)",
              sp.Poly(x**3 - 6 * x**2 - 14 * x + 18, x)))

allK, bite_said_no, pos_said_yes = True, False, False
for label, P in sites:
    d = sp.discriminant(P)
    ok = in_K(P.as_expr().subs(x, L))
    print(f"       {label}")
    print(f"           {sp.sstr(P.as_expr())[:68]}")
    print(f"           irreducible/Q {P.is_irreducible}   resolvent sf {sf(d)}   GENERATES K: {ok}")
    if "BITE" in label:
        bite_said_no = not ok
    elif "POSITIVE" in label:
        pos_said_yes = ok
    else:
        allK = allK and ok
check("C1 -- POSITIVE control: mu is found isomorphic to K", pos_said_yes)
check("C1 -- BITE control: an unrelated resolvent-77 cubic is found NOT K", bite_said_no)
CELL3 = "B" if allK else "A"
print(f"\n  CELL 3 = {CELL3}  -- " +
      ("every site's cubic generates K: the agreement at output level is real"
       if CELL3 == "B" else "the sites do not agree; L142 dissolves"))

# ================================================================== verdict
rule("VERDICT")
print(f"  CELL 1 = {CELL1}   CELL 2 = {CELL2}   CELL 3 = {CELL3}   "
      f"controls: {'ALL PASS' if not FAIL else 'FAILED ' + str(FAIL)}")
if FAIL:
    print("\n  A FAILED CONTROL VOIDS THE READING.  No verdict.")
    sys.exit(1)
if (CELL1, CELL2, CELL3) == ("B", "B", "B"):
    print("""
  L142 ANSWERS: **THREE FACTS. THE AGREEMENT IS OF OUTPUTS.**

  The cell named its own discriminating test -- "exhibit a morphism carrying one pencil to another,
  or show the agreement is only of outputs" -- and declined to guess.  Both halves are now settled
  by computation rather than by opinion:

   *  ACROSS REPRESENTATIONS there is no morphism to exhibit, and none can exist.  mu's site is a
      pencil on the adjoint 78; B969's compact-kernel site and this bench's (x14,x22) site are on
      the matter 27.  These are INEQUIVALENT irreducible e6-representations, so Hom_e6(27,78) = 0
      by Schur.  The question is closed by a theorem, not by a failed search.

   *  WITHIN THE 27 the two pencils are NOT CONJUGATE, and again this is proved rather than
      searched: a conjugation invariant DIFFERS between the ordered pairs (rho(x8), rho(x16)) and
      (rho(x14), rho(x22)).  No T in GL(27) carries one to the other.

   *  AND THE AGREEMENT IS REAL: every site's cubic generates K, with the test controlled in both
      directions -- mu is found isomorphic to K, and an unrelated cubic of the same resolvent
      Q(sqrt77) is found NOT to be.

  THE RESIDUE, which a B/B/B result does NOT exclude and which the seal required be stated rather
  than buried: the sites are not related by a morphism, but they are all determined by THE SAME
  FOUR-DIMENSIONAL CHARGE SPACE.  "Three facts" here means three constructions with no map between
  them -- NOT three unrelated accidents.  A COMMON UPSTREAM CAUSE IS UNTOUCHED BY THIS RESULT, and
  is the successor question: not "is there a morphism between the sites" (no) but "what property of
  the charge space makes every construction on it return the same cubic field".

  WHAT THIS DOES NOT DO.  It does not prove or refute B882.  It does not decide whether the
  object's cubic is canonically K.  It produces no value, ratio or prediction; Gate 5 untouched.
""")
else:
    print("\n  Not the B/B/B pattern.  The morphism question stays live; read the cells above.")
print("Gate 5 untouched.  No measured value is used or named.")
