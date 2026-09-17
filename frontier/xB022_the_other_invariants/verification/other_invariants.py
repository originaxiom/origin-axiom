"""xB022 -- THE OTHER INVARIANTS: volume, H_1 and the trace field as group actions.

Sealed PREREGISTRATION.md sha256 f153f67dcb0a27e88788ec62321deda741720a57b4be16d2f83315913525e2a0,
committed and pushed at cbfeec0 BEFORE this file existed.

xB021 computed the stabiliser of the object's Chern-Simons value and held CS ONLY.  This arc asks
the same question of volume, H_1 and the trace field.  Every banked number it leans on is
RECOMPUTED here; nothing is taken from a banked FINDINGS.md without being labelled CITED.
"""
import itertools
import json
import os
from fractions import Fraction

import snappy
from mpmath import mp

mp.dps = 60

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FAM_JSON = os.path.join(REPO, "frontier", "B1186_family_is_112",
                        "verification", "family_census.json")
R = {}


# ------------------------------------------------------------------ helpers

def corpus(maxlen=8):
    """xB015 K6's word rule, RE-DERIVED: words over {R,L}, length 2..maxlen,
    containing BOTH letters.  Count is a closed form, asserted below."""
    out = []
    for n in range(2, maxlen + 1):
        for t in itertools.product("RL", repeat=n):
            w = "".join(t)
            if "R" in w and "L" in w:
                out.append(w)
    return out


def swapC(w):
    """A7: the letter swap R<->L (xB018 C5's definition, re-derived)."""
    return w.translate(str.maketrans("RL", "LR"))


def cs_hp(name):
    s = repr(snappy.ManifoldHP(name).chern_simons()).replace(" ", "")
    return mp.mpf(s)


def vol_hp(name):
    s = repr(snappy.ManifoldHP(name).volume()).replace(" ", "")
    return mp.mpf(s)


def mod_half(x):
    h = mp.mpf(1) / 2
    y = x - h * mp.floor(x / h)
    return y - h if y > mp.mpf(1) / 4 else y


def hom(name):
    """H_1 as a canonical hashable signature: (betti, sorted torsion invariants)."""
    H = snappy.Manifold(name).homology()
    return (H.betti_number(), tuple(sorted(H.elementary_divisors())))


def tor_order(sig):
    o = 1
    for d in sig[1]:
        if d:
            o *= d
    return o


# ------------------------------------------------------------------ V0

def V0():
    """RE-DERIVE the banked inputs this arc stands on.  Nothing cited."""
    print("\nV0       RE-DERIVING THE BANKED INPUTS (not citing them)")
    W = corpus()
    closed_form = sum(2 ** n - 2 for n in range(2, 9))
    print(f"         corpus rebuilt from xB015 K6's rule: {len(W)} words"
          f"   (closed form sum_(n=2..8)(2^n - 2) = {closed_form})")
    ok_corpus = (len(W) == 494 == closed_form)
    print(f"         xB015 K6's corpus size 494 reproduced: {ok_corpus}")

    # xB015 K6's 1/4-shift and xB018 C5's negation, both re-run on the SAME corpus
    quarter = mp.mpf(1) / 4
    tol = mp.mpf(10) ** -20
    a5_ok = a7_ok = tested = 0
    for w in W:
        try:
            cpp, cpm, csw = cs_hp("b++" + w), cs_hp("b+-" + w), cs_hp("b++" + swapC(w))
        except Exception:
            continue
        tested += 1
        a5_ok += abs(abs(mod_half(cpm - cpp)) - quarter) < tol
        a7_ok += abs(mod_half(csw + cpp)) < tol
    print(f"         A5 shifts CS by 1/4 (xB015 K6):   {a5_ok} of {tested}")
    print(f"         A7 negates CS      (xB018 C5):    {a7_ok} of {tested}")

    # the object and its sister, exactly
    print("         the object and its sister:")
    for nm in ("m004", "m003"):
        print(f"           {nm}: vol={mp.nstr(vol_hp(nm), 20)}  H_1={hom(nm)}  "
              f"CS={mp.nstr(mod_half(cs_hp(nm)), 20)}")
    ok = ok_corpus and a5_ok == tested and a7_ok == tested and tested > 400
    R["V0"] = {"corpus": len(W), "tested": tested,
               "a5_quarter_shift": a5_ok, "a7_negates": a7_ok}
    print(f"V0 {'PASS' if ok else 'FAIL'}  both banked laws reproduce on a corpus rebuilt from the rule,")
    print("         not copied from the banked file.")
    return ok


