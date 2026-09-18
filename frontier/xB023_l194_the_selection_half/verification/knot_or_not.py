"""xB023 ADDENDUM 2 -- is o10_143849 actually a knot complement in S^3?

SEALED at 8be6f04f before this file existed.  ADDENDUM_2 declares:
  N1 banked datum re-derived, exact agreement expected
  N2 THE DECISION: CensusKnots is COMPLETE to 10 ideal tetrahedra and o10_143849 has 10,
     so membership decides.  Prediction: NOT a census knot; >= 8 of the 14 zero-class ones ARE.
     KILL: if it IS one, we have an explicit witness that cusped eta=0 coexists with cs=1/4.
  N3 second instrument: 6-theorem slope search for an S^3 filling.  CALIBRATED on m004 first --
     if the machinery cannot find m004's own S^3 filling its negative is worthless.
  N4 sec.3's prediction re-run with the REAL predicate (in CensusKnots) in place of the proxy (H_1 = Z).
     Vacuity: fewer than 5 amphicheiral census knots => UNDERPOWERED, not confirmation.
"""
import json
import math
import os
import sys
import warnings

warnings.filterwarnings("ignore")
import snappy
from mpmath import mp

mp.dps = 30
TOL = mp.mpf(10) ** -9
R = {}
TARGET = "o10_143849"
# the 14 zero-class H_1 = Z members are recomputed, never recalled (Addendum 1 printed only 6)


def cs_class(M):
    """CS class mod 1/2, folded to [-1/4, 1/4].  Identical to Addendum 1's function."""
    try:
        s = repr(snappy.ManifoldHP(M.isometry_signature()).chern_simons()).replace(" ", "")
    except Exception:
        return None
    x = mp.mpf(s)
    h = mp.mpf(1) / 2
    y = x - h * mp.floor(x / h)
    if y > mp.mpf(1) / 4:
        y -= h
    if abs(y) < TOL:
        return "zero"
    if abs(abs(y) - mp.mpf(1) / 4) < TOL:
        return "quarter"
    return "other"


def h1sig(M):
    H = M.homology()
    return (H.betti_number(), tuple(sorted(d for d in H.elementary_divisors() if d)))


def amphicheiral(M):
    try:
        G = M.symmetry_group()
        return bool(G.is_full_group() and G.is_amphicheiral())
    except Exception:
        return None


# ---------------------------------------------------------------- N1
def N1():
    print("\nN1       THE BANKED DATUM, RE-DERIVED FROM SCRATCH (not recalled)")
    M = snappy.Manifold(TARGET)
    got = {
        "num_cusps": M.num_cusps(),
        "num_tetrahedra": M.num_tetrahedra(),
        "orientable": bool(M.is_orientable()),
        "solution_type": M.solution_type(),
        "volume": float(M.volume()),
        "homology": str(M.homology()),
        "h1sig": h1sig(M),
        "amphicheiral": amphicheiral(M),
        "symmetry_group": str(M.symmetry_group()),
        "cs_class": cs_class(M),
    }
    for k, v in got.items():
        print(f"         {k:18s} {v}")
    want = {"num_cusps": 1, "num_tetrahedra": 10, "orientable": True,
            "h1sig": (1, ()), "amphicheiral": True, "cs_class": "quarter"}
    bad = {k: (got[k], v) for k, v in want.items() if got[k] != v}
    R["N1"] = {"measured": got, "expected": want, "disagreements": bad}
    if bad:
        print(f"         *** DISAGREEMENT WITH ADDENDUM 1: {bad}")
        print("         Addendum 1's table is wrong and THAT is the headline.")
    else:
        print("         EXACT AGREEMENT with Addendum 1 on all six checked fields.")
    print(f"N1 {'PASS' if not bad else 'FAIL'}")
    return not bad


