"""xB029 ADDENDUM 1 -- Friedmann-Witten read at source.  SEALED at b812b698.

F2  does T_O = -log|Tor H_1| hold independently of pi_1?  (FW's own chain-level recipe)
F3  *** SUPERSEDED AND DEFECTIVE -- DO NOT READ ITS OUTPUT AS A RESULT. ***
    It scored n = 5 and n = 7 as CLEAN when their |H_1| are 11^2 and 841 = 29^2, so their ONLY
    cyclic-cover degrees are 11 and 29 -- both ABOVE its search bound of 8.  Those rows were
    UNMEASURED, not negative, and max(..., default=0) printed a zero for them.  The two members
    carrying the SHARPEST zero modes are exactly the two it scored clean.
    THE LIVE CELL IS fw_f3.py.  This one is kept only so the defect stays on the record.
"""
import json, math, os, random, sys, warnings
warnings.filterwarnings("ignore")
R = {}


def smith_divisors(A):
    """Elementary divisors of coker(A) for a square integer matrix, via sympy SNF."""
    from sympy import Matrix
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(Matrix(A))
    return [abs(int(S[i, i])) for i in range(min(S.shape))]


def F2():
    print("\nF2       WHAT SURVIVES -- is T_O = -log|Tor H_1| independent of pi_1?")
    print("         FW Appendix A's recipe is CHAIN-LEVEL ALGEBRA: remove the free homology,")
    print("         alternating sum of logs of the boundary maps.  For a rational homology")
    print("         3-sphere what survives is Z^m --d--> Z^m with det d != 0 and H_1 = coker d.")
    from sympy import Matrix
    # CALIBRATION: FW's own lens case, m = 1, d = (q)
    cal = []
    for q in (2, 3, 5, 7, 99, 316):
        d = [[q]]
        dv = smith_divisors(d)
        prod = 1
        for x in dv:
            prod *= x
        T_O = -math.log(abs(Matrix(d).det()))
        cal.append((q, int(Matrix(d).det()), prod, T_O, abs(T_O + math.log(q)) < 1e-12))
        print(f"         CAL  q={q:4d}  det={int(Matrix(d).det()):4d}  |coker|={prod:4d}  "
              f"T_O={T_O:9.5f}   equals FW's -log q: {cal[-1][4]}")
    cal_ok = all(c[4] for c in cal)
    print(f"         calibration reproduces FW's T_O(S^3/Z_q) = log(1/q): {cal_ok}")

    # the general claim, on random square integer boundary maps
    random.seed(20260918)
    bad = []
    n_ok = 0
    for trial in range(400):
        m = random.randint(1, 6)
        while True:
            A = [[random.randint(-6, 6) for _ in range(m)] for _ in range(m)]
            det = int(Matrix(A).det())
            if det != 0:
                break
        dv = smith_divisors(A)
        prod = 1
        for x in dv:
            prod *= x
        if prod != abs(det):
            bad.append((m, A, det, dv))
        else:
            n_ok += 1
    print(f"         random square boundary maps, m = 1..6: |det d| = |coker d| on "
          f"{n_ok} of 400; mismatches {len(bad)}")
    print(f"         => T_O = -log|det d| = -log|Tor H_1(Q)| for EVERY rational homology")
    print(f"            3-sphere.  NOTHING IN THIS ARGUMENT MENTIONS pi_1.")

    # and against the record's own closed tower members
    import snappy
    def lucas(k):
        a, b = 2, 1
        for _ in range(k):
            a, b = b, a + b
        return a
    tower = []
    for n in range(2, 13):
        pred = lucas(2 * n) - 2
        tower.append((n, pred, -math.log(pred)))
    print("         T_O for the record's closed tower members (from |Tor H_1| = L_2n - 2):")
    print("           " + "  ".join(f"n={n}:{t:.3f}" for n, _, t in tower[:6]) + " ...")
    ok = cal_ok and not bad
    R["F2"] = {"calibration": cal, "calibration_ok": bool(cal_ok),
               "random_trials": 400, "random_ok": n_ok, "mismatches": len(bad),
               "tower_T_O": tower, "pi1_mentioned_in_argument": False}
    print(f"F2 {'PASS' if ok else 'FAIL'}")
    return ok


