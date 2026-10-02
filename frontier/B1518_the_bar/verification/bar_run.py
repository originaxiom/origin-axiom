"""B1518 -- THE BAR, its sealed run: main's class-index census (B1439) read against a null model.

Run only after PREREGISTRATION.md is sealed and pushed. Reads:
  covariates.json            (own code: the 758 word states, 536 manifolds, cheap invariants)
  level_covariates.json      (own code: main's 988 levels, their G and manifold keys)
  main_B1439_firing_own_states.json, main_B1439_levels.json   (main's records, quoted with source and sha)
Writes bar_run.json. Every number is computed here; nothing is typed in.

Hit (main's definition, B1434 PREREGISTRATION :34; B1439 PREREGISTRATION :9-13): a level carries a generation-shaped background when its
five charged sectors have equal non-zero index; a state fires at its own level when its k = 1 level carries one.

    python3 bar_run.py --dry     # the planted controls: synthetic hits from covariates only (no outcome is read)
    python3 bar_run.py --write   # the sealed run (after the seal): writes bar_run.json
"""
import json
import pathlib
import random
import sys
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import null_model as nm  # noqa: E402

B1434_OWN = ["-LLRLR", "-LLLRLR"]           # m369 and s639, main B1434 FINDINGS :34-35 (lengths 5 and 6)
STRATA = {"S1": ["d1", "d2"], "S2": ["d1", "d2", "sign"], "S3": ["d1", "d2", "sign", "symmetry_order"]}
TRIALS = 2                                   # the arc's significance tests: T2 (S1) and T3 (PREREGISTRATION 6.2)
GATE = 0.01                                  # B614 G3: no significance claim unless the trials-corrected p < 0.01
ROOT = "+LR"


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def level_manifolds(level_records, lev_cov):
    """One row per level-manifold (B1517's unit carried to level k). Keys whose duplicates disagree are returned."""
    by_key = defaultdict(list)
    for r in level_records:
        by_key[lev_cov[(r["state"], r["k"])]["manifold_key"]].append(r)
    lm, split = {}, {}
    for key, rs in by_key.items():
        counts = {r["backgrounds"] for r in rs}
        if len(counts) > 1:
            split[key] = sorted(counts)
        r = rs[0]
        lm[key] = {"k": r["k"], "hit": r["backgrounds"] > 0, "backgrounds": r["backgrounds"], "N": r["N"],
                   "records": len(rs)}
    return lm, split


