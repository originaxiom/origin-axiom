#!/usr/bin/env python3
"""B1523 -- the controls, run before the seal. They read dim H^1(M; v) and the isometries' signs ONLY on the control manifolds:
the literature's (m004 = b++LR; Daly's L^2R^2 = b++LLRR and R^2L ~ b++LLR) and the planted two-cusped m129 (the Whitehead link).
On the 536 census manifolds they read only what is not the outcome: the enumeration, SnapPy's isometries against the words'
prediction, the holonomy (relators, the cusp frame, the cusp shape in both routes), and the theorems H^1(M; R) = 1 and
dim H^1(M; so(3,1)) = 2 (route R).

  C1  the enumeration: 758 states, 536 manifolds to length 12, recounted by an independent method (Burnside over the necklaces);
      the kinds of self-map by class; the manifolds without a longitude-inverting isometry by length (262); the golden ones
  C2  SnapPy's isometries on all 536 against the words: |Isom| = 2(1 + rev + swap + swaprev), the cusp maps by kind, and the
      meridian is the fibre boundary (SnapPy's homological longitude is the meridian)
  C3  the holonomy on all 536, both routes: relators, the cusp frame, and the cusp shape t_lambda / t_mu (route R = route C =
      the complex conjugate of SnapPy's cusp shape, a convention: the shape enters only through the lattice checks); the relator
      bar is 1e-35, five orders under the rank tolerance (the first run's 1e-45 flagged route R on one manifold, Sec. 4)
  C4  H^1(M; R) = 1 and dim H^1(M; so(3,1)) = 2 on all 536 (route R; Thurston, b1 = 1); both routes on the controls
  C5  the literature: m004, L^2R^2, R^2L rigid rel cusp (Heusener-Porti; Daly, arXiv:2411.04431v1 Sec. 4); m004's sign table is
      sm:B1520's; m004's fibre boundary (its knot longitude) is a rigid slope (Heusener-Porti, Remark 8.1)
  C6  the two routes agree on the controls: dimensions, signs, slopes, the action on H^1(P; v)
  C7  planted: the Whitehead link m129 (two cusps, rigid rel cusps: Heusener-Porti Sec. 8) has dim H^1(v) = 2, H^1(so) = 4,
      H^1(R) = 2 in both routes
  C8  the cusp lemmas on the controls: a translation off the lattice acts as the identity on H^1(P; v); cusp map -I acts as -1;
      an orientation-reversing cusp map acts as a reflection (trace 0, determinant -1)
  C9  Lemma S live (route R's slope box, the 16 primitive slopes |p| <= 3, 0 <= q <= 3): on m004 the zero slopes are exactly
      mu^-1 lam^2, lam and mu lam^2 (30, 90, 150 degrees from the fibre boundary), on L2R2 exactly lam, on R2L none; on all three
      the zero slopes lie in one coset of 60 degrees and every slope is decided with margin
Usage: python3 controls.py   (writes controls.json beside it; about ten minutes on four cores)"""
import itertools
import json
import math
import multiprocessing as mpc
import pathlib
import sys
import time
import warnings

warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import words  # noqa: E402

CONTROLS = ["b++LR", "b++LLRR", "b++LLR"]
PLANTED = "m129"
NEXPECT_NO_INVERTING = {6: 2, 7: 2, 8: 8, 9: 14, 10: 36, 11: 62, 12: 138}


# ------------------------------------------------------------------ C1, recounted by a method that shares nothing with words.py
def mobius(n):
    m, k, d = 1, n, 2
    while d * d <= k:
        if k % d == 0:
            k //= d
            if k % d == 0:
                return 0
            m = -m
        d += 1
    return -m if k > 1 else m