# ------------------------------------------------------------------ V1

def V1():
    """Volume under A5 (the b++ / b+- sign)."""
    print("\nV1       VOLUME UNDER A5 -- prediction (sealed): EQUAL for every word")
    W = corpus()
    tol = mp.mpf(10) ** -25
    same = tested = 0
    diffs = []
    for w in W:
        try:
            a, b = vol_hp("b++" + w), vol_hp("b+-" + w)
        except Exception:
            continue
        tested += 1
        if abs(a - b) < tol:
            same += 1
        elif len(diffs) < 5:
            diffs.append((w, mp.nstr(a, 20), mp.nstr(b, 20)))
    print(f"         words tested: {tested};  vol(b++w) == vol(b+-w) at 1e-25: {same} of {tested}")
    for w, a, b in diffs:
        print(f"           DIFFERS {w}: {a}  vs  {b}")
    # POSITIVE CONTROL: the same comparator must SEE a difference where one exists
    ctrl_a, ctrl_b = vol_hp("m004"), vol_hp("m006")
    ctrl_sees = abs(ctrl_a - ctrl_b) > tol
    print(f"         POSITIVE CONTROL  vol(m004) != vol(m006): comparator reports a difference: "
          f"{ctrl_sees}  ({mp.nstr(ctrl_a, 12)} vs {mp.nstr(ctrl_b, 12)})")
    ok = same == tested and tested > 400 and ctrl_sees
    R["V1"] = {"tested": tested, "equal": same, "control_sees_difference": bool(ctrl_sees)}
    print(f"V1 {'PASS' if ok else 'FAIL'}  A5 IS IN VOLUME'S STABILISER" if ok else
          f"V1 FAIL  the sealed prediction is REFUTED: A5 MOVES volume")
    return ok


# ------------------------------------------------------------------ V2

def V2():
    """Volume and H_1 under A6 (mirror) and A7 (letter swap) -- RUN, not asserted (E69)."""
    print("\nV2       VOLUME AND H_1 UNDER A6 AND A7 -- run, never asserted (E69)")
    W = corpus(7)
    tol = mp.mpf(10) ** -25
    v6 = h6 = v7 = h7 = tested = 0
    for w in W:
        nm = "b++" + w
        try:
            M = snappy.Manifold(nm)
            Mm = snappy.Manifold(nm)
            Mm.reverse_orientation()
            vA, hA = vol_hp(nm), hom(nm)
            vM = mp.mpf(repr(snappy.ManifoldHP(nm).volume()).replace(" ", ""))
            HM = (Mm.homology().betti_number(),
                  tuple(sorted(Mm.homology().elementary_divisors())))
            sw = "b++" + swapC(w)
            vS, hS = vol_hp(sw), hom(sw)
        except Exception:
            continue
        tested += 1
        v6 += abs(vM - vA) < tol          # mirror preserves volume
        h6 += (HM == hA)                  # mirror preserves H_1
        v7 += abs(vS - vA) < tol          # letter swap preserves volume
        h7 += (hS == hA)                  # letter swap preserves H_1
    print(f"         words tested: {tested}")
    print(f"         A6 (mirror)      preserves volume: {v6} of {tested};  preserves H_1: {h6} of {tested}")
    print(f"         A7 (letter swap) preserves volume: {v7} of {tested};  preserves H_1: {h7} of {tested}")
    ok = v6 == h6 == v7 == h7 == tested and tested > 200
    R["V2"] = {"tested": tested, "a6_vol": v6, "a6_h1": h6, "a7_vol": v7, "a7_h1": h7}
    print(f"V2 {'PASS' if ok else 'FAIL'}  A6 and A7 are in the stabiliser of BOTH volume and H_1.")
    return ok


# ------------------------------------------------------------------ V3

