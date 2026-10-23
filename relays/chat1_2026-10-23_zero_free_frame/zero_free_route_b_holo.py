#!/usr/bin/env python3
"""POST HOC, labelled (written after zero_free_route_b and zero_free_readout were read; committed before its run).
  1. The holomorphic reading.  zero_free_route_b scanned S~ for every sector and the split.  But the zero-free census
     showed that the lines with e = +1 (a = 6, 14, 22) fit with S for every sector, the reading in which every coupling
     is holomorphic in tau (W135: every family mass must be a modular form).  So: the same pairs, kappa grid,
     horocycles and Clebsch (-3, and 1 as the control), with S for every sector; base points by the same rule but in
     this reading (each first line's ten best census rows with S for every sector and the by-hand Clebsch 3).
  2. The covariance control, corrected.  zero_free_route_b's control compared a fixed kappa between unit theta-vectors
     at tau and tau + 1 and failed (0.59).  The unit vectors drop the factors eta^(3-a) and eta^(3-b), whose ratio
     eta^(a-b) carries the phase -1 under T when |a - b| = 12, so a fixed kappa there is not a covariant model; the
     per-point scan is unaffected, since kappa is scanned over all phases and magnitudes at each point.  Here the
     model is built from the full sections, F_a + kappa F_b, with kappa fixed, and compared at tau and tau + 1
     (b -> b - a), for a same-twist pair and a cross-twist pair.
    python3 -B zero_free_route_b_holo.py      # writes zero_free_route_b_holo.json and _run.txt"""
import contextlib, importlib.util, io, json, math, sys, pathlib
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zrb", HERE / "zero_free_route_b.py")
src = (HERE / "zero_free_route_b.py").read_text()
cut = src.index("# controls\n")
NS = {"__file__": str(HERE / "zero_free_route_b.py"), "__name__": "zrb_defs"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:cut], "zero_free_route_b.py", "exec"), NS)          # definitions, targets, SPACES, RHO, PHI, census
zfc, rbs, B, tic = NS["zfc"], NS["rbs"], NS["B"], NS["tic"]
T6, T9, P094, SIG, SPACES, RHO, PHI = NS["T6"], NS["T9"], NS["P094"], NS["SIG"], NS["SPACES"], NS["RHO"], NS["PHI"]
X, IDX, TASKS = NS["X"], NS["IDX"], NS["TASKS"]
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


# base points in the holomorphic reading (S for every sector, Clebsch 3 by hand)
def six_sall(d):
    di = IDX["dirs"].index(d); Y = X[:, di]
    L = np.concatenate([Y[..., 0:2], Y[..., 4:6], Y[..., 8:10]], axis=-1) * math.log(10)    # up S, down S, lep S
    L[..., 4] += math.log(3); L[..., 5] -= math.log(3)
    return np.max(np.abs(L - T6), axis=-1)


BASE = {}
for r, aa in SPACES.items():
    for a in aa:
        s = np.min(six_sall(f"F_{a}"), axis=1)
        BASE[a] = [tuple(TASKS[int(p)]) for p in np.argsort(s)[:10]]
OUT["base points (S for every sector)"] = {str(a): BASE[a] for a in BASE}


def outs_S(M, hor, Sq, Sl):
    Yu, Yd, Yl = B.coupling(Sq, M[("up", hor)]), B.coupling(Sq, M[("down", hor)]), B.coupling(Sl, M[("lep", hor)])
    o = []
    for Y in (Yu, Yd, Yl):
        s = np.linalg.svd(Y, compute_uv=False); o += [s[1] / s[0], s[2] / s[0]]
    return o + tic.ckm_left(Yu, Yd)


# 2. the corrected covariance control: full sections
mp.mp.dps = 30


def full_section(a, t):
    t2, t3, t4 = zfc.th(t); e = 1 if ((a + 2) // 2) % 4 == 0 else -1
    et = mp.exp(1j * mp.pi * mp.mpc(t) / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * mp.mpc(t) * n) for n in range(1, 300))
    return np.array([complex(et ** (3 - a) * e * t2 ** a), complex(et ** (3 - a) * e * t4 ** a), complex(et ** (3 - a) * 1j * t3 ** a)])


