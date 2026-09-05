"""B1257 -- the orbit that REMEMBERS 2T: Brieskorn-Slodowy selects the subregular, uniquely.

I-25 (B1256) registered an unearned input: the object's SL(2) was assumed to embed in
E6 via the PRINCIPAL sl2, a choice never derived.  This arc exhibits a CANONICAL
selection criterion that picks a different orbit -- and picks it uniquely.

THE ARCHAEOLOGY.  The principal grading entered at B327 ("the principal 27 decomposition
is V(16)+V(8)+V(0)"; fence: "Exact E6 Weyl-orbit + principal grading"), and was never
revisited across ~930 arcs.  B327's OWN bibliography line reads: "Kostant (principal
SL(2)); the McKay correspondence 2T <-> E6-tilde (Gonzalez-Sprinberg-Verdier, SLODOWY)".
Both were cited; only Kostant's was used.  The theorem that selects the other orbit was
already in the arc's reading list.

THE CRITERION.  For a simple Lie algebra g of type ADE, BRIESKORN-SLODOWY: the transverse
(Slodowy) slice S_e to a nilpotent orbit O meets the nilpotent cone N in a variety of
dimension dim N - dim O, and for the SUBREGULAR orbit this is a SIMPLE SURFACE
SINGULARITY C^2/Gamma of the SAME ADE type as g.  For E6, Gamma = 2T -- the binary
tetrahedral group.

THE POINT.  The object's E6 was BUILT from 2T by McKay (I-1, EARNED: the rep graph IS the
diagram).  So among E6's canonical nilpotent orbits, ask which one's geometry RETURNS the
very group the algebra was built from.  Exactly one does.

    principal  (2,2,2,2,2,2)  dim O = 72  ->  dim(S cap N) = 0  -- a POINT: 2T forgotten
    SUBREGULAR (2,2,2,0,2,2)  dim O = 70  ->  dim(S cap N) = 2  -- a SURFACE = C^2/2T

and the subregular's 27-decomposition is 13 + 9 + 5: three NONTRIVIAL ODD summands, no
trivial one, hence (B1256's addendum, computed) h^1 = 3 ALL CHIRAL.

WHAT THIS CLAIMS.  A canonical, unique, non-fitted criterion selecting the embedding that
yields three chiral generations, replacing an unexamined default that has NO attachment to
the object's own 2T.  It is a CANDIDATE ROUTE to earning I-25.

WHAT IT DOES NOT CLAIM.  It does not prove the object's holonomy realises this embedding.
Both orbits are intrinsically defined in E6; what distinguishes the subregular is a CLOSURE
condition -- its slice geometry reproduces the input datum -- not an aesthetic preference.
The remaining step is exhibiting that the object's SL(2) lands there.  I-25 stays UNEARNED.

CONTROLS (MB12, both directions):
  - the criterion CAN fail: every orbit's slice dimension is computed and reported, and 28
    of 30 give neither 0 nor 2 -- it is not a tautology;
  - the orbit-dimension formula is validated against the known regular orbit (72);
  - the root system is rebuilt independently (72 roots);
  - the DECISIVE control: the selected orbit was NOT chosen to give three chiral summands --
    the slice criterion is computed from dimensions ALONE, with no reference to the 27's
    decomposition, and the decomposition is read off afterwards.
"""
import collections, itertools, json, os
import sympy as sp

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DIM_G, RANK = 78, 6
DIM_N = DIM_G - RANK
CARTAN = sp.Matrix([
    [ 2, 0,-1, 0, 0, 0], [ 0, 2, 0,-1, 0, 0], [-1, 0, 2,-1, 0, 0],
    [ 0,-1,-1, 2,-1, 0], [ 0, 0, 0,-1, 2,-1], [ 0, 0, 0, 0,-1, 2]])
PRINCIPAL, SUBREGULAR = (2, 2, 2, 2, 2, 2), (2, 2, 2, 0, 2, 2)


