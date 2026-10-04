#!/usr/bin/env python3
"""B1474 follow-up (post-seal, disclosed; P3 failed informatively): the sign characters of the ORIENTATION-PRESERVING
isometries.  For each amphichiral member find every automorphism sigma of pi_1 with rho o sigma ~ rho in PSL(2,C) by the
same word search (target rho instead of conj rho); its sign character chi_sigma (C rho(g) C^-1 = chi(g) rho(sigma g)).
K = {chi_sigma} is a subgroup of Hom(pi_1, +-1); the mirror's eta is defined modulo K, and the swap is GENUINE iff no
reversing isometry has trivial eta, i.e. eta_0 not in K.  Checks: the set of reversing eta's found in spin_swap.json
is a single coset eta_0 K; the torsion route (B1471: odd-n real <=> eta_0 in K) agrees."""
import json, sys, itertools, pathlib, warnings; warnings.filterwarnings("ignore")
import spin_swap as SS, realness as R
from mpmath import eye, norm, inverse
HERE = pathlib.Path(__file__).resolve().parent


def find_preserving(pk, L=5, max_solutions=60):
    gens, rels, rho = pk["gens"], pk["rels"], pk["rho"]
    target = {g: rho[g] for g in gens}
    ttr = {g: target[g][0, 0] + target[g][1, 1] for g in gens}
    cand = {g: [] for g in gens}; cache = {}
    for w in SS.words(gens, L):
        Mw = R.word_mat(w, rho); cache[w] = Mw; tr = Mw[0, 0] + Mw[1, 1]
        for g in gens:
            if abs(tr - ttr[g]) < SS.TOL or abs(tr + ttr[g]) < SS.TOL: cand[g].append(w)
    g0, g1 = gens[0], gens[1]; rest = gens[2:]
    def apply(sub, word):
        out = ""
        for ch in word:
            w = sub[ch.lower()]; out += w if ch.islower() else w.swapcase()[::-1]
        return out
    chis = set(); n = 0
    for w0 in cand[g0]:
        for w1 in cand[g1]:
            pair = SS.intertwiner_pm([target[g0], target[g1]], [cache[w0], cache[w1]])
            if pair is None: continue
            C, signs = pair; Ci = inverse(C); sub = {g0: w0, g1: w1}; chi = {g0: signs[0], g1: signs[1]}; ok = True
            for g in rest:
                X = C * target[g] * Ci; hit = None
                for w in cand[g]:
                    Y = cache[w]
                    if norm(X - Y) < SS.TOL: hit = (w, 1); break
                    if norm(X + Y) < SS.TOL: hit = (w, -1); break
                if hit is None: ok = False; break
                sub[g] = hit[0]; chi[g] = hit[1]
            if not ok: continue
            if any(min(norm(R.word_mat(apply(sub, rel), rho) - eye(2)), norm(R.word_mat(apply(sub, rel), rho) + eye(2))) > SS.TOL for rel in rels): continue
            chis.add(tuple(chi[g] for g in gens)); n += 1
            if n >= max_solutions: return chis, n
    return chis, n


if __name__ == "__main__":
    sw = json.load(open(HERE / "spin_swap.json")); real = json.load(open(HERE.parent.parent / "B1471_the_cancellation_is_a_theorem_of_amphichirality" / "verification" / "realness.json"))
    odd_real = {r["name"]: all(r["n"][n]["T1_verdict"] == "real-up-to-unit" for n in ("1", "3")) for r in real if "error" not in r}
    out = {}
    for nm, v in sw.items():
        if "error" in v or not v.get("amphichiral_snappy"): continue
        pk, _ = R.setup(nm); gens = pk["gens"]
        K, n = find_preserving(pk, L=5)
        etas = {tuple(e[g] for g in gens) for e in v["etas"]}
        if not etas:                      # no mirror word found for this member (o10_150696): K recorded, no coset
            out[nm] = dict(gens=gens, K=sorted(K), K_size=len(K), preserving_found=n, reversing_etas=[], verdict="UNDETERMINED (no reversing tau found)", torsion_route_odd_real=odd_real.get(nm), agrees_with_torsion=None)
            print(nm, "K", sorted(K), "no reversing tau found -> UNDETERMINED", flush=True)
            json.dump(out, open(HERE / "preserving_characters.json", "w"), indent=1, default=str); continue
        # coset check: eta_0 K == etas (as far as found)
        e0 = next(iter(etas)); coset = {tuple(a * b for a, b in zip(e0, k)) for k in K}
        genuine = all(any(x == -1 for x in e) for e in etas) and (tuple([1] * len(gens)) not in coset)
        row = dict(gens=gens, K=sorted(K), K_size=len(K), preserving_found=n, reversing_etas=sorted(etas), coset_eta0K=sorted(coset),
                   etas_subset_of_coset=etas <= coset, trivial_in_coset=tuple([1] * len(gens)) in coset,
                   verdict="GENUINE SWAP" if not (tuple([1] * len(gens)) in coset) else "FIX-ABLE (eta_0 in K)",
                   torsion_route_odd_real=odd_real.get(nm), agrees_with_torsion=(odd_real.get(nm) == (tuple([1] * len(gens)) in coset)))
        out[nm] = row; print(nm, "K", row["K"], "etas", row["reversing_etas"], "->", row["verdict"], "| torsion odd-real", row["torsion_route_odd_real"], "agree", row["agrees_with_torsion"], flush=True)
        json.dump(out, open(HERE / "preserving_characters.json", "w"), indent=1, default=str)