def analyse(cov, own_hits, level_records, lev_cov, n_perm=20000, n_perm_auc=2000):
    """Pure: the readings, the decided checks and the tests, from covariates, an own-level hit set and level records."""
    out = {"readings": {}, "decided": {}, "tests": {}}
    U, split_u = nm.units(cov, own_hits, "manifold")
    W, _ = nm.units(cov, own_hits, "word")
    lm, split_l = level_manifolds(level_records, lev_cov)
    out["split_level_manifolds"] = {k: v for k, v in sorted(split_l.items())[:10]}
    out["split_level_manifolds_k1"] = sorted(k for k in split_l if lm[k]["k"] == 1)
    levels_ok = not split_l
    # ---------------------------------------------------------------- readings
    R = out["readings"]
    R["R1 base rate, word states"] = nm.base_rate(W)
    R["R1 base rate, manifolds"] = nm.base_rate(U)
    R["R1 split own-level manifolds (B1517 C5 found none)"] = split_u
    by_len = defaultdict(lambda: [0, 0])
    for u in U:
        by_len[u["length"]][0] += u["hit"]
        by_len[u["length"]][1] += 1
    R["R2 manifolds by word length (hits, units)"] = {str(k): v for k, v in sorted(by_len.items())}
    tors = sorted(u["torsion"] for u in U if u["hit"])
    R["R2 smallest fibre torsion of a firing manifold"] = tors[0] if tors else None
    R["R2 manifolds with smaller fibre torsion (none fires, by the line above)"] = sum(
        1 for u in U if tors and u["torsion"] < tors[0])
    R["R5 amphichiral manifolds, unconditional (descriptive, not a test: nearly all are reversal-closed, F4)"] = {
        "amphichiral": [sum(u["hit"] for u in U if u["amphichiral"]), sum(1 for u in U if u["amphichiral"])],
        "chiral": [sum(u["hit"] for u in U if not u["amphichiral"]), sum(1 for u in U if not u["amphichiral"])]}
    rate = R["R1 base rate, manifolds"]["rate"]
    n6 = sum(1 for u in U if u["length"] <= 6)
    R["R4 chance that a scan of n manifolds finds at least one carrier, at the census rate"] = {
        f"n = {n6} (B1434's census, lengths 2 to 6)": round(1 - (1 - rate) ** n6, 4),
        f"n = {len(U)} (the census to length 12)": round(1 - (1 - rate) ** len(U), 4)}
    # R6: the bar's comparable-object table for this frame's own level (PREREGISTRATION section 3, step 3)
    tab = defaultdict(lambda: [0, 0])
    for u in U:
        tab[(u["d1"], u["d2"], u["sign"], u["reversal_closed"])][0] += u["hit"]
        tab[(u["d1"], u["d2"], u["sign"], u["reversal_closed"])][1] += 1
    R["R6 the bar's strata (d1, d2, sign, reversal-closed): hits, units"] = [
        [k[0], k[1], k[2], k[3], v[0], v[1]] for k, v in sorted(tab.items())]
    if levels_ok:
        by_k = defaultdict(lambda: [0, 0])
        for v in lm.values():
            by_k[v["k"]][0] += v["hit"]
            by_k[v["k"]][1] += 1
        R["R3 level-manifolds by k (hits, units)"] = {str(k): v for k, v in sorted(by_k.items())}
    else:
        R["R3 level-manifolds by k (hits, units)"] = "withheld: a level-manifold's records disagree (control C2b)"
    # ---------------------------------------------------------------- decided at design time, checked here
    D = out["decided"]
    small = [v for v in lm.values() if v["N"] <= 2]
    D["D1 main's B1442 lemma: level-manifolds of exponent <= 2, and how many carry a background"] = [
        len(small), sum(v["hit"] for v in small)]
    D["D1 holds"] = all(not v["hit"] for v in small)
    root1 = lm.get(f"{ROOT}^1")
    D["D2 the root's own level is silent (main B1434 (a): torsion 1, no character)"] = bool(root1) and not root1["hit"]
    if levels_ok:
        t5 = {}
        for k in range(2, 8):                # k = 2 is reported; the decided check reads k = 3 to 7 (PREREG 6.1)
            root = lm.get(f"{ROOT}^{k}")
            others = [v for key, v in lm.items() if v["k"] == k and key != f"{ROOT}^{k}"]
            t5[str(k)] = {"root_hit": root["hit"] if root else None,
                          "root_backgrounds": root["backgrounds"] if root else None,
                          "others": len(others), "others_hit": sum(v["hit"] for v in others)}
        D["D3 the root's tower against the other level-manifolds at the same k"] = t5
        comparable = [v for k, v in t5.items() if int(k) >= 3 and v["others"] >= 2 and v["root_hit"]]
        D["D3 holds (k = 3 to 7: wherever the root fires and two or more others exist, half or more of them fire)"] = all(
            v["others_hit"] * 2 >= v["others"] for v in comparable)
    else:
        D["D3 the root's tower against the other level-manifolds at the same k"] = "withheld (control C2b)"
    # ---------------------------------------------------------------- tests
    T = out["tests"]
    for name, keys in STRATA.items():
        T[f"T1 determinism under {name}"] = nm.determinism(U, keys)
        T[f"T2 leave-one-out AUC under {name}"] = round(nm.loo_auc(U, keys), 4)
    T["T2 AUC under S1 against its permutation null"] = nm.auc_permutation(U, STRATA["S1"], n_perm=n_perm_auc)
    T["T3 reversal-closed, unconditional (hits, units)"] = {
        "closed": [sum(u["hit"] for u in U if u["reversal_closed"]), sum(1 for u in U if u["reversal_closed"])],
        "paired": [sum(u["hit"] for u in U if not u["reversal_closed"]), sum(1 for u in U if not u["reversal_closed"])]}
    T["T3 reversal-closed given S2: Mantel-Haenszel"] = nm.mantel_haenszel(U, "reversal_closed", STRATA["S2"])
    T["T3 reversal-closed given S2: conditional permutation"] = nm.conditional_permutation(
        U, "reversal_closed", STRATA["S2"], n_perm=n_perm)
    return out


def read(out):
    """The sealed reading rules (PREREGISTRATION section 6.2), applied mechanically."""
    t = out["tests"]
    p = {}
    p["P1 not determined by the fibre torsion with the monodromy's action (some mixed S2 stratum)"] = \
        t["T1 determinism under S2"]["mixed_strata"] > 0
    p["P2 not determined by G, sign and symmetry order (some mixed S3 stratum)"] = \
        t["T1 determinism under S3"]["mixed_strata"] > 0
    p_auc = nm.sidak(t["T2 AUC under S1 against its permutation null"]["p"], TRIALS)
    p["P3 G predicts the hit beyond chance (AUC under S1, Sidak-corrected p < 0.01)"] = p_auc < GATE
    or3 = t["T3 reversal-closed given S2: Mantel-Haenszel"]["odds_ratio"]
    p3 = nm.sidak(t["T3 reversal-closed given S2: conditional permutation"]["p_greater"], TRIALS)
    p["P4 reversal enrichment survives G and sign (MH OR > 1, Sidak-corrected p < 0.01)"] = or3 > 1 and p3 < GATE
    p["corrected p-values (T2, T3)"] = [round(p_auc, 6), round(p3, 6)]
    return p


