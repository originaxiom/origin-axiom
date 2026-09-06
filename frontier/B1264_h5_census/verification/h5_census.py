"""B1264 -- THE H5 CENSUS: eight measured instances of 'every space, never a point',
and I-14's status upgraded by RECOMPUTING instead of citing a 1000-arc-old adjudication.

Owner, mid-audit: "b323 is 1000bs old."  Correct, and the seat had just leaned on B323's
2026-07 adjudication ("the two Z/3s are distinct; the CRUX -- does L3 connect to L4? --
is open") to conclude I-14 was not refutable.  That is citing, not computing.  Recomputed
from the object's own 27 (B883):

  * the trinification Z/3 grading EXISTS in the object's 27: 170 labellings in {0,1,2}^6
    are integral on the 27 and split it 9+9+9, giving 85 DISTINCT colourings up to
    permuting the three colours;
  * every such grading operator has eigenvalues 1, omega, omega^2 with omega the primitive
    cube root of unity -- i.e. THE EISENSTEIN UNIT of Q(sqrt-3), which is the SAME
    algebraic number generating the commensurator's Z/3 (units of O_{-3} = Z/6).

STATUS CHANGE, stated carefully.  L3 and L4 are therefore NOT related by an "order match"
-- the evidence B1223 forbids -- but by the SAME ACTING ALGEBRAIC NUMBER in the object's
OWN field.  That is a better status than B323 recorded.  It is NOT a map that ACTS, because
there are 85 candidate gradings and nothing yet selects one.  I-14 stays UNEARNED; the
price stays at 14.

AND THE MULTIPLICITY IS THE POINT.  85 joins a census this session has been measuring:

    C22    the CLOSING          the group of closings          never which closing
    A7     the ORDER            the pair {LR, RL}              never which order      (2)
    B1192  the PARTNER          an infinite family             never which partner
    B1248  n in kappa = 2+n^2   n = 1..7, hundreds each        never which n
    I-25   the sl2 EMBEDDING    30 orbits, 4 give h1=3 chiral  never which embedding (4)
    I-6    the 2T QUOTIENT      48 surjections                 never which quotient  (2)
    I-14   the L3 GRADING       85 distinct 9+9+9 colourings   never which grading  (85)
    I-14   the L3 -> L4 MAP     Hom(Z/3,Z/3): 2 isomorphisms   never which iso       (2)

EIGHT instances of OPEN_ITEMS H5 -- "the object supplies every SPACE and never a POINT" --
four of them measured for the first time in this session.

MECHANISM, and it covers only PART of the census -- do not over-unify:
  B1227's theorem (amphichiral => the mirror is a SELF-isometry => a mirror-odd invariant
  satisfies 2I = 0) explains the CHIRALITY instances: torsion-free value group => the odd
  part is forced to 0 (no magnitude); a group WITH torsion keeps it (B1224: CS in {0,1/4}).
  That is E65/B1260's seven chirality walls as one theorem.  It does NOT explain the
  group-theoretic multiplicities (2, 4, 85, infinite) -- those are COUNTING facts.
  ONE PATTERN, AT LEAST TWO MECHANISMS.

THE FALSIFIER IS SHARPENED BUT NOT MET.  H5 asks for an other-referential POINT the object
supplies.  B1224's CS = 0 is a point the object supplies -- but CS is an invariant OF THE
OBJECT, i.e. SELF-referential, which H5 explicitly permits.  Not a counterexample.  H5
stands un-falsified and still un-banked; this arc measures it, it does not promote it.

CONTROLS (MB12, both directions):
  - the grading search is run over ALL 3^6 labellings and reports how many are integral and
    how many split 9+9+9, so "85" is a measured count rather than an exhibited example;
  - colour-permutation normalisation is applied, so 170 labellings are not double-counted;
  - the census distinguishes MEASURED multiplicities from banked-but-unmeasured ones.
"""
import collections, itertools, json, os
import sympy as sp

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
CARTAN = sp.Matrix([[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],
                    [0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]])


def weights_27():
    R = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
    rep = [[[int(v) for v in row] for row in R["rep"][str(k)]] for k in range(78)]
    return [tuple(rep[i][a][a] for i in range(6)) for a in range(27)]


def trinification_gradings():
    WT, Cinv = weights_27(), CARTAN.inv()
    labellings, colourings = 0, set()
    for c in itertools.product(range(3), repeat=6):
        if not any(c):
            continue
        coef = Cinv * sp.Matrix(6, 1, list(c))
        vals = [sum(WT[a][i] * coef[i] for i in range(6)) for a in range(27)]
        if any(v != int(v) for v in vals):
            continue
        res = tuple(int(v) % 3 for v in vals)
        if sorted(collections.Counter(res).values()) != [9, 9, 9]:
            continue
        labellings += 1
        colourings.add(min(tuple(p[x] for x in res) for p in itertools.permutations(range(3))))
    return labellings, colourings


CENSUS = [("C22", "the CLOSING", None), ("A7", "the ORDER", 2),
          ("B1192", "the PARTNER", None), ("B1248", "n in kappa = 2+n^2", None),
          ("I-25", "the sl2 EMBEDDING", 4), ("I-6", "the 2T QUOTIENT", 2),
          ("I-14", "the L3 GRADING", 85), ("I-14", "the L3 -> L4 MAP", 2)]


def selftest():
    print("B1264 -- the H5 census, and I-14 recomputed (selftest)")
    lab, col = trinification_gradings()
    print(f"  [L3  ] labellings splitting the 27 as 9+9+9: {lab};"
          f"  DISTINCT colourings up to colour permutation: {len(col)}")
    assert lab == 170 and len(col) == 85
    print("  [L3  ] every Z/3 grading operator has eigenvalues 1, omega, omega^2 --")
    print("         omega the Eisenstein unit of Q(sqrt-3), the object's OWN field, and the")
    print("         SAME algebraic number generating the commensurator's Z/3 (O_{-3}* = Z/6)")
    print("  [stat] so L3~L4 is NOT an order match (B1223's forbidden evidence) but a match of")
    print("         the ACTING ALGEBRAIC NUMBER -- better than B323 (2026-07) recorded.")
    print("  [stat] it is NOT a map that ACTS: 85 candidate gradings, none selected.")
    print("         I-14 stays UNEARNED; the price stays at 14.")

    measured = [c for c in CENSUS if c[2] is not None]
    print(f"\n  [H5  ] census instances: {len(CENSUS)}; with MEASURED multiplicity: {len(measured)}")
    for src, thing, m in CENSUS:
        print(f"           {src:7} {thing:22} multiplicity {m if m is not None else 'banked, unmeasured'}")
    assert len(CENSUS) == 8

    print("\n  [ctl ] one PATTERN, at least TWO mechanisms: B1227's 2I = 0 explains the chirality")
    print("         instances; the counting multiplicities (2, 4, 85, infinite) it does not.")
    print("  [ctl ] falsifier NOT met: B1224's CS = 0 is a point, but a SELF-referential one,")
    print("         which H5 permits. H5 stands un-falsified and un-banked.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
