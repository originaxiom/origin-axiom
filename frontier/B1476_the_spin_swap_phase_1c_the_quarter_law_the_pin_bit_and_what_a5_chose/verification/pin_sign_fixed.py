#!/usr/bin/env python3
"""B1476 C4, corrected post-seal (disclosed): C conj(C) is a scalar only when tau^2 is the identity; in general tau^2 is inner,
tau^2(g) = w g w^-1, and C conj(C) = eps * rho(w) with eps = +-1 -- the referee's 'W conj(W) = +A' (r14 (4)).  For each
reversing tau of m004 (eta trivial, so the lift is mirror-fixed): the word w (found by matching the intertwiner of rho and
rho o tau^2 against rho(words)), eps for the geometric lift, and eps * chi(w) for the other lift rho (x) chi.  B1382's claim:
the two lifts carry opposite signs (one Pin+, one Pin-)."""
import sys, json, itertools, pathlib, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = next((p for p in HERE.parents if p.name == "frontier"), pathlib.Path.cwd() / "frontier")
for d in ("B1471_the_cancellation_is_a_theorem_of_amphichirality", "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route", "B1475_the_spin_swap_phase_1b_does_the_swap_carry_a_quantity"):
    sys.path.insert(0, str(FRONTIER / d / "verification"))
import realness as R, spin_swap as SS, spin_quantity as SQ
from mpmath import mp, mpf, matrix, eye, inverse, norm, nstr, conj as cj
mp.dps = 50; TOL = mpf(10) ** -20


def conjm(M): return matrix([[cj(M[i, j]) for j in range(2)] for i in range(2)])


def apply(sub, word):
    out = ""
    for ch in word:
        w = sub[ch.lower()]; out += w if ch.islower() else w.swapcase()[::-1]
    return out


def run(nm, taus, L=7):
    pk, _ = R.setup(nm); gens, rho = pk["gens"], pk["rho"]; chars = SQ.characters(pk); rows = []
    words = list(SS.words(gens, L)); cache = {w: R.word_mat(w, rho) for w in words}
    for T in taus:
        tau = T["tau"]
        Xs = [conjm(rho[g]) for g in gens]; Ys = [R.word_mat(tau[g], rho) for g in gens]
        r = SS.intertwiner_pm(Xs, Ys)
        if r is None:
            rows.append(dict(tau=tau, result="no intertwiner")); continue
        C, signs = r
        if any(s != 1 for s in signs):
            rows.append(dict(tau=tau, eta=dict(zip(gens, signs)), result="eta nontrivial: the lift is not mirror-fixed, no Pin type")); continue
        CC = C * conjm(C)
        # tau^2 as words; find w with CC = eps rho(w): match CC against +-rho(w) over words
        tau2 = {g: apply(tau, tau[g]) for g in gens}
        hit = None
        for w, Mw in cache.items():
            if norm(CC - Mw) < TOL: hit = (w, 1); break
            if norm(CC + Mw) < TOL: hit = (w, -1); break
        if hit is None:
            rows.append(dict(tau=tau, tau2=tau2, result="C conj(C) matched no +-rho(w) to length %d" % L, CC00=nstr(CC[0, 0], 10)))
            continue
        w, eps = hit
        # check: tau^2 is conjugation by w on the holonomy
        innerok = all(norm(R.word_mat(tau2[g], rho) - cache[w] * rho[g] * inverse(cache[w])) < TOL for g in gens)
        other = [dict(chi=tuple(c[g] for g in gens), eps_chi=eps * SQ.chi_of_word(c, w)) for c in chars]
        rows.append(dict(tau=tau, tau2=tau2, w=w, eps_geometric=eps, tau2_is_conj_by_w=innerok, lifts=other, pin={str(o["chi"]): ("Pin+" if o["eps_chi"] == 1 else "Pin-") for o in other}))
    return rows


if __name__ == "__main__":
    sw = json.load(open(FRONTIER / "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route" / "verification" / "spin_swap.json"))
    out = {}
    for nm in ("m004", "m206", "t12839"):
        out[nm] = run(nm, sw[nm]["solutions"][:6])
        for r in out[nm]: print(nm, r.get("tau"), "| w =", r.get("w"), "eps =", r.get("eps_geometric"), "| inner ok", r.get("tau2_is_conj_by_w"), "| pins", r.get("pin", r.get("result")), flush=True)
    json.dump(out, open(HERE / "pin_sign_fixed.json", "w"), indent=1, default=str)
