#!/usr/bin/env python3
"""B1536 control K4 (banked and literature data only): the two states themselves (the degree-1 cover), by both routes, at every
pulled-back character of the base's own kappa population (mu_12, L = 1).
  - m004: h^1(m004; rho) = 1 and n(rho) = 0 (Kapovich's two-parabolic theorem, as Bart-Scannell Prop. 4.1 and Example 1 state
    it; sm:B1515's Part 0); the trivial member reads (0, 0) (sm:B1515's M1 row); no member at kappa in {-1, +-i, omega,
    omega^2} (sm:B1515's population B on M1).
  - m003: every member at kappa = 1 is simple (sm:B1530 Proposition P), so n(nu^3 rho) = 0 there.
The members found and every reading are recorded; the comparisons are asserted in identity.py.

    python3 control_k4.py [--record]   ->  k4.json"""
import json
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run as RUN  # noqa: E402

ONE = {"a": [0], "b": [0], "t": [0]}


def main():
    t0 = time.time()
    out = {}
    for name in ("m004", "m003"):
        for rt in ("N", "R"):
            rows = RUN.read_cover((rt, name, "d1.1", ONE))
            out[f"{rt} {name}"] = [{k: r[k] for k in ("u", "kappa", "member", "S", "P") if k in r} for r in rows[:-1]]
    checks = {}
    for rt in ("N", "R"):
        m4 = {r["kappa"]: r for r in out[f"{rt} m004"]}
        checks[f"{rt}: m004 kappa = 1: h1(rho) = 1, n(rho) = 0, n(1) = 0, count (0, 0)"] = (
            m4["0"]["S"]["h1(V_eta)"] == 1 and m4["0"]["S"]["n((VL)*)"] == 0 and m4["0"]["S"]["n(L)"] == 0 and
            m4["0"]["P"]["count"] == [0, 0])
        checks[f"{rt}: m004 no member at kappa in -1, +-i, omega, omega^2"] = not any(
            m4[k]["member"] for k in ("1/2", "1/4", "3/4", "1/3", "2/3"))
        m3 = [r for r in out[f"{rt} m003"] if r["kappa"] == "0"]
        checks[f"{rt}: m003 kappa = 1: every member simple (n(nu^3 rho) = 0, h1(V_eta) = 1)"] = all(
            r["S"]["n((VL)*)"] == 0 and r["S"]["h1(V_eta)"] == 1 for r in m3 if r["member"]) and len(m3) == 5
    for name in ("m004", "m003"):
        a = [(r["u"], r["kappa"], r["S"], r.get("P", {}).get("count")) for r in out[f"N {name}"]]
        b = [(r["u"], r["kappa"], r["S"], r.get("P", {}).get("count")) for r in out[f"R {name}"]]
        checks[f"routes agree on {name}"] = a == b
    res = {"checks": checks, "holds": all(checks.values()), "readings": out, "seconds": round(time.time() - t0)}
    print(json.dumps({"checks": checks, "holds": res["holds"], "seconds": res["seconds"]}, indent=1))
    if "--record" in sys.argv:
        (HERE / "k4.json").write_text(json.dumps(res, indent=1) + "\n")
    return res


if __name__ == "__main__":
    main()