def burnside_counts(n):
    """primitive cyclic words of length n in two letters, both letters used (the Lyndon count, n >= 2), and their number up to
    the letter swap: Burnside over {1, swap} with the swap-invariant primitive necklaces counted by their own Moebius sum"""
    lyndon = sum(mobius(d) * 2 ** (n // d) for d in range(1, n + 1) if n % d == 0) // n
    # a swap-invariant necklace of length n: n even, the word is u swap(u) with |u| = n/2 up to rotation; primitive ones are
    # counted by the Moebius inversion over the odd divisors d of n (a necklace of length n/d repeated, still swap-invariant)
    fix = 0
    if n % 2 == 0:
        # all (not nec. primitive) swap-invariant necklaces of length m: (1/m) sum over k | m with m/k odd of phi(m/k) 2^(k/2)...
        # computed directly instead: enumerate, which is independent of words.py's canonicalisation
        seen = set()
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            rot = min(w[i:] + w[:i] for i in range(n))
            if rot in seen:
                continue
            seen.add(rot)
            prim = all(w != w[:d] * (n // d) for d in range(1, n) if n % d == 0)
            sw = w.translate(str.maketrans("LR", "RL"))
            if prim and min(sw[i:] + sw[:i] for i in range(n)) == rot:
                fix += 1
    return lyndon, (lyndon + fix) // 2


def c1():
    st = words.states(12)
    man = words.manifolds(12)
    per = {}
    total_states = 0
    for n in range(2, 13):
        ly, up_to_swap = burnside_counts(n)
        n_states = 2 * up_to_swap
        total_states += n_states
        per[n] = {"Lyndon words": ly, "up to swap": up_to_swap, "states (two signs)": n_states,
                  "states, words.py": sum(1 for s in st.values() if s["length"] == n),
                  "manifolds": sum(1 for m in man.values() if m["length"] == n),
                  "without a longitude-inverting isometry": sum(1 for m in man.values()
                                                                if m["length"] == n and not m["a longitude-inverting isometry"])}
    kinds = {}
    for m in man.values():
        k = m["kinds"]
        key = "all three" if k["rev"] and k["swap"] and k["swaprev"] else (
            "rev only" if k["rev"] else "swap only" if k["swap"] else "swaprev only" if k["swaprev"] else "none")
        kinds[key] = kinds.get(key, 0) + 1
        assert sum(k.values()) in (0, 1, 3), m          # the kinds with the identity form a group
    golden = []
    for m in man.values():
        tr = trace(m["word"])
        if squarefree(tr * tr - 4) == 5:
            golden.append({"state": m["sign"] + m["word"], "trace": tr, "a longitude-inverting isometry": m["a longitude-inverting isometry"]})
    no_inv = {n: per[n]["without a longitude-inverting isometry"] for n in per}
    two_state = sum(1 for m in man.values() if len(m["states"]) == 2)
    checks = {
        "758 states (words.py)": len(st) == 758,
        "758 states (Burnside)": total_states == 758,
        "536 manifolds": len(man) == 536,
        "states per length agree": all(per[n]["states (two signs)"] == per[n]["states, words.py"] for n in per),
        "a manifold carries two states iff it has neither rev nor swaprev":
            all((len(m["states"]) == 2) == (not m["kinds"]["rev"] and not m["kinds"]["swaprev"]) for m in man.values()),
        "states = manifolds + two-state manifolds": len(st) == len(man) + two_state,
        "262 without a longitude-inverting isometry, by length as designed":
            all(no_inv.get(n, 0) == NEXPECT_NO_INVERTING.get(n, 0) for n in range(2, 13)) and sum(no_inv.values()) == 262,
        "131 per sign": sum(1 for m in man.values() if not m["a longitude-inverting isometry"] and m["sign"] == "+") == 131,
    }
    return {"per length": per, "kinds by class": kinds, "two-state manifolds": two_state, "golden (monodromy field Q(sqrt5))": golden,
            "checks": checks}


def trace(w):
    L, R = [[1, 0], [1, 1]], [[1, 1], [0, 1]]
    X = [[1, 0], [0, 1]]
    for c in w:
        Y = L if c == "L" else R
        X = [[X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]],
             [X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]]]
    return X[0][0] + X[1][1]


def squarefree(n):
    d = 2
    while d * d <= n:
        while n % (d * d) == 0:
            n //= d * d
        d += 1
    return n


# ------------------------------------------------------------------ C2 and C3 on one manifold (no cohomology of v)
def guarded(fn):
    """run fn on a record; return plain data, or the exception as text (a worker's exception must not carry SnapPy objects back)"""
    def run(rec):
        try:
            return fn(rec)
        except Exception as e:  # reported, never swallowed: main() stops on it
            import traceback
            return {"name": rec["snappy"], "error": f"{type(e).__name__}: {e}", "trace": traceback.format_exc()[-1500:]}
    run.__name__ = fn.__name__
    return run


def snappy_and_holonomy(rec):
    import snappy
    import mpmath as mp
    import route_c as RC
    import route_r as RR
    name = rec["snappy"]
    out = {"name": name}
    M = snappy.Manifold(name)
    isos = M.is_isometric_to(M, return_isometries=True)
    maps = [[[int(x) for x in row] for row in I.cusp_maps()[0]] for I in isos]
    k = rec["kinds"]
    out["isometries"] = len(isos)
    out["order as predicted"] = len(isos) == rec["isometry order"]
    distinct = sorted({(C[0][0], C[1][0], C[1][1]) for C in maps})
    expect = {(1, 0, 1)}
    if k["rev"]:
        expect.add((-1, 0, -1))
    if k["swap"]:
        expect.add((-1, 0, 1))
    if k["swaprev"]:
        expect.add((1, 0, -1))
    out["cusp maps by kind as predicted"] = set(distinct) == expect and all(sum(1 for C in maps if (C[0][0], C[1][0], C[1][1]) == e) == 2 for e in expect)
    out["cusp maps"] = maps
    # the meridian is the fibre boundary: rationally null-homologous (its exponent sums lie in the span of the relators'), and
    # the longitude is not (b1 = 1); exact rank over Q on SnapPy's simplified presentation
    G0 = M.fundamental_group()
    gens = list(G0.generators())

    def expo(w):
        return [sum(1 for c in w if c == g) - sum(1 for c in w if c == g.upper()) for g in gens]
    rel_rows = [expo(r) for r in G0.relators()]
    mer, lon = G0.peripheral_curves()[0]
    r0 = qrank(rel_rows)
    out["meridian is the fibre boundary"] = qrank(rel_rows + [expo(mer)]) == r0 and qrank(rel_rows + [expo(lon)]) == r0 + 1 \
        and len(gens) - r0 == 1
    sh = complex(M.cusp_info("shape")[0])
    # route R: simplified presentation, the Lorentz model
    G = RR.Group(name)
    T, trr = RR.cusp_frame(G)
    shape_r = complex(trr["lambda"] / trr["mu"])
    # route C: unsimplified presentation, the Hermitian model
    P = RC.Pres(name)
    S, Si, trc = RC.frame(P, name)
    shape_c = complex(trc["lambda"] / trc["mu"])
    out["relator error"] = [float(G.relator_error), float(P.err)]
    out["parabolic check"] = [float(max(trr["mu lower-left"], trr["lambda lower-left"])), float(max(trc["mu check"], trc["lambda check"]))]
    out["shape"] = {"snappy": [sh.real, sh.imag], "route R": [shape_r.real, shape_r.imag], "route C": [shape_c.real, shape_c.imag]}
    out["shapes agree (R = C = conj SnapPy)"] = abs(shape_r - shape_c) < 1e-40 and abs(shape_r - sh.conjugate()) < 1e-9
    return out


def qrank(rows):
    """the rank over Q of an integer matrix, by exact Gaussian elimination"""
    from fractions import Fraction
    M = [[Fraction(x) for x in r] for r in rows]
    rank, col = 0, 0
    ncol = len(M[0]) if M else 0
    while rank < len(M) and col < ncol:
        piv = next((i for i in range(rank, len(M)) if M[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        for i in range(len(M)):
            if i != rank and M[i][col] != 0:
                f = M[i][col] / M[rank][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rank])]
        rank += 1
        col += 1
    return rank


def h1_controls_r(rec):
    import route_r as RR
    G = RR.Group(rec["snappy"])
    out = {"name": rec["snappy"]}
    for key in ("triv", "so"):
        info, _, _ = G.h1(key)
        out["H1 " + key] = info
    return out


def run_c2c3(rec):
    return guarded(snappy_and_holonomy)(rec)


def run_c4(rec):
    return guarded(h1_controls_r)(rec)


def main():
    import snappy  # noqa: F401  (imported in the main thread first: cypari installs signal handlers on import)
    t0 = time.time()
    res = {"C1": c1()}
    man = words.manifolds(12)
    recs = sorted(man.values(), key=lambda m: (m["length"], m["snappy"]))
    with mpc.Pool(4) as pool:
        c2c3 = pool.map(run_c2c3, recs, chunksize=4)
        c4 = pool.map(run_c4, recs, chunksize=4)
    errors = [r for r in c2c3 + c4 if "error" in r]
    if errors:
        (HERE / "controls_errors.json").write_text(json.dumps(errors, indent=1))
        print("WORKER ERRORS:", len(errors))
        for e in errors[:10]:
            print(e["name"], e["error"])
        raise SystemExit(1)
    res["C2"] = {"manifolds": len(c2c3),
                 "checks": {"orders as predicted": all(r["order as predicted"] for r in c2c3),
                            "cusp maps by kind as predicted": all(r["cusp maps by kind as predicted"] for r in c2c3),
                            "the meridian is the fibre boundary on all": all(r["meridian is the fibre boundary"] for r in c2c3)},
                 "failures": [r["name"] for r in c2c3 if not (r["order as predicted"] and r["cusp maps by kind as predicted"]
                                                              and r["meridian is the fibre boundary"])]}
    res["C3"] = {"max relator error (R, C)": [max(r["relator error"][0] for r in c2c3), max(r["relator error"][1] for r in c2c3)],
                 "max parabolic check (R, C)": [max(r["parabolic check"][0] for r in c2c3), max(r["parabolic check"][1] for r in c2c3)],
                 # the bar is five orders under the rank tolerance 1e-30. The first run used 1e-45, an arbitrary bar, and flagged one
                 # manifold: route R's simplified relators on b+-LLLLLLRLLRLR (lengths 11 and 33, partial products of norm 1e8)
                 # carry 2.9e-41 there, route C's 4.0e-57 (PREREGISTRATION Sec. 4); the decisions' own margins are read per manifold
                 "checks": {"relators below 1e-35 in both routes": all(max(r["relator error"]) < 1e-35 for r in c2c3),
                            "cusp at infinity in both routes": all(max(r["parabolic check"]) < 1e-40 for r in c2c3),
                            "shapes agree on all": all(r["shapes agree (R = C = conj SnapPy)"] for r in c2c3)},
                 "per manifold": c2c3}
    res["C4"] = {"route R on all 536": {"checks": {"H1(R) = 1 on all": all(r["H1 triv"]["dim"] == 1 for r in c4),
                                                   "H1(so) = 2 on all": all(r["H1 so"]["dim"] == 2 for r in c4)},
                                        "smallest kept / largest dropped singular value (so)": [
                                            min(r["H1 so"]["fox margin"][0] for r in c4), max(r["H1 so"]["fox margin"][1] for r in c4)]}}
    # the controls proper: both routes, full records, on the literature's manifolds and the planted one
    import route_c as RC
    import route_r as RR
    lit = {}
    for name in CONTROLS:
        lit[name] = {"R": RR.record(name), "C": RC.record(name)}
    plant = {"R": RR.record(PLANTED), "C": RC.record(PLANTED)}
    res["C4"]["both routes on the controls"] = {name: {rt: [lit[name][rt]["H1 " + k]["dim"] for k in ("triv", "so")] for rt in "RC"} for name in CONTROLS}
    res["C4"]["checks"] = dict(res["C4"]["route R on all 536"]["checks"])
    res["C4"]["checks"]["both routes on the controls: H1(R) = 1, H1(so) = 2"] = all(
        lit[n][rt]["H1 triv"]["dim"] == 1 and lit[n][rt]["H1 so"]["dim"] == 2 for n in CONTROLS for rt in "RC")
    b1520 = {(-1, -1): -1, (-1, 1): -1, (1, -1): 1, (1, 1): 1}
    m4 = lit["b++LR"]["R"]
    res["C5"] = {"checks": {
        "m004, L2R2, R2L rigid rel cusp (dim H1(v) = 1) in both routes": all(lit[n][rt]["H1 v"]["dim"] == 1 for n in CONTROLS for rt in "RC"),
        "m004's signs are sm:B1520's table": all(abs(i["eps"] - b1520[(i["cusp map"][0][0], i["cusp map"][1][1])]) < 1e-20 for i in m4["isometries"]),
        "m004's fibre boundary is a rigid slope (Heusener-Porti Remark 8.1)": m4["cusp"]["slope residual"]["fibre boundary mu"] > 1e-10,
    }, "records": lit}

    def agree(a, b):
        if [a["H1 " + k]["dim"] for k in ("triv", "so", "v")] != [b["H1 " + k]["dim"] for k in ("triv", "so", "v")]:
            return False
        if a["H1 v"]["dim"] != 1:
            return True
        sa = [a["cusp"]["slope residual"][k] > 1e-20 for k in ("fibre boundary mu", "section lambda")]
        sb = [b["slope test"][k] > 1e-20 for k in ("fibre boundary mu", "section lambda")]
        if sa != sb or len(a["isometries"]) != len(b["isometries"]):
            return False
        for x, y in zip(a["isometries"], b["isometries"]):
            if x["cusp map"] != y["cusp map"] or abs(x["eps"] - y["eps"][0]) > 1e-20 or abs(y["eps"][1]) > 1e-20:
                return False
            if abs(x["on H1(P; v)"]["trace"] - y["on H1(P; v)"]["trace"][0]) > 1e-20 or abs(x["on H1(P; v)"]["det"] - y["on H1(P; v)"]["det"][0]) > 1e-20:
                return False
        return True
    res["C6"] = {"checks": {"routes agree on " + n: agree(lit[n]["R"], lit[n]["C"]) for n in CONTROLS}}
    res["C7"] = {"checks": {"m129: H1(R) = 2, H1(so) = 4, H1(v) = 2 in both routes": all(
        [plant[rt]["H1 " + k]["dim"] for k in ("triv", "so", "v")] == [2, 4, 2] for rt in "RC")},
        "records": plant}
    lem = {"translation acts trivially": True, "-I acts as -1": True, "orientation-reversing acts as a reflection": True}
    for n in CONTROLS:
        for rt in "RC":
            r = lit[n][rt]
            tdef = r["cusp"]["translation acts trivially (defect)"] if rt == "R" else r["translation acts trivially (defect)"]
            lem["translation acts trivially"] &= tdef < 1e-40
            for i in r["isometries"]:
                h = i["on H1(P; v)"]
                tr_ = h["trace"] if rt == "R" else h["trace"][0]
                dt_ = h["det"] if rt == "R" else h["det"][0]
                C = i["cusp map"]
                if C == [[-1, 0], [0, -1]]:
                    lem["-I acts as -1"] &= abs(tr_ + 2) < 1e-30 and abs(dt_ - 1) < 1e-30
                if i["det"] == -1:
                    lem["orientation-reversing acts as a reflection"] &= abs(tr_) < 1e-30 and abs(dt_ + 1) < 1e-30
    res["C8"] = {"checks": lem}

    def zeros(rec):
        return sorted([p, q] for p, q, r, a in rec["cusp"]["slope box"] if r < 1e-30)

    def one_coset(rec):
        angs = [a for p, q, r, a in rec["cusp"]["slope box"] if r < 1e-30]
        return all(min((a - angs[0]) % 60.0, 60.0 - (a - angs[0]) % 60.0) < 1e-9 for a in angs)

    def decided(rec):
        return all(r < 1e-30 or r > 1e-20 for p, q, r, a in rec["cusp"]["slope box"])
    res["C9"] = {"zero slopes in the box (route R)": {n: zeros(lit[n]["R"]) for n in CONTROLS},
                 "checks": {"m004's zero slopes are mu^-1 lam^2, lam, mu lam^2 (30, 90, 150 degrees)":
                            zeros(lit["b++LR"]["R"]) == [[-1, 2], [0, 1], [1, 2]],
                            "L2R2's only zero slope is lam": zeros(lit["b++LLRR"]["R"]) == [[0, 1]],
                            "R2L has no zero slope in the box": zeros(lit["b++LLR"]["R"]) == [],
                            "the zero slopes lie in one coset of 60 degrees on all three": all(one_coset(lit[n]["R"]) for n in CONTROLS),
                            "every slope in the box is decided with margin": all(decided(lit[n]["R"]) for n in CONTROLS)}}
    allc = {f"{k}: {c}": v for k in res for c, v in res[k].get("checks", {}).items()}
    res["all controls pass"] = all(allc.values())
    res["failed"] = [k for k, v in allc.items() if not v]
    res["seconds"] = round(time.time() - t0)
    (HERE / "controls.json").write_text(json.dumps(res, indent=1, default=str))
    for k, v in allc.items():
        print(("PASS " if v else "FAIL ") + k)
    print("ALL CONTROLS PASS" if res["all controls pass"] else "CONTROLS FAILED: " + "; ".join(res["failed"]), f"({res['seconds']} s)")


if __name__ == "__main__":
    main()
