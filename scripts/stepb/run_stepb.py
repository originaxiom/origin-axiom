#!/usr/bin/env python3
"""STEP B, THE RUN (read ONCE, after the seal; THE FINAL ATTACK, P-495).  Refused unless the refined census's manifest is
committed and pushed (guard.py).  Nothing here is run before the seal; it is committed with the card.

Inputs: the census and its manifest (guarded); the sigma-only file; the pre-seal p2 output (its Clopper-Pearson upper end);
m, the joint look ledger's count at the seal plus one (at least 53); the targets -- the nine from B1741's sealed comparison
(compare.arrays()["T9"], natural logs, in sigma's order) and J from the declared source (the PDG 2024 CKM review's global
fit), given as a number.  Our world is scored at c = 3 only (the card's section 2).

In order, written once to <out.json>:
  S    in support (cells.CellIndex.support at c = 3, chi2_ten < 23.209 on continuous tau); the least chi2_ten and its address
       (branch-and-bound, relative 1e-3); read-outs: the least chi2_nine, and S at the c = 1 arm.
  K    kten.K_ten at c = 3: C_six, bits_CKM, C_ten; p_K = 2^-C_ten (exact; outcome.p_exact).
  CKM  p_CKM = 2^-bits_CKM (exact); the clause (kten.ckm_clause at c = 3).
  X2   p2's upper end (pre-seal, from the p2 driver's output).
  T    T1 under the area clock at y0 = the least chi2_ten's Im tau (exact); T is NEGATIVE only if NEGATIVE under every clock
       of the menu, so a CONSISTENT area grade settles it; a NEGATIVE area grade stops the run for the other clocks.
  the legs and the pre-written reading (outcome.py).
    python3 -I run_stepb.py <refined dir> <manifest.json> <manifest sha256> <sigma file> <p2.json> <m> <J> <out.json>"""
import contextlib, io, json, math, pathlib, sys, time

GEN = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(GEN))
import numpy as np

import clocks
import compression as K
import kten
import outcome as O
import stepb_core as C
from p2_driver import build


def targets(J: float) -> np.ndarray:
    B1741 = ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification"
    sys.path.insert(0, str(B1741))
    with contextlib.redirect_stdout(io.StringIO()):
        import compare
        T9 = np.asarray(compare.arrays()["T9"], float)
    assert T9.shape == (9,) and np.isfinite(T9).all()
    assert J > 0
    t = np.concatenate([T9, [math.log(J)]])
    return t