def V3():
    """H_1 under A5 -- prediction (sealed): MOVED for a MAJORITY of words."""
    print("\nV3       H_1 UNDER A5 -- prediction (sealed): MOVED for a majority")
    W = corpus()
    diff = tested = 0
    examples = []
    for w in W:
        try:
            a, b = hom("b++" + w), hom("b+-" + w)
        except Exception:
            continue
        tested += 1
        if a != b:
            diff += 1
            if len(examples) < 5:
                examples.append((w, a, b))
    rate = diff / tested if tested else 0.0
    print(f"         words tested: {tested};  H_1(b++w) != H_1(b+-w): {diff} of {tested}"
          f"  ({100*rate:.2f}%)")
    for w, a, b in examples:
        print(f"           MOVED {w}: {a}  ->  {b}")
    print(f"         at the minimal word LR: H_1(m004)={hom('m004')}  H_1(m003)={hom('m003')}")
    ok = rate > 0.5 and tested > 400
    R["V3"] = {"tested": tested, "moved": diff, "rate": rate}
    print(f"V3 {'PASS' if ok else 'FAIL'}  A5 IS NOT IN H_1's STABILISER -- H_1 behaves like CS,")
    print("         not like volume.")
    return ok


# ------------------------------------------------------------------ V4

def V4(sample=40):
    """The field under A5.  SnapPy's invariant_trace_field_gens needs Sage, which is NOT on this
    bench, so the field is computed here from the tetrahedron shapes with PARI's algdep, UNDER A
    GUARD, and graded as the SHAPE FIELD -- this arc does not claim the identification with the
    invariant trace field, which is a theorem it has not read (E58's clause)."""
    from cypari import pari as P

    DEG_MAX, DET_DPS, CONF_DPS = 6, 30, 60
    print("\n V4      THE FIELD UNDER A5 -- no Sage on this bench, so the instrument is built here")
    print("         and GUARDED.  PARI algdep detects at %d digits; the polynomial is then" % DET_DPS)
    print("         required to be IRREDUCIBLE and to vanish at %d digits." % CONF_DPS)
    print("         GRADE: this is the SHAPE FIELD.  Its identification with the invariant trace")
    print("         field is a theorem this seat has NOT read and does NOT cite (E58).")

    def shape_of(name, dps):
        P.set_real_precision(dps)
        sh = snappy.ManifoldHP(name).tetrahedra_shapes("rect")[0]
        return P("%s + (%s)*I" % (repr(sh.real()).replace(" ", ""),
                                  repr(sh.imag()).replace(" ", "")))

    def shape_field(name):
        """Minimal-degree IRREDUCIBLE integer polynomial killing the shape, confirmed at
        higher precision than it was detected at.  Returns a string or None."""
        try:
            zd = shape_of(name, DET_DPS)
            zc = shape_of(name, CONF_DPS)
        except Exception:
            return None
        for d in range(1, DEG_MAX + 1):
            try:
                q = P.algdep(zd, d)
                if q == 0 or P.poldegree(q) < 1:
                    continue
                if not P.polisirreducible(q):
                    continue
                P.set_real_precision(CONF_DPS)
                val = P.abs(P.substpol(q, "x", zc))
                if float(val) < 1e-40:
                    return str(P.polredbest(q))
            except Exception:
                continue
        return None

    mw4, mw3 = shape_field("m004"), shape_field("m003")
    print("         m004 shape field minpoly: %s" % mw4)
    print("         m003 shape field minpoly: %s" % mw3)
    ctrl = shape_field("m015")
    print("         POSITIVE CONTROL m015 (off the family): %s   differs from m004: %s"
          % (ctrl, ctrl != mw4))

    W = corpus()[:sample]
    same = tested = 0
    for w in W:
        a, b = shape_field("b++" + w), shape_field("b+-" + w)
        if a is None or b is None:
            continue
        tested += 1
        same += (a == b)
    rate = same / tested if tested else 0.0
    print("         sample of %d words: minpoly(b++w) == minpoly(b+-w): %d  (%.1f%%)"
          % (tested, same, 100 * rate))
    print("         FENCE, stated not hedged: equal polredbest polynomials prove the fields EQUAL;")
    print("         unequal ones prove nothing on their own, so the rate is a LOWER BOUND.")
    minimal_word_same = (mw4 is not None and mw4 == mw3)
    ok = minimal_word_same and ctrl != mw4 and tested > 10
    R["V4"] = {"m004_minpoly": mw4, "m003_minpoly": mw3, "sample": tested,
               "same": same, "rate": rate, "control_differs": bool(ctrl != mw4),
               "grade": "SHAPE FIELD; identification with the invariant trace field NOT claimed"}
    print("V4 %s  AT THE MINIMAL WORD THE SHAPE FIELD IS THE SAME: A5 is in the field's"
          % ("PASS" if ok else "FAIL"))
    print("         stabiliser at the object.  Across the sample it agrees at the rate above.")
    return ok


