#!/usr/bin/env python3
"""B1603 -- THE COUNT AT EVERY MEMBER: on every forced cover of B1602's census (74 signed threads to length eight) and at
every sign character with an interior class of the four (a member), the extension W1 = [[V, z], [0, 1]] by each interior
class and its reading (I(W1), I(Lambda^2 W1)) with B1492's stacked index; the class's per-cusp pattern (dead on cusp i:
restricting to a coboundary there); the cusps on which the character is trivial (m_A), b0 = [nu^4 = 1] = 1 for a sign
character, k = the cusps on which the class is not dead.  The SM seat's floor -I(W1) <= m_A + b0 - k and its ceiling
I(W1) >= -(2 m_A + m_B - b0) (m_B = cusps - m_A at sign characters) are checked on every reading.

    python3 count_every.py THREAD ...   -> count_<thread>.json beside this file (only threads with members produce rows)
    python3 count_every.py carriers     -> the carrier threads of B1602's census"""
import sys, json, pathlib
import snappy
HERE = pathlib.Path(__file__).resolve().parent
B1602 = HERE.parents[1] / "B1602_the_forced_cover_on_every_thread" / "verification"
sys.path.insert(0, str(B1602))
import forced_every as FE
MC, RM = FE.MC, FE.RM


def carriers():
    rows = [json.loads(l) for l in open(B1602 / "census_8.jsonl") if l.strip()]
    return [r["thread"] for r in rows if r["any_member"]]


def nu_on_word(nu, w):
    v = 1
    for ch in w:
        v *= nu[ch.lower()] if ch.islower() else 1 / nu[ch.lower()]
    return v


def run(name):
    M = snappy.Manifold(name); G, eps, label, group, good, ks = FE.forced(M)
    out = {"thread": name, "deck": label, "covers": []}
    for img in ks:
        perms = [[group.index(FE.mul(group[i], img[g])) for i in range(len(group))] for g in G.generators()]
        N = M.cover(perms); S = FE.site_of(N)
        cov = {"cover_homology": str(N.homology()), "cusps": S.m, "members": []}
        for vals, nu in RM.sign_characters(S):
            V = S.four(nu); c = S.counts(V)
            if c["n"] <= 0:
                continue
            interior, other = S.classes(V)
            m_A = sum(1 for i in range(S.m) if all(abs(nu_on_word(nu, w) - 1) < 1e-20 for w in S.cusps[i]))
            row = {"nu": list(vals), "h1": c["a1"], "r1": c["r1"], "n": c["n"], "t0": c["t0"], "m_A": m_A, "interior": len(interior), "readings": []}
            for z, dead in interior:
                W = S.extension(V, z); I1 = S.index(W); L2 = {g: MC.ext2(W[g]) for g in S.gens}; I2 = S.index(L2)
                k = sum(1 for d in dead if not d); b0 = 1; m_B = S.m - m_A
                row["readings"].append({"dead_on_cusps": dead, "k": k, "I_W1": I1["I"], "I_L2W1": I2["I"],
                                        "floor_holds": -I1["I"] <= m_A + b0 - k, "ceiling_holds": I1["I"] >= -(2 * m_A + m_B - b0),
                                        "generation_shaped": I1["I"] == -1 and I2["I"] == -1 and all(dead)})
            cov["members"].append(row)
        out["covers"].append(cov)
    (HERE / f"count_{name}.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    kinds = sorted({(r["I_W1"], r["I_L2W1"]) for cv in out["covers"] for m in cv["members"] for r in m["readings"]})
    print(json.dumps({"thread": name, "members": sum(len(cv["members"]) for cv in out["covers"]), "readings": sum(len(m["readings"]) for cv in out["covers"] for m in cv["members"]), "kinds": kinds,
                      "generation_shaped": sum(1 for cv in out["covers"] for m in cv["members"] for r in m["readings"] if r["generation_shaped"]),
                      "floor_fails": sum(1 for cv in out["covers"] for m in cv["members"] for r in m["readings"] if not r["floor_holds"]),
                      "ceiling_fails": sum(1 for cv in out["covers"] for m in cv["members"] for r in m["readings"] if not r["ceiling_holds"])}), flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "carriers":
        print(" ".join(carriers()))
    else:
        for n in sys.argv[1:]:
            run(n)
