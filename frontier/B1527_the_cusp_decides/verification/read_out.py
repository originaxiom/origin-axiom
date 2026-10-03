#!/usr/bin/env python3
"""B1527 read-out: P1-P8 of PREREGISTRATION section 6, read from run_<name>.json exactly as sealed.  Writes read_out.json."""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from run import MANIFOLDS, A_SCAN, name_of, circ_dist  # noqa: E402

REFLECTIVE = {"+LR", "-LR", "+LLRLRR", "-LLRLRR"}
CHIRAL = {"+LLLRLRR", "-LLLRLRR"}
GOLDEN = {"+LLLLRLLLRR", "-LLLLRLLLRR", "+LLLLRLRRRLRR", "-LLLLRLRRRLRR"}


def flt(x):
    return float(str(x).replace(" ", ""))


def margins_ok(m):
    return flt(m["smallest kept"]) > 1e-20 and flt(m["largest dropped"]) < 1e-40


def p1(rec):
    bad = []
    for r in rec["H"]["rows"]:
        tag = (r["u"], r["lambda"], r["module"])
        want_t0 = (1 if r["module"] == "4" else 2) if r["lambda"] == "lambda_c" else 0
        ok = (r["I"] == 0 and all(r["checks"].values()) and r["V"]["t0"] == want_t0 and r["V*"]["t0"] == want_t0
              and r["V"]["a0"] == 0 and r["V*"]["a0"] == 0 and margins_ok(r["margins"]))
        if "W" in r:
            ok = ok and r["W"]["I"] == r["I"] and r["W"]["t0"] == r["V"]["t0"] and r["W"]["s0"] == r["V*"]["t0"]
        if not ok:
            bad.append(tag)
    return {"rows": len(rec["H"]["rows"]), "route W rows": sum(1 for r in rec["H"]["rows"] if "W" in r), "failures": bad,
            "holds": not bad}


def beta_groups(clusters):
    groups = []
    for c in clusters:
        b = c["beta (a=0.002)"]
        for g in groups:
            if circ_dist(g["beta"], b, 180.0) < 1.0:
                g["members"].append(c)
                break
        else:
            groups.append({"beta": b, "members": [c]})
    for g in groups:
        b2 = [m["beta (a=0.002)"] for m in g["members"]]
        b1 = [m["beta (a=0.001)"][0] for m in g["members"] if m["beta (a=0.001)"]]
        g["beta (a=0.002)"] = float(np.mean(b2))
        g["beta (a=0.001)"] = float(np.mean(b1)) if b1 else None
        g["beta extrapolated to a = 0"] = 2 * g["beta (a=0.001)"] - g["beta (a=0.002)"] if b1 else None
    return sorted(groups, key=lambda g: g["beta (a=0.002)"])


def p2(rec):
    cl = rec["clusters"]
    groups = beta_groups(cl)
    betas = [g["beta (a=0.002)"] for g in groups]
    gaps = [circ_dist(betas[i], betas[(i + 1) % len(betas)], 180.0) for i in range(len(betas))] if len(betas) > 1 else []
    holds = len(cl) == 6 and len(groups) == 3 and all(abs(gp - 60) <= 1.0 for gp in gaps)
    return {"alpha clusters": len(cl), "beta groups": [{k: g[k] for k in ("beta (a=0.002)", "beta (a=0.001)",
            "beta extrapolated to a = 0")} | {"alpha clusters": len(g["members"])} for g in groups], "gaps": gaps,
            "holds": holds}


def p3(rec):
    groups = beta_groups(rec["clusters"])
    b0 = sorted(g["beta extrapolated to a = 0"] for g in groups if g["beta extrapolated to a = 0"] is not None)
    coset_ok = len(b0) == 3 and all(abs(x - w) <= 0.3 for x, w in zip(b0, (30.0, 90.0, 150.0)))
    sym = [g for g in groups if g["beta extrapolated to a = 0"] is not None and abs(g["beta extrapolated to a = 0"] - 90) <= 0.3]
    lattice = []
    for g in sym:
        for c in g["members"]:
            s = c["point"]["unipotent line's nearest lattice slope"]
            lattice.append({"slope": s["slope (p, q)"], "X-translation": s["X-translation"]})
    lat_ok = bool(lattice) and all(abs(flt(x["X-translation"])) < 1e-25 for x in lattice)
    return {"beta at a -> 0": b0, "symmetric family's lattice slope": lattice, "holds": coset_ok and lat_ok}


