#!/usr/bin/env python3
"""B1523 -- the read-out of census.json against the sealed predictions P1-P9 (PREREGISTRATION.md Sec. 5).

Decisions, with their margins recorded:
  - rigid rel cusp: dim H^1(M; v) = 1 in both routes (Heusener-Porti Cor. 5.4);
  - eps = +1 or -1: |eps -+ 1| < 1e-20 with eigen-residual < 1e-20 (route R; route C the same with |Im eps| < 1e-20);
  - a slope is rigid (Heusener-Porti Def. 7.1) when route R's residual and route C's test both exceed 1e-20, not rigid when both
    are below 1e-30; anything else is a disagreement (P4 fails and the reading stops there).
  - every rank decision (H^1 with coefficients R, so(3,1), v; both routes) keeps its margin: largest dropped singular value
    < 1e-35, smallest kept > 1e-20; a decision outside it counts as a disagreement.
A disagreement between the routes, or a lemma check that fails, is a bug to be found before anything is read (Sec. 5).
Usage: python3 read_out.py   (writes read_out.json beside it)"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
NONZERO, ZERO = 1e-20, 1e-30
GOLDEN_BROKEN = {"+LLLLRLLLRR", "-LLLLRLLLRR", "+LLLLRLRRRLRR", "-LLLLRLRRRLRR"}


def sign_of(e, im=0.0, res=0.0):
    if abs(im) > NONZERO or res > NONZERO:
        return None
    if abs(e + 1) < NONZERO:
        return -1
    if abs(e - 1) < NONZERO:
        return 1
    return None


def main():
    census = json.loads((HERE / "census.json").read_text())
    controls = json.loads((HERE / "controls.json").read_text())
    ms = census["manifolds"]
    out = {"manifolds read": len(ms), "missing": census["missing"]}
    disagreements, lemma_failures, rows = [], [], []
    for m in ms:
        R, C = m["R"], m["C"]
        dR = [R["H1"][k]["dim"] for k in ("triv", "so", "v")]
        dC = [C["H1"][k]["dim"] for k in ("triv", "so", "v")]
        row = {"manifold": m["manifold"], "length": m["length"], "states": m["states"], "kinds": m["kinds"],
               "dims R": dR, "dims C": dC}
        if dR != dC:
            disagreements.append((m["manifold"], "dimensions", dR, dC))
        row["rigid"] = dR[2] == 1 and dC[2] == 1
        if row["rigid"]:
            # slopes
            sl = {}
            for key in ("fibre boundary mu", "section lambda"):
                a, b = R["slope residual"][key], C["slope test"][key]
                if a > NONZERO and b > NONZERO:
                    sl[key] = True
                elif a < ZERO and b < ZERO:
                    sl[key] = False
                else:
                    sl[key] = None
                    disagreements.append((m["manifold"], "slope " + key, a, b))
            row["fibre boundary rigid"], row["section rigid"] = sl["fibre boundary mu"], sl["section lambda"]
            # isometries
            isos = []
            if len(R["isometries"]) != len(C["isometries"]):
                disagreements.append((m["manifold"], "isometry count", len(R["isometries"]), len(C["isometries"])))
            for x, y in zip(R["isometries"], C["isometries"]):
                if x["cusp map"] != y["cusp map"]:
                    disagreements.append((m["manifold"], "cusp maps", x["cusp map"], y["cusp map"]))
                sR = sign_of(x["eps"], 0.0, x["residual"])
                sC = sign_of(y["eps"][0], y["eps"][1], y["residual"])
                if sR is None or sR != sC:
                    disagreements.append((m["manifold"], "eps", x["cusp map"], x["eps"], y["eps"], x["residual"], y["residual"]))
                checks = max(x["lattice check"], x["normaliser check"], y["lattice check"], y["normaliser check"])
                if checks > 1e-30:
                    lemma_failures.append((m["manifold"], "lattice/normaliser", x["cusp map"], checks))
                hR, hC = x["on H1(P; v)"], y["on H1(P; v)"]
                if abs(hR["trace"] - hC["trace"][0]) > NONZERO or abs(hR["det"] - hC["det"][0]) > NONZERO:
                    disagreements.append((m["manifold"], "action on H1(P; v)", x["cusp map"], hR, hC))
                Cm = x["cusp map"]
                # the lemmas: iota (cusp map I) +1; -I acts as -1 and has eps -1; det -1 acts as a reflection
                if Cm == [[1, 0], [0, 1]] and not (sR == 1 and abs(hR["trace"] - 2) < 1e-30 and abs(hR["det"] - 1) < 1e-30):
                    lemma_failures.append((m["manifold"], "L-iota", Cm, sR, hR))
                if Cm == [[-1, 0], [0, -1]] and not (sR == -1 and abs(hR["trace"] + 2) < 1e-30 and abs(hR["det"] - 1) < 1e-30):
                    lemma_failures.append((m["manifold"], "L-rev", Cm, sR, hR))
                if x["det"] == -1:
                    if not (abs(hR["trace"]) < 1e-30 and abs(hR["det"] + 1) < 1e-30):
                        lemma_failures.append((m["manifold"], "L-R reflection", Cm, hR))
                    # Lemma R: eps = -1 iff (inverts the fibre boundary) XOR (the fibre boundary is not a rigid slope)
                    if sl["fibre boundary mu"] is not None and sR is not None:
                        if (sR == -1) != (x["inverts the fibre boundary"] != (not sl["fibre boundary mu"])):
                            lemma_failures.append((m["manifold"], "L-R equivalence", Cm, sR, sl["fibre boundary mu"]))
                isos.append({"cusp map": Cm, "det": x["det"], "inverts": x["inverts the fibre boundary"], "eps": sR})
            if max(R["translation defect"], C["translation defect"]) > 1e-30:
                lemma_failures.append((m["manifold"], "translation", R["translation defect"], C["translation defect"]))
            row["isometries"] = isos
            row["dualising isometry"] = any(i["eps"] == -1 for i in isos)
            row["longitude rule holds"] = all((i["eps"] == -1) == i["inverts"] for i in isos)
            row["orientation-reversing isometry"] = any(i["det"] == -1 for i in isos)
        row["a longitude-inverting isometry"] = m["a longitude-inverting isometry (words)"]
        rows.append(row)
    # every rank decision with its margin, both routes, all three modules: dropped < 1e-35, kept > 1e-20 (Sec. 5, P4)
    undecided = []
    for m in ms:
        for rt in "RC":
            for k in ("triv", "so", "v"):
                fk, fd = m[rt]["H1"][k]["fox margin"]
                ck, cd = m[rt]["H1"][k]["coboundary margin"]
                if (fd is not None and fd > 1e-35) or (cd is not None and cd > 1e-35) or (fk is not None and fk < 1e-20) or (ck is not None and ck < 1e-20):
                    undecided.append((m["manifold"], rt, k, fk, fd, ck, cd))
    for u in undecided:
        disagreements.append(("margin",) + tuple(u))
    out["rank decisions outside the margin"] = [list(map(str, u)) for u in undecided]
    rigid = [r for r in rows if r["rigid"]]
    reflective = [r for r in rigid if r["orientation-reversing isometry"]]
    broken = [r for r in rigid if not r["dualising isometry"]]
    predicted_broken = [r for r in rigid if not r["a longitude-inverting isometry"]]
    golden_broken = {r["manifold"] for r in broken} & GOLDEN_BROKEN
    golden_all = {g["state"] for g in controls["C1"]["golden (monodromy field Q(sqrt5))"]}
    P = {}
    P["P1 the controls pass and the census re-reads them"] = bool(controls["all controls pass"] and census["banked identity (controls re-read)"])
    P["P2 every manifold is rigid rel cusp"] = len(rigid) == len(rows) == 536
    P["P3 on every rigid manifold with an orientation-reversing isometry, eps = -1 exactly on the fibre-boundary-inverting isometries"] = \
        all(r["longitude rule holds"] for r in reflective)
    P["P4 the routes agree everywhere"] = not disagreements
    P["P5 the mirror-broken rigid manifolds are exactly the rigid ones without a longitude-inverting isometry"] = \
        {r["manifold"] for r in broken} == {r["manifold"] for r in predicted_broken}
    P["P6 the fibre boundary is a rigid slope on every rigid manifold"] = all(r["fibre boundary rigid"] for r in rigid)
    P["P7 the golden mirror-broken manifolds are exactly +-L4RL3R2 and +-L4RLR3LR2"] = \
        {r["manifold"] for r in broken if r["manifold"] in golden_all} == GOLDEN_BROKEN
    P["P8 the lemmas hold on every rigid manifold in both routes"] = not lemma_failures
    # P9: Lemma S on every rigid manifold (route R's slope box); on a reflective one the coset is 30 + 60Z (fibre boundary rigid)
    # or 60Z (not rigid), Lemma R
    s_fail = []
    for m in ms:
        if "slope box" not in m["R"]:
            continue
        box = m["R"]["slope box"]
        if any(ZERO <= r <= NONZERO for p, q, r, a in box):
            s_fail.append((m["manifold"], "a slope in the box is undecided"))
            continue
        angs = [a for p, q, r, a in box if r < ZERO]
        if angs and not all(min((a - angs[0]) % 60.0, 60.0 - (a - angs[0]) % 60.0) < 1e-9 for a in angs):
            s_fail.append((m["manifold"], "zero slopes off one coset of 60 degrees", angs))
        row = next(x for x in rows if x["manifold"] == m["manifold"])
        if angs and row.get("orientation-reversing isometry") and row.get("fibre boundary rigid") is not None:
            coset = angs[0] % 60.0
            want = 30.0 if row["fibre boundary rigid"] else 0.0
            if min(abs(coset - want), 60.0 - abs(coset - want)) > 1e-9:
                s_fail.append((m["manifold"], "reflective: coset not as Lemma R says", angs, row["fibre boundary rigid"]))
    out["lemma S failures"] = [list(map(str, f)) for f in s_fail]
    out["zero slopes in the box, by manifold"] = {m["manifold"]: [[p, q, a] for p, q, r, a in m["R"]["slope box"] if r < ZERO]
                                                  for m in ms if "slope box" in m["R"]}
    P["P9 Lemma S on every rigid manifold: the zero slopes in the box lie in one coset of 60 degrees (30 + 60Z or 60Z on a "
      "reflective one, as its fibre boundary is or is not rigid)"] = not s_fail
    out["predictions"] = P
    out["counts"] = {
        "manifolds": len(rows), "rigid": len(rigid), "not rigid": [(r["manifold"], r["dims R"], r["dims C"]) for r in rows if not r["rigid"]],
        "rigid with an orientation-reversing isometry": len(reflective),
        "mirror-broken rigid manifolds": len(broken), "of them by sign": {s: sum(1 for r in broken if r["manifold"][0] == s) for s in "+-"},
        "mirror-broken word states": sum(len(r["states"]) for r in broken),
        "mirror-broken by kind": {k: sum(1 for r in broken if (("all three" if all(r["kinds"].values()) else
                                                                 "rev only" if r["kinds"]["rev"] else "swap only" if r["kinds"]["swap"] else
                                                                 "swaprev only" if r["kinds"]["swaprev"] else "none") == k))
                                  for k in ("none", "swaprev only", "swap only", "rev only", "all three")},
        "mirror-broken by length": {n: sum(1 for r in broken if r["length"] == n) for n in range(2, 13)},
        "golden mirror-broken": sorted(golden_broken | {r["manifold"] for r in broken if r["manifold"] in golden_all}),
        "fibre boundary rigid": sum(1 for r in rigid if r["fibre boundary rigid"]),
        "section rigid": sum(1 for r in rigid if r["section rigid"]),
        "section not rigid": [r["manifold"] for r in rigid if r["section rigid"] is False],
        "fibre boundary not rigid": [r["manifold"] for r in rigid if r["fibre boundary rigid"] is False],
        "longitude rule fails on": [r["manifold"] for r in rigid if not r["longitude rule holds"]],
    }
    # margins of every decision
    vR = [m["R"]["H1"]["v"] for m in ms]
    out["margins"] = {
        "v: smallest kept singular value (Fox, route R / C)": [min(x["fox margin"][0] for x in vR),
                                                               min(m["C"]["H1"]["v"]["fox margin"][0] for m in ms)],
        "v: largest dropped singular value (Fox, route R / C)": [max(x["fox margin"][1] for x in vR),
                                                                 max(m["C"]["H1"]["v"]["fox margin"][1] for m in ms)],
        "slope residual: smallest counted nonzero / largest counted zero (route R)": [
            min([m["R"]["slope residual"][k] for m in ms if "slope residual" in m["R"] for k in m["R"]["slope residual"]
                 if m["R"]["slope residual"][k] > NONZERO], default=None),
            max([m["R"]["slope residual"][k] for m in ms if "slope residual" in m["R"] for k in m["R"]["slope residual"]
                 if m["R"]["slope residual"][k] < ZERO], default=None)],
        "slope test: smallest counted nonzero / largest counted zero (route C)": [
            min([m["C"]["slope test"][k] for m in ms if "slope test" in m["C"] for k in m["C"]["slope test"]
                 if m["C"]["slope test"][k] > NONZERO], default=None),
            max([m["C"]["slope test"][k] for m in ms if "slope test" in m["C"] for k in m["C"]["slope test"]
                 if m["C"]["slope test"][k] < ZERO], default=None)],
        "eps: largest distance from +-1 (route R)": max([min(abs(i["eps"] - 1), abs(i["eps"] + 1)) for m in ms if "isometries" in m["R"]
                                                         for i in m["R"]["isometries"]], default=None),
        "eps: largest eigen-residual (route R / C)": [max([i["residual"] for m in ms if "isometries" in m["R"] for i in m["R"]["isometries"]], default=None),
                                                      max([i["residual"] for m in ms if "isometries" in m["C"] for i in m["C"]["isometries"]], default=None)],
    }
    out["disagreements"] = [list(map(str, d)) for d in disagreements]
    out["lemma failures"] = [list(map(str, f)) for f in lemma_failures]
    if not P["P4 the routes agree everywhere"] or not P["P8 the lemmas hold on every rigid manifold in both routes"] or s_fail:
        out["outcome"] = "NOT READ: a disagreement or a lemma failure is a bug to be found first (Sec. 5)"
    elif not broken:
        out["outcome"] = "A: every flexible state's family is dualised by an isometry"
    else:
        out["outcome"] = ("B: mirror-broken flexible states exist" + ("" if P["P2 every manifold is rigid rel cusp"] else
                                                                      "; C: some manifolds are not rigid rel cusp (listed)"))
    out["rows"] = rows
    (HERE / "read_out.json").write_text(json.dumps(out, indent=1))
    for k, v in P.items():
        print(("YES " if v else "NO  ") + k)
    for k, v in out["counts"].items():
        if isinstance(v, list) and len(v) > 12:
            v = f"{len(v)} items: {v[:12]} ..."
        print(f"  {k}: {v}")
    print("margins:", json.dumps(out["margins"]))
    print("disagreements:", len(disagreements), "lemma failures:", len(lemma_failures))
    print("OUTCOME", out["outcome"])


if __name__ == "__main__":
    main()
