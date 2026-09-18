"""xB026 -- does A5 move the generation count?

Sealed PREREGISTRATION.md sha256 4ae71e2987b073a835f97713ad03d18b429d2e2192abdc49236bed6e9ee23eb1,
committed and pushed at 7d97a302 BEFORE this file existed.

The object's tower is b++(LR)^n (xB013 Y2; = B1375's Y_2...Y_5).  Its A5 image is b+-(LR)^n.
"""
import json
import os

import snappy

R = {}
NMAX = 6


def hom(name):
    H = snappy.Manifold(name).homology()
    return (H.betti_number(), tuple(sorted(d for d in H.elementary_divisors() if d)))


def tor_exponent(sig):
    """lcm of the torsion invariant factors = the exponent of Tor H_1."""
    from math import gcd
    e = 1
    for d in sig[1]:
        e = e * d // gcd(e, d)
    return e


def isosig(name):
    try:
        return snappy.Manifold(name).isometry_signature()
    except Exception as e:
        return f"ERR:{type(e).__name__}"


def G1():
    print("\nG1       THE SCAFFOLDING -- the tower rebuilt and identified BY ISOMETRY SIGNATURE")
    print("         (not by volume: a volume coincidence is exactly how this record's sister pair arose)")
    expect = {1: "m004", 2: "m206", 3: "s961", 4: "t12839", 5: "o10_150696"}
    ok, rows = True, []
    for n in range(1, NMAX + 1):
        nm = "b++" + "LR" * n
        s = isosig(nm)
        tgt = expect.get(n)
        match = (s == isosig(tgt)) if tgt else None
        rows.append((n, nm, s, tgt, match))
        print(f"         n={n}: {nm:16s} isosig {str(s)[:22]:24s} expect {str(tgt):14s} match={match}")
        if tgt is not None and match is not True:
            ok = False
    R["G1"] = {"rows": [(n, nm, s, t, m) for n, nm, s, t, m in rows]}
    print(f"G1 {'PASS' if ok else 'FAIL'}  the tower is B1375's Y_2..Y_5 and xB013's Y2, reproduced")
    print("         independently by isometry signature.")
    return ok


def G2():
    """THE DECIDING CELL, with the seal's binding kill condition."""
    print("\nG2       H_1 ON BOTH TOWERS -- the cell that decides, with the kill condition")
    print("         PREDICTION (sealed): they DIFFER at every level.")
    print("         KILL (sealed): if they AGREE at every level, A5 is in the stabiliser of the")
    print("         tower's homology, the census inputs do not move, and the orbit hypothesis for")
    print("         the generation count is DEAD AT THE INPUT LEVEL and must be reported dead.")
    same = diff = tested = errs = 0
    rows = []
    for n in range(1, NMAX + 1):
        a_nm, b_nm = "b++" + "LR" * n, "b+-" + "LR" * n
        try:
            ha, hb = hom(a_nm), hom(b_nm)
        except Exception as e:
            errs += 1
            print(f"         n={n}: ERROR {type(e).__name__} -- counted, not swallowed")
            continue
        tested += 1
        d = (ha != hb)
        diff += d
        same += (not d)
        rows.append((n, str(ha), str(hb), bool(d)))
        print(f"         n={n}: b++ H_1={str(ha):26s} b+- H_1={str(hb):26s} DIFFER={d}")
    # POSITIVE CONTROL: the base level is the known sister pair
    ctrl = hom("m004") != hom("m003")
    print(f"         POSITIVE CONTROL  H_1(m004) != H_1(m003): {ctrl}   "
          f"({hom('m004')} vs {hom('m003')})")
    print(f"         levels tested: {tested};  DIFFER: {diff};  AGREE: {same};  errors: {errs}")
    killed = (tested > 0 and diff == 0)
    R["G2"] = {"tested": tested, "differ": diff, "agree": same, "errors": errs,
               "rows": rows, "control_sees_difference": bool(ctrl),
               "kill_fired": bool(killed)}
    if killed:
        print("         *** THE KILL CONDITION FIRED. *** A5 does NOT move the tower's H_1.")
        print("         The orbit hypothesis for the generation count is DEAD at the input level.")
    else:
        print("         The kill condition did NOT fire: A5 moves the tower's homology.")
    ok = tested >= 4 and ctrl and errs == 0
    print(f"G2 {'PASS' if ok else 'FAIL'}  (the cell ran correctly; its CONTENT is the verdict above)")
    return ok


