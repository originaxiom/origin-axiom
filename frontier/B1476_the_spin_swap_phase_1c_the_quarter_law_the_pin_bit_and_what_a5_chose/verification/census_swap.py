#!/usr/bin/env python3
"""B1476 C7 (P7/P8): the fix/swap verdict by B1474's matrix route on the amphichiral census manifolds OUTSIDE the 112-family
(cusped, first 3000) and on the closed amphichiral census (37), against their CS class.  Verdict per member:
GENUINE SWAP iff no reversing witness has trivial eta modulo the orientation-preserving character group K (the K cell of
B1474 when the eta-set is not a singleton).  Usage: census_swap.py census_lists.json out.json [cusped|closed|all]"""
import sys, json, pathlib, warnings, contextlib; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = next((p for p in HERE.parents if p.name == "frontier"), pathlib.Path.cwd() / "frontier")
for d in ("B1471_the_cancellation_is_a_theorem_of_amphichirality", "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route"):
    sys.path.insert(0, str(FRONTIER / d / "verification"))
import realness as R, spin_swap as SS, preserving_characters as PC
import itertools, snappy
from mpmath import mpf, eye


def setup_any(name, randomize=0):
    """realness.setup without phi: the holonomy with the SL(2,C) lift repaired, for any H_1 rank (closed manifolds included)"""
    M = snappy.ManifoldHP(name)
    for _ in range(randomize): M.randomize()
    G = M.fundamental_group(); gens, rels = G.generators(), G.relators()
    rho = {g: R.mat2(G.SL2C(g)) for g in gens}
    def relsign(r):
        A = R.word_mat(r, rho)
        p = max(abs(A[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2)); m = max(abs(A[i, j] + (1 if i == j else 0)) for i in range(2) for j in range(2))
        return 0 if p < R.TOL else (1 if m < R.TOL else None)
    want = [relsign(r) for r in rels]
    if any(w is None for w in want): return None, "holonomy fails the relators"
    if any(want):
        E = [[x % 2 for x in R.expvec(r, gens)] for r in rels]; sol = None
        for bits in itertools.product((0, 1), repeat=len(gens)):
            if all(sum(E[i][k] * bits[k] for k in range(len(gens))) % 2 == want[i] for i in range(len(rels))): sol = bits; break
        if sol is None: return None, "the PSL representation does not lift"
        for k, g in enumerate(gens):
            if sol[k]: rho[g] = -rho[g]
    return dict(M=M, G=G, gens=gens, rels=rels, rho=rho, phi=None, phi_per=None, h1=str(M.homology())), None


@contextlib.contextmanager
def matrix_route():
    """spin_swap.classify calls realness.setup, which refuses H_1 of rank != 1; the matrix route needs rho and the relators
    only, so setup_any stands in for the duration of one verdict and realness.setup is restored after.  (R60-7, 2026-10-07:
    until then this was a module-level replacement, R.setup = setup_any at import, which every later importer of realness in
    the same interpreter inherited; the verdicts are unchanged.)"""
    saved = R.setup; R.setup = setup_any
    try: yield
    finally: R.setup = saved


def verdict(nm):
    with matrix_route(): return _verdict(nm)


def _verdict(nm):
    r = SS.classify(nm, Ls=(5, 6, 7))
    if "error" in r:                                   # H_1 rank != 1: realness.setup refuses; the matrix route needs only rho and the relators
        return dict(name=nm, error=r["error"])
    if r["n_solutions"] == 0: return dict(name=nm, verdict="UNDETERMINED (no mirror word to L=%s)" % r["L"], L=r["L"])
    etas = {tuple(e[g] for g in r["gens"]) for e in r["etas"]}
    if all(all(v == 1 for v in e) for e in etas): return dict(name=nm, verdict="FIX", etas=sorted(etas), K=None, n=r["n_solutions"])
    pk, _ = setup_any(nm); K, nK = PC.find_preserving(pk, L=5)
    one = tuple([1] * len(r["gens"])); e0 = next(iter(etas))
    # close K
    Kc = set(K) | {one}
    while True:
        new = {tuple(a * b for a, b in zip(x, y)) for x in Kc for y in Kc} | Kc
        if new == Kc: break
        Kc = new
    coset = {tuple(a * b for a, b in zip(e0, k)) for k in Kc}
    return dict(name=nm, verdict=("GENUINE SWAP" if one not in coset else "FIX-able (eta_0 in K)"), etas=sorted(etas), K=sorted(Kc), n=r["n_solutions"], etas_in_coset=etas <= coset)


if __name__ == "__main__":
    lists = json.load(open(sys.argv[1])); outp = sys.argv[2]; which = sys.argv[3] if len(sys.argv) > 3 else "all"
    todo = []
    if which in ("cusped", "all"): todo += [(r["name"], r["cls"], "cusped") for r in lists["cusped"] if not r["in_family"]]
    if which in ("closed", "all"): todo += [(r["name"], r["cls"], "closed") for r in lists["closed"]]
    out = {}
    for nm, cls, kind in todo:
        v = verdict(nm); v.update(cs_class=cls, kind=kind); out[nm] = v
        print(nm, kind, "CS", cls, "->", v.get("verdict", v.get("error")), flush=True)
        json.dump(out, open(outp, "w"), indent=1, default=str)
    law = [(nm, v["cs_class"], v["verdict"]) for nm, v in out.items() if "verdict" in v and not v["verdict"].startswith("UNDETERMINED")]
    ok = all((c == "quarter") == (vd == "GENUINE SWAP") for nm, c, vd in law)
    print("P7/P8 law swap <=> quarter on", len(law), "decided members:", ok, "| exceptions:", [(nm, c, vd) for nm, c, vd in law if (c == "quarter") != (vd == "GENUINE SWAP")], flush=True)
