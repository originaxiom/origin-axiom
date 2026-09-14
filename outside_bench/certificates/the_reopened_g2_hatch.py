#!/usr/bin/env python3
"""THE REOPENED G2 HATCH -- is the enhancement isolated in the sense AW needs?

Seal: outside_bench/seals/THE_REOPENED_G2_HATCH_PREREG.md
      sha256 c5fde1341873b983e854b4de719c7d2cb1b4a75157d1847afa74af174f42f1c4

B1259 proved no FLAT G2 orbifold has an element with a 0-dimensional fixed set
(G2 < SO(7); every element of SO(odd) has eigenvalue +1).  B1304 scoped its
CONSEQUENCE: the lemma "does not by itself rule out an isolated enhancement
stratum ... Its quantifiers may not be interchanged", and reopened that as a
question.  No arc has walked it.

TWO READINGS, run together until now:
  R1  an isolated maximal-isotropy STRATUM (the apex, where everything meets)
      -- what B1304 established, on (Z/2)^3
  R2  an isolated A1-E6 INTERSECTION -- what Acharya-Witten needs

This cell computes R2 exactly on B1084's own Ghat (|Ghat| = 96), reusing
B1084's own exact Q(sqrt2) machinery by executing its verifier and taking its
namespace -- no reimplementation of the group.
"""
from __future__ import annotations