def weights_27():
    R = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
    rep = [[[int(v) for v in row] for row in R["rep"][str(k)]] for k in range(78)]
    return [tuple(rep[i][a][a] for i in range(6)) for a in range(27)]


def roots_E6():
    return [v for v in itertools.product(range(-3, 4), repeat=6)
            if (sp.Matrix(6, 1, list(v)).T * CARTAN * sp.Matrix(6, 1, list(v)))[0, 0] == 2]


def decompose(vals):
    m = collections.Counter(vals); out = []
    while sum(m.values()):
        top = max(k for k in m if m[k] > 0)
        if top < 0: return None
        out.append(top)
        for v in range(top, -top - 1, -2):
            m[v] -= 1
            if m[v] < 0: return None
    return sorted(out, reverse=True)


def orbit_dim(c, roots):
    vals = [sum(r[j] * c[j] for j in range(6)) for r in roots]
    return DIM_G - (sum(1 for x in vals if x == 0) + RANK) - sum(1 for x in vals if x == 1)


def table():
    WT, Cinv, roots = weights_27(), CARTAN.inv(), roots_E6()
    rows = []
    for c in itertools.product((0, 1, 2), repeat=6):
        coef = Cinv * sp.Matrix(6, 1, list(c))
        vals = [sum(WT[a][i] * coef[i] for i in range(6)) for a in range(27)]
        if any(v != int(v) for v in vals): continue
        d = decompose([int(v) for v in vals])
        if d is None: continue
        rows.append((c, [k + 1 for k in d], orbit_dim(c, roots)))
    return rows, roots


def selftest():
    print("B1257 -- Brieskorn-Slodowy selects the subregular, uniquely (selftest)")
    rows, roots = table()
    print(f"  [ctl ] root system rebuilt: {len(roots)} roots (must be 72)")
    assert len(roots) == 72
    dp = next(r for r in rows if r[0] == PRINCIPAL)[2]
    print(f"  [ctl ] orbit-dim formula on the regular orbit: {dp} (must be 72)")
    assert dp == 72
    print(f"  [set ] dim g = {DIM_G}, rank {RANK} -> dim N = {DIM_N};  dim(S cap N) = dim N - dim O")

    surf = [r for r in rows if DIM_N - r[2] == 2]
    pt   = [r for r in rows if DIM_N - r[2] == 0]
    other = len(rows) - len(surf) - len(pt)
    print(f"  [ctl ] slice dims across all {len(rows)} orbits: point {len(pt)}, SURFACE {len(surf)},"
          f" neither {other}  (not a tautology)")
    assert other == 28

    print(f"  [pt  ] slice = a POINT: {pt[0][0]}  27 = {' + '.join(map(str,pt[0][1]))}"
          f"   -> 2T is FORGOTTEN")
    assert pt[0][0] == PRINCIPAL

    print(f"  [HIT ] slice = a SURFACE (= C^2/2T, Brieskorn-Slodowy): {len(surf)} orbit")
    c, dims, dO = surf[0]
    print(f"           {c}  dim O = {dO}  27 = {' + '.join(map(str, dims))}")
    assert len(surf) == 1 and c == SUBREGULAR and dims == [13, 9, 5]

    # THE DECISIVE CONTROL: the criterion never looked at the 27's decomposition.
    chiral  = sum(1 for t in dims if t % 2 == 1 and t > 1)
    abelian = sum(1 for t in dims if t == 1)
    print(f"  [read] its decomposition, read off AFTER selection: chiral {chiral}, abelian {abelian}"
          f"  -> h^1 = 3 ALL CHIRAL" if (chiral, abelian) == (3, 0) else "")
    assert (chiral, abelian) == (3, 0)

    print("\n  => the ONLY orbit whose slice geometry returns the 2T that BUILT E6 (McKay, I-1")
    print("     EARNED) is the subregular -- and it is exactly the embedding giving three chiral")
    print("     generations. A candidate route to earning I-25; I-25 itself stays UNEARNED.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
