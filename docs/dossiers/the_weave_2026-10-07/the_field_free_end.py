"""W71: the field-free end (P024's second test). On the weave's forced quaternion holonomies, in the audit lane's
registered E8 embedding and (1,1) parent with a complete cusp, every flat end datum of a stated family is scored by
its gapless (slot, channel) pairs: a pair is gapless exactly when its total transition around the cusp is 1 and its
radial drift is 0. The rule (W71_RULE.md) was committed before this script.

  E1  the twists: the lane's nine twists x four spin lines, with no flat datum added
  E2  gauge Wilson lines in the forced holonomies' commutant F4 x SU(2)_w, by peripheral class; the U(1)_em lemma
  E3  R-holonomies, by peripheral class, in the R factors each twist leaves whole
  E4  the model operator d/dt + d + k e^t on [0, T] (Dirichlet at both ends): the second route
  E5  the verdict
  plus the read-outs: the full table, the 16 channels, the model values, the commutant's dimension by characters

Coordinates are W70's (`the_cusp_condensate_charge_map.py`), exact.

Run: python3 the_field_free_end.py  ->  the_field_free_end.json beside it.
"""
import cmath
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.linalg import solveh_banded

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_cusp_condensate_charge_map as CM  # noqa: E402  (W70: the roots, the weights of the 6, the hypercharges)

OUT = HERE / "the_field_free_end.json"
TWISTS = list(itertools.product((-1, 0, 1), repeat=2))
SPINS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
# the lane's slots: twisted spin 2s, chirality sign sigma, R-charges (qA, qB)
SLOT_R = [(1, F(1, 2), 0), (1, F(-1, 2), 0), (-1, 0, F(1, 2)), (-1, 0, F(-1, 2))]
FAM = [CM.ycartan((F(1), F(-1), F(0))), CM.ycartan((F(0), F(1), F(-1)))]
SUB = {"colour": list(CM.COLOUR), "family": FAM, "weak": [CM.WEAK]}


def slots(a, b):
    out = []
    for sigma, qa, qb in SLOT_R:
        two_s = sigma + 2 * (a * qa + b * qb)
        drift = -sigma * (a * qa + b * qb)                    # = 1/2 - s (sigma = +1), 1/2 + s (sigma = -1)
        out.append({"2s": int(two_s), "drift": F(drift), "sigma": sigma, "qA": qa, "qB": qb})
    return out


assert all(CM.dot(r, CM.HQ).denominator == 1 for r in CM.RR)    # p = (-1)^{r.hq} is a sign on every root
CHANNELS = [(r, (-1) ** int(CM.dot(r, CM.HQ)), "root") for r in sorted(CM.RR)] + \
           [(None, 1, "cartan")] * 8


def phase_class(r, q):
    """the class of e^{2 pi i r.X} for the gauge peripheral class q: ('fixed', Fraction mod 1) or ('generic',)"""
    if r is None:
        return ("fixed", F(0))
    kind, data = q
    if kind == "trivial":
        return ("fixed", F(0))
    if kind == "point":                                           # an exact X
        return ("fixed", CM.dot(r, data) % 1)
    vecs = [v for name in data for v in SUB[name]]                # generic X in the span of these directions
    if all(CM.dot(r, v) == 0 for v in vecs):
        return ("fixed", F(0))
    return ("generic",)


def r_phase(slot, rcls, a, b):
    """the R peripheral phase on a slot: ('fixed', Fraction mod 1) or ('generic',); a factor acts only if whole"""
    kind = rcls
    if kind == "none":
        return ("fixed", F(0))
    in_A, in_B = slot["qA"] != 0, slot["qB"] != 0
    whole = (in_A and a == 0) or (in_B and b == 0)
    if not whole:
        return ("fixed", F(0))
    if kind == "quaternion point":
        return ("fixed", F(1, 2))                                 # -1 on every R-doublet
    return ("generic",)


