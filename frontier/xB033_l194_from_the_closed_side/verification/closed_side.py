"""xB033 -- L194 from the closed side.  SEALED at 0721f678.

Y1  every CLOSED amphichiral hyperbolic 3-manifold has cs = 0 (mod 1/2).  NEGATIVE CONTROL binding.
Y2  the cusped contrast, re-measured.
"""
import json, os, re, sys, warnings
warnings.filterwarnings("ignore")
import snappy
from mpmath import mp
mp.dps = 30
TOL = mp.mpf(10) ** -7
R = {}
NAME_RE = re.compile(r"^([A-Za-z0-9_]+)\(([-0-9]+),([-0-9]+)\)$")


def to_mpf(x):
    """SnapPy returns its own Number type, not a float; keep every digit it offers."""
    if isinstance(x, mp.mpf):
        return x
    try:
        return mp.mpf(repr(x).replace(" ", ""))
    except Exception:
        return mp.mpf(float(x))


def fold_half(x):
    """reduce mod 1/2 and fold to [-1/4, 1/4]"""
    h = mp.mpf(1) / 2
    x = to_mpf(x)
    y = x - h * mp.floor(x / h)
    if y > mp.mpf(1) / 4:
        y -= h
    return y


def klass(x):
    y = fold_half(x)
    if abs(y) < TOL:
        return "zero"
    if abs(abs(y) - mp.mpf(1) / 4) < TOL:
        return "quarter"
    return "other"


def closed_cs(name):
    """cs of a closed census manifold: the invariant must be computed on the CUSPED parent first."""
    m = NAME_RE.match(name)
    if not m:
        return None, "unparsed name"
    base, p, q = m.group(1), int(m.group(2)), int(m.group(3))
    for ctor in (snappy.ManifoldHP, snappy.Manifold):      # HP first: closed cs at double precision
        try:                                                # is only ~10 digits, and the fold needs digits
            N = ctor(base)
            N.chern_simons()                                # makes CS known on the CUSPED parent
            N.dehn_fill((p, q))
            return N.chern_simons(), None
        except Exception as e:
            last = f"{type(e).__name__}"
    return None, last


N_CONTROL = 400