def F3():
    print("\nF3       *** SUPERSEDED AND DEFECTIVE -- see this file's docstring and fw_f3.py.")
    print("         It scores n=5 and n=7 CLEAN although their only cover degrees (11, 29) are")
    print("         ABOVE its search bound of 8.  Those rows are UNMEASURED, not negative.")
    print("         KEPT ONLY SO THE DEFECT STAYS ON THE RECORD.  Do not read what follows as a result.")
    print("\nF3       DOES THE FINITE-pi_1 HYPOTHESIS BITE?  b1 > 0 in a cyclic cover IS a zero mode.")
    print("         FENCE, sealed: this tests ONLY ABELIAN characters.  FW's statement covers")
    print("         EVERY non-trivial irreducible rep, so a pass here is STRICTLY WEAKER.")
    import snappy

    def b1_of_cyclic_covers(M, maxdeg, label):
        out = []
        for d in range(2, maxdeg + 1):
            try:
                cv = M.covers(d, cover_type="cyclic")
            except Exception as e:
                out.append((d, f"err {type(e).__name__}")); continue
            if not cv:
                continue
            bs = []
            for c in cv:
                bs.append(c.homology().betti_number())
            out.append((d, len(cv), max(bs)))
        return out

    # CALIBRATION: a lens space -- FINITE pi_1, must give b1 = 0 throughout
    print("         CALIBRATION (finite pi_1): the lens space L(5,2) = 2-fold branched cover of 4_1")
    L = snappy.Manifold("m003")      # placeholder replaced below
    lens = snappy.Manifold("L(5,2)") if "L(5,2)" in dir(snappy) else None
    # build the lens space as a filling of the solid torus is not available; use the
    # branched cover construction that G3b calibrated instead
    K = snappy.Manifold("4_1")
    X2 = K.covers(2, cover_type="cyclic")[0]
    X2.dehn_fill((1, 0))
    print(f"           Sigma_2: H_1 = {X2.homology()}  (must be Z/5)")
    calrows = b1_of_cyclic_covers(X2, 6, "Sigma_2")
    print(f"           cyclic covers, (degree, #covers, max b1): {calrows}")
    cal_ok = all((len(r) == 3 and r[2] == 0) for r in calrows if len(r) == 3)
    print(f"         calibration: finite-pi_1 example has b1 = 0 throughout: {cal_ok}")

    # the hyperbolic closed tower members
    print("         THE HYPERBOLIC MEMBERS (infinite pi_1), closed, b1 = 0, |H_1| = L_2n - 2:")
    def lucas(k):
        a, b = 2, 1
        for _ in range(k):
            a, b = b, a + b
        return a
    rows = []
    for n in range(3, 8):
        X = K.covers(n, cover_type="cyclic")[0]
        # pick the closing slope G3b found, preferring a hyperbolic one
        chosen = None
        for (p, q) in [(0, 1), (1, 1), (1, -1), (2, 1), (1, 0)]:
            X.dehn_fill((p, q))
            H = X.homology()
            tor = 1
            for dd in H.elementary_divisors():
                if dd:
                    tor *= dd
            if H.betti_number() == 0 and tor == lucas(2 * n) - 2:
                try:
                    if X.solution_type().startswith("all tetrahedra"):
                        chosen = (p, q, tor, float(X.volume())); break
                except Exception:
                    pass
                if chosen is None:
                    chosen = (p, q, tor, None)
        if chosen is None:
            rows.append((n, "no closing slope in the shortlist")); continue
        X.dehn_fill((chosen[0], chosen[1]))
        cov = b1_of_cyclic_covers(X, 8, f"Sigma_{n}")
        maxb = max([r[2] for r in cov if len(r) == 3], default=0)
        rows.append((n, chosen, cov, maxb))
        print(f"           n={n}: slope {chosen[:2]}  |H_1|={chosen[2]}  vol="
              f"{round(chosen[3],5) if chosen[3] else 'non-hyp'}  covers {cov}  max b1={maxb}")
    anyb = [r for r in rows if len(r) == 4 and r[3] > 0]
    print(f"         cyclic covers with b1 > 0 (a ZERO MODE): {len(anyb)}")
    R["F3"] = {"calibration": calrows, "calibration_ok": bool(cal_ok),
               "rows": [list(map(str, r)) for r in rows],
               "members_with_zero_modes": len(anyb),
               "fence": "abelian characters only; FW's statement covers all irreducible reps"}
    if not cal_ok:
        print("         *** CALIBRATION FAILED.  F3 reports nothing.")
        return False
    if anyb:
        print("         *** THE KILL CONDITION FIRED: zero modes are REAL on the hyperbolic side.")
        print("         FW's simple torsion formula needs the K_i correction there, and L225 DIES.")
    else:
        print("         *** b1 = 0 throughout.  THE CONCLUSION SURVIVES WHERE THE HYPOTHESIS")
        print("         DOES NOT -- for ABELIAN characters only, which is STRICTLY WEAKER than")
        print("         FW's statement.  This is NOT 'the hypothesis was unnecessary'.")
    print("F3 PASS  (the cell ran and calibrated; its CONTENT is the verdict above)")
    return True


if __name__ == "__main__":
    only = sys.argv[1:] or None
    res = {}
    for k, f in {"F2": F2, "F3": F3}.items():
        if only and k not in only:
            continue
        try:
            res[k] = bool(f())
        except Exception as e:
            print(f"{k} EXCEPTION {type(e).__name__}: {e}")
            res[k] = False
    print("\n" + "=" * 78)
    print("ALL CELLS RAN" if all(res.values()) else "NOT ALL CELLS PASSED")
    json.dump({"cells": res, "results": R},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fw_read.json"),
                   "w", encoding="utf-8"), indent=1, default=str)
