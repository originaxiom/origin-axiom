"""T-SIGN (T_SIGN_PREREGISTRATION.md, sealed at 50352be3a, sha256 258718ef...). Minus threads b+-W against plus threads b++W."""
import itertools, json, math, pathlib, warnings
warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent
PI2 = math.pi ** 2
def red(x):
    y = math.fmod(x, PI2)
    if y > PI2 / 2: y -= PI2
    if y <= -PI2 / 2: y += PI2
    return y
def lyndon_upto(n):
    return [w for m in range(2, n + 1) for w in ("".join(p) for p in itertools.product("LR", repeat=m))
            if all(w < w[i:] + w[:i] for i in range(1, len(w)))]
def lr(w): return min(w[i:] + w[:i] for i in range(len(w)))
def swap(w): return w.translate(str.maketrans("LR", "RL"))
def meas(name):
    M = snappy.Manifold(name)
    return float(M.volume()), red(complex(M.complex_volume()).imag), M.solution_type(), M.is_orientable()
out, fails = {}, []
m003 = snappy.Manifold("b+-LR")
v0, c0, s0, o0 = meas("b+-LR")
out["N0_m003"] = {"identify": [str(x) for x in m003.identify()][:2], "cs": c0, "orientable": o0, "solution": s0}
sym14 = [w for w in lyndon_upto(14) if lr(swap(w)) in (w, lr(w[::-1]))]
n1_bad, n1_rows = [], {}
for w in sym14:
    try:
        v, c, s, o = meas("b+-" + w)
        n1_rows[w] = [v, c, s, o]
        if not (abs(abs(c) - PI2 / 2) < 1e-6): n1_bad.append([w, c])
    except Exception as e:
        fails.append([w, repr(e)])
words10 = lyndon_upto(10)
n2_bad, n2_rows = [], {}
for w in words10:
    try:
        vm, cm, sm, om = meas("b+-" + w)
        vp, cp, sp, op = meas("b++" + w)
        n2_rows[w] = [vp, cp, vm, cm]
        if abs(abs(red(cm - cp)) - PI2 / 2) > 1e-6: n2_bad.append([w, cp, cm])
    except Exception as e:
        fails.append([w, repr(e)])
geo_bad = [w for w, r in n1_rows.items() if r[2] != "all tetrahedra positively oriented" or not r[3]]
out["N0"] = bool(any(s.startswith("m003") for s in out["N0_m003"]["identify"]) and abs(abs(c0) - PI2 / 2) < 1e-6
                 and o0 and not fails and not geo_bad)
out["N1"] = {"swap_symmetric_to_14": len(sym14), "violations": n1_bad[:30], "n_violations": len(n1_bad),
             "holds": bool(not n1_bad and not fails)}
out["N2"] = {"words_to_10": len(words10), "violations": n2_bad[:30], "n_violations": len(n2_bad),
             "holds": bool(not n2_bad and not fails)}
out["failures"] = fails[:20]; out["non_geometric_or_nonorientable"] = geo_bad[:20]
out["readout_vol_minus_vs_plus_first12"] = {w: n2_rows[w] for w in list(n2_rows)[:12]}
out["cells"] = {"N0": out["N0"], "N1": out["N1"]["holds"], "N2": out["N2"]["holds"]}
(HERE / "t_sign.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
print(json.dumps(out, indent=1, default=str))