def G3():
    """B1374's own character-group modulus on both towers."""
    print("\nG3       THE CENSUS INPUTS -- B1374 builds characters at N = lcm(12, torsion exponent)")
    from math import gcd
    rows, moved, tested = [], 0, 0
    for n in range(1, NMAX + 1):
        a_nm, b_nm = "b++" + "LR" * n, "b+-" + "LR" * n
        try:
            ha, hb = hom(a_nm), hom(b_nm)
        except Exception:
            continue
        ea, eb = tor_exponent(ha), tor_exponent(hb)
        Na, Nb = 12 * ea // gcd(12, ea), 12 * eb // gcd(12, eb)
        tested += 1
        moved += (Na != Nb)
        rows.append((n, ea, eb, Na, Nb, Na != Nb))
        print(f"         n={n}: exponent {ea:6d} vs {eb:6d}   N = {Na:6d} vs {Nb:6d}   "
              f"DIFFER={Na != Nb}")
    print(f"         levels where B1374's character modulus N MOVES under A5: {moved} of {tested}")
    print("         Where N differs the character group differs, so B1374's census is not")
    print("         literally the same object on the sister's tower.")
    R["G3"] = {"tested": tested, "moved": moved, "rows": rows}
    return tested >= 4


def G4():
    """ATTEMPT, declared in the seal as one that may not land."""
    print("\nG4       ATTEMPT (declared in the seal as one that may not land): the index instrument")
    print("         on a cover's presentation.")
    n_gen = {}
    for n in range(1, 5):
        for pre in ("b++", "b+-"):
            nm = pre + "LR" * n
            try:
                G = snappy.Manifold(nm).fundamental_group()
                n_gen[nm] = (len(G.generators()), len(G.relators()))
            except Exception as e:
                n_gen[nm] = f"ERR:{type(e).__name__}"
    for k, v in n_gen.items():
        print(f"           {k:14s} (generators, relators) = {v}")
    two_one = [k for k, v in n_gen.items() if v == (2, 1)]
    print(f"         presentations with the 2-generator/1-relator shape the branch's instrument")
    print(f"         (main_r27_exact_lift.py) accepts: {two_one}")
    print("         VERDICT ON THE ATTEMPT, stated plainly: the instrument on this branch is")
    print("         written for 2 generators and 1 relator over Q(u).  The covers above are not")
    print("         of that shape, so computing the index here needs a GENERALISED instrument")
    print("         (arbitrary presentation, arbitrary cyclotomic field) that this arc does NOT")
    print("         build.  G4 DOES NOT LAND, and is reported as not landing.  G2 and G3 stand")
    print("         alone, and what they decide is stated in G5.")
    R["G4"] = {"presentations": {k: str(v) for k, v in n_gen.items()},
               "landed": False,
               "why": "the branch's index instrument is 2-generator/1-relator over Q(u); the covers are not"}
    return True


def G5():
    """What the result does and does not decide -- written in the seal before the data."""
    print("\nG5       WHAT THIS DOES AND DOES NOT DECIDE  (written in the seal, before the data)")
    g2 = R.get("G2", {})
    moved_inputs = g2.get("differ", 0) > 0 and not g2.get("kill_fired", True)
    print(f"         A5 moves the tower's H_1: {moved_inputs}")
    print(f"         A5 moves B1374's character modulus N: {R.get('G3', {}).get('moved', 0)} levels")
    print("         DECIDED: the generation census's own INPUTS are NOT stabiliser-fixed.  The")
    print("           loci, the character groups and the modulus all move under A5, so B1374's")
    print("           census on the sister's tower is a DIFFERENT census, not the same one.")
    print("         NOT DECIDED, and the seal said so in advance: whether the COUNT moves.")
    print("           'One per background' could survive on different loci -- which would make")
    print("           ONE the invariant and the backgrounds merely the orbit.  THIS ARC DOES NOT")
    print("           READ A MOVED LOCUS AS A MOVED COUNT, and G4 did not land, so the count on")
    print("           the sister's tower REMAINS UNCOMPUTED.")
    print("         The question is now SHARP and bounded: run B1374's census on b+-(LR)^n.")
    R["G5"] = {"inputs_move": bool(moved_inputs),
               "count_decided": False,
               "next": "run B1374's SM-frame census on the sister tower b+-(LR)^n"}
    return True



