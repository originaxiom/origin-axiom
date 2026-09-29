#!/usr/bin/env python3
"""B1399 -- post-run checks on the sealed census (census.json).  They read the run; they decide nothing the seal decides.

(1) The cusps.  For every census member (SnapPy seed 1399, as in the run) and every cusp: SnapPy's cusp shape tau, reduced to the
    fundamental domain of SL(2, Z); its class (hexagonal: |tau| = 1 and |Re tau| = 1/2; square: tau = i; other); whether tau lies in
    Q(sqrt -3); the number of directions in each of the lattice's first six shells, and the index of the sublattice each shell's
    vectors span (0 when they span a line).  In two dimensions the dual lattice is the lattice turned through a right angle and
    rescaled, so these are the Fourier shells the solve reads.  A shell spanning a sublattice of index m makes its function invariant
    under a free Z/m of translations, so chi of its positive set is a multiple of m.
(2) The leading shells, re-read.  For every cusp of every resolved member: the number of directions the pipeline recorded for the
    leading shell must equal the directions of that shell of the cusp's lattice.  A match on every cusp also confirms that the solve
    and SnapPy number the cusps alike.
(3) Where the count can live.  C(v) can be non-zero only at a cusp whose leading shell has three or more directions (a shell of one
    or two directions gives a band, chi = 0, in every direction).  The table: per member, the cusps whose first shell has three or
    more directions (hexagonal cusps), the cusps whose leading shell does, and max |C|.
(4) Reproducibility.  Five members re-run from scratch in this process (the first resolved member with max |C| > 0, two of dimension
    2 with one cusp, one of dimension 2 with three or more cusps, one of dimension 3); every recorded field must come back identical.
(5) For context, outside the census: cube~3.24's four cusps (B1387's member, built as in the banked identity), by the same lattice
    arithmetic.
(6) The parity lemma, directly: B1387's Morse count chi_plus on 40 random shell functions (numpy default_rng(1399)) for each of three
    three-direction shells -- the sqrt(-3) cusp's third shell (index 2), the hexagonal first shell (index 1) and the hexagonal sqrt(3)
    shell (index 3); every value must be a multiple of the index, and each shell must show a non-zero value.
Usage: python3 post_run_checks.py [--no-rerun]"""
import cmath
import importlib.util
import json
import math
import sys
import warnings
from collections import Counter
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("b1399_rank_two_higgs", HERE / "rank_two_higgs.py")
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

RHO = complex(0.5, math.sqrt(3) / 2)


def reduce_tau(tau):
    """tau (Im > 0) moved into |Re tau| <= 1/2, |tau| >= 1 by SL(2, Z)"""
    if tau.imag < 0:
        tau = -tau
    for _ in range(200):
        tau = complex(tau.real - round(tau.real), tau.imag)
        if abs(tau) < 1 - 1e-12:
            tau = -1 / tau
        else:
            return tau
    raise RuntimeError("reduction did not settle")


def classify(t):
    if abs(abs(t) - 1) < 1e-9 and abs(abs(t.real) - 0.5) < 1e-9:
        return "hexagonal"
    if abs(t - 1j) < 1e-9:
        return "square"
    return "other"


def in_q_sqrt_minus_3(t):
    a = Fraction(t.real).limit_denominator(1000)
    b = Fraction(t.imag / math.sqrt(3)).limit_denominator(1000)
    return abs(float(a) - t.real) < 1e-9 and abs(float(b) * math.sqrt(3) - t.imag) < 1e-9, "%s + %s*sqrt(-3)" % (a, b)


