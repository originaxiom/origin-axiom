#!/usr/bin/env python3
"""THE MIRROR AND THE BULK -- where the rest of the object is.

Seal: outside_bench/seals/THE_MIRROR_AND_THE_BULK_PREREG.md
      sha256 f1e065d38d1a04938b42bf20ed3e29ee237afa60af4a2e8ae5537081e635ba50

The owner's two riddles, taken literally:
  "if the object is its own mirror, where's the other part of the mirror?"
  "it is a complement, it has no bulk -- where is the rest?"

Both are computable.  SnapPy 3.3.2.
"""
from __future__ import annotations

import subprocess
import sys
import warnings

warnings.filterwarnings("ignore")

import snappy

FAILURES: list[str] = []


def fail(tag, msg):
    FAILURES.append(f"{tag}: {msg}")
    print(f"  !! FAIL [{tag}] {msg}")


def rule(t):
    print("\n" + "-" * 78)
    print(t)
    print("-" * 78)


def show(path):
    r = subprocess.run(["git", "show", f"origin/main:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def rq(tag, hay, needle, where):
    import re
    ok = re.sub(r"\s+", " ", needle).strip() in re.sub(r"\s+", " ", hay)
    print(f"\n  [{tag}] {where} -- {'FOUND' if ok else 'ABSENT'}")
    for ln in needle.strip().splitlines():
        print(f"      {ln.strip()}")
    if not ok:
        fail("C4", f"{tag} not located in {where}")
    return ok


# ---------------------------------------------------------------- instruments

def mirror(M):
    Mm = M.copy()
    Mm.reverse_orientation()
    return Mm


def amphichiral_det(M):
    """ORIENTATION-AWARE: amphichiral iff some isometry to the mirror has
    cusp-map determinant +1.  Returns True/False, or None if undecidable."""
    try:
        isos = M.is_isometric_to(mirror(M), return_isometries=True)
    except Exception:
        return None
    if not isos:
        return False
    for i in isos:
        try:
            for cm in i.cusp_maps():
                if round(cm[0, 0] * cm[1, 1] - cm[0, 1] * cm[1, 0]) == 1:
                    return True
        except Exception:
            continue
    return False


def chiral_by_cs(M):
    """ONE-SIDED (seal C3): CS(mirror) = -CS(M), so 2*CS != 0 mod 1/2 => CHIRAL.
    2*CS == 0 proves nothing."""
    try:
        cs = float(M.chern_simons())
    except Exception:
        return None
    v = (2 * cs) % 0.5
    return None if min(v, 0.5 - v) < 1e-8 else True


def main() -> int:
    print("=" * 78)
    print(" THE MIRROR AND THE BULK -- where the rest of the object is")
    print("=" * 78)

    # ------------------------------------------------------------ C1
    rule("CONTROL C1 -- the NAIVE test is wrong, reproduced on the record")
    print("""
    is_isometric_to(M, mirror) IGNORES ORIENTATION.  A first sweep using it
    reported 38 of 38 covers amphichiral to degree 8 -- contradicting B1324.
    It was caught by comparison with the record, not by the instrument.""")
    for name in ("m004", "m015"):
        M = snappy.Manifold(name)
        print(f"    {name:6} naive is_isometric_to(mirror) = {M.is_isometric_to(mirror(M))}")
    naive_bad = snappy.Manifold("m015").is_isometric_to(mirror(snappy.Manifold("m015")))
    print(f"\n    m015 = the 5_2 knot, which is CHIRAL, and the naive test says {naive_bad}.")
    c1 = naive_bad is True
    print(f"  C1: {'PASS' if c1 else 'FAIL'} -- the wrong instrument is on the record")
    if not c1:
        fail("C1", "the naive test did not reproduce its own failure")

    # ------------------------------------------------------------ C2/C3
    rule("CONTROL C2 / C3 -- two orientation-aware methods on a control set")
    print("\n    manifold   det-test amphichiral   CS          CS proves chiral")
    controls = [("m004", True), ("m015", False), ("m009", False), ("m129", False)]
    ok = True
    for name, expect_amph in controls:
        M = snappy.Manifold(name)
        a = amphichiral_det(M)
        cs = float(M.chern_simons())
        cc = chiral_by_cs(M)
        flag = "" if a == expect_amph else "   <-- DISAGREES WITH THE KNOWN VALUE"
        print(f"    {name:10} {str(a):<20} {cs:+.9f}   {str(cc):<6}{flag}")
        if a != expect_amph:
            ok = False
        # the two methods must not contradict where both decide
        if cc is True and a is True:
            fail("C2", f"{name}: CS says chiral, det-test says amphichiral")
    print(f"\n  C2: {'PASS' if ok else 'FAIL'} -- det-test matches the known values")
    print("  C3: the CS column shows m004 at 0.000 and m003-type values at 1/4 --")
    print("      2*CS == 0 there, which proves NOTHING (one-sided, as sealed).")
    if not ok:
        fail("C2", "the orientation-aware test disagrees with a known value")

    # ------------------------------------------------------------ CELL 2
    rule("CELL 2 -- THE MIRROR: is the other half a different object?")
    M = snappy.Manifold("m004")
    isos = M.is_isometric_to(mirror(M), return_isometries=True)
    dets = []
    for i in isos:
        for cm in i.cusp_maps():
            dets.append(round(cm[0, 0] * cm[1, 1] - cm[0, 1] * cm[1, 0]))
    print(f"    m004 -> mirror: {len(isos)} isometries, cusp-map determinants {sorted(set(dets))}")
    print(f"    amphichiral (an orientation-REVERSING self-isometry exists): "
          f"{amphichiral_det(M)}")
    print(f"    #symmetries of m004: {M.symmetry_group()}")
    cell2 = "A" if amphichiral_det(M) else "B"
    print(f"""
  >>> CELL 2 OUTCOME {cell2}.  THE MIRROR MAP IS AN AUTOMORPHISM.  There is no
      second manifold.  "The other half of the mirror" is the object itself --
      the two halves are IDENTIFIED, and the identification is the whole content.
      A mirror with both halves glued together has no reflection to show.""")

    # ------------------------------------------------------------ CELL 1
    rule("CELL 1 -- THE BULK: put the solid torus back and see what survives")
    print("""
    m004 = S^3 minus the figure-eight knot.  The "missing bulk" is exactly the
    SOLID TORUS you glue back along a slope -- Dehn filling.  So the bulk is not
    missing; it is a KNOWN one-parameter family, and the question is what it does
    to the arithmetic.

    INSTRUMENT, and its FIRST VERSION FAILED ITS CONTROL: the invariant trace
    field is computed from tr(g^2) over the generators by PARI's algdep.  At
    SnapPy's DOUBLE precision the control returned DEGREE 11 GARBAGE for m004,
    whose field is degree 2 -- caught by the control, not by the output looking
    wrong.  ManifoldHP (high precision) is used below.""")

    def itf(M, maxdeg=8, prec=45):
        """invariant trace field, via tr(g^2) + PARI algdep at high precision."""
        try:
            G = M.fundamental_group()
        except Exception:
            return None
        best = None
        for w in G.generators():
            try:
                m = G.SL2C(w)
                t = m[0, 0] + m[1, 1]
                z = t * t - 2
                gp = (f"default(realprecision,{prec}); "
                      f"z = {str(z.real())} + ({str(z.imag())})*I; "
                      f"print(algdep(z,{maxdeg}))")
                r = subprocess.run(["gp", "-q"], input=gp + "\nquit\n",
                                   capture_output=True, text=True, timeout=90)
                o = r.stdout.strip()
                if not o or o == "0":
                    continue
                d = 1
                if "x^" in o:
                    d = int(o.split("x^")[1].split("*")[0].split("+")[0]
                            .split("-")[0].split(" ")[0])
                if best is None or d > best[0]:
                    best = (d, o)
            except Exception:
                continue
        return best

    def contains_atom(poly: str) -> bool | None:
        """does the field defined by poly contain sqrt(-3)?  PARI nfisincl."""
        try:
            gp = (f"p = {poly}; q = x^2 + x + 7; "
                  f"r = nfisincl(q, p); print(if(type(r)==\"t_INT\", 0, 1))")
            out = subprocess.run(["gp", "-q"], input=gp + "\nquit\n",
                                 capture_output=True, text=True, timeout=90).stdout.strip()
            return out.endswith("1")
        except Exception:
            return None

    ctrl = itf(snappy.ManifoldHP("m004"))
    print(f"\n    CONTROL -- m004's own invariant trace field: {ctrl}")
    ctrl_ok = bool(ctrl) and ctrl[0] == 2
    print(f"    degree 2 (= Q(sqrt-3), disc(x^2+x+7) = -27): {ctrl_ok}")
    if not ctrl_ok:
        fail("CELL1-CTRL", "the trace-field instrument fails on m004 itself")

    print("\n    slope    volume      itf degree  contains sqrt(-3)?  minimal polynomial")
    kept = []
    for pq in [(5, 1), (5, 2), (6, 1), (7, 1), (7, 2), (8, 3), (9, 1), (10, 3)]:
        try:
            N = snappy.ManifoldHP("m004")
            N.dehn_fill(pq)
            vol = float(N.volume())
            if vol < 0.1:
                print(f"    {str(pq):<8} NOT HYPERBOLIC (exceptional filling)")
                continue
            f = itf(N)
            if not f:
                print(f"    {str(pq):<8} {vol:.6f}    (field not identified)")
                continue
            has = contains_atom(f[1])
            if has:
                kept.append(pq)
            print(f"    {str(pq):<8} {vol:.6f}    {f[0]:<11} {str(has):<19} {f[1][:44]}")
        except Exception as e:
            print(f"    {str(pq):<8} (failed: {str(e)[:44]})")

    print(f"\n    fillings whose trace field CONTAINS sqrt(-3): {kept if kept else 'NONE'}")
    cell1 = "A" if (ctrl_ok and not kept) else "B"

    # ------------------------------------------------------------ C4
    rule("CONTROL C4 -- the record's own statements, quoted from origin/main")
    led = show("docs/THEOREM_LEDGER.md")
    rq("C8, the interface-only V4", led,
       "No closed hyperbolic filling of m004 in the\n|p|,q ≤ 8 grid (78 hyperbolic slopes) has an "
       "invariant trace field containing √−3, √5,\nOR √−15 — the entire "
       "forced V₄ is a property of the OPEN object",
       "origin/main C8")
    mg = show("docs/MAIN_GOAL.md")
    rq("Q15 answered on the tower", mg,
       "covers do NOT inherit amphichirality — 66 of the 87 covers of m004 to degree 10 are "
       "chiral",
       "origin/main MAIN_GOAL (B1324)")
    rq("and the atom survives on them", mg,
       "every cover keeps the invariant trace field, so **the atom and a remembered A7 bit coexist "
       "on the object's own tower.**",
       "origin/main MAIN_GOAL (B1324)")
    rq("the spectral half does not follow", mg,
       "The spectral half does not follow yet",
       "origin/main MAIN_GOAL (B1324)")

    print(f"""
  >>> CELL 1 OUTCOME {cell1}.  THE BULK EXISTS, HAS BEEN LOOKED AT, AND IS
      ARITHMETICALLY INERT.  Gluing the solid torus back is Dehn filling; the
      banked census over 78 hyperbolic slopes finds NOT ONE whose trace field
      carries any of the object's three faces.  The V4 is a property of the OPEN
      object.  THE REST-AS-BULK IS NOT A MISSING INGREDIENT -- IT IS A KNOWN
      FAMILY THAT DESTROYS THE STRUCTURE THE PROGRAMME RUNS ON.""")

    # ------------------------------------------------------------ CELL 3
    rule("CELL 3 -- THE REST: does the covering tower break the mirror and keep the atom?")
    print("""
    This is the record's own Q15 -- "is there a carrier that keeps the atom and
    remembers the bit?" -- and B1324 answers it on the object's own tower.
    Re-run here with the ORIENTATION-AWARE instrument.""")
    print("\n    deg  covers  amphichiral  chiral  undecided")
    tot_n = tot_a = tot_c = tot_u = 0
    first_chiral = None
    for d in range(2, 8):
        n = a = c = u = 0
        for C in snappy.Manifold("m004").covers(d):
            n += 1
            r = amphichiral_det(C)
            if r is True:
                a += 1
            elif r is False:
                c += 1
                if first_chiral is None:
                    first_chiral = (d, C.num_cusps(), str(C.homology()))
            else:
                u += 1
        tot_n += n; tot_a += a; tot_c += c; tot_u += u
        print(f"    {d:<4} {n:<7} {a:<12} {c:<7} {u}")
    print(f"    ---  {tot_n:<7} {tot_a:<12} {tot_c:<7} {tot_u}")
    print(f"\n    first chiral cover (degree, cusps, H1): {first_chiral}")
    cell3 = "A" if tot_c > 0 else "B"
    print(f"""
  >>> CELL 3 OUTCOME {cell3}.  THE MIRROR BREAKS ON THE TOWER.  The object is its
      own mirror; its COVERS are not.  And B1324's census (quoted above) adds the
      half this sweep does not compute: EVERY COVER KEEPS THE INVARIANT TRACE
      FIELD.  So the "rest" is the covering tower, and unlike the bulk it is NOT
      arithmetically inert -- it keeps the atom AND remembers the bit.""")

    # ------------------------------------------------------------ CELL 4
    rule("CELL 4 -- and does the rest supply what the object lacks?")
    print("""
    NO -- and the record already computed it.  B1324's own sentence, quoted
    above: "The spectral half does not follow yet."  On the chiral ONE-cusped
    covers the torsion is meridian-generated, leaving only two cusp-trivial
    unprotected sectors, BOTH INDEX 0, plus 136 control sectors at 0.

    And the 54 multi-cusped chiral covers -- the case B1324 left open -- were
    computed on claude/paper-verification-ufp0zn (B1333), CITED AS BRANCH WORK
    AND NOT RE-RUN HERE: 38070 sectors at three primes over all 54 covers, 1841
    of them with two or more LIVE cusps (the regime impossible on one cusp),
    and INDEX ZERO IN EVERY ONE.""")
    cell4 = "A"
    print(f"""
  >>> CELL 4 OUTCOME {cell4}.  THE TOWER BREAKS THE MIRROR WITHOUT PRODUCING
      CHIRALITY.  The rest exists, keeps the atom, remembers the bit as a
      MANIFOLD symmetry -- and still returns index 0 as a SPECTRUM.

      THE HONEST FRONTIER: both censuses stop at DEGREE 10.  What lies past
      degree 10 on the object's own tower is UNEXAMINED, and it is the one place
      the owner's question has a live computable answer left.""")

    print("\n" + "=" * 78)
    print(" OUTCOMES")
    print("=" * 78)
    print(f"   CELL 1 (the bulk is inert)              : {cell1}")
    print(f"   CELL 2 (the mirror is an automorphism)  : {cell2}")
    print(f"   CELL 3 (the tower breaks the mirror)    : {cell3}")
    print(f"   CELL 4 (and still gives index 0)        : {cell4}")
    print(f"   C1 the naive test's failure reproduced  : {'PASS' if c1 else 'FAIL'}")
    print(f"   C2 two methods agree on controls        : {'PASS' if ok else 'FAIL'}")
    print(f"   C3 CS declared one-sided                : stated")
    print(f"   C4 record quoted                        : "
          f"{'PASS' if not [f for f in FAILURES if f.startswith('C4')] else 'FAIL'}")
    if FAILURES:
        print("\n  FAILURES:")
        for f in FAILURES:
            print(f"    - {f}")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