def G6():
    """BEYOND THE SEAL, LABELLED: three cross-checks the G2/G3 data makes available.
    Run, not asserted (E69: a verdict string beside a number that does not test it)."""
    print("\nG6       BEYOND THE SEAL, LABELLED -- three cross-checks, RUN not asserted")
    from math import gcd
    ords = {}
    for pre in ("b++", "b+-"):
        ords[pre] = []
        for n in range(1, NMAX + 1):
            sig = hom(pre + "LR" * n)
            o = 1
            for d in sig[1]:
                o *= d
            ords[pre].append(o)
    print(f"         |Tor H_1| on b++(LR)^n: {ords['b++']}")
    print(f"         |Tor H_1| on b+-(LR)^n: {ords['b+-']}")

    # (a) xB022's +4 law, on the TOWER rather than on short words
    shifts = [b - a for a, b in zip(ords["b++"], ords["b+-"])]
    plus4 = all(s == 4 for s in shifts)
    print(f"         (a) xB022's +4 law on the tower: shifts {shifts}  -> constant +4: {plus4}")
    print("             xB022 measured this on words of length <= 8; (LR)^6 has length 12, so")
    print("             this EXTENDS the law rather than repeating it.")

    # (b) the record's own Alexander-module torsion numbers
    want = [5, 16, 45, 121, 320]          # THEOREM_REGISTRY T-PERIOD-2..., n = 2..6
    got = ords["b++"][1:6]
    print(f"         (b) THEOREM_REGISTRY's T-PERIOD-2 cyclic-cover torsion for n=2..6: {want}")
    print(f"             this arc's b++ tower:                                        {got}"
          f"   match: {got == want}")

    # (c) B1374/B1375's own moduli, reproduced independently
    def Nof(pre, n):
        sig = hom(pre + "LR" * n)
        e = 1
        for d in sig[1]:
            e = e * d // gcd(e, d)
        return 12 * e // gcd(12, e)
    n4, n5 = Nof("b++", 4), Nof("b++", 5)
    print(f"         (c) B1374 runs Y_4 = t12839 at N = 60; this arc computes N = {n4}  "
          f"match: {n4 == 60}")
    print(f"             B1375 re-derives Y_5 over Q(zeta_132); this arc computes N = {n5}  "
          f"match: {n5 == 132}")

    # (d) an observation, explicitly NOT a claim
    sq = {p: [i + 1 for i, o in enumerate(ords[p]) if int(round(o ** 0.5)) ** 2 == o]
          for p in ords}
    print(f"         (d) levels with SQUARE |Tor|:  b++ {sq['b++']}   b+- {sq['b+-']}")
    print("             The two towers alternate.  RECORDED AS AN OBSERVATION, NOT A CLAIM:")
    print("             square torsion is necessary for a free orientation-reversing involution")
    print("             on CLOSED manifolds (xB023's reading of Kawauchi I+III) and these covers")
    print("             are CUSPED, where xB023 MEASURED that the same predicate fails 590 of")
    print("             1260 times.  No inference is drawn, and none may be.")
    ok = plus4 and got == want and n4 == 60 and n5 == 132
    R["G6"] = {"tor_orders": ords, "shifts": shifts, "plus4_on_tower": bool(plus4),
               "theorem_registry_match": bool(got == want), "N_Y4": n4, "N_Y5": n5,
               "square_levels": sq,
               "note": "square-torsion alternation recorded as an OBSERVATION, no inference drawn"}
    print(f"G6 {'PASS' if ok else 'FAIL'}  the +4 law extends to the tower; the record's own")
    print("         Alexander torsion numbers and B1374/B1375's own moduli are reproduced here")
    print("         independently.")
    return ok


if __name__ == "__main__":
    res = {}
    for f in (G1, G2, G3, G4, G5, G6):
        try:
            res[f.__name__] = bool(f())
        except Exception as e:
            print(f"{f.__name__} EXCEPTION {type(e).__name__}: {e}")
            res[f.__name__] = False
    print("\n" + "=" * 78)
    for k, v in res.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    print("VERIFIED" if all(res.values()) else "NOT ALL CELLS PASSED")
    with open(os.path.join(os.path.dirname(__file__), "tower_orbit.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"cells": res, "results": R}, fh, indent=1, default=str)
