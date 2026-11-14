"""Review 82 (agy-exp's finding F4 on this arc): seat_formula_check.json keeps 24 cases (eight characteristics at three
points of the golden geodesic), but seat_formula.py's own run covers four characteristics, two placements, at one
point. This script reproduces the kept 24 from seat_formula.py's F and step3_norm.py's norm, unchanged: the three
points and eight characteristics are read from the kept file, u = c - (1/2, 1/2). The two points off the top are kept
to four decimals; they lie on the golden geodesic (centre 1/2, radius sqrt(5)/2) to 4e-5, and the formula is an
identity at every tau, so the points' rounding does not matter to the check. It writes seat_formula_24_run.json.
Main's code; nothing of any seat's is read or run."""
import json, pathlib, sys, warnings
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.simplefilter("ignore")
import mpmath as mp
import seat_formula as SF, step3_norm as S

C = -2 * mp.pi * (mp.euler + mp.log(mp.pi))

if __name__ == "__main__":
    kept = json.loads((HERE / "seat_formula_check.json").read_text())
    out = []
    for r in kept:
        t = complex(*r["tau"]); tau = mp.mpc(t.real, t.imag); c = tuple(r["c"])
        n = S.norm(c, t)
        f = float(SF.F(c[0] - .5, c[1] - .5, tau) + mp.pi * mp.log(tau.imag) + C)
        out.append({"tau": r["tau"], "c": r["c"], "N": n, "F_u+pi log y+C": f, "diff": abs(n - f),
                    "N vs kept": abs(n - r["N"]), "F vs kept": abs(f - r["F_u+pi log y+C"])})
        print(r["tau"], r["c"], "diff %.2e" % out[-1]["diff"], "N vs kept %.1e" % out[-1]["N vs kept"],
              "F vs kept %.1e" % out[-1]["F vs kept"], flush=True)
    (HERE / "seat_formula_24_run.json").write_text(json.dumps(out, indent=1))
