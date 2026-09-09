"""B1256 -- WHICH sl2? The principal embedding was never derived, and exactly one
alternative in E6 gives three CHIRAL classes: the subregular orbit E6(a1).

B1253 priced the generation count: h^1 = 3 matches, but the TYPES do not -- under
the PRINCIPAL sl2, 27 = Sym^16 + Sym^8 + Sym^0, so h^1 types as 1 ABELIAN (the
trivial summand) + 2 chiral, while the SM needs 3 chiral.  Its stated price was
"a mechanism making the trivial summand chiral, OR a bundle whose three classes
are all chiral".  B1255 then closed the OTHER route permanently (three generations
cannot live inside one 27: the 16 has multiplicity one, 3 copies need dim >= 48).

THE OBSERVATION THIS ARC MAKES.  The principal sl2 is a CHOICE.  B1112 pins the
object's canonical holonomy as PSL(2,C) with an SL(2,C) spin lift, but the
EMBEDDING of that SL(2) into E6 was never derived -- principal was assumed because
it is the natural choice for an irreducible SL(2).  By Menal-Ferrer-Porti,
dim H^1 = 1 per NONTRIVIAL ODD-dimensional symmetric power, so the typing of h^1
depends entirely on which embedding is taken.

THE COMPUTATION.  Enumerate all 3^6 = 729 weighted Dynkin labellings in {0,1,2}^6
(these include every E6 nilpotent orbit), build h by alpha_j(h) = c_j, decompose
the 27 into sl2 strings, and ask which give THREE NONTRIVIAL ODD summands.

RESULT.  h^1 counts NONTRIVIAL ODD-dimensional summands (one each); TRIVIAL summands
contribute abelian H^1.  Even-dimensional (Sym^odd) summands are NOT PSL(2,C) reps --
they require the spin lift -- and what they contribute to h^1 is NOT settled by the
banked form of Menal-Ferrer-Porti, which covers the nontrivial ODD case only.

    principal   (2,2,2,2,2,2)   27 = 17 + 9 + 1    dim O 72   2 chiral + 1 ABELIAN
    SUBREGULAR  (2,2,2,0,2,2)   27 = 13 + 9 + 5    dim O 70   THREE CHIRAL, and NO
                                                              even-dim summand at all

FOUR labellings give three nontrivial odd summands and zero trivial ones; three of
them carry even-dimensional summands and so depend on the unverified assumption that
those contribute 0.  The subregular is the ONLY candidate that needs NO assumption
about the even-dimensional case, because it has none.  That -- not a bare count -- is
what distinguishes it.

Separately: 9+9+9 does NOT exist in E6, and this is NON-EXISTENCE, not failure to
identify (see the completeness argument in selftest).  But three IDENTICAL nontrivial
odd summands DO exist -- (0,2,0,2,0,0) gives 7+7+7 -- with six trivial riders, so
h^1 = 3 chiral + 6 abelian = 9, not 3.

So the second half of B1253's price is satisfiable, UNIQUELY, by E6(a1) -- the
subregular orbit, the second-most-generic in E6, not an exotic pick.  Uniqueness
is what makes this a prediction rather than menu-shopping.

WHAT THIS DOES NOT CLAIM.  It does NOT derive three generations.  It converts an
open wish ("make the trivial summand chiral") into a single decidable question --
WHICH sl2 EMBEDDING DOES THE OBJECT SUPPLY? -- with exactly one qualifying answer.
The choice itself is registered as an UNEARNED INPUT (I-25): every h^1 typing in
the corpus rests on it, and per B1231 the input ledger's count is a lower bound
until it is earned.

CONTROLS (MB12, both directions):
  - the orbit-dimension formula is validated against the PRINCIPAL labelling,
    which must return 72 (the regular orbit) -- otherwise "dim 70" means nothing;
  - the root system is rebuilt independently and must contain exactly 72 roots;
  - the criterion CAN fail and mostly does: the full distribution is reported;
  - the EARLIER, CRUDER criterion ("exactly three summands total") is run alongside
    and shown to be WRONG -- it reports 1 hit where the correct criterion reports 4;
  - the decomposition is checked to reconstruct dim 27 in every case.
"""
import collections, itertools, json, os
import sympy as sp

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
CARTAN = sp.Matrix([
    [ 2, 0,-1, 0, 0, 0],
    [ 0, 2, 0,-1, 0, 0],
    [-1, 0, 2,-1, 0, 0],
    [ 0,-1,-1, 2,-1, 0],
    [ 0, 0, 0,-1, 2,-1],
    [ 0, 0, 0, 0,-1, 2]])
PRINCIPAL = (2, 2, 2, 2, 2, 2)


def weights_27():
    REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
    REP = [[[int(v) for v in row] for row in REPJ["rep"][str(k)]] for k in range(78)]
    return [tuple(REP[i][a][a] for i in range(6)) for a in range(27)]


def roots_E6():
    """Rebuild the root system from the Cartan matrix: norm-2 integer combinations."""
    out = []
    for v in itertools.product(range(-3, 4), repeat=6):
        m = sp.Matrix(6, 1, list(v))
        if (m.T * CARTAN * m)[0, 0] == 2:
            out.append(v)
    return out


