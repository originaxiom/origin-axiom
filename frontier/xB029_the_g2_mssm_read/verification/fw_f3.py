"""xB029 ADDENDUM 1, F3 v2.  v1 REPORTED A FALSE NEGATIVE AND IS RECORDED AS DEFECTIVE:
it printed 'max b1 = 0' for n = 5 and n = 7, whose |H_1| are 121 = 11^2 and 841 = 29^2, so the
ONLY cyclic cover degrees are 11, 121 and 29, 841 -- all ABOVE its search bound of 8.  Those rows
were UNMEASURED, not negative, and max(..., default=0) printed a zero for them.

v2: enumerate the admissible degrees from H_1 itself, measure every one below a stated bound, and
mark the rest UNMEASURED rather than scoring them.
"""
import json, os, warnings
warnings.filterwarnings("ignore")
import snappy
MAXDEG = 33


def lucas(k):
    a, b = 2, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def divisors_of_exponent(H):
    ds = [d for d in H.elementary_divisors() if d]
    if not ds:
        return []
    e = max(ds)                      # exponent of a finite abelian group = largest divisor
    return [d for d in range(2, e + 1) if e % d == 0]


def scan(M, label):
    H = M.homology()
    admissible = divisors_of_exponent(H)
    measured, unmeasured, hits = [], [], []
    for d in admissible:
        if d > MAXDEG:
            unmeasured.append(d); continue
        try:
            cv = M.covers(d, cover_type="cyclic")
        except Exception as e:
            unmeasured.append((d, f"err {type(e).__name__}")); continue
        bs = [c.homology().betti_number() for c in cv]
        measured.append((d, len(cv), max(bs) if bs else None))
        if bs and max(bs) > 0:
            hits.append((d, max(bs)))
    return {"label": label, "H1": str(H), "admissible_degrees": admissible,
            "measured": measured, "unmeasured": unmeasured, "zero_mode_hits": hits}


print("F3 v2    DOES THE FINITE-pi_1 HYPOTHESIS BITE?  b1 > 0 in a cyclic cover IS a zero mode:")
print("         for a degree-d cyclic cover of a QHS^3, b1 = sum over the nontrivial characters")
print("         chi with chi^d = 1 of dim H^1(Q; C_chi).")
print(f"         Search bound: every admissible degree <= {MAXDEG}; the rest are UNMEASURED.")
print("         FENCE, sealed: ABELIAN characters only.  FW's statement covers EVERY non-trivial")
print("         irreducible rep, so a pass here would be STRICTLY WEAKER than their hypothesis.")

K = snappy.Manifold("4_1")
rows = []

# ---- CALIBRATION: finite pi_1
X2 = K.covers(2, cover_type="cyclic")[0]
X2.dehn_fill((1, 0))
cal = scan(X2, "Sigma_2 = L(5,2), FINITE pi_1")
print(f"\n         CALIBRATION {cal['label']}: H_1 = {cal['H1']}, degrees {cal['admissible_degrees']}")
print(f"           measured {cal['measured']}; zero-mode hits {cal['zero_mode_hits']}")
cal_ok = not cal["zero_mode_hits"] and bool(cal["measured"])
print(f"         finite-pi_1 calibration gives b1 = 0 throughout: {cal_ok}")

# ---- the tower's closed members
print("\n         THE CLOSED TOWER MEMBERS:")
for n in range(3, 9):
    X = K.covers(n, cover_type="cyclic")[0]
    target = lucas(2 * n) - 2
    chosen = None
    for (p, q) in [(0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (3, 1), (1, 0)]:
        X.dehn_fill((p, q))
        H = X.homology()
        t = 1
        for dd in H.elementary_divisors():
            if dd:
                t *= dd
        if H.betti_number() != 0 or t != target:
            continue
        try:
            st = X.solution_type(); v = float(X.volume())
        except Exception:
            st, v = "n/a", None
        hyp = st.startswith("all tetrahedra")
        if hyp:
            chosen = (p, q, t, v, st); break
        if chosen is None:
            chosen = (p, q, t, v, st)
    if chosen is None:
        print(f"           n={n}: no closing slope in the shortlist"); continue
    X.dehn_fill((chosen[0], chosen[1]))
    hyp = chosen[4].startswith("all tetrahedra")
    s = scan(X, f"n={n}")
    s.update({"slope": chosen[:2], "tor": chosen[2], "vol": chosen[3],
              "soltype": chosen[4], "hyperbolic": bool(hyp)})
    rows.append(s)
    print(f"           n={n} slope={chosen[:2]} |H_1|={chosen[2]} "
          f"{'HYPERBOLIC vol=' + format(chosen[3], '.5f') if hyp else 'NOT hyperbolic'}")
    print(f"             admissible degrees {s['admissible_degrees']}; measured "
          f"{s['measured']}; UNMEASURED {s['unmeasured']}")
    print(f"             ZERO MODES (degree, b1): {s['zero_mode_hits'] or 'none found'}")

hypr = [r for r in rows if r["hyperbolic"]]
hyp_hits = [r for r in hypr if r["zero_mode_hits"]]
fully = [r for r in rows if not r["unmeasured"]]
print(f"\n         hyperbolic members examined: {len(hypr)}; of those, with a zero mode: "
      f"{len(hyp_hits)}  ({[r['label'] for r in hyp_hits]})")
print(f"         members whose admissible degrees were ALL measured: {len(fully)} of {len(rows)}")
print(f"         members with UNMEASURED degrees (not scored either way): "
      f"{[(r['label'], r['unmeasured']) for r in rows if r['unmeasured']]}")

if not cal_ok:
    print("         *** CALIBRATION FAILED.  F3 reports nothing.")
elif hyp_hits:
    print("\n         *** THE KILL CONDITION FIRED, ON A HYPERBOLIC MEMBER.")
    print("         A closed hyperbolic rational homology 3-sphere in the record's own tower has")
    print("         abelian characters with H^1 != 0.  Zero modes are REAL once pi_1 is infinite.")
    print("         FW's no-zero-mode statement genuinely NEEDS its finite-pi_1 hypothesis, and")
    print("         the simple torsion formula does NOT carry over to the hyperbolic side.")
    print("         L225's physics-facing half DIES.  Its T_O algebra (F2) is untouched.")
else:
    print("\n         *** No zero mode found on a hyperbolic member in the measured range.")

json.dump({"calibration": cal, "calibration_ok": bool(cal_ok), "rows": rows,
           "hyperbolic_examined": len(hypr), "hyperbolic_with_zero_modes": len(hyp_hits),
           "maxdeg": MAXDEG},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fw_f3.json"),
               "w", encoding="utf-8"), indent=1, default=str)
print(f"\nF3 v2 {'PASS' if cal_ok else 'FAIL'}  (calibrated; content is the verdict above)")