def run():
    cov = load("covariates.json")["rows"]
    lev_cov = {(r["state"], r["k"]): r for r in load("level_covariates.json")["rows"]}
    main_own = load("main_B1439_firing_own_states.json")
    main_lev = load("main_B1439_levels.json")["records"]
    level_records = [{"state": r["state"], "k": r["k"], "N": r["N"], "torsion": r["torsion"],
                      "backgrounds": r["generation_backgrounds"]} for r in main_lev]
    controls = {}
    # banked identities first: the two main records must agree, the instrument and the covariates must pass
    own_hits_summary = {e[0] for e in main_own["firing_own_states"]} | set(B1434_OWN)
    own_hits = {r["state"] for r in level_records if r["k"] == 1 and r["backgrounds"] > 0}
    controls["C1 main's two records agree on the own-level hits"] = own_hits_summary == own_hits
    controls["C1 hit count (main B1439: 95)"] = len(own_hits)
    controls["C3 instrument planted controls"] = all(nm.selftest().values())
    controls["C4 covariate and level-covariate controls"] = (load("covariates.json")["controls"]["passed"]
                                                           and load("level_covariates.json")["controls"]["passed"])
    controls["C5 planted controls of this script (dry run)"] = dry_run()["passed"]
    lm, split_l = level_manifolds(level_records, lev_cov)
    controls["C2a no own-level manifold is split (B1517 C5 reproduced)"] = not [k for k in split_l if lm[k]["k"] == 1]
    controls["C2b no level-manifold at k >= 2 is split (else R3 and D3 are withheld, nothing else)"] = not [
        k for k in split_l if lm[k]["k"] >= 2]
    stop = [k for k, v in controls.items() if isinstance(v, bool) and not v and not k.startswith("C2b")]
    result = {"controls": controls}
    if stop:
        result["stopped"] = f"control(s) failed: {stop}; no test is computed"
        return result
    out = analyse(cov, own_hits, level_records, lev_cov)
    result.update(out)
    result["predictions"] = read(out)
    return result


def dry_run():
    """Planted controls in both directions, on synthetic hits drawn from covariates only (no outcome field is read)."""
    cov = load("covariates.json")["rows"]
    lev_cov = {(r["state"], r["k"]): r for r in load("level_covariates.json")["rows"]}
    rng = random.Random(2026)
    # synthetic level records: main's non-outcome fields only, a made-up background count (constant on manifolds)
    recs = []
    for r in load("main_B1439_levels.json")["records"]:
        key = lev_cov[(r["state"], r["k"])]["manifold_key"]
        recs.append({"state": r["state"], "k": r["k"], "N": r["N"], "torsion": r["torsion"],
                     "backgrounds": (len(key) % 3) * (r["N"] > 2)})
    by_m = defaultdict(list)
    for r in cov:
        by_m[r["manifold"]].append(r)
    # (a) a hit that is a law of G (exponent divisible by 3): P1 must read NO and the AUC must be significant
    hits_a = {r["state"] for r in cov if r["d2"] % 3 == 0}
    a = analyse(cov, hits_a, recs, lev_cov, n_perm=2000, n_perm_auc=1000)
    pa = read(a)
    # (b) a hit planted on reversal symmetry inside every stratum: P1 YES, P4 YES
    hits_b = set()
    for m, rs in by_m.items():
        if rng.random() < (0.45 if rs[0]["reversal_closed"] else 0.04):
            hits_b |= {r["state"] for r in rs}
    b = analyse(cov, hits_b, recs, lev_cov, n_perm=2000, n_perm_auc=1000)
    pb = read(b)
    # (c) a hit independent of every covariate: P3 NO, P4 NO
    hits_c = set()
    for m, rs in by_m.items():
        if rng.random() < 0.16:
            hits_c |= {r["state"] for r in rs}
    c = analyse(cov, hits_c, recs, lev_cov, n_perm=2000, n_perm_auc=1000)
    pc = read(c)
    k1, k3, k4 = (list(x) for x in (pa, pb, pc))
    checks = {
        "(a) a law of G leaves no mixed S2 stratum": not pa[k1[0]],
        "(a) a law of G is predicted beyond chance": pa[k1[2]],
        "(b) a planted reversal effect is found": pb[k3[3]],
        "(b) its strata are mixed": pb[k3[0]],
        "(c) a covariate-free hit is not predicted by G": not pc[k4[2]],
        "(c) nor enriched on reversal symmetry": not pc[k4[3]],
        "the manifold collapse splits no unit (hits drawn by manifold)": not (a["readings"][
            "R1 split own-level manifolds (B1517 C5 found none)"] or b["readings"][
            "R1 split own-level manifolds (B1517 C5 found none)"]),
        "the synthetic level records collapse cleanly": not a["split_level_manifolds"],
    }
    return {"checks": checks, "passed": all(checks.values()),
            "corrected p (a, b, c)": [pa[k1[4]], pb[k3[4]], pc[k4[4]]]}


if __name__ == "__main__":
    if "--dry" in sys.argv:
        d = dry_run()
        for k, v in d["checks"].items():
            print(f"  [{'PASS' if v else 'FAIL'}] {k}")
        print("corrected p (a, b, c):", d["corrected p (a, b, c)"])
        print("DRY RUN PASSES" if d["passed"] else "DRY RUN FAILS")
        sys.exit(0 if d["passed"] else 1)
    out = run()
    text = json.dumps(out, indent=1, default=str)
    print(text)
    if "--write" in sys.argv:
        (HERE / "bar_run.json").write_text(text + "\n", encoding="utf-8")