def Y1(limit=None):
    print("\nY1       CLOSED, AMPHICHIRAL -> cs = 0 (mod 1/2)?   THE QUARTER CLASS SHOULD BE EMPTY")
    amph, nona, errs = [], [], 0
    n = 0
    for M in snappy.OrientableClosedCensus():
        name = str(M)
        n += 1
        if limit and n > limit:
            break
        try:
            G = M.symmetry_group()
            is_a = bool(G.is_full_group() and G.is_amphicheiral())
        except Exception:
            errs += 1
            continue
        # cs for EVERY amphichiral member (the claim is about them); for the NEGATIVE CONTROL a
        # BOUNDED sample of non-amphichiral ones -- computing all ~11k costs hours and proves
        # nothing extra.  The bound is declared here and printed, not silent.
        if (not is_a) and len(nona) >= N_CONTROL:
            continue
        cs, err = closed_cs(name)
        if cs is None:
            errs += 1
            continue
        k = klass(cs)
        (amph if is_a else nona).append((name, float(cs), float(fold_half(cs)), k))
        if (len(amph) + len(nona)) % 100 == 0:
            print(f"           ... {n} scanned, amph {len(amph)}, control {len(nona)}", flush=True)
    def dist(rows):
        d = {}
        for r in rows:
            d[r[3]] = d.get(r[3], 0) + 1
        return d
    da, dn = dist(amph), dist(nona)
    print(f"         scanned {n} closed census manifolds; errors {errs}; non-amphichiral "
          f"CONTROL SAMPLE capped at N_CONTROL={N_CONTROL} (declared, not silent)")
    print(f"         AMPHICHIRAL     : {len(amph)}  class distribution {da}")
    print(f"         NON-amphichiral : {len(nona)}  class distribution {dn}")
    bad = [r for r in amph if r[3] != "zero"]
    print(f"         amphichiral members with cs != 0 (mod 1/2): {len(bad)}  {bad[:6]}")
    if amph[:6]:
        print(f"         first amphichiral rows (name, cs, folded, class):")
        for r in amph[:6]:
            print(f"           {r[0]:16s} cs={r[1]:+.10f}  folded={r[2]:+.10f}  {r[3]}")
    spread = len([k for k in dn if k != "zero"]) > 0 and dn.get("zero", 0) < len(nona)
    print(f"         NEGATIVE CONTROL -- non-amphichiral cs values SPREAD off zero: {spread}")
    under = len(amph) < 20
    print(f"         VACUITY CONTROL -- at least 20 amphichiral members: {not under} ({len(amph)})")
    R["Y1"] = {"scanned": n, "errors": errs, "n_amph": len(amph), "n_nonamph": len(nona),
               "amph_dist": da, "nonamph_dist": dn, "violations": bad[:20],
               "negative_control_spread": bool(spread), "underpowered": bool(under),
               "amph_sample": amph[:20]}
    if not spread:
        print("         *** NEGATIVE CONTROL FAILED: closed cs does not discriminate. The cell")
        print("         measures NOTHING and no conclusion may be drawn.")
        return False
    if under:
        print("         *** UNDERPOWERED: fewer than 20 amphichiral members. Reported as such.")
        return False
    if bad:
        print("         *** THE KILL FIRED: a closed amphichiral manifold sits off 0 (mod 1/2).")
        print("         One of (i) cs mod 1 for closed, (ii) the cusped modulus, (iii) cs(M*) = -cs(M)")
        print("         is WRONG -- most likely (iii), the declared weakest link.  THAT is the headline.")
    else:
        print("         *** THE PREDICTION HOLDS: every closed amphichiral member is at class ZERO,")
        print("         and the QUARTER CLASS IS EMPTY -- while the non-amphichiral ones spread.")
        print("         The derivation needed NO eta and NO APS: only the modulus and cs(M*) = -cs(M).")
    print(f"Y1 {'PASS' if (spread and not under) else 'FAIL'}  (content is the verdict above)")
    return spread and not under


def Y2():
    print("\nY2       THE CUSPED CONTRAST, re-measured (xB023 banked 106 zero / 75 quarter / 0 other)")
    def cs_class_cusped(M):
        try:
            s = repr(snappy.ManifoldHP(M.isometry_signature()).chern_simons()).replace(" ", "")
        except Exception:
            return None
        return klass(mp.mpf(s))
    d = {"zero": 0, "quarter": 0, "other": 0}
    errs = 0
    for M in snappy.OrientableCuspedCensus(num_cusps=1):
        try:
            G = M.symmetry_group()
            if not (G.is_full_group() and G.is_amphicheiral()):
                continue
        except Exception:
            errs += 1
            continue
        k = cs_class_cusped(M)
        if k is None:
            errs += 1
            continue
        d[k] += 1
    print(f"         amphichiral one-cusped: {d}; errors {errs}")
    print(f"         xB023 banked           : {{'zero': 106, 'quarter': 75, 'other': 0}}")
    ok = (d == {"zero": 106, "quarter": 75, "other": 0})
    print(f"         reproduces xB023 exactly: {ok}")
    print(f"         THE QUARTER CLASS IS NON-EMPTY IN THE CUSPED CASE: {d['quarter'] > 0}")
    R["Y2"] = {"cusped_dist": d, "errors": errs, "reproduces_xB023": bool(ok)}
    print(f"Y2 {'PASS' if ok else 'FAIL (does not reproduce)'}")
    return ok


if __name__ == "__main__":
    only = sys.argv[1:] or None
    res = {}
    for k, f in {"Y1": Y1, "Y2": Y2}.items():
        if only and k not in only:
            continue
        try:
            res[k] = bool(f())
        except Exception as e:
            import traceback; traceback.print_exc()
            res[k] = False
    print("\n" + "=" * 78)
    print("ALL CELLS PASSED" if all(res.values()) else "NOT ALL CELLS PASSED")
    json.dump({"cells": res, "results": R},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "closed_side.json"),
                   "w", encoding="utf-8"), indent=1, default=str)
