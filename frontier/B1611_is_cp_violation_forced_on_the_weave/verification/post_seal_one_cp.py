#!/usr/bin/env python3
"""B1611 -- POST-SEAL (disclosed): the sealed C5 asked, sector by sector, whether some CP candidate is consistent on T and
on that sector.  A theory containing every sector needs ONE automorphism consistent on all of them at once; and the
reading names the swap's conjugation as the weave's CP.  Computed here with the sealed instrument's own functions: the
automorphisms consistent (twisted Frobenius-Schur indicator +-1, conjugate character) on T and on every irreducible of
T (x) T and T (x) T-bar simultaneously; the swap's conjugation's indicator on each; whether the consistent ones are
involutions up to inner automorphisms.  Writes post_seal_one_cp.json."""
import json, pathlib, importlib.util
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cp", HERE / "cp_on_the_weave.py"); cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
G = cp.Group([cp.W.ML, cp.W.MR]); TB = cp.TB; R = lambda M: cp.restrict(M, TB)
chis = {"T": [complex(np.trace(R(M))) for M in G.els]}
for label, mk in (("T(x)T", lambda M: np.kron(R(M), R(M))), ("T(x)Tbar", lambda M: np.kron(R(M), R(M).conj()))):
    mats = [mk(M) for M in G.els]; pieces, _ = cp.decompose(mats, 9)
    for n, P in enumerate(pieces):
        Q, _ = np.linalg.qr(P); chis[f"{label}[{n}] dim {P.shape[1]}"] = [complex(np.trace(Q.conj().T @ A @ Q)) for A in mats]
auts = G.automorphisms()
inner = {tuple(G.inner(h)) for h in range(G.n)}
def fs(chi, u): return complex(sum(chi[G.mult[g][u[g]]] for g in range(G.n)) / G.n)
def conj_ok(chi, u): return all(abs(chi[u[g]] - np.conj(chi[g])) < 1e-6 for g in range(G.n))
def consistent(u): return all(conj_ok(c, u) and abs(abs(fs(c, u)) - 1) < 1e-6 for c in chis.values())
good = [u for u in auts if consistent(u)]
def compose(u, v): return [u[v[g]] for g in range(G.n)]
swap = [G.idx[cp.key(cp.W.MP @ M @ np.linalg.inv(cp.W.MP))] for M in G.els]
out = {"irreducibles_checked": list(chis.keys()), "automorphisms": len(auts),
       "one_cp_consistent_on_every_sector": len(good),
       "those_are_involutions_up_to_inner": all(tuple(compose(u, u)) in inner for u in good),
       "swap_conjugation": {k: [round(fs(c, swap).real, 6), round(fs(c, swap).imag, 6)] for k, c in chis.items()},
       "swap_conjugation_consistent_on_every_sector": consistent(swap),
       "indicator_signs_of_the_consistent_cps_on_T": sorted({round(fs(chis["T"], u).real, 6) for u in good})}
json.dump(out, open(HERE / "post_seal_one_cp.json", "w"), indent=1); print(json.dumps(out, indent=1))
