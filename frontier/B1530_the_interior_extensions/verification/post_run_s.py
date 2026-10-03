#!/usr/bin/env python3
"""B1530 post-run check S (written after run_a.py had read its outcome on m135; disclosed in FINDINGS): a state's characters
of order dividing twelve read on SnapPy's own presentation and SnapPy's own holonomy.

Why.  Routes E and N share two inputs: the group (family_lib.word_group, the bundle presentation <a, b, t>, with its cusp
words abAB and abt) and the hyperbolic point (sm:B1529's exact record and family_lib's seeded solve, both on that
presentation).  Routes T, G, N and W of Part B and post_run_b.py share the same two.  A slip in either would reach every
route alike.  Route S takes both from SnapPy instead: the bundle b+<sign><word> (SnapPy's name for <sign><word>; its
identify() is recorded), SnapPy's simplified presentation of its fundamental group and its peripheral curves, and its
polished holonomy at 256 bits (PSL(2, C): the four is blind to the sign).  The four is X -> g X g^* on M_2(C).

The characters are every nu: pi_1 -> mu_12, found by solving the relators' exponent sums mod 12.  kappa is read without the
fibration: the fibre's boundary is the peripheral class that dies in H_1(M; Z), nu is 1 on it, and nu(P) = <kappa>; so the
order of kappa is the order of nu(P) (kappa = 1, -1; +-i and omega, omega^2 are each read up to inversion, the orientation of
t' not being fixed here).  B1515's frame: V = nu (x) rho, V_eta = nu^5 (x) rho, L = nu^-4; a member is nu with
h^1(V_eta) >= 1, read at every class of an orthonormal basis of the interior classes, at the sum of the basis, and (kappa = 1)
at the boundary-type classes and their sums with the interior class.  The readings use route N's numerical classes and
sm:B1527's cusp_lib class index (the code that routes E and N already cross-check); what route S adds is an independent
group, cusp and point.
Compared, as multisets (the two presentations are not matched character by character):
  - at kappa = 1 on -LLRR, with run_a.json's eight rows;
  - the characters with h^1(nu (x) rho) >= 1 at kappa of order 2, 3 or 4, with census_bc's route-T hits on the state;
  - the kappa = -1 members' readings, with post_run_b.jsonl's rows on the state.
Usage: python3 post_run_s.py [STATE]   (default -LLRR) -> post_run_s_<m|p><word>.json and _log.txt"""
import itertools
import json
import sys
import time
import warnings
from datetime import datetime, timezone
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402

import route_n as N  # noqa: E402

mp.mp.dps = 60
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def to_mp(z):
    return mp.mpc(mp.mpf(str(z.real())), mp.mpf(str(z.imag())))


def snappy_group(state):
    import snappy
    name = "b+" + state[0] + state[1:]
    M = snappy.Manifold(name)
    ident = [str(x) for x in M.identify()]
    sol = M.solution_type()
    assert sol == "all tetrahedra positively oriented", sol
    assert M.num_cusps() == 1
    G0 = M.polished_holonomy(bits_prec=256, lift_to_SL2=False)      # PSL(2, C): the four is blind to the sign
    gens = list(G0.generators())
    rels = list(G0.relators())
    mer, lon = G0.peripheral_curves()[0]
    sl2 = {}
    for g in gens:
        m = G0.SL2C(g)
        sl2[g] = mp.matrix([[to_mp(m[0, 0]), to_mp(m[0, 1])], [to_mp(m[1, 0]), to_mp(m[1, 1])]])
    # SnapPy's words multiply left to right, as cusp_lib's do (checked up to sign on one word)
    w = "".join(gens) + gens[0].upper()
    mw = G0.SL2C(w)
    X = mp.eye(2)
    for c in w:
        X = X * (sl2[c] if c.islower() else mp.inverse(sl2[c.lower()]))
    conv = min(max(abs(to_mp(mw[i, j]) - e * X[i, j]) for i in range(2) for j in range(2)) for e in (1, -1))
    info = {"name": name, "identify": ident, "solution type": str(sol), "volume": str(M.volume()),
            "homology": str(M.homology()), "generators": gens, "relators": rels, "peripheral (meridian, longitude)":
            [mer, lon], "product convention residual": mp.nstr(conv, 3)}
    return gens, rels, (mer, lon), sl2, info