def census(a, b, q, rcls):
    gapless, thresholds, pairs = 0, [], []
    for j, sl in enumerate(slots(a, b)):
        spin = F(1, 2) if sl["2s"] % 2 else F(0)                  # the bounding spin's -1 on half-integer slots
        rp = r_phase(sl, rcls, a, b)
        for idx, (r, eps, kind) in enumerate(CHANNELS):
            gp = phase_class(r, q)
            if gp[0] == "generic" or rp[0] == "generic":
                theta = None                                      # a non-real phase: never periodic
            else:
                theta = ((F(0) if eps == 1 else F(1, 2)) + gp[1] + spin + rp[1]) % 1
            periodic = theta == 0
            if periodic and sl["drift"] == 0:
                gapless += 1
                pairs.append((j, idx))
            elif periodic:
                thresholds.append(sl["drift"] ** 2)
    return gapless, (min(thresholds) if thresholds else None), pairs


def symmetries(q, rcls, a, b):
    kind, data = q
    if kind == "trivial":
        moved = set()
    elif kind == "point":
        moved = {"weak"} if CM.dot(data, CM.WEAK) != 0 else set()
    else:
        moved = set(data)
    weak_broken = "weak" in moved                                 # q_w != 1 needs a non-commuting weak pair
    # Y is block-scalar, so it lies in su(3)_fam: keeping T3 + Y needs the weak holonomies in U(1)_T3 and the F4
    # holonomies in Y's centraliser (colour x the family torus), whose commutators lie in colour
    em_broken = bool(moved & {"weak", "family"})
    r_whole = [f for f, w in (("A", a == 0), ("B", b == 0)) if w]
    return {"colour kept": "colour" not in moved, "weak SU(2) kept": not weak_broken,
            "U(1)_em kept (all six admissible Y)": not em_broken,
            "R-symmetry kept": rcls == "none", "R factors left whole by the twist": r_whole}


def su2_commutant_dim(A, B):
    """dimension of the su(2) elements commuting with both A and B"""
    basis = [np.array([[1j, 0], [0, -1j]]), np.array([[0, 1], [-1, 0]], dtype=complex),
             np.array([[0, 1j], [1j, 0]])]
    cols = [np.concatenate([(A @ X - X @ A).reshape(-1), (B @ X - X @ B).reshape(-1)]) for X in basis]
    M = np.array(cols).T                                          # 8 x 3 (complex)
    return 3 - np.linalg.matrix_rank(np.vstack([M.real, M.imag]), tol=1e-12)


def model_sigma_min(d, k, T, per_unit=4000, cap=200000, iters=400):
    """smallest singular value of u -> u' + (d + k e^t) u on [0, T], u(0) = u(T) = 0, midpoint differences"""
    N = min(int(per_unit * T), cap)
    h = T / N
    tm = (np.arange(N) + 0.5) * h                                 # midpoints
    c = d + k * np.exp(tm)
    lo = -1.0 / h + c / 2.0                                       # coefficient of u_i at midpoint i + 1/2
    hi = 1.0 / h + c / 2.0                                        # coefficient of u_{i+1}
    # A maps interior u_1..u_{N-1} to N midpoints; A^T A is tridiagonal, symmetric positive definite
    diag = hi[:-1] ** 2 + lo[1:] ** 2
    off = hi[1:-1] * lo[1:-1]
    ab = np.zeros((2, N - 1))
    ab[0, 1:] = off
    ab[1, :] = diag

    def apply_A(u):
        full = np.concatenate([[0.0], u, [0.0]])
        return lo * full[:-1] + hi * full[1:]
    x = np.sin(np.pi * np.arange(1, N) / N)
    rq = None
    for _ in range(iters):
        x = solveh_banded(ab, x)
        x /= np.linalg.norm(x)
        new = float(np.linalg.norm(apply_A(x)))
        if rq is not None and abs(new - rq) < 1e-14 * max(new, 1e-300):
            rq = new
            break
        rq = new
    return rq


def commutant_dimension():
    chi_minus = 8 + sum((-1) ** int(CM.dot(r, CM.HQ)) for r in CM.RR)
    chi_g4 = 8 + sum(cmath.exp(1j * math.pi / 2 * float(CM.dot(r, CM.HQ))) for r in CM.RR)
    return chi_minus, chi_g4, (248 + chi_minus + 6 * chi_g4) / 8


