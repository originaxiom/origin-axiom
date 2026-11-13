"""B1922: is the frame periodic along the golden thread's geodesic at the thread's own line, with the invariant end?

The golden thread's monodromy acts on the modulus as gamma = T R: tau -> (2 tau + 1)/(tau + 1). By B1724's transport rules
(R: (a, b) -> (a - b, b), L -> L + log|tau + 1|; T: (a, b) -> (a, b - a)), gamma carries a line (a, b) to (a - b, 2b - a)
and the end L to L + log|tau + 1|, which keeps B1921's L~ fixed. The frame's line (2/5, 4/5) goes to (3/5, 1/5), the same
line up to sign (B1914). Written before the run: at that line the covariant readings S and S~ (B1724) give the same
outputs at tau and gamma tau with the end so shifted; at a line gamma does not fix they do not; S* (covariant only under
Gamma^0(2), which does not contain T) does not either. Only DEVIATIONS (B1724's compare: max |log ratio|) are printed and
kept, never an output of the frame. Base points: the symmetric window (tau and gamma tau equally high) and one lower."""
import sys, math, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1724_the_readings_covariance" / "verification"))
import covariance as C

phi = (1 + 5 ** 0.5) / 2
beta, betap, ell = phi, -1 / phi, 2 * math.log(phi ** 2)
LS0 = {"L_max": 1.3, "L_2": 0.9}                              # one end, held fixed as L~ (any value)
LINES = {"own line (2/5, 4/5)": (0.4, 0.8), "line (1/5, 3/5), not fixed": (0.2, 0.6)}


def zt(t):
    return complex((beta * 1j * math.exp(t) + betap) / (1j * math.exp(t) + 1))


def gamma(t):
    return (2 * t + 1) / (t + 1)


def deviations(s0, line):
    t = zt(s0); g = gamma(t)
    assert abs(g - zt(s0 + ell)) < 1e-9
    a, b = line
    d = C.compare(C.frame(t, a, b, LS0), C.frame(g, a, b, {h: LS0[h] + math.log(abs(t + 1)) for h in LS0}))
    cov = max(v for k, v in d.items() if "conjS" not in k); star = max(v for k, v in d.items() if "conjS" in k)
    return {"Im tau": t.imag, "Im gamma tau": g.imag, "S, St": cov, "S*": star}


if __name__ == "__main__":
    out = {}
    for s0 in (-ell / 2, -ell / 2 + 0.15, 0.0):
        for name, line in LINES.items():
            r = deviations(s0, line); out["%.3f %s" % (s0, name)] = r
            print("Im tau %.3f, Im gamma tau %.3f, %s: S,St %.1e  S* %.1e" % (r["Im tau"], r["Im gamma tau"], name, r["S, St"], r["S*"]), flush=True)
    (HERE / "periodic.json").write_text(json.dumps(out, indent=1))