def four(g):
    """X -> g X g^* on M_2(C), basis E11, E12, E21, E22"""
    gh = g.H
    F = mp.matrix(4, 4)
    for k in range(4):
        E = mp.matrix(2, 2)
        E[k // 2, k % 2] = 1
        Y = g * E * gh
        for m in range(4):
            F[m, k] = Y[m // 2, m % 2]
    return F


def exponent_sums(w, gens):
    return [w.count(g) - w.count(g.upper()) for g in gens]


def characters(gens, rels, n):
    """every nu: pi_1 -> mu_n, as exponent vectors k (nu(g) = e^{2 pi i k_g / n})"""
    E = [exponent_sums(r, gens) for r in rels]
    return [k for k in itertools.product(range(n), repeat=len(gens))
            if all(sum(e * x for e, x in zip(row, k)) % n == 0 for row in E)]


def homology_class(w, gens, rels):
    """is the word null-homologous over Z?  Its exponent vector in the Z-span of the relators' exponent vectors: the
    relator vectors are independent here (H_1 of rank one, as many relators as generators less one), so the rational
    solution is unique and the word is null-homologous iff that solution is integral"""
    import sympy
    R = sympy.Matrix([exponent_sums(r, gens) for r in rels]).T          # columns: relators
    assert R.rank() == R.cols
    v = sympy.Matrix(exponent_sums(w, gens))
    try:
        x, params = R.gauss_jordan_solve(v)
    except ValueError:
        return False
    assert params.shape[0] == 0
    return all(sympy.Rational(c).q == 1 for c in x)


def kappa_class(k, mer, lon, gens, n):
    """the order of nu(P) = <kappa>, from nu on the meridian and the longitude: '1', '-1', '+-i', 'omega', 'order 6', ..."""
    import math
    vals = [sum(e * x for e, x in zip(exponent_sums(w, gens), k)) % n for w in (mer, lon)]
    order = n // math.gcd(math.gcd(vals[0], vals[1]), n)
    return {1: "1", 2: "-1", 4: "+-i", 3: "omega"}.get(order, f"order {order}"), vals


KNAME = {"-1": "-1", "i": "+-i", "-i": "+-i", "omega": "omega", "omega^2": "omega"}


def pair(r):
    return (r["I(W)"], r["I(L2W)"])


def main():
    t0 = time.time()
    state = sys.argv[1] if len(sys.argv) > 1 else "-LLRR"
    tag = ("p" if state[0] == "+" else "m") + state[1:]
    n = 12
    say(f"B1530 post-run check S on {state}, {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    gens, rels, (mer, lon), sl2, info = snappy_group(state)
    say(f"SnapPy: {info['name']} = {info['identify']}, {info['solution type']}, volume {info['volume']}, H_1 "
        f"{info['homology']}; generators {gens}, relators {rels}, cusp {[mer, lon]}; product convention residual "
        f"{info['product convention residual']}")
    L = N.lib()
    G = L.Group(gens, rels, (mer, lon), f"{state} (SnapPy)")
    rho = L.Module({g: four(sl2[g]) for g in gens})
    res_rel = L.relator_residual(G, rho)
    res_cusp = L.cusp_commutator_residual(G, rho)
    # the fibre's boundary: the primitive peripheral class that dies in H_1(M; Z)
    dead = {w: homology_class(w, gens, rels) for w in (mer, lon, mer + lon, mer + lon.upper())}
    info["null-homologous peripheral words"] = [w for w, v in dead.items() if v]
    say(f"the four: relator residual {mp.nstr(res_rel, 3)}, cusp commutator residual {mp.nstr(res_cusp, 3)}; "
        f"null-homologous among m, l, ml, mL: {info['null-homologous peripheral words']}")
    chars = characters(gens, rels, n)
    say(f"characters nu: pi_1 -> mu_{n}: {len(chars)}")
    zeta = [mp.expjpi(mp.mpf(2 * j) / n) for j in range(n)]
    # h^1(nu (x) rho) at every character
    h1 = {}
    for k in chars:
        h1[k] = N.Classes(G, L.Module({g: zeta[x] * rho.M[g] for g, x in zip(gens, k)})).h1
    rows = []
    for k in chars:
        kc, pv = kappa_class(k, mer, lon, gens, n)
        k5 = tuple((5 * x) % n for x in k)
        row = {"nu (exponents of zeta_12 on the generators)": list(k), "kappa": kc, "nu on (meridian, longitude)": pv,
               "h1(nu (x) rho)": h1[k], "h1(V_eta)": h1[k5], "W1": {}}
        if h1[k5] >= 1:                                           # a member
            t1 = time.time()
            V = L.Module({g: zeta[x] * rho.M[g] for g, x in zip(gens, k)})
            Veta = L.Module({g: zeta[x] * rho.M[g] for g, x in zip(gens, k5)})
            lval = {g: zeta[(-4 * x) % n] for g, x in zip(gens, k)}
            trivial_L = all(abs(v - 1) < mp.mpf(10) ** -40 for v in lval.values())
            C = N.Classes(G, Veta)
            ints = C.interior()
            row["case"] = "(a)" if trivial_L else "(b)"
            row["interior"] = ints.cols
            zs = {f"interior {c}": ints[:, c] for c in range(ints.cols)}
            if ints.cols >= 2:
                sm = ints[:, 0]
                for c in range(1, ints.cols):
                    sm = sm + ints[:, c]
                zs["the sum of the interior basis"] = sm
            bt = C.boundary_type(ints)
            row["boundary-type"] = bt.cols
            for c in range(bt.cols):
                zs[f"boundary {c}"] = bt[:, c]
                if ints.cols:
                    zs[f"boundary {c} + interior 0"] = bt[:, c] + ints[:, 0]
                    zs[f"boundary {c} - interior 0"] = bt[:, c] - ints[:, 0]
            for name, z in zs.items():
                W1 = N.extension(V, z, gens, None if trivial_L else lval)
                r = N.reading(G, W1)
                row["W1"][name] = {"I(W)": r["I(W)"], "I(L2W)": r["I(L2W)"], "checks": r["checks"],
                                   "margins": r["margins"], "relator residual": r["relator residual"]}
            row["margins (classes)"] = C.mg.as_dict()
            row["seconds"] = round(time.time() - t1)
            say(f"  member nu {list(k)}: kappa {kc}, case {row['case']}, h1(V_eta) {h1[k5]}, interior {ints.cols}; W1 "
                f"{ {nm: pair(v) for nm, v in row['W1'].items()} } ({row['seconds']} s)")
        rows.append(row)
    out = {"state": state, "SnapPy": info,
           "the four": {"relator residual": mp.nstr(res_rel, 3), "cusp commutator residual": mp.nstr(res_cusp, 3)},
           "characters": len(chars),
           "by kappa": {kc: sum(1 for r in rows if r["kappa"] == kc) for kc in sorted({r["kappa"] for r in rows})},
           "rows": rows, "comparisons": {}}
    cmp_ = out["comparisons"]
    # (1) kappa = 1 on -LLRR, with run_a.json
    if state == "-LLRR":
        A = json.loads((HERE / "run_a.json").read_text())

        def a_profile(r):
            E_ = r["route E"]
            ints_ = [pair(v) for nm, v in E_["W1"].items() if nm in ("c_int",)]
            return (E_["h1"]["V"], E_["n"]["V_eta"], tuple(sorted(ints_)),
                    tuple(sorted({pair(v) for v in E_["W1"].values()})))

        def s_profile(r):
            ints_ = [pair(v) for nm, v in r["W1"].items() if nm == "interior 0"]
            return (r["h1(V_eta)"], r.get("interior", 0), tuple(sorted(ints_)),
                    tuple(sorted({pair(v) for v in r["W1"].values()})))
        a_prof = sorted(a_profile(r) for r in A["rows"])
        s_prof = sorted(s_profile(r) for r in rows if r["kappa"] == "1")
        cmp_["kappa = 1 with run_a (h1, interior, interior reading, all readings)"] = {
            "route S": s_prof, "run_a": a_prof, "agree": s_prof == a_prof}
        say(f"kappa = 1 against run_a: agree {s_prof == a_prof}")
    # (2) population B's characters, with census_bc's route-T hits on the state
    src = HERE / "census_bc.json"
    recs = (json.loads(src.read_text())["records"] if src.exists()
            else [json.loads(x) for x in (HERE / "census_bc.jsonl").read_text().splitlines()])
    rec = [r for r in recs if r["state"] == state and "error" not in r]
    if rec:
        t_hits = sorted((KNAME[h[2]], h[3]) for h in rec[0]["B"]["route T: h1 >= 1 at"])
        s_hits = sorted((r["kappa"], r["h1(nu (x) rho)"]) for r in rows
                        if r["kappa"] in ("-1", "+-i", "omega") and r["h1(nu (x) rho)"] >= 1)
        cmp_["population B characters with h1 >= 1 (kappa class, h1)"] = {"route S": s_hits, "route T": t_hits,
                                                                           "agree": s_hits == t_hits}
        say(f"population B characters: route S {s_hits}; route T {t_hits}; agree {s_hits == t_hits}")
    # (3) the kappa = -1 members' readings, with post_run_b.jsonl
    pb = HERE / "post_run_b.jsonl"
    if pb.exists():
        b_rows = [json.loads(x) for x in pb.read_text().splitlines()]
        b_read = sorted(tuple(v["route N"]) for r in b_rows if r["state"] == state for v in r["readings"].values()
                        if True)
        s_read = sorted(pair(v) for r in rows if r["kappa"] == "-1" for nm, v in r["W1"].items()
                        if nm.startswith("interior") or nm == "the sum of the interior basis")
        # post_run_b reads the basis and the sum (which for one class is the class again); route S reads the basis, and the
        # sum only when the basis has two or more classes: compare the sets of readings
        cmp_["kappa = -1 members' readings (as sets)"] = {"route S": sorted(set(s_read)), "post_run_b (route N)":
                                                         sorted(set(b_read)), "agree": set(s_read) == set(b_read),
                                                         "members (route S)": sum(1 for r in rows if r["kappa"] == "-1"
                                                                                  and r["W1"])}
        say(f"kappa = -1 members' readings: route S {sorted(set(s_read))}; post_run_b {sorted(set(b_read))}")
    gen_shaped = [(r["nu (exponents of zeta_12 on the generators)"], r["kappa"], nm, pair(v)) for r in rows
                  for nm, v in r["W1"].items() if pair(v)[0] == pair(v)[1] != 0]
    out["generation-shaped readings"] = gen_shaped
    out["all checks"] = all(v["checks"] for r in rows for v in r["W1"].values())
    out["all comparisons agree"] = all(c["agree"] for c in cmp_.values())
    out["seconds"] = round(time.time() - t0)
    say(f"generation-shaped readings: {gen_shaped}")
    say(f"all identity checks: {out['all checks']}; all comparisons agree: {out['all comparisons agree']} "
        f"({out['seconds']} s)")
    (HERE / f"post_run_s_{tag}.json").write_text(json.dumps(out, indent=1, default=str))
    (HERE / f"post_run_s_{tag}_log.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