# ---------------------------------------------------------------- N2
def N2():
    print("\nN2       THE DECISION -- CensusKnots is complete to 10 ideal tetrahedra")
    doc = snappy.CensusKnots.__doc__ or ""
    complete = "at most 10 ideal tetrahedra" in " ".join(doc.split())
    print(f"         completeness sentence present in CensusKnots docstring: {complete}")
    print(f"         |CensusKnots| = {len(snappy.CensusKnots())}")
    # -- instrument calibration: a manifold KNOWN to be an S^3 knot complement must be found
    cal = {}
    for nm in ("m004", "m003"):
        cal[nm] = str(snappy.CensusKnots.identify(snappy.Manifold(nm)))
    print(f"         CALIBRATION  m004 (= S^3 minus 4_1, a knot complement): {cal['m004']}")
    print(f"         CALIBRATION  m003 (H_1 has torsion, provably NOT one):  {cal['m003']}")
    cal_ok = cal["m004"] != "False" and cal["m003"] == "False"
    print(f"         calibration passes (positive found, negative rejected): {cal_ok}")

    Mt = snappy.Manifold(TARGET)
    ck = snappy.CensusKnots.identify(Mt)
    ident = [str(x) for x in Mt.identify()]
    print(f"         TARGET {TARGET}:  CensusKnots.identify -> {ck}")
    print(f"         TARGET {TARGET}:  identify() all censuses -> {ident}")
    is_knot = str(ck) != "False"

    # -- the control the cell is worthless without: the 14 zero-class H_1 = Z members
    print("         CONTROL -- recomputing the zero-class H_1 = Z members and testing each")
    zero_members, quarter_members = [], []
    errs = 0
    for M in snappy.OrientableCuspedCensus(num_cusps=1):
        a = amphicheiral(M)
        if a is None:
            errs += 1
            continue
        if not a:
            continue
        if h1sig(M) != (1, ()):
            continue
        c = cs_class(M)
        if c is None:
            errs += 1
            continue
        if c == "zero":
            zero_members.append(str(M))
        elif c == "quarter":
            quarter_members.append(str(M))
    print(f"         amphicheiral + H_1 = Z:  zero class {len(zero_members)}, "
          f"quarter class {len(quarter_members)}, errors {errs}")
    print(f"         zero class:    {zero_members}")
    print(f"         quarter class: {quarter_members}")
    zk = {m: str(snappy.CensusKnots.identify(snappy.Manifold(m))) for m in zero_members}
    n_zero_knots = sum(1 for v in zk.values() if v != "False")
    for m, v in sorted(zk.items()):
        print(f"           {m:14s} -> {v}")
    print(f"         of the {len(zero_members)} zero-class members, {n_zero_knots} ARE knot "
          f"complements in S^3")
    print(f"         TARGET is a knot complement in S^3: {is_knot}")
    R["N2"] = {"completeness_sentence": bool(complete), "calibration": cal,
               "calibration_ok": bool(cal_ok), "target": TARGET,
               "target_censusknots": str(ck), "target_identify": ident,
               "target_is_S3_knot": bool(is_knot),
               "zero_members": zero_members, "quarter_members": quarter_members,
               "zero_member_knots": zk, "n_zero_knots": n_zero_knots, "errors": errs}
    if not cal_ok:
        print("         *** THE INSTRUMENT FAILED CALIBRATION.  N2 REPORTS NOTHING.")
        return False
    if is_knot:
        print("         *** THE KILL CONDITION FIRED.  The target IS an amphicheiral knot")
        print("         complement in S^3, so MO Cor 2.5 gives eta = 0 -- while its CS class is")
        print("         QUARTER.  THIS IS AN EXPLICIT WITNESS THAT THE CUSPED eta -> cs STEP FAILS.")
    else:
        print("         *** The target is NOT a knot complement in S^3 (decisive: it has 10")
        print("         tetrahedra and the tabulation is complete at 10).  MO Cor 2.5 NEVER")
        print("         APPLIED TO IT, so Addendum 1's refutation is of this seat's PROXY.")
    print("N2 PASS  (the cell ran and calibrated; its CONTENT is the verdict above)")
    return True


