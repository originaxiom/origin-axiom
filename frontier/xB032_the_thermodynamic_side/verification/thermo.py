"""xB032 -- the thermodynamic side.  SEALED at 988ca30d.

T1  the sixth name: log alpha IS the topological entropy of m004's monodromy
T2  the extremality, joined: the dilatation column IS the torsion-growth column
"""
import json, math, os, sys, warnings
warnings.filterwarnings("ignore")
import sympy as sp

R = {}


def word_matrix(w):
    Rm = sp.Matrix([[1, 1], [0, 1]])
    Lm = sp.Matrix([[1, 0], [1, 1]])
    M = sp.eye(2)
    for ch in w:
        M = M * (Rm if ch == 'R' else Lm)
    return M


def T1():
    print("\nT1       THE SIXTH NAME -- and it is thermodynamic")
    t = sp.symbols('t')
    phi = (1 + sp.sqrt(5)) / 2
    alpha = (3 + sp.sqrt(5)) / 2
    M = word_matrix('RL')
    print(f"         m004 = the once-punctured-torus bundle with monodromy RL")
    print(f"         RL = [[1,1],[0,1]]*[[1,0],[1,1]] = {M.tolist()}   trace = {M.trace()}  "
          f"det = {M.det()}")
    cp = sp.expand(M.charpoly(t).as_expr())
    alex = t**2 - 3*t + 1
    e1 = sp.simplify(cp - alex) == 0
    print(f"         characteristic polynomial = {cp}")
    print(f"         Alexander polynomial of 4_1 = {alex}    IDENTICAL: {e1}")
    ev = sorted([sp.nsimplify(sp.radsimp(v)) for v in M.eigenvals()], key=lambda v: -float(v))
    lam = ev[0]
    e2 = sp.simplify(lam - alpha) == 0
    e3 = sp.simplify(alpha - phi**2) == 0
    print(f"         eigenvalues {ev}; spectral radius = dilatation lambda = {sp.radsimp(lam)}")
    print(f"         lambda == alpha = (3+sqrt5)/2 : {e2}      alpha == phi^2 : {e3}")
    h = float(sp.log(lam))
    print(f"         topological entropy of the monodromy h_top = log lambda = {h:.10f}")
    print(f"                                                   = 2 log phi  = {float(2*sp.log(phi)):.10f}")

    # THE CONSEQUENCE: xB029's MEASURED growth constant, re-read, not recalled
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "xB029_the_g2_mssm_read", "verification", "g2_mssm.json")
    meas = None
    try:
        meas = json.load(open(p, encoding="utf-8"))["results"]["G3"]["measured_growth_per_degree"]
    except Exception as e:
        print(f"         COULD NOT re-read xB029's artefact: {type(e).__name__}")
    e4 = meas is not None and abs(meas - h) < 1e-9
    print(f"         xB029's MEASURED torsion growth per level (re-read) = {meas}")
    print(f"         equals h_top to 1e-9 : {e4}")
    ok = bool(e1 and e2 and e3 and e4)
    R["T1"] = {"RL": M.tolist(), "trace": int(M.trace()), "charpoly": str(cp),
               "charpoly_is_alexander": bool(e1), "dilatation": str(sp.radsimp(lam)),
               "lambda_is_alpha": bool(e2), "alpha_is_phi2": bool(e3),
               "h_top": h, "xB029_measured": meas, "growth_is_entropy": bool(e4)}
    if ok:
        print("         *** THE JOIN:  log|Tor H_1(X_n)| = n * h_top(monodromy) + o(1).")
        print("         The tower's torsion IS an ENTROPY, growing at exactly the entropy rate of")
        print("         the object's own monodromy.  So Friedmann-Witten's T_O term,")
        print("         P_eff = log|Tor H_1|, is on this tower  n * h_top.")
        print("         FENCE: for a FIBRED knot the Alexander polynomial IS the characteristic")
        print("         polynomial of the monodromy -- CLASSICAL.  The content is that three arcs")
        print("         carried the same number without the join, not that the number is new.")
    print(f"T1 {'PASS' if ok else 'FAIL'}")
    return ok


