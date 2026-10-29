"""B1811 census (P-432's second half): the frame's outputs at the four configurations the object's symmetry fixes (B1810),
in B1726's census format, for B1810's 13 directions (B1809's Table T and B1730's complete n = 1 zero-free family).
B1740's sealed census module is loaded unchanged (its sha256 asserted) and its compute() called exactly; only its Higgs
function is extended from {F_-2, DR} to the 13 directions (F_a = (eps th2^a, eps th4^a, i th3^a), eps = i^((a+2)/2),
B1730; F_-2 is B1740's own -- control C1a), and the radii are passed as B1667's exact values at each point (B1810).
Lines in compute()'s convention w = a tau + b (b1656_funcs' line_w(p1, p2, tau) = p1 tau - p2, so (p1, p2) -> (p1, -p2 mod 1)):
(i, 0), (omega, 0) with omega = e^{i pi/3}, (i, (1/2, 1/2)), (omega, (1/3, 2/3) in line_w) = (1/3, 1/3) here.  52 rows.
    python3 -B census.py      # writes census.jsonl and control.json; prints "census exit 0"
Importing computes nothing."""
import sys, json, math, hashlib, pathlib, importlib.util
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
SRC = ROOT / "frontier" / "B1740_the_non_null_higgs_under_the_standard_models_reading" / "verification" / "census.py"
SRC_SHA = "f5c874f7149752e33f5579d65a36a1213e1eaed5771f91c8d5bee34fcb40f5f1"
OUT = HERE / "census.jsonl"
W = (0.5, math.sqrt(3) / 2)
CONFIGS = [("(i, 0)", (0.0, 1.0), (0, 0)), ("(omega, 0)", W, (0, 0)), ("(i, (1/2, 1/2))", (0.0, 1.0), (Fr(1, 2), Fr(1, 2))),
           ("(omega, (1/3, 2/3))", W, (Fr(1, 3), Fr(1, 3)))]
DIRS = ["DR", "a0", "R", "t=-5/288"] + ["F_%d" % a for a in (-10, -6, -2, 6, 10, 14, 18, 22, 26)]
_C = {}


def K():
    if "K" not in _C:
        assert hashlib.sha256(SRC.read_bytes()).hexdigest() == SRC_SHA
        sp = importlib.util.spec_from_file_location("b1740_census", SRC)
        m = importlib.util.module_from_spec(sp); sys.modules["b1740_census"] = m; sp.loader.exec_module(m)
        _C["K"] = m; _C["orig_higgs"] = m.higgs
        m.higgs = higgs
    return _C["K"]


def higgs(t, which):
    """the 13 directions at tau = t (normalised by the largest component; no ratio depends on the scalar)"""
    import mpmath as mp
    from fractions import Fraction as F
    k = K(); te = k._modules()["te"]; T = mp.mpc(t.real, t.imag)
    if which in ("DR", "Fm2"):
        return _C["orig_higgs"](t, which)
    if which in ("a0", "R", "t=-5/288"):
        S = te.S
        sec = {"R": te.B[0],
               "a0": [te.B[2][j] + S.c(F(-1, 48)) * te.e4 * te.B[0][j] for j in range(3)],
               "t=-5/288": [te.B[2][j] + S.c(F(-5, 288)) * te.e4 * te.B[0][j] for j in range(3)]}[which]
        v = [complex(te.ev(c, T)) for c in sec]
    else:
        a = int(which[2:]); eps = 1j ** ((a + 2) // 2)
        th2 = mp.fsum(mp.exp(1j * mp.pi * T * (n + mp.mpf(1) / 2) ** 2) for n in range(-30, 30))
        th3 = mp.fsum(mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31))
        th4 = mp.fsum((-1) ** n * mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31))
        v = [complex(eps * th2 ** a), complex(eps * th4 ** a), complex(1j * th3 ** a)]
    m = max(abs(x) for x in v)
    return [x / m for x in v]


def radii(re_t, im_t):
    b = json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text(encoding="utf-8"))
    pts = b["points"]; pts = pts if isinstance(pts, list) else list(pts.values())
    for p in pts:
        if isinstance(p, dict) and "tau" in p and abs(complex(*p["tau"]) - complex(re_t, im_t)) < 1e-9:
            return {"L_max": p["L_max"], "L_2": p["L_2"]}
    raise KeyError((re_t, im_t))


def main():
    k = K(); rows = []
    for di, d in enumerate(DIRS):
        for ci, (cname, (re_t, im_t), (a, b)) in enumerate(CONFIGS):
            r = k.compute(re_t, im_t, a, b, Ls=radii(re_t, im_t), which=d)
            r.update(line=10 * di + ci, Re_tau=re_t, Im_tau=im_t, direction=d, config=cname); rows.append(r)
            print(d, cname, "done", flush=True)
    assert all(math.isfinite(v) for r in rows for k_, x in r.items() if "|" in k_ for v in x)
    OUT.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    # controls
    ctrl = {}
    t = complex(0.37, 2.41)
    va, vb = higgs(t, "F_-2"), _C["orig_higgs"](t, "Fm2")
    ctrl["C1a_F-2_equals_B1740s_higgs"] = max(abs(x - y) for x, y in zip(va, vb))
    b40 = [json.loads(l) for l in (SRC.parent / "census.jsonl").read_text(encoding="utf-8").splitlines()[:1] if l.strip()][0]
    a40, bb40 = k.lines()[b40["line"]]
    rr = k.compute(b40["Re_tau"], b40["Im_tau"], a40, bb40, which="Fm2")
    ctrl["C1b_B1740_row_reproduced"] = max(abs(x - y) for key in rr for x, y in zip(rr[key], b40[key]))
    tab = {(x["config"], x["direction"], x["radius"], x["reading"]): x for x in
           json.loads((ROOT / "frontier" / "B1810_the_symmetry_selection_value_table" / "verification" / "symmetry_selection_table.json").read_text(encoding="utf-8"))["rows"]}
    dev, nck = 0.0, 0
    SEC = (("up", "up", 0), ("down", "down", 1), ("lep", "lepton", 2))
    for r in rows:
        for h in ("L_max", "L_2"):
            for sec, key, pos in SEC:
                for rn in ("S", "St"):
                    rs = "".join("S~" if (j == pos and rn == "St") else "S" for j in range(3))
                    ref = tab[(r["config"], r["direction"], h, rs)][key]; mine = r["%s|%s|%s" % (sec, h, rn)]
                    dev = max(dev, abs(mine[0] - ref[1]) / max(abs(ref[1]), 1e-2), abs(mine[1] - ref[0]) / max(abs(ref[0]), 1e-2))
            for ru in ("S", "St"):
                for rd in ("S", "St"):
                    rs = ("S~" if ru == "St" else "S") + ("S~" if rd == "St" else "S") + "S"
                    t_ = tab[(r["config"], r["direction"], h, rs)]
                    if t_["V defined"]:
                        nck += 1
                        dev = max(dev, max(abs(x - y) / max(abs(y), 1e-2) for x, y in zip(r["ckm|%s|%s|%s" % (h, ru, rd)][:3], t_["|V_us|, |V_cb|, |V_ub|"])))
    ctrl["C1c_ckm_cells_compared"] = nck
    ctrl["C1c_B1810_rows_reproduced_relative"] = dev
    (HERE / "control.json").write_text(json.dumps(ctrl, indent=1), encoding="utf-8")
    print(json.dumps(ctrl)); print("census exit 0")


if __name__ == "__main__":
    main()