# ---------------------------------------------------------------- N3
def slopes_within(M, Lmax=6.0, rng=40):
    """Every primitive slope whose length on the maximal cusp is <= Lmax."""
    m_t, l_t = M.cusp_translations()[0]
    m = complex(m_t)
    l = complex(l_t)
    area = abs((m.conjugate() * l).imag)
    out = []
    for p in range(-rng, rng + 1):
        for q in range(-rng, rng + 1):
            if (p, q) == (0, 0) or math.gcd(abs(p), abs(q)) != 1:
                continue
            L = abs(p * m + q * l)
            if L <= Lmax:
                out.append((p, q, L))
    out.sort(key=lambda t: t[2])
    return out, area, abs(m), abs(l)


def s3_filling_search(name, Lmax=6.0):
    M = snappy.Manifold(name)
    sl, area, am, al = slopes_within(M, Lmax)
    found = []
    tested = 0
    for (p, q, L) in sl:
        M.dehn_fill((p, q))
        try:
            H = M.homology()
            triv_h1 = (H.betti_number() == 0 and
                       len([d for d in H.elementary_divisors() if d]) == 0)
        except Exception:
            triv_h1 = False
        if not triv_h1:
            continue
        tested += 1
        ng = None
        try:
            G = M.fundamental_group(simplify_presentation=True)
            ng = G.num_generators()
        except Exception:
            pass
        st = M.solution_type()
        vol = None
        try:
            vol = float(M.volume())
        except Exception:
            pass
        hyp = (st == "all tetrahedra positively oriented" and vol is not None and vol > 0.9)
        if ng == 0:
            found.append((p, q, L, "TRIVIAL pi_1 -> S^3 (Perelman)"))
        elif not hyp and ng is not None and ng > 0:
            found.append((p, q, L, f"non-hyperbolic, pi_1 has {ng} generators - undecided"))
        M.dehn_fill((0, 0))
    return {"slopes_le_Lmax": len(sl), "cusp_area": area, "merid_len": am, "long_len": al,
            "homology_sphere_slopes": tested, "hits": found}


def N3():
    print("\nN3       SECOND INSTRUMENT -- 6-theorem slope search for an S^3 filling")
    print("         Every slope of length > 6 on the maximal cusp fills hyperbolically")
    print("         (Agol, Lackenby), hence not to S^3.  So the search below is FINITE.")
    cal = s3_filling_search("m004")
    print(f"         CALIBRATION m004 = S^3 minus 4_1 -- it MUST find the S^3 filling")
    print(f"           cusp area {cal['cusp_area']:.6f}  |m| {cal['merid_len']:.6f}  "
          f"|l| {cal['long_len']:.6f}")
    print(f"           slopes of length <= 6: {cal['slopes_le_Lmax']}; of those with trivial H_1: "
          f"{cal['homology_sphere_slopes']}")
    for h in cal["hits"]:
        print(f"           HIT  ({h[0]},{h[1]})  len {h[2]:.4f}  {h[3]}")
    cal_ok = any("S^3" in h[3] for h in cal["hits"])
    print(f"         calibration passes (m004's S^3 filling found): {cal_ok}")

    tgt = s3_filling_search(TARGET)
    print(f"         TARGET {TARGET}")
    print(f"           cusp area {tgt['cusp_area']:.6f}  |m| {tgt['merid_len']:.6f}  "
          f"|l| {tgt['long_len']:.6f}")
    print(f"           slopes of length <= 6: {tgt['slopes_le_Lmax']}; of those with trivial H_1: "
          f"{tgt['homology_sphere_slopes']}")
    for h in tgt["hits"]:
        print(f"           HIT  ({h[0]},{h[1]})  len {h[2]:.4f}  {h[3]}")
    s3 = any("S^3" in h[3] for h in tgt["hits"])
    print(f"         an S^3 filling of {TARGET} was found: {s3}")
    R["N3"] = {"calibration_m004": cal, "target": tgt, "calibration_ok": bool(cal_ok),
               "target_has_S3_filling": bool(s3)}
    print("         FENCE, declared in the seal: SnapPy's cusp translations are UNVERIFIED")
    print("         floating point and the 6-theorem needs the MAXIMAL EMBEDDED cusp.  N3 is")
    print("         CORROBORATION BY A SECOND INSTRUMENT, NOT AN INDEPENDENT PROOF.")
    if not cal_ok:
        print("         *** N3 FAILED CALIBRATION.  It reports nothing about the target.")
        return False
    print("N3 PASS  (calibrated; its CONTENT is the verdict above)")
    return True


