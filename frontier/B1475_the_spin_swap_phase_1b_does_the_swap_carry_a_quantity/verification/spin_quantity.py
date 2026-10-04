#!/usr/bin/env python3
"""B1475 (THE SPIN SWAP, Phase 1b): every spin structure of a member, the mirror pairing on all of them, the orientation-odd
spin-dependent quantity D_s(t) = Im R_1^{(s)}(t), and the mirror-invariant spin structures.

Spin(M) = {rho (x) chi : chi in Hom(pi_1, +-1)}, s_0 = rho the geometric lift.  From B1474 (spin_swap.json): the reversing
automorphisms tau (as words) with sign characters eta_tau.  For s = rho (x) chi:
    conj(rho (x) chi) ~ (rho (x) eta_tau (x) chi o tau^-1) o tau,  so  conj R^{(chi)}(t) = R^{(eta_tau . chi o tau^-1)}(t)
    (homeomorphism invariance; the mirror partner of chi is  tau.chi := eta_tau . (chi o tau^-1)).
Mirror-invariant spin structures of tau: chi with tau.chi = chi.  Cells C1-C3; C4 (the index) is in spin_index_1b.py."""
import sys, json, itertools, pathlib, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = next((p for p in HERE.parents if p.name == "frontier"), pathlib.Path.cwd() / "frontier")
sys.path.insert(0, str(FRONTIER / "B1471_the_cancellation_is_a_theorem_of_amphichirality" / "verification"))
import realness as R
from mpmath import mp, mpf, nstr, conj as cj, im, re as mre
mp.dps = 50
TOL = mpf(10) ** -20
SWAP = ["m003", "m207", "s955", "s957", "s960", "t12838", "o10_150695"]; FIX = ["m004", "s961", "t12839"]


def characters(pk):
    gens, rels = pk["gens"], pk["rels"]
    out = []
    for signs in itertools.product((1, -1), repeat=len(gens)):
        chi = dict(zip(gens, signs))
        if all(sum(1 for ch in r if chi[ch.lower()] == -1) % 2 == 0 for r in rels): out.append(chi)
    return out


def chi_of_word(chi, w):
    s = 1
    for ch in w: s *= chi[ch.lower()]
    return s


def pull(chi, tau):
    """chi o tau on generators"""
    return {g: chi_of_word(chi, tau[g]) for g in chi}


def mirror_partner(chi, tau, eta, chars):
    """tau.chi = eta . (chi o tau^-1): the chi' with chi' o tau == chi, times eta"""
    key = lambda c: tuple(c[g] for g in sorted(c))
    inv = [c for c in chars if key(pull(c, tau)) == key(chi)]
    assert len(inv) == 1, ("tau* not a permutation on the characters found", len(inv))
    c = inv[0]; return {g: eta[g] * c[g] for g in c}


def run(nm, taus, pts=(mpf(2), mpf(3), mpf("0.6"))):
    pk, err = R.setup(nm)
    if err: return dict(name=nm, error=err)
    chars = characters(pk); key = lambda c: tuple(c[g] for g in pk["gens"])
    out = dict(name=nm, h1=pk["h1"], gens=pk["gens"], n_spin=len(chars), spin=[], pairing=[], invariant=[], checks=dict(symmetry_all_s=0, symmetry_fail=0, D_odd_fail=0))
    Rval = {}
    for chi in chars:
        pk2 = dict(pk); pk2["rho"] = {g: chi[g] * pk["rho"][g] for g in pk["gens"]}
        row = dict(chi=key(chi))
        for n in (1, 3):
            W = R.Wada(pk2, n); vals = {str(t): W.value(t) for t in pts}
            Rval[(key(chi), n)] = vals
            row["R%d" % n] = {k: nstr(v, 15) for k, v in vals.items()}
            row["D%d" % n] = {k: nstr(im(v), 12) for k, v in vals.items()}
        out["spin"].append(row)
    # the mirror pairing for every reversing tau found in B1474 and every spin structure
    for T in taus:
        tau, eta = T["tau"], T["eta"]
        fixed = []
        for chi in chars:
            part = mirror_partner(chi, tau, eta, chars)
            for n in (1, 3):
                a, b = Rval[(key(chi), n)], Rval[(key(part), n)]
                ok = all(abs(cj(a[k]) - b[k]) < TOL * max(1, abs(a[k])) for k in a)
                out["checks"]["symmetry_all_s" if ok else "symmetry_fail"] += 1
            if key(part) == key(chi): fixed.append(key(chi))
            out["pairing"].append(dict(tau=tau, chi=key(chi), partner=key(part), D1_chi=nstr(im(Rval[(key(chi), 1)]["2.0"]), 10), D1_partner=nstr(im(Rval[(key(part), 1)]["2.0"]), 10)))
            if abs(im(Rval[(key(chi), 1)]["2.0"]) + im(Rval[(key(part), 1)]["2.0"])) > TOL * 10: out["checks"]["D_odd_fail"] += 1
        out["invariant"].append(dict(tau=tau, eta=eta, mirror_invariant_spin_structures=fixed, count=len(fixed)))
    allfixed = set()
    for r in out["invariant"]: allfixed |= set(map(tuple, r["mirror_invariant_spin_structures"]))
    out["mirror_invariant_any_tau"] = sorted(allfixed); out["has_mirror_invariant_spin_structure"] = bool(allfixed)
    out["D_s0_at_2"] = nstr(im(Rval[(key(dict((g, 1) for g in pk["gens"])), 1)]["2.0"]), 12)
    return out


if __name__ == "__main__":
    sw = json.load(open(FRONTIER / "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route" / "verification" / "spin_swap.json"))
    retri = FRONTIER / "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route" / "verification" / "o10_150696_retri.json"
    names = sys.argv[1:] or SWAP + FIX
    res = {}
    for nm in names:
        taus = sw[nm]["solutions"] if nm in sw and sw[nm].get("solutions") else []
        # distinct tau's by their eta and word tuple (the stored first six)
        seen, T = set(), []
        for s in taus:
            k = (tuple(sorted(s["eta"].items())), tuple(sorted(s["tau"].items())))
            if k not in seen: seen.add(k); T.append(s)
        r = run(nm, T); res[nm] = r
        if "error" in r: print(nm, "ERR", r["error"]); continue
        print(nm, r["h1"], "spin structures", r["n_spin"], "| D_s0(2) =", r["D_s0_at_2"], "| symmetry on all s:", r["checks"], "| mirror-invariant:", r["mirror_invariant_any_tau"] or "NONE", flush=True)
        json.dump(res, open(HERE / "spin_quantity.json", "w"), indent=1, default=str)