def T2(NMAX=60):
    print("\nT2       THE EXTREMALITY, JOINED -- is the dilatation column the torsion column?")
    print("         CONTROL, binding: the identity must be tested where lambda is NOT phi^2.")
    print("         At least four distinct dilatations required.")
    import snappy
    words = ["RL", "RRL", "RLL", "RRLL", "RLRRL", "RRRL", "RLRL", "RRLRL"]
    rows = []
    for w in words:
        Mw = word_matrix(w)
        tr = int(Mw.trace())
        if abs(tr) <= 2:
            rows.append((w, tr, None, None, None, "not pseudo-Anosov (|trace| <= 2)")); continue
        lam = max(abs(complex(v)) for v in Mw.eigenvals())
        h = math.log(lam)
        name = "b++" + w
        try:
            Mf = snappy.Manifold(name)
            vol = float(Mf.volume())
        except Exception as e:
            rows.append((w, tr, lam, h, None, f"snappy err {type(e).__name__}")); continue
        # measured torsion growth on the cyclic tower of THIS bundle: b++ (w)^n
        best = None
        for n in (30, 40, 50, 60):
            if n > NMAX:
                break
            try:
                H = snappy.Manifold("b++" + w * n).homology()
                tor = 1
                for d in H.elementary_divisors():
                    if d:
                        tor *= d
                if tor > 1:
                    best = (n, math.log(tor) / n)
            except Exception:
                break
        rows.append((w, tr, lam, h, vol, best))
    print(f"         {'word':8s} {'trace':>5s} {'dilatation':>12s} {'h=log lam':>11s} "
          f"{'volume':>10s}  measured log|Tor|/n")
    agree, tested = [], []
    for r in rows:
        w, tr, lam, h, vol, best = r
        if isinstance(best, tuple):
            n, g = best
            ok = abs(g - h) < 1e-6
            agree.append(ok); tested.append(round(h, 6))
            print(f"         {w:8s} {tr:5d} {lam:12.8f} {h:11.8f} {vol:10.6f}  "
                  f"n={n}: {g:.10f}   match {ok}")
        else:
            print(f"         {w:8s} {tr:5d} {'-' if lam is None else f'{lam:12.8f}'} "
                  f"{'-' if h is None else f'{h:11.8f}'} "
                  f"{'-' if vol is None else f'{vol:10.6f}'}  {best}")
    distinct = len(set(tested))
    print(f"         distinct dilatations tested: {distinct}  (>= 4 required by the control)")
    print(f"         the two columns agree on {sum(agree)} of {len(agree)}")
    mins = [r for r in rows if isinstance(r[5], tuple)]
    if mins:
        hmin = min(r[3] for r in mins); vmin = min(r[4] for r in mins)
        w_h = [r[0] for r in mins if r[3] == hmin]; w_v = [r[0] for r in mins if r[4] == vmin]
        print(f"         minimum entropy at {w_h}; minimum volume at {w_v}")
    ok = distinct >= 4 and all(agree) and len(agree) >= 4
    R["T2"] = {"rows": [[str(x) for x in r] for r in rows], "agree": sum(agree),
               "tested": len(agree), "distinct_dilatations": distinct,
               "control_satisfied": bool(distinct >= 4)}
    if not (distinct >= 4):
        print("         *** CONTROL FAILED: fewer than four distinct dilatations. The identity is")
        print("         NOT established -- agreement at one value is not evidence of an identity.")
    elif all(agree):
        print("         *** THE DILATATION COLUMN AND THE TORSION-GROWTH COLUMN ARE THE SAME")
        print("         COLUMN, at four or more distinct values.  xB014's 'extremal three ways'")
        print("         therefore says something it did not say: the object is the SLOWEST")
        print("         TORSION PRODUCER in its class -- it minimises the entropy.")
        print("         FENCE: minimal dilatation is a KNOWN THEOREM; minimal volume is")
        print("         Cao-Meyerhoff.  The join is the content, not the mathematics.")
    else:
        print("         *** THE COLUMNS DISAGREE somewhere -- see the rows above.")
    print(f"T2 {'PASS' if ok else 'FAIL'}")
    return ok


if __name__ == "__main__":
    only = sys.argv[1:] or None
    res = {}
    for k, f in {"T1": T1, "T2": T2}.items():
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
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "thermo.json"),
                   "w", encoding="utf-8"), indent=1, default=str)