# ---------------------------------------------------------------- N4
def N4():
    print("\nN4       SECTION 3's PREDICTION, RE-RUN WITH THE REAL PREDICATE")
    print("         Addendum 1 used H_1 = Z (NECESSARY only).  Here: in CensusKnots (EXACT for")
    print("         this census).  Among AMPHICHEIRAL knot complements in S^3, how do CS classes")
    print("         split?")
    counts = {"zero": 0, "quarter": 0, "other": 0}
    members = {"zero": [], "quarter": [], "other": []}
    errs = 0
    n_amph = 0
    total = 0
    for M in snappy.CensusKnots():
        total += 1
        a = amphicheiral(M)
        if a is None:
            errs += 1
            continue
        if not a:
            continue
        n_amph += 1
        c = cs_class(M)
        if c is None:
            errs += 1
            continue
        counts[c] += 1
        if len(members[c]) < 40:
            members[c].append(str(M))
    print(f"         census knots scanned {total}; amphicheiral {n_amph}; errors {errs}")
    print(f"         CS class of the amphicheiral census knots: {counts}")
    for k in ("zero", "quarter", "other"):
        print(f"           {k:8s} {counts[k]:4d}  {members[k]}")
    underpowered = n_amph < 5
    holds = (counts["quarter"] == 0 and counts["other"] == 0 and not underpowered)
    R["N4"] = {"census_knots_scanned": total, "amphicheiral": n_amph, "errors": errs,
               "counts": counts, "members": members,
               "underpowered": bool(underpowered), "corrected_prediction_holds": bool(holds)}
    if underpowered:
        print("         *** UNDERPOWERED: fewer than 5 amphicheiral census knots.  Reported as")
        print("         such; this is NOT a confirmation.")
    elif counts["quarter"] or counts["other"]:
        print("         *** THE CORRECTED PREDICTION IS REFUTED TOO: an amphicheiral knot")
        print("         complement in S^3 sits off class zero.  That is the headline.")
    else:
        print("         *** THE CORRECTED PREDICTION HOLDS: every amphicheiral knot complement")
        print("         in S^3 in this census sits at CS class ZERO, none at quarter.")
        print("         FENCE: this is an EMPIRICAL REGULARITY OVER A FINITE CENSUS, not a")
        print("         theorem.  The eta -> cs step stays blocked by MO Prop 2.2's (1/3)Z slack.")
    print("N4 PASS  (the cell ran; its CONTENT is the verdict above)")
    return True


if __name__ == "__main__":
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    cells = {"N1": N1, "N2": N2, "N3": N3, "N4": N4}
    res = {}
    for k, f in cells.items():
        if only and k not in only:
            continue
        try:
            res[k] = bool(f())
        except Exception as e:
            print(f"{k} EXCEPTION {type(e).__name__}: {e}")
            res[k] = False
    print("\n" + "=" * 78)
    print("ALL CELLS RAN" if all(res.values()) else "NOT ALL CELLS PASSED")
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knot_or_not.json")
    prev = {}
    if os.path.exists(out):
        try:
            prev = json.load(open(out, encoding="utf-8"))
        except Exception:
            prev = {}
    prev.setdefault("cells", {}).update(res)
    prev.setdefault("results", {}).update(R)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(prev, fh, indent=1, default=str)