def main(refined, manifest, expected, sigma_file, p2_file, m, J, out):
    m = int(m); J = float(J); t0 = time.time()
    if m < 53:
        sys.exit("m is the joint look ledger's count at the seal plus one, at least 53")
    ci, sig, meta = build(refined, manifest, expected, sigma_file, spaces=("nine", "six", "ckm3"), gauss=(4, 16, 32, 64))
    t10 = targets(J)
    rep = dict(meta, m=m, gate_bits=K.gate_bits(m), J_source="PDG 2024 CKM review, global fit")
    def save(status):
        rep["status"] = status; rep["seconds"] = round(time.time() - t0, 1)
        pathlib.Path(out).write_text(json.dumps(rep, indent=1, default=str) + "\n", encoding="utf-8")
    # S
    s = ci.support(t10, C.C_OURS)
    g = ci.global_min(t10, C.C_OURS)
    if g["row"] is None or g["point"] is None:
        rep["S"] = {"in_support": bool(s["in_support"]), "undecided": s["undecided"]}
        save("STOPPED: the least chi2_ten has no address (global_min returned none)"); sys.exit(rep["status"])
    g9 = ci.global_min(t10, C.C_OURS, comps=tuple(range(9)))
    s1 = ci.support(t10, C.C_ARM1)
    rep["S"] = {"in_support": bool(s["in_support"]), "undecided": s["undecided"], "least_chi2_ten": g["min_chi2"],
                "address": {"key": [str(x) for x in ci.ch.keys[ci.choice[g["row"]]]], "tau": g["point"]},
                "readout_least_chi2_nine": g9["min_chi2"], "readout_c1_in_support": bool(s1["in_support"])}
    save("S computed")
    # the fidelity read-out at the decisive address (the fifth review's N1): the evaluator itself at the least-chi2 point
    rep["S"]["readout_fresh_at_address"] = fresh_chi2(ci, g, t10, refined)
    save("S computed; fresh check done")
    # K and the CKM leg
    k = kten.K_ten(ci, t10, C.C_OURS)
    rep["K"] = {key: (float(v) if isinstance(v, np.floating) else v) for key, v in k.items() if key not in ("six_report", "num_report", "marg_report")}
    rep["K"]["reports"] = {key: k.get(key) for key in ("six_report", "num_report", "marg_report")}
    K_grade = k["grade"]
    if K_grade == "JUDGED" and not k.get("converged", False):
        K_grade = "UNJUDGED"; rep["K"]["unjudged_reason"] = "the quadrature's checks or the windows' dropped mass did not converge"
    if K_grade == "JUDGED":
        pK, pC = O.p_exact(k["C_ten"]), O.p_exact(k["bits_CKM"])
        cl = kten.ckm_clause(ci, t10 - C.c_shift(3.0))
    else:
        pK, pC, cl = 1.0, 1.0, {"clause": False}
    rep["CKM"] = {"p_CKM": pC, "clause": cl}
    save("S, K and the CKM leg computed")
    # X2: p2's upper end counts the undecided worlds as possible hits (the fifth review's N2)
    p2 = json.loads(pathlib.Path(p2_file).read_text())
    p2_up = float(p2["p2_cp95"][1])
    # T
    y0 = g["point"][1]
    T_area = clocks.T1(clocks.area_cdf, y0)
    if T_area["grade"] == "NEGATIVE":
        rep["T"] = {"area": T_area}
        save("STOPPED: the area clock is NEGATIVE; the menu's other clocks must be computed"); sys.exit(rep["status"])
    rep["T"] = {"area": T_area, "decides": "CONSISTENT under area: T is not NEGATIVE under every clock"}
    L = O.legs(rep["S"]["in_support"], p2_up, K_grade, k.get("C_ten"), pK, pC, bool(cl["clause"]), m)
    rep["legs"] = L; rep["p"] = {"p2_up": p2_up, "p_K": pK, "p_CKM": pC, "gate": 0.01 / m}
    rep["reading"] = O.reading(L, (T_area["grade"],))
    if not rep["S"]["in_support"] and s["undecided"]:
        rep["reading"] += " (the support search left %d cells undecided below 1e-7 in tau)" % s["undecided"]
    save("DONE")
    print(json.dumps(rep, indent=1, default=str))


def fresh_chi2(ci, g, t10, refined):
    """chi2_ten at the least-chi2 address by the census's own evaluator (B1821's cm_zero_line.rows_at), against the
    interpolant's value there: a read-out of the interpolant's fidelity at the decisive point"""
    from fractions import Fraction as Fr
    import stepb_core as C_
    EVAL = ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"
    sys.path.insert(0, str(EVAL))
    import cm_zero_line as Z
    from census_io import reading_index, line_key
    key = ci.ch.keys[ci.choice[g["row"]]]; line, d, r, kk = key
    # the census file's own representative of the line class (its name: N<order>_<a>_<b>, fractions written p-q)
    ab = None
    for f in sorted(pathlib.Path(refined).glob("*.jsonl.gz")):
        _, fa, fb = f.name[:-len(".jsonl.gz")].split("_")
        fa, fb = (str(Fr(*map(int, x.split("-")))) for x in (fa, fb))
        if line_key(fa, fb) == line:
            ab = (Fr(fa), Fr(fb)); break
    if ab is None:
        return {"defined": False, "reason": "no census file for the line"}
    (a, b) = ab
    x, y = g["point"]
    tt = np.asarray(t10, float) - C_.c_shift(g["c"])
    for row in Z.rows_at(complex(x, y), (Fr(a), Fr(b))):
        if Z.DIRS.index(row["direction"]) == d and ("L_max", "L_2").index(row["radius"]) == r and reading_index(row["reading"]) == kk:
            if not row["V defined"]:
                return {"defined": False}
            f = np.log(np.array([row["up"][1], row["up"][0], row["down"][1], row["down"][0], row["lepton"][1], row["lepton"][0],
                                 *row["V"], abs(row["J"])], float))
            z = (f - tt) / ci.sig
            return {"defined": True, "tau": [x, y], "chi2_ten_fresh": float(z @ z), "chi2_ten_interpolant": g["min_chi2"]}
    return {"defined": False, "reason": "the row's key was not found in the fresh evaluation"}


if __name__ == "__main__":
    if len(sys.argv) != 9: sys.exit(__doc__)
    main(*sys.argv[1:])