def cov_full(a, b, base, kap):
    k, re_t, im_t = base
    la, lb, _ = zfc.LINES[k]
    M0, M1 = rbs.channels(re_t, im_t, la, lb), rbs.channels(re_t + 1, im_t, la, lb - la)
    Fa0, Fb0 = full_section(a, complex(re_t, im_t)), full_section(b, complex(re_t, im_t))
    Fa1, Fb1 = full_section(a, complex(re_t + 1, im_t)), full_section(b, complex(re_t + 1, im_t))
    dev = 0.0
    for hor in rbs.HORS:
        for St in (False, True):
            f = (lambda S: rbs.St(S)) if St else (lambda S: S)
            q0 = rbs.S_of(Fa0) + kap * rbs.S_of(Fb0); l0 = rbs.S_of(Fa0) - 3 * kap * rbs.S_of(Fb0)
            q1 = rbs.S_of(Fa1) + kap * rbs.S_of(Fb1); l1 = rbs.S_of(Fa1) - 3 * kap * rbs.S_of(Fb1)
            o0, o1 = outs_S(M0, hor, f(q0), f(l0)), outs_S(M1, hor, f(q1), f(l1))
            dev = max(dev, max(abs(math.log(x / y)) for x, y in zip(o0[:9], o1[:9])))
    return dev


base0 = BASE[6][0]
F6n = np.linalg.norm(full_section(6, complex(base0[1], base0[2]))); F18n = np.linalg.norm(full_section(18, complex(base0[1], base0[2])))
kap = 0.05 * np.exp(0.7j) * F6n / F18n
OUT["controls"] = {"full sections, a = 6 with b = 18 (r = 12), kappa fixed": cov_full(6, 18, base0, kap),
                   "full sections, a = 6 with b = 2 (r = 12 with r = 4), kappa fixed": cov_full(6, 2, base0,
                       0.05 * np.exp(0.7j) * F6n / np.linalg.norm(full_section(2, complex(base0[1], base0[2]))))}
say(f"controls (max |delta ln| under tau -> tau + 1, b -> b - a; both readings): {OUT['controls']}")

# 1. the scan, S for every sector
NROW = sum(len(BASE[a]) * (len(SPACES[(2 * a) % 24]) - 1) for a in BASE) * len(RHO) * len(PHI) * len(rbs.HORS)
res = {c: np.zeros((NROW, 10)) for c in (-3, 1)}
meta = []
for a in sorted(BASE):
    partners = [b for b in SPACES[(2 * a) % 24] if b != a]
    for base in BASE[a]:
        k, re_t, im_t = base
        la, lb, _ = zfc.LINES[k]
        M = rbs.channels(re_t, im_t, la, lb)
        Sa = rbs.S_of(zfc.direction(f"F_{a}", re_t, im_t))
        for b in partners:
            Sb = rbs.S_of(zfc.direction(f"F_{b}", re_t, im_t))
            for ir, rho in enumerate(RHO):
                for ip, phi in enumerate(PHI):
                    kp = rho * np.exp(1j * phi)
                    for ih, hor in enumerate(rbs.HORS):
                        n = len(meta); meta.append((a, b, base, ir, ip, ih))
                        for c in (-3, 1):
                            res[c][n] = outs_S(M, hor, Sa + kp * Sb, Sa + c * kp * Sb)
    say(f"a = {a} done")
assert len(meta) == NROW
NS["meta"], NS["LOG"] = meta, LOG                                         # summ and where read these at call time
b0, b1 = src.index("rng = random.Random(1720)"), src.index('OUT["summaries"] = {}')
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[b0:b1], "zero_free_route_b.py", "exec"), NS)       # main's generator, d6, d9, A_, RH, where, summ
summ = NS["summ"]
OUT["summaries"] = {}
for c, Xr in res.items():
    OUT["summaries"][f"S-all c={c} all pairs"] = summ(Xr, np.ones(len(Xr), dtype=bool), f"S-all, Clebsch {c}, all pairs", True)
    for a in sorted(BASE):
        OUT["summaries"][f"S-all c={c} a={a}"] = summ(Xr, NS["A_"] == a, f"   S-all, Clebsch {c}, first line a = {a}", False)
(HERE / "zero_free_route_b_holo.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "zero_free_route_b_holo_run.txt").write_text("\n".join(LOG) + "\n")