import io
import os
import sys
from contextlib import redirect_stdout

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
B1084 = os.path.join(ROOT, "frontier", "B1084_g2_cone", "exact_verify.py")


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def main() -> int:
    print("=" * 78)
    print(" THE REOPENED G2 HATCH -- R1 vs R2")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/THE_REOPENED_G2_HATCH_PREREG.md
    sha256 c5fde1341873b983e854b4de719c7d2cb1b4a75157d1847afa74af174f42f1c4""")
    failures = []

    # ------------------------------------------------------------------ G1
    rule("CONTROL G1 -- B1084's own verifier re-run; its banked items must PASS")
    ns = {"__name__": "b1084_exact", "__file__": B1084}
    buf = io.StringIO()
    with redirect_stdout(buf):
        with open(B1084, encoding="utf-8") as fh:
            exec(compile(fh.read(), B1084, "exec"), ns)
    out = buf.getvalue()
    checks = [
        ("|Ghat| = 96", "ITEM 1: |Ghat| (exact closure) = 96"),
        ("census {3:53, 1:42}", "census over 95 nonidentity elements: {3: 53, 1: 42}"),
        ("stabiliser(R^3) = 24", "ITEM 3: |pointwise-stabilizer(R^3 (+) 0)| = 24"),
        ("stabiliser is the 2T copy", "ITEM 3: equals the left-2T copy exactly: True"),
        ("30 A1 planes, stabiliser 2", "pointwise-stabilizer-order distribution over the 30 planes: {2: 30}"),
        ("orbits [6, 12, 12]", "orbit sizes = [6, 12, 12]"),
    ]
    ok_g1 = True
    for label, needle in checks:
        hit = needle in out
        print(f"    [{'ok ' if hit else 'MISS'}] {label}")
        ok_g1 = ok_g1 and hit
    fails = out.count("RESULT: FAIL")
    print(f"    B1084 items reporting FAIL: {fails}")
    ok_g1 = ok_g1 and fails == 0
    print(f"    -> {'PASS' if ok_g1 else 'FAIL'}")
    if not ok_g1:
        failures.append("G1")
        print("    nothing after this counts; stopping.")
        return 1

    group = ns["group"]; I7 = ns["I7"]; I3 = ns["I3"]
    rank = ns["rank"]; mat_sub = ns["mat_sub"]; mat_eq = ns["mat_eq"]
    nullspace_basis = ns["nullspace_basis"]; mat_key = ns["mat_key"]
    QZ = ns["QZERO"] if "QZERO" in ns else None

    def fix_basis(M):
        """Exact basis of ker(M - I7) = Fix(M), over Q(sqrt2)."""
        return nullspace_basis(mat_sub(M, I7), 7)

    def dim_span(vecs):
        return rank([list(v) for v in vecs]) if vecs else 0

    def dim_meet(U, V):
        """dim(U cap V) = dim U + dim V - dim(U + V), all exact."""
        return dim_span(U) + dim_span(V) - dim_span(list(U) + list(V))

    # ------------------------------------------------------------------ G3
    rule("CONTROL G3 -- the routine must be able to RETURN ZERO")
    print("""
    An intersection routine that can only ever report >= 1 is an instrument
    that cannot fire (#164).  Two subspaces of R^7 meeting only at the origin
    are constructed and the routine is required to return 0.
""")
    e = [[ns["QONE"] if j == i else ns["QZERO"] for j in range(7)] for i in range(7)] \
        if "QONE" in ns and "QZERO" in ns else None
    if e is None:
        one = I7[0][0]; zero = mat_sub(I7, I7)[0][0]
        e = [[one if j == i else zero for j in range(7)] for i in range(7)]
    U0 = [e[0], e[1], e[2]]
    V0 = [e[3], e[4], e[5], e[6]]
    d0 = dim_meet(U0, V0)
    Vsame = [e[2], e[3]]
    d1 = dim_meet(U0, Vsame)
    print(f"    span(e1,e2,e3) cap span(e4,e5,e6,e7) = {d0}   (must be 0)")
    print(f"    span(e1,e2,e3) cap span(e3,e4)       = {d1}   (must be 1)")
    ok_g3 = (d0 == 0 and d1 == 1)
    print(f"    -> {'PASS' if ok_g3 else 'FAIL'}")
    if not ok_g3:
        failures.append("G3")

    # ------------------------------------------------------------------ the loci
    rule("THE LOCI, from B1084's own group")
    twoT = [M for M in group if mat_eq([row[:3] for row in M[:3]], I3)]
    E6 = None
    for M in twoT:
        B = fix_basis(M)
        E6 = B if E6 is None else [v for v in E6 if dim_meet([v], B) == 1]
    E6dim = dim_span(E6)
    print(f"    E6 locus = common fixed space of the {len(twoT)}-element 2T copy: dim {E6dim}")

    a1 = []
    idk = mat_key(I7)
    for M in group:
        if mat_key(M) == idk:
            continue
        M3 = [row[:3] for row in M[:3]]; M4 = [row[3:] for row in M[3:]]
        d3 = 3 - rank(mat_sub(M3, I3)); d4 = 4 - rank(mat_sub(M4, ns["I4"]))
        if (d3, d4) == (1, 2):
            a1.append((M, fix_basis(M)))
    print(f"    A1 loci = fixed spaces of the (1,2)-type elements: {len(a1)} of them, "
          f"each dim {dim_span(a1[0][1]) if a1 else '-'}")

    # ------------------------------------------------------------------ G4 + the question
    rule("CONTROL G4 + THE QUESTION -- every A1 locus against the E6 locus, exact")
    print(f"    population: {len(a1)} A1 loci, 1 E6 locus, {len(a1)} intersections")
    assert len(a1) > 0 and E6dim > 0, "empty population -- the B1197 vacuity trap"
    dist = {}
    zero_hits = []
    for idx, (M, B) in enumerate(a1):
        d = dim_meet(E6, B)
        dist[d] = dist.get(d, 0) + 1
        if d == 0:
            zero_hits.append(idx)
    print(f"    intersection-dimension distribution: {dict(sorted(dist.items()))}")
    print(f"    A1 loci meeting E6 in dimension 0: {len(zero_hits)}")

    outcome = "A" if zero_hits else "B"
    print(f"\n    -> OUTCOME {outcome}")
    if outcome == "A":
        print("""    Some A1 locus meets the E6 locus at the origin alone.  R2 HOLDS on this
    Ghat: AW isolation is available in the sense the construction needs, and
    the reopened hatch is genuinely open.""")
    else:
        print(f"""    EVERY A1 locus meets the E6 locus in dimension {sorted(dist)[0]}.  R2 FAILS.

    THE REASON, and it is structural rather than numerical: the E6 locus is
    R^3 (+) 0, and each A1 locus is (a line in R^3) (+) (a plane in H).  Their
    intersection is therefore that line -- dimension 1 -- for every one of the
    {len(a1)} planes.  No choice of A1 locus escapes it.

    SO THE TWO READINGS COME APART, and the cell's whole content is that they
    do:
      R1  the apex IS an isolated maximal-isotropy stratum -- B1304 is right,
          and the SO(odd) lemma does not touch it.
      R2  no A1-E6 enhancement is isolated -- what Acharya-Witten needs is
          absent from this Ghat.
    THE HATCH IS OPEN AS STATED AND SHUT AS NEEDED.""")

    rule("WHAT THIS DOES NOT SAY")
    print("""    It does not say what Acharya-Witten's theorem formally requires: that is
    literature, and B1304's own fence on its (Z/2)^3 example is "the example is
    not an Acharya-Witten construction".  This cell computes GEOMETRY and puts
    the two readings side by side so a specialist can say which one AW needs.

    It does not close the 7d route.  B1259's own consequence stands and is
    where this axis continues: chiral matter "requires genuine CURVATURE -- a
    conical G2 singularity, whose local model is a CONE OVER A 6-MANIFOLD
    rather than a linear action on R^7".  Every result here is about FLAT
    orbifolds, which is precisely the class B1259 closed.

    No chiral matter is derived.  No generation count -- I-26 is UNEARNED and
    untouched.  No value.  Gate 5 untouched.""")

    rule("VERDICT")
    print(f"    OUTCOME {outcome}   ({len(a1)} intersections, dims {dict(sorted(dist.items()))})")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