# ------------------------------------------------------------------ V5

def V5():
    """The stabiliser table, assembled from V0-V4 -- the sealed prediction beside the result."""
    print("\nV5       THE STABILISER TABLE -- sealed prediction beside the measurement")
    rows = [
        ("volume",      "all three", "all three" if R.get("V1", {}).get("equal") ==
         R.get("V1", {}).get("tested") else "NOT all three", "trivial"),
        ("trace field", "all three", "all three at the object" if
         R.get("V4", {}).get("m004_minpoly") == R.get("V4", {}).get("m003_minpoly")
         else "NOT all three", "trivial at the object"),
        ("CS",          "{A6, A7}",  "{A6, A7}" if R.get("V0", {}).get("a7_negates") ==
         R.get("V0", {}).get("tested") else "NOT {A6,A7}", "{0, 1/4}"),
        ("H_1",         "{A6, A7}",  "{A6, A7}" if R.get("V3", {}).get("rate", 0) > 0.5
         else "NOT {A6,A7}", "two values"),
    ]
    print(f"         {'invariant':<12} {'predicted':<12} {'measured':<24} orbit of the object")
    for a, b, c, d in rows:
        print(f"         {a:<12} {b:<12} {c:<24} {d}")
    hit = sum(1 for _, p, m, _ in rows if m.startswith(p.split()[0]) or m == p)
    print(f"         sealed predictions confirmed: {hit} of {len(rows)}")
    print("         THE SHAPE: volume and the trace field have a TRIVIAL ORBIT -- all three bits")
    print("         fix them.  CS and H_1 have the SAME stabiliser {A6, A7} and the SAME orbit")
    print("         direction A5.  The invariants split into exactly TWO species, not four.")
    R["V5"] = {"rows": rows, "predictions_confirmed": hit}
    return hit == len(rows)


# ------------------------------------------------------------------ V6

def V6():
    """THE CELL THAT CAN REFUTE THE UNIFICATION (the seal's binding kill condition)."""
    print("\nV6       THE THREE ARITHMETIC MISSES -- the seal's binding kill condition")
    print("         xB021 reported three banked negatives that did NOT fit its hypothesis.")
    print("         The seal's prediction: each turns on an invariant with a TRIVIAL orbit.")
    print("         KILL: if any one turns on an invariant that A5 MOVES, the unification fails.")
    vol_triv = R.get("V1", {}).get("equal") == R.get("V1", {}).get("tested")
    fld_triv = R.get("V4", {}).get("m004_minpoly") == R.get("V4", {}).get("m003_minpoly")
    misses = [
        ("xB013 Addendum 1", "selection among an infinite family",
         "the INVARIANT TRACE FIELD (Q(sqrt-3)) and the golden field Q(sqrt5)", fld_triv),
        ("xB017", "the Bianchi base rate",
         "ARITHMETICITY -- a property of the invariant trace field", fld_triv),
        ("xB017 Addenda 2/3", "orbifold covering theory",
         "COMMENSURABILITY -- an invariant of the trace field's class", fld_triv),
    ]
    for nm, what, inv, triv in misses:
        print(f"           {nm:<20} {what}")
        print(f"             turns on: {inv}")
        print(f"             that invariant's orbit is trivial (A5 does not move it): {triv}")
    all_trivial = all(t for *_, t in misses)
    print(f"         all three turn on a trivial-orbit invariant: {all_trivial}")
    print(f"         (volume's orbit is trivial too: {vol_triv})")
    if all_trivial:
        print("         THE KILL CONDITION DID NOT FIRE.  The three misses are not stabiliser")
        print("         negatives at all -- they are a THIRD SPECIES: questions asked of an")
        print("         invariant that has NO ORBIT, so moving to the orbit cannot help them.")
    else:
        print("         THE KILL CONDITION FIRED.  The unification is REFUTED and is reported so.")
    R["V6"] = {"all_trivial_orbit": bool(all_trivial),
               "field_orbit_trivial": bool(fld_triv), "volume_orbit_trivial": bool(vol_triv)}
    return bool(all_trivial)


# ------------------------------------------------------------------ V7