def main():
    out = {"status": "W71: the field-free end (the rule W71_RULE.md first; one run)"}
    # E1: the twists, no flat datum, all four spin lines (they enter only through the bounding factor)
    e1 = {}
    drift_ok = True
    pairs_ok = True
    for a, b in TWISTS:
        rows = []
        for _ in SPINS:
            g, thr, pairs = census(a, b, ("trivial", None), "none")
            rows.append(g)
            for j, idx in pairs:
                pairs_ok &= slots(a, b)[j]["2s"] in (1, -1) and CHANNELS[idx][1] == -1
        drift_ok &= all((sl["drift"] == 0) == (sl["2s"] in (1, -1)) for sl in slots(a, b))
        e1[f"{a},{b}"] = {"gapless per spin line": rows, "smallest positive threshold": str(thr)}
    want = {k: ([448] * 4 if k == "0,0" else [224] * 4 if k.count("0") == 1 else [0] * 4) for k in e1}
    e1_holds = all(e1[k]["gapless per spin line"] == want[k] for k in e1) and drift_ok and pairs_ok
    out["E1"] = {"per twist": e1, "drift 0 exactly on untwisted slots": drift_ok,
                 "every gapless pair is an untwisted slot on a p-odd channel": pairs_ok, "holds": bool(e1_holds)}
    # E2: gauge Wilson lines, untwisted, no R datum
    qclasses = {"trivial": ("trivial", None), "generic in the family torus": ("generic", ["family"]),
                "generic in F4's torus": ("generic", ["colour", "family"]),
                "q_w = -1": ("point", CM.scale(CM.WEAK, F(1, 2))), "generic weak": ("generic", ["weak"]),
                "generic in the whole torus": ("generic", ["colour", "family", "weak"])}
    e2, sixteen = {}, None
    for name, q in qclasses.items():
        g, thr, pairs = census(0, 0, q, "none")
        e2[name] = {"gapless": g, "smallest positive threshold": str(thr), **symmetries(q, "none", 0, 0)}
        if name == "generic in the family torus":
            sixteen = sorted({CHANNELS[idx][0] for j, idx in pairs})
    sixteen_ok = (sixteen is not None and len(sixteen) == 16
                  and all(CM.colour(r) == (0, 0) and abs(CM.dot(r, CM.WEAK)) == 1 for r in sixteen))
    blocks_ok = True
    rows16 = []
    adm = [tuple(F(x) for x in y) for y in json.loads(
        (HERE / "the_cusp_condensate_charge_map.json").read_text(encoding="utf-8"))["N2"]["admissible"]]
    for r in sixteen or []:
        v = [CM.dot(r, w) for w in CM.WS]
        S = tuple(j for j in range(6) if v[j] == F(1, 2))
        blocks_ok &= len(S) == 3 and sorted(j // 2 for j in S) == [0, 1, 2]
        rows16.append({"root": [str(x) for x in r], "SU(6) indices": S, "T3": str(CM.dot(r, CM.WEAK) / 2),
                       "Y under each admissible": [str(CM.dot(r, CM.ycartan(y))) for y in adm]})
    # the lemma: a non-commuting pair in SU(2) has zero commutant in su(2); Y has no weak component
    A = np.array([[1j, 0], [0, -1j]])
    B = np.array([[0, 1], [-1, 0]], dtype=complex)
    rng = np.random.default_rng(71)
    lemma_dims = [su2_commutant_dim(A, B)]
    for _ in range(5):
        def rand_su2():
            v = rng.normal(size=4)
            v /= np.linalg.norm(v)
            return np.array([[v[0] + 1j * v[1], v[2] + 1j * v[3]], [-v[2] + 1j * v[3], v[0] - 1j * v[1]]])
        lemma_dims.append(su2_commutant_dim(rand_su2(), rand_su2()))
    y_weak = [str(CM.dot(CM.ycartan(y), CM.WEAK)) for y in adm]
    e2_want = {"trivial": 448, "generic in the family torus": 64, "generic in F4's torus": 64, "q_w = -1": 0,
               "generic weak": 0, "generic in the whole torus": 0}
    zero_breaks = all(not e2[n]["U(1)_em kept (all six admissible Y)"] for n in e2 if e2[n]["gapless"] == 0)
    e2_holds = (all(e2[n]["gapless"] == e2_want[n] for n in e2) and sixteen_ok and blocks_ok
                and all(d == 0 for d in lemma_dims) and all(x == "0" for x in y_weak) and zero_breaks)
    out["E2"] = {"per class": e2, "the 16 are colour-singlet weak doublets": sixteen_ok,
                 "one SU(6) index per block": blocks_ok,
                 "su(2) commutant of non-commuting pairs (the lemma)": [int(d) for d in lemma_dims],
                 "Y's weak component, per admissible Y": y_weak,
                 "Y in the family Cartans' span (read-out)": all(
                     CM.ycartan(y) == CM.add(CM.scale(FAM[0], y[0]), CM.scale(FAM[1], y[0] + y[1])) for y in adm),
                 "every count-0 class breaks U(1)_em": zero_breaks, "holds": bool(e2_holds)}
    # E3: R-holonomies
    e3 = {}
    for a, b in TWISTS:
        for rcls in ("none", "quaternion point", "generic"):
            g, thr, _ = census(a, b, ("trivial", None), rcls)
            e3[f"{a},{b} / {rcls}"] = {"gapless": g, "smallest positive threshold": str(thr),
                                       **symmetries(("trivial", None), rcls, a, b)}
    e3_holds = (e3["0,0 / generic"]["gapless"] == 0 and e3["0,0 / generic"]["colour kept"]
                and e3["0,0 / generic"]["weak SU(2) kept"] and e3["0,0 / quaternion point"]["gapless"] == 544
                and e3["1,0 / generic"]["gapless"] == 0 and e3["-1,0 / generic"]["gapless"] == 0
                and e3["1,1 / generic"]["gapless"] == 0
                and e3["1,1 / generic"]["R factors left whole by the twist"] == [])
    out["E3"] = {"per twist and R class": e3, "holds": bool(e3_holds)}
    # E4: the model operator
    model = {}
    classes = {"k=0, d=0": (0.0, 0.0), "k=0, d=+1/2": (0.5, 0.0), "k=0, d=-1/2": (-0.5, 0.0),
               "k=0, d=+1": (1.0, 0.0), "k=0, d=-1": (-1.0, 0.0),
               "theta=1/2, d=0": (0.0, 2 * math.pi * 0.5), "theta=1/4, d=0": (0.0, 2 * math.pi * 0.25)}
    e4_ok = True
    for name, (d, k) in classes.items():
        vals = {}
        for T in (10, 20, 40):
            s = model_sigma_min(d, k, T)
            vals[str(T)] = s
            if k == 0:
                exact = math.sqrt((math.pi / T) ** 2 + d ** 2)
                e4_ok &= abs(s - exact) / exact < 0.01
        if k != 0:
            e4_ok &= abs(vals["40"] - vals["20"]) / vals["20"] < 0.01 and vals["40"] > 0.1
        model[name] = vals
    out["E4"] = {"smallest singular values": model, "holds": bool(e4_ok)}
    # E5: the verdict
    gauge_only_em = [n for n in e2 if e2[n]["U(1)_em kept (all six admissible Y)"] and e2[n]["gapless"] == 0]
    field_free_gaps = sorted([f"twist {k}" for k in e1 if e1[k]["gapless per spin line"] == [0] * 4]
                             + [f"gauge {n}" for n in e2 if e2[n]["gapless"] == 0]
                             + [f"R {k}" for k in e3 if e3[k]["gapless"] == 0 and not k.endswith("none")])
    e5_holds = bool(field_free_gaps and not gauge_only_em and e2["generic in F4's torus"]["gapless"] == 64
                    and e1["1,1"]["gapless per spin line"] == [0] * 4 and e3["0,0 / generic"]["gapless"] == 0)
    out["E5"] = {"field-free data that gap every channel": field_free_gaps,
                 "gauge-only classes that gap every channel and keep U(1)_em": gauge_only_em, "holds": e5_holds}
    out["cells"] = {k: out[k]["holds"] for k in ("E1", "E2", "E3", "E4", "E5")}
    chi_m, chi_4, dim_c = commutant_dimension()
    out["read-outs"] = {"the 16 channels": rows16,
                        "the commutant by characters": {"chi(-1)": chi_m, "chi(g4)": [chi_4.real, chi_4.imag],
                                                        "dimension": [dim_c.real, dim_c.imag]}}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