def shell_directions(t, nshell=6, N=12):
    """directions (pairs +-k) in the first nshell shells of the lattice Z + t Z, their norms relative to the first, and the index of
    the sublattice each shell's vectors span (0: a line)"""
    shells = {}
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m == 0 and n == 0:
                continue
            shells.setdefault(round(abs(m + n * t), 9), []).append((m, n))
    ks = sorted(shells)[:nshell]
    index = []
    for k in ks:
        minors = [abs(a * d - b * c) for (a, b) in shells[k] for (c, d) in shells[k]]
        index.append(math.gcd(*minors))
    return [len(shells[k]) // 2 for k in ks], [k / ks[0] for k in ks], index


def cusps_of(label=None):
    if label is None:                                                # cube~3.24, as in the banked identity
        R.snappy.set_rand_seed(R.SNAPPY_SEED)
        M = R.HF.member()
    else:
        M = R.manifold(label)
    out = []
    for c, info in enumerate(M.cusp_info()):
        tau = complex(info["shape"])
        t = reduce_tau(tau)
        ok, form = in_q_sqrt_minus_3(t)
        dirs, ratios, index = shell_directions(t)
        out.append(dict(cusp=c, shape=[tau.real, tau.imag], reduced=[t.real, t.imag], cls=classify(t), in_Q_sqrt_minus_3=ok, form=form,
                        shell_directions=dirs, shell_ratios=[round(x, 6) for x in ratios], shell_span_index=index))
    return out


LEMMA_SHELLS = {"sqrt(-3) third shell, index 2": ([(2, 0), (1, 1), (1, -1)], 2),
                "hexagonal first shell, index 1": ([(1, 0), (0, 1), (1, 1)], 1),
                "hexagonal sqrt(3) shell, index 3": ([(1, -1), (2, 1), (1, 2)], 3)}


def parity_lemma(draws=40):
    rng = R.np.random.default_rng(1399)
    out = {}
    for name, (ks, m) in LEMMA_SHELLS.items():
        minors = [abs(a * d - b * c) for (a, b) in ks for (c, d) in ks]
        assert math.gcd(*minors) == m
        vals = Counter()
        for _ in range(draws):
            z = rng.normal(size=3) + 1j * rng.normal(size=3)
            vals[R.HF.chi_plus(list(zip(ks, z)))[0]] += 1
        assert all(v % m == 0 for v in vals) and any(v != 0 for v in vals), (name, vals)
        out[name] = {str(k): n for k, n in sorted(vals.items())}
    return out


def main(rerun=True):
    census = json.load(open(HERE / "census.json"))
    members = census["members"]
    rep = dict(members=[], summary={})
    mismatches, cls_count, first3, lead3 = [], Counter(), Counter(), Counter()
    for m in members:
        cu = cusps_of(m["label"])
        row = dict(label=m["label"], parent=m["parent"], degree=m["degree"], status=m["status"], cusps=cu,
                   hexagonal=[x["cusp"] for x in cu if x["cls"] == "hexagonal"],
                   first_shell_3plus=[x["cusp"] for x in cu if x["shell_directions"][0] >= 3])
        for x in cu:
            cls_count[(m["status"], x["cls"])] += 1
            assert x["in_Q_sqrt_minus_3"], (m["label"], x)
        if m["status"] == "resolved":
            row["maxC"] = m["maxC"]
            row["leading_3plus"] = []
            for c, ld in m["leading"].items():
                x = cu[int(c)]
                want = x["shell_directions"][ld["index"]]
                if want != ld["vectors"]:
                    mismatches.append((m["label"], c, ld, x["shell_directions"]))
                if ld["vectors"] >= 3:
                    row["leading_3plus"].append(int(c))
                    lead3[(x["cls"], ld["index"], x["shell_span_index"][ld["index"]])] += 1
        else:
            row["reason"] = m["reason"]
        first3[(m["status"], len(row["first_shell_3plus"]))] += 1
        rep["members"].append(row)
    res = [r for r in rep["members"] if r["status"] == "resolved"]
    rep["summary"] = dict(
        cusps_by_status_and_class={"%s/%s" % k: v for k, v in sorted(cls_count.items())},
        every_shape_in_Q_sqrt_minus_3=True,
        leading_shell_directions_match_the_lattice=not mismatches, mismatches=mismatches,
        members_by_status_and_number_of_hexagonal_cusps={"%s/%d" % k: v for k, v in sorted(first3.items())},
        resolved_cusps_leading_with_3plus_directions={"%s/shell %d/span index %d" % k: v for k, v in sorted(lead3.items())},
        hexagonal_first_shell_span_index=sorted({x["shell_span_index"][0] for r in rep["members"] for x in r["cusps"] if x["cls"] == "hexagonal"}),
        resolved_members_with_a_3plus_leading_shell=[(r["label"][:24], r["parent"], r["leading_3plus"], r["maxC"]) for r in res if r["leading_3plus"]],
        resolved_nonzero=[(r["label"][:24], r["parent"], r["maxC"]) for r in res if r["maxC"]],
        members_with_hexagonal_cusps=[(r["label"][:24], r["parent"], r["status"], r["hexagonal"], r.get("maxC"), r.get("reason"))
                                      for r in rep["members"] if r["hexagonal"]])
    rep["summary"]["parity lemma: chi values over 40 random shell functions"] = parity_lemma()
    rep["summary"]["cube~3.24 (outside the census)"] = [dict(cusp=x["cusp"], cls=x["cls"], form=x["form"], shell_directions=x["shell_directions"],
                                                            shell_span_index=x["shell_span_index"]) for x in cusps_of(None)]
    if rerun:
        rows = {m["label"]: m for m in members}
        resd = [m for m in members if m["status"] == "resolved"]
        pick = ([m for m in resd if m["maxC"]][:1] + [m for m in resd if m["dim"] == 2 and m["cusps"] == 1][:2]
                + [m for m in resd if m["dim"] == 2 and m["cusps"] >= 3][:1] + [m for m in resd if m["dim"] == 3][:1])
        rr = []
        for m in pick:
            again = R.run_member(R.manifold(m["label"]), expect_dim=m["dim"], label=m["label"])
            again = json.loads(json.dumps(again, default=float))
            keys = ("status", "dim", "maxC", "achievable_g", "g3", "leading", "circles", "V_circle", "positive")
            same = {k: again.get(k) == rows[m["label"]].get(k) for k in keys}
            rr.append(dict(label=m["label"][:24], parent=m["parent"], dim=m["dim"], cusps=m["cusps"], identical=all(same.values()),
                           fields=same, maxC=again.get("maxC"), seconds=again.get("seconds")))
            print("re-run %s (parent %s, dim %d, %d cusps): identical %s, max |C| %s, %ss" % (m["label"][:24], m["parent"], m["dim"],
                  m["cusps"], all(same.values()), again.get("maxC"), again.get("seconds")), flush=True)
        rep["summary"]["reproduced"] = rr
    json.dump(rep, open(HERE / "post_run_checks.json", "w"), indent=1, default=str)
    return rep


if __name__ == "__main__":
    rep = main(rerun="--no-rerun" not in sys.argv)
    print(json.dumps(rep["summary"], indent=1, default=str))
    print("DONE")
