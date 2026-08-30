#!/usr/bin/env python3
"""B1186 independent enumeration -- the family-definition cell, own code.

Criteria over the full orientable cusped census:
  (A) all tetrahedra regular ideal: every shape z = e^{i pi/3} = 1/2 + (sqrt3/2) i
  (B) every shape in Q(sqrt-3):     Re(z), Im(z)/sqrt3 both rational (bounded den)
Double-precision pass with tolerance, then a high-precision re-verify of every
candidate (and near-miss controls). Also: cusp shapes 2sqrt3 i, amphichirality
of every B-member, and the quine-filter check (volume/cusp-count of carriers).
"""
import json, sys, time
from fractions import Fraction

import snappy

SQ3 = 3.0 ** 0.5
TOL = 1e-9
MAXDEN = 256          # scan bound: observed member denominators are <= 14; 1/(2*256^2) >> TOL keeps false positives rare

def near_rational(x, maxden=MAXDEN, tol=TOL):
    f = Fraction(x).limit_denominator(maxden)
    return abs(float(f) - x) < tol

def shapes_ok(M):
    """(passes_B, all_regular) at double precision."""
    try:
        shapes = M.tetrahedra_shapes('rect')
    except Exception:
        return False, False
    reg = True
    for z in shapes:
        z = complex(z)
        if not (near_rational(z.real) and near_rational(z.imag / SQ3)):
            return False, False
        if abs(z - complex(0.5, SQ3 / 2)) > 1e-9:
            reg = False
    return True, reg

def hp_confirm(name):
    """Genuine high-precision re-verify (212-bit shapes via mpmath, NOT double casts).

    The first implementation cast the 212-bit shapes to double and demanded 1e-25
    agreement -- impossible except by mantissa cancellation; it wrongly rejected
    o9_41001 (denominator-7 shapes). Caught in-cell by chasing the disagreement.
    """
    import mpmath as mp
    mp.mp.dps = 60
    sq3 = mp.sqrt(3)
    M = snappy.Manifold(name).high_precision()
    reg = True
    for z in M.tetrahedra_shapes('rect'):
        re = mp.mpf(str(z.real()).replace(' ', '')); im = mp.mpf(str(z.imag()).replace(' ', ''))
        fr = Fraction(float(re)).limit_denominator(MAXDEN)
        fi = Fraction(float(im / sq3)).limit_denominator(MAXDEN)
        if abs(mp.mpf(fr.numerator) / fr.denominator - re) > mp.mpf(10) ** -45:
            return False, False
        if abs(mp.mpf(fi.numerator) / fi.denominator - im / sq3) > mp.mpf(10) ** -45:
            return False, False
        if not (fr == Fraction(1, 2) and fi == Fraction(1, 2)):
            reg = False
    return True, reg

def main():
    census = snappy.OrientableCuspedCensus
    total = len(census)
    print(f"census size = {total}", flush=True)
    cand = []
    t0 = time.time()
    for i, M in enumerate(census):
        if i % 20000 == 0:
            print(f"  scan {i}/{total}  ({time.time()-t0:.0f}s)", flush=True)
        b, reg = shapes_ok(M)
        if b:
            cand.append((M.name(), reg))
    print(f"double-precision candidates: {len(cand)}  ({time.time()-t0:.0f}s)", flush=True)

    members, regs = [], []
    for name, _ in cand:
        b, reg = hp_confirm(name)
        if b:
            members.append(name)
            if reg:
                regs.append(name)
    print(f"HIGH-PRECISION: |B| = {len(members)}, |A| = {len(regs)}, "
          f"in B not A = {len(members)-len(regs)}, in A not B = 0 (A recomputed inside B)", flush=True)

    carriers, amph_fail, quine = [], [], []
    for name in members:
        M = snappy.Manifold(name)
        nc = M.num_cusps()
        shs = [complex(ci['shape']) for ci in M.cusp_info()]
        if any(abs(s - complex(0, 2*SQ3)) < 1e-6 for s in shs):
            carriers.append(name)
        W = snappy.Manifold(name); W.reverse_orientation()
        try:
            ok = M.is_isometric_to(W)
        except RuntimeError:
            ok = M.high_precision().is_isometric_to(W.high_precision())
        if not ok:
            amph_fail.append(name)
        if name != 'm004':
            one_cusped = (nc == 1)
            vol_match = abs(float(M.volume()) - 2.029883212819) < 1e-6
            shape_match = any(abs(s - complex(0, 2*SQ3)) < 1e-6 for s in shs)
            if one_cusped and vol_match and shape_match:
                quine.append(name)

    out = {
        "census": "snappy.OrientableCuspedCensus", "census_size": total,
        "B_shape_field_in_Qsqrt3": len(members), "A_all_regular": len(regs),
        "in_B_not_A": len(members) - len(regs),
        "members_B": members, "members_A": regs,
        "carriers_2sqrt3i_excl_m004": sorted(n for n in carriers if n != 'm004'),
        "amphichirality_failures": amph_fail,
        "quine_collisions": quine,
        "known_member_control": {n: (n in members) for n in
            ["m004","s955","t12840","o9_41001","o9_41009",
             "o10_150684","o10_150685","o10_150693","o10_150700"]},
    }
    with open(sys.argv[1] if len(sys.argv) > 1 else "b1186_family_census.json", "w") as f:
        json.dump(out, f, indent=1)
    print("carriers 2sqrt3i (excl m004):", out["carriers_2sqrt3i_excl_m004"], flush=True)
    print("amphichirality failures:", amph_fail, flush=True)
    print("quine collisions (1-cusped + vol + shape):", quine, flush=True)
    print("DONE", flush=True)

if __name__ == "__main__":
    main()
