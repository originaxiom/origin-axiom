#!/usr/bin/env python3
"""B1530 read-out: the sealed predictions (PREREGISTRATION section 7) read from run_a.json and census_bc.json.  Written and
committed with PREREGISTRATION.md before either instrument read any outcome.  Writes read_out.json and prints it.

P1  Lemma A: I(W1) = -1 at c_int at both of m135's non-simple members, both routes.
P2  the question at m135: (I(W1), I(Lambda^2 W1)) = (-1, -1) at c_int, both routes, both members (generation-shaped).
P3  Lemmas C and D: at the boundary-type classes I(W1) is one value, equal to [Jordan type (3, 1)], and no boundary-type class is
    generation-shaped (both routes).
P4  Lemma 8: m135's six simple members read (0, 0), both routes.
P5  Lemma M: W2 reads -W1 at corresponding classes at all eight characters (interior to interior; a boundary-type c' to one of
    the boundary-type readings).
P6  population B at kappa = -1 is empty: no character nu at kappa = -1 with h^1(nu^5 (x) rho) >= 1, on any word state or level,
    by routes T and G.
P7  Part C: Lambda_A meet pi_A = 0 at every chi = nu^2 (kappa = 1), by rank and by pairing, everywhere.
P8  the mechanism at m135: x cup c_int = 0, and c_int lifts, at both members.
G   every state carrying a generation-shaped member is golden (|trace| in {3, 7, 18, 47, 123, 322}); vacuous if there is none.
The verdict rule (section 9): PROVED if P2 holds with the routes agreeing; NEGATIVE if P2 fails, no kappa = -1 member is
generation-shaped, and P7 holds; otherwise withheld until the members named are read (post_run_b.py, disclosed)."""
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

GOLDEN = {3, 7, 18, 47, 123, 322}


def pair(r):
    return (r["I(W)"], r["I(L2W)"])


def neg(p):
    return (-p[0], -p[1])


def gen_shaped(p):
    return p[0] == p[1] != 0


def part_a(A):
    nonsimple = [r for r in A["rows"] if not r["route E"]["simple"]]
    simple = [r for r in A["rows"] if r["route E"]["simple"]]
    out = {"non-simple members": [r["u"] for r in nonsimple], "simple members": len(simple),
           "routes agree everywhere": A["routes agree everywhere"]}
    p1 = p2 = p3 = p8 = len(nonsimple) == 2
    p5 = True
    gens = []
    bnames = ("c_b", "c_b + c_int", "c_b - c_int", "c_b + 2 c_int")
    for r in nonsimple:
        E_, N_ = r["route E"], r["route N"]
        ci_e, ci_n = pair(E_["W1"]["c_int"]), pair(N_["W1"]["c_int"])
        p1 &= ci_e[0] == -1 and ci_n[0] == -1
        p2 &= ci_e == (-1, -1) and ci_n == (-1, -1)
        jt = E_["mechanism (route E)"]["Jordan type of S0 on C at 1"]
        b_e = {pair(E_["W1"][k]) for k in bnames}
        b_n = {pair(N_["W1"][k]) for k in bnames if k in N_["W1"]}
        w1_values = {p[0] for p in b_e | b_n}
        p3 &= len(w1_values) == 1 and w1_values == {1 if jt == [3, 1] else 0} and not any(gen_shaped(p) for p in b_e | b_n)
        mech = E_["mechanism (route E)"]
        p8 &= mech.get("x cup c_int = 0") is True and mech.get("c_int lifts") is True
        # P5: interior to interior; boundary-type c' to the negated boundary-type readings
        p5 &= pair(E_["W2"]["c'_int"]) == neg(ci_e)
        negb = {neg(p) for p in b_e}
        p5 &= all(pair(E_["W2"][k]) in negb for k in ("c'_b", "c'_b + c'_int"))
        for cls, p in list(E_["W1"].items()) + [(k, pair(v)) for k, v in N_["W1"].items()]:
            pp = p if isinstance(p, tuple) else pair(p)
            if gen_shaped(pp):
                gens.append({"u": r["u"], "class": cls, "reading": list(pp)})
        out[f"u = {tuple(r['u'])}"] = {"c_int": {"E": ci_e, "N": ci_n}, "boundary-type": sorted(b_e | b_n),
                                       "W2": {k: pair(v) for k, v in E_["W2"].items()}, "Jordan type": jt,
                                       "mechanism": mech}
    p4 = len(simple) == 6
    for r in simple:
        E_, N_ = r["route E"], r["route N"]
        pe, pn = pair(E_["W1"]["the class"]), pair(N_["W1"]["the class"])
        p4 &= pe == (0, 0) and pn == (0, 0)
        p5 &= pair(E_["W2"]["the class"]) == neg(pe)
        if gen_shaped(pe) or gen_shaped(pn):
            gens.append({"u": r["u"], "class": "the class", "reading": [list(pe), list(pn)]})
    out["generation-shaped readings"] = gens
    return out, {"P1": p1, "P2": p2, "P3": p3, "P4": p4, "P5": p5, "P8": p8}, gens