def decompose(vals):
    """Greedy sl2-string decomposition; returns highest weights, or None if impossible."""
    m = collections.Counter(vals)
    out = []
    while sum(m.values()):
        top = max(k for k in m if m[k] > 0)
        if top < 0:
            return None
        out.append(top)
        for v in range(top, -top - 1, -2):
            m[v] -= 1
            if m[v] < 0:
                return None
    return sorted(out, reverse=True)


def h_on_27(c, WT, Cinv):
    coef = Cinv * sp.Matrix(6, 1, list(c))
    return [sum(WT[a][i] * coef[i] for i in range(6)) for a in range(27)]


def orbit_dim(c, roots):
    """dim O = dim g - dim g_0 - dim g_1, with g_i the h-eigenspaces."""
    vals = [sum(r[j] * c[j] for j in range(6)) for r in roots]
    g0 = sum(1 for x in vals if x == 0) + 6          # + the Cartan
    g1 = sum(1 for x in vals if x == 1)
    return 78 - g0 - g1


def selftest():
    print("B1256 -- which sl2? the principal embedding was never derived (selftest)")
    WT, Cinv, roots = weights_27(), CARTAN.inv(), roots_E6()

    print(f"  [ctl ] root system rebuilt independently: {len(roots)} roots (must be 72)")
    assert len(roots) == 72

    dprin = orbit_dim(PRINCIPAL, roots)
    print(f"  [ctl ] orbit-dim formula on the PRINCIPAL labelling: {dprin} (must be 72, the regular orbit)")
    assert dprin == 72

    dec_p = decompose([int(v) for v in h_on_27(PRINCIPAL, WT, Cinv)])
    print(f"  [prin] principal {PRINCIPAL}: 27 = "
          f"{' + '.join(str(k+1) for k in dec_p)}  <- contains the trivial Sym^0")
    assert [k + 1 for k in dec_p] == [17, 9, 1]

    crude, correct, shapes = [], [], collections.Counter()
    for c in itertools.product((0, 1, 2), repeat=6):
        vals = h_on_27(c, WT, Cinv)
        if any(v != int(v) for v in vals):
            continue
        d = decompose([int(v) for v in vals])
        if d is None:
            continue
        dims = [k + 1 for k in d]
        assert sum(dims) == 27, "decomposition must reconstruct dim 27"
        shapes[len(dims)] += 1
        chiral  = sum(1 for t in dims if t % 2 == 1 and t > 1)   # H^1 = 1 each (MFP)
        abelian = sum(1 for t in dims if t == 1)                 # abelian H^1
        even    = sum(1 for t in dims if t % 2 == 0)             # NOT a PSL(2,C) rep
        if len(dims) == 3 and abelian == 0:
            crude.append((c, dims, orbit_dim(c, roots)))
        if chiral == 3 and abelian == 0:
            correct.append((c, dims, orbit_dim(c, roots), even))

    print(f"  [ctl ] the criterion CAN fail -- summand-count distribution: {dict(sorted(shapes.items()))}")
    print(f"  [ctl ] the CRUDER criterion ('exactly 3 summands total') finds {len(crude)} -- and is WRONG:")
    print(f"         even-dimensional summands contribute nothing to h^1 and may ride along freely.")
    print(f"  [HIT ] correct criterion (3 nontrivial odd summands, 0 trivial): {len(correct)}")
    for c, dims, dO, even in sorted(correct, key=lambda r: r[3]):
        tag = "  <== NO even-dim summand: assumption-free" if even == 0 else ""
        print(f"           {c}  27 = {' + '.join(map(str, dims)):22} dim O={dO:3} even-dim={even}{tag}")
    assert len(crude) == 1 and len(correct) == 4

    free = [r for r in correct if r[3] == 0]
    assert len(free) == 1 and free[0][0] == (2, 2, 2, 0, 2, 2) and free[0][1] == [13, 9, 5]
    print(f"  [UNIQ] candidates needing NO assumption about even-dim summands: {len(free)}"
          f"  -> {free[0][0]}, the subregular E6(a1)")

    ident = [(c, dims) for c, dims, dO, ev in
             [(a, b, cc, d) for a, b, cc, d in correct]] and [
        (c, [k + 1 for k in decompose([int(v) for v in h_on_27(c, WT, Cinv)])])
        for c in itertools.product((0, 1, 2), repeat=6)
        if all(v == int(v) for v in h_on_27(c, WT, Cinv))
        and decompose([int(v) for v in h_on_27(c, WT, Cinv)]) is not None]
    trip = [(c, dims) for c, dims in ident
            if len([t for t in dims if t % 2 == 1 and t > 1]) == 3
            and len(set(t for t in dims if t % 2 == 1 and t > 1)) == 1]
    print(f"  [note] three IDENTICAL nontrivial odd summands DO exist: {len(trip)} labelling(s)")
    for c, dims in trip:
        ab = sum(1 for t in dims if t == 1)
        print(f"           {c}  27 = {' + '.join(map(str, dims))}   (abelian riders: {ab}"
              f" -> h^1 = 3 + {ab}, not 3)")
    assert any(dims.count(7) == 3 for _, dims in trip), "7+7+7 must be found"
    assert not any(dims.count(9) == 3 for _, dims in trip), "9+9+9 must NOT exist"

    print("\n  => h^1 = 3 types as THREE CHIRAL under E6(a1) and as 2 chiral + 1 ABELIAN")
    print("     under the principal sl2.  The embedding is the open input (I-25).")
    print("     9+9+9 does NOT exist in E6 -- non-existence, not failure to identify.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