def p4(rec):
    bad, n = [], 0
    for c in rec["clusters"]:
        pt = c["point"]
        ok_pt = flt(pt["polished |F|"]) < 1e-40 and flt(pt["min |eigenvalue - 1|"]) > 1e-6
        if not ok_pt:
            bad.append((c["alpha"], "point"))
        for r in pt["index rows"]:
            n += 1
            ok = (r["I"] == 0 and all(r["checks"].values()) and r["V"]["t0"] == 0 and r["V*"]["t0"] == 0
                  and r["V"]["h1(Delta)"] == 0 and r["V"]["a0"] == 0 and r["V*"]["a0"] == 0 and margins_ok(r["margins"]))
            if "W" in r:
                ok = ok and r["W"]["I"] == r["I"] == 0
            if not ok:
                bad.append((c["alpha"], r["u"], r["lambda"], r["module"]))
    return {"points": len(rec["clusters"]), "index rows": n, "failures": bad, "holds": bool(rec["clusters"]) and not bad}


def p5(rec):
    bf = rec["scans"]["b free"]
    conv = [r for r in bf if r["converged"]]
    frac = len(conv) / len(bf)
    track = [circ_dist(r["alpha"], r["alpha seed"]) < 5 for r in conv]
    tfrac = sum(track) / len(track) if track else 0.0
    signs_ok = []
    for c in rec["clusters"]:
        al = c["alpha"]
        left = [r for r in conv if 0 < ((al - r["alpha"]) % 360) <= 15]
        right = [r for r in conv if 0 < ((r["alpha"] - al) % 360) <= 15]
        if not left or not right:
            signs_ok.append(None)
            continue
        lo = min(left, key=lambda r: (al - r["alpha"]) % 360)
        hi = min(right, key=lambda r: (r["alpha"] - al) % 360)
        signs_ok.append(bool(np.sign(lo["b"]) != np.sign(hi["b"])))
    holds = frac >= 0.5 and tfrac >= 0.9 and bool(signs_ok) and all(s is True for s in signs_ok)
    return {"converged fraction": frac, "tracking fraction": tfrac, "b changes sign across each type-one frame": signs_ok,
            "holds": holds}


def p6(rec):
    conv = sorted([r for r in rec["scans"]["b free"] if r["converged"]], key=lambda r: r["alpha"])
    crossings = []
    for i in range(len(conv)):
        r, s = conv[i], conv[(i + 1) % len(conv)]
        gap = (s["alpha"] - r["alpha"]) % 360
        if gap == 0 or gap > 15 or abs(r["b"]) > 50 * A_SCAN or abs(s["b"]) > 50 * A_SCAN:
            continue
        for gname, g in (("psi_a + psi_b", lambda x: x["psi_a(l)"] + x["psi_b(l)"]),
                         ("3 psi_a - psi_b", lambda x: 3 * x["psi_a(l)"] - x["psi_b(l)"]),
                         ("3 psi_b - psi_a", lambda x: 3 * x["psi_b(l)"] - x["psi_a(l)"])):
            if np.sign(g(r)) != np.sign(g(s)):
                crossings.append({"between alpha": [r["alpha"], s["alpha"]], "g": gname})
    return {"crossings": crossings, "holds": bool(crossings)}


def p7(rec):
    bad = []
    for c in rec["clusters"]:
        pt = c["point"]
        n1, n2 = pt["nullity, type one"], pt["nullity, b free"]
        ok = n1["nullity"] == 4 and n2["nullity"] == 5 and n1["gap ratio"] > 1e6 and n2["gap ratio"] > 1e6
        if not ok:
            bad.append({"alpha": c["alpha"], "type one": n1, "b free": n2})
    return {"failures": bad, "holds": bool(rec["clusters"]) and not bad}


def main():
    out, rows = {}, {}
    for sign, word in MANIFOLDS:
        p = HERE / ("run_" + name_of(sign, word) + ".json")
        if not p.exists():
            rows[sign + word] = "missing"
            continue
        rec = json.loads(p.read_text())
        r = {"P1": p1(rec), "P2": p2(rec), "P4": p4(rec), "P5": p5(rec), "P6": p6(rec), "P7": p7(rec)}
        if sign + word in REFLECTIVE:
            r["P3"] = p3(rec)
        rows[sign + word] = r
    done = {k: v for k, v in rows.items() if v != "missing"}
    preds = {}
    for P in ("P1", "P2", "P4", "P5", "P6", "P7"):
        preds[P] = all(v[P]["holds"] for v in done.values())
    preds["P3"] = all(v["P3"]["holds"] for k, v in done.items() if k in REFLECTIVE)
    preds["P8"] = all(done[k]["P2"]["holds"] and done[k]["P4"]["holds"] for k in GOLDEN | CHIRAL if k in done)
    if not (preds["P1"] and preds["P4"]):
        outcome = "C"
    elif not all(done[k]["P2"]["holds"] for k in (GOLDEN | CHIRAL) if k in done):
        outcome = "B"
    elif preds["P2"]:
        outcome = "A"
    else:
        outcome = "A' (P2 fails only on a reflective manifold)"
    out = {"manifolds": len(done), "missing": [k for k, v in rows.items() if v == "missing"], "predictions": preds,
           "outcome": outcome, "rows": rows}
    (HERE / "read_out.json").write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps({"predictions": preds, "outcome": outcome, "missing": out["missing"]}, indent=1))


if __name__ == "__main__":
    main()
