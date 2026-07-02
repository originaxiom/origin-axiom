"""B349 / gate A (S032-A) -- the irregular-cover class through index 6: canonical multisets,
isometry-identified multiplicities, no forced choice.

Extends B330's mechanism to another of its named untested classes: invariants of IRREGULAR
(non-normal, non-cyclic) covers. B350 sealed the cyclic tower; this probe enumerates ALL
covers of the figure-eight through index 6 (SnapPy subgroup enumeration) and asks the gate-A
question at each index: does any cover-level invariant hand the object a forced choice?

Verified here (SnapPy 3.3.x; all values banked as exact integers/homology types):
  (i)   CROSS-VALIDATION: the cyclic covers' H1 torsion from SnapPy equals B350's
        coker(A^n - I) Smith normal forms exactly (n = 2..6: [5], [4,4], [3,15], [11,11],
        [8,40]) -- two independent routes (group enumeration vs. monodromy algebra), one answer;
  (ii)  the cover CENSUS per index is a canonical multiset of (type, H1): index 4 = 1 cyclic
        + 1 irregular (H1 = Z^2, torsion-free); index 5 = 1 cyclic + 3 irregular; index 6 =
        1 cyclic + 10 irregular. The multiset is what the object determines -- no member
        carries a mark;
  (iii) EVERY within-index invariant multiplicity is resolved by ISOMETRY: the two index-5
        irregular covers with H1 = Z/2 + Z^2 are isometric (4 isometries); the index-6
        multiplicity groups (4x Z/3+Z^2, 2x Z/12+Z, 2x Z/5+Z^2) each collapse to a SINGLE
        isometry class. The "distinct" members are the same geometric object seen through
        non-conjugate subgroups -- a distinction no manifold invariant sees, identified by
        the object's own symmetries (the covering isometries live in the commensurator;
        cf. B348's self-symmetrization and B323's four-level framework).

MB-guard note: is_isometric_to() is orientation-BLIND (REPRODUCIBILITY MB/B128). Here that is
sufficient honestly: gate A asks whether the object DISTINGUISHES members; identification by
ANY self-isometry (orientation-preserving or not) already means no member is distinguished.

HONEST SCOPE (C-guardrail): index <= 6 only (a computational horizon, not a theorem); the
class "all irregular covers" stays formally open beyond it. Firewalled; nothing to CLAIMS.md.
Needs SnapPy (importorskip-gated in the lock, like the other 16 SnapPy locks).
"""
import collections


# Banked census (type, torsion-part-of-H1, betti) per index -- the canonical multisets.
EXPECTED_CYCLIC_TORSION = {2: (5,), 3: (4, 4), 4: (3, 15), 5: (11, 11), 6: (8, 40)}
EXPECTED_CENSUS = {
    4: {("cyclic", (3, 15), 1): 1, ("irregular", (), 2): 1},
    5: {("cyclic", (11, 11), 1): 1, ("irregular", (), 3): 1, ("irregular", (2,), 2): 2},
    6: {("cyclic", (8, 40), 1): 1, ("irregular", (3,), 2): 4, ("irregular", (12,), 1): 2,
        ("irregular", (5,), 2): 2, ("irregular", (2, 4), 2): 1, ("irregular", (4, 8), 1): 1},
}


def _h1_key(C):
    h = C.homology()
    torsion = tuple(int(c) for c in h.coefficients if c != 0)
    betti = h.betti_number()
    return torsion, betti


def cover_census(M, k):
    """The multiset {(cover type, H1 torsion, betti)} at index k -- the canonical datum."""
    cnt = collections.Counter()
    for C in M.covers(k):
        torsion, betti = _h1_key(C)
        cnt[(C.cover_info()["type"], torsion, betti)] += 1
    return dict(cnt)


def cyclic_covers_match_B350(M, nmax=6):
    """(i) SnapPy's cyclic-cover H1 torsion == B350's coker(A^n - I) SNF, n = 2..nmax."""
    out = {}
    for n in range(2, nmax + 1):
        cyc = [C for C in M.covers(n) if C.cover_info()["type"] == "cyclic"]
        assert len(cyc) == 1                     # knot in S^3: one cyclic cover per index
        torsion, betti = _h1_key(cyc[0])
        out[n] = (torsion, betti == 1, torsion == tuple(d for d in EXPECTED_CYCLIC_TORSION[n] if d != 1))
    return out


def multiplicities_resolved_by_isometry(M, k):
    """(iii) within-index same-(type, H1) groups: how many isometry classes each?
    Returns {key: (group size, number of isometry classes)} for the multiplicity groups."""
    groups = collections.defaultdict(list)
    for C in M.covers(k):
        groups[(C.cover_info()["type"],) + _h1_key(C)].append(C)
    out = {}
    for key, cs in groups.items():
        if len(cs) < 2:
            continue
        classes = []
        for C in cs:
            for cl in classes:
                if cl[0].is_isometric_to(C):
                    cl.append(C)
                    break
            else:
                classes.append([C])
        out[key] = (len(cs), len(classes))
    return out


def main():
    import snappy
    M = snappy.Manifold("4_1")
    print("B349 -- irregular covers through index 6 (gate A extension)\n")
    print("(i) cyclic covers vs B350 SNF:", cyclic_covers_match_B350(M))
    for k in (4, 5, 6):
        census = cover_census(M, k)
        print(f"(ii) index {k} census: {census}  matches banked: {census == EXPECTED_CENSUS[k]}")
    for k in (5, 6):
        res = multiplicities_resolved_by_isometry(M, k)
        print(f"(iii) index {k} multiplicity groups -> isometry classes: {res}")
    print("\nCONDITIONAL: through index 6, cover multisets are canonical and every invariant")
    print("multiplicity is isometry-identified -- no forced choice. Higher indexes untested.")


if __name__ == "__main__":
    main()