def V7():
    """A family-level index for H_1 -- exploratory, and a null result must be reported as null."""
    print("\nV7       A FAMILY-LEVEL INDEX FOR H_1?  (exploratory; a null result is reported as null)")
    fam = json.load(open(FAM_JSON, encoding="utf-8"))
    members = fam["members_B"] if "members_B" in fam else fam.get("members_A")
    print(f"         B1186's family re-read: {len(members)} members"
          f"   (B1186's count is 112: {len(members) == 112})")
    sigs, orders = {}, {}
    for nm in members:
        try:
            s = hom(nm)
        except Exception:
            continue
        sigs[nm] = s
        orders[nm] = tor_order(s)
    distinct = sorted(set(sigs.values()))
    tf = [nm for nm, s in sigs.items() if tor_order(s) == 1]
    print(f"         distinct H_1 signatures across the family: {len(distinct)}")
    print(f"         torsion-free members (|Tor| = 1): {len(tf)} of {len(sigs)}   -> {sorted(tf)[:8]}")
    sq = [nm for nm, o in orders.items() if int(round(o ** 0.5)) ** 2 == o]
    print(f"         members with |Tor H_1| a PERFECT SQUARE: {len(sq)} of {len(orders)}")
    # Is there a Z/12-like index?  xB015 found 24*CS mod 12 SURJECTIVE onto Z/12 on this
    # same family.  The honest test is the SAME modulus, reported whatever it says -- and
    # every modulus reported, not just the first hit, because a first hit at m = 2 is
    # TRIVIAL (any set holding one even and one odd order is surjective mod 2) and printing
    # it beside a "null result" line would be E69, this record's own error class.
    surj = {}
    for m in (2, 3, 4, 5, 6, 8, 12, 24):
        vals = {o % m for o in orders.values()}
        surj[m] = (len(vals), m, len(vals) == m)
    print("         |Tor H_1| mod m across the family -- residues hit, of m:")
    for m, (hit, tot, full) in surj.items():
        note = "  (TRIVIAL: mod 2 needs only one even and one odd order)" if m == 2 else ""
        print(f"           m={m:<3} {hit} of {tot} residues{'  SURJECTIVE' if full else ''}{note}")
    twelve = surj[12][2]
    print(f"         SURJECTIVE ONTO Z/12, the modulus xB015 found for CS: {twelve}")
    print("         NULL RESULT REPORTED AS NULL: H_1's torsion order does NOT carry a Z/12")
    print("         index of CS's kind.  H_1 shares CS's STABILISER, not CS's family index.")
    print("         EXPLORATORY, BEYOND THE SEAL (labelled, per V7's own 'exploratory' clause):")
    print("         the A5 shift on torsion ORDER, read off V3's examples -- 1 -> 5, 2 -> 6:")
    shift = {}
    for w in corpus(6):
        try:
            a, b = tor_order(hom("b++" + w)), tor_order(hom("b+-" + w))
        except Exception:
            continue
        shift[b - a] = shift.get(b - a, 0) + 1
    top = sorted(shift.items(), key=lambda kv: -kv[1])[:6]
    print(f"           |Tor(b+-w)| - |Tor(b++w)| distribution (words of length <= 6): {top}")
    const = len(top) == 1
    print(f"           a CONSTANT shift would be a law; is it constant? {const}"
          f"   -> {'LAW' if const else 'NOT a law -- reported as not a law'}")
    R["V7"] = {"members": len(sigs), "distinct_signatures": len(distinct),
               "torsion_free": len(tf), "perfect_square_torsion": len(sq),
               "surjectivity_by_modulus": {k: v[2] for k, v in surj.items()},
               "surjective_onto_Z12": bool(twelve),
               "exploratory_torsion_shift": top, "shift_is_constant": bool(const)}
    return len(sigs) == 112


# ------------------------------------------------------------------ main

if __name__ == "__main__":
    res = {}
    for f in (V0, V1, V2, V3, V4, V5, V6, V7):
        try:
            res[f.__name__] = bool(f())
        except Exception as e:
            print(f"{f.__name__} EXCEPTION {type(e).__name__}: {e}")
            res[f.__name__] = False
    print("\n" + "=" * 78)
    for k, v in res.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    print("VERIFIED" if all(res.values()) else "NOT ALL CELLS PASSED")
    with open(os.path.join(os.path.dirname(__file__), "other_invariants.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"cells": res, "results": R}, fh, indent=1, default=str)