def fifth_powers(state_read_as):
    """the fibre characters u' = 5u (u a torsion character fixed by phi) of a state"""
    import exact_states as S
    FL = S.family()
    sign, word = state_read_as[0], state_read_as[1:]
    G, img = FL.word_group(sign, word)
    chars, D = FL.torsion_characters(img)
    return {((5 * u[0]) % 1, (5 * u[1]) % 1) for u in chars}


def part_bc(BC):
    out = {"manifolds": BC["manifolds"], "errors": len(BC["errors"])}
    hits = BC["B"]["route T: characters with h1 >= 1 at kappa != 1"]
    recs = {r["state"]: r for r in BC["records"]}
    members = {k: [] for k in ("-1", "i", "-i", "omega", "omega^2")}
    # nu at kappa is a member iff nu^5 is a hit: nu^5 has fibre part 5u and twist kappa^5
    k5 = {"-1": "-1", "i": "i", "-i": "-i", "omega": "omega^2", "omega^2": "omega"}
    by_state = {}
    for h in hits:
        state, golden, ua, ub, kname, g = h
        by_state.setdefault(state, []).append((Fraction(ua), Fraction(ub), kname, g))
    for state, hs in by_state.items():
        fp = fifth_powers(recs[state]["read as"])
        for ua, ub, kname, g in hs:
            if (ua, ub) in fp:
                kappa_member = [k for k, v in k5.items() if v == kname][0]
                members[kappa_member].append([state, recs[state]["golden"], str(ua), str(ub), kname, g])
    out["route T hits at kappa != 1"] = len(hits)
    out["members (nu^5 a hit)"] = {k: len(v) for k, v in members.items()}
    out["members at kappa = -1"] = members["-1"]
    out["members at other kappa (Lemma 5: not generation-shaped)"] = {k: v for k, v in members.items() if k != "-1"}
    out["route G at kappa = -1"] = BC["B"]["route G at kappa = -1, all characters"]
    out["B disagreements"] = BC["B"]["disagreements"]
    out["H0(F) != 0"] = BC["B"]["H0(F) != 0"]
    C = BC["C"]
    out["C"] = {k: (len(v) if isinstance(v, list) else v) for k, v in C.items()}
    p6 = not members["-1"] and not BC["B"]["disagreements"] and not BC["errors"]
    p7 = (not C["meet != 0 (rank)"] and not C["meet != 0 (pairing)"] and not C["dims not (2, 2)"]
          and not C["rank and pairing disagree"] and not BC["errors"])
    return out, {"P6": p6, "P7": p7}, members


def main():
    A = json.loads((HERE / "run_a.json").read_text())
    BC = json.loads((HERE / "census_bc.json").read_text())
    a_out, a_p, gens = part_a(A)
    bc_out, bc_p, members = part_bc(BC)
    preds = {**a_p, **bc_p}
    golden_of = {r["state"]: r["golden"] for r in BC["records"] if "golden" in r}
    gen_states = sorted({"-LLRR"} if gens else set())
    if members["-1"]:
        b_file = HERE / "post_run_b.json"
        if b_file.exists():
            for m in json.loads(b_file.read_text()).get("generation-shaped", []):
                gen_states = sorted(set(gen_states) | {m["state"]})
    preds["G"] = all(golden_of.get(s, False) for s in gen_states)
    agree = A["routes agree everywhere"] and not BC["B"]["disagreements"] and not BC["C"]["rank and pairing disagree"]
    if not agree:
        verdict = "WITHHELD: the routes disagree (ERROR_LEDGER first)"
    elif preds["P2"]:
        verdict = "PROVED: m135's interior class is generation-shaped (both routes)"
    elif members["-1"] and not (HERE / "post_run_b.json").exists():
        verdict = "PENDING: kappa = -1 members to read (post_run_b.py)"
    elif preds["P7"] and not gen_states:
        verdict = "NEGATIVE: no generation-shaped member at the hyperbolic point of any word state to length 12 or of M1 .. M6"
    elif gen_states:
        verdict = "PROVED: generation-shaped member(s) on " + ", ".join(gen_states)
    else:
        verdict = "WITHHELD: P7 fails; the simple members there are read directly first"
    res = {"predictions": preds, "verdict": verdict, "G vacuous": not gen_states, "generation-shaped states": gen_states,
           "Part A": a_out, "Parts B and C": bc_out}
    (HERE / "read_out.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps({k: v for k, v in res.items() if k not in ("Part A", "Parts B and C")}, indent=1, default=str))
    print(json.dumps(res["Part A"], indent=1, default=str)[:4000])
    print(json.dumps(res["Parts B and C"], indent=1, default=str)[:4000])


if __name__ == "__main__":
    main()
