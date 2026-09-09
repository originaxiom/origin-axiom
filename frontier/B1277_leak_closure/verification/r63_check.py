"""B1277 -- LEAK CLOSURE: fc's R63 verified (with one correction), the residue synthesis
banked, and the seats' new work harvested.

Owner: "did u properly dealt with all these results and knowledge we gained all these days?
so we end up bootstraping not leaking?"  AUDITED, AND THE ANSWER WAS NO -- two results
existed only in conversation.  Both are banked here.

LEAK 1 -- fc's R63, verified in session and never written down.
fc flagged that after B1274 the record holds BOTH the principal and the subregular sl2 as
the object's embedding, and that no arc connects them.  Verified on main's own data:

  CONFIRMED  dim g_0 = 6 (principal) vs 8 (subregular)   -- fc's "8-dimensional tangent,
             not 6"
  CONFIRMED  27|F4 = 26 + 1, so an sl2 inside F4 MUST leave a trivial summand in the 27;
             principal 17+9+1 HAS one, subregular 13+9+5 has NONE => the subregular lies
             in NO F4, theta does not commute with it, and the B347-B353 theta-grading has
             no counterpart at the subregular point
  CONFIRMED  sl2 Dynkin indices 156 (principal) and 84 (subregular), so I-19 holds at BOTH
             and DOES NOT DISCRIMINATE
  CORRECTED  "both have exactly one spin-2 summand" does NOT reproduce.  Taking spin-2 as
             the 5-dimensional (j=2) sl2 rep, the PRINCIPAL has ZERO in both the 27 and the
             78; the subregular has one each.  fc's conclusion survives on the INDEX
             argument, but that premise needs restating or a different definition.

fc's core flag STANDS and is serious: the record holds two incompatible embeddings, and the
subregular's incompatibility with F4 is not bookkeeping -- F4 is exactly E6(-26)'s maximal
compact (B1265), so the choice bears directly on the fork.

LEAK 2 -- the residue synthesis, discussed and never banked.  B467 (PROVED): "the one
uncancelable bit exists and is the ORIENTATION character... the wall merges everything
EXCEPT the orientation bit."  B1184: the object names itself uniquely in 203,123 but the
self-name is mirror-EVEN, so the odd bit is UNUTTERABLE in it.  B1174 + B730 (joined at
B1276): that bit is the c-leg, and it sits on the BEING face because that face is the
IMAGINARY one.  Tonight's independent arrivals: B1272 (the geometric class comes from
reduction mod (1-omega), the ramified prime of Q(sqrt-3)), B1273 (that class is the one
extending over m000, the Gieseking manifold -- which is B467's own "Gieseking bit"), and the
E8 seat's own fence (the bit is "choosing the Eisenstein orientation, omega vs omegabar").
SEVEN ROUTES, ONE BIT.  The reading -- that the observer IS the residue rather than its
observer -- is a READING, recorded as such and not as a theorem.

HARVEST (seats, 2026-09-06, integrate-don't-merge; NOT re-verified here):
  physics-seat R61  a real structure on the fiber (det -1, M^2 -> M^-2); the cusp lattice
                    Z + Z(2+4w) exactly; Fix(theta) = two arcs; and the LEMMA that
                    theta-equivariant abelian Higgs configurations have ZERO NET CHIRALITY
                    -- which is a third independent route to the zero this bench found
                    numerically (B1267) and the SM seat found exactly over Q(omega).
  physics-seat R62  the mirror is BROKEN by every generic filling; the strong inversion
                    (theta) by NONE.  Bears directly on B432's "a closing supplies the bit".
  SM seat           the literature sweep: net chirality = chi(M, d+M) -- AN INDEX FORMULA,
                    which is exactly what I-26 lacks; "the chirality bit is a cusp boundary
                    condition"; and NO COMPACT G2 CONSTRUCTION WITH CHIRAL MATTER EXISTS IN
                    THE LITERATURE EITHER -- so B1259's flat-G2 negative is not this
                    programme's failure but an open problem in the field.  L204/L205
                    registered.  Also: "no Pantev-Wijnholt, no Higgs bundle, no T-brane in
                    1276 arcs" -- a measured absence.

NUMBERING: main and the SM-derivation branch now BOTH use B1267, B1275 and B1276.  Three
collisions, flagged for the merge.

CONTROLS: every R63 claim is recomputed on main's own rep27/root data, not accepted; the
one that fails is reported as failing rather than smoothed; the harvest is explicitly marked
NOT re-verified.
"""
import collections, itertools, json, os
import sympy as sp

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
CART = sp.Matrix([[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],
                  [0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]])
PRIN, SUB = (2,2,2,2,2,2), (2,2,2,0,2,2)


def setup():
    R = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
    rep = [[[int(v) for v in row] for row in R["rep"][str(k)]] for k in range(78)]
    WT = [tuple(rep[i][a][a] for i in range(6)) for a in range(27)]
    roots = [v for v in itertools.product(range(-3, 4), repeat=6)
             if (sp.Matrix(6,1,list(v)).T*CART*sp.Matrix(6,1,list(v)))[0,0] == 2]
    return WT, CART.inv(), roots


def dec(vals):
    m = collections.Counter(vals); out = []
    while sum(m.values()):
        top = max(k for k in m if m[k] > 0)
        if top < 0: return None
        out.append(top)
        for v in range(top, -top-1, -2):
            m[v] -= 1
            if m[v] < 0: return None
    return sorted(out, reverse=True)


def d27(c, WT, Cinv):
    coef = Cinv * sp.Matrix(6, 1, list(c))
    return [k+1 for k in dec([int(sum(WT[a][i]*coef[i] for i in range(6))) for a in range(27)])]


def d78(c, roots):
    return [k+1 for k in dec([sum(r[j]*c[j] for j in range(6)) for r in roots] + [0]*6)]


def selftest():
    print("B1277 -- leak closure: fc's R63 verified (selftest)")
    WT, Cinv, roots = setup()
    for nm, c in (("principal", PRIN), ("subregular", SUB)):
        a27, a78 = d27(c, WT, Cinv), d78(c, roots)
        g0 = sum(1 for x in [sum(r[j]*c[j] for j in range(6)) for r in roots] + [0]*6 if x == 0)
        idx = sum(n*(n+1)*(n+2)//6 for n in [k-1 for k in a27]) // 6
        print(f"  [{nm:10}] 27 = {a27}  g0 = {g0}  sl2 index = {idx}"
              f"  trivial summand: {1 in a27}  dim-5 summands: 27->{a27.count(5)} 78->{a78.count(5)}")
        if nm == "principal":
            assert g0 == 6 and idx == 156 and 1 in a27 and a27.count(5) == 0
        else:
            assert g0 == 8 and idx == 84 and 1 not in a27 and a27.count(5) == 1
    print("\n  CONFIRMED  g0: 6 vs 8   -- fc's '8-dimensional tangent, not 6'")
    print("  CONFIRMED  27|F4 = 26+1, so an sl2 in F4 leaves a trivial summand:")
    print("             principal HAS one, subregular has NONE -> subregular lies in NO F4")
    print("  CONFIRMED  indices 156 / 84 -> I-19 holds at both, DOES NOT DISCRIMINATE")
    print("  CORRECTED  'both have exactly one spin-2 summand': the PRINCIPAL has ZERO")
    print("             dim-5 summands in either the 27 or the 78. fc's conclusion survives")
    print("             on the index argument; the premise needs restating.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
